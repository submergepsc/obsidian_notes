# C 输入 & 输出

- Source: https://www.runoob.com/cprogramming/c-input-output.html

当我们提到**输入**时，这意味着要向程序填充一些数据。输入可以是以文件的形式或从命令行中进行。C 语言提供了一系列内置的函数来读取给定的输入，并根据需要填充到程序中。


当我们提到**输出**时，这意味着要在屏幕上、打印机上或任意文件中显示一些数据。C 语言提供了一系列内置的函数来输出数据到计算机屏幕上和保存数据到文本文件或二进制文件中。


## 标准文件


C 语言把所有的设备都当作文件。所以设备（比如显示器）被处理的方式与文件相同。以下三个文件会在程序执行时自动打开，以便访问键盘和屏幕。


| 标准文件 | 文件指针 | 设备 |
| --- | --- | --- |
| 标准输入 | stdin | 键盘 |
| 标准输出 | stdout | 屏幕 |
| 标准错误 | stderr | 您的屏幕 |


文件指针是访问文件的方式，本节将讲解如何从键盘上读取值以及如何把结果输出到屏幕上。


C 语言中的 I/O (输入/输出) 通常使用 **printf()** 和 **scanf()** 两个函数。


scanf() 函数用于从标准输入（键盘）读取并格式化， printf() 函数发送格式化输出到标准输出（屏幕）。


### printf() 函数

printf() 函数用于将格式化的数据输出到标准输出设备（通常是屏幕）。


语法：


```
int printf(const char *format, ...);
```


参数：


- `format`：格式化字符串，指定输出的格式。
- `...`：可变参数列表，根据格式化字符串中的格式说明符，提供要输出的数据。


## 实例


```c
#include <stdio.h>      // 执行 printf() 函数需要该库
int main()
{
    printf("菜鸟教程");  //显示引号中的内容
    return 0;
}
```


编译以上程序，输出结果为：


```
菜鸟教程
```


**实例解析：**


- 所有的 C 语言程序都需要包含 **main()** 函数。 代码从 **main()** 函数开始执行。
- **printf()** 用于格式化输出到屏幕。**printf()** 函数在 **"stdio.h"** 头文件中声明。
- **stdio.h** 是一个头文件 (标准输入输出头文件) and **#include** 是一个预处理命令，用来引入头文件。 当编译器遇到 **printf()** 函数时，如果没有找到 **stdio.h** 头文件，会发生编译错误。
- **return 0;** 语句用于表示退出程序。


## %d 格式化输出整数


```c
#include <stdio.h>
int main()
{
    int testInteger = 5;
    printf("Number = %d", testInteger);
    return 0;
}
```


编译以上程序，输出结果为：


```
Number = 5
```


在 printf() 函数的引号中使用 "%d" (整型) 来匹配整型变量 testInteger 并输出到屏幕。


## %f 格式化输出浮点型数据


```c
#include <stdio.h>
int main()
{
    float f;
    printf("Enter a number: ");
    // %f 匹配浮点型数据
    scanf("%f",&f);
    printf("Value = %f", f);
    return 0;
}
```


### scanf() 函数

scanf() 函数用于从标准输入设备（通常是键盘）读取格式化的输入。


语法：


```
int scanf(const char *format, ...);
```


参数：

- `format`：格式化字符串，指定输入的格式。
- `...`：可变参数列表，根据格式化字符串中的格式说明符，提供存储输入数据的变量地址。


## 实例


```c
#include <stdio.h>

int main() {
    int a;
    float b;
    printf("Enter an integer and a float: ");
    scanf("%d %f", &a, &b);
    printf("You entered: %d and %.2f\n", a, b);
    return 0;
}
```


执行以上代码，然后输入：


```
10 3.14
```


输出：


```
You entered: 10 and 3.14
```


---


## 字符输入输出


### getchar() & putchar() 函数


**int getchar(void)** 函数从屏幕读取下一个可用的字符，并把它返回为一个整数。这个函数在同一个时间内只会读取一个单一的字符。您可以在循环内使用这个方法，以便从屏幕上读取多个字符。


**int putchar(int c)** 函数把字符输出到屏幕上，并返回相同的字符。这个函数在同一个时间内只会输出一个单一的字符。您可以在循环内使用这个方法，以便在屏幕上输出多个字符。


请看下面的实例：


## 实例


```c
#include <stdio.h>

int main( )
{
   int c;

   printf( "Enter a value :");
   c = getchar( );

   printf( "\nYou entered: ");
   putchar( c );
   printf( "\n");
   return 0;
}
```


当上面的代码被编译和执行时，它会等待您输入一些文本，当您输入一个文本并按下回车键时，程序会继续并只会读取一个单一的字符，显示如下：


```
$./a.out
Enter a value :runoob

You entered: r
```


## 字符串输入输出


### gets() 和 fgets() 函数


gets() 函数用于从标准输入设备读取一行字符串，但不推荐使用，因为它容易导致缓冲区溢出，推荐使用 **fgets()** 函数。


语法：


```
char *fgets(char *str, int n, FILE *stream);
```


参数：


