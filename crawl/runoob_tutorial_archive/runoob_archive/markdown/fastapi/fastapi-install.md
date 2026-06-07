# FastAPI 安装与环境配置

- Source: https://www.runoob.com/fastapi/fastapi-install.html

FastAPI 依赖 Python 3.8 及更高版本。本节介绍如何安装 FastAPI 以及配置开发环境。


---


## 检查 Python 版本


在安装 FastAPI 之前，先确认你的 Python 版本：


```
$ python --version
Python 3.11.0

# 或者
$ python3 --version
Python 3.11.0
```


如果你的 Python 版本低于 3.8，请先升级 Python。


---


## 创建虚拟环境


推荐在虚拟环境中安装 FastAPI，避免与系统 Python 包产生冲突：


```
# 创建虚拟环境
$ python -m venv venv

# 激活虚拟环境（macOS/Linux）
$ source venv/bin/activate

# 激活虚拟环境（Windows）
$ venv\Scripts\activate
```


**
虚拟环境是 Python 开发的最佳实践。每个项目使用独立的虚拟环境，可以避免不同项目之间的依赖冲突。


---


## 安装 FastAPI


使用 pip 安装 FastAPI：


```
$ pip install fastapi
```


这条命令只安装 FastAPI 核心包。如果你需要一次性安装 FastAPI 及其所有可选依赖，可以使用：


```
$ pip install "fastapi[all]"
```


`fastapi[all]` 会安装以下组件：


| 包名 | 用途 |
| --- | --- |
| uvicorn[standard] | ASGI 服务器，用于运行 FastAPI 应用 |
| python-multipart | 表单数据和文件上传支持 |
| jinja2 | HTML 模板引擎 |
| python-jose[cryptography] | JWT 令牌支持 |
| passlib[bcrypt] | 密码哈希与加密 |
| python-dotenv | 环境变量管理 |


---


## 安装 Uvicorn


FastAPI 是一个 ASGI 框架，需要一个 ASGI 服务器来运行。最常用的是 Uvicorn：


```
$ pip install "uvicorn[standard]"
```


`[standard]` 会安装 uvloop（高性能事件循环）和 httptools（高性能 HTTP 解析器），显著提升性能。


> ASGI（Asynchronous Server Gateway Interface）是 Python 异步 Web 服务器与应用程序之间的标准接口，是 WSGI 的异步版本。传统框架如 Flask 使用 WSGI（同步），而 FastAPI 使用 ASGI（异步），能够更高效地处理并发请求。


---


## 运行第一个 FastAPI 应用


安装完成后，创建一个名为 **main.py** 的文件：


## 实例


```python
from fastapi import FastAPI

# 创建 FastAPI 应用实例
app = FastAPI()

# 定义根路径的 GET 路由
@app.get("/")
async def root():
    return {"message": "Hello World"}
```


在命令行中启动应用：


```
$ uvicorn main:app --reload
```


参数说明：


| 参数 | 说明 |
| --- | --- |
| main:app | main 指文件名 main.py，app 指文件中创建的 FastAPI 实例变量名 |
| --reload | 开发模式，代码修改后自动重载服务器（仅用于开发环境） |


启动成功后，终端会显示：


```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```


打开浏览器访问 http://127.0.0.1:8000**，你将看到如下 JSON 响应：


```
{"message": "Hello World"}
```


![](https://www.runoob.com/wp-content/uploads/2023/12/a2e311f60bc9dfa46cf6474eaf2f8278.png)


同时，FastAPI 自动生成了交互式 API 文档：


| 地址 | 文档类型 | 说明 |
| --- | --- | --- |
| http://127.0.0.1:8000/docs | Swagger UI | 可交互测试 API 的文档界面 |
| http://127.0.0.1:8000/redoc | ReDoc | 更注重阅读体验的文档界面 |


---


## 使用 FastAPI CLI


FastAPI 新版本提供了 **fastapi** 命令行工具，可以更方便地运行应用：


```
# 开发模式（自动重载）
$ fastapi dev

# 生产模式
$ fastapi run
```


`fastapi dev` 会自动查找项目中的 FastAPI 应用并启动开发服务器，等同于 `uvicorn main:app --reload`。


---


## 推荐开发工具


| 工具 | 说明 |
| --- | --- |
| VS Code | 免费、轻量，配合 Python 和 Pylance 插件有极佳的 FastAPI 开发体验 |
| PyCharm | 专业 Python IDE，内置 FastAPI 项目模板和强大的调试功能 |
| 阿里 Qoder | 阿里推出的 AI 编程 IDE，基于 VS Code 深度定制 |
| 字节 Trae | 字节跳动推出的 AI 驱动开发工具，内置 Python 支持 |


**推荐使用 VS Code + Python 插件，它对 FastAPI 的类型注解和自动补全支持最好，且完全免费。








	  AI 思考中...





			** [FastAPI 教程](https://www.runoob.com/fastapi-tutorial.html)
			[第一个 FastAPI 应用](https://www.runoob.com/fastapi-step1.html) **













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