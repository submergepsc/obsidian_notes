# ADO Command 对象

- Source: https://www.runoob.com/ado/ado-command.html

---


## Command 对象


ADO Command 对象用于执行面向数据库的一次简单查询。此查询可执行诸如创建、添加、取回、删除或更新记录等动作。


如果该查询用于取回数据，此数据将以一个 RecordSet 对象返回。这意味着被取回的数据能够被 RecordSet 对象的属性、集合、方法或事件进行操作。


Command 对象的主要特性是有能力使用存储查询和带有参数的存储过程。


### ProgID


set objCommand=Server.CreateObject("ADODB.command")


---


## 属性


| 属性 | 描述 |
| --- | --- |
| ActiveConnection | 设置或返回包含了定义连接或 Connection 对象的字符串。 |
| CommandText | 设置或返回包含提供者（provider）命令（如 SOL 语句、表格名称或存储的过程调用）的字符串值。默认值为 ""（零长度字符串）。 |
| CommandTimeout | 设置或返回长整型值，该值指示等待命令执行的时间（单位为秒）。默认值为 30。 |
| CommandType | 设置或返回一个 Command 对象的类型 |
| Name | 设置或返回一个 Command 对象的名称 |
| Prepared | 指示执行前是否保存命令的编译版本（已经准备好的版本）。 |
| State | 返回一个值，此值可描述该 Command 对象处于打开、关闭、连接、执行还是取回数据的状态。 |


## 方法


| 方法 | 描述 |
| --- | --- |
| Cancel | 取消一个方法的一次执行。 |
| CreateParameter | 创建一个新的 Parameter 对象 |
| Execute | 执行 CommandText 属性中的查询、SQL 语句或存储过程。 |


## 集合


| 集合 | 描述 |
| --- | --- |
| Parameters | 包含一个 Command 对象的所有 Parameter 对象。 |
| Properties | 包含一个 Command 对象的所有 Property 对象。 |









	  AI 思考中...





			** [ADO 通过 GetString() 加速脚本](https://www.runoob.com/ado-getstring.html)
			[ADO Connection 对象](https://www.runoob.com/ado-ref-connection.html) **













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