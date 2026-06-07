# VS Code MCP 服务

- Source: https://www.runoob.com/vscode/vscode-mcp-servers.html

MCP（Model Context Protocol）是一种开放标准，提供统一接口，让 AI 模型（例如 Copilot Chat）能够发现和调用外部工具，实现读取文件、调用 API、执行任务等多种操作。


在 VS Code 中，MCP 客户端（Copilot）通过 MCP 服务器提供的工具完成任务，而服务器端可以部署在本地或远程。


![](https://www.runoob.com/wp-content/uploads/2025/08/usb-c-example-mcp-servers-from-norah-sakal-blog.png)


上图是 MCP 架构图：


- MCP 是核心，一边连 客户端（MCP clients），像用 client.py 写的程序；另一边通过服务器（MCP server），连远程服务（比如图里的彩色图标 App）和本地数据源（蓝色笑脸图标这类）。
- 客户端还能对接 MCP 主机（hosts），像 Claude、ChatGPT 这些，让 MCP 能调用它们的能力，把各方串起来干活～ 就像给不同工具搭了个 "协作网"，让 MCP 能连通远程、本地，还能借外部大模型的力 。


在使用 VS Code MCP 服务前，确保安装最新版的 Visual Studio Code。


然后还要安装相关的 VS Code 的 AI 扩展，我们可以使用微软的 GitHub Copilot，登录账号（包括 Free、Business 或 Enterprise 计划）即可。


从 VS Code 1.102 版本开始，VS Code 中的 MCP 支持已全面可用，可以在设置中看是否启用。


![](https://www.runoob.com/wp-content/uploads/2025/08/8d6f88b2-ff06-4521-8d12-8a76e7a6caf7.png)


---

## 配置 MCP 服务器


在 VS Code 中添加 MCP 服务器有多种方式：


- 直接安装：访问精选的 MCP 服务器列表 [https://code.visualstudio.com/mcp](https://code.visualstudio.com/mcp)，选择任意 MCP 服务器上的 "安装"，即可自动将其添加到你的 VS Code 实例中。
- 工作区设置：在工作区中添加 **.vscode/mcp.json** 文件，为该工作区配置 MCP 服务器，并与团队成员共享配置。
- 用户设置：在用户配置（通过 "MCP：打开用户配置"）中指定服务器，使该 MCP 服务器在所有工作区中启用，并通过 "设置同步" 进行同步。
- 自动发现：启用自动发现功能（chat.mcp.discovery.enabled），以发现其他工具（如 Claude 桌面版）中定义的 MCP 服务器。


本章节我们使用工作区设的方法。


### 实例


以下是一个简单的 VS Code 中 MCP 应用的 "Hello World" 示例，我们先创建一个 python 文件 test.py，代码如下：


## test.py 文件代码


```
import sys
import json

# 读取 MCP 初始化请求
_ = json.load(sys.stdin)

# 输出 MCP 响应（标准 JSON）
json.dump({
    "type": "text",
    "text": "Hello World from MCP!"
}, sys.stdout)
```


接下来我们创建一个能返回 "Hello World" 的 MCP 服务器配置。


在你的工作区文件夹中创建 **.vscode/mcp.json**（没有 **.vscode** 目录就创建它） 文件，填入以下配置（模拟一个简单的本地 MCP 服务器）:


## .vscode/mcp.json 文件代码


```
{
  "servers": {
    "HelloWorldServer": {
      "type": "stdio",
      "command": "python3",
      "args": ["test.py"]
    }
  }
}
```


![](https://www.runoob.com/wp-content/uploads/2025/08/eaa1c292-9f3b-4ad5-a6d9-11f22739e751.png)



保存文件后，打开 VS Code 命令面板（Ctrl+Shift+P）：运行 "MCP: Show Installed Servers" 命令:


![](https://www.runoob.com/wp-content/uploads/2025/08/a895dfdc-b5f3-4116-b1c9-d4e62214588c.png)


你会看到配置的 "HelloWorldServer":


![](https://www.runoob.com/wp-content/uploads/2025/08/18c501dd-7d86-4b14-9389-a503df0a6dc0.png)


启动该服务器，它会立即返回 "Hello World from MCP!" 信息

我们可以在 AI 的聊天窗口输入"执行 HelloWorldServer"，就可以看到输出结果了：


![](https://www.runoob.com/wp-content/uploads/2025/08/3fb50db9-42e5-4f30-a708-49cdcf9e9abe.png)


打开 **.vscode/mcp.json** 右下角有个"添加服务器..."的图标，我们可以通过它添加更多服务，包含执行的命令或者远程的 http 服务：


![](https://www.runoob.com/wp-content/uploads/2025/08/7c1dcdec-25a7-4932-8610-722a69816411.png)

使用 MCP 控制浏览器


我们可以在 VS Code 里控制 Chrome 浏览器，比如自动打开网页、抓取内容、截图甚至填写表单等。

这里需要借助开源项目 mcp-chrome，开源地址为 [https://github.com/hangwin/mcp-chrome/](https://github.com/hangwin/mcp-chrome/) 。


我们可以让 AI agent或工具通过 MCP 协议操作浏览器。


**环境要求：**


- Chrome 或 Chromium 浏览器
- Node.js ≥ v18.19.0
- VS Code、Github Copilot

### 安装 mcp-chrome-bridge mcp-chrome-bridge 这是 VS Code 与浏览器之间的桥梁。


```
npm install -g mcp-chrome-bridge
```


### 安装并配置浏览器插件

前往 GitHub Releases 页面 [https://github.com/hangwin/mcp-chrome/releases](https://github.com/hangwin/mcp-chrome/releases) 下载 mcp-chrome 插件源码（不是 .crx，而是完整解压包）。

![](https://www.runoob.com/wp-content/uploads/2025/08/1699b3a5-c94f-4513-9bbb-7c6607a0896f.png)


打开 Chrome 输入：**chrome://extensions**




开启右上角"开发者模式"



点击"加载未打包扩展程序"，选择你下载的插件文件夹



安装成功后点击插件图标，点击"连接"


![](https://www.runoob.com/wp-content/uploads/2025/08/00cd8cee-3410-4ca0-b449-3b03c9c3958d.png)


点击插件图标打开插件，点击连接即可看到 mcp 的配置：


![](https://www.runoob.com/wp-content/uploads/2025/08/01380c12-9611-4185-bef4-3e5eafc17f87.png)


## 配置 VS Code 与 MCP 通信

在工程目录下创建 **.vscode/mcp.json**，加入如下基本配置：


```
{
  "servers": {
     "chrome-mcp": {
      "type": "http",
      "url": "http://127.0.0.1:12306/mcp"
    }
  }
}
```


http://127.0.0.1:12306/ 这个地址是插件桥接服务的默认监听地址。


启动它：


![](https://www.runoob.com/wp-content/uploads/2025/08/c65533f5-8d10-402d-8b7c-7457335482d9.png)


-->







	  AI 思考中...





			** [VSCode 数据库客户端扩展](https://www.runoob.com/vscode-db-extensions.html)














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