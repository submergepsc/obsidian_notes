# 参考手册

- Source: https://www.runoob.com/appml/appml-reference.html

---


## 数据模型：


<appml security="*security*">**

<datasource>
*Datasource definition goes here
*</datasource>


<filters>
*Filter definitions goes here (if any)
*</filters>


<update>
*Update definitions goes here (if any)
*</update>


<anything>
*Anything you want to add to the model
*</anything>

</appml>


---


## 安全


 安全通过  标签中的安全属性设置。


<appml security="artists">


以上应用开头包含了安全定义属性，只允许 artists 用户登陆。


在这种情况下，用户登录的用户名必须为 "artists"组的成员。


---


## 元素


应用的的  元素定义了4个不同数据类型的:


### 子元素（只有一个可以适用）


| 元素 | 描述 |
| --- | --- |
|  | 定义数据类型 |
|  | 定义 XML 源文件 |
|  | 定义一个逗号分隔的文本文件 |


---


## 元素


 元素定义了数据库


### 子元素


| 元素 | 描述 |
| --- | --- |
|  | 链接数据库名 |
|  | 数据检索前执行的SQL语句（可选） |
|  | 用于检索数据的SQL语句 |
|  | 应用程序的主表（可选） |
|  | 主表的键字段（可选） |


---


## 存储在SQL数据库中的数据


这是面向数据的应用程序最常用的解决方案。


<datasource>

<database>

<connection>CDDataBase</connection>

<sql>SELECT Artist, Title, Country FROM CD_Catalog</sql>

</database>

</datasource>


上面的模型可以从"CDDataBase"数据库的"CD_Catalog"表中选择三个数据选项 (Artist, Title, Country) 。


结果返回的行数是未知的。


---


## 存储在 XML 文件中的数据


 可以从XML文件中读取数据:


## 实例


```
<appml>
<datasource>
<xmlfile src="cd_catalog.xml">
<record>CD</record>
<item>
<name>Title</name>
<nodename>TITLE</nodename>
</item>
<item>
<name>Artist</name>
<nodename>ARTIST</nodename>
</item>
<item>
<name>Country</name>
<nodename>COUNTRY</nodename>
</item>
</xmlfile>
</datasource>
</appml>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryappml_from_xml)


此方法能够将数据存储在服务器上的XML文件。


---


## 数据存储在 文本（Text）文件中


 可以从文本文件中读取数据：


## 实例


```
<appml>
<datasource>
<csvfile src="cd_catalog.txt">
<item>
<name>Title</name>
<index>1</index>
</item>
<item>
<name>Artist</name>
<index>2</index>
</item>
<item>
<name>Price</name>
<index>5</index>
</item>
</csvfile>
</datasource>
</appml>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryappml_from_txt)


此方法可以在服务器上的将数据存储在文本文件中。



---


## 如果需要你可以创建数据库


 如果有需要你可以创建一个数据库：


<database>

<connection>CDDataBase</connection>


<execute>

CREATE TABLE CD_catalog
(
CD_Id INT IDENTITY,
Title NVARCHAR(255),
Artist NVARCHAR(255),
Country NVARCHAR(255),
Company NVARCHAR(255),
Price NUMBER,Published INT)

</execute>


</database>


完善快速原型模型！








	  AI 思考中...





			** [AppML 架构](https://www.runoob.com/appml-architecture.html)
			[AppML 案例简介](https://www.runoob.com/appml-case-intro.html) **













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