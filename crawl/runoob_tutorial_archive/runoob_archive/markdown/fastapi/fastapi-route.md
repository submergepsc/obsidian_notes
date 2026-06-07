# FastAPI 基本路由

- Source: https://www.runoob.com/fastapi/fastapi-route.html

在 FastAPI 中，基本路由是定义 API 端点的关键。每个路由都映射到应用程序中的一个函数，用于处理特定的 HTTP 请求，并返回相应的响应。


### 根路径路由

创建 FastAPI 实例和根路径路由：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```


**代码说明：**


- `FastAPI()`：创建 FastAPI 应用实例。
- `@app.get("/")`：使用 `@app.get` 装饰器创建一个处理根路径的路由。
- `def read_root()`：路由处理函数，返回一个包含 {"Hello": "World"} 的字典。


### 路径参数


设置路由的参数：


## 实例


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```


**代码说明：**


- `@app.get("/items/{item_id}")`：定义了一个路由路径，其中 `{item_id}` 是路径参数，对应于函数参数 `item_id`。
- `def read_item(item_id: int, q: str = None)`：路由处理函数接受一个整数类型的路径参数 `item_id` 和一个可选的字符串类型查询参数 `q`。


在路由操作中，可以使用函数参数声明查询参数。例如，**q: str = None** 表示 **q** 是一个可选的字符串类型查询参数，默认值为 **None**。


### 启动应用和测试路由

使用 Uvicorn 启动应用：


```
uvicorn main:app --reload
```


访问 **http://127.0.0.1:8000** 查看根路径的响应：


![](https://www.runoob.com/wp-content/uploads/2023/12/a2e311f60bc9dfa46cf6474eaf2f8278.png)


访问 http://127.0.0.1:8000/items/42?q=runoob 查看带路径参数和查询参数的响应：


![](https://www.runoob.com/wp-content/uploads/2023/12/6a83565422bf2ed93c6db75fc3927ff8.png)


FastAPI 自动生成的交互式 API 文档将包括定义的路由信息、路径参数、查询参数等。访问文档地址 **http://127.0.0.1:8000/docs** 查看详细的文档和测试界面：


![](https://www.runoob.com/wp-content/uploads/2023/12/index-01-swagger-ui-simple.png)








	  AI 思考中...





			** [FastAPI 交互式 API 文档](https://www.runoob.com/fastapi-api-doc.html)
			[FastAPI Pydantic 模型](https://www.runoob.com/fastapi-pydantic.html) **













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