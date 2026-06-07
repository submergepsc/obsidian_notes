# C 标准库 -

- Source: https://www.runoob.com/cprogramming/c-standard-library-ctype-h.html

## 简介


C 标准库的 **ctype.h** 头文件提供了一些函数，可用于测试和转换字符，这些函数主要用于检查字符的类型（如字母、数字、空白字符等）以及进行字符大小写转换。


`` 提供了一组方便的函数，用于处理字符的分类和转换操作，是 C 标准库中处理字符操作的重要工具。


以下是一个简单的示例，演示了如何使用 `` 提供的函数：


## 实例


```c
#include <stdio.h>
#include <ctype.h>

int main() {
    char ch;

    // 示例字符
    char chars[] = "a1 B? \n";

    // 检查每个字符的类型
    for (int i = 0; chars[i] != '\0'; i++) {
        ch = chars[i];
        printf("Character: '%c'\n", ch);
        if (isalpha(ch)) {
            printf(" - isalpha: Yes\n");
        } else {
            printf(" - isalpha: No\n");
        }
        if (isdigit(ch)) {
            printf(" - isdigit: Yes\n");
        } else {
            printf(" - isdigit: No\n");
        }
        if (isspace(ch)) {
            printf(" - isspace: Yes\n");
        } else {
            printf(" - isspace: No\n");
        }
        if (isprint(ch)) {
            printf(" - isprint: Yes\n");
        } else {
            printf(" - isprint: No\n");
        }
        if (ispunct(ch)) {
            printf(" - ispunct: Yes\n");
        } else {
            printf(" - ispunct: No\n");
        }
    }

    // 字符大小写转换示例
    char lower = 'a';
    char upper = 'A';

    printf("tolower('%c') = '%c'\n", upper, tolower(upper));
    printf("toupper('%c') = '%c'\n", lower, toupper(lower));

    return 0;
}
```


输出结果为：


```
Character: 'a'
 - isalpha: Yes
 - isdigit: No
 - isspace: No
 - isprint: Yes
 - ispunct: No
Character: '1'
 - isalpha: No
 - isdigit: Yes
 - isspace: No
 - isprint: Yes
 - ispunct: No
Character: ' '
 - isalpha: No
 - isdigit: No
 - isspace: Yes
 - isprint: Yes
 - ispunct: No
Character: 'B'
 - isalpha: Yes
 - isdigit: No
 - isspace: No
 - isprint: Yes
 - ispunct: No
Character: '?'
 - isalpha: No
 - isdigit: No
 - isspace: No
 - isprint: Yes
 - ispunct: Yes
Character: '
'
 - isalpha: No
 - isdigit: No
 - isspace: Yes
 - isprint: No
 - ispunct: No
tolower('A') = 'a'
toupper('a') = 'A'
```


## 库函数


下面列出了头文件 ctype.h 中定义的函数。


这些函数用于测试字符是否属于某种类型，这些函数接受 **int** 作为参数，它的值必须是 EOF 或表示为一个无符号字符。


如果参数 c 满足描述的条件，则这些函数返回非零（true）。如果参数 c 不满足描述的条件，则这些函数返回零。


| 序号 | 函数 & 描述 |
| --- | --- |
| 1 | int isalnum(int c)该函数检查所传的字符是否是字母和数字。 |
| 2 | int isalpha(int c)该函数检查所传的字符是否是字母。 |
| 3 | int iscntrl(int c)该函数检查所传的字符是否是控制字符。 |
| 4 | int isdigit(int c)该函数检查所传的字符是否是十进制数字。 |
| 5 | int isgraph(int c)该函数检查所传的字符是否有图形表示法。 |
| 6 | int islower(int c)该函数检查所传的字符是否是小写字母。 |
| 7 | int isprint(int c)该函数检查所传的字符是否是可打印的。 |
| 8 | int ispunct(int c)该函数检查所传的字符是否是标点符号字符。 |
| 9 | int isspace(int c)该函数检查所传的字符是否是空白字符。 |
| 10 | int isupper(int c)该函数检查所传的字符是否是大写字母。 |
| 11 | int isxdigit(int c)该函数检查所传的字符是否是十六进制数字。 |


标准库还包含了两个转换函数，它们接受并返回一个 "int"


| 序号 | 函数 & 描述 |
| --- | --- |
| 1 | int tolower(int c)该函数把大写字母转换为小写字母。 |
| 2 | int toupper(int c)该函数把小写字母转换为大写字母。 |


## 字符类


| 序号 | 字符类 & 描述 |
| --- | --- |
| 1 | 数字完整的数字集合 { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 } |
| 2 | 十六进制数字集合 { 0 1 2 3 4 5 6 7 8 9 A B C D E F a b c d e f } |
| 3 | 小写字母集合 { a b c d e f g h i j k l m n o p q r s t u v w x y z } |
| 4 | 大写字母集合 {A B C D E F G H I J K L M N O P Q R S T U V W X Y Z } |
| 5 | 字母小写字母和大写字母的集合 |
| 6 | 字母数字字符数字、小写字母和大写字母的集合 |
| 7 | 标点符号字符集合 ! " # $ % & ' ( ) * + , - . / : ; ? @ [ \ ] ^ _ ` { \| } ~ |
| 8 | 图形字符字母数字字符和标点符号字符的集合 |
| 9 | 空格字符制表符、换行符、垂直制表符、换页符、回车符、空格符的集合。 |
| 10 | 可打印字符字母数字字符、标点符号字符和空格字符的集合。 |
| 11 | 控制字符在 ASCII 编码中，这些字符的八进制代码是从 000 到 037，以及 177（DEL）。 |
| 12 | 空白字符包括空格符和制表符。 |
| 13 | 字母字符小写字母和大写字母的集合。 |








	  AI 思考中...





			** [C 标准库 – ](https://www.runoob.com/c-standard-library-assert-h.html)
			[C 标准库 – ](https://www.runoob.com/c-standard-library-errno-h.html) **













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