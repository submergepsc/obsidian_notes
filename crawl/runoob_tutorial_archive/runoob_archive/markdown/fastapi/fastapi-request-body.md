# FastAPI 请求体

- Source: https://www.runoob.com/fastapi/fastapi-request-body.html

请求体是客户端发送给 API 的数据。当你需要从客户端接收 JSON 数据时，使用请求体来传递。FastAPI 使用 Pydantic 模型来声明请求体的结构，自动完成数据校验、转换和文档生成。


---


## 请求体与查询参数的区别


| 数据传递方式 | 位置 | 适用场景 | HTTP 方法 |
| --- | --- | --- | --- |
| 路径参数 | URL 路径 /items/5 | 标识资源 | GET、PUT、DELETE 等 |
| 查询参数 | URL 中 ?key=value | 筛选、分页等可选参数 | 主要是 GET |
| 请求体 | 请求的 JSON 数据 | 提交复杂数据 | POST、PUT、PATCH |


**
发送数据应使用 `POST`（最常见）、`PUT`、`DELETE` 或 `PATCH`。虽然 FastAPI 技术上支持 GET 请求携带请求体，但这不符合 HTTP 规范，Swagger UI 也不会为 GET 请求显示请求体文档。


---


## 使用 Pydantic 模型声明请求体


### 1. 导入 BaseModel


```
from pydantic import BaseModel
```


### 2. 创建数据模型


定义一个继承 `BaseModel` 的类，使用 Python 标准类型声明所有属性：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义请求体数据模型
class Item(BaseModel):
    name: str               # 必填：商品名称
    description: str | None = None  # 可选：商品描述
    price: float            # 必填：商品价格
    tax: float | None = None        # 可选：税费

@app.post("/items/")
async def create_item(item: Item):
    return item
```


属性是否必填的规则与查询参数相同：


- 有默认值的属性是可选的（如 `description`、`tax`）
- 没有默认值的属性是必填的（如 `name`、`price`）


以下 JSON 都是有效的请求体：


```
// 包含所有字段
{
    "name": "Foo",
    "description": "可选描述",
    "price": 45.2,
    "tax": 3.5
}

// 省略可选字段
{
    "name": "Foo",
    "price": 45.2
}
```


---


## FastAPI 对请求体的处理


仅通过 Python 类型声明，FastAPI 就能自动完成以下工作：


| 功能 | 说明 |
| --- | --- |
| 读取请求体 | 以 JSON 格式读取请求中的数据 |
| 类型转换 | 将数据转换为声明的类型（如字符串转浮点数） |
| 数据校验 | 校验数据有效性，无效时返回清晰的错误信息 |
| 赋值参数 | 将校验后的数据赋值给函数参数，获得编辑器自动补全 |
| 生成文档 | 自动生成 JSON Schema，出现在 API 文档中 |


---


## 使用模型属性


在路径操作函数内部，你可以像操作普通 Python 对象一样访问模型的所有属性：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    # 直接访问模型属性
    item_dict = item.model_dump()  # Pydantic v2 的序列化方法
    if item.tax:
        # 计算含税价格
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
```


> Pydantic v2 使用 `model_dump()` 替代了 v1 的 `dict()` 方法来序列化模型数据。`model_dump()` 返回一个包含模型所有字段的字典。


---


## 请求体 + 路径参数


可以同时声明路径参数和请求体，FastAPI 会自动从正确的位置获取数据：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# 同时使用路径参数和请求体
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}
```


FastAPI 识别规则：


- `item_id` 在路径 `{item_id}` 中出现 -> 路径参数
- `item` 的类型是 Pydantic 模型 -> 请求体


---


## 请求体 + 路径参数 + 查询参数


三者可以同时使用：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# 同时使用路径参数、查询参数和请求体
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
```


FastAPI 的完整参数识别规则：


| 识别条件 | 参数来源 |
| --- | --- |
| 参数名在路径的 {} 中声明 | 路径参数 |
| 参数是单一类型（int、str、bool 等） | 查询参数 |
| 参数类型是 Pydantic 模型 | 请求体 |


---


## 小结


请求体的核心要点：


- 使用 Pydantic 的 `BaseModel` 定义请求体结构
- 有默认值的字段可选，没有默认值的字段必填
- 请求体可以与路径参数和查询参数同时使用
- FastAPI 自动完成数据校验、类型转换和文档生成
- Pydantic v2 使用 `model_dump()` 进行序列化









	  AI 思考中...





			** [FastAPI 查询参数](https://www.runoob.com/fastapi-query-params.html)
			[FastAPI 查询参数校验](https://www.runoob.com/fastapi-query-params-validation.html) **













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