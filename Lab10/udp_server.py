# UDP (connectionless) server
import socket

HOST, PORT = "127.0.0.1", 6000
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"[UDP Server] Waiting for datagram on {HOST}:{PORT}")
    data, addr = s.recvfrom(1024)    # no connection, no handshake
    print(f"[UDP Server] Received '{data.decode()}' from {addr}")
    s.sendto(("ACK: " + data.decode()).encode(), addr)
