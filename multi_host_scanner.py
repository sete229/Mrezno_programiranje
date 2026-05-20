import socket

socket.setdefaulttimeout(0.5)

hosts = [
    "127.0.0.1",
    "scanme.nmap.org",
    "portquiz.net"
]

ports = [22, 80, 443, 8080]

for host in hosts:

    print(f"\nHost: {host}")

    for port in ports:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} OPEN")
        else:
            print(f"Port {port} CLOSED")

        sock.close()