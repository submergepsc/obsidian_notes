实验二　Wireshark抓包实践

## 一、实验目标

-   学习Wireshark的基本使用方法，利用Wireshark加深对理论课讲解知识的印象；

-   学习HTTP、DNS、TCP、UDP等重要基础协议的数据抓取和过滤，并对结果进行分析；

-   复习UDP和**TCP协议（重点）；**

-   鼓励探索计算机网络课外知识，鼓励独立思考和调研。

## 二、提前阅读

**2.1 实验报告书写要求（重要！）**

**1、需要回答问题的部分会使用红字标出，例如"请使用文字与截图（可选）回答"，没有红色标注的部分不需要回答；**

**2、请将你的回答中的文字设置为"深蓝色"，方便批改；**

**3、回答问题时不抄袭、不直接复制大模型的回答、不堆砌文字、保持简洁、体现自己的思考。**

**2.2 知识补充**

1.  [[Wireshark过滤器使用指南]{.underline}](https://cloud.tencent.com/developer/article/2462400?policyId=1)

2.  [[HTTP的概念、原理、工作机制、数据格式]{.underline}](https://juejin.cn/post/6896747292091482119)

3.  [[DNS原理]{.underline}](https://juejin.cn/post/6884183177926033416#heading-4)

4.  [[UDP原理]{.underline}](https://blog.csdn.net/aa1928992772/article/details/85240358)

5.  [[TCP原理**（重点）**]{.underline}](https://juejin.cn/post/6983639186146328607#heading-7)

6.  [[TCP & UDP
    通识视频]{.underline}](https://www.bilibili.com/video/BV1kV411j7hA?from=search&seid=17537688449178395114&spm_id_from=333.337.0.0)

7.  《图解网络-小林coding》：TCP篇

注：《图解网络》可在"课程群文件-参考资料"或实验室教师共享盘中下载。

**2.3 扩展阅读：如何抓取HTTPS数据？**

本次实验并不要求大家抓取HTTPS数据，此处提供的资料仅供感兴趣的同学参考学习使用：

1、[[Wireshark配置HTTPS解密]{.underline}](https://blog.csdn.net/weixin_44786530/article/details/125130165)（推荐）

2、[[Windows下如何使用Wireshark解析HTTPS流量]{.underline}](https://medium.com/blacksecurity/%E7%94%A8wireshark-%E8%A7%A3%E6%9E%90%E4%BD%BF%E7%94%A8%E8%80%85%E7%80%8F%E8%A6%BD%E5%99%A8https%E6%B5%81%E9%87%8F%E6%95%99%E5%AD%B8-8c15948f38fd)

3、[[MacOS/Linux下如何使用Wireshark解析HTTPS流量]{.underline}](https://www.trickster.dev/post/decrypting-your-own-https-traffic-with-wireshark/)

4、其他安全分析工具，如mitmproxy、Fiddler、Charles、ZAProxy、Burp
Suite等，都可以用来解析HTTPS数据，它们解析HTTPS的方法与Wireshark不同。这些工具会自己生成一份假的根证书、导入目标设备，从而实现MITM（man-in-the-middle）攻击，截获、分析、修改HTTPS会话中的数据。这些工具仅可用于开发、测试等合法用途！

## 三、实验设备

个人主机、Wireshark软件

注：[[Wireshark下载链接]{.underline}](https://www.wireshark.org/#download)（请根据自己实验平台下载）

## 

## 四、实验要求

**4.1 实验环境配置**

1）自行完成Wireshark软件的安装；

2）在浏览器中找到并关闭"**一律使用安全连接**"或类似的设置。该设置会强制使用HTTPS连接，与后续需要使用HTTP的实验冲突，故需要将其临时关闭。以Chrome浏览器为例，该设置位于"设置-隐私与安全-安全-安全连接"下；

3）在进行实验前，关闭有可能产生网络流量的软件，减少干扰；

4）整个实验过程中务必**关闭网络代理（VPN）！**否则代理软件会对数据进行加密，导致很多数据Wireshark抓不到，影响实验。

**4.2 HTTP抓包分析**

**4.2.1 实验步骤**

1.  打开 Wireshark
    并且在捕获选项中选择被抓包的网卡，如下图1所示，通常选择
    WLAN（Windows）或
    Wi-Fi:en0（MacOS）。选择完成后Wireshark会自动开始抓包。

> ![](media/image1.png){width="4.733333333333333in"
> height="3.566666666666667in"}**图1： Wireshark抓包网卡选择界面**

2.  在浏览器输入

[[http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html\
]{.underline}](http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html)
如果出现如图2的界面，说明成功。

> ![](media/image2.png){width="5.308333333333334in"
> height="0.6833333333333333in"}

**图2：服务器返回的HTML页面**

3.  停止抓包，分析结果。**后续实验也均要及时停止抓包，减少不必要的干扰。**

**4.2.2 问题：请使用文字与截图（可选）回答**

1）结合上节课学过的网络命令，本机和服务器（指gaia.cs.umass.edu，后面简称为"服务器"）的ip地址是什么？

本机ip: 10.42.239.78

服务器ip: 128.119.245.12

2）结合问题1）的结果，在搜索栏中筛选出本机跟服务器之间的http交互数据（比如输入"ip.addr
== 128.119.245.12 and
http"\[1\]，就是筛选出ip地址为128.119.245.12的http数据包），查看过滤结果，找到本机发送请求数据包和服务器返回的响应包，并回答以下问题：

服务器返回的状态码是什么？这个状态码是什么意思？

200
OK;客户端发送的http请求已经被服务器相应和处理,并且返回了对应的网页资源.

![](media/image3.png){width="5.767361111111111in"
height="0.4791666666666667in"}服务器返回的响应报头中"Last-Modified"是什么？

Last-Modified: Tue, 28 Oct 2025 05:59:01 GMT\\r\\n

请求包和响应包的大小是多少？

![](media/image4.png){width="5.764583333333333in"
height="0.9791666666666666in"}617,555

4.  计算从本机发送http get请求到gaia.cs.umass.edu返回200
    ok响应的时间差。**提示：可查看Time字段，如图3。**

34.777204937 s − 34.404304724 s= 0.372900213 s

> ![](media/image5.png){width="6.617361111111111in"
> height="0.40694444444444444in"}**图3：数据包返回时间查看**

关于Time字段的含义可通过：视图-\>时间显示格式来选择或查看，如图4。

> ![](media/image6.png){width="5.286111111111111in"
> height="2.464583333333333in"}**图4：时间格式选择**

4）再次在浏览器输入实验网址：

[[http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html。\
]{.underline}](http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html。)
观察第一次和第二次本机收到的**http响应报文**，是否两次都有"Last-Modified"字段，解释这个字段的作用以及为什么两次呈现不同的情况。\[2\]

Last-Modified
字段用于表示资源最后修改时间。浏览器再次请求相同资源时，可能在请求头中携带
If-Modified-Since
字段。如果服务器判断资源自该时间以来没有发生修改，则可能返回 304 Not
Modified，从而让浏览器继续使用缓存内容；如果资源已经更新，则服务器会返回
200 OK 和新的资源内容

**4.3 DNS抓包分析 \[3\]**

**4.3.1 实验步骤**

1）用 ipconfig /flushdns
命令，清空本地DNS缓存(该命令较安全可放心使用)。Linux下如果本身没有安装系统缓存软件的，可忽略这一步。MacOS
系统需使用的命令，请回顾实验1的实验要求文档；

2）打开浏览器，清空浏览器的DNS记录。以Chrome浏览器为例，从地址栏进入chrome://net-internals/#dns，然后点击"clear
host cache"；

3）打开Wireshark，在搜索框输入"ip.addr
==自己的IP地址"，过滤掉不属于本机的ip数据包；

4）使用Wireshark，开始抓包；

5）利用浏览器访问"http://www.ietf.org",注意观察浏览器地址栏中的协议（HTTP/HTTPS）变化；

6）停止抓包。

**4.3.2 问题：请使用文字与截图（可选）回答**

1）找到查询"www.ietf.org"域名的 DNS 查询和响应消息，它们是通过 UDP 还是
TCP 发送的？

udp

2）DNS 查询消息的目标端口是什么？DNS 响应消息的源端口是什么？是否一样？

53;53;一样

3）DNS 查询消息发送到哪个 IP 地址？使用 ipconfig 来确定本地 DNS 服务器的
IP 地址。这两个 IP 地址是否相同？

119.29.29.29和 223.5.5.5;
![](media/image7.png){width="5.759027777777778in"
height="0.8909722222222223in"}当前dns服务器地址,10.42.239.149;不相同

5.  检查 DNS
    查询消息，DNS查询是什么\"Type\"？查询消息是否包含任何\"answers\"？

    A和AAAA类型都有.不包含

5）检查 DNS
响应消息，它提供了多少个\"answers\"？这些答案具体包含什么？逐个解释这些答案。![](media/image8.png){width="5.760416666666667in"
height="3.33125in"}

![](media/image9.png){width="5.7625in" height="3.3409722222222222in"}

对于发送给223.5.5.5的dns请求,A和AAAA类查询分别返回了两个ipv4和两个ipv6地址,对于发送给119.29.29.29也是类似.

6）考虑从主机发送的后续TCP
SYN数据包。这些SYN数据包的目的IP地址是否与DNS响应消息中提供的任何IP地址相对应？

7）在进行实验步骤5）时，你观察到了什么变化？上网查找相关资料，解释为什么会产生这种现象？提示：观察你输入的和浏览器最终使用的协议，是HTTP还是HTTPS？

**其他提示：**

1.  可以通过ipconfig /all查看本机网口的IP地址、MAC地址、DNS服务器等信息

2.  可以通过nslookup命令查看目的域名对应的ip地址，如图5查看baidu.com对应的ip地址。

> ![](media/image10.png){width="5.741666666666666in"
> height="1.7in"}**图5：nslookup查看域名对应的ip地址**

3、如果你的设备、网络环境均支持IPv6，则第一次DNS请求查询域名的Type对应IPv4地址（A代表IPv4），第二次DNS请求查询域名对应IPv6地址（AAAA代表IPv6）

**4.4 UDP抓包分析**

**4.4.1 实验步骤**

1）打开Wireshark开始抓包，然后执行会导致主机发送和接收 UDP
数据包的操作（比如提前动手写一个UDP发包程序并运行、执行DNS查询、用浏览器访问网页等，任选其一即可）

2）停止抓包，把UDP数据包过滤出来。

**4.4.2 问题：请使用文字与截图（可选）回答**

1.  任意选择一个 UDP 数据包，观察UDP报头中有哪些字段，逐个解释这些字段；

2.  观察UDP报头中各个字段的信息，请问UDP报头长度是多少？

3.  UDP报头中的长度字段（Length）是什么意思，请结合你抓到的UDP数据包回答。

4.  结合长度字段的比特长度大小，思考UDP报文的最大负载是多少？

5.  你选择的UDP数据报源端口和目的端口是什么？思考端口号范围大小是什么？

6.  UDP
    的协议号是什么？以十六进制和十进制表示法给出答案。**提示：在IP层找Protocol字段。**

7）观察一对UDP请求与响应包，描述两者间端口号的联系。

**4.5 TCP抓包分析：三次握手**

**4.5.1 实验步骤**

1）清理浏览器的缓存。以谷歌浏览器为例：历史记录-历史记录-清除浏览数据-清除图片和文件

2）打开Wireshark并启动抓包，在浏览器中输入：

http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip

待文件下载完后，停止抓包。由于使用了不安全的连接（HTTP），一些浏览器可能阻止本次下载，点击下载界面中的"保留"按钮即可。

3）把本机与"gaia.cs.umass.edu"（下面简称"服务器"）之间发送的所有数据包过滤出来（过滤条件：ip.addr==服务器IP地址，确定服务器IP地址的方式前面已经介绍过）

**4.5.2 问题：请使用文字与截图（可选）回答**

1.  本机是利用哪个IP和端口与服务器进行交互的？

2.  服务器是利用哪个IP和端口与本机进行交互的？

3.  找到本机与服务器第一次握手的数据包，你是如何确定这是第一次握手的数据包的？

4.  分析3）中你找到的第一次握手数据包，其序列号（seq）是多少？注意：Wireshark对于初始序列号会有两个描述，一个是relative，一个是raw，我们这里指raw，原始数据。

5.  找到服务器与本机第二次握手的数据包，你是如何确定这是第二次握手的数据包的？

6.  分析5）中你找到的第二次握手数据包，请问其序列号（seq）是多少？确认号字段（ack）的值是多少？ack的值是由什么决定的？

7.  找到服务器与本机第三次握手的数据包，你是如何确定这是第三次握手的数据包的？

8.  分析7）中你找到的第三次握手数据包，请问其序列号（seq）是多少？结合第一次和第二次握手的序列号、确认号以及包长度，解释为什么第三次握手的序列号和确认号是这个值？

9.  观察三次握手之后的普通TCP数据报文，其与三次握手报文的最大区别是什么？**提示：从报头的字段来进行解释。**

## 五、课后练习题

**请使用文字与截图（可选）回答以下问题。**

1）在使用Wireshark抓包时，你可能观察到一些先前未详细学习过的协议（如QUIC）。请自行查阅相关资料，在此简要介绍一个或两个课本中没有详细学习的协议。例如：它们属于哪一层、主要用于什么场景、有什么优缺点。

2）简述从浏览器输入域名开始，计算机是如何解析出目的IP地址的？

3）查阅相关资料，简要解释响应头中一些有关缓存的字段的作用，如：\
Cache-Control、Expires、Last-Modified、ETag。浏览器和服务器如何使用这些字段完成资源缓存功能的？

4）查阅相关资料，简要解释强缓存、协商缓存的区别；

5）观察多次建立TCP连接的初始序列号，我们发现TCP报文的初始序列号都是一串随机数（relative
seq本身并不在TCP报文中，它是Wireshark软件额外算出来的，目的是方便我们观察），请问TCP为什么这么设计？

6）为什么TCP握手必须要三次，两次、四次可以吗？从其优缺点来分析。

7）探索你所使用的浏览器，简要介绍：如何打开开发者工具？如何关闭浏览器的缓存功能？如何在浏览器中管理cookie？可选：浏览器中你还发现了什么有趣的功能，简单介绍一下？

## 六、参考

\[1\] Wiki.wireshark.org. 2022. DisplayFilters. \[online\] Available at:
\<https://wiki.wireshark.org/DisplayFilters\> \[Accessed 26 February
2022\].

\[2\] Segmentfault.com. 2022. 一张图理解Http缓存 - SegmentFault 思否.
\[online\] Available at: \<https://segmentfault.com/a/1190000015816331\>

\[3\] Cnblogs.com. 2022. wireshark dns域名解析抓包实验分析 -
不忘初心dbsdxq - 博客园. \[online\] Available at:
\<https://www.cnblogs.com/mggahui/p/13899888.html\> \[Accessed 26
February 2022\].

## 七、提交要求

1、实验报告：完成所有需要回答的部分（已使用**红字**指出），适当配合截图加以说明。你的回答应尽可能条理清晰，截图请缩放至适当大小；

2、提交截止时间：2026/5/27 中午11:59:59

3、提交方式：将该文档**转换为PDF**，上传至坚果云。注意**正确填写坚果云界面中要求的姓名、学号等字段**，系统会自动重命名。只需提交
PDF 实验报告。

4、提交链接：[[实验课小实验报告统一收集]{.underline}](https://send2me.cn/XinCp2uN/R0Ko-AQUUq13mw)
