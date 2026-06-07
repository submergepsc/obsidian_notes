# C++ 文件输入输出库 -

- Source: https://www.runoob.com/cplusplus/cpp-libs-fstream.html

在 C++ 中，` ` 是标准库中用于文件输入输出操作的类。它提供了一种方便的方式来读写文件。

`fstream`是`iostream`库的一部分，支持文本和二进制文件的读写。


`fstream`类是`iostream`库中的一个类，它继承自`istream`和`ostream`类，这意味着它既可以用于输入也可以用于输出。


### 语法


`fstream` 的基本语法如下：


```cpp
#include <fstream>

int main() {
    std::fstream file; // 创建fstream对象
    file.open("filename", mode); // 打开文件
    // 进行文件操作
    file.close(); // 关闭文件
    return 0;
}
```


其中`filename` 是文件的名称，`mode` 是打开文件的模式，常见的模式有：


- `std::ios::in`：以输入模式打开文件。
- `std::ios::out`：以输出模式打开文件。
- `std::ios::app`：以追加模式打开文件。
- `std::ios::ate`：打开文件并定位到文件末尾。
- `std::ios::trunc`：打开文件并截断文件，即清空文件内容。


### 实例


写入文本文件:


## 实例


```cpp
#include <fstream>
#include <iostream>

int main() {
    std::fstream file;
    file.open("example.txt", std::ios::out); // 以输出模式打开文件

    if (!file) {
        std::cerr << "Unable to open file!" << std::endl;
        return 1; // 文件打开失败
    }

    file << "Hello, World!" << std::endl; // 写入文本
    file.close(); // 关闭文件

    return 0;
}
```


在当前目录下创建一个名为`example.txt`的文件，文件内容为：


```
Hello, World!
```


读取文本文件


## 实例


```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    std::fstream file;
    file.open("example.txt", std::ios::in); // 以输入模式打开文件

    if (!file) {
        std::cerr << "Unable to open file!" << std::endl;
        return 1; // 文件打开失败
    }

    std::string line;
    while (getline(file, line)) { // 逐行读取
        std::cout << line << std::endl;
    }

    file.close(); // 关闭文件

    return 0;
}
```


如果 `example.txt` 文件包含以下内容：


```
Hello, World!
This is a test file.
```


则程序将输出：


```
Hello, World!
This is a test file.
```


追加到文件:


## 实例


```cpp
#include <fstream>
#include <iostream>

int main() {
    std::fstream file;
    file.open("example.txt", std::ios::app); // 以追加模式打开文件

    if (!file) {
        std::cerr << "Unable to open file!" << std::endl;
        return 1; // 文件打开失败
    }

    file << "Appending this line to the file." << std::endl; // 追加文本
    file.close(); // 关闭文件

    return 0;
}
```


`example.txt` 文件原本包含以下内容：


```
Hello, World!
This is a test file.
```


执行上述程序后，文件内容将变为：


```
Hello, World!
This is a test file.
Appending this line to the file.
```










	  AI 思考中...





			** [C++ 标准输入输出 — *](https://www.runoob.com/cpp-libs-iostream.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-sstream.html) *













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