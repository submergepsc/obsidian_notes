# Java 实例 - 获取线程状态

- Source: https://www.runoob.com/java/thread-status.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


Java 线程的生命周期中，在 Thread 类里有一个枚举类型 State，定义了线程的几种状态，分别有：


- New
- Runnable
- Blocked
- Waiting
- Timed Waiting
- Terminated

![](https://www.runoob.com/wp-content/uploads/2015/05/threadLifeCycle.jpg)

各个状态说明：


### 1. 初始状态 - NEW


声明：


```
public static final Thread.State NEW
```


实现 Runnable 接口和继承 Thread 可以得到一个线程类，new 一个实例出来，线程就进入了初始状态。


### 2. RUNNABLE


声明：


```
public static final Thread.State RUNNABLE
```


**2.1. 就绪状态**


就绪状态只是说你资格运行，调度程序没有挑选到你，你就永远是就绪状态。


调用线程的 start() 方法，此线程进入就绪状态。


当前线程 sleep() 方法结束，其他线程 join() 结束，等待用户输入完毕，某个线程拿到对象锁，这些线程也将进入就绪状态。


当前线程时间片用完了，调用当前线程的 yield() 方法，当前线程进入就绪状态。


锁池里的线程拿到对象锁后，进入就绪状态。


**2.2. 运行中状态**


线程调度程序从可运行池中选择一个线程作为当前线程时线程所处的状态。这也是线程进入运行状态的唯一一种方式。


### 3. 阻塞状态 - BLOCKED


声明：


```
public static final Thread.State BLOCKED
```


阻塞状态是线程阻塞在进入synchronized关键字修饰的方法或代码块(获取锁)时的状态。


### 4. 等待 - WAITING


声明：


```
public static final Thread.State WAITING
```


处于这种状态的线程不会被分配 CPU 执行时间，它们要等待被显式地唤醒，否则会处于无限期等待的状态。


**5. 超时等待 - TIMED_WAITING**


声明：


```
public static final Thread.State TIMED_WAITING
```


处于这种状态的线程不会被分配 CPU 执行时间，不过无须无限期等待被其他线程显示地唤醒，在达到一定时间后它们会自动唤醒。


### 6. 终止状态 - TERMINATED


声明：


```
public static final Thread.State TERMINATED
```


当线程的 run() 方法完成时，或者主线程的 main() 方法完成时，我们就认为它终止了。这个线程对象也许是活的，但是，它已经不是一个单独执行的线程。线程一旦终止了，就不能复生。


在一个终止的线程上调用 start() 方法，会抛出 java.lang.IllegalThreadStateException 异常。


以下实例演示了如何获取线程的状态：


## Main.java 文件



```java
// Java 程序 - 演示线程状态
class thread implements Runnable
{
    public void run()
    {
        //  thread2  - 超时等待
        try
        {
            Thread.sleep(1500);
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }

        System.out.println("State of thread1 while it called join() method on thread2 -"+
            Test.thread1.getState());
        try
        {
            Thread.sleep(200);
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }
    }
}

public class Test implements Runnable
{
    public static Thread thread1;
    public static Test obj;

    public static void main(String[] args)
    {
        obj = new Test();
        thread1 = new Thread(obj);

        // 创建 thread1，现在是初始状态
        System.out.println("State of thread1 after creating it - " + thread1.getState());
        thread1.start();

        // thread1 - 就绪状态
        System.out.println("State of thread1 after calling .start() method on it - " +
            thread1.getState());
    }

    public void run()
    {
        thread myThread = new thread();
        Thread thread2 = new Thread(myThread);

        // 创建 thread1，现在是初始状态
        System.out.println("State of thread2 after creating it - "+ thread2.getState());
        thread2.start();

        // thread2 - 就绪状态
        System.out.println("State of thread2 after calling .start() method on it - " +
            thread2.getState());

        // moving thread1 to timed waiting state
        try
        {
            //moving - 超时等待
            Thread.sleep(200);
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }
        System.out.println("State of thread2 after calling .sleep() method on it - "+
            thread2.getState() );

        try
        {
            // 等待 thread2 终止
            thread2.join();
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }
        System.out.println("State of thread2 when it has finished it's execution - " +
            thread2.getState());
    }

}
```


以上代码运行输出结果为：


```
State of thread1 after creating it - NEW
State of thread1 after calling .start() method on it - RUNNABLE
State of thread2 after creating it - NEW
State of thread2 after calling .start() method on it - RUNNABLE
State of thread2 after calling .sleep() method on it - TIMED_WAITING
State of thread1 while it called join() method on thread2 -WAITING
State of thread2 when it has finished it's execution - TERMINATED
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 获取所有线程](https://www.runoob.com/thread-showall.html)
			[Java 实例 – 中断线程](https://www.runoob.com/thread-interrupt.html) **













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

      : ·[Java 实例](https://www.runoob.com/java-examples.html)





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