# Selenium元素操作

- Source: https://www.runoob.com/selenium/selenium-ele-operator.html

在 Selenium 中，定位到元素后，可以对其进行各种操作，例如点击、输入文本、获取属性等。

以下是 Selenium 中常用的元素操作及其详细说明。


| 操作类型 | 方法 | 说明 | 示例 |
| --- | --- | --- | --- |
| 输入文本 | send_keys("text") | 向输入框或文本区域输入指定的文本。 | element.send_keys("testuser") |
| 点击元素 | click() | 点击按钮、链接或其他可点击的元素。 | element.click() |
| 清除输入框内容 | clear() | 清除输入框或文本区域中的内容。 | element.clear() |
| 获取元素属性 | get_attribute("attribute_name") | 获取元素的指定属性值（如 value、href、class 等）。 | value = element.get_attribute("value") |
| 获取元素文本 | text | 获取元素的可见文本内容。 | print(element.text) |
| 复选框/单选框操作 | is_selected() 和 click() | 检查复选框或单选框是否被选中，并选中或取消选中。 | if not checkbox.is_selected(): checkbox.click() |
| 下拉列表操作 | Select 类的 select_by_index、select_by_value、select_by_visible_text | 通过索引、值或可见文本选择下拉列表的选项。 | dropdown.select_by_visible_text("China") |
| 鼠标操作 | ActionChains 类的 click、double_click、context_click、drag_and_drop、move_to_element | 执行复杂的鼠标操作，如点击、双击、拖放、悬停等。 | actions.move_to_element(element).perform() |
| 键盘操作 | Keys 类的 send_keys(Keys.KEY_NAME) | 模拟键盘操作，如按下回车键、Tab 键、组合键等。 | element.send_keys(Keys.ENTER) |
| 文件上传 | send_keys("file_path") | 通过 元素上传文件。 | element.send_keys("/path/to/file.txt") |
| 执行 JavaScript | execute_script("javascript_code") | 执行 JavaScript 代码，用于复杂的操作或修改页面内容。 | driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") |


## 1. 输入文本（send_keys）


在自动化测试中，经常需要向输入框中输入文本，Selenium 提供了`send_keys`方法来实现这一功能。


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# 设置正确的驱动路径
service = ChromeService(executable_path="./chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# 启动浏览器
driver = webdriver.Chrome()

# 打开网页
driver.get("https://example.com")

# 定位输入框元素
input_element = driver.find_element_by_name("username")

# 输入文本
input_element.send_keys("your_username")

# 关闭浏览器
driver.quit()
```


在上面的代码中，我们首先定位了一个输入框元素，然后使用`send_keys`方法向其中输入了文本"your_username"。


## 2. 点击元素（click）


点击操作是自动化测试中最常见的操作之一。Selenium提供了`click`方法来模拟用户点击元素。


## 实例


```python
# 定位按钮元素
button_element = driver.find_element_by_id("submit-button")

# 点击按钮
button_element.click()
```


在这个例子中，我们定位了一个按钮元素，并使用`click`方法模拟了用户点击该按钮的操作。


## 3. 清除输入框内容（clear）


有时我们需要清除输入框中已有的内容，然后再输入新的内容。Selenium提供了`clear`方法来实现这一功能。


## 实例


```python
# 定位输入框元素
input_element = driver.find_element_by_name("username")

# 清除输入框内容
input_element.clear()

# 输入新的文本
input_element.send_keys("new_username")
```


在这个例子中，我们首先清除了输入框中的内容，然后输入了新的文本"new_username"。


## 4. 获取元素属性（get_attribute）


在自动化测试中，有时需要获取元素的属性值。Selenium提供了`get_attribute`方法来获取元素的属性。


## 实例


```python
# 定位元素
element = driver.find_element_by_id("element-id")

# 获取元素的属性值
attribute_value = element.get_attribute("class")

print(attribute_value)
```


在这个例子中，我们获取了一个元素的`class`属性值，并将其打印出来。


## 5. 获取元素文本（text）


有时我们需要获取元素内部的文本内容。Selenium提供了`text`属性来获取元素的文本。


## 实例


```python
# 定位元素
element = driver.find_element_by_id("element-id")

# 获取元素的文本内容
text_content = element.text

print(text_content)
```


在这个例子中，我们获取了一个元素的文本内容，并将其打印出来。


## 6. 复选框和单选框操作


复选框和单选框是Web表单中常见的元素。Selenium提供了`click`方法来操作这些元素。


### 复选框操作


## 实例


```python
# 定位复选框元素
checkbox_element = driver.find_element_by_id("checkbox-id")

# 如果复选框未被选中，则点击选中
if not checkbox_element.is_selected():
    checkbox_element.click()
```


在这个例子中，我们首先检查复选框是否已经被选中，如果没有被选中，则点击选中它。


### 单选框操作


## 实例


```python
# 定位单选框元素
radio_button_element = driver.find_element_by_id("radio-button-id")

# 如果单选框未被选中，则点击选中
if not radio_button_element.is_selected():
    radio_button_element.click()
```


单选框的操作与复选框类似，我们也是先检查单选框是否已经被选中，如果没有被选中，则点击选中它。


## 7. 下拉列表操作（Select 类）


下拉列表是Web表单中常见的元素之一。Selenium提供了`Select`类来方便地操作下拉列表。


## 实例


```python
from selenium.webdriver.support.ui import Select

# 定位下拉列表元素
dropdown_element = driver.find_element_by_id("dropdown-id")

# 创建Select对象
select = Select(dropdown_element)

# 通过可见文本选择选项
select.select_by_visible_text("Option 1")

# 通过值选择选项
select.select_by_value("1")

# 通过索引选择选项
select.select_by_index(0)
```


在这个例子中，我们首先定位了一个下拉列表元素，然后使用`Select`类来操作它。我们可以通过可见文本、值或索引来选择下拉列表中的选项。


## 总结


本文详细介绍了Selenium中常见的元素操作，包括输入文本、点击元素、清除输入框内容、获取元素属性和文本、操作复选框和单选框，以及处理下拉列表。掌握这些基础操作是进行自动化测试的关键。希望本文能帮助你更好地理解和使用Selenium进行Web自动化测试。









	  AI 思考中...





			** [Selenium 元素定位](https://www.runoob.com/selenium-element-positioning.html)
			[Selenium 等待机制](https://www.runoob.com/selenium-wait.html) **













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