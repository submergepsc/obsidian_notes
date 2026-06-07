# PostgreSQL 运算符

- Source: https://www.runoob.com/postgresql/postgresql-operators.html

运算符是一种告诉编译器执行特定的数学或逻辑操作的符号。


PostgreSQL 运算符是一个保留关键字或字符，一般用在 WHERE 语句中，作为过滤条件。


常见的运算符有：


- 算术运算符
- 比较运算符
- 逻辑运算符
- 按位运算符


---


## 算术运算符


假设变量 a 为 2，变量 b 为 3，则：


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| + | 加 | a + b 结果为 5 |
| - | 减 | a - b 结果为 -1 |
| * | 乘 | a * b 结果为 6 |
| / | 除 | b / a 结果为 1 |
| % | 模（取余） | b % a 结果为 1 |
| ^ | 指数 | a ^ b 结果为 8 |
| \|/ | 平方根 | \|/ 25.0 结果为 5 |
| \|\|/ | 立方根 | \|\|/ 27.0 结果为 3 |
| ! | 阶乘 | 5 ! 结果为 120 |
| !! | 阶乘（前缀操作符） | !! 5 结果为 120 |


### 实例


```
runoobdb=# select 2+3;
 ?column?
----------
        5
(1 row)


runoobdb=# select 2*3;
 ?column?
----------
        6
(1 row)


runoobdb=# select 10/5;
 ?column?
----------
        2
(1 row)


runoobdb=# select 12%5;
 ?column?
----------
        2
(1 row)


runoobdb=# select 2^3;
 ?column?
----------
        8
(1 row)


runoobdb=# select |/ 25.0;
 ?column?
----------
        5
(1 row)


runoobdb=# select ||/ 27.0;
 ?column?
----------
        3
(1 row)


runoobdb=# select 5 !;
 ?column?
----------
      120
(1 row)


runoobdb=# select !!5;
 ?column?
----------
      120
(1 row)
```


---


## 比较运算符


假设变量 a 为 10，变量 b 为 20，则：


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| = | 等于 | (a = b) 为 false。 |
| != | 不等于 | (a != b) 为 true。 |
|  | 不等于 | (a b) 为 true。 |
| > | 大于 | (a > b) 为 false。 |
| = | 大于等于 | (a >= b) 为 false。 |
| > | 二进制右移运算符。将一个数的各二进制位全部右移若干位，正数左补0，负数左补1，右边丢弃。 | A >> 2 将得到 15，即为 0000 1111 |


### 实例


```
runoobdb=# select 60 | 13;
 ?column?
----------
       61
(1 row)


runoobdb=# select 60 & 13;
 ?column?
----------
       12
(1 row)


runoobdb=#  select  (~60);
 ?column?
----------
      -61
(1 row)


runoobdb=# select  (60 << 2);
 ?column?
----------
      240
(1 row)


runoobdb=# select  (60 >> 2);
 ?column?
----------
       15
(1 row)


runoobdb=#  select 60 # 13;
 ?column?
----------
       49
(1 row)
```









	  AI 思考中...





			** [PostgreSQL SELECT 语句](https://www.runoob.com/postgresql-select.html)
			[PostgreSQL 表达式](https://www.runoob.com/postgresql-expressions.html) **













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