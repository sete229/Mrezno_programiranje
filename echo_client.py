import socket
from local_machine_info import print_machine_info

print_machine_info()

HOST = "localhost"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    print("[ECHO CLIENT] Connected to server.")

    while True:
        message = input("Unesi poruku ili 'exit': ")

        if message.lower() == "exit":
            break

        client.sendall(message.encode())

        data = client.recv(1024)

        print(f"[ECHO CLIENT] Received: {data.decode()}")