# FastAPI 路径参数数值校验

- Source: https://www.runoob.com/fastapi/fastapi-path-params-validation.html

与查询参数使用 `Query` 添加校验的方式相同，你可以使用 `Path` 为路径参数声明数值校验和元数据。


---


## 导入 Path


从 `fastapi` 导入 `Path`，从 `typing` 导入 `Annotated`：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    # 为路径参数添加元数据和校验
    item_id: Annotated[int, Path(title="商品ID", description="要获取的商品ID", ge=1)],
):
    return {"item_id": item_id}
```


**
路径参数总是必填的，因为它必须是 URL 路径的一部分。即使你为其声明了默认值，它仍然会作为必填参数处理。


---


## 数值校验


`Path` 和 `Query` 都支持以下数值校验参数：


| 参数 | 含义 | 英文来源 |
| --- | --- | --- |
| gt | 大于 | greater than |
| ge | 大于等于 | greater than or equal |
| lt | 小于 | less than |
| le | 小于等于 | less than or equal |


### 大于等于（ge）


限制 `item_id` 必须 >= 1：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(ge=1)],  # item_id 必须 >= 1
):
    return {"item_id": item_id}
```


### 组合使用数值校验


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    # item_id 必须 > 0 且 <= 1000
    item_id: Annotated[int, Path(gt=0, le=1000)],
    # 查询参数也可以用数值校验
    size: Annotated[float, Query(gt=0, lt=10.5)] = 5.0,
):
    return {"item_id": item_id, "size": size}
```


### 浮点数校验


数值校验同样适用于浮点数。`gt`（大于）和 `ge`（大于等于）的区别在浮点数场景下很重要：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(ge=1, le=1000)],
    # size 必须 > 0 且 < 10.5
    # 0.5 是有效值，0.0 和 0 不是（因为 gt=0 严格大于 0）
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    return {"item_id": item_id, "size": size}
```


---


## 路径参数与查询参数混合使用


当你同时使用 `Path` 和 `Query` 时，使用 `Annotated` 可以避免参数顺序的问题：


## 实例


```python
from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    # 使用 Annotated 后，参数顺序无关紧要
    item_id: Annotated[int, Path(title="商品ID", ge=1, le=1000)],
    q: Annotated[str | None, Query(max_length=50)] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```


---


## 小结


路径参数数值校验的核心要点：


- 使用 `Annotated` + `Path` 声明路径参数的校验规则
- 数值校验：`gt`（大于）、`ge`（大于等于）、`lt`（小于）、`le`（小于等于）
- `Path` 和 `Query` 共享相同的校验参数，包括字符串校验（`min_length` 等）和元数据（`title`、`description` 等）
- 路径参数始终是必填的，无论是否声明默认值









	  AI 思考中...





			** [FastAPI 查询参数校验](https://www.runoob.com/fastapi-query-params-validation.html)
			[FastAPI 请求体字段与嵌套模型](https://www.runoob.com/fastapi-body-fields.html) **













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