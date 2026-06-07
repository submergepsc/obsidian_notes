# Linux ssh 命令

- Source: https://www.runoob.com/python3/linux-comm-ssh.html

[![Linux 命令大全](https://www.runoob.com/images/up.gif) Linux 命令大全](https://www.runoob.com/linux-command-manual.html)


**ssh** 命令用于通过 SSH 协议连接到远程主机，实现远程登录和执行命令，它加密会话中的所有通信，确保数据传输的安全性。


SSH (Secure Shell) 是一种用于远程登录和其他网络服务之间的加密协议，SSH 提供了一个安全的通信渠道，以保护数据的机密性和完整性。


### 语法


```
ssh [options] [user@]hostname [command]
```



**参数说明**


- `[user@]hostname`：要连接的远程主机的用户名和主机名。
- `[command]`：可选的在远程主机上执行的命令。


**常用选项**


- `-l user`：指定要登录的用户。
- `-p port`：指定连接到远程主机的端口号，默认是22。
- `-i identity_file`：指定身份验证文件（私钥文件）。
- `-v`：详细模式，可以显示调试信息。
- `-C`：启用压缩。
- `-N`：不执行远程命令，只进行端口转发。
- `-f`：后台运行。
- `-L local_port:remote_host:remote_port`：本地端口转发。
- `-R remote_port:local_host:local_port`：远程端口转发。
- `-D [bind_address:]port`：动态应用程序级端口转发。


## 实例

### 基本用法

连接到远程主机：


```
ssh user@hostname
```


示例：


```
ssh [email protected]
```


指定端口连接：


```
ssh -p 2222 user@hostname
```


示例：


```
ssh -p 2222 [email protected]
```


使用身份验证文件：


```
ssh -i /path/to/private_key user@hostname
```


示例：


```
ssh -i ~/.ssh/id_rsa [email protected]
```


在远程主机上执行命令：


```
ssh user@hostname command
```


示例：


```
ssh [email protected] ls -la
```


详细模式：


```
ssh -v user@hostname
```


示例：


```
ssh -v [email protected]
```


启用压缩：


```
ssh -C user@hostname
```


示例：


```
ssh -C [email protected]
```


后台运行且不执行命令：


```
ssh -f -N user@hostname
```


示例：


```
ssh -f -N [email protected]
```


### 端口转发


本地端口转发：


```
ssh -L local_port:remote_host:remote_port user@hostname
```


示例：


```
ssh -L 8080:localhost:80 [email protected]
```


远程端口转发：


```
ssh -R remote_port:local_host:local_port user@hostname
```


示例：


```
ssh -R 8080:localhost:80 [email protected]
```


动态端口转发：


```
ssh -D [bind_address:]port user@hostname
```


示例：


```
ssh -D 1080 [email protected]
```


### 高级用法


**配置文件**


SSH 客户端配置文件位于 ~/.ssh/config，可以在其中设置常用配置。


示例：


```
Host example
    HostName example.com
    User john
    Port 2222
    IdentityFile ~/.ssh/id_rsa
```


使用时只需：


```
ssh example
```


**SSH 代理转发**


启用代理转发：


```
ssh -A user@hostname
```


示例：


```
ssh -A [email protected]
```


**X11 转发**


启用 X11 转发：


```
ssh -X user@hostname
```


示例：


```
ssh -X [email protected]
```


[![Linux 命令大全](https://www.runoob.com/images/up.gif) Linux 命令大全](https://www.runoob.com/linux-command-manual.html)








	  AI 思考中...





			** [Python 装饰器](https://www.runoob.com/python-decorators.html)
			[Python os.startfile 方法](https://www.runoob.com/python3-os-startfile.html) **













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