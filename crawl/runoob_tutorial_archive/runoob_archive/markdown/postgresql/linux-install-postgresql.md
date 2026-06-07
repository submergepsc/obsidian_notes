# Linux 上安装 PostgreSQL

- Source: https://www.runoob.com/postgresql/linux-install-postgresql.html

打开 PostgreSQL 官网 [https://www.postgresql.org/](https://www.postgresql.org/)，点击菜单栏上的 **Download** ，可以看到这里包含了很多平台的安装包，包括 Linux、Windows、Mac OS等 。


Linux 我们可以看到支持 Ubuntu 和 Red Hat 等各个平台，点击具体的平台链接，即可查看安装方法：


![](https://www.runoob.com/wp-content/uploads/2019/05/28AD14E3-B089-4235-A2ED-626CE011E4EC.jpg)


点击上图中的 **file browser**，我们还能下载 PostgreSQL 最新的源码。 ![](https://www.runoob.com/wp-content/uploads/2019/05/235E36B8-603B-4335-B3A6-26F0C9A3910A.jpg)


本章节以 Ubuntu 为例。


### Ubuntu 安装 PostgreSQL


Ubuntu 可以使用 apt-get 安装 PostgreSQL：


```
sudo apt-get update
sudo apt-get install postgresql postgresql-client
```


安装完毕后，系统会创建一个数据库超级用户 postgres，密码为空。


```
#  sudo -i -u postgres
```


这时使用以下命令进入 postgres，输出以下信息，说明安装成功：


```
~$ psql
psql (9.5.17)
Type "help" for help.

postgres=#
```


输入以下命令退出 PostgreSQL 提示符：


```
\q
```


PostgreSQL 安装完成后默认是已经启动的，但是也可以通过下面的方式来手动启动服务。


```
sudo /etc/init.d/postgresql start   # 开启
sudo /etc/init.d/postgresql stop    # 关闭
sudo /etc/init.d/postgresql restart # 重启
```










	  AI 思考中...





			** [PostgreSQL 教程](https://www.runoob.com/postgresql-tutorial.html)
			[Windows 上安装 PostgreSQL](https://www.runoob.com/windows-install-postgresql.html) **













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