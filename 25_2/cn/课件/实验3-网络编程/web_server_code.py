# import socket module
from socket import *
import os
HOST='127.0.0.1'
PORT=6789
WEB_ROOT='.'

if __name__ == '__main__':
    # 准备TCP套接字
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 将TCP套接字绑定到指定端口
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind((HOST,PORT))
    # 设置最大连接数
    serverSocket.listen(1)
    while True:
        print(f"Web server is running at http://{HOST}:{PORT}")
        # 准备迎接客户端的连接
        print('Ready to serve...')
        # 接收到客户连接请求后，建立新的TCP连接套接字
        connectionSocket, addr = serverSocket.accept()
        try:
            # 获取客户发送的报文
            message = connectionSocket.recv(1024).decode('utf-8',errors='ignore') 
            if not message:
                print("Client closed connection")
                continue  
            print(f"get request:{message}")
            # 获取客户端需要的文件名，根据html格式来进行切分
            request_line=message.splitlines()[0]
            filename =request_line.split()[1][1:] 

            # 简单防止访问上级目录，例如 ../xxx
            filename = os.path.normpath(filename)
            if filename.startswith("..") or os.path.isabs(filename):
                raise IOError
            
            file_path=os.path.join(WEB_ROOT,filename)
            with open(file_path,'r',encoding='utf-8') as f :
                outputdata=f.read() 
            # 发送http响应，记得要encode一下，因为网络传的是数据流，并在响应头设置好你设定的编码方式，比如utf-8
            # 200响应行
            response_line = "HTTP/1.1 200 OK\r\n"
            # 响应头
            response_header = "Content-Type: text/html; charset=utf-8\r\n"
            # 空行
            empty ="\r\n"
            # 响应体
            response_body = outputdata
            # 拼接响应
            response = response_line + response_header + empty + response_body
            # 发送响应
            connectionSocket.sendall(response.encode('utf-8'))
            # 关闭连接
            connectionSocket.close()
        except IOError:
            # 找不到这个文件，返回404
            # 读取404页面文件
            f = open(os.path.join(WEB_ROOT,"404.html"),'r',encoding='utf-8')
            outputdata = f.read()
            f.close()
            # 404响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
            # 响应头
            response_header = "Content-Type: text/html; charset=utf-8\r\n"
            # 空行
            empty = "\r\n"
            # 响应体
            response_body = outputdata
            # 拼接响应
            response = response_line+response_header+empty+response_body
            # 发送响应
            connectionSocket.sendall(response.encode('utf-8'))
            # 关闭连接
            connectionSocket.close()
    serverSocket.close() 