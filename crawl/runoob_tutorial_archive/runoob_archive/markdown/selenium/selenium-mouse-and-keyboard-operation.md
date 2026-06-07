# Selenium 鼠标和键盘操作

- Source: https://www.runoob.com/selenium/selenium-mouse-and-keyboard-operation.html

Selenium 提供了丰富的鼠标和键盘操作功能，可以模拟用户的交互行为，例如点击、双击、拖放、悬停、输入文本、按下组合键等。

以下是 Selenium 中常用的鼠标和键盘操作及其说明：

### 鼠标操作


| 操作类型 | 方法 | 说明 |
| --- | --- | --- |
| 点击 | click(element) 或 click() | 点击指定的元素或当前鼠标位置。 |
| 双击 | double_click(element) 或 double_click() | 双击指定的元素或当前鼠标位置。 |
| 右键点击 | context_click(element) 或 context_click() | 右键点击指定的元素或当前鼠标位置。 |
| 拖放 | drag_and_drop(source, target) | 将源元素拖放到目标元素。 |
| 悬停 | move_to_element(element) | 将鼠标移动到指定元素上。 |
| 按住和释放 | click_and_hold(element) 和 release() | 按住指定元素并释放，用于实现拖拽操作。 |

### 键盘操作


| 操作类型 | 方法 | 说明 |
| --- | --- | --- |
| 输入文本 | send_keys("text") | 向输入框或文本区域输入指定的文本。 |
| 按下组合键 | send_keys(Keys.CONTROL + 'a') | 模拟按下组合键（如 Ctrl + A）。 |
| 按下单个键 | send_keys(Keys.KEY_NAME) | 模拟按下单个键（如 Enter、Tab、Shift 等）。 |
| 释放按键 | key_up(key) | 释放按下的键。 |


### 常用键盘键值


| 键值 | 说明 |
| --- | --- |
| Keys.ENTER | 回车键 |
| Keys.TAB | Tab 键 |
| Keys.SHIFT | Shift 键 |
| Keys.CONTROL | Ctrl 键 |
| Keys.ALT | Alt 键 |
| Keys.ESCAPE | Esc 键 |
| Keys.BACKSPACE | 退格键 |
| Keys.SPACE | 空格键 |
| Keys.ARROW_UP | 上箭头键 |
| Keys.ARROW_DOWN | 下箭头键 |
| Keys.ARROW_LEFT | 左箭头键 |
| Keys.ARROW_RIGHT | 右箭头键 |

---


## 鼠标操作（ActionChains 类）


在 Selenium 中，鼠标操作主要通过 `ActionChains` 类来实现。`ActionChains` 类允许我们执行复杂的鼠标操作，如点击、双击、右键点击、拖放和悬停等。


### 点击、双击、右键点击


- **点击（Click）**：模拟鼠标左键点击操作。
- **双击（Double Click）**：模拟鼠标左键双击操作。
- **右键点击（Right Click）**：模拟鼠标右键点击操作。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
driver.get("https://example.com")

# 定位元素
element = driver.find_element(By.ID, "element_id")

# 创建 ActionChains 对象
actions = ActionChains(driver)

# 点击操作
actions.click(element).perform()

# 双击操作
actions.double_click(element).perform()

# 右键点击操作
actions.context_click(element).perform()

# 关闭浏览器
driver.quit()
```


### 拖放操作


拖放操作是指将一个元素拖动到另一个位置或另一个元素上。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
driver.get("https://example.com")

# 定位拖动的元素和目标元素
source_element = driver.find_element(By.ID, "source_element_id")
target_element = driver.find_element(By.ID, "target_element_id")

# 创建 ActionChains 对象
actions = ActionChains(driver)

# 拖放操作
actions.drag_and_drop(source_element, target_element).perform()

# 关闭浏览器
driver.quit()
```


### 悬停操作


悬停操作是指将鼠标指针悬停在某个元素上，通常用于触发下拉菜单或显示提示信息。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# 初始化浏览器驱动
driver = webdriver.Chrome()

# 打开网页
driver.get("https://example.com")

# 定位元素
element = driver.find_element(By.ID, "element_id")

# 创建 ActionChains 对象
actions = ActionChains(driver)

# 悬停操作
actions.move_to_element(element).perform()

# 关闭浏览器
driver.quit()
```


## 键盘操作（Keys 类）


Selenium 中的键盘操作主要通过 `Keys` 类来实现。`Keys` 类提供了各种键盘按键的模拟操作，包括发送组合键和特殊键操作。


### 发送组合键


组合键操作是指同时按下多个键，例如 `Ctrl + C`（复制）或 `Ctrl + V`（粘贴）。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
driver.get("https://example.com")

# 定位输入框
input_element = driver.find_element(By.ID, "input_element_id")

# 输入内容并发送组合键
input_element.send_keys("Hello, World!")
input_element.send_keys(Keys.CONTROL, 'a')  # 全选
input_element.send_keys(Keys.CONTROL, 'c')  # 复制
input_element.send_keys(Keys.CONTROL, 'v')  # 粘贴

# 关闭浏览器
driver.quit()
```


### 特殊键操作（Enter、Tab、Shift 等）


特殊键操作是指模拟按下键盘上的特殊键，如 `Enter`、`Tab`、`Shift` 等。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
driver.get("https://example.com")

# 定位输入框
input_element = driver.find_element(By.ID, "input_element_id")

# 输入内容并按下 Enter 键
input_element.send_keys("Hello, World!")
input_element.send_keys(Keys.ENTER)

# 按下 Tab 键切换到下一个元素
input_element.send_keys(Keys.TAB)

# 按下 Shift 键并输入大写字母
input_element.send_keys(Keys.SHIFT, "a")  # 输入大写的 'A'

# 关闭浏览器
driver.quit()
```


---


## 综合示例


以下是一个完整的示例，展示如何使用鼠标和键盘操作：


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
driver.get("https://www.example.com")

# 鼠标操作
element = driver.find_element(By.ID, "button")
actions = ActionChains(driver)
actions.move_to_element(element).click().perform()

# 键盘操作
input_box = driver.find_element(By.ID, "input-box")
input_box.send_keys("Hello, Selenium!")
input_box.send_keys(Keys.ENTER)

# 关闭浏览器
driver.quit()
```









	  AI 思考中...





			** [Selenium 浏览器操作](https://www.runoob.com/selenium-browser-operator.html)
			[Selenium 文件上传和下载](https://www.runoob.com/selenium-file-operator.html) **













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