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
    def receive_messages(self):
        """Receive messages from the server and display them in the chat window."""
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.display_message(message)
            except:
                self.display_message("Connection to the server was lost.")
                break

    def send_message(self, event=None):
        """Send a message to the server."""
        message = self.message_entry.get()
        if message.strip():
            # Display the message in the chat window with "You:"
            self.display_message(f"You: {message}")
            # Send the message to the server
            self.client_socket.send(message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)

    def display_message(self, message):
        """Display a received or sent message in the chat window."""
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, message + "\n")
        self.chat_window.config(state='disabled')
        self.chat_window.yview(tk.END)
        
def main():
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()

if __name__ == "__main__":
    main()
