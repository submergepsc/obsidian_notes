# C 标准库 -

- Source: https://www.runoob.com/cprogramming/c-standard-library-stddef-h.html

## 简介


**stddef .h** 头文件定义了各种变量类型和宏，这些定义和宏主要用于内存管理、对象大小、和指针算术等方面。


## 库变量


下面是头文件 stddef.h 中定义的变量类型：


| 序号 | 变量 & 描述 |
| --- | --- |
| 1 | ptrdiff_tptrdiff_t 是一种有符号整数类型，用于表示两个指针之间的差值。其定义同样依赖于实现，通常是 int 或 long。
```
ptrdiff_t diff = ptr2 - ptr1; // 计算两个指针之间的差值
```
 |
| 2 | size_t 这是无符号整数类型，它是 sizeof 关键字的结果，通常用来表示对象的大小或数组的索引。其定义依赖于实现，通常是 unsigned int 或 unsigned long。
```
size_t size = sizeof(int); // 获取 int 类型的大小
```
 |
| 3 | wchar_t 这是一个宽字符常量大小的整数类型，用于表示多字节字符。其大小和表示方式依赖于具体实现。
```
wchar_t wideChar = L'A'; // 宽字符常量
```
 |


## 库宏


下面是头文件 stddef.h 中定义的宏：


| 序号 | 宏 & 描述 |
| --- | --- |
| 1 | NULL这个宏是一个空指针常量的值。 |
| 2 | offsetof(type, member-designator)这会生成一个类型为 size_t 的整型常量，它是一个结构成员相对于结构开头的字节偏移量。成员是由 member-designator 给定的，结构的名称是在 type 中给定的。 |








	  AI 思考中...





			** [C 标准库 – ](https://www.runoob.com/c-standard-library-stdarg-h.html)
			[C 标准库 – ](https://www.runoob.com/c-standard-library-stdio-h.html) **













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