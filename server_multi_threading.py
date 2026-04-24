import socket
import threading

def handle_client(conn, addr):
    print(f"Connected to {addr}")
    
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"{addr}: {msg}")
            conn.send("Received".encode())
        except:
            conn.close()
            break
    
    conn.close()
    print(f"{addr} disconnected")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen()

print("Server running...")

while True:
    conn, addr = server.accept()
    
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()