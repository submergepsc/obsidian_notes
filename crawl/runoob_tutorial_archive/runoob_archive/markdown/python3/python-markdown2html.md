# Python Markdown 生成 HTML

- Source: https://www.runoob.com/python3/python-markdown2html.html

Markdown 是一种轻量级的标记语言，它允许你使用易读易写的纯文本格式来编写文档，然后将其转换为结构化的 HTML 文档。


Markdown 的语法简单直观，常用于编写博客、文档、README 文件等。

更多 Markdown 内容参考：[Markdown 教程](https://www.runoob.com/../markdown/md-tutorial.html)

Python 可以使用 markdown 模块将 Markdown 文本转换为 HTML。


---


## 将 Markdown 转换为 HTML 的步骤


### 1. 安装 markdown 库


首先，我们需要安装 Python 的 `markdown` 库，可以使用 `pip` 来安装它：


```
pip install markdown
```


### 2. 编写 Python 脚本


以下是一个简单的实例，将 Markdown 文本转换为 HTML：


## 实例


```python
import markdown

# 定义 Markdown 文本
md_text = """
# 这是标题
这是 **加粗** 的文本。
这是 *斜体* 的文本。

- 列表项 1
- 列表项 2

[点击这里](https://www.runoob.com) 访问网站。
"""

# 转换为 HTML
html_output = markdown.markdown(md_text)

# 输出 HTML
print(html_output)
```


输出结果为：


```
<h1>这是标题</h1>
<p>这是 <strong>加粗</strong> 的文本。
这是 <em>斜体</em> 的文本。</p>
<ul>
<li>列表项 1</li>
<li>列表项 2</li>
</ul>
<p><a href="https://www.runoob.com">点击这里</a> 访问网站。</p>
```


接下来，我们可以编写一个简单的 Python 脚本来将 Markdown 文件（可以把上面实例的 markdown 文本放到文件中）转换为 HTML 文件：


## convert_markdown_to_html.py 文件代码：


```python
import markdown

# 读取 Markdown 文件
with open('example.md', 'r', encoding='utf-8') as file:
    markdown_text = file.read()

# 将 Markdown 转换为 HTML
html = markdown.markdown(markdown_text)

# 将 HTML 写入文件
with open('example.html', 'w', encoding='utf-8') as file:
    file.write(html)

print("Markdown 文件已成功转换为 HTML 文件！")
```


### 3. 运行脚本


将上述代码保存为 `convert_markdown_to_html.py`，然后在终端中运行它：


```
python convert_markdown_to_html.py
```


运行后，`example.md` 文件将被转换为 `example.html` 文件。


** 代码说明：**


**import markdown**：这行代码导入了 `markdown` 库，它提供了将 Markdown 文本转换为 HTML 的功能。


```
with open('example.md', 'r', encoding='utf-8') as file:
    markdown_text = file.read()
```


这段代码使用 `open` 函数打开 `example.md` 文件，并读取其内容到 `markdown_text` 变量中。


**html = markdown.markdown(markdown_text)** ：这行代码使用 `markdown.markdown()` 函数将 Markdown 文本转换为 HTML 文本。


```
with open('example.html', 'w', encoding='utf-8') as file:
    file.write(html)
```


这段代码将转换后的 HTML 文本写入 `example.html` 文件中。


---


## 扩展功能


`markdown` 库支持多种扩展，例如表格、代码高亮等。你可以通过以下方式启用扩展：


```
html = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])
```


你可以根据需要自定义 HTML 输出的样式和结构。


通过 Python 将 Markdown 转换为 HTML 是一个简单而强大的工具，可以帮助你自动化文档生成过程。无论是编写博客、文档还是项目说明，这种方法都能大大提高你的工作效率。希望这篇文章能帮助你快速上手 Python 中的 Markdown 转换功能！


---


## 参考资源


- [Python Markdown 库官方文档](https://python-markdown.github.io/)
- [Markdown 教程](https://www.runoob.com/../markdown/md-tutorial.html)
- [Markdown 语法指南](https://www.markdownguide.org/)








	  AI 思考中...





			** [Python __name__ 与 __main__](https://www.runoob.com/python3-name-main.html)
			[Python sys 模块](https://www.runoob.com/python-sys.html) **













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