# R MySQL 连接

- Source: https://www.runoob.com/r/r-mysql-connect.html

MySQL 是最流行的关系型数据库管理系统，在 WEB 应用方面 MySQL 是最好的 RDBMS(Relational Database Management System：关系数据库管理系统)应用软件之一。


如果你对 MySQL 还不了解，可以先查阅：[MySQL 教程](https://www.runoob.com/../mysql/mysql-tutorial.html)


R 语言读写 MySQL 文件需要安装扩展包，我们可以在 R 到控制台输入以下命令来安装：


```
install.packages("RMySQL", repos = "https://mirrors.ustc.edu.cn/CRAN/")
```


查看是否安装成功：


```
> any(grepl("RMySQL",installed.packages()))
[1] TRUE
```


MySQL 目前被甲骨文收购，所以很多人使用来它的复制版本 MariaDB，MariaDB 在 GNU GPL下开源，MariaDB 的开发是由 MySQL 的一些原始开发者领导的，所以语法操作都差不多：


```
install.packages("RMariaDB", repos = "https://mirrors.ustc.edu.cn/CRAN/")
```
 在 test 数据库中创建数据表 runoob，表结构及数据代码如下：


## 实例


```r
--
-- 表的结构 `runoob`
--

CREATE TABLE `runoob` (
  `id` int(11) NOT NULL,
  `name` char(20) NOT NULL,
  `url` varchar(255) NOT NULL,
  `likes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `runoob`
--

INSERT INTO `runoob` (`id`, `name`, `url`, `likes`) VALUES
(1, 'Google', 'www.google.com', 111),
(2, 'Runoob', 'www.runoob.com', 222),
(3, 'Taobao', 'www.taobao.com', 333);
```


接下来我们可以使用 RMySQL 包来读取数据：


## 实例


```r
library(RMySQL)

# dbname 为数据库名，这边的参数请根据自己实际情况填写
mysqlconnection = dbConnect(MySQL(), user = 'root', password = '', dbname = 'test',host = 'localhost')

# 查看数据
dbListTables(mysqlconnection)
```


接下来我们可以使用 dbSendQuery 来读取数据库的表，结果集通过 fetch() 函数来获取：


## 实例


```r
library(RMySQL)
# 查询 sites 表，增删改查操作可以通过第二个参数的 SQL 语句来实现
result = dbSendQuery(mysqlconnection, "select * from sites")

# 获取前面两行数据
data.frame = fetch(result, n = 2)
print(data.frame)
```









	  AI 思考中...





			** [R JSON 文件](https://www.runoob.com/r-input-json-file.html)
			[R 绘图 – 饼图](https://www.runoob.com/r-pie-charts.html) **













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