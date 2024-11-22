# **Akshit_Chat_Tkinter_Socket**
Chat application Assignment with GUI

This is a simple Python-based chat application with a server-client architecture. The server manages connections and broadcasts messages to all clients. The client has a graphical user interface (GUI) for sending and receiving messages.

---

### **1. Project Structure**

. ├── client_gui.py # Client-side GUI for chatting ├── server_with_launcher.py # Server-side GUI with client launcher └── README.md # Project documentation

yaml
Copy code

---

### **2. Prerequisites**

Before running the application, ensure you have the following:

1. **Python 3.6** or higher
2. Install **tkinter** (usually pre-installed with Python)
3. Ensure both `server_with_launcher.py` and `client_gui.py` are in the same directory.

---

### **3. Setup and Usage**

Follow these steps to set up and use the application:

#### **3.1 Clone or Download the Repository**

Run the following commands to clone or download the repository:

```bash
git clone https://github.com/your-repo/chat-app.git
cd chat-app
3.2 Run the Server
Start the server by running:

bash
Copy code
python server_with_launcher.py
3.3 Server Interface
Start Server: Click this to start the server.
+ Add Client: Once the server is started, click this to open new client instances.
Stop Server: Stops the server and disables client creation.
3.4 Chat as a Client
Enter your username when the client starts.
Use the chat window to send and receive messages.
4. How It Works
Server:

The server listens for incoming client connections.
Messages from clients are broadcast to all other clients.
The server GUI allows for managing server and client processes.
Client:

Clients connect to the server.
Messages can be sent to the server and received from other clients.
5. Future Enhancements
Add encryption for secure communication.
Allow file sharing between clients.
Support for multiple rooms or channels.
