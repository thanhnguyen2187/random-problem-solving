open Eio.Std

type process_state =
    | Follower
    | Candidate
    | Leader
[@@deriving show]

type message_content =
    | Heartbeat
    | Timeout
    | VoteRequest
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

    val voted_for : int Atomic.t
    val clock : Eio.Time.clock

    val last_heartbeat : float Atomic.t
    val timeout_s : float
end

let create_process
    (index : int)
    (max_index : int)
    (outbox: message Eio.Stream.t)
    (clock : Eio.Time.clock)
    (* (vote_counter : (int * int, int) Hashtbl.t) *)
    (timeout_s : float)
    : (module Process_type) =
    let () = traceln "Created process %d with timeout %f" index timeout_s in
    (module struct
        let index = index
        let max_index = max_index
        let state = Atomic.make Follower
        let inbox = Eio.Stream.create 3
        let outbox = outbox
        let term = Atomic.make 0

        let voted_for = Atomic.make (-1)
        let clock = clock

        let last_heartbeat = Atomic.make (Unix.gettimeofday ())
        let timeout_s = timeout_s
    end)

let create_message
    (proc : (module Process_type))
    (to_index : int)
    (msg_content : message_content)
    : message =
    let module Proc = (val proc) in
    {
        from_index = Proc.index;
        to_index;
        term = Atomic.get Proc.term;
        content = msg_content;
    }

let create_heartbeat_monitor (proc: (module Process_type)) : unit -> unit =
    fun () ->
        let module Proc = (val proc) in
        let () = traceln "Created heartbeat monitor for process %d" Proc.index in
        while true do
            let current_time = Unix.gettimeofday () in
            let gap = current_time -. Atomic.get Proc.last_heartbeat in
            if (Atomic.get Proc.state != Leader) && (gap >= Proc.timeout_s)
            then
                (let msg = create_message proc Proc.index Timeout in
                Eio.Stream.add Proc.inbox msg);
            Eio.Time.sleep Proc.clock 1.0;
        done

let print_state (proc : (module Process_type)) : unit =
    let module Proc = (val proc) in
    traceln "Term %d; Process %d; State %s; Voted for process %d"
        (Atomic.get Proc.term)
        Proc.index
        (show_process_state (Atomic.get Proc.state))
        (Atomic.get Proc.voted_for)

let create_state_printer (proc : (module Process_type)) : unit -> unit =
    fun () ->
        let module Proc = (val proc) in
        let () = traceln "Created state printer for process %d" Proc.index in
        while true do
            print_state proc;
            Eio.Time.sleep Proc.clock 3.0
        done

let print_message (msg : message) : unit =
    traceln "Term %d; From process %d; To process %d; Message %s"
        msg.term
        msg.from_index
        msg.to_index
        (show_message_content msg.content)

let send_to_all (proc: (module Process_type)) (msg_content : message_content) : unit =
    let module Proc = (val proc) in
    for i = 0 to Proc.max_index do
        if i != Proc.index then
            let msg = create_message proc i msg_content in
            Eio.Stream.add Proc.outbox msg;
    done

let create_state_handler (proc: (module Process_type)) : unit -> unit =
    fun () ->
        let module Proc = (val proc) in
        let () = traceln "Created state handler for process %d" Proc.index in
        while true do
            match Atomic.get Proc.state with
            (* TODO: investigate why putting Eio.Time.sleep at the end doesn't
                     work *)
            (* | Follower -> () *)
            | Candidate ->
                send_to_all proc VoteRequest;
                Eio.Time.sleep Proc.clock 2.0;
            | Leader ->
                send_to_all proc Heartbeat;
                Eio.Time.sleep Proc.clock 2.0;
            | _ -> Eio.Time.sleep Proc.clock 2.0;

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
            match msg.content, Atomic.get Proc.state with
            | Heartbeat, Follower ->
                if (msg.term >= Atomic.get Proc.term)
                then
                    Atomic.set Proc.term msg.term;
                    Atomic.set Proc.last_heartbeat (Unix.gettimeofday ());
            | Heartbeat, Candidate ->
                Atomic.set Proc.state Follower;
                Atomic.set Proc.last_heartbeat (Unix.gettimeofday ());
                Atomic.set Proc.voted_for (-1);

            | Timeout, Follower ->
                if Atomic.get Proc.voted_for = (-1)
                then begin
                    Atomic.set Proc.state Candidate;
                    Atomic.set Proc.voted_for Proc.index;
                    Atomic.incr Proc.term;
                    send_to_all proc VoteRequest;
                end
            | Timeout, Candidate ->
                Atomic.incr Proc.term;

            | Promotion, Follower
            | Promotion, Candidate ->
                Atomic.set Proc.voted_for (-1);
                Atomic.set Proc.state Leader;

            | VoteRequest, Follower
            | VoteRequest, Candidate ->
                if Atomic.get Proc.voted_for = (-1)
                && Atomic.get Proc.term < msg.term
                then Atomic.set Proc.voted_for msg.from_index;

            | _ -> let _ = failwith "unreachable code" in ();

            Eio.Time.sleep Proc.clock 1.0
        done

let main _env =
    let clock = Eio.Stdenv.clock _env in
    let outbox = (Eio.Stream.create 5) in
    let processes = List.init
        5
        (fun i -> create_process
            i 4
            outbox
            clock
            (4.0 +. (Random.float 2.0))
            )
    in ();

    (* let module Proc = (val (List.nth processes 3)) in *)
    (* Eio.Stream.add Proc.inbox { *)
    (*     term = 0; *)
    (*     from_index = -1; *)
    (*     to_index = 3; *)
    (*     content = Promotion; *)
    (* }; *)

    Eio.Fiber.all [
        (create_outbox_orchestrator outbox processes);
        (fun () -> Eio.Fiber.all (List.map create_heartbeat_monitor processes));
        (fun () -> Eio.Fiber.all (List.map create_message_handler processes));
        (fun () -> Eio.Fiber.all (List.map create_state_handler processes));
        (fun () -> Eio.Fiber.all (List.map create_state_printer processes));
    ];
