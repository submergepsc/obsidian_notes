# ARP 协议

- Source: https://www.runoob.com/np/arp-protocol.html

ARP（Address Resolution Protocol，地址解析协议）是一种用于将网络层地址（如 IP 地址）解析为数据链路层地址（如 MAC 地址）的协议。

ARP 在局域网（LAN）中广泛使用，帮助设备在通信时确定目标设备的物理地址。


---

## ARP 的工作原理


ARP 的核心功能是通过广播请求和单播响应，将 IP 地址解析为 MAC 地址。


### 1. ARP 请求


当设备需要与目标设备通信时，如果不知道目标设备的 MAC 地址，它会发送一个 ARP 请求广播包，询问"谁拥有这个 IP 地址？"。


![](https://www.runoob.com/wp-content/uploads/2025/02/arp-n-1.png)


- 发送方广播 ARP 请求包，询问目标 IP 地址对应的 MAC 地址。
- 局域网中的所有设备都会收到该请求。


### 2. ARP 响应


如果某个设备发现自己的 IP 地址与 ARP 请求中的目标 IP 地址匹配，它会发送一个 ARP 响应包，告知自己的 MAC 地址。


![](https://www.runoob.com/wp-content/uploads/2025/02/arp-n-2.png)


- 接收方发送 ARP 响应包，告知自己的 MAC 地址。
- ARP 响应包是单播的，只发送给请求方。


### 3. ARP 缓存


发送方在收到 ARP 响应后，会将 IP 地址和 MAC 地址的映射关系存储在本地 ARP 缓存中，以便后续通信时直接使用。


![](https://www.runoob.com/wp-content/uploads/2025/02/arp-n-3.png)


- ARP 缓存会定期更新或过期，以确保映射关系的准确性。


---


## ARP 的关键特性


- **IP 地址到 MAC 地址的映射**： - 将网络层地址解析为数据链路层地址。
- **广播请求和单播响应**： - 使用广播发送 ARP 请求，使用单播发送 ARP 响应。
- **ARP 缓存**： - 存储 IP 地址和 MAC 地址的映射关系，减少重复的 ARP 请求。
- **局域网内使用**： - ARP 主要用于局域网中，不适用于跨网络通信。


---


## ARP 的应用场景


ARP 广泛应用于以下场景：


- **局域网通信**： - 设备在局域网中通信时，需要知道目标设备的 MAC 地址。
- **路由器转发**： - 路由器在转发数据包时，需要知道下一跳的 MAC 地址。
- **网络诊断**： - 使用 ARP 命令查看本地 ARP 缓存，诊断网络问题。


---


## ARP 的安全性


ARP 本身是不安全的，容易受到以下攻击：


- **ARP 欺骗（ARP Spoofing）**： - 攻击者伪造 ARP 响应，将自己的 MAC 地址与目标 IP 地址关联。
- **ARP 泛洪（ARP Flooding）**： - 攻击者发送大量伪造的 ARP 请求，耗尽网络资源。


为了提高安全性，可以使用以下防护措施：


- **静态 ARP 表**：手动配置 IP 地址和 MAC 地址的映射关系。
- **ARP 检测**：监控网络中的 ARP 流量，检测异常行为。
- **网络隔离**：使用 VLAN 或子网隔离设备，减少 ARP 攻击的影响。


---


## ARP 的替代方案


在某些场景下，可以使用以下替代方案：


- **RARP（Reverse ARP）**： - 将 MAC 地址解析为 IP 地址。
- **NDP（Neighbor Discovery Protocol）**： - 在 IPv6 中替代 ARP，提供地址解析和其他功能。


---


总结来说，ARP 是一种用于将 IP 地址解析为 MAC 地址的协议，通过广播请求和单播响应实现地址映射。它广泛应用于局域网通信和网络诊断中，但需要注意其安全性问题。








	  AI 思考中...





			** [TLS 协议](https://www.runoob.com/tls-protocol.html)
			[RARP 协议](https://www.runoob.com/rarp-protocol.html) **













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