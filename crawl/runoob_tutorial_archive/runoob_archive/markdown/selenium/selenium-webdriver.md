# Selenium WebDriver

- Source: https://www.runoob.com/selenium/selenium-webdriver.html

Selenium WebDriver 是 Selenium 的核心组件，它提供了与浏览器交互的 API，允许开发者通过编程语言控制浏览器并执行各种操作。


### 启动浏览器

Selenium WebDriver 支持多种浏览器（如 Chrome、Firefox、Edge 等）。


启动浏览器前，需要下载并配置对应的浏览器驱动（如 ChromeDriver、GeckoDriver 等），详细可参见 [selenium 安装](https://www.runoob.com/selenium-install.html)。


启动浏览器的代码示例（Python）。

在 Selenium 4 中，引入了 Service 对象来设置驱动程序路径，这种方式更加灵活，且符合 Selenium 4 的设计规范。


## Selenium 4 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path="PATH_TO_DRIVER")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
```


- 导入所需的模块（`webdriver` 和 `ChromeService`）。
- 创建 `ChromeService` 对象，指定 ChromeDriver 的路径。
- 创建 `ChromeOptions` 对象，用于配置浏览器的启动选项。
- 使用 `webdriver.Chrome()` 启动 Chrome 浏览器，并传入 `service` 和 `options` 参数。


在 Selenium 3 及之前的版本中，通常直接在 webdriver.Chrome() 中设置驱动程序路径，例如：


## Selenium 3 实例


```python
from selenium import webdriver

# 设置 ChromeDriver 路径
driver_path = "/path/to/chromedriver"

# 启动 Chrome 浏览器
driver = webdriver.Chrome(executable_path=driver_path)
```


### 关闭浏览器

使用 **quit()** 方法关闭浏览器并结束 WebDriver 会话。


```
driver.quit()
```


### 打开和关闭网页


使用 **get()** 方法打开指定的 URL。


```
driver.get("https://www.example.com")
```


### 关闭当前标签页

使用 close() 方法关闭当前标签页。


```
driver.close()
```


如果只有一个标签页，close() 会关闭浏览器。


---


## 浏览器窗口操作


### 最大化窗口

使用 maximize_window() 方法将浏览器窗口最大化。


```
driver.maximize_window()
```


### 最小化窗口

使用 minimize_window() 方法将浏览器窗口最小化。


```
driver.minimize_window()
```


### 设置窗口大小

使用 set_window_size(width, height) 方法设置浏览器窗口的大小。


```
driver.set_window_size(1024, 768)  # 设置窗口大小为 1024x768 像素
```


### 全屏模式

使用 fullscreen_window() 方法将浏览器窗口设置为全屏模式。


```
driver.fullscreen_window()
```


---


## 页面导航


### 前进和后退

使用 back() 方法返回上一个页面。


使用 forward() 方法前进到下一个页面。


```
driver.get("https://www.baidu.com")
driver.get("https://www.runoob.com")

driver.back()    # 返回 baidu.com
driver.forward() # 前进到 runoob.com
```


### 刷新页面

使用 refresh() 方法刷新当前页面。


```
driver.refresh()
```


---


## 取页面标题和 URL


### 获取页面标题

使用 title 属性获取当前页面的标题。


```
title = driver.title
print("页面标题:", title)
```


### 获取当前 URL

使用 current_url 属性获取当前页面的 URL。


```
url = driver.current_url
print("当前 URL:", url)
```


## 综合示例

---

以下是一个完整的示例，演示如何启动浏览器、打开网页、操作窗口、导航页面以及获取页面信息：


## 实例


```python
# 导入所需模块
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
# 配置浏览器选项
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
driver.get("https://www.runoob.com")

# 最大化窗口
driver.maximize_window()

# 获取页面标题和 URL
print("页面标题:", driver.title)
print("当前 URL:", driver.current_url)

# 导航到另一个页面
driver.get("https://www.jyshare.com")

# 返回上一个页面
driver.back()

# 刷新页面
driver.refresh()

# 关闭浏览器
driver.quit()
```


以上代码执行后会执行以下步骤：


- 启动 Chrome 浏览器。
- 打开指定网页（`https://www.runoob.com`）。![](https://www.runoob.com/wp-content/uploads/2025/01/b58db729-9543-44b0-9673-20d6c37cfb82.png)
- 最大化浏览器窗口。
- 获取并打印页面标题和 URL。
- 导航到另一个网页（`https://www.jyshare.com`）。 ![](https://www.runoob.com/wp-content/uploads/2025/01/c7c497fc-9547-42c7-a0f7-97b359a99acc.png)
- 返回上一个页面。
- 刷新当前页面。
- 关闭浏览器。


输出结果为：


```
页面标题: 菜鸟教程 - 学的不仅是技术，更是梦想！
当前 URL: https://www.runoob.com/
```









	  AI 思考中...





			** [Selenium 安装](https://www.runoob.com/selenium-install.html)
			[Selenium 元素定位](https://www.runoob.com/selenium-element-positioning.html) **













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