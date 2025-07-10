import socket

def tcp_users_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    message = "Привет, сервер?"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"\nОтвет от сервера:\n{response}")

    client_socket.close()

if __name__ == "__main__":
    tcp_users_client()

