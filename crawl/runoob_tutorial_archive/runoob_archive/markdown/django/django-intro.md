# Django 简介

- Source: https://www.runoob.com/django/django-intro.html

Django 是一个由 Python 编写的一个开放源代码的 Web 应用框架。


使用 Django，只要很少的代码，Python 的程序开发人员就可以轻松地完成一个正式网站所需要的大部分内容，并进一步开发出全功能的 Web 服务。


Django 提供了全栈开发所需的工具，包括数据库 ORM、模板引擎、路由系统、用户认证等，大幅减少重复代码。


**Django 的哲学:**

- **DRY（Don't Repeat Yourself）:** 避免重复代码，提倡复用（如模板继承、模型继承）。
- **约定优于配置: ** 默认提供合理配置（如自动生成 Admin 界面），减少决策成本。
- **快速开发: **从原型到生产环境均可高效推进。


Django 遵循 MVC（Model-View-Controller）架构，但在 Django 中更常被称为 MTV（Model-Template-View）。


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-MVT-pattern.webp)


### 内置功能

| 功能 | 说明 |
| --- | --- |
| Admin 后台 | 自动生成管理界面，无需手动编写 CRUD 逻辑。 |
| ORM | 用 Python 类操作数据库，无需写 SQL。 |
| 表单处理 | 内置表单验证，防止 CSRF 攻击。 |
| 用户认证 | 提供登录、注册、权限管理（django.contrib.auth）。 |
| 路由系统 | URL 映射灵活，支持正则表达式。 |
| 缓存机制 | 支持 Memcached、Redis 等后端。 |


---


## 核心特点


- **快速开发：**Django 提供了大量内置功能，如认证、管理后台、表单处理等，让开发者专注于业务逻辑，而非底层实现。
- **自动化管理后台：**只需简单的模型定义，即可生成强大的后台管理界面，支持增删改查。
- **ORM 数据库映射：**Django 内置 ORM (Object-Relational Mapping)，可以让开发者使用 Python 类与数据库交互，无需编写 SQL。
- **强大的 URL 路由：**使用正则表达式灵活定义 URL，轻松实现页面路由。
- **模板引擎：**内置强大的模板系统，支持逻辑判断、循环处理，方便渲染 HTML 页面。
- **国际化支持：**Django 支持多语言国际化，非常适合全球化应用。
- **高安全性：**内置多种安全保护措施，如防止 SQL 注入、XSS 攻击、CSRF 攻击等。
- **丰富的社区与扩展：**大量开源的第三方库，如 Django REST framework、Django CMS 等，快速扩展功能。


---


## MVC 与 MTV模型


![](https://www.runoob.com/wp-content/uploads/2020/05/1_gJqbf68KhZQUZfboS-Eniw.png)


### MVC (Model-View-Controller)

- **Model (模型)**：处理与数据库的交互，定义数据的结构和业务逻辑。
- **View (视图)**：负责数据展示，生成用户看到的 HTML 页面。
- **Controller (控制器)**：接收用户请求，调用 Model 处理数据，并将结果传递给 View 渲染页面。


**流程：**


- 用户发送请求到 Controller。
- Controller 处理逻辑，调用 Model 获取数据。
- Controller 将数据传递给 View。
- View 渲染并返回 HTML 页面给用户。



### MVT (Model-Template-View) —— Django 的实现方式


Django 中采用了 **MVT** 设计模式，类似于 MVC，但有一些区别：


- **Model (模型)**：与数据库交互，处理数据的创建、读取、更新、删除。
- **Template (模板)**：负责页面渲染，生成最终的 HTML 内容。
- **View (视图)**：Django 的 View 更偏向于控制器的角色，接收请求并决定使用哪个模板和数据。


**流程：**


- 用户访问 URL，请求被 Django 的 `urls.py` 映射到相应的 View。
- View 处理业务逻辑，调用 Model 获取数据。
- View 将数据传递给 Template。
- Template 渲染 HTML，最终返回给用户。


---


## Django 的适用场景

适合用 Django 的项目:

- ✅ 内容管理系统（CMS）（如新闻网站、博客）
- ✅ 社交平台（用户系统、动态发布）
- ✅ 电子商务网站（订单管理、支付集成）
- ✅ API 后端（结合 Django REST framework）


不适合的场景:

- ❌ 超高性能要求的实时系统（如高频交易平台，推荐 Go 或 Rust）
- ❌ 极度轻量级的微服务（可以考虑 Flask 或 FastAPI）


---


## Django vs 其他框架


| 框架 | 特点 |
| --- | --- |
| Flask | 轻量级，灵活，适合小型项目或微服务。 |
| FastAPI | 异步支持强，适合高性能 API 开发。 |
| Ruby on Rails | 类似 Django，但使用 Ruby 语言。 |
| Laravel | PHP 生态的 MVC 框架，功能与 Django 类似。 |


** Django 优势：**


- "开箱即用"：无需额外安装插件即可实现完整功能。
- 安全性：自动防范 SQL 注入、XSS、CSRF 等常见攻击。
- 社区活跃：丰富的第三方库（如 Django REST framework、Django CMS）。










	  AI 思考中...





			** [Django Nginx+uwsgi 安装配置](https://www.runoob.com/django-nginx-uwsgi.html)
			[Django 路由](https://www.runoob.com/django-routers.html) **













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