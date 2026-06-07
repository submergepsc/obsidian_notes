# C 预处理器

- Source: https://www.runoob.com/cprogramming/c-preprocessors.html

**C 预处理器(CPP)**是编译过程中的独立阶段，在**实际编译前**对源代码进行文本处理。主要功能包括：


- 宏展开
- 文件包含
- 条件编译
- 特殊指令处理


**C 预处理器**不是编译器的组成部分，但是它是编译过程中一个单独的步骤。

简言之，C 预处理器只不过是一个文本替换工具而已，它们会指示编译器在实际编译之前完成所需的预处理。

我们将把 C 预处理器（C Preprocessor）简写为 CPP。


所有的预处理器命令都是以井号 **#** 开头。它必须是第一个非空字符，为了增强可读性，预处理器指令应从第一列开始。

下面列出了所有重要的预处理器指令：


| 指令 | 描述 | 使用示例 |
| --- | --- | --- |
| #define | 定义宏（符号常量或函数式宏） | #define PI 3.14159#define MAX(a,b) ((a) > (b) ? (a) : (b)) |
| #include | 包含头文件 | #include #include "myheader.h" |
| #undef | 取消已定义的宏 | #undef PI |
| #ifdef | 如果宏已定义则编译后续代码 | #ifdef DEBUGprintf("Debug info\n");#endif |
| #ifndef | 如果宏未定义则编译后续代码（常用于头文件保护） | #ifndef HEADER_H#define HEADER_H/* 内容 */#endif |
| #if | 条件编译（可配合defined操作符使用） | #if VERSION > 2/* 新版代码 */#endif |
| #else | #if/#ifdef/#ifndef的替代分支 | #ifdef WIN32/* Windows代码 */#else/* 其他系统 */#endif |
| #elif | 类似于else if | #if defined(UNIX)/* Unix代码 */#elif defined(WIN32)/* Windows代码 */#endif |
| #endif | 结束条件编译块 | 如上例所示 |
| #error | 产生编译错误并输出消息 | #if !defined(C99)#error "需要C99标准"#endif |
| #pragma | 编译器特定指令（非标准，各编译器不同） | #pragma once#pragma pack(1) |


## 预处理器实例


分析下面的实例来理解不同的指令。


```
#define MAX_ARRAY_LENGTH 20
```


这个指令告诉 CPP 把所有的 MAX_ARRAY_LENGTH 定义为 20。使用 *#define* 定义常量来增强可读性。


```
#include <stdio.h>
#include "myheader.h"
```


这些指令告诉 CPP 从**系统库**中获取 stdio.h，并添加文本到当前的源文件中。下一行告诉 CPP 从本地目录中获取 **myheader.h**，并添加内容到当前的源文件中。


```
#undef  FILE_SIZE
#define FILE_SIZE 42
```


这个指令告诉 CPP 取消已定义的 FILE_SIZE，并定义它为 42。


```
#ifndef MESSAGE
   #define MESSAGE "You wish!"
#endif
```


这个指令告诉 CPP 只有当 MESSAGE 未定义时，才定义 MESSAGE。


```
#ifdef DEBUG
   /* Your debugging statements here */
#endif
```


这个指令告诉 CPP 如果定义了 DEBUG，则执行处理语句。在编译时，如果您向 gcc 编译器传递了 *-DDEBUG* 开关量，这个指令就非常有用。它定义了 DEBUG，您可以在编译期间随时开启或关闭调试。


## 实例


```c
#include <stdio.h>

// 定义常量宏
#define PI 3.1415926
#define GREETING "Hello, World!"

// 定义函数式宏（注意括号的使用）
#define SQUARE(x) ((x) * (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

// 条件编译示例
#define DEBUG 1

int main() {
    // 使用常量宏
    printf("PI的值: %f\n", PI);
    printf("%s\n", GREETING);

    // 使用函数式宏
    int x = 5;
    printf("%d的平方是: %d\n", x, SQUARE(x));
    printf("3和5中较大的数是: %d\n", MAX(3, 5));

    // 条件编译示例
    #ifdef DEBUG
    printf("[调试信息] 程序运行到main函数\n");
    #endif

    // 编译器版本检查
    #if __STDC_VERSION__ >= 201112L
    printf("使用C11标准\n");
    #elif __STDC_VERSION__ >= 199901L
    printf("使用C99标准\n");
    #else
    printf("使用C89/C90标准\n");
    #endif

    // 错误指令示例（取消注释将导致编译错误）
    // #error "这是一个手动触发的错误"

    return 0;
}
```


### 最佳实践建议


- **宏命名**： - 使用全大写字母和下划线命名宏 - 示例：`#define MAX_SIZE 100`
- **函数式宏注意事项**： - 每个参数和整个表达式都要用括号括起来 - 避免使用有副作用的参数（如`SQUARE(x++)`）
- **头文件保护**：
```
#ifndef MY_HEADER_H
#define MY_HEADER_H
/* 头文件内容 */
#endif
```

- **条件编译调试**：
```
#ifdef DEBUG
#define DEBUG_PRINT(fmt, ...) printf(fmt, ##__VA_ARGS__)
#else
#define DEBUG_PRINT(fmt, ...)
#endif
```

- **跨平台开发**：
```
#if defined(_WIN32)
// Windows特定代码
#elif defined(__linux__)
// Linux特定代码
#elif defined(__APPLE__)
// macOS特定代码
#endif
```


