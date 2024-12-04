import socket
import threading

# Server configuration
HOST = '192.168.143.108'  # Localhost
PORT = 12345        # Port to bind the server

# List to hold connected clients
clients = []

def broadcast(message, current_client):
    """Send message to all clients except the sender."""
    for client in clients:
        if client != current_client:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client):
    """Handle communication with a single client."""
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def start_server():
    """Start the server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server started on {HOST}:{PORT}")

    while True:
        client, address = server.accept()
        print(f"New connection from {address}")
        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    start_server()
