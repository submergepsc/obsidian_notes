# MongoDB Shell

- Source: https://www.runoob.com/mongodb/mongodb-shell.html

MongoDB Shell 是 MongoDB 提供的官方交互式界面，允许用户与 MongoDB 数据库进行交互、执行命令和操作数据库。

MongoDB Shell 是基于 JavaScript 的，允许用户直接在命令行或者脚本中使用 JavaScript 语言来操作 MongoDB 数据库。

---


## 安装 MongoDB Shell


MongoDB Shell 是 MongoDB 数据库安装包的一部分，因此，安装 MongoDB 数据库也会自动安装 MongoDB Shell。


### 在 macOS 上安装 MongoDB Shell


**使用 Homebrew 安装：**

如果你使用 Homebrew 管理 macOS 上的软件包，可以通过以下命令安装 MongoDB：


```
brew tap mongodb/brew
brew install mongodb-community-shell
```


这将安装 MongoDB 的最新版本及其相关工具，包括 MongoDB Shell。

** 手动下载安装：**

另一种方法是从 MongoDB 官网下载适用于 macOS 的 MongoDB Shell，下载地址 [https://www.mongodb.com/try/download/shell](https://www.mongodb.com/try/download/shell) :


![](https://www.runoob.com/wp-content/uploads/2024/06/1730c0439cc5568232067f2d2021fca3.png)


下载后，解压安装包，将 bin 目录中 mongosh 二进制文件复制到 PATH 变量中列出的目录中，例如 /usr/local/bin：


```
sudo cp mongosh /usr/local/bin/
sudo cp mongosh_crypt_v1.so /usr/local/lib/
```


安装完成后，MongoDB Shell 将可以在命令行中通过 **mongosh** 命令启动。


若 macOS 阻止运行 mongosh，打开"系统偏好设置"中的"安全与隐私"以允许其运行。


### 在 Linux 上安装 MongoDB Shell

在大多数 Linux 发行版中，可以通过包管理器来安装 MongoDB Shell。例如，在 Ubuntu 上可以使用 apt 包管理器：


为 Ubuntu 22.04 (Jammy) 创建 /etc/apt/sources.list.d/mongodb-org-7.0.list 文件：


```
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
```


```
sudo apt update
sudo apt install mongodb-shell
```


安装完成后，MongoDB Shell 将可以在命令行中通过 **mongosh** 命令启动。


另一种方法是从 MongoDB 官网下载适用于 Linux 的 MongoDB Shell，下载地址 [https://www.mongodb.com/try/download/shell](https://www.mongodb.com/try/download/shell) :


![](https://www.runoob.com/wp-content/uploads/2024/06/fb02c0cbf311ab95064bb0b6282c5f2d-2.png)


下载后，解压安装包，将 bin 目录中 mongosh 二进制文件复制到 PATH 变量中列出的目录中，例如 /usr/local/bin：


```
sudo cp mongosh /usr/local/bin/
sudo cp mongosh_crypt_v1.so /usr/local/lib/
```


安装完成后，MongoDB Shell 将可以在命令行中通过 **mongosh** 命令启动。


### 在 Windows 上安装 MongoDB Shell


访问 MongoDB 官网下载页面（[https://www.mongodb.com/try/download/shell](https://www.mongodb.com/try/download/shell)），选择适合 Windows 的 MongoDB Shell 版本，并下载安装程序。


![](https://www.runoob.com/wp-content/uploads/2024/06/23bc1e03cb63ef2e51b2fda7d633aa44.png)


运行下载的安装程序，并按照指示进行安装。在安装过程中，确保选择安装 MongoDB Shell（默认情况下会包含在安装中）。


可以选择在安装过程中配置环境变量，这样可以在命令行中直接运行 mongosh 命令来启动 MongoDB Shell。

---


## 使用 MongoDB Shell


安装完成后，可以通过以下步骤来使用 MongoDB Shell 连接到 MongoDB 数据库并执行操作。


** 启动 MongoDB Shell：**


在命令行中输入 mongosh 命令，启动 MongoDB Shell，如果 MongoDB 服务器运行在本地默认端口（27017），则可以直接连接。


```
mongosh
```


查看版本：


```
mongosh --version
2.2.9
```


** 连接到 MongoDB 服务器：**


如果 MongoDB 服务器运行在非默认端口或者远程服务器上，可以使用以下命令连接：


```
mongosh --host <hostname>:<port>
```


其中 `` 是 MongoDB 服务器的主机名或 IP 地址，`` 是 MongoDB 服务器的端口号。


**执行基本操作：**


连接成功后，可以执行各种 MongoDB 数据库操作。例如：



- 查看当前数据库：`db`
- 显示数据库列表：`show dbs`
- 切换到指定数据库：`use `
- 执行查询操作：`db..find()`
- 插入文档：`db..insertOne({ ... })`
- 更新文档：`db..updateOne({ ... })`
- 删除文档：`db..deleteOne({ ... })`
- 退出 MongoDB Shell：`quit()` 或者 `exit`


### 实例

以下是使用 MongoDB Shell 连接到本地 MongoDB 服务器，并执行一些基本操作的示例：


## 实例


```mongodb
# 启动 MongoDB Shell
mongosh

# 连接到本地 MongoDB 服务器
test> show dbs
admin   40.00 KiB
config  72.00 KiB
local   40.00 KiB
runoob  72.00 KiB
test> use runoob
switched to db runoob

# 插入文档
runoob> db.mycollection.insertOne({ name: "Alice", age: 30 })
{
  acknowledged: true,
  insertedId: ObjectId('667cd8789a69705686ed70f2')
}

# 查询文档
runoob> db.mycollection.find()
[
  { _id: ObjectId('667cd8789a69705686ed70f2'), name: 'Alice', age: 30 }
]

# 更新文档
runoob> db.mycollection.updateOne({ name: "Alice" }, { $set: { age: 31 } })
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}

# 删除文档
runoob> db.mycollection.deleteOne({ name: "Alice" })
{ acknowledged: true, deletedCount: 1 }

# 退出 MongoDB Shell
runoob> quit()
```


![](https://www.runoob.com/wp-content/uploads/2024/06/d867822e85a8b2baf7456a230132beb5.png)

通过上述步骤和示例，你可以开始使用 MongoDB Shell 来管理和操作 MongoDB 数据库。

官方安装说明：[https://www.mongodb.com/zh-cn/docs/mongodb-shell/install/](https://www.mongodb.com/zh-cn/docs/mongodb-shell/install/)








	  AI 思考中...





			** [MongoDB 更新集合名](https://www.runoob.com/mongodb-renamecollection.html)
			[MongoDB 用户管理](https://www.runoob.com/mongodb-user.html) **













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