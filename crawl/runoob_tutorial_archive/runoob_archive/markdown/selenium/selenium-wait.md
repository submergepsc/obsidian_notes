# Selenium 等待机制

- Source: https://www.runoob.com/selenium/selenium-wait.html

在 Selenium 中，等待机制是确保页面元素加载完成后再进行操作的关键。


由于网页加载速度受网络、服务器性能等因素影响，直接操作未加载完成的元素会导致脚本失败。

Selenium 提供了多种等待机制来解决这一问题。


## 1. 隐式等待（implicitly_wait）


### 1.1 什么是隐式等待？


隐式等待是一种全局性的等待机制，它会在查找元素时等待一定的时间。如果在指定的时间内找到了元素，Selenium 会立即继续执行后续操作；如果超时仍未找到元素，则会抛出 `NoSuchElementException` 异常。


### 1.2 如何使用隐式等待？


隐式等待通过 `implicitly_wait()` 方法来设置。这个方法只需要调用一次，之后的所有元素查找操作都会遵循这个等待时间。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 设置隐式等待时间为 10 秒
driver.implicitly_wait(10)

# 打开网页
driver.get("https://example.com")

# 查找元素
element = driver.find_element_by_id("element_id")

# 关闭浏览器
driver.quit()
```


### 1.3 隐式等待的优缺点


**优点：**


- 简单易用，只需设置一次即可应用于所有元素查找操作。
- 适用于大多数简单的场景。


**缺点：**


- 全局性等待，可能会导致不必要的等待时间。
- 无法处理某些复杂的等待条件，例如等待元素变为可点击状态。


## 2. 显式等待（WebDriverWait 和 expected_conditions）


### 2.1 什么是显式等待？


显式等待是一种更为灵活的等待机制，它允许你为特定的操作设置等待条件。显式等待通常与 `WebDriverWait` 类和 `expected_conditions` 模块一起使用。


### 2.2 如何使用显式等待？


显式等待的基本用法如下：


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
driver.get("https://example.com")

# 设置显式等待，最多等待 10 秒，直到元素出现
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "element_id"))
)

# 关闭浏览器
driver.quit()
```


### 2.3 常用的 expected_conditions


`expected_conditions` 模块提供了多种预定义的等待条件，以下是一些常用的条件：


- `presence_of_element_located`：等待元素出现在 DOM 中。
- `visibility_of_element_located`：等待元素出现在 DOM 中并且可见。
- `element_to_be_clickable`：等待元素可点击。
- `text_to_be_present_in_element`：等待元素的文本包含指定的文本。


### 2.4 显式等待的优缺点


**优点：**


- 灵活性高，可以为不同的操作设置不同的等待条件。
- 可以处理复杂的等待场景。


**缺点：**


- 代码相对复杂，需要更多的代码量。
- 需要为每个操作单独设置等待条件。


## 3. 固定等待（time.sleep）


### 3.1 什么是固定等待？


固定等待是一种最简单的等待机制，它通过 `time.sleep()` 方法让脚本暂停执行指定的时间。无论页面是否加载完成，脚本都会等待指定的时间后再继续执行。


### 3.2 如何使用固定等待？


## 实例


```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
driver.get("https://example.com")

# 固定等待 5 秒
time.sleep(5)

# 查找元素
element = driver.find_element_by_id("element_id")

# 关闭浏览器
driver.quit()
```


### 3.3 固定等待的优缺点


**优点：**


- 简单易用，适用于简单的测试场景。


**缺点：**


- 效率低下，可能会导致不必要的等待时间。
- 无法根据页面加载情况动态调整等待时间。


---


## 4. Fluent Wait


**作用：**动态设置等待条件，可以自定义轮询频率和忽略特定异常。


**方法：**WebDriverWait 结合 polling_every 和 ignoring


**特点：**更灵活，适用于需要动态调整等待时间的场景。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.example.com")

# 设置 Fluent Wait
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
element = wait.until(EC.presence_of_element_located((By.ID, "username")))
```


## 5. 总结


- **隐式等待**：适用于简单的场景，全局性等待，但可能会导致不必要的等待时间。
- **显式等待**：适用于复杂的场景，灵活性高，但代码相对复杂。
- **固定等待**：简单易用，但效率低下，不推荐在复杂的测试场景中使用。
- **Fluent Wait：**：适用于需要动态调整等待时间的场景。


在实际的自动化测试中，建议根据具体的测试需求选择合适的等待机制。通常情况下，显式等待是最为推荐的方式，因为它能够提供更好的灵活性和效率。


---

## 6. 综合示例

以下是一个完整的示例，展示如何使用隐式等待和显式等待：


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 设置隐式等待
driver.implicitly_wait(5)

# 打开网页
driver.get("https://www.example.com")

# 使用显式等待等待元素可见
username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "username"))
)
username.send_keys("testuser")

# 使用显式等待等待元素可点击
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "submit-btn"))
)
submit_button.click()

# 关闭浏览器
driver.quit()
```









	  AI 思考中...





			** [Selenium 元素操作](https://www.runoob.com/selenium-ele-operator.html)
			[Selenium 浏览器操作](https://www.runoob.com/selenium-browser-operator.html) **













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