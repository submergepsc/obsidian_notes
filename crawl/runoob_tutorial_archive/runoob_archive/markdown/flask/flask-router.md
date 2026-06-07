# Flask 路由

- Source: https://www.runoob.com/flask/flask-router.html

Flask 路由是 Web 应用程序中将 URL 映射到 Python 函数的机制。


Flask 路由是 Flask 应用的核心部分，用于处理不同 URL 的请求，并将请求的处理委托给相应的视图函数。


以下是关于 Flask 路由的详细说明，包括路由的定义、参数、方法和规则等。


- **定义路由**：使用 `@app.route('/path')` 装饰器定义 URL 和视图函数的映射。
- **路由参数**：通过动态部分在 URL 中传递参数。
- **路由规则**：使用类型转换器指定 URL 参数的类型。
- **请求方法**：指定允许的 HTTP 请求方法。
- **路由函数返回**：视图函数可以返回不同类型的响应。
- **静态文件和模板**：管理静态文件和动态渲染 HTML 模板。
- **路由优先级**：确保路由顺序正确，以避免意外的匹配结果。


### 1. 定义路由


基本路由定义：


## 实例


```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'
```


- `@app.route('/')`：装饰器，用于定义路由。`/` 表示根 URL。
- `def home()`：视图函数，当访问根 URL 时，返回 `'Welcome to the Home Page!'`。


### 2. 路由参数

路由可以包含动态部分，通过在路由中指定参数，可以将 URL 中的部分数据传递给视图函数。


## 实例


```python
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'
```


### 3. 路由规则

路由规则支持不同类型的参数和匹配规则。

类型规则：

- **字符串（默认）：** 匹配任意字符串。
- **整数（`*`）：** 匹配整数值。
- **浮点数（``）：** 匹配浮点数值。
- **路径（`
`）：** 匹配任意字符，包括斜杠 `/`。 ## 实例
```python
@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return f'User ID: {user_id}'

@app.route('/files/<path:filename>')
def serve_file(filename):
    return f'Serving file: {filename}'
```
 - `@app.route('/user/')`：匹配整数类型的 `user_id`。 - `@app.route('/files/')`：匹配包含斜杠的路径 `filename`。 ### 4. 请求方法 Flask 路由支持不同的 HTTP 请求方法，如 GET、POST、PUT、DELETE 等。可以通过 methods 参数指定允许的请求方法。


## 实例


```python
@app.route('/submit', methods=['POST'])
def submit():
    return 'Form submitted!'
```


### 5. 路由转换器

Flask 提供了一些内置的转换器，可以对 URL 中的参数进行特定类型的转换。

常用转换器：

- **`int`：** 匹配整数。
- **`float`：** 匹配浮点数。
- **`path`：** 匹配任意路径，包括斜杠。


## 实例


```python
@app.route('/items/<int:item_id>/details')
def item_details(item_id):
    return f'Item details for item ID: {item_id}'
```


- ``：将 URL 中的 `item_id` 转换为整数。


### 6. 路由函数返回

视图函数可以返回多种类型的响应：

- **字符串**：返回纯文本响应。
- **HTML**：返回 HTML 页面。
- **JSON**：返回 JSON 数据。
- **Response 对象**：自定义响应。


## 实例


```python
from flask import jsonify, Response

@app.route('/json')
def json_response():
    data = {'key': 'value'}
    return jsonify(data)

@app.route('/custom')
def custom_response():
    response = Response('Custom response with headers', status=200)
    response.headers['X-Custom-Header'] = 'Value'
    return response
```


- `jsonify(data)`：将字典转换为 JSON 响应。
- `Response('Custom response with headers', status=200)`：创建自定义响应对象。


### 7. 静态文件和模板

静态文件（如 CSS、JavaScript、图片）可以通过 static 路由访问。模板文件则通过 templates 文件夹组织，用于渲染 HTML 页面。


静态文件访问：


```
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```


## 实例


```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```


模板文件渲染：


## 实例


```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```


模板文件 (templates/hello.html)：


## 实例


```python
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```


### 8. 路由优先级

Flask 按照定义的顺序匹配路由，第一个匹配成功的路由将被处理。确保更具体的路由放在更一般的路由之前。


## 实例


```python
@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return f'User ID: {user_id}'

@app.route('/user')
def user_list():
    return 'User List'
```


- `/user/123` 将匹配到 `/user/`，而 `/user` 将匹配到 `user_list`。








	  AI 思考中...





			* [Flask 项目结构](https://www.runoob.com/flask-layout.html)
			[Flask 视图函数](https://www.runoob.com/flask-views-functions.html) **













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