# Multi-client TCP server: one thread per client (client-server model)
import socket, threading

HOST, PORT = "127.0.0.1", 7000

def handle(conn, addr):
    with conn:
        name = conn.recv(1024).decode()
        print(f"[Server] {name} connected from port {addr[1]}")
        conn.sendall(f"Welcome {name}! Send text, I will return it in UPPERCASE.".encode())
        msg = conn.recv(1024).decode()
        print(f"[Server] {name} says: {msg}")
        conn.sendall(msg.upper().encode())
    print(f"[Server] {name} disconnected")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"[Server] Listening on {HOST}:{PORT}")
    for _ in range(3):                      # serve three clients, then stop
        conn, addr = s.accept()
        threading.Thread(target=handle, args=(conn, addr)).start()
