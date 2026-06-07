# RESTful API 教程

- Source: https://www.runoob.com/restfulapi/restful-api-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/05/fn4media_rest_api.png)

在现代 Web 开发中，RESTful API 已成为应用程序之间通信的标准方式。


REST（Representational State Transfer，表述性状态转移）是一种软件架构风格，由 Roy Fielding 博士在 2000 年提出。


REST 定义了一组约束条件和原则，用于创建可扩展、松耦合的 Web 服务。


RESTful API 是遵循 REST 架构风格设计的 API。它使用HTTP协议的特性，通过 URL 定位资源，用 HTTP 方法（GET、POST等）描述操作，实现客户端与服务器之间的交互。


---


## 谁适合阅读本教程？


无论你是前端开发者需要与后端 API 交互，还是后端开发者需要设计 API 接口，掌握 RESTful API 都是必备技能。


---


## RESTful API 特点？


**关键特点**：


- **无状态**：每个请求包含处理所需的所有信息
- **统一接口**：使用标准 HTTP 方法进行操作
- **资源导向**：所有内容都被抽象为资源
- **可缓存**：响应应明确是否可缓存


---


## RESTful API的核心原则


### 1. 资源与URI


在REST中，所有事物都被抽象为资源，每个资源有唯一的标识符（URI）。


**URI设计规范**：


- 使用名词而非动词表示资源
- 使用复数形式命名集合
- 使用小写字母和连字符(-)
- 避免文件扩展名


**示例**：


```
/users          # 用户集合
/users/123      # ID为123的用户
/users/123/orders  # 用户123的订单集合
```


### 2. HTTP方法的使用


RESTful API充分利用HTTP方法的语义：


| HTTP方法 | 描述 | 幂等性 | 安全性 |
| --- | --- | --- | --- |
| GET | 获取资源 | 是 | 是 |
| POST | 创建资源 | 否 | 否 |
| PUT | 完整更新资源 | 是 | 否 |
| PATCH | 部分更新资源 | 否 | 否 |
| DELETE | 删除资源 | 是 | 否 |


### 3. 无状态性


每个请求必须包含处理所需的所有信息，服务器不保存客户端状态。这使得API易于扩展和负载均衡。


### 4. 表述形式


资源可以有多种表述形式（如JSON、XML），客户端通过Accept头指定需要的格式。









	  AI 思考中...






			[RESTful API 概念](https://www.runoob.com/restful-api-intro.html) **













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