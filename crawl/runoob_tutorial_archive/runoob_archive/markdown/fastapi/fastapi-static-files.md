# FastAPI 静态文件

- Source: https://www.runoob.com/fastapi/fastapi-static-files.html

FastAPI 可以方便地提供静态文件服务（如图片、CSS、JavaScript 文件），使用 Starlette 的 `StaticFiles` 实现。


---


## 安装依赖


`StaticFiles` 包含在 `aiofiles` 中，需要安装：


```
pip install aiofiles
```


---


## 挂载静态文件目录


使用 `app.mount()` 将静态文件目录挂载到应用上：


## 实例


```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 挂载静态文件目录
# "/static" 是 URL 路径前缀
# directory="static" 是本地目录名
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}
```


代码说明：


| 参数 | 说明 |
| --- | --- |
| "/static" | URL 路径前缀，如访问 /static/logo.png |
| directory="static" | 本地目录名，存放静态文件的文件夹 |
| name="static" | 内部使用的名称，用于生成 URL（通过 url_for） |


**
`mount` 是将一个独立的"子应用"挂载到指定路径上。`StaticFiles` 本身就是一个 ASGI 应用，它负责处理静态文件请求。挂载后，所有以 `/static` 开头的请求都由 `StaticFiles` 处理，不会经过 FastAPI 的路由系统。


---


## 目录结构示例


```
project/
├── main.py
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    └── images/
        └── logo.png
```


访问方式：


| 文件路径 | URL |
| --- | --- |
| static/css/style.css | http://127.0.0.1:8000/static/css/style.css |
| static/js/app.js | http://127.0.0.1:8000/static/js/app.js |
| static/images/logo.png | http://127.0.0.1:8000/static/images/logo.png |


---


## HTML 模板渲染


FastAPI 支持 Jinja2 模板引擎，可以动态渲染 HTML 页面：


## 实例


```python
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 配置模板目录
templates = Jinja2Templates(directory="templates")

@app.get("/hello/{name}")
async def hello(request: Request, name: str):
    # 渲染模板并传递上下文变量
    return templates.TemplateResponse(
        "hello.html",
        {"request": request, "name": name}
    )
```


模板文件 `templates/hello.html`：


## 实例


```python
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <img src="/static/images/logo.png" alt="Logo">
</body>
</html>
```


> 模板渲染时，必须传递 `request` 对象，因为模板中可能需要使用请求上下文（如生成 URL 等）。


---


## 小结


- 使用 `StaticFiles` 提供静态文件服务
- 使用 `app.mount()` 挂载静态文件目录到指定路径
- 挂载后的静态文件路径不受 FastAPI 路由系统管理
- 配合 Jinja2 模板引擎可以实现 HTML 页面渲染
- 静态文件适合存放 CSS、JS、图片等不会动态变化的资源









	  AI 思考中...





			** [FastAPI CORS 跨域](https://www.runoob.com/fastapi-cors.html)
			[FastAPI 安全认证](https://www.runoob.com/fastapi-security.html) **













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