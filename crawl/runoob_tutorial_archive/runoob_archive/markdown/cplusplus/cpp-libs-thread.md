# C++ 多线程库

- Source: https://www.runoob.com/cplusplus/cpp-libs-thread.html

C++11 引入了多线程支持，通过 `` 库，开发者可以轻松地在程序中实现并行处理。

本文将将介绍 `` 库的基本概念、定义、语法以及如何使用它来创建和管理线程。


线程是程序执行的最小单元，是操作系统能够进行运算调度的最小单位。

在多线程程序中，多个线程可以并行执行，提高程序的执行效率。


### C++ 库概述


`` 库是 C++ 标准库的一部分，提供了创建和管理线程的基本功能，它包括以下几个关键组件：


- `std::thread`：表示一个线程，可以创建、启动、等待和销毁线程。
- `std::this_thread`：提供了一些静态成员函数，用于操作当前线程。
- `std::thread::id`：线程的唯一标识符。


### 创建线程


要创建一个线程，你需要实例化 `std::thread` 类，并传递一个可调用对象（函数、lambda 表达式或对象的成员函数）作为参数。


## 实例


```cpp
#include <iostream>
#include <thread>

void print_id(int id) {
    std::cout << "ID: " << id << ", Thread ID: " << std::this_thread::get_id() << std::endl;
}

int main() {
    std::thread t1(print_id, 1);
    std::thread t2(print_id, 2);
}
```


### 启动线程


创建 `std::thread` 对象后，线程会立即开始执行，你可以调用 `join()` 方法来等待线程完成。


```
t1.join();
t2.join();
```


### 等待线程完成


`join()` 方法会阻塞当前线程，直到被调用的线程完成执行。


### 销毁线程


当线程执行完毕后，你可以使用 `detach()` 方法来分离线程，或者让 `std::thread` 对象超出作用域自动销毁。


```
t1.detach(); // 线程将继续运行，但无法再被 join 或 detach
```


## 实例：使用 创建并行计算


下面是一个使用 `` 库实现的并行计算实例，计算两个数的和。


## 实例


```cpp
#include <iostream>
#include <thread>

int sum = 0;

void add(int a, int b) {
    sum += a + b;
}

int main() {
    int a = 5;
    int b = 10;

    std::thread t1(add, a, b);
    std::thread t2(add, a, b);

    t1.join();
    t2.join();

    std::cout << "Sum: " << sum << std::endl; // 输出结果：Sum: 30
}
```


输出结果为：


```
Sum: 30
```


以下实例我们将创建两个线程，每个线程都会执行一个简单的函数，该函数打印一个消息并休眠一段时间：


## 实例


```cpp
#include <iostream>
#include <thread>
#include <chrono>

// 简单的函数，在线程中执行
void print_message(const std::string& message, int delay) {
    std::this_thread::sleep_for(std::chrono::milliseconds(delay));
    std::cout << message << std::endl;
}

int main() {
    // 创建两个线程，执行 print_message 函数
    std::thread t1(print_message, "Hello from thread 1", 1000);
    std::thread t2(print_message, "Hello from thread 2", 500);

    // 等待线程 t1 完成
    if (t1.joinable()) {
        t1.join();
    }

    // 等待线程 t2 完成
    if (t2.joinable()) {
        t2.join();
    }

    std::cout << "Main thread finished." << std::endl;

    return 0;
}
```


输出结果为：


```
Hello from thread 2
Hello from thread 1
Main thread finished.
```


### 注意事项


- 线程安全：在多线程环境中，共享资源需要同步访问，以避免数据竞争。
- 线程生命周期：确保在线程执行完毕后正确地处理线程对象，避免资源泄露。


---

## 类和函数


`` 库包含了一系列的类和函数，用于创建、管理和同步线程。

以下是对 C++ `` 库的详细介绍:


### 主要组件


- **std::thread**
- **std::mutex**
- **std::lock_guard**
- **std::unique_lock**
- **std::condition_variable**
- **std::future 和 std::promise**
- **std::async**


