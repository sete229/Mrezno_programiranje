import socket
from local_machine_info import print_machine_info

print_machine_info()

HOST = "0.0.0.0"
PORT = 65433

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"[UDP SERVER] Listening on {HOST}:{PORT}")

while True:
    data, client_address = server.recvfrom(1024)
    message = data.decode()

    print(f"[UDP SERVER] Received from {client_address}: {message}")

    response = "Poruka primljena"
    server.sendto(response.encode(), client_address)