import socket
import threading
import tkinter as tk
from subprocess import Popen

# Server details
HOST = '127.0.0.1'
PORT = 12345
clients = {}
server_socket = None
server_running = False





def start_server(add_client_button, start_button, stop_button):
    """Start the chat server."""
    global server_socket, server_running
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")
    server_running = True

    # Enable/Disable buttons
    add_client_button.config(state=tk.NORMAL)
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

    # Accept clients in a separate thread
    threading.Thread(target=accept_clients, args=(server_socket,), daemon=True).start()


def stop_server(add_client_button, start_button, stop_button):
    """Stop the chat server."""
    global server_socket, server_running
    if server_running:
        server_running = False
        server_socket.close()
        print("Server stopped.")

        # Enable/Disable buttons
        add_client_button.config(state=tk.DISABLED)
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    server_gui()
