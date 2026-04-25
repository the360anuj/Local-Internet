import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = []
lock = threading.Lock()

def broadcast(message, sender_conn):
    with lock:
        for client in clients[:]: 
            if client != sender_conn:
                try:
                    client.send(message)
                except:
                    clients.remove(client)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    with lock:
        clients.append(conn)

    try:
        while True:
            msg = conn.recv(1024)
            if not msg:
                break

            print(f"{addr}: {msg.decode()}")
            broadcast(msg, conn)

    except Exception as e:
        print(f"[ERROR] {addr}: {e}")

    finally:
        with lock:
            if conn in clients:
                clients.remove(conn)
        conn.close()
        print(f"[DISCONNECTED] {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[STARTED] Server running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()