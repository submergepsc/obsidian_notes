# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-ctime.html

C++ 标准库提供了丰富的功能，其中 `` 是处理时间和日期的标准库之一。它提供了一组函数，用于获取当前时间、日期以及执行时间相关的计算。


`` 库定义了一组与时间相关的函数和类型，这些函数和类型允许程序员在程序中处理时间。它包括：


- `time_t`：表示时间的类型，通常是一个长整型。
- `tm`：一个结构体，用于表示时间的各个部分，如年、月、日、小时等。
- 一系列函数，如 `time()`, `localtime()`, `gmtime()`, `strftime()` 等。


## 语法


以下是 `` 库中一些常用函数的基本语法：


- 获取当前时间（以秒为单位，从1970年1月1日开始计算）：
```
time_t t = time(NULL);
```

- 将 `time_t` 类型的时间转换为 `tm` 结构体：
```
struct tm *tm = localtime(&t);
```

- 将 `time_t` 类型的时间转换为协调世界时（UTC）的 `tm` 结构体：
```
struct tm *tm_utc = gmtime(&t);
```

- 格式化时间：
```
char buffer[80];
strftime(buffer, 80, "%Y-%m-%d %H:%M:%S", tm);
```


## 实例


下面是一个使用 `` 库的简单示例，展示如何获取当前时间并格式化输出。


## 实例


```cpp
#include <iostream>
#include <ctime>
#include <iomanip>
#include <sstream>

int main() {
    // 获取当前时间
    time_t now = time(NULL);

    // 将当前时间转换为本地时间
    struct tm *local_tm = localtime(&now);

    // 使用 strftime 格式化时间
    char buffer[80];
    strftime(buffer, 80, "%Y-%m-%d %H:%M:%S", local_tm);

    // 输出当前时间
    std::cout << "Current local time: " << buffer << std::endl;

    // 将当前时间转换为UTC时间
    struct tm *utc_tm = gmtime(&now);

    // 格式化UTC时间
    strftime(buffer, 80, "%Y-%m-%d %H:%M:%S", utc_tm);

    // 输出UTC时间
    std::cout << "Current UTC time: " << buffer << std::endl;

    return 0;
}
```


运行上述程序，你将看到类似以下的输出（具体时间取决于你运行程序的时间）：


```
Current local time: 2023-04-01 12:34:56
Current UTC time: 2023-04-01 12:34:56
```


请注意，由于时区差异，本地时间和UTC时间可能相同，也可能不同。


`` 库是 C++ 中处理时间和日期的重要工具。通过上述示例，我们可以看到如何使用 `` 库来获取和格式化当前时间。这在开发需要时间信息的应用程序时非常有用，例如日志记录、定时任务等。希望这篇文章能帮助初学者更好地理解和使用 `` 库。








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-chrono.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-regex.html) **













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