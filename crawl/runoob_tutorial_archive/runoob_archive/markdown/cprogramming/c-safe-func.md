# C 安全函数

- Source: https://www.runoob.com/cprogramming/c-safe-func.html

在 C 语言中，为了提高代码的安全性，尤其是防止缓冲区溢出等常见的安全问题，C11 标准引入了一些**安全函数**，也称为 **Annex K** 标准库函数。这些安全函数主要是标准字符串和内存操作函数的增强版本，通过增加参数（如缓冲区大小）来提供更好的错误检测和处理。


**安全函数的特点：**


- **缓冲区大小检查**：所有的安全函数都要求传入目标缓冲区的大小参数，以防止缓冲区溢出。
- **返回值检查**：大多数函数返回 `errno_t` 类型的错误代码，可以检查函数是否成功执行。
- **更好的错误处理**：当缓冲区大小不够或出现其他问题时，这些函数会返回错误码，并尝试清空或初始化输出缓冲区。


安全函数在 Visual Studio 等编译器中得到较好的支持，但在一些较老版本的编译器中可能不可用，需要注意兼容性。

以下是 C 中常见的安全函数及其对应的传统函数对比：


### 1、字符串操作安全函数

**strcpy_s**：安全版本的 strcpy，复制字符串并检查目标缓冲区大小。


```
errno_t strcpy_s(char *dest, rsize_t destsz, const char *src);
```


**strcat_s**：安全版本的 strcat，将源字符串追加到目标字符串末尾，并检查缓冲区大小。


```
errno_t strcat_s(char *dest, rsize_t destsz, const char *src);
```


**strncpy_s**：安全版本的 strncpy，复制最多 n 个字符，并检查缓冲区大小。


```
errno_t strncpy_s(char *dest, rsize_t destsz, const char *src, rsize_t count);
```


**strncat_s**：安全版本的 strncat，追加最多 n 个字符到目标字符串末尾，并检查缓冲区大小。


```
errno_t strncat_s(char *dest, rsize_t destsz, const char *src, rsize_t count);
```


**strtok_s**：安全版本的 strtok，引入上下文参数，解决线程安全问题。


```
char *strtok_s(char *str, const char *delim, char **context);
```


### 2、格式化输出安全函数

**sprintf_s**：安全版本的 sprintf，格式化输出到字符串时检查缓冲区大小。


```
int sprintf_s(char *buffer, rsize_t buffer_size, const char *format, ...);
```


**snprintf_s**：安全版本的 snprintf，格式化输出时限制字符数并检查缓冲区大小。


```
int snprintf_s(char *buffer, rsize_t buffer_size, const char *format, ...);
```


**vsprintf_s**：安全版本的 vsprintf，接收 va_list 参数列表，并检查缓冲区大小。


```
int vsprintf_s(char *buffer, rsize_t buffer_size, const char *format, va_list argptr);
```


### 3、内存操作安全函数

**memcpy_s**：安全版本的 memcpy，复制内存区域时检查目标缓冲区大小。


```
errno_t memcpy_s(void *dest, rsize_t destsz, const void *src, rsize_t count);
```


**memmove_s**：安全版本的 memmove，复制内存区域，允许重叠，并检查目标缓冲区大小。


```
errno_t memmove_s(void *dest, rsize_t destsz, const void *src, rsize_t count);
```


**memset_s**：安全版本的 memset，将指定的字符填充到内存块中，并检查缓冲区大小。


```
errno_t memset_s(void *dest, rsize_t destsz, int ch, rsize_t count);
```


### 4、其他常用安全函数

**_itoa_s** 和 **_ultoa_s**：安全版本的整数转换函数，将整数转换为字符串时检查目标缓冲区大小。


```
errno_t _itoa_s(int value, char *buffer, size_t buffer_size, int radix);
errno_t _ultoa_s(unsigned long value, char *buffer, size_t buffer_size, int radix);
```


**_strlwr_s** 和 **_strupr_s**：将字符串转换为小写或大写的安全版本。


```
errno_t _strlwr_s(char *str, size_t numberOfElements);
errno_t _strupr_s(char *str, size_t numberOfElements);
```


---

## 实例


以下是使用 C 安全函数进行字符串操作和内存操作的示例，展示它们如何避免常见的缓冲区溢出问题并提供更安全的编程方式。


### 示例 1：strcpy_s 和 strcat_s


## 实例


```c
#include <stdio.h>
#include <string.h>

int main() {
    char dest[20]; // 目标缓冲区大小为 20
    const char *src = "Hello, World!";

    // 使用 strcpy_s 将 src 复制到 dest
    if (strcpy_s(dest, sizeof(dest), src) != 0) {
        printf("strcpy_s failed!\n");
        return 1; // 返回错误代码
    } else {
        printf("After strcpy_s: %s\n", dest);
    }

    // 使用 strcat_s 将 " C Language" 追加到 dest
    const char *appendStr = " C Language";
    if (strcat_s(dest, sizeof(dest), appendStr) != 0) {
        printf("strcat_s failed!\n");
        return 1; // 返回错误代码
    } else {
        printf("After strcat_s: %s\n", dest);
    }

    return 0;
}
```


输出:


```
After strcpy_s: Hello, World!
strcat_s failed!
```


在上述代码中，strcpy_s 成功复制了字符串 "Hello, World!" 到 dest，但由于 dest 的大小为 20，不足以容纳 "Hello, World! C Language"，所以 strcat_s 会检测到缓冲区不足，并返回错误代码。


