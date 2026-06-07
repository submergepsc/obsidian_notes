# FastAPI 请求头与 Cookie

- Source: https://www.runoob.com/fastapi/fastapi-header-cookie.html

FastAPI 提供了 `Header` 和 `Cookie` 类型，用于从 HTTP 请求头和 Cookie 中获取数据。


---


## 请求头参数


使用 `Header` 声明请求头参数：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(
    # 接收 User-Agent 请求头
    user_agent: Annotated[str | None, Header()] = None,
):
    return {"User-Agent": user_agent}
```


访问 **http://127.0.0.1:8000/items/**，返回的 JSON 中包含浏览器的 User-Agent 信息。


---


## 请求头的自动转换


HTTP 请求头中的字段名使用连字符（如 `X-Token`），而 Python 变量名不能包含连字符。FastAPI 会自动进行转换：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(
    # Python 变量名用下划线，FastAPI 自动转换为 X-Token 请求头
    x_token: Annotated[list[str] | None, Header()] = None,
):
    return {"X-Token values": x_token}
```


转换规则：


| Python 变量名 | HTTP 请求头 | 说明 |
| --- | --- | --- |
| x_token | X-Token | 下划线自动转为连字符 |
| user_agent | User-Agent | 同上 |
| content_type | Content-Type | 同上 |


**
FastAPI 自动将变量名中的下划线 `_` 转换为连字符 `-` 来匹配请求头。如果你需要禁用此转换，设置 `Header(convert_underscores=False)`。


---


## 接收重复的请求头


有些请求头可能出现多次（如 `Set-Cookie`），使用 `list` 类型接收：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(
    # 接收多个 X-Token 请求头
    x_token: Annotated[list[str] | None, Header()] = None,
):
    return {"X-Token values": x_token}
```


请求示例：


```
GET /items/ HTTP/1.1
X-Token: foo
X-Token: bar
```


响应：`{"X-Token values": ["foo", "bar"]}`


---


## Cookie 参数


使用 `Cookie` 声明 Cookie 参数：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get("/items/")
async def read_items(
    # 接收名为 session_token 的 Cookie
    session_token: Annotated[str | None, Cookie()] = None,
):
    return {"session_token": session_token}
```


---


## 请求头与 Cookie 同时使用


可以在同一个路由中同时获取请求头和 Cookie：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Header, Cookie

app = FastAPI()

@app.get("/items/")
async def read_items(
    user_agent: Annotated[str | None, Header()] = None,
    session_token: Annotated[str | None, Cookie()] = None,
    ads_id: Annotated[str | None, Cookie()] = None,
):
    return {
        "User-Agent": user_agent,
        "Session-Token": session_token,
        "Ads-ID": ads_id,
    }
```


![](https://www.runoob.com/wp-content/uploads/2023/12/2b6c7d84b40b515a8a9e19c59406a283.png)


---


## 小结


- 使用 `Header` 获取 HTTP 请求头参数
- 使用 `Cookie` 获取 Cookie 参数
- FastAPI 自动将 Python 变量名中的下划线转为请求头中的连字符
- 使用 `list[str]` 接收重复的请求头
- 请求头和 Cookie 参数支持与查询参数相同的校验规则









	  AI 思考中...





			** [FastAPI 文件上传](https://www.runoob.com/fastapi-file-upload.html)
			[FastAPI 错误处理](https://www.runoob.com/fastapi-error-handling.html) **













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