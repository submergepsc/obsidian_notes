# FastAPI 第一个应用

- Source: https://www.runoob.com/fastapi/fastapi-step1.html

本节通过一个完整的示例，带你从零开始创建一个 FastAPI 应用，并理解其中每一行代码的含义。


---


## 最简应用


创建一个名为 **main.py** 的文件，添加以下代码：


## 实例


```python
from fastapi import FastAPI

# 步骤1：导入 FastAPI 类
# 步骤2：创建应用实例
app = FastAPI()

# 步骤3：定义路径操作装饰器
# 步骤4：定义路径操作函数
@app.get("/")
async def root():
    # 步骤5：返回响应内容
    return {"message": "Hello World"}
```


启动应用：


```
$ uvicorn main:app --reload
```


访问 **http://127.0.0.1:8000**，返回：


```
{"message": "Hello World"}
```


---


## 代码拆解


### 1. 导入 FastAPI


```
from fastapi import FastAPI
```


`FastAPI` 是 Python 类，为你的 API 提供所有核心功能。它直接继承自 Starlette，因此你也可以使用 Starlette 的所有功能。


### 2. 创建应用实例


```
app = FastAPI()
```


创建一个 FastAPI 实例，变量名通常用 `app`。这个实例是创建所有 API 的主要交互对象。与 Flask 不同，FastAPI 不需要传递 `__name__` 参数。


### 3. 定义路径操作装饰器


```
@app.get("/")
```


这行代码告诉 FastAPI：当用户通过 **GET** 方法访问根路径 **/** 时，执行下方函数。


其中涉及两个概念：


| 概念 | 说明 | 示例 |
| --- | --- | --- |
| 路径（Path） | URL 中从第一个 / 起的后半部分，也称为"端点"或"路由" | /items/foo |
| 操作（Operation） | HTTP 方法，对应不同的操作语义 | GET、POST、PUT、DELETE |


FastAPI 支持所有 HTTP 方法的装饰器：


| 装饰器 | HTTP 方法 | 常见用途 |
| --- | --- | --- |
| @app.get() | GET | 获取/读取数据 |
| @app.post() | POST | 创建新数据 |
| @app.put() | PUT | 完整更新数据 |
| @app.patch() | PATCH | 部分更新数据 |
| @app.delete() | DELETE | 删除数据 |


### 4. 定义路径操作函数


```
async def root():
```


这是路径操作函数，每当 FastAPI 接收到 `GET /` 请求时就会调用它。函数名可以随意取，但建议取有意义的名称。


**你可以使用 `async def` 或普通的 `def` 来定义函数。FastAPI 会自动处理两者的区别。如果你不熟悉异步编程，使用普通 `def` 即可，后续章节会详细介绍异步。


### 5. 返回响应内容


```
return {"message": "Hello World"}
```


函数返回一个字典，FastAPI 会自动将其转换为 JSON 格式响应。你可以返回 `dict`、`list`、`str`、`int` 等类型，FastAPI 都会自动处理 JSON 转换。


---


## 添加更多路由


接下来我们添加路径参数和查询参数，丰富应用功能：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """根路径，返回欢迎信息"""
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    """根据 ID 获取条目，支持可选的查询参数 q"""
    return {"item_id": item_id, "q": q}
```


新增路由的参数说明：


| 参数 | 类型 | 来源 | 说明 |
| --- | --- | --- | --- |
| item_id | int | 路径参数 | 从 URL 路径中获取，FastAPI 自动将字符串转为整数 |
| q | str \| None | 查询参数 | 从 URL 的 ?q=xxx 部分获取，默认值为 None，表示可选 |


访问测试：


```
# 访问根路径
GET http://127.0.0.1:8000/
响应: {"message": "Hello World"}

# 访问带路径参数的路由
GET http://127.0.0.1:8000/items/5
响应: {"item_id": 5, "q": null}

# 同时传递路径参数和查询参数
GET http://127.0.0.1:8000/items/5?q=runoob
响应: {"item_id": 5, "q": "runoob"}
```


注意 `item_id` 的值是整数 `5` 而不是字符串 `"5"`，这就是 FastAPI 类型声明的数据转换功能。如果传入非整数（如 `/items/foo`），FastAPI 会返回清晰的校验错误信息。


---


## 添加 POST 请求


下面我们添加一个使用请求体的 POST 路由：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义请求体数据模型
class Item(BaseModel):
    name: str           # 必填：商品名称
    description: str | None = None  # 可选：商品描述
    price: float        # 必填：商品价格
    tax: float | None = None        # 可选：税费

@app.post("/items/")
async def create_item(item: Item):
    """创建新商品，接收 JSON 请求体"""
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """更新指定商品，同时使用路径参数和请求体"""
    return {"item_id": item_id, "item_name": item.name}
```


这里使用了 Pydantic 的 `BaseModel` 来定义请求体的结构。FastAPI 会自动：


- 将请求中的 JSON 数据解析为 `Item` 对象
- 校验数据类型和必填字段
- 在 API 文档中展示请求体结构


> Pydantic 是 FastAPI 的核心依赖，用于数据校验和序列化。后续章节会详细介绍它的用法。


---


## FastAPI 参数识别规则


FastAPI 通过以下规则自动识别参数来源：


| 参数来源 | 识别条件 | 示例 |
| --- | --- | --- |
| 路径参数 | 参数名出现在路由路径的 {} 中 | item_id 在 /items/{item_id} 中 |
| 查询参数 | 参数是单一类型（int、str、bool 等） | q: str \| None = None |
| 请求体 | 参数类型是 Pydantic 模型 | item: Item |


你可以在同一个函数中混合使用这三种参数，FastAPI 会自动从正确的位置获取数据。


---


## 小结


创建 FastAPI 应用的核心步骤：


- 导入 `FastAPI`
- 创建应用实例 `app = FastAPI()`
- 使用装饰器（如 `@app.get()`）定义路径操作
- 定义路径操作函数，使用类型注解声明参数
- 使用 `uvicorn main:app --reload` 运行开发服务器









	  AI 思考中...





			** [FastAPI 安装](https://www.runoob.com/fastapi-install.html)
			[FastAPI 交互式 API 文档](https://www.runoob.com/fastapi-api-doc.html) **













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