# RARP 协议

- Source: https://www.runoob.com/np/rarp-protocol.html

RARP（Reverse Address Resolution Protocol，反向地址解析协议）是一种用于将数据链路层地址（如 MAC 地址）解析为网络层地址（如 IP 地址）的协议。


RARP 是 ARP（Address Resolution Protocol，地址解析协议）的反向操作，主要用于无盘工作站等设备在启动时获取自己的 IP 地址。 --- ## RARP 的工作原理 RARP 的核心功能是通过广播请求和单播响应，将 MAC 地址解析为 IP 地址。


### 1. RARP 请求


当设备启动时，如果不知道自己的 IP 地址，它会发送一个 RARP 请求广播包，询问"谁拥有这个 MAC 地址？"。


![](https://www.runoob.com/wp-content/uploads/2025/02/rarp-n-1.png)


- 发送方广播 RARP 请求包，询问自己的 MAC 地址对应的 IP 地址。
- 局域网中的所有设备都会收到该请求。


### 2. RARP 响应


如果某个设备（通常是 RARP 服务器）发现自己的配置中包含了该 MAC 地址的 IP 地址映射，它会发送一个 RARP 响应包，告知对应的 IP 地址。


![](https://www.runoob.com/wp-content/uploads/2025/02/rarp-n-2.png)


- RARP 服务器发送 RARP 响应包，告知发送方的 IP 地址。
- RARP 响应包是单播的，只发送给请求方。


---


#### 3. IP 地址配置


发送方在收到 RARP 响应后，会使用获取的 IP 地址配置自己的网络接口，从而能够与其他设备通信。


![](https://www.runoob.com/wp-content/uploads/2025/02/rarp-n-3.png)


---


## RARP 的关键特性


- **MAC 地址到 IP 地址的映射**： - 将数据链路层地址解析为网络层地址。
- **广播请求和单播响应**： - 使用广播发送 RARP 请求，使用单播发送 RARP 响应。
- **无盘工作站使用**： - 主要用于无盘工作站在启动时获取 IP 地址。
- **局域网内使用**： - RARP 主要用于局域网中，不适用于跨网络通信。


---


## RARP 的应用场景


RARP 广泛应用于以下场景：


- **无盘工作站**： - 无盘工作站在启动时通过 RARP 获取 IP 地址。
- **网络配置**： - 在缺乏 DHCP 的环境中，使用 RARP 为设备分配 IP 地址。


---


## RARP 的局限性


RARP 存在以下局限性：


- **功能单一**： - 只能提供 IP 地址，无法提供其他网络配置信息（如子网掩码、网关）。
- **依赖 RARP 服务器**： - 需要配置专门的 RARP 服务器，增加了管理复杂性。
- **安全性差**： - 容易受到欺骗攻击，攻击者可以伪造 RARP 响应。


---


## RARP 的替代方案


由于 RARP 的局限性，它已被更强大的协议取代，主要包括：


- **BOOTP（Bootstrap Protocol）**： - 提供 IP 地址和其他网络配置信息。
- **DHCP（Dynamic Host Configuration Protocol）**： - 动态分配 IP 地址和其他网络配置信息，是 BOOTP 的扩展。


---


总结来说，RARP 是一种用于将 MAC 地址解析为 IP 地址的协议，通过广播请求和单播响应实现地址映射。它主要用于无盘工作站在启动时获取 IP 地址，但由于其功能单一和安全性差，已被 BOOTP 和 DHCP 取代。









	  AI 思考中...





			** [ARP 协议](https://www.runoob.com/arp-protocol.html)
			[DHCP 协议](https://www.runoob.com/dhcp-protocol.html) **













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