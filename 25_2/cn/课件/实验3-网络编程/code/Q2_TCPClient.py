import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12000
BUFFER_SIZE = 1024


def main():
    """实现一个 TCP 客户端：发送一行大写字母，并接收服务端返回的小写结果。"""
    message = input("Input uppercase sentence:")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        client_socket.sendall(message.encode())
        modified_message = client_socket.recv(BUFFER_SIZE)
        print(modified_message.decode())


if __name__ == "__main__":
    main()
