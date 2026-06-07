# FastAPI 查询参数校验

- Source: https://www.runoob.com/fastapi/fastapi-query-params-validation.html

FastAPI 允许你为查询参数声明额外的校验规则和元数据，例如字符串长度限制、正则匹配等。通过 `Query` 和 `Annotated`，你可以在不改变函数逻辑的情况下增强参数校验。


---


## 基本校验


以下示例为查询参数 `q` 添加最大长度限制：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    # 使用 Annotated + Query 添加校验
    q: Annotated[str | None, Query(max_length=50)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```


代码说明：


| 部分 | 说明 |
| --- | --- |
| Annotated[str \| None, ...] | 类型注解，表示 q 可以是字符串或 None |
| Query(max_length=50) | 校验规则，q 的最大长度为 50 个字符 |
| = None | 默认值，使参数变为可选 |


**
FastAPI 推荐使用 `Annotated` 方式声明校验，而非将 `Query` 作为默认值。因为 `Annotated` 方式下，函数的默认值就是真正的默认值，更符合 Python 的直觉，且编辑器和类型检查工具支持更好。


---


## 添加更多校验


你可以同时添加多种校验规则：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    # 同时限制最小长度、最大长度和正则表达式
    q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```


字符串校验参数：


| 参数 | 类型 | 说明 |
| --- | --- | --- |
| min_length | int | 最小长度 |
| max_length | int | 最大长度 |
| pattern | str | 正则表达式匹配 |


正则表达式 `^fixedquery$` 的含义：


- `^` -- 必须以接下来的字符开头
- `fixedquery` -- 值必须精确等于 `fixedquery`
- `$` -- 到此结束，后面不能有其他字符


---


## 带默认值的校验


你可以为查询参数同时设置默认值和校验规则：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    # 默认值为 "fixedquery"，同时要求最小长度为 3
    q: Annotated[str, Query(min_length=3)] = "fixedquery",
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```


> 任何类型的默认值（包括非 `None` 值）都会让参数变为可选。没有默认值也没有 `Query(default=...)` 的参数是必填的。


---


## 必填参数


使用 `Query` 时，如果不声明默认值，参数就是必填的：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    # 没有 = None，所以 q 是必填参数
    q: Annotated[str, Query(min_length=3)],
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    results.update({"q": q})
    return results
```


### 必填但可以为 None


有时你需要客户端必须传值，但值可以是 `None`：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    # 客户端必须提供 q 参数，但值可以是 None
    q: Annotated[str | None, Query(min_length=3)],
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```


---


## 查询参数列表 / 多个值


使用 `Query` 可以声明接收多个值的查询参数：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    # q 可以在 URL 中出现多次，值会被收集为列表
    q: Annotated[list[str] | None, Query()] = None,
):
    query_items = {"q": q}
    return query_items
```


访问 http://127.0.0.1:8000/items/?q=foo&q;=bar**，返回：


```
{"q": ["foo", "bar"]}
```


**
要声明类型为 `list` 的查询参数，必须显式使用 `Query()`，否则 FastAPI 会将其解释为请求体。


---


## 声明元数据


`Query` 还支持为参数添加元数据，这些信息会出现在 API 文档中：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(
        title="查询字符串",           # 参数标题
        description="用于筛选商品的查询字符串",  # 参数描述
        min_length=3,
        max_length=50,
        alias="item-query",    # URL 中的参数名别名
        deprecated=True,       # 标记为已弃用
    )] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```


元数据参数说明：


| 参数 | 说明 | 使用场景 |
| --- | --- | --- |
| alias | URL 中的参数名别名 | 参数名含连字符（如 item-query），不是有效 Python 变量名时 |
| title | 参数标题 | 在文档中显示参数标题 |
| description | 参数描述 | 在文档中显示参数的详细说明 |
| deprecated | 标记为已弃用 | 参数仍可使用，但文档中会标记为"已弃用" |
| include_in_schema | 是否出现在 API 文档中 | 设为 False 可隐藏参数 |


---


## 从 OpenAPI 中排除参数


如果某个查询参数不应出现在 API 文档中：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    # hidden_query 不会出现在 API 文档中，但仍然可以使用
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    return {"items": [{"item_id": "Foo"}]}
```


---


## 小结


查询参数校验的核心要点：


- 使用 `Annotated` + `Query` 声明校验规则（推荐方式）
- 字符串校验：`min_length`、`max_length`、`pattern`
- 没有默认值 = 必填参数，有默认值 = 可选参数
- `alias` 用于 URL 中使用非 Python 变量名的参数名
- `deprecated=True` 标记过时的参数
- 使用 `list[str]` 接收多个相同名称的查询参数









	  AI 思考中...





			** [FastAPI 请求体](https://www.runoob.com/fastapi-request-body.html)
			[FastAPI 路径参数数值校验](https://www.runoob.com/fastapi-path-params-validation.html) **













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