# Selenium测试框架集成

- Source: https://www.runoob.com/selenium/selenium-unittest.html

Selenium 可以与多种测试框架集成，例如 unittest 和 pytest，从而实现更结构化的测试代码管理和测试报告生成。

---


## 与 unittest 集成


`unittest` 是 Python 标准库中的一个测试框架，它提供了丰富的断言方法和测试组织方式。

我们可以将 Selenium 与 `unittest` 集成，以编写结构化的测试用例。


### 基本结构


以下是一个简单的 Selenium 与 `unittest` 集成的示例：


## 实例


```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

class TestGoogleSearch(unittest.TestCase):

    def setUp(self):
        # 设置正确的驱动路径
        service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("https://www.baidu.com")

    def test_search(self):
        search_box = self.driver.find_element(By.NAME, "wd")
        search_box.send_keys("Selenium")
        search_box.submit()
        self.assertIn("Selenium", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```


### 代码解析


- **`setUp` 方法**：在每个测试用例执行之前运行，用于初始化测试环境。在这里，我们启动浏览器并打开Google首页。
- **`test_search` 方法**：这是一个测试用例，用于测试Google搜索功能。我们找到搜索框，输入"Selenium"，然后提交搜索。最后，我们断言页面标题中是否包含"Selenium"。
- **`tearDown` 方法**：在每个测试用例执行之后运行，用于清理测试环境。在这里，我们关闭浏览器。


### 运行测试


可以通过以下命令运行测试：


```
python -m unittest test_baidu_search.py
```


---


## 与 pytest 集成


`pytest` 是另一个流行的Python测试框架，它提供了更简洁的语法和更强大的功能。我们可以将Selenium与`pytest`集成，以编写更灵活的测试用例。


### 基本结构


以下是一个简单的Selenium与`pytest`集成的示例：


## 实例


```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    # 设置正确的驱动路径
    service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_baidu_search(browser):
    browser.get("https://www.baidu.com")
    search_box = browser.find_element(By.NAME, "wd")
    search_box.send_keys("Selenium")
    search_box.submit()
    assert "Selenium" in browser.title
```


### 代码解析


- **`browser` 夹具**：这是一个`pytest`夹具，用于在每个测试用例执行之前启动浏览器，并在测试用例执行之后关闭浏览器。
- **`test_baidu_search` 函数**：这是一个测试用例，用于测试Google搜索功能。我们找到搜索框，输入"Selenium"，然后提交搜索。最后，我们断言页面标题中是否包含"Selenium"。


### 运行测试


可以通过以下命令运行测试：


```
pytest test_baidu_search.py
```


---


## 生成测试报告


在自动化测试中，生成测试报告是非常重要的。我们可以使用`pytest-html`插件来生成HTML格式的测试报告。


### 安装 pytest-html


可以通过以下命令安装`pytest-html`插件：


## 实例


```python
pip install pytest-html
```


### 生成测试报告


在运行测试时，可以通过以下命令生成HTML格式的测试报告：


```
pytest --html=report.html
```


生成的`report.html`文件将包含测试的详细结果，包括通过的测试用例、失败的测试用例以及错误信息。


## 测试代码


Selenium 4 引入了许多新特性，如相对定位器、改进的窗口管理、更好的 DevTools 支持等：


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_baidu_search():
    # 设置正确的驱动路径
    service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # 打开百度首页
    driver.get("https://www.baidu.com")

    # 定位搜索框并输入关键词
    search_box = driver.find_element(By.NAME, "wd")  # 百度搜索框的 name 是 "wd"
    search_box.send_keys("Selenium")

    # 定位搜索按钮并点击
    search_button = driver.find_element(By.ID, "su")  # 百度搜索按钮的 id 是 "su"
    search_button.click()

    # 等待页面加载完成（简单等待，实际项目中建议使用显式等待）
    driver.implicitly_wait(5)

    # 断言搜索结果页面是否包含关键词
    assert "Selenium" in driver.page_source

    # 关闭浏览器
    driver.quit()

# 运行测试
if __name__ == "__main__":
    test_baidu_search()
```










	  AI 思考中...





			** [Selenium Grid](https://www.runoob.com/selenium-grid.html)
			[Selenium 高级功能](https://www.runoob.com/selenium-advanced.html) **













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