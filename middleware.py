import socket
import threading

class middleware:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 8080
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)

    def is_valid_message(self, message):
        # Implement your validation logic here
        return True

    def handle_client(self, client):
        while True:
            data = client.recv(1024)
            if not data or not self.is_valid_message(data):
                break
            # Forward valid data to the server
            self.forward_to_server(data)
        client.close()

    def forward_to_server(self, data):
        # Implement the logic to send data to the server
        pass

    def start(self):
        while True:
            client, _ = self.sock.accept()
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()
