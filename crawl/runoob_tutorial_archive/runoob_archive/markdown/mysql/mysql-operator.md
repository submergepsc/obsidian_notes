# MySQL 运算符

- Source: https://www.runoob.com/mysql/mysql-operator.html

本章节我们主要介绍 MySQL 的运算符及运算符的优先级。


MySQL 主要有以下几种运算符：

- 算术运算符
- 比较运算符
- 逻辑运算符
- 位运算符


---


## 算术运算符


MySQL 支持的算术运算符包括:


| 运算符 | 作用 |
| --- | --- |
| + | 加法 |
| - | 减法 |
| * | 乘法 |
| / 或 DIV | 除法 |
| % 或 MOD | 取余 |


在除法运算和模运算中，如果除数为0，将是非法除数，返回结果为NULL。


1、加


```
mysql> select 1+2;
+-----+
| 1+2 |
+-----+
|   3 |
+-----+
```


2、减


```
mysql> select 1-2;
+-----+
| 1-2 |
+-----+
|  -1 |
+-----+
```


3、乘


```
mysql> select 2*3;
+-----+
| 2*3 |
+-----+
|   6 |
+-----+
```


4、除


```
mysql> select 2/3;
+--------+
| 2/3    |
+--------+
| 0.6667 |
+--------+
```


5、商


```
mysql> select 10 DIV 4;
+----------+
| 10 DIV 4 |
+----------+
|        2 |
+----------+
```


6、取余


```
mysql> select 10 MOD 4;
+----------+
| 10 MOD 4 |
+----------+
|        2 |
+----------+
```


---


## 比较运算符


SELECT 语句中的条件语句经常要使用比较运算符。通过这些比较运算符，可以判断表中的哪些记录是符合条件的。比较结果为真，则返回 1，为假则返回 0，比较结果不确定则返回 NULL。


| 符号 | 描述 | 备注 |
| --- | --- | --- |
| = | 等于 |  |
| , != | 不等于 |  |
| > | 大于 |  |
| = | 大于等于 |  |
| BETWEEN | 在两值之间 | >=min&&> | 右移 |


1、按位与


```
mysql> select 3&5;
+-----+
| 3&5 |
+-----+
|   1 |
+-----+
```


2、按位或


```
mysql> select 3|5;
+-----+
| 3|5 |
+-----+
|   7 |
+-----+
```


3、按位异或


```
mysql> select 3^5;
+-----+
| 3^5 |
+-----+
|   6 |
+-----+
```


4、按位取反


```
mysql> select ~18446744073709551612;
+-----------------------+
| ~18446744073709551612 |
+-----------------------+
|                     3 |
+-----------------------+
```


5、按位右移


```
mysql> select 3>>1;
+------+
| 3>>1 |
+------+
|    1 |
+------+
```


6、按位左移


```
mysql> select 3<<1;
+------+
| 3<<1 |
+------+
|    6 |
+------+
```


---

## 运算符优先级


最低优先级为： **:=**。


![](https://www.runoob.com/wp-content/uploads/2018/11/1011652-20170416163043227-1936139924.png)


最高优先级为： **!**、**BINARY**、 **COLLATE**。








	  AI 思考中...





			** [MySQL IFNULL() 函数](https://www.runoob.com/mysql-func-ifnull.html)
			[MySQL 命令大全](https://www.runoob.com/mysql-command-manual.html) **













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