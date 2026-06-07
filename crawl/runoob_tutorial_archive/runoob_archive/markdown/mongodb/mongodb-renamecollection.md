# MongoDB 更新集合名

- Source: https://www.runoob.com/mongodb/mongodb-renamecollection.html

在 MongoDB 中，不能直接通过命令来重命名集合。

MongoDB 可以使用 renameCollection 方法来来重命名集合。

renameCollection 方法在 MongoDB 的 admin 数据库中运行，可以将一个集合重命名为另一个名称。


renameCollection 命令的语法：


```
db.adminCommand({
  renameCollection: "sourceDb.sourceCollection",
  to: "targetDb.targetCollection",
  dropTarget: <boolean>
})
```


**参数说明：**


- **renameCollection**：要重命名的集合的完全限定名称（包括数据库名）。
- **to**：目标集合的完全限定名称（包括数据库名）。
- **dropTarget**（可选）：布尔值。如果目标集合已经存在，是否删除目标集合。默认值为 `false`。


### 实例

假设你要将 test 数据库中的 oldCollection 重命名为 newCollection，可以按以下步骤进行：


1. 确保已连接到 test 数据库


```
use test
```


2. 运行 renameCollection 命令


```
db.adminCommand({
  renameCollection: "test.oldCollection",
  to: "test.newCollection"
});
```


如果你要将集合重命名到另一个数据库，例如将 test 数据库中的 oldCollection 重命名为 production 数据库中的 newCollection，可以这样做：


```
db.adminCommand({
  renameCollection: "test.oldCollection",
  to: "production.newCollection"
});
```


### 注意事项


- **权限要求**：执行 `renameCollection` 命令需要具有对源数据库和目标数据库的适当权限。通常需要 `dbAdmin` 或 `dbOwner` 角色。
- **目标集合不存在**：目标集合不能已经存在。如果目标集合存在，则会返回错误。
- **索引和数据**：重命名集合会保留所有文档和索引。


### 检查重命名结果

重命名后，可以通过以下命令检查新的集合是否存在：


```
use test
show collections
```


如果集合已重命名为 newCollection，你应该会在结果中看到 newCollection。


### 处理重命名失败的情况

如果重命名过程中发生错误，你可以根据错误消息采取相应的措施。例如，如果目标集合已经存在，可以先删除目标集合（如果确认不需要），然后重新执行重命名操作：


## 实例


```mongodb
use production
db.newCollection.drop();

use test
db.adminCommand({
  renameCollection: "test.oldCollection",
  to: "production.newCollection"
});
```


通过 renameCollection 方法，你可以有效地管理 MongoDB 集合的名称，确保数据库结构符合应用需求。









	  AI 思考中...





			** [MongoDB 删除集合](https://www.runoob.com/mongodb-delete-collection.html)
			[MongoDB Shell](https://www.runoob.com/mongodb-shell.html) **













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