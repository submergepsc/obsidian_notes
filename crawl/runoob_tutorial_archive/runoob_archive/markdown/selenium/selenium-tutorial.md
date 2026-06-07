# Selenium 教程

- Source: https://www.runoob.com/selenium/selenium-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2024/08/selenium.png)

Selenium 是一个用于自动化 Web 浏览器操作的工具集。


Selenium主要用于 Web 应用程序的自动化测试。


Selenium支持多种编程语言（如 Python、Java、C#、JavaScript 等），并且可以在多种浏览器（如 Chrome、Firefox、Edge、Safari 等）和操作系统（如 Windows、macOS、Linux）上运行。

Selenium 的核心功能是模拟用户在浏览器中的操作，例如点击按钮、输入文本、导航页面等。


## 谁适合阅读本教程？


- **软件测试工程师**
- **开发人员**（前端、后端、全栈）
- **数据分析师和数据科学家**
- **DevOps 工程师**
- **学生和编程爱好者**
- **技术经理和团队负责人**
- **创业者和产品经理**

Selenium 是一个功能强大的自动化测试工具，适用于 Web 应用程序的自动化测试和其他浏览器自动化任务。

通过 Selenium，你可以编写脚本来模拟用户在浏览器中的操作，从而提高测试效率。


## 阅读本教程前，您需要了解的知识：


- **编程基础**（如 Python、Java、JavaScript 等）
- **Web 开发基础**（HTML、CSS、JavaScript）
- **浏览器开发者工具**（如 Chrome DevTools）
- **版本控制工具**（如 Git，可选）
- **测试基础**（如单元测试、断言，可选）
- **操作系统和命令行基础**
- **学习资源**（官方文档、教程、书籍）


---


## 学习路径


- **学习编程基础**（如 Python 或 Java）。
- **学习 Web 开发基础**（HTML、CSS、JavaScript）。
- **熟悉浏览器开发者工具**。
- **学习 Selenium 基础**（环境搭建、元素定位、元素操作）。
- **实践项目**（如自动化登录、表单提交、数据抓取等）。
- **学习高级主题**（如等待机制、浏览器操作、测试框架集成）。


---


## 编写第一个 Selenium 脚本


下面是一个使用 Python 编写的简单 Selenium 脚本示例，这个脚本会打开 Chrome 浏览器，访问百度首页，并在搜索框中输入 "Runoob" 并点击搜索按钮。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 创建 Chrome WebDriver 实例
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com")

# 查找搜索框元素
search_box = driver.find_element_by_name("wd")

# 在搜索框中输入 "Runoob"
search_box.send_keys("Runoob")

# 模拟按下回车键
search_box.send_keys(Keys.RETURN)

# 关闭浏览器
driver.quit()
```


### 代码解析


- `webdriver.Chrome()`：创建一个 Chrome WebDriver 实例。
- `driver.get("https://www.baidu.com")`：打开百度首页。
- `driver.find_element_by_name("wd")`：查找页面中 name 属性为 "wd" 的元素（即搜索框）。
- `search_box.send_keys("Runoob")`：在搜索框中输入 "Runoob"。
- `search_box.send_keys(Keys.RETURN)`：模拟按下回车键，触发搜索。
- `driver.quit()`：关闭浏览器。


---

## 相关链接


官网：[https://www.selenium.dev/](https://www.selenium.dev/)


Selenium 下载：[https://www.selenium.dev/downloads/](https://www.selenium.dev/downloads/)


Selenium 中文文档： [https://www.selenium.dev/zh-cn/documentation/](https://www.selenium.dev/zh-cn/documentation/)

Github 开源地址：[https://github.com/SeleniumHQ](https://github.com/SeleniumHQ)








	  AI 思考中...






			[Selenium 简介](https://www.runoob.com/selenium-intro.html) **













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