## 预定义宏


ANSI C 定义了许多宏。在编程中您可以使用这些宏，但是不能直接修改这些预定义的宏。


| 宏 | 描述 |
| --- | --- |
| __DATE__ | 当前日期，一个以 "MMM DD YYYY" 格式表示的字符常量。 |
| __TIME__ | 当前时间，一个以 "HH:MM:SS" 格式表示的字符常量。 |
| __FILE__ | 这会包含当前文件名，一个字符串常量。 |
| __LINE__ | 这会包含当前行号，一个十进制常量。 |
| __STDC__ | 当编译器以 ANSI 标准编译时，则定义为 1。 |


让我们来尝试下面的实例：


## 实例


```c
#include <stdio.h>

/*
 * 预定义宏演示程序
 * 展示ANSI C标准中常用的预定义宏及其用途
 */
int main() {
    // 打印当前源文件名（字符串常量）
    printf("当前文件: %s\n", __FILE__);

    // 打印编译日期（"MMM DD YYYY"格式）
    printf("编译日期: %s\n", __DATE__);

    // 打印编译时间（"HH:MM:SS"格式）
    printf("编译时间: %s\n", __TIME__);

    // 打印当前行号（十进制整数）
    printf("当前行号: %d\n", __LINE__);

    // 检查是否符合ANSI/ISO标准（1表示符合）
    printf("ANSI标准: %d\n", __STDC__);

    // 实用示例：调试信息输出
    printf("\n[调试信息] %s (第%d行) 编译于 %s %s\n",
           __FILE__, __LINE__, __DATE__, __TIME__);

    return 0;
}
```


当上面的代码（在文件 **test.c** 中）被编译和执行时，它会产生下列结果：


```
当前文件: predef_macros.c
编译日期: Jul 5 2023
编译时间: 14:30:45
当前行号: 13
ANSI标准: 1

[调试信息] predef_macros.c (第16行) 编译于 Jul 5 2023 14:30:45
```


## 预处理器运算符


C 预处理器提供了下列的运算符来帮助您创建宏：


### 宏延续运算符（\）


一个宏通常写在一个单行上。但是如果宏太长，一个单行容纳不下，则使用宏延续运算符（\）。例如：


```
#define  message_for(a, b)  \
    printf(#a " and " #b ": We love you!\n")
```


##### 字符串常量化运算符（#）


在宏定义中，当需要把一个宏的参数转换为字符串常量时，则使用字符串常量化运算符（#）。在宏中使用的该运算符有一个特定的参数或参数列表。例如：


## 实例


```c
#include <stdio.h>

#define  message_for(a, b)  \
    printf(#a " and " #b ": We love you!\n")

int main(void)
{
   message_for(Carole, Debra);
   return 0;
}
```


当上面的代码被编译和执行时，它会产生下列结果：


```
Carole and Debra: We love you!
```


### 标记粘贴运算符（##）


宏定义内的标记粘贴运算符（##）会合并两个参数。它允许在宏定义中两个独立的标记被合并为一个标记。例如：


## 实例


```c
#include <stdio.h>

#define tokenpaster(n) printf ("token" #n " = %d", token##n)

int main(void)
{
   int token34 = 40;

   tokenpaster(34);
   return 0;
}
```


当上面的代码被编译和执行时，它会产生下列结果：


```
token34 = 40
```


这是怎么发生的，因为这个实例会从编译器产生下列的实际输出：


```
printf ("token34 = %d", token34);
```


这个实例演示了 token##n 会连接到 token34 中，在这里，我们使用了**字符串常量化运算符（#）**和**标记粘贴运算符（##）**。


### defined() 运算符


预处理器 **defined** 运算符是用在常量表达式中的，用来确定一个标识符是否已经使用 #define 定义过。如果指定的标识符已定义，则值为真（非零）。如果指定的标识符未定义，则值为假（零）。下面的实例演示了 defined() 运算符的用法：


## 实例


```c
#include <stdio.h>

#if !defined (MESSAGE)
   #define MESSAGE "You wish!"
#endif

int main(void)
{
   printf("Here is the message: %s\n", MESSAGE);
   return 0;
}
```


当上面的代码被编译和执行时，它会产生下列结果：


```
Here is the message: You wish!
```


## 参数化的宏


CPP 一个强大的功能是可以使用参数化的宏来模拟函数。例如，下面的代码是计算一个数的平方：


```
int square(int x) {
   return x * x;
}
```


我们可以使用宏重写上面的代码，如下：


```
#define square(x) ((x) * (x))
```


在使用带有参数的宏之前，必须使用 **#define** 指令定义。参数列表是括在圆括号内，且必须紧跟在宏名称的后边。宏名称和左圆括号之间不允许有空格。例如：


## 实例


```c
#include <stdio.h>

#define MAX(x,y) ((x) > (y) ? (x) : (y))

int main(void)
{
   printf("Max between 20 and 10 is %d\n", MAX(10, 20));
   return 0;
}
```


当上面的代码被编译和执行时，它会产生下列结果：


```
Max between 20 and 10 is 20
```









	  AI 思考中...





			** [C 文件读写](https://www.runoob.com/c-file-io.html)
			[C 头文件](https://www.runoob.com/c-header-files.html) **