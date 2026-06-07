# C 标准库 -

- Source: https://www.runoob.com/cprogramming/c-standard-library-time-h.html

## 简介


**time.h** 头文件定义了四个变量类型、两个宏和各种操作日期和时间的函数。


`` 是 C 标准库中的一个头文件，提供了处理和操作日期和时间的函数和类型。这个头文件中的函数用于获取当前时间、设置时间、格式化时间和计算时间差等。


### 常量与宏

| 常量/宏 | 说明 |
| --- | --- |
| CLOCKS_PER_SEC | 每秒的时钟周期数。 |
| NULL | 空指针常量。 |
| TIME_UTC | 表示 UTC 时间（C11）。 |


### 库变量


下面是头文件 time.h 中定义的变量类型：


| 序号 | 变量 & 描述 |
| --- | --- |
| 1 | size_t 是无符号整数类型，它是 sizeof 关键字的结果。 |
| 2 | clock_t 这是一个适合存储处理器时间的类型。 |
| 3 | time_t is 这是一个适合存储日历时间的类型。 |
| 4 | struct tm 这是一个用来保存时间和日期的结构。 |


tm 结构的定义如下：


```
struct tm {
   int tm_sec;         /* 秒，范围从 0 到 59        */
   int tm_min;         /* 分，范围从 0 到 59        */
   int tm_hour;        /* 小时，范围从 0 到 23        */
   int tm_mday;        /* 一月中的第几天，范围从 1 到 31    */
   int tm_mon;         /* 月，范围从 0 到 11        */
   int tm_year;        /* 自 1900 年起的年数        */
   int tm_wday;        /* 一周中的第几天，范围从 0 到 6    */
   int tm_yday;        /* 一年中的第几天，范围从 0 到 365    */
   int tm_isdst;       /* 夏令时                */
};
```


## 库宏


下面是头文件 time.h 中定义的宏：


| 序号 | 宏 & 描述 |
| --- | --- |
| 1 | NULL这个宏是一个空指针常量的值。 |
| 2 | CLOCKS_PER_SEC 这个宏表示每秒的处理器时钟个数。 |


## 库函数


下面是头文件 time.h 中定义的函数：


| 序号 | 函数 & 描述 |
| --- | --- |
| 1 | char *asctime(const struct tm *timeptr)返回一个指向字符串的指针，它代表了结构 timeptr 的日期和时间。 |
| 2 | clock_t clock(void)返回程序执行起（一般为程序的开头），处理器时钟所使用的时间。 |
| 3 | char *ctime(const time_t *timer)返回一个表示当地时间的字符串，当地时间是基于参数 timer。 |
| 4 | double difftime(time_t time1, time_t time2)返回 time1 和 time2 之间相差的秒数 (time1-time2)。 |
| 5 | struct tm *gmtime(const time_t *timer)timer 的值被分解为 tm 结构，并用协调世界时（UTC）也被称为格林尼治标准时间（GMT）表示。 |
| 6 | struct tm *localtime(const time_t *timer)timer 的值被分解为 tm 结构，并用本地时区表示。 |
| 7 | time_t mktime(struct tm *timeptr)把 timeptr 所指向的结构转换为一个依据本地时区的 time_t 值。 |
| 8 | size_t strftime(char *str, size_t maxsize, const char *format, const struct tm *timeptr)根据 format 中定义的格式化规则，格式化结构 timeptr 表示的时间，并把它存储在 str 中。 |
| 9 | time_t time(time_t *timer)计算当前日历时间，并把它编码成 time_t 格式。 |
| 10 | int timespec_get(struct timespec *ts, int base);获取当前时间（C11）。 |


### 实例


以下是使用 `` 中一些函数的示例。


获取当前时间：


## 实例


```c
#include <stdio.h>
#include <time.h>

int main() {
    time_t current_time;
    time(&current_time);
    printf("Current time: %s", ctime(&current_time));

    return 0;
}
```


格式化时间:


## 实例


```c
#include <stdio.h>
#include <time.h>

int main() {
    time_t current_time;
    struct tm *time_info;
    char buffer[80];

    time(&current_time);
    time_info = localtime(&current_time);

    strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", time_info);
    printf("Formatted time: %s\n", buffer);

    return 0;
}
```


计算时间差:


## 实例


```c
#include <stdio.h>
#include <time.h>

int main() {
    time_t start_time, end_time;
    double time_diff;

    time(&start_time);
    // 模拟一个耗时操作
    for (int i = 0; i < 100000000; i++);

    time(&end_time);
    time_diff = difftime(end_time, start_time);
    printf("Time difference: %.2f seconds\n", time_diff);

    return 0;
}
```


使用 **struct tm**:


## 实例


```c
#include <stdio.h>
#include <time.h>

int main() {
    struct tm time_info;
    char buffer[80];

    time_info.tm_year = 2024 - 1900;  // 年份从 1900 年开始计算
    time_info.tm_mon = 5;             // 六月，范围从 0 到 11
    time_info.tm_mday = 12;
    time_info.tm_hour = 12;
    time_info.tm_min = 0;
    time_info.tm_sec = 0;
    time_info.tm_isdst = -1;          // 自动判断是否为夏令时

    mktime(&time_info);

    strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", &time_info);
    printf("Custom time: %s\n", buffer);

    return 0;
}
```


### 注意事项

- 使用 `localtime` 和 `gmtime` 时，返回的指针指向的 `struct tm` 结构是静态存储的，每次调用会覆盖之前的内容。
- 使用 `mktime` 函数时，必须确保 `struct tm` 中的各个字段是合法的。
- 使用 `strftime` 函数进行时间格式化时，要确保目标缓冲区足够大，以避免缓冲区溢出。

通过理解和使用 `` 提供的函数，可以方便地进行时间和日期的操作，从而编写更加功能丰富和高效的 C 程序。








	  AI 思考中...





			** [C 标准库 – ](https://www.runoob.com/c-standard-library-string-h.html)
			[C 库宏 – assert()](https://www.runoob.com/c-macro-assert.html) **













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