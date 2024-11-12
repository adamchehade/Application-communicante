import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Configuration du client
HOST = '127.0.0.1'  # Adresse IP du serveur
PORT = 12345        # Port d'écoute du serveur

# Classe pour l'application de chat
class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Client")
        
        # Zone pour afficher les messages
        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Zone de saisie pour les messages
        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(padx=10, pady=5, fill=tk.X, side=tk.LEFT)
        self.message_entry.bind("<Return>", self.send_message)
        
        # Bouton pour envoyer le message
        self.send_button = tk.Button(self.root, text="Envoyer", command=self.send_message)
        self.send_button.pack(padx=10, pady=5, side=tk.LEFT)
        
        # Connecter au serveur
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
        
        # Démarrer le thread de réception de messages
        threading.Thread(target=self.receive_messages, daemon=True).start()
    
    # Envoyer un message
    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.client_socket.send(message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)
    
    # Recevoir et afficher les messages
    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.display_message(message)
            except ConnectionAbortedError:
                break
            except:
                print("Erreur lors de la réception du message.")
                self.client_socket.close()
                break
    
    # Afficher un message dans la zone de texte
    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

# Démarrer l'application
root = tk.Tk()
client = ChatClient(root)
root.mainloop()
