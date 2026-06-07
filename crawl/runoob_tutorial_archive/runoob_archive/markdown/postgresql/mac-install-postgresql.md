# 

- Source: https://www.runoob.com/postgresql/mac-install-postgresql.html

## Mac OS 上安装 PostgreSQL


使用 EnterpriseDB 来下载安装，EnterpriseDB 是全球唯一一家提供基于 PostgreSQL 企业级产品与服务的厂商。


下载地址：[https://www.enterprisedb.com/downloads/postgres-postgresql-downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)。


![](https://www.runoob.com/wp-content/uploads/2019/05/48D4B0D8-4B9C-4C63-A533-7893AD084319.jpg)


下载 postgresql-****-osx.dmg 文件，双击安装文件：


![](https://www.runoob.com/wp-content/uploads/2019/05/A5DB76D0-948A-45E3-9CC5-1184963806F4.jpg)


这时会要求你输入管理员密码，输入即可，之后弹出安装向导：


![](https://www.runoob.com/wp-content/uploads/2019/05/5C240279-9C03-4F49-BE44-05D6FA5961CF.jpg)


接下来就是一些基本的配置，比如：安装目录、扩展安装、数据库目录、用户密码、端口设置等，一般使用默认的就好，直接点 Next：


![](https://www.runoob.com/wp-content/uploads/2019/05/psql.gif)


最后，点击 Finish 即可：


![](https://www.runoob.com/wp-content/uploads/2019/05/0DE638F4-B631-412C-9C41-98B706B6FBC2.jpg)


执行以下脚本启动 PostgreSQL。


以下几个选项你可以自己输入，或者用默认的，默认回车就行，密码的地方为刚才你在安装过程中设置的密码：


```
$ /Library/PostgreSQL/11/scripts/runpsql.sh ;exit
Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Password for user postgres:
psql (11.3)
Type "help" for help.

postgres=#
```


![](https://www.runoob.com/wp-content/uploads/2019/05/8E6381B7-9646-4934-BA32-F5C01B3DB12C.jpg)


### pgAdmin 4


**打开 pgAdmin 4：**

![](https://www.runoob.com/wp-content/uploads/2019/05/9F82C8C5-7588-40A8-91A9-EB097288A7AE.jpg)


或者在屏幕右上方点击大象头像的图标：


![](https://www.runoob.com/wp-content/uploads/2019/05/C1D23400-B7CD-4E94-B19B-BC2F1A46C723.jpg)


pgAdmin 主页如下

![](https://www.runoob.com/wp-content/uploads/2019/05/1558508886-8320-080418-0846-HowtoDownlo15.png)

**点击左侧的 Servers > Postgre SQL 10 **

![](https://www.runoob.com/wp-content/uploads/2019/05/1558508887-9542-080418-0846-HowtoDownlo16.png)

**输入密码，点击 OK 即可**

![](https://www.runoob.com/wp-content/uploads/2019/05/1558508890-7567-080418-0846-HowtoDownlo17.png)

控制面板如下

![](https://www.runoob.com/wp-content/uploads/2019/05/1558508891-7409-080418-0846-HowtoDownlo18.png)









	  AI 思考中...





			** [Windows 上安装 PostgreSQL](https://www.runoob.com/windows-install-postgresql.html)
			[PostgreSQL 语法](https://www.runoob.com/postgresql-syntax.html) **













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