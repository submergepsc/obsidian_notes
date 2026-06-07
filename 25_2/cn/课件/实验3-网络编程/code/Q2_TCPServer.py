import socket

HOST = "127.0.0.1"
PORT = 12000
BUFFER_SIZE = 1024


def handle_client(connection_socket, client_address):
    """处理一个 TCP 客户端连接。"""
    with connection_socket:
        message = connection_socket.recv(BUFFER_SIZE)
        if not message:
            return
        modified_message = message.lower()
        connection_socket.sendall(modified_message)


def main():
    """实现一个 TCP 服务端：一次连接处理一条消息，然后继续等待下一个连接。"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"TCP server listening on {HOST}:{PORT}")

        while True:
            connection_socket, client_address = server_socket.accept()
            handle_client(connection_socket, client_address)


if __name__ == "__main__":
    main()