### 示例 2：memcpy_s


## 实例


```c
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Sensitive Data";
    char dest[15]; // 目标缓冲区大小为 15

    // 使用 memcpy_s 将数据复制到 dest
    if (memcpy_s(dest, sizeof(dest), src, strlen(src) + 1) != 0) {
        printf("memcpy_s failed!\n");
        return 1; // 返回错误代码
    } else {
        printf("After memcpy_s: %s\n", dest);
    }

    return 0;
}
```


输出:


```
After memcpy_s: Sensitive Data
```


此示例中，memcpy_s 检查了目标缓冲区 dest 是否足够大来容纳 src 的数据，包括字符串末尾的空字符。如果 destsz 小于 strlen(src) + 1，则函数会返回错误并不会执行内存复制。


### 示例 3：strtok_s


## 实例


```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "apple,orange,banana";
    char *token;
    char *context = NULL;

    // 使用 strtok_s 分割字符串
    token = strtok_s(str, ",", &context);
    while (token != NULL) {
        printf("Token: %s\n", token);
        token = strtok_s(NULL, ",", &context);
    }

    return 0;
}
```


输出:


```
Token: apple
Token: orange
Token: banana
```


在这个示例中，strtok_s 分割字符串时使用 context 参数来保存上下文信息，从而避免了 strtok 线程不安全的问题。


### 示例 4：sprintf_s


## 实例


```c
#include <stdio.h>

int main() {
    char buffer[50];
    int num = 42;
    const char *str = "Hello";

    // 使用 sprintf_s 格式化字符串并检查缓冲区大小
    if (sprintf_s(buffer, sizeof(buffer), "Number: %d, String: %s", num, str) < 0) {
        printf("sprintf_s failed!\n");
        return 1; // 返回错误代码
    } else {
        printf("Formatted String: %s\n", buffer);
    }

    return 0;
}
```


输出:


```
Formatted String: Number: 42, String: Hello
```


在这里，sprintf_s 格式化字符串时，接受缓冲区大小作为参数。如果格式化后的字符串超过了 buffer 的大小，函数会返回错误，从而避免缓冲区溢出。

以上例子展示了使用 C 安全函数进行字符串复制、拼接、内存复制、字符串分割和格式化输出的方式。这些函数提供了对缓冲区大小的检查，显著提高了代码的安全性。


---


## 参考手册

安全函数主要是为了预防缓冲区溢出（Buffer Overflow）,这类漏洞通常源于函数不检查目标缓冲区的大小。


目前主流的安全函数标准主要来自 C11 标准的 Annex K (边界检查接口)，以及各操作系统（如 Windows 的 MSVC CRT）提供的增强版本。


下表展示了 C 安全函数的参考表格。


### 1、字符串处理


这是最容易发生溢出的重灾区，安全函数通常要求传入目标缓冲区的大小。


| 原始函数 (不安全) | 安全替代函数 | 主要改进点 |
| --- | --- | --- |
| strcpy | strcpy_s | 增加目标缓冲区大小参数；如果源字符串太长，会调用约束处理程序。 |
| strcat | strcat_s | 增加目标缓冲区剩余空间大小参数，防止拼接时越界。 |
| strncpy | strncpy_s | 确保目标字符串以 \0 结尾，且增加了运行时错误检查。 |
| strtok | strtok_s | 引入了上下文指针（Context），使其变为线程安全且更健壮。 |
| strlen | strnlen_s | 增加最大检查长度，防止在没有 \0 的坏数据中无限循环。 |


### 2、格式化输入/输出


不安全的格式化函数可能导致格式化字符串漏洞或缓冲区溢出。


| 原始函数 (不安全) | 安全替代函数 | 主要改进点 |
| --- | --- | --- |
| sprintf | snprintf / sprintf_s | snprintf 限制写入字符数；sprintf_s 检查格式化字符串的合法性。 |
| vsprintf | vsnprintf_s | 增加缓冲区大小限制，适用于可变参数列表。 |
| scanf | scanf_s | 对 %s 和 %c 等转换说明符，强制要求提供缓冲区大小。 |
| fscanf | fscanf_s | 读取文件输入时增加长度限制。 |
| sscanf | sscanf_s | 从字符串读取时增加长度限制。 |


3、标准输入/输出

| 原始函数 (不安全) | 安全替代函数 | 主要改进点 |
| --- | --- | --- |
| gets | gets_s / fgets | gets 在 C11 中已被废弃。gets_s 必须指定读取上限。 |
| tmpnam | tmpnam_s | 增加了对生成临时文件名缓冲区大小的检查。 |


### 4、内存操作


| 原始函数 (不安全) | 安全替代函数 | 主要改进点 |
| --- | --- | --- |
| memcpy | memcpy_s | 增加目标缓冲区大小检查。如果发生重叠或溢出，会返回错误。 |
| memmove | memmove_s | 处理重叠内存区域时增加大小限制检查。 |
| memset | memset_s | 保证编译器不会因为优化而跳过清除内存的操作（常用于清除密码等敏感数据）。 |








	  AI 思考中...





			** [C 库函数 – timespec_get](https://www.runoob.com/c-function-timespec_get.html)
			[C 标准库 ](https://www.runoob.com/c-standard-library-stdbool-h.html) **













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