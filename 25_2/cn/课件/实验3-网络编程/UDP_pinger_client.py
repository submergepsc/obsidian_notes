from socket import *
import time

if __name__ == '__main__': 
    serverName = '127.0.0.1'
    serverPort = 12000  
    clientSocket = socket(AF_INET, SOCK_DGRAM) 
    clientSocket.settimeout(5) 
    ping_count = 10 
    received_count = 0 
    rtt_list = []

    print(f"正在 Ping {serverName} 具有 32 字节的数据:")

    for i in range(1, ping_count + 1): 
        message = f"Ping {i}".ljust(32)

        try: 
            start_time = time.time() 
            clientSocket.sendto(message.encode(), (serverName, serverPort)) 
            modifiedMessage, serverAddress = clientSocket.recvfrom(1024) 
            end_time = time.time() 
            rtt = (end_time - start_time) * 1000 
            rtt_list.append(rtt) 
            received_count += 1 
            if rtt < 1:
                print(f"来自 {serverAddress[0]} 的回复: 字节={len(modifiedMessage)} 时间<1ms")
            else:
                print(f"来自 {serverAddress[0]} 的回复: 字节={len(modifiedMessage)} 时间={round(rtt)}ms")

        except timeout: 
            print("请求超时。") 
    clientSocket.close() 
    lost_count = ping_count - received_count
    lost_rate = lost_count / ping_count * 100

    print()
    print(f"{serverName} 的 Ping 统计信息:")
    print(f"    数据包: 已发送 = {ping_count}，已接收 = {received_count}，丢失 = {lost_count} ({lost_rate:.0f}% 丢失)，")
 
    if len(rtt_list) > 0:
        min_rtt = min(rtt_list)
        max_rtt = max(rtt_list)
        avg_rtt = sum(rtt_list) / len(rtt_list)

        print("往返行程的估计时间(以毫秒为单位):")
        print(f"    最短 = {round(min_rtt)}ms，最长 = {round(max_rtt)}ms，平均 = {round(avg_rtt)}ms")
    else:
        print("所有请求均超时，无法计算往返时间。")