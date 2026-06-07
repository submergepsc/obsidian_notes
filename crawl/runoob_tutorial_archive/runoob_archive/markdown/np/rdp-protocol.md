# RDP 协议

- Source: https://www.runoob.com/np/rdp-protocol.html

RDP（Remote Desktop Protocol，远程桌面协议）是由 Microsoft 开发的一种协议，用于远程访问和控制另一台计算机的桌面。


RDP 允许用户通过网络在本地设备上操作远程计算机，就像坐在远程计算机前一样。


---


## RDP 的工作原理


RDP 使用客户端-服务器模型，通过加密的通信通道传输远程桌面的图像、输入和声音。它的核心功能是远程访问和控制。


### 1. RDP 连接建立


![](https://www.runoob.com/wp-content/uploads/2025/02/rdp-n-1.png)


- 客户端连接到服务器的 3389 端口（默认的 RDP 端口）。
- 服务器发送证书给客户端。
- 客户端验证服务器证书。
- 客户端和服务器协商加密算法。
- 客户端生成会话密钥，用服务器公钥加密后发送。
- 双方使用会话密钥加密后续通信。


---


### 2. 远程桌面会话


在连接建立后，客户端可以远程访问和控制服务器：


![](https://www.runoob.com/wp-content/uploads/2025/02/rdp-n-2.png)


- 客户端发送输入（如键盘、鼠标）到服务器。
- 服务器发送屏幕更新到客户端。


---


### 3. 连接关闭


在远程会话完成后，客户端可以关闭连接：


![](https://www.runoob.com/wp-content/uploads/2025/02/rdp-n-3.png)


- 客户端请求断开连接。
- 服务器关闭会话。


---


## RDP 的关键特性


- **远程访问和控制**： - 允许用户远程访问和控制另一台计算机的桌面。
- **加密通信**： - 使用 TLS/SSL 加密通信，保护数据传输的安全。
- **多设备支持**： - 支持多种客户端设备（如 Windows、Mac、Linux、Android、iOS）。
- **高效传输**： - 使用压缩和优化技术，减少带宽占用。
- **多用户支持**： - 支持多个用户同时连接到同一台服务器（需要 Windows Server 版本）。


---


## RDP 的应用场景


RDP 广泛应用于以下场景：


- **远程办公**：员工可以远程访问公司计算机。
- **技术支持**：IT 人员可以远程协助用户解决问题。
- **服务器管理**：管理员可以远程管理服务器。
- **教育和培训**：教师可以远程演示和指导学生。


---


## RDP 的安全性


RDP 通过以下机制提高安全性：


- **加密通信**：防止数据被窃听。
- **身份验证**：通过用户名和密码或智能卡验证用户身份。
- **网络级身份验证（NLA）**：在建立会话前验证用户身份，防止暴力破解。


---


## RDP 的替代方案


在某些场景下，可以使用以下替代方案：


- **VNC（Virtual Network Computing）**：一种跨平台的远程桌面协议。
- **SSH**：用于远程命令行访问。
- **TeamViewer**：一种商业远程桌面软件，支持多种平台。


---


总结来说，RDP 是一种用于远程访问和控制计算机桌面的协议，通过加密通信和高效传输技术提供安全的远程会话。它广泛应用于远程办公、技术支持和服务器管理等场景。如果你对 RDP 的某个具体特性或应用场景感兴趣，可以进一步探讨！








	  AI 思考中...





			** [IMAP 协议](https://www.runoob.com/imap-protocol.html)
			[SFTP 协议](https://www.runoob.com/sftp-protocol.html) **













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