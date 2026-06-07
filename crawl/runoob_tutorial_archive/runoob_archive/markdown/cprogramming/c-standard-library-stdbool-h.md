# C 标准库

- Source: https://www.runoob.com/cprogramming/c-standard-library-stdbool-h.html

在 C99 标准之前，C 语言中通常使用整数类型（如 `int`）来表示布尔值。例如，`0` 表示假，非零值（通常是 `1`）表示真。这种方式虽然可行，但缺乏直观性和类型安全性。为了解决这个问题，C99 标准引入了 `stdbool.h` 头文件，定义了布尔类型和相关宏。


`` 是 C 语言中的一个标准头文件，定义了布尔类型及其相关的常量。它使得 C 语言的布尔类型（`bool`）变得更加明确和可用，避免了使用整数（如 0 或 1）来表示布尔值的传统做法。


`stdbool.h` 头文件定义了以下内容：


- `bool`：布尔类型，用于声明布尔变量。
- `true`：表示真值的宏，通常定义为 `1`。
- `false`：表示假值的宏，通常定义为 `0`。
- `__bool_true_false_are_defined`：一个宏，用于指示 `true` 和 `false` 是否已定义。

这些宏的定义如下：


```
#define bool _Bool
#define true 1
#define false 0
#define __bool_true_false_are_defined 1
```


bool 是 _Bool 类型的别名。

_Bool 是 C99 标准中引入的原生类型，表示一个布尔值。_Bool 类型只能保存 0 或 1，因此适合用来存储逻辑值。


```
#include <stdbool.h>

_Bool is_valid = 1;  // 也可以直接使用 _Bool 类型
```


要在 C 程序中使用布尔类型和相关宏，首先需要引入 `` 头文件：


```
#include <stdbool.h>

bool is_raining = true;
bool is_sunny = false;
```


### 实例

以下是一个使用 `` 的简单示例：


## 实例


```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    // 声明布尔变量
    bool isReady = true;
    bool isFinished = false;

    // 使用布尔变量
    if (isReady) {
        printf("The system is ready.\n");
    } else {
        printf("The system is not ready.\n");
    }

    if (!isFinished) {
        printf("The task is not finished.\n");
    }

    // 布尔变量的值
    printf("isReady: %d\n", isReady);       // 输出 1 (true)
    printf("isFinished: %d\n", isFinished); // 输出 0 (false)

    return 0;
}
```


输出结果：


```
The system is ready.
The task is not finished.
isReady: 1
isFinished: 0
```


### bool 类型


使用 bool 类型定义布尔变量：


## 实例


```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    bool flag = true;  // 使用 bool 类型

    if (flag) {
        printf("Flag is true.\n");
    } else {
        printf("Flag is false.\n");
    }

    return 0;
}
```


以上实例中，flag 是一个布尔类型的变量，初始值为 true。判断 flag 是否为 true，然后打印相应的消息。


### true 和 false 宏

true 和 false 是预定义的宏，分别对应布尔值 1 和 0，可以直接在条件判断中使用：


## 实例


```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    bool is_logged_in = false;

    // 改变布尔值
    if (!is_logged_in) {
        is_logged_in = true;
        printf("User logged in: %s\n", is_logged_in ? "true" : "false");
    }

    return 0;
}
```


在此代码中，is_logged_in 的初始值是 false，然后在逻辑中将其改变为 true。


### 与 if 和 while 等语句配合使用

布尔类型在 if、while、for 等控制结构中很有用：


## 实例


```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    bool condition = false;

    while (!condition) {
        printf("The condition is false.\n");
        condition = true;  // 改变条件为真
    }

    return 0;
}
```


这里，while 循环会继续执行，直到 condition 变为 true。


### 布尔类型与整数的兼容性

尽管 bool 类型本身是一个专门的类型，但在底层实现上，它通常依赖于整数类型（通常为 int）。因此，true 可以被认为是 1，而 false 则是 0。


但是，在编程时应该避免将布尔值与普通整数混用，尽量保持类型的清晰性和可读性。


## 实例


```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    bool is_active = true;

    // 错误的做法：将布尔值与整数混合使用
    int status = is_active;  // 这行可以正常编译，但最好避免

    if (status) {
        printf("Status is true.\n");
    } else {
        printf("Status is false.\n");
    }

    return 0;
}
```


虽然上述代码会正确执行，但不推荐使用，因为它混合了布尔值和整数类型，容易让代码变得难以理解。

### 布尔类型的优势


- **可读性**：使用 `bool` 类型使得程序的意图更加明确，比起使用 `int` 类型代表真或假，`bool` 类型能够清晰地表明该变量只用来表示布尔值。
- **标准化**：`` 提供了一个标准的方式来处理布尔值，避免了使用宏或整数类型来表示布尔值的复杂性。
- **类型安全**：与 `int` 类型不同，`bool` 类型专门用于逻辑判断，减少了类型不匹配的问题。








	  AI 思考中...





			** [C 安全函数](https://www.runoob.com/c-safe-func.html)
			[C 标准库 ](https://www.runoob.com/c-standard-library-stdint-h.html) **













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