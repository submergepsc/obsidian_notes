# Selenium 无头浏览器模式

- Source: https://www.runoob.com/selenium/selenium-headless.html

无头浏览器模式（Headless Mode）是指在没有图形用户界面（GUI）的情况下运行浏览器，换句话说，浏览器在后台运行，不会弹出可见的窗口。


无头浏览器模式通常用于自动化测试、网页抓取、性能测试等场景，因为它可以节省系统资源，并且在没有显示器的服务器上也能正常运行。


- **启用无头模式**：通过 `ChromeOptions` 或 `FirefoxOptions` 添加 `--headless` 参数。
- **优化设置**：禁用 GPU 加速、设置窗口大小等。
- **验证无头模式**：通过打印页面标题或截图验证脚本运行结果。


### 为什么使用无头浏览器模式？


- **节省资源**：无头模式不需要渲染图形界面，因此可以节省 CPU 和内存资源。
- **提高速度**：由于不需要加载和渲染图形界面，无头模式通常比普通模式更快。
- **适合自动化**：在自动化测试和网页抓取中，无头模式可以避免干扰，并且可以在没有显示器的服务器上运行。
- **便于调试**：在某些情况下，无头模式可以帮助开发者更快地调试和定位问题。

---


## Selenium 中的无头浏览器模式


### 设置 Chrome 无头模式


在 Selenium 中，你可以通过 `ChromeOptions` 类来设置 Chrome 浏览器的无头模式。以下是一个简单的示例：


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 设置 Chrome 无头模式
chrome_options = Options()
chrome_options.add_argument("--headless")  # 启用无头模式
chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速

# 创建 WebDriver 实例
driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=chrome_options)

# 打开网页
driver.get("https://www.baidu.com")

# 打印网页标题
print(driver.title)

# 关闭浏览器
driver.quit()
```


### 设置 Firefox 无头模式


对于 Firefox 浏览器，你可以使用 `FirefoxOptions` 类来设置无头模式。以下是一个示例：


## 实例


```python
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# 设置 Firefox 无头模式
firefox_options = Options()
firefox_options.add_argument("--headless")  # 启用无头模式

# 创建 WebDriver 实例
driver = webdriver.Firefox(service=Service('/path/to/geckodriver'), options=firefox_options)

# 打开网页
driver.get("https://www.example.com")

# 打印网页标题
print(driver.title)

# 关闭浏览器
driver.quit()
```


### 设置 Edge 无头模式


对于 Edge 浏览器，你可以使用 `EdgeOptions` 类来设置无头模式。以下是一个示例：


## 实例


```python
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# 设置 Edge 无头模式
edge_options = Options()
edge_options.add_argument("--headless")  # 启用无头模式

# 创建 WebDriver 实例
driver = webdriver.Edge(service=Service('/path/to/msedgedriver'), options=edge_options)

# 打开网页
driver.get("https://www.example.com")

# 打印网页标题
print(driver.title)

# 关闭浏览器
driver.quit()
```


---


## 无头模式下的常见问题及解决方案


### 页面加载不完全


在无头模式下，有时页面可能加载不完全，导致元素无法找到。可以通过以下方式解决：


- **增加等待时间**：使用 `WebDriverWait` 显式等待元素加载完成。
- **调整窗口大小**：有时页面元素的位置和大小会根据窗口大小变化，可以通过 `driver.set_window_size(width, height)` 设置窗口大小。


### 截图和日志


在无头模式下，你可能需要截图或记录日志来调试问题。可以使用以下方法：


- **截图**：使用 `driver.save_screenshot('screenshot.png')` 保存当前页面的截图。
- **日志**：通过 `driver.get_log('browser')` 获取浏览器日志。


无头浏览器模式是 Selenium 自动化测试和网页抓取中的一个强大工具。通过简单的设置，你可以在没有图形界面的情况下运行浏览器，节省资源并提高效率。无论是 Chrome、Firefox 还是 Edge，Selenium4 都提供了简单的方法来启用无头模式。


以下是如何在无头模式下使用 Selenium 截取百度首页（www.baidu.com）的完整代码示例。

代码中启用了 Chrome 浏览器的无头模式，并截取页面截图保存为文件。


## 实例


```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 配置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 启用无头模式
chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速
chrome_options.add_argument("--window-size=1920,1080")  # 设置窗口大小

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 打开百度首页
    driver.get("https://www.baidu.com")
    # 等待页面加载完成
    time.sleep(2)  # 可以根据需要调整等待时间

    # 强制停止页面加载
    driver.execute_script("window.stop();")
    # 打印页面标题
    print("页面标题:", driver.title)

    # 截取页面截图并保存
    screenshot_path = "baidu_screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"截图已保存到: {screenshot_path}")

finally:
    # 关闭浏览器
    driver.quit()
```


执行成功后，会输出：


```
页面标题: 百度一下，你就知道
截图已保存到: baidu_screenshot.png
```


打开当前目录会看到 baidu_screenshot.png 文件，打开如下所示：


![](https://www.runoob.com/wp-content/uploads/2025/01/baidu_screenshot.png)








	  AI 思考中...





			** [Selenium 高级功能](https://www.runoob.com/selenium-advanced.html)
			[Selenium 实战项目](https://www.runoob.com/selenium-practical.html) **













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