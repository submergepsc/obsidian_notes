# FastAPI 请求体字段与嵌套模型

- Source: https://www.runoob.com/fastapi/fastapi-body-fields.html

在 Pydantic 模型内部，你可以使用 `Field` 为字段声明校验规则和元数据，也可以将模型嵌套使用来处理复杂的 JSON 数据结构。


---


## 使用 Field 声明字段校验


与路径操作函数中使用 `Query`、`Path` 声明校验的方式一样，Pydantic 模型内部使用 `Field` 声明字段校验：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100, description="商品名称")  # 必填，1-100字符
    description: str | None = Field(default=None, max_length=300, description="商品描述")  # 可选
    price: float = Field(gt=0, description="商品价格")  # 必填，必须大于 0
    tax: float | None = Field(default=None, ge=0, description="税费")  # 可选，>= 0

@app.post("/items/")
async def create_item(item: Item):
    return item
```


`Field` 支持的校验参数：


| 参数类型 | 参数 | 说明 |
| --- | --- | --- |
| 字符串校验 | min_length | 最小长度 |
| max_length | 最大长度 |  |
| pattern | 正则表达式匹配 |  |
| 数值校验 | gt | 大于 |
| ge | 大于等于 |  |
| lt | 小于 |  |
| le | 小于等于 |  |
| 元数据 | title | 字段标题 |
| description | 字段描述 |  |


**
注意 `Field` 从 `pydantic` 导入，而不是从 `fastapi` 导入。这与 `Query`、`Path` 等从 `fastapi` 导入不同。


---


## 列表类型字段


你可以将字段声明为列表，并指定元素类型：


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
    tags: list[str] = []  # 字符串列表，默认为空列表

@app.post("/items/")
async def create_item(item: Item):
    return item
```


请求体示例：


```
{
    "name": "Foo",
    "price": 42.0,
    "tags": ["rock", "metal", "bar"]
}
```


### 使用 Set 去重


如果标签不应重复，使用 `set` 类型：


## 实例


```python
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()  # 自动去除重复标签
```


即使请求中包含重复的标签，响应中也会自动去重。


---


## 嵌套模型


Pydantic 模型的字段类型可以是另一个 Pydantic 模型，支持任意深度的嵌套：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# 子模型：图片
class Image(BaseModel):
    url: HttpUrl      # 自动校验是否为有效的 URL
    name: str

# 主模型：商品，包含图片子模型
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None  # 可选的图片信息

@app.post("/items/")
async def create_item(item: Item):
    return item
```


对应的请求体结构：


```
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
```


---


## 列表中的子模型


可以将子模型放在列表中：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None  # 图片列表

@app.post("/items/")
async def create_item(item: Item):
    return item
```


对应的请求体：


```
{
    "name": "Foo",
    "price": 42.0,
    "images": [
        {"url": "http://example.com/baz.jpg", "name": "The Foo live"},
        {"url": "http://example.com/dave.jpg", "name": "The Baz"}
    ]
}
```


---


## 深度嵌套模型


你可以定义任意深度的嵌套结构：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]  # Offer 包含多个 Item，Item 又包含多个 Image

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer
```


---


## 纯列表请求体


如果请求体的最外层就是一个 JSON 数组，可以直接在函数参数中声明列表类型：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

# 请求体直接是一个 Image 列表
@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images
```


---


## 任意 dict 构成的请求体


当你需要接收键名不确定的字典数据时，可以声明 `dict` 类型的请求体：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

# 接收键为 int、值为 float 的字典
@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
```


请求体示例：


```
{
    "1": 0.5,
    "2": 1.5,
    "3": 2.0
}
```


> JSON 只支持字符串类型的键，但 Pydantic 会自动将字符串键转换为声明的类型（如本例中的 `int`）。


---


## 小结


- 使用 Pydantic 的 `Field` 为模型字段添加校验和元数据
- `list[str]`、`set[str]` 等集合类型可以声明列表/集合字段
- 模型可以嵌套使用，支持任意深度的 JSON 结构
- `HttpUrl` 等特殊类型自动校验格式
- 纯列表和任意字典也可以作为请求体类型









	  AI 思考中...





			** [FastAPI 路径参数数值校验](https://www.runoob.com/fastapi-path-params-validation.html)
			[FastAPI 响应模型](https://www.runoob.com/fastapi-response-model.html) **













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