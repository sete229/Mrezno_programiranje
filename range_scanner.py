import socket

socket.setdefaulttimeout(0.5)

host = input("Unesi host: ")

start_port = int(input("Početni port: "))
end_port = int(input("Završni port: "))

if start_port < 1 or end_port > 65535 or start_port > end_port:
    print("Neispravan raspon portova.")
    exit()

print(f"\nOtvoreni portovi na {host}:\n")

for port in range(start_port, end_port + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((host, port))

    if result == 0:

        try:
            service = socket.getservbyport(port)
        except:
            service = "Nepoznat servis"

        print(f"- {port} ({service})")

    sock.close()