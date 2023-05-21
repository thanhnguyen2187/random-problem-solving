open Eio.Std

type process_state =
    | Follower
    | Candidate
    | Leader
[@@deriving show]

type message_content =
    | Heartbeat
    | Timeout
    | Promotion
[@@deriving show]

type message = {
    term: int;
    from_index: int;
    to_index: int;
    content: message_content;
}

module type Process_type = sig
    val index : int
    val max_index : int
    val state : process_state Atomic.t
    val inbox : message Eio.Stream.t
    val outbox : message Eio.Stream.t
    val term : int Atomic.t

    val vote_counter : (int * int, int) Hashtbl.t
    val clock : Eio.Time.clock

    val last_heartbeat : float Atomic.t
    val timeout_s : float
end

let create_process
    (index : int)
    (max_index : int)
    (outbox: message Eio.Stream.t)
    (clock : Eio.Time.clock)
    (vote_counter : (int * int, int) Hashtbl.t)
    (timeout_s : float)
    : (module Process_type) =
    (module struct
        let index = index
        let max_index = max_index
        let state = Atomic.make Follower
        let inbox = Eio.Stream.create 3
        let outbox = outbox
        let term = Atomic.make 0

        let vote_counter = vote_counter
        let clock = clock

        let last_heartbeat = Atomic.make (Unix.gettimeofday ())
        let timeout_s = timeout_s
    end)

let create_heartbeat_monitor (proc: (module Process_type)) : unit -> unit =
    fun () ->
        let module Proc = (val proc) in
        let () = traceln "Created heartbeat monitor for process %d" Proc.index in
        while true do
            let current_time = Unix.gettimeofday () in
            let gap = current_time -. Atomic.get Proc.last_heartbeat in
            if (Atomic.get Proc.state != Leader) && (gap >= Proc.timeout_s)
            then
                Eio.Stream.add Proc.inbox
                {
                    from_index = Proc.index;
                    to_index = Proc.index;
                    content = Timeout;
                    term = Atomic.get Proc.term;
                };
            Eio.Time.sleep Proc.clock 1.0;
        done

let print_state (proc : (module Process_type)) : unit =
    let module Proc = (val proc) in
    traceln "Process %d is in state %s" Proc.index (show_process_state (Atomic.get Proc.state))

let create_state_printer (proc : (module Process_type)) : unit -> unit =
    fun () ->
        let module Proc = (val proc) in
        let () = traceln "Created state printer for process %d" Proc.index in
        while true do
            print_state proc;
            Eio.Time.sleep Proc.clock 3.0
        done

let print_message (msg : message) : unit =
    traceln "Process %d received message %s from process %d" msg.to_index (show_message_content msg.content) msg.from_index

let create_state_handler (proc: (module Process_type)) : unit -> unit =
    fun () ->
        let module Proc = (val proc) in
        let () = traceln "Created state handler for process %d" Proc.index in
        while true do
            match Atomic.get Proc.state with
            (* TODO: investigate why putting Eio.Time.sleep at the end doesn't
                     work *)
            (* | Follower -> () *)
            (* | Candidate -> () *)
            | Leader ->
                for i = 0 to Proc.max_index do
                    Eio.Stream.add Proc.outbox {
                        from_index = Proc.index;
                        to_index = i;
                        term = Atomic.get Proc.term;
                        content = Heartbeat;
                    }
                done;
                Eio.Time.sleep Proc.clock 3.0;
            | _ -> Eio.Time.sleep Proc.clock 3.0;

            (* Eio.Time.sleep Proc.clock 3.0; *)
        done

let create_outbox_orchestrator (outbox: message Eio.Stream.t) (procs: ((module Process_type) list)) : unit -> unit =
    fun () ->
        let () = traceln "Created outbox orchestrator" in
        while true do
            let msg = Eio.Stream.take outbox in
            let module Dest_proc = (val (List.nth procs msg.to_index)) in
            Eio.Stream.add Dest_proc.inbox msg;
            Eio.Fiber.yield ();
        done

let create_message_handler (proc: (module Process_type)) : unit -> unit =
    fun () ->
        let module Proc = (val proc) in
        let () = traceln "Created message handler for process %d" Proc.index in
        while true do
            let msg = Eio.Stream.take Proc.inbox in
            let () = print_message msg in
            match Atomic.get Proc.state, msg.content with
            | Follower, Timeout ->
                Atomic.set Proc.state Candidate;
                Atomic.set Proc.last_heartbeat (Unix.gettimeofday ());
            | Follower, Heartbeat ->
                Atomic.set Proc.last_heartbeat (Unix.gettimeofday ());
            | Follower, Promotion ->
                Atomic.set Proc.state Leader;
            | _ -> ();
            Eio.Time.sleep Proc.clock 1.0
        done

let main _env =
    let clock = Eio.Stdenv.clock _env in
    let vote_counter = Hashtbl.create 20 in
    let outbox = (Eio.Stream.create 3) in
    let processes = List.init
        5
        (fun i -> create_process
            i 4
            outbox
            clock
            vote_counter
            4.0)
    in ();

    let module Proc = (val (List.nth processes 3)) in
    Eio.Stream.add Proc.inbox {
        term = 0;
        from_index = -1;
        to_index = 3;
        content = Promotion;
    };

    Eio.Fiber.all [
        (create_outbox_orchestrator outbox processes);
        (fun () -> Eio.Fiber.all (List.map create_heartbeat_monitor processes));
        (fun () -> Eio.Fiber.all (List.map create_state_printer processes));
        (fun () -> Eio.Fiber.all (List.map create_message_handler processes));
        (fun () -> Eio.Fiber.all (List.map create_state_handler processes));
    ];
