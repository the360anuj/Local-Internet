import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5000))
server.listen()

print("Server is listening..")
conn, addr = server.accept()
print(f"connected to addr {addr}")

while True:
    msg = conn.recv(1024).decode()
    if not msg:
        break
    print("Client:", msg)
    conn.send("Message received".encode())

conn.close()

