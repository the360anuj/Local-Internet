import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print("\n" + message)
        except:
            print("[DISCONNECTED FROM SERVER]")
            break

def send_messages():
    while True:
        try:
            msg = input()
            client.send(msg.encode())
        except:
            break

# Start threads
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()