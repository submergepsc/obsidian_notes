import socket
HOST = "127.0.0.1"
PORT = 12000
BUFFER_SIZE = 1024
QUIT_MESSAGE = "bye"
def handle_client(connection_socket, client_address):
    """在同一个 TCP 连接中持续处理客户端消息。"""
    # TODO:
    print(f"Connected by {client_address}")
    # 1. 循环接收客户端数据。
    with connection_socket:
        while True:
            data=connection_socket.recv(BUFFER_SIZE)
            # print("recv raw data:", repr(data))
    # 3. 如果 recv 返回空字节，说明客户端已经关闭连接。
            if not data:
                print(f"Client closed connection:")
                break   
        # 2. 如果客户端发送 QUIT_MESSAGE，结束本次连接。 
            message=data.decode()
            if message==QUIT_MESSAGE:
                print(f"Client sent quit message,closing this connection")
                break
    # 4. 对普通消息，转换为小写并发回客户端。
            modified_message=message.lower()
            connection_socket.sendall(modified_message.encode()) 
def main():
    """实现一个 TCP 长连接服务端：处理完一个客户端后继续等待下一个客户端。"""
    # TODO:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 1. 创建 TCP 监听 socket，并绑定到 HOST 和 PORT。
        server_socket.bind((HOST,PORT))
    # 2. 开始监听客户端连接。
        print(f"TCP listing on {HOST}:{PORT}")
        server_socket.listen(1)

    # 3. 每次 accept 后，在 handle_client 中处理这个连接的多次请求。
        while True:
            connection_socket,client_address=server_socket.accept()
            handle_client(connection_socket,client_address)
    # 4. 当前客户端断开后，继续等待新的客户端连接。 
if __name__ == "__main__":
    main()
