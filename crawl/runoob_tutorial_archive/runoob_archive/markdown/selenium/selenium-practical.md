# Selenium 实战项目

- Source: https://www.runoob.com/selenium/selenium-practical.html

在现代软件开发中，自动化测试已经成为确保软件质量的重要手段之一。

Selenium 是一个广泛使用的自动化测试工具，它支持多种编程语言和浏览器，能够模拟用户操作，进行功能测试、回归测试等。

本文将详细介绍如何使用 Selenium 进行自动化测试，并通过实战项目演示如何实现登录、注册和搜索（以百度为例）等常见功能的自动化测试。


## 1. 实战项目：自动化测试案例


### 1.1 登录功能测试


假设我们有一个登录页面，包含用户名和密码输入框以及登录按钮，我们将编写一个自动化测试脚本来模拟用户登录操作。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开登录页面
driver.get("https://example.com/login")

# 定位用户名输入框并输入用户名
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("testuser")

# 定位密码输入框并输入密码
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("password123")

# 定位登录按钮并点击
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# 验证登录是否成功
assert "Welcome" in driver.page_source

# 关闭浏览器
driver.quit()
```


### 1.2 注册功能测试


接下来，我们编写一个自动化测试脚本来模拟用户注册操作。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# 配置 Chrome 选项
chrome_options = Options()

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开注册页面
driver.get("https://example.com/register")

# 定位用户名输入框并输入用户名
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("newuser")

# 定位邮箱输入框并输入邮箱
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("[email protected]")

# 定位密码输入框并输入密码
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("newpassword123")

# 定位确认密码输入框并输入密码
confirm_password_input = driver.find_element(By.ID, "confirm-password")
confirm_password_input.send_keys("newpassword123")

# 定位注册按钮并点击
register_button = driver.find_element(By.ID, "register-button")
register_button.click()

# 验证注册是否成功
assert "Registration successful" in driver.page_source

# 关闭浏览器
driver.quit()
```


### 1.3 搜索功能测试（百度）


最后，我们编写一个自动化测试脚本来模拟用户在百度搜索框中输入关键词并搜索的操作。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 配置 Chrome 选项
chrome_options = Options()

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开百度首页
driver.get("https://www.baidu.com")

# 定位搜索框并输入关键词
search_box = driver.find_element(By.NAME, "wd")
search_box.send_keys("runoob")

# 模拟按下回车键进行搜索
search_box.send_keys(Keys.RETURN)

# 验证搜索结果页面是否包含关键词
assert "runoob" in driver.page_source

# 关闭浏览器
driver.quit()
```










	  AI 思考中...





			** [Selenium 无头浏览器模式](https://www.runoob.com/selenium-headless.html)














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