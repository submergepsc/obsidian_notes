# MongoDB 用户管理

- Source: https://www.runoob.com/mongodb/mongodb-user.html

在 MongoDB 中进行用户管理涉及用户的创建、分配角色、认证和登录等操作。

下面是一个详细的说明，包含如何使用 MongoDB Shell (mongo) 或 MongoDB Compass 来管理用户。


### 使用 MongoDB Shell (mongo) 管理用户


以下是使用 MongoDB Shell (mongosh) 进行用户管理的详细说明，包括创建用户、分配角色、认证和登录的具体步骤。


**1. 连接到 MongoDB**

首先，打开你的终端并使用 mongosh 命令连接到 MongoDB 服务器：


```
mongosh --host <hostname> --port <port>
```


说明：


- `mongosh`：启动 MongoDB Shell 命令行工具。
- `--host `：指定 MongoDB 服务器的主机名或 IP 地址。``：MongoDB 服务器的主机名（如 `localhost`）或 IP 地址（如 `127.0.0.1`）。
`--port <port>`：指定 MongoDB 服务器的端口号。
- `
`：MongoDB 服务器监听的端口号，默认端口是 `27017`。 ** 2. 切换到目标数据库**


在 MongoDB 中，用户是针对特定数据库创建的，使用 **use** 命令切换到你要创建用户的数据库：


```
use <database_name>
```



- **database_name** - 为要切换的数据库。


** 3. 创建用户**

使用 db.createUser 命令创建用户并分配角色。

例如，创建一个名为 testuser 的用户，密码为 password123，并赋予 readWrite 和 dbAdmin 角色：


```
db.createUser({
  user: "testuser",
  pwd: "password123",
  roles: [
    { role: "readWrite", db: "<database_name>" },
    { role: "dbAdmin", db: "<database_name>" }
  ]
})
```


**4. 验证用户**

创建用户后，你可以使用 db.auth 命令验证用户身份：


```
db.auth("testuser", "password123")
```


**5. 启用身份验证**

为了确保只有经过身份验证的用户才能访问 MongoDB，需要启用身份验证。

编辑 MongoDB 配置文件 mongod.conf，并在其中添加以下内容：


```
security:
  authorization: "enabled"
```


然后重启 MongoDB 服务以应用更改。

** 6. 使用用户身份登录**

启用身份验证后，你需要使用创建的用户身份连接到 MongoDB：


```
mongosh --host <hostname> --port <port> -u "testuser" -p "password123" --authenticationDatabase "<database_name>"
```


**7. 删除用户**

使用 **db.dropUser** 命令删除指定用户。

例如，删除名为 testuser 的用户：


```
db.dropUser("testuser")
```


### 实例操作

以下是一个完整的示例操作流程：


启动 MongoDB Shell 并连接到服务器：


```
mongosh --host localhost --port 27017
```


切换到 testdb 数据库：


```
use testdb
```


创建 testuser 用户：


```
db.createUser({
  user: "testuser",
  pwd: "password123",
  roles: [{ role: "readWrite", db: "testdb" }]
})
```


**启用身份验证并重启 MongoDB 实例**

编辑 mongod.conf 文件，添加以下内容：


```
security:
  authorization: "enabled"
```


重启 MongoDB 服务：


```
sudo systemctl restart mongod
```


使用 testuser 用户进行身份验证连接：


```
mongosh --host localhost --port 27017 -u "testuser" -p "password123" --authenticationDatabase "testdb"
```


删除 testuser 用户：


```
db.dropUser("testuser")
```









	  AI 思考中...





			** [MongoDB Shell](https://www.runoob.com/mongodb-shell.html)














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