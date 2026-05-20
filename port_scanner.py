import socket

socket.setdefaulttimeout(0.5)

host = input("Unesi host: ")
port = int(input("Unesi port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = sock.connect_ex((host, port))

if result == 0:
    print(f"Port {port} je otvoren na hostu {host}")
else:
    print(f"Port {port} je zatvoren ili nedostupan na hostu {host}")

sock.close()