# Java 实例 - 获取线程id

- Source: https://www.runoob.com/java/thread-id.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何使用 getThreadId() 方法获取线程id：


## Main.java 文件



```java
public class Main extends Object implements Runnable {
  private ThreadID var;

  public Main(ThreadID v) {
    this.var = v;
  }

  public void run() {
    try {
      print("var getThreadID =" + var.getThreadID());
      Thread.sleep(2000);
      print("var getThreadID =" + var.getThreadID());
    } catch (InterruptedException x) {
    }
  }

  private static void print(String msg) {
    String name = Thread.currentThread().getName();
    System.out.println(name + ": " + msg);
  }

  public static void main(String[] args) {
    ThreadID tid = new ThreadID();
    Main shared = new Main(tid);

    try {
      Thread threadA = new Thread(shared, "threadA");
      threadA.start();

      Thread.sleep(500);

      Thread threadB = new Thread(shared, "threadB");
      threadB.start();

      Thread.sleep(500);

      Thread threadC = new Thread(shared, "threadC");
      threadC.start();
    } catch (InterruptedException x) {
    }
  }
}

class ThreadID extends ThreadLocal {
  private int nextID;

  public ThreadID() {
    nextID = 10001;
  }

  private synchronized Integer getNewID() {
    Integer id = new Integer(nextID);
    nextID++;
    return id;
  }

  protected Object initialValue() {
    print("in initialValue()");
    return getNewID();
  }

  public int getThreadID() {
    Integer id = (Integer) get();
    return id.intValue();
  }

  private static void print(String msg) {
    String name = Thread.currentThread().getName();
    System.out.println(name + ": " + msg);
  }
}
```


以上代码运行输出结果为：


```
threadA: in initialValue()
threadA: var getThreadID =10001
threadB: in initialValue()
threadB: var getThreadID =10002
threadC: in initialValue()
threadC: var getThreadID =10003
threadA: var getThreadID =10001
threadB: var getThreadID =10002
threadC: var getThreadID =10003
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 线程挂起](https://www.runoob.com/thread-suspend.html)
			[Java 实例 – 查看线程优先级](https://www.runoob.com/thread-priorityinfo.html) **













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