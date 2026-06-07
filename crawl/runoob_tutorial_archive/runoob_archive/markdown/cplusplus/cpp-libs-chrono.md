# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-chrono.html

C++11 引入了 `` 库，这是一个用于处理时间和日期的库。它提供了一套丰富的工具来测量时间间隔、执行时间点的计算以及处理日期和时间。`` 库是 C++ 标准库中处理时间相关操作的核心部分。


## 基本概念


### 时间点（Time Points）


时间点表示一个特定的时间点，通常与某个特定的时钟相关联。


### 持续时间（Durations）


持续时间表示两个时间点之间的时间间隔。


### 时钟（Clocks）


时钟是时间点和持续时间的来源。C++ 提供了几种不同的时钟，例如系统时钟、高分辨率时钟等。


## 基本语法


### 包含头文件


在使用 `` 库之前，需要包含相应的头文件：


```
#include <chrono>
```


### 使用时间点


```
auto now = std::chrono::system_clock::now();
```


### 使用持续时间


```
auto duration = std::chrono::seconds(5);
```


### 计算时间点


```
auto future_time = now + duration;
```


## 实例


### 测量函数执行时间


下面是一个使用 `` 库测量函数执行时间的简单示例：


## 实例


```cpp
#include <iostream>
#include <chrono>

void someFunction() {
    // 模拟一些操作
    std::this_thread::sleep_for(std::chrono::seconds(1));
}

int main() {
    auto start = std::chrono::high_resolution_clock::now();

    someFunction();

    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cout << "Function took " << duration.count() << " milliseconds to execute." << std::endl;

    return 0;
}
```


输出结果：


```
Function took 1000 milliseconds to execute.
```


### 处理日期和时间


`` 库也可以用来处理日期和时间。下面是一个使用 `std::chrono::system_clock` 和 `std::chrono::time_point` 来获取当前日期和时间的示例：


## 实例


```cpp
#include <iostream>
#include <chrono>
#include <ctime>

int main() {
    auto now = std::chrono::system_clock::now();
    std::time_t now_c = std::chrono::system_clock::to_time_t(now);

    std::cout << "Current date and time: " << std::ctime(&now_c);

    return 0;
}
```


输出结果：


```
Current date and time: Fri Mar 11 12:34:56 2022
```


## 高级用法


### 使用不同的时钟


C++ 提供了多种时钟，例如：


- `std::chrono::system_clock`：系统时钟，通常与系统时间同步。
- `std::chrono::steady_clock`：单调时钟，不会受到系统时间变化的影响。
- `std::chrono::high_resolution_clock`：提供最高分辨率的时钟。


### 格式化日期和时间


可以使用 `` 和 `` 来格式化日期和时间：


## 实例


```cpp
#include <iostream>
#include <iomanip>
#include <chrono>
#include <ctime>

int main() {
    auto now = std::chrono::system_clock::now();
    std::time_t now_c = std::chrono::system_clock::to_time_t(now);

    std::cout << std::put_time(std::localtime(&now_c), "%Y-%m-%d %H:%M:%S");

    return 0;
}
```


输出结果：


```
2022-03-11 12:34:56
```










	  AI 思考中...





			** [C++ 多线程库 ](https://www.runoob.com/cpp-libs-thread.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-ctime.html) **













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