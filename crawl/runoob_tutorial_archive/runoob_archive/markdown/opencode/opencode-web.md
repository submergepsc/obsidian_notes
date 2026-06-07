# OpenCode Web 使用（浏览器界面）

- Source: https://www.runoob.com/opencode/opencode-web.html

除了终端（TUI）之外，OpenCode 还提供了 Web 界面，可以通过浏览器直接使用 AI 编程能力。


**Web 模式适合：远程访问、团队协作、可视化操作。**


**OpenCode Web 是 TUI 的图形化版本，让 AI 编程从终端工具升级为可视化协作平台。**


---


## 一、什么是 OpenCode Web？


OpenCode Web 是基于 HTTP 服务的图形界面版本，本质上是：


- 后端：OpenCode 服务（CLI 启动）
- 前端：浏览器界面


可以理解为：**TUI 的可视化版本**


![](https://www.runoob.com/wp-content/uploads/2026/04/web-homepage-new-session.BB1mEdgo_Z1AT1v3.png)


---


## 二、启动 Web 服务


### 1、基本启动


```
opencode web
```


默认会：


- 启动本地 HTTP 服务
- 自动打开浏览器


---


### 2、自定义端口


```
opencode web --port 4096
```


---


### 3、允许外部访问（重要）


```
opencode web --hostname 0.0.0.0 --port 4096
```


可在局域网或远程访问


---


## 三、访问方式


启动后，在浏览器访问：


```
http://localhost:4096
```


或：


```
http://你的IP:4096
```


---


## 四、界面说明


OpenCode Web 界面通常包含：


- **输入区：**输入提示词（类似 ChatGPT）
- **对话区：**显示 AI 输出结果
- **文件上下文：**自动读取项目代码
- **操作记录：**执行命令与修改日志


本质与 TUI 一致，只是更直观


---


## 五、基本使用方式


### 1、提问


```
帮我分析这个项目的结构
```


### 2、引用文件


```
这个函数是做什么的？@src/index.js
```


### 3、执行修改


```
把这个函数拆成三个函数，并增加错误处理
```


**说明：**


- Web 与 TUI 的指令完全一致
- 同样支持上下文理解


### 4、会话

在主页上查看和管理你的会话。你可以查看活跃的会话，也可以创建新的会话。


![](https://www.runoob.com/wp-content/uploads/2026/04/web-homepage-active-session.BbK4Ph6e_Z1O7nO1.png)


### 5、服务器状态

点击 **See Servers** 可以查看已连接的服务器及其状态。


![](https://www.runoob.com/wp-content/uploads/2026/04/web-homepage-see-servers.BpCOef2l_ZB0rJd.png)


---


## 六、认证（安全设置）


如果你在公网或团队环境使用，建议开启认证：


```
export OPENCODE_SERVER_PASSWORD=123456
opencode web
```


**说明：**


- 用户名默认：opencode
- 密码：你设置的值


---


## 七、常见使用场景


### 1、远程开发


- 服务器运行 OpenCode
- 浏览器远程访问


### 2、团队共享


- 多人查看 AI 修改结果
- 共享对话上下文


### 3、演示 / 教学


- 比终端更直观
- 适合录屏与展示


---


## 八、Web vs TUI


| 维度 | TUI（终端） | Web（浏览器） |
| --- | --- | --- |
| 使用方式 | 命令行 | 图形界面 |
| 操作效率 | 高（快捷键多） | 中 |
| 可视化 | 较弱 | 更直观 |
| 远程访问 | 较复杂 | 简单 |
| 适合人群 | 开发者 | 新手 / 团队 |


---


## 九、常见问题


### 1、无法访问页面


检查：


- 端口是否开放
- 是否使用正确地址（localhost / IP）


### 2、无法远程访问


确保使用：


```
--hostname 0.0.0.0
```


### 3、端口被占用


更换端口：


```
opencode web --port 5000
```










	  AI 思考中...





			** [OpenCode CLI 使用](https://www.runoob.com/opencode-cli.html)
			[OpenCode GitHub](https://www.runoob.com/opencode-github.html) **













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