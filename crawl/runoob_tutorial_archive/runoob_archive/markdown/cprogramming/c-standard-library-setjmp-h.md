# C 标准库 -

- Source: https://www.runoob.com/cprogramming/c-standard-library-setjmp-h.html

## 简介


**setjmp.h** 头文件定义了宏 **setjmp()**、函数 **longjmp()** 和变量类型 **jmp_buf**，该变量类型会绕过正常的函数调用和返回规则。


`` 是 C 标准库中的一个头文件，提供了一组函数和宏，用于非本地跳转（即从一个函数跳转到另一个之前调用过的函数，而不需要正常的函数返回机制）。这种机制通常用于错误处理、异常处理或者跳出深层嵌套的循环或递归。


## 库变量


下面列出了头文件 setjmp.h 中定义的变量：


| 序号 | 变量 & 描述 |
| --- | --- |
| 1 | jmp_buf jmp_buf 是一个数据类型，用于保存调用环境，包括栈指针、指令指针和寄存器等。在执行 setjmp() 时，这些环境信息会被保存到 jmp_buf 类型的变量中。 |


## 库宏


下面是这个库中定义的唯一的一个宏：


| 序号 | 宏 & 描述 |
| --- | --- |
| 1 | int setjmp(jmp_buf environment)这个宏把当前环境保存在变量 environment 中，以便函数 longjmp() 后续使用。如果这个宏直接从宏调用中返回，则它会返回零，但是如果它从 longjmp() 函数调用中返回，则它会返回一个非零值。 |


## 库函数


下面是头文件 setjmp.h 中定义的唯一的一个函数：


| 序号 | 函数 & 描述 |
| --- | --- |
| 1 | void longjmp(jmp_buf environment, int value)该函数恢复最近一次调用 setjmp() 宏时保存的环境，jmp_buf 参数的设置是由之前调用 setjmp() 生成的。 |


### 实例


以下示例展示了如何使用 setjmp() 和 longjmp() 实现非本地跳转：


## 实例


```c
#include <stdio.h>
#include <setjmp.h>

jmp_buf env;

void second() {
    printf("Entering second()\n");
    longjmp(env, 1);
    printf("This line will never be executed\n");
}

void first() {
    printf("Entering first()\n");
    if (setjmp(env) == 0) {
        printf("Calling second() from first()\n");
        second();
    } else {
        printf("Returned to first() from second() using longjmp\n");
    }
    printf("Exiting first()\n");
}

int main() {
    printf("Starting main()\n");
    first();
    printf("Exiting main()\n");
    return 0;
}
```


运行上述程序将输出类似以下内容：


```
Starting main()
Entering first()
Calling second() from first()
Entering second()
Returned to first() from second() using longjmp
Exiting first()
Exiting main()
```



### 代码解析


- `jmp_buf env`：定义一个用于保存环境信息的变量 `env`。
- `first()` 函数：调用 `setjmp(env)` 保存当前环境信息，并根据其返回值决定是否调用 `second()` 函数。
- `second()` 函数：调用 `longjmp(env, 1)`，跳转回 `setjmp(env)`，并使其返回 1。
- `main()` 函数：调用 `first()` 函数。

### 使用场景


- **错误处理**：在深层嵌套的函数调用中使用 `setjmp()` 和 `longjmp()` 实现错误处理机制。
- **异常处理**：用于实现简单的异常处理。
- **中断控制流**：在某些情况下，可以中断正常的控制流，跳出多层嵌套的循环或函数调用。


### 注意事项


- 使用 `setjmp()` 和 `longjmp()` 需要小心，因为它们会跳过正常的栈展开过程，可能导致资源泄漏（如未释放的内存、未关闭的文件等）。
- 避免在调用 `setjmp()` 和 `longjmp()` 之间修改局部变量，因为这可能导致未定义行为。
- 非本地跳转可能使代码难以阅读和调试，因此应谨慎使用。


### 总结


`` 提供了 `setjmp()` 和 `longjmp()` 函数，用于实现非本地跳转。这些函数在错误处理和异常处理中非常有用，但需要谨慎使用以避免潜在的问题。








	  AI 思考中...





			** [C 标准库 – ](https://www.runoob.com/c-standard-library-float-h.html)
			[C 标准库 – ](https://www.runoob.com/c-standard-library-limits-h.html) **













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