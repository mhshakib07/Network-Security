import socket
import threading

# Function to handle each client
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf-8")
            if not msg:
                break
            print(f"[{addr}] {msg}")

            # Send a reply back
            reply = f"Server received: {msg}"
            client_socket.sendall(reply.encode("utf-8"))
        except:
            break
    print(f"[DISCONNECTED] {addr}")
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 12345))   # Bind to all interfaces, port 12345
    server.listen(5)
    print("[LISTENING] Server is listening on port 12345...")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
