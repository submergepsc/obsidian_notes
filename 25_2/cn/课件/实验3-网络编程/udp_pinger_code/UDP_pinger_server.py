from socket import *
import random
if __name__ == '__main__':
    # 创建 UDP socket
    # SOCK_DGRAM 表示使用 UDP 数据报
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    # 绑定服务器 IP 地址和端口号
    serverSocket.bind(('127.0.0.1', 12000))
    while True:
        # 生成 0 到 10 之间的随机整数
        rand = random.randint(0, 10)
        # 接收客户端数据报及其来源地址
        message, address = serverSocket.recvfrom(1024)
        # 将客户端消息转换为大写
        message = message.upper()
        # 如果随机数小于 4，则认为该数据报丢失，不向客户端回复
        if rand < 4:
            continue
        # 否则，将处理后的消息发回客户端
        serverSocket.sendto(message, address)
