# ASP.NET MVC - SQL 数据库

- Source: https://www.runoob.com/aspnet/mvc-database.html

---


为了学习 ASP.NET MVC，我们将构建一个 Internet 应用程序。


第 6 部分：添加数据库。


---


## 创建数据库


Visual Web Developer 带有名为 SQL Server Compact 免费的 SQL 数据库。


本教程所需的这个数据库可以通过以下几个简单的步骤来创建：


- 右击 **Solution Explorer** 窗口中的 **App_Data** 文件夹
- 选择 **Add, New Item**
- 选择 **SQL Server Compact Local Database ***
- 将数据库命名为 **Movies.sdf**
- 点击 **Add** 按钮


***** 如果选项中没有 SQL Server Compact Local Database，则说明您尚未在计算机上安装 SQL Server Compac。请通过以下链接进行安装：[SQL Server Compact](http://www.microsoft.com/web/gallery/install.aspx?appid=SQLCE;SQLCEVSTools_4_0)


Visual Web Developer 会自动在 App_Data 文件夹中创建该数据库。


**注释：**在本教程中，需要您掌握一些关于 SQL 数据库的基础知识。如果您想先学习这个主题，请访问我们的 SQL 教程。


---


## 添加数据库表


双击 **App_Data** 文件夹中的 **Movies.sdf** 文件，将打开 **Database Explorer** 窗口。


如需在数据库中创建一个新的表，请右击 **Tables** 文件夹，然后选择 **Create Table**。


创建如下的列：


| 列 | 类型 | 是否允许为 Null |
| --- | --- | --- |
| ID | int (primary key) | No |
| Title | nvarchar(100) | No |
| Director | nvarchar(100) | No |
| Date | datetime | No |


对列的解释：


**ID** 是用于标识表中每条记录的整数（全数字）。


**Title** 是 100 个字符长度的文本列，用于存储影片的名称。


**Director** 是 100 个字符长度的文本列，用于存储导演的名字。


**Date** 是日期列，用于存储影片的发布日期。


在创建好上述列之后，您必须将 ID 列设置为表的主键（记录标识符）。要做到这点，请点击列名（ID），并选择 **Primary Key**。在 ** Column Properties** 窗口中，设置 **Identity** 属性为 ** True**：


![DB Explorer](https://www.runoob.com/wp-content/uploads/2013/08/pic_mvc_dbexplorer.jpg)


当您创建好表列后，保存表并命名为 **MovieDBs**。


**注释：**


我们特意把表命名为 "MovieDBs"（以 s 结尾）。在下一章中，您将看到用于数据模型的 "MovieDB"。这看起来有点奇怪，不过这种命名惯例能确保控制器连接上数据库表，您必须这么使用。


---


## 添加数据库记录


您可以使用 Visual Web Developer 向 movie 数据库中添加一些测试记录。


双击 **App_Data** 文件夹中的 **Movies.sdf** 文件。


右击 Database Explorer 窗口中的 **MovieDBs** 表，并选择 **Show Table Data**。


添加一些记录：


| ID | Title | Director | Date |
| --- | --- | --- | --- |
| 1 | Psycho | Alfred Hitchcock | 01.01.1960 |
| 2 | La Dolce Vita | Federico Fellini | 01.01.1960 |


**注释：**ID 列会自动更新，您可以不用编辑它。


---


## 添加连接字符串


向您的 **Web.config** 文件中的 **** 元素添加如下元素：


<add name="MovieDBContext"**connectionString="Data
	Source=|DataDirectory|Movies.sdf"
providerName="System.Data.SqlServerCe.4.0"/>










	  AI 思考中...





			** [ASP.NET MVC 视图](https://www.runoob.com/mvc-views.html)
			[ASP.NET MVC 模型](https://www.runoob.com/mvc-models.html) **













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