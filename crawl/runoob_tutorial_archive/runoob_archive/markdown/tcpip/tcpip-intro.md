# TCP/IP 介绍

- Source: https://www.runoob.com/tcpip/tcpip-intro.html

---


TCP/IP 是用于因特网 (Internet) 的通信协议。


---


## 计算机通信协议（Computer Communication Protocol）


计算机通信协议是对那些计算机必须遵守以便彼此通信的的规则的描述。


---


## 什么是 TCP/IP？


TCP/IP 是供已连接因特网的计算机进行通信的通信协议。


TCP/IP 指传输控制协议/网际协议（***T*ransmission *C*ontrol *P*rotocol** / ***I*nternet *P*rotocol**）。


TCP/IP 定义了电子设备（比如计算机）如何连入因特网，以及数据如何在它们之间传输的标准。


---


## 在 TCP/IP 内部


在 TCP/IP 中包含一系列用于处理数据通信的协议：


- TCP (传输控制协议) - 应用程序之间通信
- UDP (用户数据报协议) - 应用程序之间的简单通信
- IP (网际协议) - 计算机之间的通信
- ICMP (因特网消息控制协议) - 针对错误和状态
- DHCP (动态主机配置协议) - 针对动态寻址


---


## TCP 使用固定的连接


TCP 用于应用程序之间的通信。


当应用程序希望通过 TCP 与另一个应用程序通信时，它会发送一个通信请求。这个请求必须被送到一个确切的地址。在双方"握手"之后，TCP 将在两个应用程序之间建立一个全双工 (full-duplex) 的通信。


这个全双工的通信将占用两个计算机之间的通信线路，直到它被一方或双方关闭为止。


UDP 和 TCP 很相似，但是更简单，同时可靠性低于 TCP。


---


## IP 是无连接的


IP 用于计算机之间的通信。


IP 是无连接的通信协议。它不会占用两个正在通信的计算机之间的通信线路。这样，IP 就降低了对网络线路的需求。每条线可以同时满足许多不同的计算机之间的通信需要。


通过 IP，消息（或者其他数据）被分割为小的独立的包，并通过因特网在计算机之间传送。


IP 负责将每个包路由至它的目的地。


---


## IP 路由器


当一个 IP 包从一台计算机被发送，它会到达一个 IP 路由器。


IP 路由器负责将这个包路由至它的目的地，直接地或者通过其他的路由器。


在一个相同的通信中，一个包所经由的路径可能会和其他的包不同。而路由器负责根据通信量、网络中的错误或者其他参数来进行正确地寻址。


---


## TCP/IP


TCP/IP 意味着 TCP 和 IP 在一起协同工作。


TCP 负责应用软件（比如您的浏览器）和网络软件之间的通信。


IP 负责计算机之间的通信。


TCP 负责将数据分割并装入 IP 包，然后在它们到达的时候重新组合它们。


IP 负责将包发送至接受者。









	  AI 思考中...





			** [TCP/IP 教程](https://www.runoob.com/tcpip-tutorial.html)
			[TCP/IP 寻址](https://www.runoob.com/tcpip-addressing.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/../skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/../skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/../skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/../skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/../skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/../skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/../skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)

      : · [免责声明](https://www.runoob.com/../disclaimer/index.html)

      : · [关于我们](https://www.runoob.com/../aboutus/index.html)

      : · [文章归档](https://www.runoob.com/../archives/index.html)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/../index/index.html)**
    **[runoob.com](https://www.runoob.com/../index/index.html)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **