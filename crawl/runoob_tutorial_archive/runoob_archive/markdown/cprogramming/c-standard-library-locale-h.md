# C 标准库 -

- Source: https://www.runoob.com/cprogramming/c-standard-library-locale-h.html

## 简介


`` 是 C 标准库中的一个头文件，用于支持程序的国际化和本地化。它提供了一组函数和宏来设置或查询程序的本地化信息，例如日期、时间、货币、数字格式等。


接下来我们将介绍一些宏，以及一个重要的结构 **struct lconv** 和两个重要的函数。


## 库宏


下面列出了头文件 locale.h 中定义的宏，这些宏将在下列的两个函数中使用：


| 序号 | 宏 & 描述 |
| --- | --- |
| 1 | LC_ALL用于设置或查询所有本地化类别。 |
| 2 | LC_COLLATE用于设置或查询字符串比较的本地化信息。 |
| 3 | LC_CTYPE用于设置或查询字符处理的本地化信息。 |
| 4 | LC_MONETARY用于设置或查询货币格式的本地化信息。 |
| 5 | LC_NUMERIC用于设置或查询数字格式的本地化信息（例如小数点的符号）。 |
| 6 | LC_TIME用于设置或查询时间格式的本地化信息。 |
| 7 | locale_t表示区域设置信息的类型。 |


## 库函数


下面列出了头文件 locale.h 中定义的函数：


| 序号 | 函数 & 描述 |
| --- | --- |
| 1 | char *setlocale(int category, const char *locale)设置或读取地域化信息。 |
| 2 | struct lconv *localeconv(void)设置或读取地域化信息。 |
| 3 | locale_t newlocale(int category_mask, const char *locale, locale_t base)创建一个新的本地化对象。 |
| 4 | freelocale(locale_t locale)释放一个本地化对象。 |
| 5 | locale_t uselocale(locale_t newloc)设置或查询线程的本地化对象。 |

### 实例


设置和查询本地化信息:


## 实例


```c
#include <stdio.h>
#include <locale.h>

int main() {
    // 设置本地化信息为用户环境变量中的默认设置
    setlocale(LC_ALL, "");

    // 获取和打印当前的本地化信息
    printf("Current locale for LC_ALL: %s\n", setlocale(LC_ALL, NULL));
    printf("Current locale for LC_TIME: %s\n", setlocale(LC_TIME, NULL));
    printf("Current locale for LC_NUMERIC: %s\n", setlocale(LC_NUMERIC, NULL));

    return 0;
}
```


编译输出结果为：


```
Current locale for LC_ALL: zh_CN.UTF-8
Current locale for LC_TIME: zh_CN.UTF-8
Current locale for LC_NUMERIC: zh_CN.UTF-8
```


获取数字和货币格式信息:


## 实例


```c
#include <stdio.h>
#include <locale.h>

int main() {
    // 设置本地化信息为用户环境变量中的默认设置
    setlocale(LC_ALL, "");

    // 获取本地化的数字和货币格式信息
    struct lconv *lc = localeconv();

    // 打印数字和货币格式信息
    printf("Decimal point character: %s\n", lc->decimal_point);
    printf("Thousands separator: %s\n", lc->thousands_sep);
    printf("Currency symbol: %s\n", lc->currency_symbol);

    return 0;
}
```


编译输出结果为：


```
Decimal point character: .
Thousands separator: ,
Currency symbol: ￥
```


使用自定义本地化对象:


## 实例


```c
#include <stdio.h>
#include <locale.h>
#include <xlocale.h>

int main() {
    // 创建一个新的本地化对象，使用 "en_US.UTF-8" 区域设置
    locale_t newloc = newlocale(LC_ALL_MASK, "en_US.UTF-8", (locale_t)0);

    // 将当前线程的本地化对象设置为新的本地化对象
    locale_t oldloc = uselocale(newloc);

    // 获取和打印当前线程的本地化信息
    printf("Current locale for LC_NUMERIC: %s\n", setlocale(LC_NUMERIC, NULL));

    // 释放新的本地化对象
    uselocale(oldloc);
    freelocale(newloc);

    return 0;
}
```


编译输出结果为：


```
Current locale for LC_NUMERIC: C
```


## 库结构
```
typedef struct {
   char *decimal_point;
   char *thousands_sep;
   char *grouping;
   char *int_curr_symbol;
   char *currency_symbol;
   char *mon_decimal_point;
   char *mon_thousands_sep;
   char *mon_grouping;
   char *positive_sign;
   char *negative_sign;
   char int_frac_digits;
   char frac_digits;
   char p_cs_precedes;
   char p_sep_by_space;
   char n_cs_precedes;
   char n_sep_by_space;
   char p_sign_posn;
   char n_sign_posn;
} lconv
```
 以下是各字段的描述：


| 序号 | 字段 & 描述 |
| --- | --- |
| 1 | decimal_point用于非货币值的小数点字符。 |
| 2 | thousands_sep用于非货币值的千位分隔符。 |
| 3 | grouping一个表示非货币量中每组数字大小的字符串。每个字符代表一个整数值，每个整数指定当前组的位数。值为 0 意味着前一个值将应用于剩余的分组。 |
| 4 | int_curr_symbol国际货币符号使用的字符串。前三个字符是由 ISO 4217:1987 指定的，第四个字符用于分隔货币符号和货币量。 |
| 5 | currency_symbol用于货币的本地符号。 |
| 6 | mon_decimal_point用于货币值的小数点字符。 |
| 7 | mon_thousands_sep用于货币值的千位分隔符。 |
| 8 | mon_grouping一个表示货币值中每组数字大小的字符串。每个字符代表一个整数值，每个整数指定当前组的位数。值为 0 意味着前一个值将应用于剩余的分组。 |
| 9 | positive_sign用于正货币值的字符。 |
| 10 | negative_sign用于负货币值的字符。 |
| 11 | int_frac_digits国际货币值中小数点后要显示的位数。 |
| 12 | frac_digits货币值中小数点后要显示的位数。 |
| 13 | p_cs_precedes如果等于 1，则 currency_symbol 出现在正货币值之前。如果等于 0，则 currency_symbol 出现在正货币值之后。 |
| 14 | p_sep_by_space如果等于 1，则 currency_symbol 和正货币值之间使用空格分隔。如果等于 0，则 currency_symbol 和正货币值之间不使用空格分隔。 |
| 15 | n_cs_precedes如果等于 1，则 currency_symbol 出现在负货币值之前。如果等于 0，则 currency_symbol 出现在负货币值之后。 |
| 16 | n_sep_by_space如果等于 1，则 currency_symbol 和负货币值之间使用空格分隔。如果等于 0，则 currency_symbol 和负货币值之间不使用空格分隔。 |
| 17 | p_sign_posn表示正货币值中正号的位置。 |
| 18 | n_sign_posn表示负货币值中负号的位置。 |


下面的值用于 **p_sign_posn** 和 **n_sign_posn**:


| 值 | 描述 |
| --- | --- |
| 0 | 封装值和 currency_symbol 的括号。 |
| 1 | 放置在值和 currency_symbol 之前的符号。 |
| 2 | 放置在值和 currency_symbol 之后的符号。 |
| 3 | 紧挨着放置在值和 currency_symbol 之前的符号。 |
| 4 | 紧挨着放置在值和 currency_symbol 之后的符号。 |








	  AI 思考中...





			** [C 标准库 – ](https://www.runoob.com/c-standard-library-limits-h.html)
			[C 标准库 – ](https://www.runoob.com/c-standard-library-math-h.html) **













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