# TCP (connection-oriented) server
import socket

HOST, PORT = "127.0.0.1", 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[TCP Server] Listening on {HOST}:{PORT}")
    conn, addr = s.accept()          # three-way handshake completes here
    with conn:
        print(f"[TCP Server] Connected by {addr}")
        data = conn.recv(1024)
        print(f"[TCP Server] Received: {data.decode()}")
        conn.sendall(("ACK: " + data.decode()).encode())
    print("[TCP Server] Connection closed")
