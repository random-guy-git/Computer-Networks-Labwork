# TCP (connection-oriented) client
import socket

HOST, PORT = "127.0.0.1", 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((HOST, PORT))          # three-way handshake
    print(f"[TCP Client] Connected to {HOST}:{PORT}")
    c.sendall(b"Hello TCP Server")
    reply = c.recv(1024)
    print(f"[TCP Client] Server replied: {reply.decode()}")
