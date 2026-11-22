# TCP client for the multi-client server
import socket, sys

HOST, PORT = "127.0.0.1", 7000
name = sys.argv[1] if len(sys.argv) > 1 else "Client"
text = sys.argv[2] if len(sys.argv) > 2 else "hello network"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST, PORT))
    c.sendall(name.encode())
    print(f"[{name}] {c.recv(1024).decode()}")
    c.sendall(text.encode())
    print(f"[{name}] Reply: {c.recv(1024).decode()}")
