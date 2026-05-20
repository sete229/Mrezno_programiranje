import selectors
import socket
import time

sel = selectors.DefaultSelector()

clients = {}

HOST = 'localhost'
PORT = 65433

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

lsock.bind((HOST, PORT))

lsock.listen()

lsock.setblocking(False)

sel.register(lsock, selectors.EVENT_READ)

print(f"[CHAT SERVER] Listening on {HOST}:{PORT}")

last_print = time.time()

while True:

    events = sel.select(timeout=1)

    if time.time() - last_print >= 10:
        print(f"[INFO] Aktivnih korisnika: {len(clients)}")
        last_print = time.time()

    for key, _ in events:

        if key.fileobj == lsock:

            conn, addr = lsock.accept()

            conn.setblocking(False)

            sel.register(conn, selectors.EVENT_READ)

            clients[conn] = {
                "addr": addr,
                "name": None
            }

        else:

            conn = key.fileobj

            data = conn.recv(1024)

            if data:

                if clients[conn]["name"] is None:

                    clients[conn]["name"] = data.decode().strip()

                    print(f"[LOGIN] {clients[conn]['name']} from {clients[conn]['addr']}")

                    with open("chat_log.txt", "a") as log:
                        log.write(f"{clients[conn]['name']} joined chat\n")

                else:

                    text = data.decode().strip()

                    if text == "/users":

                        users = []

                        for c in clients.values():

                            if c["name"] is not None:
                                users.append(c["name"])

                        response = "Online: " + ", ".join(users)

                        conn.sendall(response.encode())

                    else:

                        msg = f"{clients[conn]['name']}: {text}"

                        print(msg)

                        with open("chat_log.txt", "a") as log:
                            log.write(msg + "\n")

                        for c in clients:

                            if c != conn:
                                c.sendall(msg.encode())

            else:

                print(f"[LOGOUT] {clients[conn]['name']}")

                with open("chat_log.txt", "a") as log:
                    log.write(f"{clients[conn]['name']} left chat\n")

                sel.unregister(conn)

                conn.close()

                del clients[conn]