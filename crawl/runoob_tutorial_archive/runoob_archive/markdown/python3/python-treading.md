# Python threading 模块

- Source: https://www.runoob.com/python3/python-treading.html

Python 的 `threading` 模块是用于实现多线程编程的标准库之一。多线程允许程序在同一时间内执行多个任务，从而提高程序的效率和响应速度。

`threading` 模块提供了创建和管理线程的工具，使得开发者可以轻松地编写并发程序。


### 什么是线程？


你可以把线程想象成办公室里的员工：

- 一个单线程程序就像只有一个员工，他必须顺序完成打印文档、回复邮件、泡咖啡等所有工作。
- 多线程程序则像拥有多个员工，他们可以**同时**进行不同的任务，大大提高了工作效率。


在计算机科学中：


- **进程**：一个运行中的程序，拥有独立的内存空间（例如，你同时打开的浏览器和音乐播放器就是两个进程）。
- **线程**：进程内的一个独立执行流，是 CPU 调度的基本单位。同一个进程内的所有线程**共享该进程的内存空间**（如全局变量）。


### 为什么使用多线程？


在单线程程序中，任务是一个接一个地顺序执行的。如果某个任务需要等待（例如等待网络响应或文件读取），整个程序会被阻塞，直到该任务完成。而多线程可以让程序在等待某个任务的同时，继续执行其他任务，从而提高程序的整体性能。


### Python 的线程与全局解释器锁 (GIL)


Python 有一个叫做 全局解释器锁 (Global Interpreter Lock， GIL) 的机制，GIL 确保了在任意时刻，只有一个线程可以执行 Python 字节码。


**这意味着什么？** 对于 CPU 密集型任务（如科学计算、图像处理），由于 GIL 的存在，多线程通常无法利用多核优势来提升计算速度，甚至可能因为线程切换的开销而变慢。


**那么，Python 多线程的用武之地在哪里？** 对于 I/O 密集型任务（如网络请求、读写文件、等待用户输入），线程在等待 I/O 操作完成时会释放 GIL，从而让其他线程运行。这可以显著提升程序的整体响应速度和效率，因为你在等待一个网页响应时，程序可以去处理另一个任务。


---


## 如何使用 threading 模块？


使用 `threading` 模块的第一步就是导入它：


```
import threading
import time  # 用于模拟耗时操作
```


创建线程最基本的方式是使用 `threading.Thread` 类。


**语法说明：**


```
thread_obj = threading.Thread(target=函数名, args=(参数元组,))
```


- **target**: 指定线程启动后要执行的函数。
- **args**: 传递给 target 函数的参数，必须是元组类型。如果只有一个参数，需要写成 `(参数,)` 的形式。


### 1. 创建线程


在 Python 中，可以通过继承 `threading.Thread` 类或直接使用 `threading.Thread` 构造函数来创建线程。


#### 方法 1：继承 threading.Thread 类


## 实例


```python
import threading

class MyThread(threading.Thread):
    def run(self):
        print("线程开始执行")
        # 在这里编写线程要执行的代码
        print("线程执行结束")

# 创建线程实例
thread = MyThread()
# 启动线程
thread.start()
# 等待线程执行完毕
thread.join()
print("主线程结束")
```


#### 方法 2：使用 threading.Thread 构造函数


## 实例


```python
import threading

def my_function():
    print("线程开始执行")
    # 在这里编写线程要执行的代码
    print("线程执行结束")

# 创建线程实例
thread = threading.Thread(target=my_function)
# 启动线程
thread.start()
# 等待线程执行完毕
thread.join()
print("主线程结束")
```


### 2. 线程同步


在多线程编程中，多个线程可能会同时访问共享资源，这可能导致数据不一致的问题。为了避免这种情况，可以使用线程同步机制，如锁（`Lock`）。


## 实例


```python
import threading

# 创建一个锁对象
lock = threading.Lock()

def my_function():
    with lock:
        print("线程开始执行")
        # 在这里编写线程要执行的代码
        print("线程执行结束")

# 创建线程实例
thread1 = threading.Thread(target=my_function)
thread2 = threading.Thread(target=my_function)
# 启动线程
thread1.start()
thread2.start()
# 等待线程执行完毕
thread1.join()
thread2.join()
print("主线程结束")
```


### 3. 线程间通信


线程间通信可以通过队列（`Queue`）来实现。`Queue` 是线程安全的，可以在多个线程之间安全地传递数据。


## 实例


```python
import threading
import queue

def worker(q):
    while not q.empty():
        item = q.get()
        print(f"处理项目: {item}")
        q.task_done()

# 创建一个队列并填充数据
q = queue.Queue()
for i in range(10):
    q.put(i)

# 创建线程实例
thread1 = threading.Thread(target=worker, args=(q,))
thread2 = threading.Thread(target=worker, args=(q,))
# 启动线程
thread1.start()
thread2.start()
# 等待队列中的所有项目被处理完毕
q.join()
print("所有项目处理完毕")
```


---


## 常用类、方法及属性


### 1. 核心类

| 类/方法/属性 | 说明 | 示例 |
| --- | --- | --- |
| threading.Thread | 线程类，用于创建和管理线程 | t = Thread(target=func, args=(1,)) |
| threading.Lock | 互斥锁（原始锁） | lock = Lock() |
| threading.RLock | 可重入锁（同一线程可多次获取） | rlock = RLock() |
| threading.Event | 事件对象，用于线程同步 | event = Event() |
| threading.Condition | 条件变量，用于复杂线程协调 | cond = Condition() |
| threading.Semaphore | 信号量，控制并发线程数 | sem = Semaphore(3) |
| threading.BoundedSemaphore | 有界信号量（防止计数超过初始值） | b_sem = BoundedSemaphore(2) |
| threading.Timer | 定时器线程，延迟执行 | timer = Timer(5.0, func) |
| threading.local | 线程局部数据（各线程独立存储） | local_data = threading.local() |


