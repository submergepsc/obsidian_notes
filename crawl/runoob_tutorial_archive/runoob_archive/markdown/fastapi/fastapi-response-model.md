# FastAPI 响应模型

- Source: https://www.runoob.com/fastapi/fastapi-response-model.html

响应模型用于声明 API 返回的数据结构。通过声明响应模型，FastAPI 会自动完成输出数据的校验、序列化和过滤，确保客户端只接收到预期的数据。


---


## 使用返回类型注解


最简单的方式是直接注解路径操作函数的返回类型：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    # 返回的数据会自动按照 Item 模型过滤和校验
    return {
        "name": "Foo",
        "description": "A very nice Item",
        "price": 22.2,
        "secret": "this should not be visible",  # 不在 Item 中的字段会被过滤
    }
```


FastAPI 使用响应模型完成以下工作：


| 功能 | 说明 |
| --- | --- |
| 数据校验 | 如果返回数据与模型不匹配，说明应用代码有问题 |
| 数据过滤 | 只返回模型中定义的字段，过滤掉多余字段（这对安全性很重要） |
| 生成文档 | 在 OpenAPI 文档中展示响应结构 |
| 序列化 | 使用 Pydantic（Rust 实现）高效地将数据转为 JSON |


---


## response_model 参数


当返回类型与响应模型不一致时，使用装饰器的 `response_model` 参数：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# 输入模型（包含密码）
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr

# 输出模型（不包含密码）
class UserOut(BaseModel):
    username: str
    email: EmailStr

# 函数接收 UserIn，但响应使用 UserOut
@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn):
    # 返回的 user 包含密码，但 response_model=UserOut 会过滤掉密码
    return user
```


**
这是保护敏感数据的重要手段。使用不同的输入和输出模型，确保密码等敏感字段永远不会出现在 API 响应中。


---


## 返回类型与数据过滤


推荐使用类继承来实现输入/输出模型的分离，这样既能让编辑器和 mypy 正确理解类型，又能让 FastAPI 过滤数据：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# 基础用户模型
class BaseUser(BaseModel):
    username: str
    email: EmailStr

# 输入模型：继承基础模型，新增密码字段
class UserIn(BaseUser):
    password: str

@app.post("/users/")
async def create_user(user: UserIn) -> BaseUser:
    # 返回类型注解为 BaseUser，FastAPI 会过滤掉 password 字段
    # 编辑器和 mypy 也满意，因为 UserIn 是 BaseUser 的子类
    return user
```


---


## 排除未设置的默认值


使用 `response_model_exclude_unset=True`，只返回实际设置了值的字段：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
```


不同 item_id 的响应对比：


| item_id | 响应 | 说明 |
| --- | --- | --- |
| foo | {"name": "Foo", "price": 50.2} | 只返回显式设置的字段，省略了默认值 |
| bar | {"name": "Bar", "description": "...", "price": 62, "tax": 20.2} | 所有字段都有实际值，全部返回 |


相关的过滤参数：


| 参数 | 说明 |
| --- | --- |
| response_model_exclude_unset | 排除未设置值的字段 |
| response_model_exclude_defaults | 排除值为默认值的字段 |
| response_model_exclude_none | 排除值为 None 的字段 |


---


## 包含/排除特定字段


使用 `response_model_include` 和 `response_model_exclude` 精确控制输出字段：


## 实例


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5

# 只包含 name 和 description
@app.get("/items/{item_id}", response_model=Item, response_model_include={"name", "description"})
async def read_item_name(item_id: str):
    return items[item_id]

# 排除 tax
@app.get("/items/{item_id}/no-tax", response_model=Item, response_model_exclude={"tax"})
async def read_item_no_tax(item_id: str):
    return items[item_id]
```


> 虽然 `response_model_include` 和 `response_model_exclude` 可以快速过滤字段，但推荐使用多个模型类来代替，因为它们无法从 OpenAPI 文档中移除被排除的字段。


---


## 小结


- 使用 `response_model` 参数或返回类型注解声明响应模型
- 响应模型的核心作用是数据过滤，保护敏感数据不被泄露
- 为输入和输出使用不同的模型，确保密码等字段不会出现在响应中
- `response_model_exclude_unset` 只返回实际设置的字段
- 推荐使用模型继承 + 返回类型注解，而非 `response_model_include/exclude`









	  AI 思考中...





			** [FastAPI 请求体字段与嵌套模型](https://www.runoob.com/fastapi-body-fields.html)
			[FastAPI 响应状态码](https://www.runoob.com/fastapi-status-code.html) **













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