import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))  # Connect to server

    while True:
        msg = input("You: ")
        if msg.lower() == "quit":
            break
        client.sendall(msg.encode("utf-8"))

        reply = client.recv(1024).decode("utf-8")
        print("Server:", reply)

    client.close()

if __name__ == "__main__":
    start_client()

