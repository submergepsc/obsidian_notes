# Linux ping 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux ping 命令用于检测与另一个主机之间的网络连接。

ping 命令通过向目标主机发送数据包并等待回应，可以测量网络响应时间和丢包率。

执行 ping 指令会使用 ICMP（Internet Control Message Protocol） 传输协议，发出要求回应的信息，若远端主机的网络功能没有问题，就会回应该信息，因而得知该主机运作正常。

### 语法

```bash
ping [选项] [目标主机/IP地址]
```


**参数说明** ：

  * `-c`：指定发送的数据包数量，例如 `-c 4` 表示发送 4 个数据包。
  * `-i`：指定每次发送数据包的间隔时间（秒），例如 `-i 0.5` 表示每 0.5 秒发送一次。
  * `-w`：设置发送数据包的等待时间上限，超出该时间后自动停止，例如 `-w 5` 表示等待 5 秒。
  * `-s`：指定每个数据包的大小（字节），默认是 56 字节。
  * `-t`：设置数据包的生存时间（TTL），指定路由跳数。
  * `-q`：安静模式，只显示开始和结束的统计数据，不显示每个数据包的详细信息。
  * `-f`：疯狂模式，快速发送数据包，用于测试网络承载能力，需谨慎使用。
  * `-l`：指定一次发送的数据包数量，通常用于负载测试。
  * `-v`：显示详细输出信息，用于调试。
  * `-4`：强制使用 IPv4 协议。
  * `-6`：强制使用 IPv6 协议。



### 实例

**1、检测是否与主机连通：**

```bash
# ping www.runoob.com //ping主机 PING aries.m.alikunlun.com (114.80.174.110) 56(84) bytes of data. 64 bytes from 114.80.174.110: icmp_seq=1 ttl=64 time=0.025 ms 64 bytes from 114.80.174.110: icmp_seq=2 ttl=64 time=0.036 ms 64 bytes from 114.80.174.110: icmp_seq=3 ttl=64 time=0.034 ms 64 bytes from 114.80.174.110: icmp_seq=4 ttl=64 time=0.034 ms 64 bytes from 114.80.174.110: icmp_seq=5 ttl=64 time=0.028 ms 64 bytes from 114.80.174.110: icmp_seq=6 ttl=64 time=0.028 ms 64 bytes from 114.80.174.110: icmp_seq=7 ttl=64 time=0.034 ms 64 bytes from 114.80.174.110: icmp_seq=8 ttl=64 time=0.034 ms 64 bytes from 114.80.174.110: icmp_seq=9 ttl=64 time=0.036 ms 64 bytes from 114.80.174.110: icmp_seq=10 ttl=64 time=0.041 ms \--- aries.m.alikunlun.com ping statistics --- 10 packets transmitted, 30 received, 0% packet loss, time 29246ms rtt min/avg/max/mdev = 0.021/0.035/0.078/0.011 ms //需要手动终止Ctrl+C
```


**2、指限制发送数据包数量：**

```bash
# ping -c 2 www.runoob.com PING aries.m.alikunlun.com (114.80.174.120) 56(84) bytes of data. 64 bytes from 114.80.174.120: icmp_seq=1 ttl=54 time=6.18 ms 64 bytes from 114.80.174.120: icmp_seq=2 ttl=54 time=15.4 ms \--- aries.m.alikunlun.com ping statistics --- 2 packets transmitted, 2 received, 0% packet loss, time 1016ms rtt min/avg/max/mdev = 6.185/10.824/15.464/4.640 ms //收到两次包后，自动退出
```


**3、多参数使用：** -i 3 发送周期为 3秒 -s 设置发送包的大小 -t 设置TTL值为 255

```bash
# ping -i 3 -s 1024 -t 255 g.cn //ping主机 PING g.cn (203.208.37.104) 1024(1052) bytes of data. 1032 bytes from bg-in-f104.1e100.net (203.208.37.104): icmp_seq=0 ttl=243 time=62.5 ms 1032 bytes from bg-in-f104.1e100.net (203.208.37.104): icmp_seq=1 ttl=243 time=63.9 ms 1032 bytes from bg-in-f104.1e100.net (203.208.37.104): icmp_seq=2 ttl=243 time=61.9 ms \--- g.cn ping statistics --- 3 packets transmitted, 3 received, 0% packet loss, time 6001ms rtt min/avg/max/mdev = 61.959/62.843/63.984/0.894 ms, pipe 2
```


**4、设置数据包间隔时间：** 以 0.2 秒的间隔发送数据包，这个参数适合测试短时间内网络的稳定性。

```bash
ping -i 0.2 www.runoob.com
```


**5、指定数据包大小：** 设置数据包大小为 128 字节，适用于检查较大数据传输时的稳定性。

```bash
ping -s 128 www.runoob.com
```


**6、设置网络超时：** 测试时间限制为 10 秒，适合在网络环境不确定的情况下测试连通性。

```bash
ping -w 10 www.example.com
```


### 常见输出解析

ping 命令的输出通常包含以下信息：

  * **发送和接收的数据包数** ：显示测试期间发送了多少个数据包，接收了多少个，以及丢包率。
  * **往返时间统计** ：显示最小、最大、平均和标准偏差等往返时间（以毫秒为单位）。

```bash
PING www.example.com (93.184.216.34): 56 data bytes 64 bytes from 93.184.216.34: icmp_seq=0 ttl=56 time=10.1 ms 64 bytes from 93.184.216.34: icmp_seq=1 ttl=56 time=10.3 ms \--- www.example.com ping statistics --- 2 packets transmitted, 2 packets received, 0% packet loss round-trip min/avg/max/stddev = 10.1/10.2/10.3/0.1 ms
```


### 高级应用

**1、快速检测网络连接：** 发送一个数据包，并设置超时为 1 秒，快速检测网络是否连接。

```bash
ping -c 1 -W 1 www.example.com
```


**2、测试大数据包的网络稳定性：** 发送 1024 字节的数据包共计 10 次，用于检测网络承载能力。

```bash
ping -s 1024 -c 10 www.example.com
```


**3、IPv6 网络测试：** 强制使用 IPv6 协议测试连接，适用于 IPv6 环境。

```bash
ping -6 www.example.com
```


### 注意事项

  * `ping` 使用 ICMP 协议，有些防火墙可能会阻止 ICMP 数据包，这样会导致 `ping` 命令无法正常工作。
  * 疯狂模式（`-f` 参数）发包速度快，建议在安全的网络环境下使用，否则可能被视为攻击行为。



使用 ping 命令，可以快速检测网络连接状态、排查网络故障，是每位网络管理人员必备的工具。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)
