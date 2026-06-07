import socket
import struct
import random
from socket import *
def get_random_buffer_size():
    return random.randint(0, 5) + 1
    
def recv_exact(connectionSocket, size):
    """
    从TCP字节流中准确读取size个字节。
    TCP不保留消息边界，所以不能假设一次recv就能收到完整数据。
    """
    data = b''
    while len(data) < size:
        packet = connectionSocket.recv(min(get_random_buffer_size(), size - len(data)))
        # 客户端关闭连接时，recv会返回b''
        if not packet:
            return None
        data += packet
    return data
if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 设置端口重用，以便服务能迅速重启
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定端口号和套接字
    serverSocket.bind(('', serverPort))
    # 开启监听
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        # 等待接受客户端的连接
        connectionSocket, addr = serverSocket.accept()
        # 设置mes编号
        mes_idx = 1
        # 不断处理客户端的请求
        while True: 
            # 接受客户端的数据
            sentence = connectionSocket.recv(get_random_buffer_size()).decode('utf-8')
            header=recv_exact(connectionSocket,4)
            mes_len=struct.unpack('!I',header)[0]
            mes_data=recv_exact(connectionSocket,mes_len)
            if mes_data is None:
                print("Clinet closed connection")
                break
            sentence=mes_data.decode('utf-8')
            # 输出客户端发来的数据
            print('server get mes{}: {}'.format(mes_idx, sentence.replace('\0', '')))
            # 若以\0为结束，则停止监听
            if sentence.endswith('\0'):
                print('server end listening from client')
                break
            mes_idx += 1
        # 连接关闭
        connectionSocket.close()
