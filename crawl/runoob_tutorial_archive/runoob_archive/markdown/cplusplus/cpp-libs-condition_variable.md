# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-condition_variable.html

在多线程编程中，线程间的同步是一个非常重要的问题。

C++11 标准引入了 `` 头文件，它提供了一种机制，允许线程在某些条件不满足时挂起，直到其他线程通知它们条件已经满足。

`condition_variable`是用于线程间同步的一种高级工具，它比使用低级同步原语（如互斥锁和条件变量）更加安全和方便。


`condition_variable`是一个类模板，用于在多线程环境中实现线程间的同步。它允许一个或多个线程等待某个条件变为真，而其他线程可以唤醒这些等待的线程。


## 语法


以下是`condition_variable`的基本语法：


```
#include <condition_variable>

void notify_one() {
    // 唤醒一个等待的线程
}

void notify_all() {
    // 唤醒所有等待的线程
}

template <class Mutex>
class condition_variable {
public:
    condition_variable();
    ~condition_variable();

    void wait(unique_lock<mutex>& lock);
    void wait_for(unique_lock<mutex>& lock, chrono::duration<Rep, Period> const& rel_time);
    void wait_until(unique_lock<mutex>& lock, chrono::time_point<Clock, Duration> const& abs_time);

    void notify_one() noexcept;
    void notify_all() noexcept;
};
```


## 实例


下面是一个使用`condition_variable`的简单示例，展示了生产者-消费者问题的基本实现。


## 实例


```cpp
#include <iostream>
#include <condition_variable>
#include <mutex>
#include <queue>
#include <thread>

std::mutex mtx;
std::condition_variable cv;
std::queue<int> product;

void producer(int id) {
    for (int i = 0; i < 5; ++i) {
        std::unique_lock<std::mutex> lck(mtx);
        product.push(id * 100 + i);
        std::cout << "Producer " << id << " produced " << product.back() << std::endl;
        cv.notify_one();
        lck.unlock();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
}

void consumer(int id) {
    while (true) {
        std::unique_lock<std::mutex> lck(mtx);
        cv.wait(lck, []{ return !product.empty(); });
        if (!product.empty()) {
            int prod = product.front();
            product.pop();
            std::cout << "Consumer " << id << " consumed " << prod << std::endl;
        }
        lck.unlock();
    }
}

int main() {
    std::thread producers[2];
    std::thread consumers[2];

    for (int i = 0; i < 2; ++i) {
        producers[i] = std::thread(producer, i + 1);
    }

    for (int i = 0; i < 2; ++i) {
        consumers[i] = std::thread(consumer, i + 1);
    }

    for (int i = 0; i < 2; ++i) {
        producers[i].join();
        consumers[i].join();
    }

    return 0;
}
```


这个程序的输出可能会有所不同，因为它依赖于线程调度。但是，你会看到生产者生产产品，然后消费者消费这些产品。输出将类似于：


```
Producer 1 produced 100
Producer 2 produced 200
Consumer 1 consumed 100
Producer 1 produced 101
Consumer 2 consumed 200
Producer 2 produced 201
Consumer 1 consumed 101
...
```


## 注意事项


- 使用`condition_variable`时，必须确保在等待之前获取互斥锁，并且在唤醒后释放互斥锁。
- `wait`、`wait_for`和`wait_until`函数都会释放互斥锁，然后在等待期间重新获取它。
- `notify_one`唤醒一个等待的线程，而`notify_all`唤醒所有等待的线程。








	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-future.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-mutex.html) **













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