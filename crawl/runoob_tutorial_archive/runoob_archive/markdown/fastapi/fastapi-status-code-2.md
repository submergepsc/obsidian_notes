# FastAPI 响应状态码

- Source: https://www.runoob.com/fastapi/fastapi-status-code-2.html

HTTP 状态码是响应的一部分，用于告知客户端请求的处理结果。FastAPI 允许你在路径操作装饰器中声明默认的状态码，也可以在函数中动态修改。


---


## 声明状态码


使用 `status_code` 参数在装饰器中声明响应状态码：


## 实例


```python
from fastapi import FastAPI, status

app = FastAPI()

# 创建资源时，使用 201 状态码
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
```


**
`status_code` 是装饰器方法的参数（如 `@app.post()`），不是路径操作函数的参数。它可以是数字（如 `201`），也可以使用 `fastapi.status` 中的常量（推荐，有编辑器自动补全支持）。


---


## HTTP 状态码速查


| 范围 | 类别 | 常用状态码 | 含义 |
| --- | --- | --- | --- |
| 1xx | 信息 | -- | 很少直接使用 |
| 2xx | 成功 | 200 OK | 请求成功（默认状态码） |
| 201 Created | 资源创建成功 |  |  |
| 204 No Content | 成功但无内容返回 |  |  |
| 3xx | 重定向 | 304 Not Modified | 资源未修改（缓存有效） |
| 4xx | 客户端错误 | 400 Bad Request | 请求格式错误 |
| 401 Unauthorized | 未认证 |  |  |
| 403 Forbidden | 已认证但无权限 |  |  |
| 404 Not Found | 资源不存在 |  |  |
| 5xx | 服务器错误 | 500 Internal Server Error | 服务器内部错误 |


---


## 使用 status 常量


`fastapi.status` 提供了所有 HTTP 状态码的常量，配合编辑器自动补全使用更方便：


## 实例


```python
from fastapi import FastAPI, status

app = FastAPI()

# POST - 创建资源，返回 201
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}

# DELETE - 删除资源，返回 204（无内容）
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    # 删除操作通常不返回内容
    pass

# GET - 获取资源，返回 200（默认）
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```


> `204 No Content` 表示成功但没有内容返回，适用于删除操作。注意 204 响应不能包含响应体。


---


## 常用状态码常量


| 常量 | 值 | 使用场景 |
| --- | --- | --- |
| status.HTTP_200_OK | 200 | GET 请求成功（默认） |
| status.HTTP_201_CREATED | 201 | POST 创建资源成功 |
| status.HTTP_204_NO_CONTENT | 204 | DELETE 成功，无返回内容 |
| status.HTTP_400_BAD_REQUEST | 400 | 请求参数错误 |
| status.HTTP_401_UNAUTHORIZED | 401 | 未登录或 token 无效 |
| status.HTTP_403_FORBIDDEN | 403 | 无权限访问 |
| status.HTTP_404_NOT_FOUND | 404 | 资源不存在 |
| status.HTTP_409_CONFLICT | 409 | 资源冲突（如重复创建） |
| status.HTTP_422_UNPROCESSABLE_ENTITY | 422 | 数据校验失败 |
| status.HTTP_500_INTERNAL_SERVER_ERROR | 500 | 服务器内部错误 |


---


## 小结


- 使用装饰器的 `status_code` 参数声明默认状态码
- 推荐使用 `fastapi.status` 常量，有编辑器自动补全支持
- POST 创建资源用 201，DELETE 删除资源用 204，GET 获取资源用 200
- 4xx 表示客户端错误，5xx 表示服务器错误









	  AI 思考中...





			** [FastAPI 响应状态码](https://www.runoob.com/fastapi-status-code.html)
			[FastAPI 文件上传](https://www.runoob.com/fastapi-file-upload.html) **













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