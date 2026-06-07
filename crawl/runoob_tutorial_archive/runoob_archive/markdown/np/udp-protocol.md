# UDP 协议

- Source: https://www.runoob.com/np/udp-protocol.html

UDP（User Datagram Protocol，用户数据报协议）是一种简单的、无连接的传输层协议，用于在网络中传输数据。


与 [TCP](https://www.runoob.com/tcp-protocol.html) 不同，UDP 不提供可靠性、顺序性和流量控制，但它具有低延迟和高效的特点，适合对实时性要求较高的应用。


---


## UDP 的工作原理


UDP 是一种无连接协议，客户端和服务器之间不需要建立连接即可发送数据。它的核心功能是快速传输数据包。


### 1. UDP 数据包结构


UDP 数据包由以下部分组成：


- **源端口**：发送方的端口号。
- **目的端口**：接收方的端口号。
- **长度**：数据包的总长度（包括头部和数据）。
- **校验和**：用于检测数据包是否损坏（可选）。
- **数据**：实际传输的数据。


![](https://www.runoob.com/wp-content/uploads/2025/02/udp-n-1.png)


---


### 2. UDP 数据传输


![](https://www.runoob.com/wp-content/uploads/2025/02/udp-n-2.png)


- 客户端直接向服务器发送 UDP 数据包。
- 服务器接收 UDP 数据包，但不发送确认信息。


---


## UDP 的关键特性


- **无连接**： - 不需要建立连接，直接发送数据。
- **不可靠性**： - 不保证数据包的到达、顺序和完整性。
- **低延迟**： - 由于不需要建立连接和确认，传输延迟较低。
- **高效性**： - 头部开销小，适合传输小数据包。
- **支持广播和多播**： - 可以向多个接收方发送数据包。


---


## UDP 的应用场景


UDP 广泛应用于以下场景：


- **实时应用**：如 VoIP（语音通话）、视频会议、在线游戏。
- **广播和多播**：如网络广播、流媒体分发。
- **简单查询**：如 DNS 查询、DHCP 请求。
- **轻量级协议**：如 SNMP（简单网络管理协议）、TFTP（简单文件传输协议）。


---


## UDP 的优缺点


#### 优点：


- **低延迟**：适合对实时性要求高的应用。
- **高效**：头部开销小，适合传输小数据包。
- **简单**：实现简单，资源占用少。


#### 缺点：


- **不可靠**：不保证数据包的到达、顺序和完整性。
- **无流量控制**：可能导致数据包丢失或网络拥塞。
- **无连接管理**：无法检测连接状态。


---


## UDP 的替代方案


在某些场景下，可以使用以下替代方案：


- **TCP**：提供可靠性、顺序性和流量控制，适合对数据完整性要求高的应用。
- **SCTP**：结合了 TCP 和 UDP 的优点，支持多流和多宿主。


---


总结来说，UDP 是一种简单的、无连接的传输层协议，通过低延迟和高效的数据传输适合对实时性要求高的应用。它广泛应用于实时应用、广播和多播等场景，但需要注意其不可靠性和无连接管理的缺点。








	  AI 思考中...





			** [SFTP 协议](https://www.runoob.com/sftp-protocol.html)
			[SSL 协议](https://www.runoob.com/ssl-protocol.html) **













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