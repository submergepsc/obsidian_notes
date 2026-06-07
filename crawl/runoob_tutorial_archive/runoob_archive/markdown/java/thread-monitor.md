# Java 实例 - 状态监测

- Source: https://www.runoob.com/java/thread-monitor.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何通过继承 Thread 类并使用 currentThread.getName() 方法来监测线程的状态：


## Main.java 文件



```java
class MyThread extends Thread{
   boolean waiting= true;
   boolean ready= false;
   MyThread() {
   }
   public void run() {
      String thrdName = Thread.currentThread().getName();
      System.out.println(thrdName + " starting.");
      while(waiting)
      System.out.println("waiting:"+waiting);
      System.out.println("waiting...");
      startWait();
      try {
         Thread.sleep(1000);
      }
      catch(Exception exc) {
         System.out.println(thrdName + " interrupted.");
      }
      System.out.println(thrdName + " terminating.");
   }
   synchronized void startWait() {
      try {
         while(!ready) wait();
      }
      catch(InterruptedException exc) {
         System.out.println("wait() interrupted");
      }
   }
   synchronized void notice() {
      ready = true;
      notify();
   }
}
public class Main {
   public static void main(String args[])
   throws Exception{
      MyThread thrd = new MyThread();
      thrd.setName("MyThread #1");
      showThreadStatus(thrd);
      thrd.start();
      Thread.sleep(50);
      showThreadStatus(thrd);
      thrd.waiting = false;
      Thread.sleep(50);
      showThreadStatus(thrd);
      thrd.notice();
      Thread.sleep(50);
      showThreadStatus(thrd);
      while(thrd.isAlive())
      System.out.println("alive");
      showThreadStatus(thrd);
   }
   static void showThreadStatus(Thread thrd) {
      System.out.println(thrd.getName() + "Alive:=" + thrd.isAlive() + " State:=" + thrd.getState());
   }
}
```


以上代码运行输出结果为：


```
……
alive
alive
MyThread #1 terminating.
alive
……
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 线程优先级设置](https://www.runoob.com/thread-getpri.html)
			[Java 实例 – 获取当前线程名称](https://www.runoob.com/thread-name.html) **













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