# PPP 协议

- Source: https://www.runoob.com/np/ppp-protocol.html

PPP（Point-to-Point Protocol，点对点协议）是一种用于在点对点链路上传输数据的协议。


PPP 广泛应用于拨号连接、DSL、V*N 等场景，支持多种网络层协议（如 IP、IPX）的封装和传输。


---


### PPP 的工作原理


PPP 通过点对点链路在两个设备之间建立连接，并支持身份验证、数据封装和错误检测等功能。


### 1. PPP 连接建立


PPP 连接建立过程包括以下步骤：


![](https://www.runoob.com/wp-content/uploads/2025/03/ppp-n-1.png)


- **LCP（Link Control Protocol）协商**： - 设备 A 和设备 B 通过 LCP 协商链路参数（如最大帧大小、身份验证协议）。
- **身份验证**： - 设备 A 和设备 B 使用身份验证协议（如 PAP、CHAP）验证对方身份。
- **NCP（Network Control Protocol）协商**： - 设备 A 和设备 B 通过 NCP 协商网络层协议（如 IP、IPX）的参数。


### 2. PPP 数据封装


PPP 使用以下格式封装数据：


![](https://www.runoob.com/wp-content/uploads/2025/03/ppp-n-2.png)


- **标志位**：标识帧的开始和结束。
- **地址字段**：通常为 0xFF（广播地址）。
- **控制字段**：通常为 0x03（无编号帧）。
- **协议字段**：标识封装的数据类型（如 IP、IPX）。
- **数据字段**：实际传输的数据。
- **帧校验序列**：用于检测传输错误。


### 3. PPP 连接终止


PPP 连接可以通过以下步骤终止：


![](https://www.runoob.com/wp-content/uploads/2025/03/ppp-n-3.png)


- 设备 A 和设备 B 通过 LCP 终止连接。


---


### PPP 的关键特性


- **多协议支持**： - 支持多种网络层协议（如 IP、IPX）的封装和传输。
- **身份验证**： - 支持 PAP（Password Authentication Protocol）和 CHAP（Challenge Handshake Authentication Protocol）等身份验证协议。
- **错误检测**： - 使用帧校验序列（FCS）检测传输错误。
- **链路控制**： - 通过 LCP 协商链路参数，确保链路的可靠性和稳定性。
- **网络控制**： - 通过 NCP 协商网络层协议参数，确保网络层的正常运行。


---


## PPP 的应用场景


PPP 广泛应用于以下场景：


- **拨号连接**： - 通过电话线连接计算机和 ISP（互联网服务提供商）。
- **DSL**： - 通过 DSL 线路连接计算机和 ISP。
- **VPN**： - 通过 PPP 封装 IP 数据包，建立虚拟专用网络。
- **串行链路**： - 通过串行链路连接两台设备。


---


## PPP 的优缺点


#### 优点：


- **多协议支持**： - 支持多种网络层协议，适应不同的网络需求。
- **身份验证**： - 提供安全的身份验证机制，防止未授权访问。
- **错误检测**： - 通过帧校验序列检测传输错误，确保数据的可靠性。


#### 缺点：


- **复杂性**： - 需要配置和管理链路参数和网络层协议参数。
- **性能限制**： - 在低速链路上可能影响传输性能。


---


## PPP 的替代方案


在某些场景下，可以使用以下替代方案：


- **PPPoE（PPP over Ethernet）**： - 在以太网上运行 PPP，适合 DSL 和宽带连接。
- **PPPoA（PPP over ATM）**： - 在 ATM 网络上运行 PPP，适合 DSL 连接。
- **L2TP（Layer 2 Tunneling Protocol）**： - 在 IP 网络上运行 PPP，适合 VPN 连接。


---


总结来说，PPP 是一种用于在点对点链路上传输数据的协议，通过 LCP 和 NCP 协商链路和网络层参数，支持身份验证和错误检测。它广泛应用于拨号连接、DSL、VPN 等场景，适合需要点对点通信的用户。








	  AI 思考中...





			** [NTP 协议](https://www.runoob.com/ntp-protocol.html)
			[ICMP 协议](https://www.runoob.com/icmp-protocol.html) **













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