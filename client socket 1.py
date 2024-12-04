import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Client Configuration
HOST = '127.0.0.1'
PORT = 12345

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Client")
        self.root.geometry("500x400")
        self.root.configure(bg="#2c3e50")
        
        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(self.root, state='disabled', bg="#ecf0f1", fg="#2c3e50", font=("Arial", 12))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Message entry area
        self.message_entry = tk.Entry(self.root, bg="#ecf0f1", fg="#2c3e50", font=("Arial", 12))
        self.message_entry.pack(padx=10, pady=5, fill=tk.X, side=tk.LEFT, expand=True)
        self.message_entry.bind("<Return>", self.send_message)
        
        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, bg="#3498db", fg="white", font=("Arial", 12, "bold"))
        self.send_button.pack(padx=5, pady=5, side=tk.LEFT)
        
        # Connect to server
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((HOST, PORT))
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect to server: {e}")
            self.root.destroy()
            return
        
        # Start a thread to receive messages
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self, event=None):
        """Sends a message to the server."""
        message = self.message_entry.get().strip()
        if message:
            try:
                self.client_socket.send(message.encode('utf-8'))
                self.message_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send message: {e}")
    
    def receive_messages(self):
        """Receives and displays messages from the server."""
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.display_message(message)
            except Exception as e:
                self.display_message("Connection lost.")
                self.client_socket.close()
                break

    def display_message(self, message):
        """Displays a message in the chat area."""
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()
