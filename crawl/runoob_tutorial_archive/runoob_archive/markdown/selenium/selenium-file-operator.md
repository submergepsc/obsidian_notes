# Selenium4 文件上传和下载

- Source: https://www.runoob.com/selenium/selenium-file-operator.html

在 Selenium 中，文件上传和下载是常见的自动化操作需求。

- **文件上传**：通过 `send_keys()` 方法将文件路径传递给 `*` 元素。
- **文件下载**：通过配置浏览器的下载选项，并触发下载操作，等待文件下载完成。
- **注意事项**：确保文件路径正确，并根据实际需求调整等待时间和浏览器配置。

以下是文件上传和下载的详细说明：



### 文件上传


| 方法 | 说明 |
| --- | --- |
| send_keys("file_path") | 将文件路径传递给 元素，实现文件上传。 |
| execute_script() | 如果文件上传元素是隐藏的，可以使用 JavaScript 使其可见。 |
| 第三方工具（如 AutoIT） | 如果文件上传不是通过 实现的，可能需要使用第三方工具。 |


---


### 文件下载


| 方法 | 说明 |
| --- | --- |
| 配置浏览器下载选项 | 通过 ChromeOptions 或 FirefoxOptions 设置下载路径、禁用提示等。 |
| click() | 点击下载按钮，触发文件下载。 |
| 等待文件下载完成 | 使用 time.sleep() 或循环检查文件是否下载完成。 |
| 检查下载文件 | 使用 os.listdir() 检查下载目录中的文件。 |


---


### 文件上传和下载的常见问题


| 问题 | 解决方法 |
| --- | --- |
| 文件上传元素不可见 | 使用 JavaScript 使元素可见：driver.execute_script("arguments[0].style.display = 'block';", element) |
| 非 元素 | 使用第三方工具（如 AutoIT 或 PyWin32）模拟文件选择对话框。 |
| 下载路径配置失败 | 确保下载路径存在且可写，并正确配置浏览器选项。 |
| 文件未下载完成 | 增加等待时间，或使用循环检查文件是否下载完成。 |


## 文件上传操作


文件上传是 Web 应用程序中常见的功能之一。

在 Selenium 中，文件上传通常通过``元素实现。

以下是实现文件上传的步骤：


**定位文件上传元素**：首先，我们需要定位到文件上传的输入框元素。通常，这个元素是一个``标签，类型为`file`。


## 实例


```python
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
```


**发送文件路径**：一旦定位到文件上传元素，我们可以使用`send_keys()`方法将文件的绝对路径发送到该元素。


## 实例


```python
file_input.send_keys("/path/to/your/file.txt")
```


这将触发文件选择对话框，并自动选择指定的文件。


**提交表单**：在某些情况下，文件上传后需要提交表单。你可以通过点击提交按钮来完成这一操作。


## 实例


```python
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()
```


### 注意事项


- 确保文件路径是正确的，并且文件存在。
- 如果文件上传元素是隐藏的，可能需要使用 JavaScript 来使其可见。


## 文件下载操作


文件下载操作在 Selenium 中稍微复杂一些，因为涉及到浏览器的下载对话框。

以下是实现文件下载的步骤：


**设置下载路径**：首先，我们需要设置浏览器的下载路径。这可以通过设置浏览器的首选项来实现。


## 实例


```python
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/download/directory",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options)
```


这将设置浏览器的默认下载路径，并禁用下载提示。


**触发下载**：接下来，我们需要找到触发下载的链接或按钮，并点击它。


## 实例


```python
download_link = driver.find_element(By.XPATH, "//a[@id='downloadLink']")
download_link.click()
```


这将触发文件下载，并自动保存到之前设置的下载路径中。


**等待下载完成**：为了确保文件下载完成，我们可以使用`time.sleep()`或更智能的等待机制。


## 实例


```python
import time
time.sleep(10)  # 等待10秒，确保文件下载完成
```


### 注意事项


- 确保下载路径是可写的。
- 如果下载的文件较大，可能需要增加等待时间。


## 处理下载对话框


在某些情况下，浏览器可能会弹出下载对话框，询问用户是否保存文件。为了自动化处理这种情况，我们可以使用以下方法：


**使用浏览器首选项**：如上所述，通过设置浏览器的首选项，可以禁用下载对话框。


## 实例


```python
chrome_options.add_experimental_option("prefs", {
    "download.prompt_for_download": False
})
```


**使用AutoIT或类似工具**：如果无法通过浏览器首选项禁用下载对话框，可以使用AutoIT等工具来自动化处理对话框。


## 实例


```python
import autoit

autoit.win_wait_active("文件下载")
autoit.control_click("文件下载", "Button1")
```


这将自动点击下载对话框中的"保存"按钮。


### 注意事项


- AutoIT脚本需要在Windows环境下运行。
- 确保AutoIT脚本与Selenium脚本同步执行。

---


## 示例代码

以下是一个完整的示例，展示如何配置 Chrome 浏览器的下载选项并下载文件：


## 实例


```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import os

# 设置下载路径
download_dir = "/path/to/download/directory"

# 配置 Chrome 选项
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_dir,  # 设置下载路径
    "download.prompt_for_download": False,       # 禁用下载提示
    "download.directory_upgrade": True,          # 允许下载到指定目录
    "safebrowsing.enabled": True                 # 启用安全浏览
}
chrome_options.add_experimental_option("prefs", prefs)

# 启动浏览器
service = ChromeService(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开网页
driver.get("https://www.example.com/download")

# 点击下载按钮
download_button = driver.find_element(By.ID, "download-button")
download_button.click()

# 等待文件下载完成
time.sleep(10)  # 根据文件大小调整等待时间

# 检查文件是否下载成功
files = os.listdir(download_dir)
print("下载的文件列表:", files)

# 关闭浏览器
driver.quit()
```









	  AI 思考中...





			* [Selenium 鼠标和键盘操作](https://www.runoob.com/selenium-mouse-and-keyboard-operation.html)
			[Selenium Grid](https://www.runoob.com/selenium-grid.html) **













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