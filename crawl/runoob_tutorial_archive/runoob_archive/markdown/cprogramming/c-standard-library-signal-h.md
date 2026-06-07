# C 标准库 -

- Source: https://www.runoob.com/cprogramming/c-standard-library-signal-h.html

## 简介


`` 是 C 标准库中的一个头文件，用于处理信号。

**signal.h** 头文件定义了一个变量类型 **sig_atomic_t**、两个函数调用和一些宏来处理程序执行期间报告的不同信号。


信号是一种异步通知机制，允许进程在特定事件发生时执行预定义的处理函数。


下面是一个简单的示例程序，演示如何使用 signal 函数来捕捉 SIGINT 信号（通常由 Ctrl+C 产生）。


## 实例


```c
#include <stdio.h>
#include <signal.h>
#include <unistd.h>

// 全局变量，指示程序是否应退出
volatile sig_atomic_t stop = 0;

void handle_sigint(int sig) {
    printf("Caught signal %d\n", sig);
    stop = 1; // 设置退出标志
}

int main() {
    // 将 SIGINT 信号的处理程序设置为 handle_sigint 函数
    signal(SIGINT, handle_sigint);

    while (!stop) { // 检查是否应退出
        printf("Running...\n");
        sleep(1);
    }

    printf("Exiting...\n");

    return 0;
}
```


以上代码中，当程序运行时，如果用户按下 **Ctrl+C**，会捕捉到 SIGINT 信号并调用 handle_sigint 函数，打印出信号编号。


编译执行以上代码，输出结果如下：


```
Running...
Running...
Running...
^CCaught signal 2
Exiting...
```


代码解析：


- `volatile sig_atomic_t stop = 0;`：定义一个全局变量 `stop`，用于指示程序是否应退出。使用 `volatile` 关键字确保编译器不会优化掉对该变量的访问，因为它可能在信号处理程序中被修改。`sig_atomic_t` 类型保证了对该变量的访问是原子的。
- 在 `handle_sigint` 信号处理函数中，将 `stop` 设置为 1，指示程序应退出。
- 在主循环中，检查 `stop` 变量的值，如果它被设置为 1，则跳出循环，结束程序。


## 库变量


下面是头文件 signal.h 中定义的变量类型：


| 序号 | 变量 & 描述 |
| --- | --- |
| 1 | sig_atomic_t 这是 int 类型，在信号处理程序中作为变量使用。它是一个对象的整数类型，该对象可以作为一个原子实体访问，即使存在异步信号时，该对象可以作为一个原子实体访问。 |
| 2 | sigset_t 一种数据类型，用于表示信号集。 |


## 库宏









	  AI 思考中...





			** [C 标准库 – ](https://www.runoob.com/c-standard-library-math-h.html)
			[C 标准库 – ](https://www.runoob.com/c-standard-library-stdarg-h.html) **













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