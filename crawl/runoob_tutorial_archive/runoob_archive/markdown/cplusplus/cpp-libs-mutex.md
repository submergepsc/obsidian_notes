# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-mutex.html

在多线程编程中，确保数据的一致性和线程安全是至关重要的。


C++ 标准库提供了一套丰富的同步原语，用于控制对共享资源的访问。


C++ 标准库中的 `` 头文件提供了一组工具，用于在多线程程序中实现线程间的同步和互斥。


`` 头文件是 C++11 引入的，它包含了用于互斥锁（mutex）的类和函数。互斥锁是一种同步机制，用于防止多个线程同时访问共享资源。


互斥锁（Mutex）是一个用于控制对共享资源访问的同步原语。当一个线程需要访问共享资源时，它会尝试锁定互斥锁。如果互斥锁已经被其他线程锁定，请求线程将被阻塞，直到互斥锁被释放。


## 基本语法


在 C++ 中，`` 头文件提供了以下主要类：


- `std::mutex`：基本的互斥锁。
- `std::recursive_mutex`：递归互斥锁，允许同一个线程多次锁定。
- `std::timed_mutex`：具有超时功能的互斥锁。
- `std::recursive_timed_mutex`：具有超时功能的递归互斥锁。


## 实例


### 1. 使用 std::mutex


下面是一个简单的示例，展示了如何在 C++ 中使用 `std::mutex` 来同步对共享资源的访问。


## 实例


```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mtx; // 全局互斥锁
int shared_resource = 0;

void increment() {
    for (int i = 0; i < 10000; ++i) {
        mtx.lock(); // 锁定互斥锁
        ++shared_resource;
        mtx.unlock(); // 解锁互斥锁
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);

    t1.join();
    t2.join();

    std::cout << "Final value of shared_resource: " << shared_resource << std::endl;
    return 0;
}
```


输出结果：


```
Final value of shared_resource: 20000
```


### 2. 使用 std::recursive_mutex


递归互斥锁允许同一个线程多次锁定同一个互斥锁。下面是一个使用 `std::recursive_mutex` 的示例。


## 实例


```cpp
#include <iostream>
#include <thread>
#include <mutex>

std::recursive_mutex rmtx; // 创建一个递归 mutex 对象
int shared_resource = 0; // 共享资源

// 递归函数
void recursive_increment(int count) {
    if (count <= 0) return;

    std::lock_guard<std::recursive_mutex> lock(rmtx); // 上锁，确保线程安全
    ++shared_resource;
    std::cout << "Incremented shared_resource to " << shared_resource << " (count = " << count << ")" << std::endl;

    // 递归调用
    recursive_increment(count - 1);
}

int main() {
    std::thread t1(recursive_increment, 3); // 线程 t1 执行 recursive_increment(3)
    std::thread t2(recursive_increment, 3); // 线程 t2 执行 recursive_increment(3)

    t1.join(); // 等待线程 t1 完成
    t2.join(); // 等待线程 t2 完成

    std::cout << "Final value of shared_resource: " << shared_resource << std::endl;

    return 0;
}
```


输出结果：


```
Incremented shared_resource to 1 (count = 3)
Incremented shared_resource to 2 (count = 2)
Incremented shared_resource to 3 (count = 1)
Incremented shared_resource to 4 (count = 0)
Incremented shared_resource to 5 (count = 3)
Incremented shared_resource to 6 (count = 2)
Incremented shared_resource to 7 (count = 1)
Incremented shared_resource to 8 (count = 0)
Final value of shared_resource: 8
```


**代码解析：**


- **创建 `std::recursive_mutex` 对象**：`std::recursive_mutex rmtx;` 是一个递归互斥量，允许同一线程多次获得锁。
- **共享资源**：`int shared_resource = 0;` 是多个线程共同访问的资源。
- **递归函数 `recursive_increment`**： - 使用 `std::lock_guard` 对 `rmtx` 上锁。由于使用的是递归互斥量，同一个线程可以多次获得锁。 - 通过 `++shared_resource` 增加共享资源的值。 - 函数自身递归调用，演示了递归函数在多次锁定的情况下如何安全地工作。
- **创建和运行线程**： - `std::thread t1(recursive_increment, 3);` 和 `std::thread t2(recursive_increment, 3);` 分别创建两个线程，它们都会执行 `recursive_increment(3)`。 - `t1.join()` 和 `t2.join()` 等待两个线程执行完毕。


