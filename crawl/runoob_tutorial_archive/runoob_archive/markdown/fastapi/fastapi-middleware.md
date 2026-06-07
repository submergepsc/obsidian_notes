# FastAPI 中间件

- Source: https://www.runoob.com/fastapi/fastapi-middleware.html

中间件是一种在每个请求到达路由处理函数之前和之后执行的函数。它可以用于添加日志、修改请求/响应、处理 CORS 等通用逻辑。


---


## 中间件的工作原理


中间件的执行流程：


- 请求到达中间件
- 中间件执行预处理逻辑
- 中间件将请求传递给下一个中间件或路由函数
- 路由函数返回响应
- 中间件执行后处理逻辑
- 响应返回给客户端


---


## 创建中间件


使用 `@app.middleware("http")` 装饰器创建中间件：


## 实例


```python
import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # 1. 请求前的处理：记录开始时间
    start_time = time.time()

    # 2. 将请求传递给下一个中间件或路由函数
    response = await call_next(request)

    # 3. 响应后的处理：计算处理时间并添加响应头
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}
```


代码说明：


| 部分 | 说明 |
| --- | --- |
| @app.middleware("http") | 声明这是一个 HTTP 中间件 |
| request: Request | 当前请求对象 |
| call_next | 调用下一个中间件或路由函数的回调 |
| await call_next(request) | 将请求传递给下一层，获取响应 |


**
`call_next` 接收 `request` 参数并返回 `response`。你可以在调用 `call_next` 之前修改请求，在调用之后修改响应。


---


## 请求日志中间件


以下中间件记录每个请求的基本信息：


## 实例


```python
import time
import logging
from fastapi import FastAPI, Request

app = FastAPI()

logger = logging.getLogger("uvicorn.access")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    # 记录请求信息
    logger.info(f"请求: {request.method} {request.url}")

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    # 记录响应信息
    logger.info(
        f"响应: {request.method} {request.url} "
        f"状态码={response.status_code} 耗时={process_time:.3f}s"
    )

    return response
```


---


## 中间件的执行顺序


中间件按照注册顺序执行，请求按正序经过中间件，响应按反序经过中间件：


```
请求 -> 中间件A(前) -> 中间件B(前) -> 路由函数
响应 <- 中间件A(后) <- 中间件B(后) <- 路由函数
```


> 中间件的注册顺序很重要。如果你有两个中间件 A 和 B，先注册 A，则请求先经过 A 再经过 B，但响应先经过 B 再经过 A。


---


## 使用 Starlette 内置中间件


FastAPI 继承自 Starlette，可以直接使用 Starlette 提供的中间件：


## 实例


```python
from fastapi import FastAPI
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

# 强制 HTTPS 重定向
app.add_middleware(HTTPSRedirectMiddleware)

@app.get("/")
async def root():
    return {"message": "使用 HTTPS 访问"}
```


常用的内置中间件：


| 中间件 | 说明 |
| --- | --- |
| HTTPSRedirectMiddleware | 强制将 HTTP 请求重定向为 HTTPS |
| TrustedHostMiddleware | 限制允许访问的主机名 |
| GZipMiddleware | 自动压缩响应内容 |
| CORSMiddleware | 处理跨域请求（下一章详细介绍） |


---


## GZip 压缩中间件


启用 GZip 压缩可以减少响应体积，提升传输速度：


## 实例


```python
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

# 当响应大小超过 1000 字节时自动压缩
app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.get("/")
async def root():
    return {"message": "这个响应可能会被 GZip 压缩"}
```


---


## 小结


- 中间件在请求/响应的处理链中执行通用逻辑
- 使用 `@app.middleware("http")` 创建自定义中间件
- `call_next(request)` 将请求传递给下一层
- 中间件按注册顺序执行（请求正序，响应反序）
- FastAPI/Starlette 提供了 CORS、GZip、HTTPS 重定向等内置中间件









	  AI 思考中...





			** [FastAPI 错误处理](https://www.runoob.com/fastapi-error-handling.html)
			[FastAPI CORS 跨域](https://www.runoob.com/fastapi-cors.html) **













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