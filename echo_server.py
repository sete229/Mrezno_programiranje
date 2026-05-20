import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()
print(datetime.datetime.now())

HOST = "0.0.0.0"
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[ECHO SERVER] Listening on {HOST}:{PORT}")

while True:
    conn, client_address = server.accept()

    with conn:
        print(f"[ECHO SERVER] Connected by {client_address}")

        while True:
            data = conn.recv(1024)

            if not data:
                break

            message = data.decode()
            vrijeme = datetime.datetime.now()

            print(f"Vrijeme primitka: {vrijeme}")
            print(f"Sadržaj poruke: {message}")
            print(f"IP adresa klijenta: {client_address[0]}")

            if message == "Nikola_Marinovic":
                response = "Unos nije podržan."
            else:
                response = message

            conn.sendall(response.encode())