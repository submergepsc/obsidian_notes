# Flask 视图函数

- Source: https://www.runoob.com/flask/flask-views-functions.html

视图函数是 Flask 应用中的核心部分，它负责处理请求并生成响应。

视图函数与路由紧密结合，通过路由将 URL 映射到具体的视图函数。

以下是对 Flask 视图函数的详细说明，包括如何定义、使用请求数据、返回响应、以及如何处理错误等。


- **定义视图函数**：视图函数是处理请求并返回响应的核心功能。
- **接收请求数据**：使用 `request` 对象获取 URL 参数、表单数据、查询参数等。
- **返回响应**：可以返回字符串、HTML、JSON 或自定义响应对象。
- **处理请求和响应**：使用 `request` 对象和 `make_response` 来处理请求和生成自定义响应。
- **处理错误**：视图函数内处理异常或使用 Flask 的错误处理机制。
- **视图函数的装饰器**：使用 `@app.before_request`、`@app.after_request` 等装饰器处理请求前后逻辑。
- **视图函数返回的状态码**：可以指定 HTTP 状态码来表示请求的处理结果。


### 1. 定义视图函数

视图函数是一个普通的 Python 函数，它接收请求并返回响应。视图函数通常与路由配合使用，通过装饰器将 URL 映射到视图函数。


## 实例


```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
```


- `@app.route('/')`：将根 URL `/` 映射到 `home` 视图函数。 - `def home()`：视图函数，返回字符串 `'Hello, World!'` 作为响应。 ### 2. 接收请求数据 视图函数可以接收不同类型的请求数据，包括 URL 参数、表单数据、查询参数等。


获取 URL 参数：


## 实例


```python
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'
```


- `` 是一个 URL 参数，传递到视图函数 `greet`。

获取表单数据：


## 实例


```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return f'Form submitted by {username}!'
```


**request.form.get('username')**：获取 POST 请求中表单数据的 username 字段。


获取查询参数：


## 实例


```python
@app.route('/search')
def search():
    query = request.args.get('query')
    return f'Search results for: {query}'
```


**request.args.get('query')**：获取 GET 请求中的查询参数 query。


### 3. 返回响应

视图函数可以返回多种类型的响应，包括字符串、HTML、JSON、或自定义响应对象。


返回字符串：


## 实例


```python
@app.route('/message')
def message():
    return 'This is a simple message.'
```


返回 HTML 模板：


## 实例


```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```


**render_template('hello.html', name=name)**：渲染 HTML 模板 hello.html，并将 name 变量传递给模板。


返回 JSON 数据：


## 实例


```python
from flask import jsonify

@app.route('/api/data')
def api_data():
    data = {'key': 'value'}
    return jsonify(data)
```


**jsonify(data)**：将 Python 字典转换为 JSON 响应。


返回自定义响应对象：


## 实例


```python
from flask import Response

@app.route('/custom')
def custom_response():
    response = Response('Custom response with headers', status=200)
    response.headers['X-Custom-Header'] = 'Value'
    return response
```


**Response('Custom response with headers', status=200)**：创建自定义响应对象，并设置响应头。


### 4. 处理请求和响应

视图函数可以访问请求对象，并根据请求数据生成响应。可以使用 request 对象来获取请求的信息，使用 make_response 来创建自定义响应。


使用 request 对象：


## 实例


```python
from flask import request

@app.route('/info')
def info():
    user_agent = request.headers.get('User-Agent')
    return f'Your user agent is {user_agent}'
```


**request.headers.get('User-Agent')**：获取请求头中的 User-Agent 信息。


使用 make_response：


## 实例


```python
from flask import make_response

@app.route('/header')
def custom_header():
    response = make_response('Response with custom header')
    response.headers['X-Custom-Header'] = 'Value'
    return response
```


**make_response('Response with custom header')**：创建响应对象并设置自定义头信息。


### 5. 处理错误

可以在视图函数中处理异常或错误，或者通过 Flask 提供的错误处理机制来处理应用中的错误。


在视图函数中处理错误：


## 实例


```python
@app.route('/divide/<int:x>/<int:y>')
def divide(x, y):
    try:
        result = x / y
        return f'Result: {result}'
    except ZeroDivisionError:
        return 'Error: Division by zero', 400
```


使用 try-except 语句处理除零错误，并返回自定义错误消息和状态码。

全局错误处理：


## 实例


```python
@app.errorhandler(404)
def not_found(error):
    return 'Page not found', 404
```


**@app.errorhandler(404)**：定义处理 404 错误的函数。


### 6. 视图函数的装饰器

除了 @app.route，Flask 还支持其他装饰器，用于实现更复杂的功能。


示例：


- **`@app.before_request`**：在每个请求处理之前运行的函数。
- **`@app.after_request`**：在每个请求处理之后运行的函数。
- **`@app.teardown_request`**：在请求结束后运行的函数，用于清理工作。


示例装饰器使用：


## 实例


```python
@app.before_request
def before_request():
    print('Before request')

@app.after_request
def after_request(response):
    print('After request')
    return response

@app.teardown_request
def teardown_request(exception):
    print('Teardown request')
```


### 7. 视图函数返回的状态码

视图函数不仅可以返回内容，还可以指定 HTTP 状态码。


## 实例


```python
@app.route('/status')
def status():
    return 'Everything is OK', 200
```


返回状态码 200 表示请求成功。

返回带有状态码的响应对象：


## 实例


```python
from flask import Response

@app.route('/error')
def error():
    return Response('An error occurred', status=500)
```


返回状态码 500 表示服务器内部错误。








	  AI 思考中...





			** [Flask 路由](https://www.runoob.com/flask-router.html)
			[Flask 模板渲染](https://www.runoob.com/flask-templates.html) **













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