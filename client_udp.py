import socket
from local_machine_info import print_machine_info

print_machine_info()

HOST = "127.0.0.1"
PORT = 65433

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Unesi poruku: ")

client.sendto(message.encode(), (HOST, PORT))

data, server_address = client.recvfrom(1024)

print(f"[UDP CLIENT] Received: {data.decode()}")

client.close()