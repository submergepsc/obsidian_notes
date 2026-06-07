# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-future.html

C++11 引入了 `` 头文件，它提供了一种异步编程的机制，允许程序在等待某个操作完成时继续执行其他任务。`` 库是 C++ 标准库中并发编程的一部分，它允许程序员以一种更简洁和安全的方式处理异步操作。


`` 库中定义了几个关键的类型：


- `std::future`：表示异步操作的结果，可以查询操作的状态，获取结果或等待操作完成。
- `std::promise`：用于与 `std::future` 配对，用于设置异步操作的结果。
- `std::packaged_task`：封装一个函数或可调用对象，使其可以作为异步任务执行。


### std::promise


`std::promise` 用于设置异步操作的结果。它与 `std::future` 配对使用。


## 实例


```cpp
#include <iostream>
#include <future>

int main() {
    std::promise<int> prom;
    std::future<int> fut = prom.get_future();

    // 在另一个线程中设置结果
    std::thread t([prom]() {
        prom.set_value(10);
    });

    // 等待结果
    std::cout << "Future value: " << fut.get() << std::endl;

    t.join();
    return 0;
}
```


输出结果：


```
Future value: 10
```


### std::packaged_task


`std::packaged_task` 封装一个函数或可调用对象，使其可以作为异步任务执行。


## 实例


```cpp
#include <iostream>
#include <future>
#include <cmath>

int compute_square_root(double x) {
    return std::sqrt(x);
}

int main() {
    std::packaged_task<double(double)> task(compute_square_root);
    std::future<double> result = task.get_future();
    std::thread th(std::move(task), 9.0);

    std::cout << "Result: " << result.get() << std::endl;
    th.join();
    return 0;
}
```


输出结果：


```
Result: 3
```


### std::async


`std::async` 是一个方便的函数，用于启动异步任务。它可以立即返回一个 `std::future` 对象。


## 实例


```cpp
#include <iostream>
#include <future>

int main() {
    std::future<int> fut = std::async(std::launch::async, [](int x) {
        return x * x;
    }, 5);

    std::cout << "Result: " << fut.get() << std::endl;
    return 0;
}
```


输出结果：


```
Result: 25
```


## 异常处理


当异步操作抛出异常时，`std::future` 会捕获这个异常，并且可以通过调用 `.get()` 方法来重新抛出它。


## 实例


```cpp
#include <iostream>
#include <future>

void throw_exception() {
    throw std::runtime_error("Exception thrown");
}

int main() {
    std::future<void> fut = std::async(throw_exception);

    try {
        fut.get();
    } catch (const std::exception& e) {
        std::cout << "Caught exception: " << e.what() << std::endl;
    }
    return 0;
}
```


输出结果：


```
Caught exception: Exception thrown
```


`` 库为 C++ 程序员提供了一种简单而强大的异步编程方式。通过使用 `std::promise`、`std::packaged_task` 和 `std::async`，我们可以轻松地在 C++ 程序中实现并发和异步操作。同时，异常处理机制也确保了程序的健壮性。








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-atomic.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-condition_variable.html) **













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