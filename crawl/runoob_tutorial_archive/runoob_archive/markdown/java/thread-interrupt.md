# Java 实例 - 中断线程

- Source: https://www.runoob.com/java/thread-interrupt.html

[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)


以下实例演示了如何使用interrupt()方法来中断线程并使用 isInterrupted() 方法来判断线程是否已中断：


## Main.java 文件



```java
public class Main extends Object
implements Runnable {
   public void run() {
      try {
         System.out.println("in run() - 将运行 work2() 方法");
         work2();
         System.out.println("in run() - 从 work2() 方法回来");
      }
      catch (InterruptedException x) {
         System.out.println("in run() - 中断 work2() 方法");
         return;
      }
      System.out.println("in run() - 休眠后执行");
      System.out.println("in run() - 正常离开");
   }
   public void work2() throws InterruptedException {
      while (true) {
         if (Thread.currentThread().isInterrupted()) {
            System.out.println("C isInterrupted()=" + Thread.currentThread().isInterrupted());
            Thread.sleep(2000);
            System.out.println("D isInterrupted()=" + Thread.currentThread().isInterrupted());
         }
      }
   }
   public void work() throws InterruptedException {
      while (true) {
         for (int i = 0; i < 100000; i++) {
            int j = i * 2;
         }
         System.out.println("A isInterrupted()=" + Thread.currentThread().isInterrupted());
         if (Thread.interrupted()) {
            System.out.println("B isInterrupted()=" + Thread.currentThread().isInterrupted());
            throw new InterruptedException();
         }
      }
   }
   public static void main(String[] args) {
      Main si = new Main();
      Thread t = new Thread(si);
      t.start();
      try {
         Thread.sleep(2000);
      }
      catch (InterruptedException x) {
      }
      System.out.println("in main() - 中断其他线程");
      t.interrupt();
      System.out.println("in main() - 离开");
   }
}
```


以上代码运行输出结果为：


```
in run() - 将运行 work2() 方法
in main() - 中断其他线程
in main() - 离开
C isInterrupted()=true
in run() - 中断 work2() 方法
```


[![Java 实例](https://www.runoob.com/images/up.gif) Java 实例](https://www.runoob.com/java-examples.html)








	  AI 思考中...





			** [Java 实例 – 获取线程状态](https://www.runoob.com/thread-status.html)
			[Java 8 新特性](https://www.runoob.com/java8-new-features.html) **













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