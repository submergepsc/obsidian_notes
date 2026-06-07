# IOS内存管理

- Source: https://www.runoob.com/ios/ios-memory.html

---


## 简介


iOS下内存管理的基本思想就是引用计数，通过对象的引用计数来对内存对象的生命周期进行控制。具体到编程时间方面，主要有两种方式：


1：MRR（manual retain-release），人工引用计数，对象的生成、销毁、引用计数的变化都是由开发人员来完成。


2：ARC（Automatic Reference Counting），自动引用计数，只负责对象的生成，其他过程开发人员不再需要关心其销毁，使用方式类似于垃圾回收，但其实质还是引用计数。


### 面临的问题


根据苹果说明文档，面临的两个主要问题是：


释放或覆盖的数据仍然在使用。这将造成内存损坏，通常在应用程序崩溃，或者更糟，损坏用户数据。


不释放不再使用的数据会导致内存泄漏。分配的内存，内存泄漏不会释放，即使它从来没有再次使用。泄漏会导致应用程序的内存使用量日益增加，这反过来又可能会导致系统性能较差或死机。


### 内存管理规则


我们创建自己的对象，当他们不再需要的时候，释放他们。


保留需要使用的对象。如果没有必要必须释放这些对象。


不要释放我们没有拥有的对象。


### 使用内存管理工具


可以用Xcode工具仪器的帮助下分析内存的使用情况。它包括的工具有活动监视器，分配，泄漏，僵尸等


### 分析内存分配的步骤


1. 打开一个现有的应用程序。


2. 选择产品，配置文件如下所示


![mm_Profile](https://www.runoob.com/wp-content/uploads/2013/11/mm_Profile.jpg)


3.在以下界面中选择 Allocations 和 Profile。


![mm_ProfileSelect](https://www.runoob.com/wp-content/uploads/2013/11/mm_ProfileSelect.jpg)


4. 我们可以看到不同对象的内存使用情况


5. 你可以切换视图控制器查看内存是否释放。 ![mm_Instruments_Allocations](https://www.runoob.com/wp-content/uploads/2013/11/mm_Instruments_Allocations.jpg)


6.同样我们可以使用 Activity Monitor 来查看内存在应用程序中的分配的情况。


![mm_Instruments_ActivityMonitor](https://www.runoob.com/wp-content/uploads/2013/11/mm_Instruments_ActivityMonitor.jpg)


7. 这些工具可以帮助我们了解内存的使用情况及在什么地方可能发生泄漏。








	  AI 思考中...





			** [iOS Twitter和Facebook](https://www.runoob.com/ios-twitter-facebook.html)
			[iOS应用程序调试](https://www.runoob.com/ios-application-debugging.html) **













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