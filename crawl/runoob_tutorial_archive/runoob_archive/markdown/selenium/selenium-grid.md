# Selenium Grid

- Source: https://www.runoob.com/selenium/selenium-grid.html

## 1、Selenium Grid 简介


Selenium Grid 是 Selenium 套件中的一个重要组件，它允许你在多个不同的机器、浏览器和操作系统上并行执行测试。

通过 Selenium Grid，你可以实现分布式测试，从而提高测试效率，缩短测试时间。

Selenium Grid 的核心思想是将测试任务分发到多个节点（Node）上执行，而这些节点由中心节点（Hub）统一管理。


### 1.1 Selenium Grid 的主要功能


- **并行测试**：可以在多个浏览器和操作系统上同时运行测试，显著减少测试时间。
- **跨浏览器测试**：支持在不同浏览器（如 Chrome、Firefox、Edge 等）上运行测试，确保应用在各种环境下的兼容性。
- **跨平台测试**：支持在不同操作系统（如 Windows、macOS、Linux 等）上运行测试，验证应用在不同平台上的表现。
- **动态扩展**：可以根据需要动态添加或移除节点，灵活应对测试需求的变化。


### 1.2 Selenium Grid 的架构


Selenium Grid 采用 Hub-Node 架构：


- **Hub**：中心节点，负责接收测试请求并将任务分发到合适的节点上执行。
- **Node**：执行节点，负责实际执行测试任务。每个节点可以配置不同的浏览器和操作系统。

---


## 2、配置 Selenium Grid


在开始使用 Selenium Grid 之前，你需要进行一些基本的配置。以下是基于 Selenium 4 的配置步骤。


### 2.1 安装 Java


Selenium Grid 依赖于 Java 运行环境，因此首先需要安装 Java。你可以通过以下步骤安装 Java：


- 访问 [Oracle Java](https://www.oracle.com/java/technologies/javase-downloads.html) 或 [OpenJDK](https://openjdk.java.net/) 下载适合你操作系统的 Java 版本。
- 安装 Java 并配置环境变量。


### 2.2 下载 Selenium Server


Selenium Server 是 Selenium Grid 的核心组件。你可以从 [Selenium 官方网站](https://www.selenium.dev/downloads/) 下载最新版本的 Selenium Server。


- 下载 `selenium-server-.jar` 文件。
- 将下载的文件保存到一个合适的目录。


### 2.3 启动 Hub


在配置好 Java 和 Selenium Server 后，你可以启动 Hub。打开命令行工具，导航到保存 `selenium-server-.jar` 的目录，然后运行以下命令：


## 实例


```python
java -jar selenium-server-<version>.jar hub
```


这将启动 Hub，默认情况下，Hub 会监听端口 4444。你可以通过浏览器访问 `http://localhost:4444` 来查看 Hub 的状态。


### 2.4 启动 Node


接下来，你需要启动一个或多个 Node 来执行测试任务。在另一台机器或同一台机器的不同终端中，运行以下命令：


## 实例


```python
java -jar selenium-server-<version>.jar node --hub http://<hub-ip>:4444
```


其中，`` 是 Hub 所在机器的 IP 地址。如果 Hub 和 Node 在同一台机器上，可以使用 `localhost`。


### 2.5 配置 Node 的浏览器和操作系统


你可以通过命令行参数来配置 Node 的浏览器和操作系统。例如，以下命令配置了一个 Node，支持 Chrome 和 Firefox 浏览器：


## 实例


```python
java -jar selenium-server-<version>.jar node --hub http://<hub-ip>:4444 --browser "browserName=chrome" --browser "browserName=firefox"
```


## 3. 远程执行测试


配置好 Selenium Grid 后，你可以通过编写测试脚本来远程执行测试。以下是一个基于 Selenium 4 的 Python 示例。


### 3.1 安装 Selenium Python 绑定


首先，你需要安装 Selenium 的 Python 绑定：


## 实例


```python
pip install selenium
```


### 3.2 编写测试脚本


以下是一个简单的测试脚本，它通过 Selenium Grid 在远程节点上执行测试：


## 实例


```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 设置 Desired Capabilities
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['platform'] = 'WINDOWS'  # 指定操作系统
capabilities['version'] = 'latest'    # 指定浏览器版本

# 连接到 Selenium Grid Hub
driver = webdriver.Remote(
    command_executor='http://<hub-ip>:4444/wd/hub',
    desired_capabilities=capabilities
)

# 执行测试
driver.get("https://www.example.com")
print(driver.title)
driver.quit()
```


### 3.3 运行测试脚本


保存脚本并运行它。脚本将通过 Selenium Grid Hub 将测试任务分发到合适的 Node 上执行。

---


## 4、Selenium Grid 的高级配置


### 4.1 配置 Node 的浏览器和操作系统

在启动 Node 时，可以通过参数指定支持的浏览器和操作系统：


```
java -jar selenium-server-<version>.jar node --hub http://<hub-ip>:4444 --browser "browserName=chrome,platform=WINDOWS"
```


### 4.2 使用 Docker 运行 Selenium Grid

Selenium 提供了官方的 Docker 镜像，可以快速启动 Hub 和 Node：


```
# 启动 Hub
docker run -d -p 4444:4444 --name selenium-hub selenium/hub

# 启动 Node
docker run -d --link selenium-hub:hub selenium/node-chrome
```


### 4.3 配置 Grid 的负载均衡

可以通过启动多个 Hub 和 Node，配置负载均衡，提高测试的并发能力。








	  AI 思考中...





			** [Selenium 文件上传和下载](https://www.runoob.com/selenium-file-operator.html)
			[Selenium 测试框架集成](https://www.runoob.com/selenium-unittest.html) **













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