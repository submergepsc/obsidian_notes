# C 标准库 -

- Source: https://www.runoob.com/cprogramming/c-standard-library-float-h.html

## 简介


`` 是 C 标准库中的一个头文件，定义了与浮点数类型（`float`、`double` 和 `long double`）相关的宏。这些宏提供了浮点数的特性和限制，例如最大值、最小值、精度等。


C 标准库的 **float.h** 头文件包含了一组与浮点值相关的依赖于平台的常量。这些常量是由 ANSI C 提出的，这让程序更具有可移植性。在讲解这些常量之前，最好先弄清楚浮点数是由下面四个元素组成的：


| 组件 | 组件描述 |
| --- | --- |
| S | 符号 ( +/- ) |
| b | 指数表示的基数，2 表示二进制，10 表示十进制，16 表示十六进制，等等... |
| e | 指数，一个介于最小值 emin 和最大值 emax 之间的整数。 |
| p | 精度，基数 b 的有效位数 |


基于以上 4 个组成部分，一个浮点数的值如下：


**floating-point = ( S ) p x be**

或

**floating-point = (+/-) precision x baseexponent**


## 库宏


下面的值是特定实现的，且是通过 #define 指令来定义的，这些值都不得低于下边所给出的值。请注意，所有的实例 FLT 是指类型 float，DBL 是指类型 double，LDBL 是指类型 long double。


#### 单精度浮点数（float）


- `FLT_RADIX`：浮点数的基数（通常为2）。
- `FLT_MANT_DIG`：`float` 类型的有效位数。
- `FLT_DIG`：`float` 类型的十进制数精度，即能保证不失真的最大十进制位数。
- `FLT_MIN_EXP`：`float` 类型的最小负指数（以基数为底）。
- `FLT_MIN_10_EXP`：`float` 类型的最小负十进制指数。
- `FLT_MAX_EXP`：`float` 类型的最大指数（以基数为底）。
- `FLT_MAX_10_EXP`：`float` 类型的最大十进制指数。
- `FLT_MAX`：`float` 类型的最大正值。
- `FLT_MIN`：`float` 类型的最小正值。
- `FLT_EPSILON`：`float` 类型的相对误差，即1.0和比1.0大的最小浮点数之差。


#### 双精度浮点数（double）


- `DBL_MANT_DIG`：`double` 类型的有效位数。
- `DBL_DIG`：`double` 类型的十进制数精度。
- `DBL_MIN_EXP`：`double` 类型的最小负指数（以基数为底）。
- `DBL_MIN_10_EXP`：`double` 类型的最小负十进制指数。
- `DBL_MAX_EXP`：`double` 类型的最大指数（以基数为底）。
- `DBL_MAX_10_EXP`：`double` 类型的最大十进制指数。
- `DBL_MAX`：`double` 类型的最大正值。
- `DBL_MIN`：`double` 类型的最小正值。
- `DBL_EPSILON`：`double` 类型的相对误差。


#### 扩展精度浮点数（long double）


- `LDBL_MANT_DIG`：`long double` 类型的有效位数。
- `LDBL_DIG`：`long double` 类型的十进制数精度。
- `LDBL_MIN_EXP`：`long double` 类型的最小负指数（以基数为底）。
- `LDBL_MIN_10_EXP`：`long double` 类型的最小负十进制指数。
- `LDBL_MAX_EXP`：`long double` 类型的最大指数（以基数为底）。
- `LDBL_MAX_10_EXP`：`long double` 类型的最大十进制指数。
- `LDBL_MAX`：`long double` 类型的最大正值。
- `LDBL_MIN`：`long double` 类型的最小正值。
- `LDBL_EPSILON`：`long double` 类型的相对误差。


## 实例


下面的实例演示了 float.h 文件中定义的一些常量的使用。


## 实例


