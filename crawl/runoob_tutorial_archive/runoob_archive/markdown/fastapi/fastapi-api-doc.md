# FastAPI 交互式 API 文档

- Source: https://www.runoob.com/fastapi/fastapi-api-doc.html

FastAPI 基于代码中的类型注解自动生成交互式 API 文档，默认提供 Swagger UI 和 ReDoc 两种界面。开发者可以直接在文档中测试 API，无需额外的工具。


---


## 访问 API 文档


运行 FastAPI 应用后，访问以下地址查看文档：


| 地址 | 文档类型 | 特点 |
| --- | --- | --- |
| http://127.0.0.1:8000/docs | Swagger UI | 可交互测试，点击"Try it out"即可发送请求 |
| http://127.0.0.1:8000/redoc | ReDoc | 阅读体验好，适合浏览和查阅 API 定义 |
| http://127.0.0.1:8000/openapi.json | OpenAPI JSON | 原始的 OpenAPI 规范 JSON，可供工具消费 |


---


## Swagger UI


Swagger UI 提供了直观的用户界面，可以直接在浏览器中测试 API：


![](https://www.runoob.com/wp-content/uploads/2023/12/index-01-swagger-ui-simple.png)


### 测试 API 的步骤


- 点击要测试的路由，展开详情
- 点击 **"Try it out"** 按钮
- 填写参数值
- 点击 **"Execute"** 按钮发送请求
- 查看响应结果


![](https://www.runoob.com/wp-content/uploads/2023/12/index-04-swagger-03.png)


---


## ReDoc


ReDoc 注重文档的可读性，适合浏览 API 定义：


![](https://www.runoob.com/wp-content/uploads/2023/12/index-02-redoc-simple.png)


---


## OpenAPI 规范


FastAPI 使用 **OpenAPI** 标准将 API 转换为"模式"（Schema）。访问 **http://127.0.0.1:8000/openapi.json** 可以查看原始的 OpenAPI JSON：


```
{
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/{item_id}": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response"
                    }
                }
            }
        }
    }
}
```


OpenAPI 规范的用途：


- 驱动 Swagger UI 和 ReDoc 文档系统
- 自动生成各种语言的客户端代码
- 与 API 测试工具（如 Postman）集成
- 兼容大量第三方工具和平台


---


## 自定义 API 文档信息


创建 FastAPI 实例时，可以自定义文档的元数据：


## 实例


```python
from fastapi import FastAPI

app = FastAPI(
    title="我的 API",                    # API 标题
    description="这是一个示例 API，展示文档自定义功能",  # API 描述
    version="1.0.0",                    # API 版本
    terms_of_service="http://example.com/terms/",  # 服务条款 URL
    contact={                           # 联系信息
        "name": "开发者",
        "url": "http://example.com/contact/",
        "email": "[email protected]",
    },
    license_info={                      # 许可证信息
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)
```


---


## 为路由添加文档信息


可以在装饰器和函数中为每个路由添加详细的文档信息：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get(
    "/items/{item_id}",
    summary="获取商品信息",              # 简短摘要
    description="根据商品 ID 获取商品的详细信息",  # 详细描述
    response_description="商品信息对象",   # 响应描述
    tags=["商品管理"],                   # 分组标签
)
async def read_item(
    item_id: Annotated[int, Path(ge=1, description="商品ID")],
    q: Annotated[str | None, Query(description="搜索关键词")] = None,
):
    """
    获取商品信息：

    - **item_id**: 商品的唯一标识符
    - **q**: 可选的搜索关键词
    """
    return {"item_id": item_id, "q": q}
```


文档参数说明：


| 参数 | 位置 | 说明 |
| --- | --- | --- |
| summary | 装饰器 | 路由的简短摘要，显示在路由列表中 |
| description | 装饰器 | 路由的详细描述，支持 Markdown |
| response_description | 装饰器 | 响应的描述 |
| tags | 装饰器 | 路由分组，在文档中按标签分类显示 |
| docstring | 函数体 | 函数的文档字符串，会作为描述显示 |


**
如果同时设置了 `description` 和函数的 docstring，`description` 优先生效。docstring 支持 Markdown 格式，适合编写较长的说明。


---


## 使用 tags 分组


`tags` 参数可以将相关的路由归为一组，在文档中更清晰地展示：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/", tags=["用户管理"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@app.get("/items/", tags=["商品管理"])
async def read_items():
    return [{"name": "Foo"}, {"name": "Bar"}]
```


在 Swagger UI 中，路由会按标签分组显示。


---


## 禁用文档


在生产环境中，你可能想禁用自动文档：


## 实例


```python
from fastapi import FastAPI

# 禁用文档
app = FastAPI(docs_url=None, redoc_url=None)
```


---


## 小结


- FastAPI 自动生成 Swagger UI 和 ReDoc 两种交互式文档
- 文档内容基于代码中的类型注解自动生成，代码更新文档自动同步
- 使用 `title`、`description`、`tags` 等参数自定义文档信息
- 函数的 docstring 也会出现在文档中
- 生产环境可通过 `docs_url=None` 禁用文档









	  AI 思考中...





			** [第一个 FastAPI 应用](https://www.runoob.com/fastapi-step1.html)
			[FastAPI 基本路由](https://www.runoob.com/fastapi-route.html) **













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