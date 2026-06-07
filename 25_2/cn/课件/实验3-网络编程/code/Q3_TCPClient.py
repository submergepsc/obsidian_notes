import socket
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12000
BUFFER_SIZE = 1024
QUIT_MESSAGE = "bye"
def main():
    """实现一个 TCP 长连接客户端：持续发送消息，直到输入 bye。"""
    # TODO:
    # 1. 创建 TCP socket，并连接服务端。
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST,SERVER_PORT))
        # 2. 在同一个连接中循环读取键盘输入并发送给服务端。
        while True:
            message=input("input the sentence to be transformed:")
            client_socket.sendall(message.encode())
        # 3. 如果输入 QUIT_MESSAGE，通知服务端后结束循环。
            if message==QUIT_MESSAGE:
                break
        # 4. 对普通消息，接收并打印服务端返回的小写结果。
            modified_message=client_socket.recv(BUFFER_SIZE)
            if not modified_message:
                print("Server closed connection")
                break
        # 5. 退出前关闭连接。 
            print(modified_message.decode()) 

        modified_message=client_socket.recv(BUFFER_SIZE)
        print("From server:",modified_message.decode())
if __name__ == "__main__":
    main()
