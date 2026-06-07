# FastAPI 查询参数

- Source: https://www.runoob.com/fastapi/fastapi-query-params.html

查询参数是 URL 中 `?` 之后、以 `&` 分隔的键值对。当函数参数不是路径参数也不是请求体时，FastAPI 会将其自动解释为查询参数。


---


## 基本用法


声明查询参数只需要在函数参数中添加类型注解和默认值：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

# skip 和 limit 是查询参数，有默认值
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # 模拟分页查询
    return fake_items_db[skip : skip + limit]
```


查询参数在 URL 中的格式：


```
http://127.0.0.1:8000/items/?skip=0&limit=10
```


不同访问方式的参数值：


| URL | skip 的值 | limit 的值 | 说明 |
| --- | --- | --- | --- |
| /items/ | 0 | 10 | 使用默认值 |
| /items/?skip=20 | 20 | 10 | skip 使用传入值，limit 使用默认值 |
| /items/?skip=20&limit;=5 | 20 | 5 | 两个参数都使用传入值 |


---


## 可选参数


将默认值设为 `None` 即可声明可选的查询参数：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    # item_id 是路径参数（必填），q 是查询参数（可选）
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```


这里 `q: str | None = None` 表示 `q` 可以是字符串或 `None`，默认值为 `None`。


**
FastAPI 通过默认值 `= None` 判断参数是否必填，而不是通过类型注解 `str | None`。类型注解主要帮助编辑器提供更好的支持。


---


## 查询参数类型转换


FastAPI 支持将查询参数自动转换为 `bool` 类型：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, short: bool = False):
    # short 参数会被自动转换为布尔值
    if short:
        return {"item_id": item_id}
    return {"item_id": item_id, "description": "这是一段很长的描述"}
```


以下 URL 中的 `short` 参数都会被转换为 `True`：


```
/items/foo?short=1
/items/foo?short=True
/items/foo?short=true
/items/foo?short=on
/items/foo?short=yes
```


其他值会被转换为 `False`。


---


## 必选查询参数


不设置默认值的查询参数即为必选参数：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, needy: str):
    # needy 没有默认值，是必选查询参数
    return {"item_id": item_id, "needy": needy}
```


如果访问 `/items/foo` 时没有提供 `needy` 参数，FastAPI 会返回类似以下的错误：


```
{
  "detail": [
    {
      "type": "missing",
      "loc": ["query", "needy"],
      "msg": "Field required",
      "input": null
    }
  ]
}
```


---


## 混合使用必选、有默认值和可选参数


你可以在同一个函数中混合使用不同类型的查询参数：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(
    item_id: str,           # 路径参数（必填）
    needy: str,             # 必选查询参数
    skip: int = 0,          # 有默认值的查询参数
    limit: int | None = None,  # 可选查询参数
):
    item = {"item_id": item_id, "needy": needy, "skip": skip}
    if limit:
        item.update({"limit": limit})
    return item
```


参数类型总结：


| 参数 | 声明方式 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| item_id | item_id: str | 必填 | 路径参数，出现在 URL 路径中 |
| needy | needy: str | 必填 | 查询参数，无默认值 |
| skip | skip: int = 0 | 可选 | 查询参数，有默认值 0 |
| limit | limit: int \| None = None | 可选 | 查询参数，默认值为 None |


---


## 多个路径和查询参数


FastAPI 可以同时识别多个路径参数和查询参数，参数的声明顺序不影响识别：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,       # 路径参数
    item_id: str,       # 路径参数
    q: str | None = None,  # 可选查询参数
    short: bool = False,   # 有默认值的查询参数
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "这是一段很长的描述"})
    return item
```


FastAPI 通过参数名匹配路径中的变量，因此函数参数的顺序无关紧要。


---


## 小结


查询参数的核心要点：


- 有默认值的参数是可选的，没有默认值的是必选的
- FastAPI 自动将 URL 中的字符串转为声明的类型
- `bool` 类型支持多种写法（`true`、`1`、`on`、`yes` 等）
- 查询参数可以与路径参数混合使用，顺序无关









	  AI 思考中...





			** [FastAPI 路径参数](https://www.runoob.com/fastapi-path-params.html)
			[FastAPI 请求体](https://www.runoob.com/fastapi-request-body.html) **













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