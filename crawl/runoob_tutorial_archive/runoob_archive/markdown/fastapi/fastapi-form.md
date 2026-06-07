# FastAPI 表单数据

- Source: https://www.runoob.com/fastapi/fastapi-form.html

当客户端通过 HTML 表单（`application/x-www-form-urlencoded`）提交数据时，需要使用 `Form` 来接收表单字段，而不是 `BaseModel`。


---


## 安装 python-multipart


使用表单功能前，需要先安装 `python-multipart`：


```
pip install python-multipart
```


---


## 接收表单数据


使用 `Form` 声明表单字段：


## 实例


```python
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(
    username: str = Form(),      # 必填表单字段
    password: str = Form(),      # 必填表单字段
):
    return {"username": username}
```


![](https://www.runoob.com/wp-content/uploads/2023/12/927e7dfc95fb795eeaa3af240662cb94.png)


---


## 表单字段与 JSON 请求体的区别


| 对比项 | JSON 请求体 | 表单数据 |
| --- | --- | --- |
| Content-Type | application/json | application/x-www-form-urlencoded |
| 声明方式 | Pydantic BaseModel | Form() |
| 数据结构 | 支持嵌套对象和数组 | 扁平的键值对 |
| 适用场景 | API 接口（前后端分离） | HTML 表单提交 |


**
表单数据以"字段"的形式发送，不是 JSON。因此不能将 `Form` 参数声明为 Pydantic 模型。表单字段和 JSON 请求体不能在同一个路由中同时使用。


---


## 可选表单字段


与查询参数类似，有默认值的表单字段是可选的：


## 实例


```python
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/items/")
async def create_item(
    name: str = Form(...),                    # 必填
    description: str | None = Form(None),     # 可选，默认 None
    price: float = Form(..., gt=0),           # 必填，必须大于 0
):
    return {"name": name, "description": description, "price": price}
```


![](https://www.runoob.com/wp-content/uploads/2023/12/514028636203aef522a8addb3f4eb62a.png)


---


## 使用 HTML 表单测试


你可以创建一个 HTML 页面来测试表单提交：


## 实例


```python
<form action="http://localhost:8000/items/" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <br>
    <label for="description">Description:</label>
    <textarea id="description" name="description"></textarea>
    <br>
    <label for="price">Price:</label>
    <input type="number" id="price" name="price" required min="0">
    <br>
    <button type="submit">Submit</button>
</form>
```


---


## 表单数据的校验和文档


使用 `Form` 声明的字段，FastAPI 会自动进行数据校验并在 API 文档中展示：


![](https://www.runoob.com/wp-content/uploads/2023/12/0d28c66e90a6ad39fc4ef693c146835c.png)


![](https://www.runoob.com/wp-content/uploads/2023/12/7eb01111becfc49e6e380300ad66c7a3.png)


---


## 小结


- 使用 `Form` 接收 HTML 表单提交的数据
- 表单数据不是 JSON，不能与 `BaseModel` 请求体混用
- `Form()` 声明必填字段，`Form(None)` 声明可选字段
- 需要安装 `python-multipart` 包
- 表单字段支持与查询参数相同的校验规则（`min_length`、`gt` 等）









	  AI 思考中...





			** [FastAPI 依赖注入](https://www.runoob.com/fastapi-path-operation-dependencies.html)
			[FastAPI 核心概念](https://www.runoob.com/fastapi-core.html) **













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