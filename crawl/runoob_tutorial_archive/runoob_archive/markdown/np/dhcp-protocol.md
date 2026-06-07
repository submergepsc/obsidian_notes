# DHCP 协议

- Source: https://www.runoob.com/np/dhcp-protocol.html

DHCP（Dynamic Host Configuration Protocol，动态主机配置协议）是一种用于自动分配 IP 地址和其他网络配置信息（如子网掩码、默认网关、DNS 服务器）的协议。


DHCP 简化了网络管理，允许设备在加入网络时自动获取必要的配置，而无需手动设置。


---


## DHCP 的工作原理


DHCP 使用客户端-服务器模型，通过广播和单播通信实现 IP 地址的自动分配。


### 1. DHCP 发现（DHCP Discover）


当设备（DHCP 客户端）加入网络时，它会发送一个 DHCP 发现广播包，寻找可用的 DHCP 服务器。


![](https://www.runoob.com/wp-content/uploads/2025/02/dhcp-n-1.png)


- 客户端广播 DHCP Discover 包，寻找可用的 DHCP 服务器。
- 局域网中的所有设备都会收到该请求。


### 2. DHCP 提供（DHCP Offer）


DHCP 服务器收到 DHCP Discover 包后，会从地址池中选择一个可用的 IP 地址，并通过 DHCP Offer 包提供给客户端。


![](https://www.runoob.com/wp-content/uploads/2025/02/dhcp-n-2.png)


- DHCP 服务器发送 DHCP Offer 包，提供可用的 IP 地址和其他配置信息。
- DHCP Offer 包可以是广播或单播的。


### 3. DHCP 请求（DHCP Request）


客户端收到 DHCP Offer 包后，会发送一个 DHCP 请求包，确认接受提供的 IP 地址。


![](https://www.runoob.com/wp-content/uploads/2025/02/dhcp-n-3.png)


- 客户端广播 DHCP Request 包，确认接受提供的 IP 地址。
- 局域网中的所有设备都会收到该请求。


### 4. DHCP 确认（DHCP Acknowledge）


DHCP 服务器收到 DHCP Request 包后，会发送一个 DHCP 确认包，正式分配 IP 地址和其他配置信息。


![](https://www.runoob.com/wp-content/uploads/2025/02/dhcp-n-4.png)


- DHCP 服务器发送 DHCP Acknowledge 包，正式分配 IP 地址和其他配置信息。
- DHCP Acknowledge 包可以是广播或单播的。


---


## DHCP 的关键特性


- **自动分配 IP 地址**： - 从地址池中动态分配 IP 地址，避免地址冲突。
- **提供网络配置信息**： - 分配子网掩码、默认网关、DNS 服务器等配置信息。
- **租期管理**： - IP 地址的分配是有租期的，租期到期后可以续租或释放。
- **支持中继代理**： - 通过 DHCP 中继代理，可以在跨子网的网络中分配 IP 地址。
- **兼容性**： - 支持 IPv4（DHCPv4）和 IPv6（DHCPv6）。


---


## DHCP 的应用场景


DHCP 广泛应用于以下场景：


- **企业网络**： - 为员工设备自动分配 IP 地址和其他配置信息。
- **家庭网络**： - 为家庭设备（如手机、电脑）自动分配 IP 地址。
- **公共 Wi-Fi**： - 为访客设备自动分配 IP 地址和其他配置信息。
- **数据中心**： - 为服务器和虚拟机自动分配 IP 地址。


---


## DHCP 的优缺点


#### 优点：


- **简化网络管理**： - 自动分配 IP 地址和其他配置信息，减少手动配置的工作量。
- **避免地址冲突**： - 动态分配 IP 地址，确保地址的唯一性。
- **灵活配置**： - 支持租期管理、中继代理等功能，适应不同的网络需求。


#### 缺点：


- **依赖 DHCP 服务器**： - 如果 DHCP 服务器故障，设备可能无法获取 IP 地址。
- **安全性问题**： - 容易受到 DHCP 欺骗攻击，攻击者可以伪造 DHCP 服务器。


---


## DHCP 的安全性


为了提高 DHCP 的安全性，可以采取以下措施：


- **DHCP Snooping**： - 在网络设备上启用 DHCP Snooping，防止伪造的 DHCP 服务器。
- **静态绑定**： - 为特定设备配置静态 IP 地址和 MAC 地址绑定。
- **网络隔离**： - 使用 VLAN 或子网隔离设备，减少 DHCP 攻击的影响。


---


## DHCP 的替代方案


在某些场景下，可以使用以下替代方案：


- **静态 IP 地址分配**： - 手动配置设备的 IP 地址和其他配置信息。
- **BOOTP（Bootstrap Protocol）**： - 一种早期的自动配置协议，功能比 DHCP 简单。


---


总结来说，DHCP 是一种用于自动分配 IP 地址和其他网络配置信息的协议，通过客户端-服务器模型实现动态配置。它广泛应用于企业网络、家庭网络和公共 Wi-Fi 等场景，简化了网络管理，但需要注意其安全性问题。








	  AI 思考中...





			** [RARP 协议](https://www.runoob.com/rarp-protocol.html)
			[MTP 协议](https://www.runoob.com/mtp-protocol.html) **













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