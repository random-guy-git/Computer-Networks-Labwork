# UDP (connectionless) client
import socket

HOST, PORT = "127.0.0.1", 6000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as c:
    c.sendto(b"Hello UDP Server", (HOST, PORT))
    print("[UDP Client] Datagram sent")
    reply, _ = c.recvfrom(1024)
    print(f"[UDP Client] Server replied: {reply.decode()}")
