import socket
import threading

HOST = 'localhost'
PORT = 65433

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

name = input("Unesite korisničko ime: ")

sock.sendall(name.encode())

print("Chat započet. Koristite Ctrl+C za izlaz.")

def receive_messages():

    while True:

        try:

            data = sock.recv(1024)

            if data:
                print("\n" + data.decode())

        except:
            break

thread = threading.Thread(target=receive_messages)

thread.daemon = True

thread.start()

while True:

    msg = input("> ")

    sock.sendall(msg.encode())