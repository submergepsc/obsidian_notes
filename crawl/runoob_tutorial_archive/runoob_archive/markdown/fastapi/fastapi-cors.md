# FastAPI CORS 跨域

- Source: https://www.runoob.com/fastapi/fastapi-cors.html

CORS（Cross-Origin Resource Sharing，跨域资源共享）是一种安全机制，允许或限制网页从不同域名请求资源。当前后端分离开发时，前端页面通常运行在不同的域名或端口上，需要配置 CORS 才能正常访问后端 API。


---


## 什么是跨域问题


浏览器的同源策略限制了网页向不同域名发送请求。例如：


| 前端地址 | 后端 API 地址 | 是否跨域 |
| --- | --- | --- |
| http://localhost:3000 | http://localhost:8000 | 跨域（端口不同） |
| http://example.com | http://api.example.com | 跨域（域名不同） |
| https://example.com | http://example.com | 跨域（协议不同） |
| http://example.com | http://example.com/api | 同源（相同域名、端口、协议） |


同源的三要素：**协议**、**域名**、**端口**，任一不同即为跨域。


---


## 配置 CORS


FastAPI 使用 Starlette 的 `CORSMiddleware` 来处理跨域：


## 实例


```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 配置 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=[               # 允许的源（域名列表）
        "http://localhost:3000",   # 前端开发服务器
        "http://localhost:8080",
    ],
    allow_credentials=True,       # 允许携带 Cookie
    allow_methods=["*"],          # 允许的 HTTP 方法
    allow_headers=["*"],          # 允许的请求头
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
```


---


## CORS 配置参数详解


| 参数 | 类型 | 说明 | 推荐值 |
| --- | --- | --- | --- |
| allow_origins | list[str] | 允许跨域的源列表 | 生产环境用具体域名 |
| allow_methods | list[str] | 允许的 HTTP 方法 | ["GET", "POST", "PUT", "DELETE"] |
| allow_headers | list[str] | 允许的请求头 | 按需配置 |
| allow_credentials | bool | 是否允许携带 Cookie 和认证信息 | 需要认证时设为 True |
| expose_headers | list[str] | 前端可以访问的响应头 | 按需配置 |
| max_age | int | 预检请求的缓存时间（秒） | 600 |


**
`allow_origins` 使用 `["*"]` 表示允许所有源，但这与 `allow_credentials=True` 不兼容。如果需要携带 Cookie，必须指定具体的源。


---


## 开发环境 vs 生产环境


### 开发环境


开发时为了方便，可以允许所有源：


## 实例


```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 开发环境：允许所有源（仅用于开发！）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # 允许所有源
    allow_credentials=True,
    allow_methods=["*"],         # 允许所有方法
    allow_headers=["*"],         # 允许所有请求头
)
```


### 生产环境


生产环境必须指定具体的源：


## 实例


```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 生产环境：只允许特定域名
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://example.com",           # 生产前端域名
        "https://www.example.com",       # 带 www 的域名
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
    max_age=600,                  # 预检请求缓存 10 分钟
)
```


> 在生产环境中使用 `allow_origins=["*"]` 是安全隐患，可能导致跨站请求伪造（CSRF）攻击。务必指定具体的前端域名。


---


## CORS 预检请求


浏览器在发送某些跨域请求前，会先发送一个 OPTIONS** 预检请求（preflight request），询问服务器是否允许实际请求。CORS 中间件会自动处理预检请求。


需要预检的请求条件：


- 使用了 `PUT`、`DELETE` 等非简单方法
- 请求头包含自定义字段（如 `Authorization`）
- `Content-Type` 不是 `application/x-www-form-urlencoded`、`multipart/form-data` 或 `text/plain`


**
设置了 `max_age` 后，浏览器会缓存预检结果，在指定时间内不会重复发送预检请求，减少网络开销。


---


## 小结


- CORS 是浏览器安全机制，前后端分离开发时必须配置
- 使用 `CORSMiddleware` 处理跨域请求
- 生产环境务必指定具体的 `allow_origins`，不要使用 `["*"]`
- `allow_credentials=True` 与 `allow_origins=["*"]` 不兼容
- CORS 中间件自动处理浏览器的 OPTIONS 预检请求









	  AI 思考中...





			** [FastAPI 中间件](https://www.runoob.com/fastapi-middleware.html)
			[FastAPI 静态文件](https://www.runoob.com/fastapi-static-files.html) **













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