import socket

HOST = "127.0.0.1"
PORT = 12000
BUFFER_SIZE = 1024


def main():
    """实现一个 UDP 大写回显服务器。"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print(f"UDP server listening on {HOST}:{PORT}")

        while True:
            message, client_address = server_socket.recvfrom(BUFFER_SIZE)
            modified_message = message.upper()
            server_socket.sendto(modified_message, client_address)


if __name__ == "__main__":
    main()
