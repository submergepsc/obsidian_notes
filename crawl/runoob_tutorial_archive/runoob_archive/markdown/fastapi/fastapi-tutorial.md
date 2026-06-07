# FastAPI 教程

- Source: https://www.runoob.com/fastapi/fastapi-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2023/12/logo-teal.png)

FastAPI 是一个用于构建 API 的现代、快速（高性能）的 Python Web 框架，专为构建 RESTful API 而设计。


FastAPI 使用 Python 3.8+ 并基于标准的 Python 类型提示，使用 Starlette 和 Pydantic 构建，能够自动生成 API 文档并进行数据校验。


---


## 谁适合阅读本教程？


本教程适合有 Python 基础的开发者学习。如果你已经了解 Python 的基本语法和类型注解，那么你将能够快速上手 FastAPI。


---


## 学习本教程前你需要了解


学习本教程前你需要了解一些基础的 Web 知识及 [Python 3.x 基础教程](https://www.runoob.com/../python3/python3-tutorial.html)。如果你对 HTTP 请求方法（GET、POST 等）不太熟悉，建议先阅读 [HTTP 教程](https://www.runoob.com/../http/http-tutorial.html)。


---


## FastAPI 特点


FastAPI 之所以在 Python Web 框架中脱颖而出，主要得益于以下特点：


| 特点 | 说明 |
| --- | --- |
| 高性能 | 基于 Starlette 和 Pydantic，性能与 NodeJS 和 Go 相当，是最快的 Python 框架之一 |
| 快速开发 | 开发速度提升约 200%-300%，标准类型声明即可完成数据校验和文档生成 |
| 减少错误 | 减少约 40% 的人为错误，类型系统自动捕获常见问题 |
| 自动文档 | 自动生成交互式 API 文档（Swagger UI 和 ReDoc），无需手动维护 |
| 类型安全 | 基于标准 Python 类型提示，编辑器提供全面的自动补全和错误检查 |
| 异步支持 | 原生支持 async/await，可高效处理 IO 密集型任务 |


---


## FastAPI 适用场景


| 场景 | 说明 |
| --- | --- |
| 构建 API 后端 | 用于构建 RESTful API，支持前后端分离的 Web 应用 |
| 微服务架构 | 轻量高效，适合作为微服务后端框架 |
| 数据处理 API | 适用于接收和返回 JSON 数据的数据处理服务 |
| 实时通信 | 支持 WebSocket，适用于实时通信场景 |
| 机器学习服务 | 可将训练好的模型封装为 API，方便前端和其他服务调用 |


---


## FastAPI 技术栈


FastAPI 构建在两个核心库之上：


| 组件 | 作用 | 说明 |
| --- | --- | --- |
| Starlette | Web 框架层 | 提供路由、中间件、WebSocket 等基础 Web 功能，FastAPI 直接继承自 Starlette |
| Pydantic | 数据校验层 | 基于 Python 类型提示进行数据校验、序列化和文档生成 |
| Uvicorn | ASGI 服务器 | 基于 uvloop 和 httptools 的高性能 ASGI 服务器，用于运行 FastAPI 应用 |


**FastAPI 是 Starlette 的子类，因此你可以使用 Starlette 的所有功能。同时 FastAPI 完全兼容 Pydantic，包括基于 Pydantic 的 ORM（如 SQLModel）等外部库。


---


## 为什么选择 FastAPI？


| 对比维度 | FastAPI | Flask | Django |
| --- | --- | --- | --- |
| 性能 | 高（异步，ASGI） | 中（同步，WSGI） | 中（同步，WSGI） |
| 自动文档 | 内置（Swagger UI + ReDoc） | 需第三方扩展 | 需第三方扩展 |
| 类型校验 | 内置（Pydantic） | 需手动实现 | 需手动实现 |
| 异步支持 | 原生支持 | 需扩展 | 3.1+ 支持 |
| 学习曲线 | 低 | 低 | 较高 |
| 适用规模 | 中小型 / 微服务 | 中小型 | 大型 / 全栈 |


---


## 相关链接


| 资源 | 地址 |
| --- | --- |
| FastAPI 官方文档 | https://fastapi.tiangolo.com/zh/ |
| FastAPI 源码 | https://github.com/tiangolo/fastapi |
| Starlette 文档 | https://www.starlette.dev/ |
| Pydantic 文档 | https://docs.pydantic.dev/ |









	  AI 思考中...






			[FastAPI 安装](https://www.runoob.com/fastapi-install.html) **













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