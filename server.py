import socket
import threading

class Server:
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 8080
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.clients = []

    def handle_client(self, client, address):
        while True:
            data = client.recv(1024)
            if not data:
                break
            for c in self.clients:
                c.sendall(data)
        client.close()

    def start(self):
        while True:
            client, address = self.sock.accept()
            self.clients.append(client)
            thread = threading.Thread(target=self.handle_client, args=(client, address))
            thread.start()

