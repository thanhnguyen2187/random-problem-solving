open Eio.Std

type message =
    | Ack of { sequence_number: int }
    | Data of { sequence_number: int; data: string }

type sender = {
    (* mutable current_seq_num: int; *)
    current_seq_num: int Atomic.t;
    bound_seq_num: int;
    mailbox: message Eio.Stream.t;
}

type receiver = {
    mailbox: message Eio.Stream.t;
}

let main _env =
    let sender : sender = {
        current_seq_num = Atomic.make 0;
        bound_seq_num = 10;
        mailbox = (Eio.Stream.create 1);
    } in
    let receiver : receiver = {
        mailbox = (Eio.Stream.create 1);
    } in
    let create_mailbox_handler mailbox handle =
        fun () ->
            while true do
                let msg : message = Eio.Stream.take mailbox in handle msg;
            done
    in
    let () = Random.self_init () in
    let send_with_loss mailbox msg =
        let random_number = Random.int 100 in
        if random_number >= 80 then
            Eio.Stream.add mailbox msg;
    in
    Fiber.all [
        create_mailbox_handler
            receiver.mailbox
            (function
                | Ack {sequence_number = i} ->
                    begin
                        traceln "Receiver received ACK %d" i;
                    end
                | Data {sequence_number = i; data = data} ->
                    begin
                        traceln "Receiver received message no %d: %s" i data;
                        send_with_loss sender.mailbox (Ack {sequence_number = i});
                        (* traceln "Receiver sent ACK %d" i; *)
                    end;
            );
        create_mailbox_handler
            sender.mailbox
            (function
                | Ack {sequence_number = i} ->
                    begin
                        traceln "Sender received ACK %d" i;
                        Atomic.incr sender.current_seq_num;
                    end
                | Data {sequence_number = i; data = data} ->
                    begin
                        traceln "Sender received message no %i: %s" i data;
                    end;
            );
        (fun () ->
            while Atomic.get sender.current_seq_num < sender.bound_seq_num do
                (* traceln "Sender sent message no %i" (Atomic.get sender.current_seq_num); *)
                send_with_loss
                    receiver.mailbox
                    (Data {
                        sequence_number = (Atomic.get sender.current_seq_num);
                        data = string_of_int (Atomic.get sender.current_seq_num);
                    });
                Fiber.yield ();
            done);
    ]

