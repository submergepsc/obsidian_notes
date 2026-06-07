# IGMP 协议

- Source: https://www.runoob.com/np/igmp-protocol.html

IGMP（Internet Group Management Protocol，互联网组管理协议）是一种用于管理 IP 组播组成员关系的协议。


IGMP 运行在主机和与其直接相连的路由器之间，用于支持 IP 组播通信。


---


## IGMP 的工作原理


IGMP 的主要功能是让主机能够加入或离开组播组，并让路由器能够了解哪些组播组在本地网络中有成员。


### 1. 主机加入组播组


当主机希望加入某个组播组时，它会向本地网络发送 IGMP 成员报告（Membership Report）消息。


![](https://www.runoob.com/wp-content/uploads/2025/03/icmp-n-1.png)


- 主机发送 IGMP 成员报告消息，表示希望接收某个组播地址的数据。


### 2. 路由器查询组播成员


路由器定期发送 IGMP 查询（Membership Query）消息，询问本地网络中有哪些主机是组播组的成员。


![](https://www.runoob.com/wp-content/uploads/2025/03/icmp-n-2.png)


- 路由器发送 IGMP 查询消息，询问本地网络中的组播成员。
- 主机收到查询消息后，发送 IGMP 成员报告消息，表明自己仍然是组播组的成员。


---


### 3. 主机离开组播组


当主机希望离开某个组播组时，它会发送 IGMP 离开组（Leave Group）消息。


![](https://www.runoob.com/wp-content/uploads/2025/03/icmp-n-3.png)


- 主机发送 IGMP 离开组消息，表示不再接收某个组播地址的数据。
- 路由器收到离开组消息后，会发送特定组查询（Group-Specific Query），确认是否还有其他主机是该组播组的成员。


---


## IGMP 的关键特性


- **组播组成员管理**： - 支持主机动态加入或离开组播组。
- **路由器查询机制**： - 路由器通过定期查询了解本地网络中的组播成员。
- **版本支持**： - IGMP 有多个版本（IGMPv1、IGMPv2、IGMPv3），每个版本的功能和兼容性不同。
- **效率高**： - 通过组播方式传输数据，减少网络带宽的占用。


---


## IGMP 的应用场景


IGMP 广泛应用于以下场景：


- **视频流媒体**： - 支持多用户同时观看同一个视频流。
- **在线会议**： - 支持多用户参与同一个在线会议。
- **网络游戏**： - 支持多玩家同时参与同一个网络游戏。
- **数据分发**： - 支持将数据同时分发给多个接收者。


---


## IGMP 的优缺点


#### 优点：


- **高效性**： - 通过组播方式传输数据，减少网络带宽的占用。
- **灵活性**： - 支持主机动态加入或离开组播组。
- **可扩展性**： - 支持大规模组播通信。


#### 缺点：


- **复杂性**： - 组播网络的管理和配置较为复杂。
- **兼容性**： - 不同版本的 IGMP 可能存在兼容性问题。


---


### IGMP 的版本


IGMP 有多个版本，每个版本的功能和兼容性不同：


- **IGMPv1**： - 支持基本的组播组成员管理功能。
- **IGMPv2**： - 增加了离开组消息和特定组查询功能。
- **IGMPv3**： - 增加了源过滤功能，支持主机选择接收特定源的组播数据。


---


总结来说，IGMP 是一种用于管理 IP 组播组成员关系的协议，通过让主机能够加入或离开组播组，并让路由器了解本地网络中的组播成员，支持高效的组播通信。它广泛应用于视频流媒体、在线会议、网络游戏和数据分发等场景。








	  AI 思考中...





			** [ICMP 协议](https://www.runoob.com/icmp-protocol.html)
			[GGP 协议](https://www.runoob.com/ggp-protocol.html) **













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