# Java 实例 - 线程优先级设置

- Source: https://www.runoob.com/java/thread-getpri.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何通过setPriority() 方法来设置线程的优先级：


## SimplePriorities.java 文件



```java
public class SimplePriorities extends Thread {
   private int countDown = 5;
   private volatile double d = 0;
   public SimplePriorities(int priority) {
      setPriority(priority);
      start();
   }
   public String toString() {
      return super.toString() + ": " + countDown;
   }
   public void run() {
      while(true) {
         for(int i = 1; i < 100000; i++)
         d = d + (Math.PI + Math.E) / (double)i;
         System.out.println(this);
         if(--countDown == 0) return;
      }
   }
   public static void main(String[] args) {
      new SimplePriorities(Thread.MAX_PRIORITY);
      for(int i = 0; i < 5; i++)
      new SimplePriorities(Thread.MIN_PRIORITY);
   }
}
```


以上代码运行输出结果为：


```
Thread[Thread-1,1,main]: 5
Thread[Thread-2,1,main]: 5
Thread[Thread-3,1,main]: 5
Thread[Thread-0,10,main]: 5
Thread[Thread-3,1,main]: 4
Thread[Thread-0,10,main]: 4
Thread[Thread-1,1,main]: 4
Thread[Thread-5,1,main]: 5
Thread[Thread-4,1,main]: 5
Thread[Thread-2,1,main]: 4
Thread[Thread-0,10,main]: 3
Thread[Thread-1,1,main]: 3
Thread[Thread-4,1,main]: 4
Thread[Thread-2,1,main]: 3
……
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 死锁及解决方法](https://www.runoob.com/thread-deadlock.html)
			[Java 实例 – 状态监测](https://www.runoob.com/thread-monitor.html) **













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