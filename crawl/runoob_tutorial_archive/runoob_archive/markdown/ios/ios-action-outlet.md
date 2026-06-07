# 

- Source: https://www.runoob.com/ios/ios-action-outlet.html

## 简介

在iOS中，操作（action）和输出口（Outlet）指的是ibActions和ibOutlets，也就是ib接口生成器所在的地方。这些都和UI元素相关，我们将直观的了解他们后探讨如何实现他们。

## 步骤


1、让我们使用第一款iPhone应用程序。


2、从导航部分中的文件中选择ViewController.xib文件


3、从右手边得窗口下面显示的窗口格库中选择UI元素


![objectLibrary](https://www.runoob.com/wp-content/uploads/2013/11/objectLibrary.jpg)


4、拖拽UI元素到界面生成器的可视框中


5、添加标签和红色圆形按钮到可视图中


![interfaceAction](https://www.runoob.com/wp-content/uploads/2013/11/interfaceAction.jpg)


6、在工作区工具栏的右上角找到编辑器选择按钮，如下图所示


![StandardEditor](https://www.runoob.com/wp-content/uploads/2013/11/StandardEditor.jpg)


**选择编辑器按钮**


![AssistantEditor](https://www.runoob.com/wp-content/uploads/2013/11/AssistantEditor.jpg)


7、编辑器区域中心有两个窗口，ViewController.xib文件和ViewController.h


8、右击标签上的选择按钮，按住并拖动新引用参照，如下所示


![ibOutletDrag](https://www.runoob.com/wp-content/uploads/2013/11/ibOutletDrag.jpg)


9、现在放在ViewController.h之间的大括号中。也可以放在文件中，如果是这样，必须在做这个之前已经添加了。如下所示


![ibOutletDrop](https://www.runoob.com/wp-content/uploads/2013/11/ibOutletDrop.jpg)


10. 输入输出口（Outlet）的标签名称，这里给出的是myTitleLable。单击链接，完成ibOutlet


11、同样的，添加操作，只需右击倒圆角矩形，选择触摸内心拖动它下方的大括号


![ActionDrag](https://www.runoob.com/wp-content/uploads/2013/11/ActionDrag.jpg)


12、重新命名为setTitleLable


![ActionDrop](https://www.runoob.com/wp-content/uploads/2013/11/ActionDrop.jpg)


13、 选择ViewController.m文件，有一种方法，如下所示


```
-(IBAction) setTitleLabel:(id)sender{
}
```


14、在上述的方法内，如下所示，添加一个语句


```
[myTitleLabel setTitleText:@"Hello"];
```


15、选择运行按钮运行该程序，得到如下的输出


![IBActionTutorial.Simulator_Start](https://www.runoob.com/wp-content/uploads/2013/11/IBActionTutorial.Simulator_Start.jpg)


16、单击按钮


![IBActionTutorial.Simulator_end](https://www.runoob.com/wp-content/uploads/2013/11/IBActionTutorial.Simulator_end.jpg)


17.、创建的参照（outlets）按钮标签已更改为对按钮执行的操作（actions）


18、由上可知，IBOutlet将创建对UIElement的引用（此处为UILable），同样的IBAction和UIButton通过执行操作和UIButton相链接。


19、当创建动作时通过选择不同的事件你可以做不同的操作。








	  AI 思考中...





			** [创建第一款iPhone应用程序](https://www.runoob.com/ios-first-iphone-application.html)
			[iOS – 委托（Delegates）](https://www.runoob.com/ios-delegates.html) **













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