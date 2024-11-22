import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

# Server details
HOST = '127.0.0.1'
PORT = 12345


class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Application")

        # Initialize socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))

        # Ask for username
        self.username = simpledialog.askstring("Username", "Enter your username:", parent=self.master)
        if self.username:
            self.client_socket.send(self.username.encode('utf-8'))

        # GUI layout
        self.chat_window = scrolledtext.ScrolledText(master, wrap=tk.WORD, state='disabled')
        self.chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.message_entry = tk.Entry(master, font=('Arial', 14))
        self.message_entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Start thread to receive messages
        threading.Thread(target=self.receive_messages, daemon=True).start()



if __name__ == "__main__":
    main()
