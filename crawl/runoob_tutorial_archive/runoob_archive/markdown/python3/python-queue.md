# Python queue 模块

- Source: https://www.runoob.com/python3/python-queue.html

在 Python 中，`queue` 模块提供了一个线程安全的队列实现，用于在多线程编程中安全地传递数据。

队列是一种先进先出（FIFO）的数据结构，`queue` 模块提供了多种队列类型，包括 `Queue`、`LifoQueue` 和 `PriorityQueue`，以满足不同的需求。


---


## 队列类型


### 1. Queue


`Queue` 是 `queue` 模块中最常用的队列类型，它实现了标准的先进先出（FIFO）队列。以下是 `Queue` 的基本用法：


## 实例


```python
import queue

# 创建一个队列
q = queue.Queue()

# 向队列中添加元素
q.put(1)
q.put(2)
q.put(3)

# 从队列中获取元素
print(q.get())  # 输出: 1
print(q.get())  # 输出: 2
print(q.get())  # 输出: 3
```


### 2. LifoQueue


`LifoQueue` 是一种后进先出（LIFO）的队列，类似于栈。以下是 `LifoQueue` 的基本用法：


## 实例


```python
import queue

# 创建一个 LIFO 队列
q = queue.LifoQueue()

# 向队列中添加元素
q.put(1)
q.put(2)
q.put(3)

# 从队列中获取元素
print(q.get())  # 输出: 3
print(q.get())  # 输出: 2
print(q.get())  # 输出: 1
```


### 3. PriorityQueue


`PriorityQueue` 是一种优先级队列，元素按照优先级顺序被取出。以下是 `PriorityQueue` 的基本用法：


## 实例


```python
import queue

# 创建一个优先级队列
q = queue.PriorityQueue()

# 向队列中添加元素，元素为元组 (优先级, 数据)
q.put((3, 'Low priority'))
q.put((1, 'High priority'))
q.put((2, 'Medium priority'))

# 从队列中获取元素
print(q.get())  # 输出: (1, 'High priority')
print(q.get())  # 输出: (2, 'Medium priority')
print(q.get())  # 输出: (3, 'Low priority')
```


---


## 常用方法


### 1. put(item, block=True, timeout=None)


将 `item` 放入队列。如果 `block` 为 `True` 且队列已满，则等待 `timeout` 秒，直到队列有空闲空间。如果 `timeout` 为 `None`，则无限等待。


### 2. get(block=True, timeout=None)


从队列中获取并移除一个元素。如果 `block` 为 `True` 且队列为空，则等待 `timeout` 秒，直到队列中有元素。如果 `timeout` 为 `None`，则无限等待。


### 3. qsize()


返回队列中的元素数量。


### 4. empty()


如果队列为空，返回 `True`，否则返回 `False`。


### 5. full()


如果队列已满，返回 `True`，否则返回 `False`。


---


## 线程安全


`queue` 模块的所有队列类型都是线程安全的，这意味着多个线程可以安全地同时操作同一个队列，而不需要额外的同步机制。这使得 `queue` 模块成为多线程编程中传递数据的理想选择。


---


## 示例：多线程队列


以下是一个使用 `Queue` 在多线程之间传递数据的示例：


## 实例


```python
import queue
import threading
import time

# 创建一个队列
q = queue.Queue()

# 生产者线程
def producer():
    for i in range(5):
        print(f'生产 {i}')
        q.put(i)
        time.sleep(1)

# 消费者线程
def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f'消费 {item}')
        q.task_done()

# 启动生产者线程
producer_thread = threading.Thread(target=producer)
producer_thread.start()

# 启动消费者线程
consumer_thread = threading.Thread(target=consumer)
consumer_thread.start()

# 等待生产者线程完成
producer_thread.join()

# 等待队列中的所有任务完成
q.join()

# 发送结束信号
q.put(None)
consumer_thread.join()
```


---


## 常用的属性和方法


以下是 Python queue 模块（线程安全队列）的常用类、方法及属性的表格说明，包含功能描述和示例：


### queue 模块核心类

| 类 | 说明 | 适用场景 |
| --- | --- | --- |
| queue.Queue | 先进先出（FIFO）队列 | 通用任务队列 |
| queue.LifoQueue | 后进先出（LIFO）队列（类似栈） | 需要后进先出的场景 |
| queue.PriorityQueue | 优先级队列（最小堆实现） | 按优先级处理任务 |
| queue.SimpleQueue | 更简单的FIFO队列（Python 3.7+） | 不需要高级功能的场景 |


### 通用方法（所有队列类都支持）

| 方法 | 说明 | 示例 | 返回值 |
| --- | --- | --- | --- |
| put(item) | 放入元素 | q.put("task1") | None |
| get() | 取出并移除元素 | item = q.get() | 队列元素 |
| empty() | 判断队列是否为空 | if q.empty(): | True/False |
| full() | 判断队列是否已满 | if q.full(): | True/False |
| qsize() | 返回队列当前大小 | size = q.qsize() | 整数 |
| task_done() | 标记任务完成（用于join()） | q.task_done() | None |
| join() | 阻塞直到所有任务完成 | q.join() | None |


### 阻塞控制参数


| 参数 | 说明 | 默认值 | 示例 |
| --- | --- | --- | --- |
| block | 当队列为空/满时是否阻塞 | True | q.get(block=False) |
| timeout | 阻塞超时时间（秒） | None | q.put(x, timeout=5) |


### PriorityQueue 专用用法

**元素格式：**(priority, data)，优先级越小越先出队


## 实例


```python
pq = queue.PriorityQueue()
pq.put((1, "low"))
pq.put((0, "high"))
print(pq.get()[1])  # 输出: "high"
```


### 实例

生产者-消费者模型：


## 实例


```python
import queue, threading

q = queue.Queue(maxsize=3)  # 容量为3的队列

def producer():
    for i in range(5):
        q.put(f"Task-{i}")
        print(f"Produced: Task-{i}")

def consumer():
    while True:
        item = q.get()
        print(f"Consumed: {item}")
        q.task_done()

threading.Thread(target=producer, daemon=True).start()
threading.Thread(target=consumer, daemon=True).start()
q.join()  # 等待所有任务完成
```


优先级任务处理：


## 实例


```python
pq = queue.PriorityQueue()
pq.put((3, "Scan"))
pq.put((1, "Emergency"))
pq.put((2, "Log"))

while not pq.empty():
    print(pq.get()[1])  # 输出顺序: Emergency → Log → Scan
```


非阻塞获取（避免死锁）：


## 实例


```python
try:
    item = q.get_nowait()  # 等价于 q.get(block=False)
except queue.Empty:
    print("队列为空")
```









	  AI 思考中...





			** [Python subprocess 模块](https://www.runoob.com/python-subprocess.html)
			[Python csv 模块](https://www.runoob.com/python-csv.html) **













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