### 2. Thread 对象常用方法/属性

| 方法/属性 | 说明 | 示例 |
| --- | --- | --- |
| start() | 启动线程 | t.start() |
| run() | 线程执行的方法（可重写） | 自定义类时覆盖此方法 |
| join(timeout=None) | 阻塞当前线程，直到目标线程结束 | t.join() |
| is_alive() | 检查线程是否在运行 | if t.is_alive(): |
| name | 线程名称（可修改） | t.name = "Worker-1" |
| daemon | 守护线程标志（主线程退出时自动结束） | t.daemon = True |
| ident | 线程标识符（未启动时为 None） | print(t.ident) |


### 3. Lock/RLock 常用方法


| 方法 | 说明 | 示例 |
| --- | --- | --- |
| acquire(blocking=True, timeout=-1) | 获取锁（阻塞或非阻塞） | lock.acquire() |
| release() | 释放锁 | lock.release() |
| locked() | 检查锁是否被占用 | if not lock.locked(): |

### 4. Event 常用方法

| 方法 | 说明 | 示例 |
| --- | --- | --- |
| set() | 设置事件为真，唤醒所有等待线程 | event.set() |
| clear() | 重置事件为假 | event.clear() |
| wait(timeout=None) | 阻塞直到事件为真或超时 | event.wait(2.0) |
| is_set() | 检查事件状态 | if event.is_set(): |


### 5. Condition 常用方法

| 方法 | 说明 | 示例 |
| --- | --- | --- |
| wait(timeout=None) | 释放锁并阻塞，直到被通知或超时 | cond.wait() |
| notify(n=1) | 唤醒最多 n 个等待线程 | cond.notify(2) |
| notify_all() | 唤醒所有等待线程 | cond.notify_all() |

### 6. 模块级函数/属性

| 函数/属性 | 说明 | 示例 |
| --- | --- | --- |
| threading.active_count() | 返回当前活跃线程数 | print(threading.active_count()) |
| threading.current_thread() | 返回当前线程对象 | print(threading.current_thread().name) |
| threading.enumerate() | 返回所有活跃线程的列表 | for t in threading.enumerate(): |
| threading.main_thread() | 返回主线程对象 | if threading.current_thread() is threading.main_thread(): |
| threading.get_ident() | 返回当前线程的标识符（Python 3.3+） | print(threading.get_ident()) |


### 实例

1. 基础线程创建


## 实例


```python
import threading

def worker(num):
    print(f"Worker {num} started")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```


2. 使用锁保护共享资源


## 实例


```python
lock = threading.Lock()
count = 0

def increment():
    global count
    with lock:  # 自动获取和释放锁
        count += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(count)  # 输出: 10
```


3. 事件同步


## 实例


```python
event = threading.Event()

def waiter():
    print("Waiting for event...")
    event.wait()
    print("Event triggered!")

t = threading.Thread(target=waiter)
t.start()

# 主线程触发事件
threading.Event().wait(2.0)  # 模拟延迟
event.set()
t.join()
```


4. 生产者-消费者模型（Condition）


## 实例


```python
import random
from threading import Condition

queue = []
cond = Condition()
MAX_ITEMS = 5

def producer():
    for _ in range(10):
        with cond:
            while len(queue) >= MAX_ITEMS:
                cond.wait()
            item = random.randint(1, 100)
            queue.append(item)
            print(f"Produced {item}")
            cond.notify()

def consumer():
    for _ in range(10):
        with cond:
            while not queue:
                cond.wait()
            item = queue.pop(0)
            print(f"Consumed {item}")
            cond.notify()

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()
```


---


## 注意事项


- **全局解释器锁（GIL）**：Python 的 GIL 会限制同一时间只有一个线程执行 Python 字节码。因此，在 CPU 密集型任务中，多线程可能不会带来性能提升。对于 I/O 密集型任务，多线程仍然是有益的。
- **线程安全**：在多线程环境中，确保对共享资源的访问是线程安全的，避免数据竞争和死锁。
- **线程数量**：创建过多的线程可能会导致系统资源耗尽，影响程序性能。合理控制线程数量，或使用线程池（`ThreadPoolExecutor`）来管理线程。


---


## 小测验






### threading 模块知识小测验




      1. Python 的全局解释器锁 (GIL) 主要影响以下哪种类型的多线程任务性能？


          * A. I/O 密集型任务（如下载文件）


           B. CPU 密集型任务（如科学计算）


           C. 内存访问密集型任务





      2. 创建线程对象后，应该调用哪个方法来启动线程的执行？


           A. thread.run()


           B. thread.start()


           C. thread.execute()





      3. 当多个线程需要修改同一个全局变量时，为了避免数据错乱，最应该使用什么？


           A. 更快的 CPU


           B. 锁 (threading.Lock)


           C. 更多的内存





      4. 主线程使用 thread.join() 的目的是什么？


           A. 立即终止该线程


           B. 等待该线程执行完毕


           C. 暂停该线程的执行




      **
        * 提交答案


        ** 重置测验













	  AI 思考中...





			** [Python logging 模块](https://www.runoob.com/python-logging.html)
			[Python datetime 模块](https://www.runoob.com/python-datetime.html) **













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