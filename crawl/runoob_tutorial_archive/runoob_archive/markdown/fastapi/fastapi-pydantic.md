# FastAPI Pydantic 模型

- Source: https://www.runoob.com/fastapi/fastapi-pydantic.html

Pydantic 是 FastAPI 的核心依赖，用于数据校验和序列化。它让你使用标准的 Python 类型注解来定义数据模型，自动完成数据校验、类型转换和文档生成。


---


## Pydantic 是什么


Pydantic 是一个 Python 数据校验库，它的核心思想是：**用 Python 类型注解定义数据结构，Pydantic 自动负责校验和转换**。在 FastAPI 中，Pydantic 主要用于：


| 用途 | 说明 |
| --- | --- |
| 请求体校验 | 自动校验客户端发送的 JSON 数据是否符合模型定义 |
| 响应体序列化 | 将模型数据自动转换为 JSON 响应 |
| 自动文档 | 模型的字段、类型和校验规则自动出现在 API 文档中 |
| 编辑器支持 | 模型属性在编辑器中获得完整的自动补全 |


---


## 定义 Pydantic 模型


创建一个继承 `BaseModel` 的类，使用 Python 标准类型声明字段：


## 实例


```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str               # 必填：商品名称
    description: str | None = None  # 可选：商品描述
    price: float            # 必填：商品价格
    tax: float | None = None        # 可选：税费
```


字段是否必填取决于是否有默认值：


| 字段 | 声明方式 | 是否必填 |
| --- | --- | --- |
| name | name: str | 必填 |
| description | description: str \| None = None | 可选 |
| price | price: float | 必填 |
| tax | tax: float \| None = None | 可选 |


---


## 使用 Pydantic 模型


### 作为请求体


最常见的用法是将模型声明为路径操作函数的参数：


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
    # FastAPI 自动校验请求体，校验通过后赋值给 item 参数
    return item
```


### 访问和操作模型数据


## 实例


```python
@app.post("/items/")
async def create_item(item: Item):
    # 访问模型属性
    print(item.name)       # 直接访问属性
    print(item.price)      # 编辑器提供自动补全

    # 序列化为字典
    item_dict = item.model_dump()
    print(item_dict)       # {"name": "Foo", "description": None, "price": 45.2, "tax": None}

    # 序列化为 JSON 字符串
    item_json = item.model_dump_json()
    print(item_json)       # '{"name":"Foo","description":null,"price":45.2,"tax":null}'

    return item_dict
```


**
Pydantic v2 使用 `model_dump()` 和 `model_dump_json()` 替代了 v1 的 `dict()` 和 `json()` 方法。新方法性能更好（底层使用 Rust 实现）。


---


## 模型校验示例


当客户端发送的数据不符合模型定义时，FastAPI 会返回详细的校验错误：


## 实例


```python
# 客户端发送了缺少必填字段的数据
POST /items/
{
    "description": "缺少 name 和 price"
}

# FastAPI 返回校验错误
{
    "detail": [
        {
            "type": "missing",
            "loc": ["body", "name"],
            "msg": "Field required",
            "input": {"description": "缺少 name 和 price"}
        },
        {
            "type": "missing",
            "loc": ["body", "price"],
            "msg": "Field required",
            "input": {"description": "缺少 name 和 price"}
        }
    ]
}
```


如果发送了类型错误的数据：


```
// price 应该是数字，但传了字符串
{
    "name": "Foo",
    "price": "not a number"
}

// FastAPI 返回的错误
{
    "detail": [
        {
            "type": "float_parsing",
            "loc": ["body", "price"],
            "msg": "Input should be a valid number, unable to parse string as a number",
            "input": "not a number"
        }
    ]
}
```


---


## Pydantic v2 常用方法


| 方法 | v2（推荐） | v1（已弃用） | 说明 |
| --- | --- | --- | --- |
| 序列化为字典 | item.model_dump() | item.dict() | 将模型转为 Python 字典 |
| 序列化为 JSON | item.model_dump_json() | item.json() | 将模型转为 JSON 字符串 |
| 从字典创建 | Item.model_validate(data) | Item.parse_obj(data) | 从字典创建并校验模型 |
| 从 JSON 创建 | Item.model_validate_json(json_str) | Item.parse_raw(json_str) | 从 JSON 字符串创建模型 |
| 获取 JSON Schema | Item.model_json_schema() | Item.schema() | 获取模型的 JSON Schema |


---


## 模型配置（model_config）


Pydantic v2 使用 `model_config` 替代了 v1 的 `Config` 内部类：


## 实例


```python
from pydantic import BaseModel, ConfigDict

class Item(BaseModel):
    name: str
    price: float

    # Pydantic v2 的配置方式
    model_config = ConfigDict(
        json_schema_extra={  # 在 API 文档中显示示例
            "examples": [
                {
                    "name": "Foo",
                    "price": 35.4
                }
            ]
        }
    )
```


> Pydantic v2 中，`orm_mode = True` 已改为 `from_attributes = True`，`schema_extra` 已改为 `json_schema_extra`，`allow_population_by_field_name` 已改为 `populate_by_name`。


---


## 模型继承


Pydantic 模型支持继承，可以方便地创建输入模型和输出模型：


## 实例


```python
from pydantic import BaseModel, EmailStr

# 基础模型
class UserBase(BaseModel):
    username: str       # 必填
    email: EmailStr     # 必填，自动校验邮箱格式
    full_name: str | None = None  # 可选

# 创建用户时的输入模型（包含密码）
class UserCreate(UserBase):
    password: str       # 必填

# 返回用户信息时的输出模型（不包含密码）
class UserOut(UserBase):
    id: int             # 由服务器生成

# 使用示例
@app.post("/users/", response_model=UserOut)
async def create_user(user: UserCreate):
    # 函数接收 UserCreate（含密码），但响应使用 UserOut（不含密码）
    # 这样密码就不会出现在 API 响应中
    return {"id": 1, **user.model_dump(exclude={"password"})}
```


> 使用不同的输入和输出模型是保护敏感数据的重要手段。永远不要在 API 响应中返回密码等敏感字段。


---


## 小结


Pydantic 模型的核心要点：


- 使用 `BaseModel` 定义数据模型，标准 Python 类型声明字段
- 有默认值的字段可选，没有默认值的字段必填
- v2 使用 `model_dump()`、`model_validate()` 等新方法
- 通过模型继承创建不同的输入/输出模型，保护敏感数据
- 所有校验和文档都是自动的，只需声明一次类型









	  AI 思考中...





			** [FastAPI 基本路由](https://www.runoob.com/fastapi-route.html)
			[FastAPI 请求和响应](https://www.runoob.com/fastapi-request-response.html) **













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