### std::thread

std::thread 类用于创建和管理线程。


## 实例


```cpp
#include <iostream>
#include <thread>

void print_hello() {
    std::cout << "Hello from thread!" << std::endl;
}

int main() {
    std::thread t(print_hello);
    t.join(); // 等待线程 t 结束
    return 0;
}
```


**重要方法**


- **join()**: 等待线程结束。
- **detach()**: 将线程置于后台运行，不再等待线程结束。
- **joinable()**: 检查线程是否可被 join 或 detach。


### std::mutex

std::mutex 类用于同步对共享资源的访问。


## 实例


```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mtx; // 创建一个全局 mutex 对象
int shared_resource = 0; // 共享资源

// 线程函数
void increment() {
    std::lock_guard<std::mutex> lock(mtx); // 上锁，保证线程安全
    ++shared_resource;
    std::cout << "Incremented shared_resource to " << shared_resource << std::endl;
    // lock 在 lock_guard 离开作用域时自动释放
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);

    t1.join(); // 等待线程 t1 完成
    t2.join(); // 等待线程 t2 完成

    std::cout << "Final value of shared_resource: " << shared_resource << std::endl;

    return 0;
}
```


### std::lock_guard

std::lock_guard 是一个 RAII 风格的锁管理器，用于自动管理锁的生命周期。


## 实例


```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mtx;

void print_thread_id(int id) {
    std::lock_guard<std::mutex> lock(mtx);
    std::cout << "Thread ID: " << id << std::endl;
}

int main() {
    std::thread t1(print_thread_id, 1);
    std::thread t2(print_thread_id, 2);
    t1.join();
    t2.join();
    return 0;
}
```


### std::unique_lock

std::unique_lock 提供了比 std::lock_guard 更灵活的锁管理。


## 实例


```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mtx;

void print_thread_id(int id) {
    std::unique_lock<std::mutex> lock(mtx);
    std::cout << "Thread ID: " << id << std::endl;
    lock.unlock(); // 可以手动解锁
    // ... 其他操作
}

int main() {
    std::thread t1(print_thread_id, 1);
    std::thread t2(print_thread_id, 2);
    t1.join();
    t2.join();
    return 0;
}
```


### std::condition_variable

std::condition_variable 用于线程间的等待和通知。


## 实例


```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

std::mutex mtx;
std::condition_variable cv;
bool ready = false;

void print_id(int id) {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, []{ return ready; });
    std::cout << "Thread ID: " << id << std::endl;
}

void set_ready() {
    std::unique_lock<std::mutex> lock(mtx);
    ready = true;
    cv.notify_all();
}

int main() {
    std::thread t1(print_id, 1);
    std::thread t2(print_id, 2);

    std::this_thread::sleep_for(std::chrono::seconds(1));
    set_ready();

    t1.join();
    t2.join();
    return 0;
}
```


### std::future 和 std::promise

std::future 和 std::promise 用于线程间的结果传递。


## 实例


```cpp
#include <iostream>
#include <thread>
#include <future>

void calculate_square(std::promise<int> && p, int x) {
    p.set_value(x * x);
}

int main() {
    std::promise<int> p;
    std::future<int> f = p.get_future();

    std::thread t(calculate_square, std::move(p), 5);

    std::cout << "Square: " << f.get() << std::endl;

    t.join();
    return 0;
}
```


### std::async

std::async 用于启动异步任务，并返回一个 std::future。


## 实例


```cpp
#include <iostream>
#include <future>

int calculate_square(int x) {
    return x * x;
}

int main() {
    std::future<int> result = std::async(calculate_square, 5);

    std::cout << "Square: " << result.get() << std::endl;

    return 0;
}
```


C++ 的 `` 库为开发者提供了强大的多线程支持。通过本文的介绍，我们应该能够理解线程的基本概念，并学会如何使用 `` 库来创建和管理线程。在实际开发中，合理利用多线程可以显著提高程序的性能和响应速度。








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-mutex.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-chrono.html) **













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