```c
#include <stdio.h>
#include <float.h>

int main() {
    printf("Single precision (float):\n");
    printf("FLT_RADIX: %d\n", FLT_RADIX);
    printf("FLT_MANT_DIG: %d\n", FLT_MANT_DIG);
    printf("FLT_DIG: %d\n", FLT_DIG);
    printf("FLT_MIN_EXP: %d\n", FLT_MIN_EXP);
    printf("FLT_MIN_10_EXP: %d\n", FLT_MIN_10_EXP);
    printf("FLT_MAX_EXP: %d\n", FLT_MAX_EXP);
    printf("FLT_MAX_10_EXP: %d\n", FLT_MAX_10_EXP);
    printf("FLT_MAX: %e\n", FLT_MAX);
    printf("FLT_MIN: %e\n", FLT_MIN);
    printf("FLT_EPSILON: %e\n", FLT_EPSILON);

    printf("\nDouble precision (double):\n");
    printf("DBL_MANT_DIG: %d\n", DBL_MANT_DIG);
    printf("DBL_DIG: %d\n", DBL_DIG);
    printf("DBL_MIN_EXP: %d\n", DBL_MIN_EXP);
    printf("DBL_MIN_10_EXP: %d\n", DBL_MIN_10_EXP);
    printf("DBL_MAX_EXP: %d\n", DBL_MAX_EXP);
    printf("DBL_MAX_10_EXP: %d\n", DBL_MAX_10_EXP);
    printf("DBL_MAX: %e\n", DBL_MAX);
    printf("DBL_MIN: %e\n", DBL_MIN);
    printf("DBL_EPSILON: %e\n", DBL_EPSILON);

    printf("\nExtended precision (long double):\n");
    printf("LDBL_MANT_DIG: %d\n", LDBL_MANT_DIG);
    printf("LDBL_DIG: %d\n", LDBL_DIG);
    printf("LDBL_MIN_EXP: %d\n", LDBL_MIN_EXP);
    printf("LDBL_MIN_10_EXP: %d\n", LDBL_MIN_10_EXP);
    printf("LDBL_MAX_EXP: %d\n", LDBL_MAX_EXP);
    printf("LDBL_MAX_10_EXP: %d\n", LDBL_MAX_10_EXP);
    printf("LDBL_MAX: %Le\n", LDBL_MAX);
    printf("LDBL_MIN: %Le\n", LDBL_MIN);
    printf("LDBL_EPSILON: %Le\n", LDBL_EPSILON);

    return 0;
}
```


让我们编译和运行上面的程序，这将产生下列结果：


```
Single precision (float):
FLT_RADIX: 2
FLT_MANT_DIG: 24
FLT_DIG: 6
FLT_MIN_EXP: -125
FLT_MIN_10_EXP: -37
FLT_MAX_EXP: 128
FLT_MAX_10_EXP: 38
FLT_MAX: 3.402823e+38
FLT_MIN: 1.175494e-38
FLT_EPSILON: 1.192093e-07

Double precision (double):
DBL_MANT_DIG: 53
DBL_DIG: 15
DBL_MIN_EXP: -1021
DBL_MIN_10_EXP: -307
DBL_MAX_EXP: 1024
DBL_MAX_10_EXP: 308
DBL_MAX: 1.797693e+308
DBL_MIN: 2.225074e-308
DBL_EPSILON: 2.220446e-16

Extended precision (long double):
LDBL_MANT_DIG: 64
LDBL_DIG: 18
LDBL_MIN_EXP: -16381
LDBL_MIN_10_EXP: -4931
LDBL_MAX_EXP: 16384
LDBL_MAX_10_EXP: 4932
LDBL_MAX: 1.189731e+4932
LDBL_MIN: 3.362103e-4932
LDBL_EPSILON: 1.084202e-19
```


`` 提供了一组宏，用于描述浮点数类型的特性和限制。通过使用这些宏，我们可以编写更健壮的代码，处理与浮点数相关的边界情况和特殊情况。








	  AI 思考中...





			** [C 标准库 – ](https://www.runoob.com/c-standard-library-errno-h.html)
			[C 标准库 – ](https://www.runoob.com/c-standard-library-setjmp-h.html) **













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