- `str`：指向字符数组的指针，用于存储读取的字符串。
- `n`：要读取的最大字符数（包括空字符`\0`）。
- `stream`：文件流，通常使用`stdin`表示标准输入。


## 实例


```c
#include <stdio.h>

int main() {
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    printf("You entered: %s", str);
    return 0;
}
```


### puts() 函数


puts() 函数用于将一个字符串输出到标准输出设备，并自动在末尾添加换行符。


语法：


```
int puts(const char *str);
```


参数：


- `str`：要输出的字符串。


返回值：


- 成功时返回非负值，失败时返回`EOF`。


## 实例


```c
#include <stdio.h>

int main() {
    char str[] = "Hello, World!";
    puts(str);
    return 0;
}
```


输出：


```
Hello, World!
```


### fputs() 函数

fputs() 函数用于将字符串输出到指定的流（如标准输出、文件等），但不会自动在字符串末尾添加换行符。


语法：


```
int fputs(const char *str, FILE *stream);
```


参数：


- `str`：要输出的字符串（以空字符 `\0` 结尾的字符数组）。
- `stream`：指定输出的流，可以是标准输出（`stdout`）、文件流等。


返回值：

- 成功时返回一个非负值（通常是输出的字符数）。
- 失败时返回 `EOF`。

特点：


- **不添加换行符**：`fputs()` 不会在输出字符串后自动添加换行符。
- **灵活的输出流**：`fputs()` 可以输出到任意流，如标准输出、文件等。


## 实例


```c
#include <stdio.h>

int main() {
    char str[] = "Hello, World!";
    fputs(str, stdout);  // 输出 "Hello, World!"，不换行
    return 0;
}
```


### puts() 和 fputs() 的区别


| 特性 | puts() | fputs() |
| --- | --- | --- |
| 换行符 | 自动在字符串末尾添加换行符 | 不添加换行符 |
| 输出流 | 只能输出到标准输出（屏幕） | 可以输出到任意流（如文件、屏幕） |
| 参数 | 只需要一个字符串参数 | 需要字符串参数和流参数 |
| 返回值 | 成功时返回非负值，失败时返回 EOF | 成功时返回非负值，失败时返回 EOF |


## scanf() 和 printf() 函数


**int scanf(const char *format, ...)** 函数从标准输入流 **stdin** 读取输入，并根据提供的 **format** 来浏览输入。


**int printf(const char *format, ...)** 函数把输出写入到标准输出流 **stdout **，并根据提供的格式产生输出。


**format** 可以是一个简单的常量字符串，但是您可以分别指定 %s、%d、%c、%f 等来输出或读取字符串、整数、字符或浮点数。还有许多其他可用的格式选项，可以根据需要使用。如需了解完整的细节，可以查看这些函数的参考手册。现在让我们通过下面这个简单的实例来加深理解：


## 实例


```c
#include <stdio.h>
int main( ) {

   char str[100];
   int i;

   printf( "Enter a value :");
   scanf("%s %d", str, &i);

   printf( "\nYou entered: %s %d ", str, i);
   printf("\n");
   return 0;
}
```


当上面的代码被编译和执行时，它会等待您输入一些文本，当您输入一个文本并按下回车键时，程序会继续并读取输入，显示如下：


```
$./a.out
Enter a value :runoob 123

You entered: runoob 123
```


在这里，应当指出的是，scanf() 期待输入的格式与您给出的 %s 和 %d 相同，这意味着您必须提供有效的输入，比如 "string integer"，如果您提供的是 "string string" 或 "integer integer"，它会被认为是错误的输入。另外，在读取字符串时，只要遇到一个空格，scanf() 就会停止读取，所以 "this is test" 对 scanf() 来说是三个字符串。


---


## 文件输入与输出

C 语言还提供了文件输入输出的功能，允许从文件中读取数据或向文件中写入数据。


### fopen() 函数

fopen() 函数用于打开一个文件。


语法：


```
FILE *fopen(const char *filename, const char *mode);
```


参数：

- `filename`：要打开的文件名。
- `mode`：打开文件的模式，如`"r"`（只读）、`"w"`（只写）、`"a"`（追加）等。


返回值：

- 成功时返回指向`FILE`对象的指针，失败时返回`NULL`。


### fclose() 函数

fclose() 函数用于关闭一个已打开的文件。


语法：


```
int fclose(FILE *stream);
```


参数：

- `stream`：指向`FILE`对象的指针。

返回值：

- 成功时返回`0`，失败时返回`EOF`。


## 实例


```c
#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("example.txt", "w");
    if (file != NULL) {
        fprintf(file, "Hello, world!\n");
        fclose(file);
    }

    char buffer[100];
    file = fopen("example.txt", "r");
    if (file != NULL) {
        fgets(buffer, sizeof(buffer), file);  // 读取整行
        printf("Read from file: %s", buffer);  // fgets 会保留换行符
        fclose(file);
    }
    return 0;
}
```


输出内容：


```
Read from file: Hello, world!
```









	  AI 思考中...





			** [C typedef](https://www.runoob.com/c-typedef.html)
			[C 文件读写](https://www.runoob.com/c-file-io.html) **