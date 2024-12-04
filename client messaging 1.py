import socket
import threading
from tkinter import Tk, Text, Entry, Button, END, DISABLED, NORMAL

# Server configuration
SERVER_HOST = '192.168.143.108'  # Server IP
SERVER_PORT = 12345        # Server Port

class ChatClient:
    def __init__(self, root):
        """Initialize the chat client GUI."""
        self.root = root
        self.root.title("Chat Client")

        # Chat display
        self.chat_display = Text(root, state=DISABLED, width=50, height=20, bg="lightgray")
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Message entry box
        self.message_entry = Entry(root, width=40)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10)
        self.message_entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = Button(root, text="Send", width=10, command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        # Start the client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_HOST, SERVER_PORT))
        self.chat_display.config(state=NORMAL)
        self.chat_display.insert(END, "Connected to the server!\n")
        self.chat_display.config(state=DISABLED)

        # Start a thread to listen for incoming messages
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def receive_messages(self):
        """Receive messages from the server."""
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                self.chat_display.config(state=NORMAL)
                self.chat_display.insert(END, f"{message}\n")
                self.chat_display.config(state=DISABLED)
                self.chat_display.yview(END)  # Auto-scroll to the latest message
            except:
                self.chat_display.config(state=NORMAL)
                self.chat_display.insert(END, "Connection to the server lost.\n")
                self.chat_display.config(state=DISABLED)
                self.client_socket.close()
                break

    def send_message(self, event=None):
        """Send a message to the server."""
        message = self.message_entry.get()
        if message:
            self.client_socket.send(message.encode("utf-8"))
            self.message_entry.delete(0, END)

# Run the chat client GUI
if __name__ == "__main__":
    root = Tk()
    client = ChatClient(root)
    root.mainloop()