## 注意事项


- 确保在每次锁定互斥锁后，都进行解锁操作，以避免死锁。
- 使用 `std::lock_guard` 或 `std::unique_lock` 可以自动管理互斥锁的锁定和解锁，减少出错的可能性。
- 避免在持有互斥锁的情况下调用可能抛出异常的函数，因为这可能导致死锁。


`` 是 C++ 标准库中一个非常重要的头文件，它为多线程编程提供了基本的同步机制。通过使用互斥锁，我们可以确保对共享资源的访问是安全的，从而避免数据竞争和不一致的问题。


---


## 更多说明


### 1. std::mutex


提供基本的互斥量，确保在同一时刻只有一个线程可以访问共享资源。


## 实例


```cpp
#include <mutex>

std::mutex mtx;

void thread_function() {
    std::lock_guard<std::mutex> lock(mtx);
    // 访问共享资源
}
```


### 2. std::recursive_mutex

允许同一线程多次获得锁，而不会造成死锁，这对递归函数特别有用。


## 实例


```cpp
#include <mutex>

std::recursive_mutex rmtx;

void recursive_function(int count) {
    if (count <= 0) return;
    std::lock_guard<std::recursive_mutex> lock(rmtx);
    // 递归调用
    recursive_function(count - 1);
}
```


### 3. std::timed_mutex

提供定时的互斥量，可以在尝试获得锁时设置超时时间。


## 实例


```cpp
#include <mutex>
#include <chrono>

std::timed_mutex tm;

void try_lock_for_example() {
    if (tm.try_lock_for(std::chrono::seconds(1))) {
        // 成功获得锁
        tm.unlock();
    } else {
        // 锁获取失败
    }
}
```


### 4. std::recursive_timed_mutex

继承自 std::timed_mutex，允许同一线程多次获得锁，同时支持定时功能。


## 实例


```cpp
#include <mutex>
#include <chrono>

std::recursive_timed_mutex rtm;

void recursive_timed_function(int count) {
    if (count <= 0) return;
    if (rtm.try_lock_for(std::chrono::seconds(1))) {
        // 成功获得锁
        recursive_timed_function(count - 1);
        rtm.unlock();
    } else {
        // 锁获取失败
    }
}
```


### 5. std::lock_guard


一种自动管理 std::mutex 锁的封装器，使用 RAII 风格，确保在作用域结束时自动释放锁。


## 实例


```cpp
#include <mutex>

std::mutex mtx;

void function() {
    std::lock_guard<std::mutex> lock(mtx);
    // 访问共享资源
}
```


### 6. std::unique_lock


提供比 std::lock_guard 更灵活的锁管理，可以手动释放和重新获得锁，还支持定时锁定。


## 实例


```cpp
#include <mutex>
#include <chrono>

std::mutex mtx;

void function() {
    std::unique_lock<std::mutex> lock(mtx);
    // 访问共享资源

    // 可以手动释放锁
    lock.unlock();

    // 可以重新获得锁
    lock.lock();

    // 可以进行定时锁定
    if (lock.try_lock_for(std::chrono::seconds(1))) {
        // 成功获得锁
    }
}
```


### 7. std::adopt_lock_t


标志类型，用于指定 std::unique_lock 采用已有的锁。


## 实例


```cpp
std::mutex mtx;
std::unique_lock<std::mutex> lock(mtx, std::adopt_lock);
```


### 8. std::defer_lock_t

功能：标志类型，用于延迟锁定，初始化时不锁定。


## 实例


```cpp
std::mutex mtx;
std::unique_lock<std::mutex> lock(mtx, std::defer_lock);
// 可以在之后的某个时刻调用 lock.lock()
```


### 9. std::try_to_lock_t


标志类型，用于尝试锁定而不阻塞。


## 实例


```cpp
std::mutex mtx1, mtx2;
std::unique_lock<std::mutex> lock1(mtx1, std::try_to_lock);
std::unique_lock<std::mutex> lock2(mtx2, std::try_to_lock);

if (lock1 && lock2) {
    // 成功获得两个锁
}
```









	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-condition_variable.html)
			[C++ 多线程库 ](https://www.runoob.com/cpp-libs-thread.html) **













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