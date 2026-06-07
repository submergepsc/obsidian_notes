# Eclipse Debug 调试

- Source: https://www.runoob.com/eclipse/eclipse-debugging-program.html

---


## Debug 调试 Java 程序


我们可以在 Package Explorer 视图调试 Java 程序，操作步骤如下：


- 鼠标右击包含 main 函数的 java 类
- 选择 Debug As > Java Application


该操作也可以通过快捷键来完成，快捷键组合为 Alt + Shift + D, J。 以上操作会创建一个新的 [Debug Configuration（调试配置）](https://www.runoob.com/eclipse-debug-configuration.html) ，并使用该配置来启动 Java 应用。


如果 Debug Configuration（调试配置）已经创建，你可以通过 Run 菜单选择 Debug Configurations 选取对应的类并点击 Debug 按钮来启动 Java 应用。


![](https://www.runoob.com/wp-content/uploads/2014/12/debug_program_1.jpg)

Run 菜单的 Debug 菜单项可以重新加载之前使用了调试模式的 java 应用。

![debug_program_menu](https://www.runoob.com/wp-content/uploads/2014/12/debug_program_menu.jpg)

重新加载之前使用了调试模式的 java 应用快捷键为 F11。


当使用调试模式开启java程序时，会提示用户切换到调试的透视图。调试透视图提供了其他的视图用于排查应用程序的故障。


java 编辑器可以设置断点调试。 在编辑器中右击标记栏并选择 Toggle Breakpoint 来设置断点调试。


![](https://www.runoob.com/wp-content/uploads/2014/12/debug_program_2.jpg)

断点可以在标记栏中看到。也可以在 Breakpoints View（断点视图）中看到。


当程序执行到断点标记的代码时 JVM 会挂起程序，这时你可以查看内存使用情况及控制程序执行。


程序挂起时，Debug(调试)视图可以检查调用堆栈。

![](https://www.runoob.com/wp-content/uploads/2014/12/debug_program_3.jpg)


variables(变量)视图可以查看变量的值。


![](https://www.runoob.com/wp-content/uploads/2014/12/debug_program_4.jpg)

Run 菜单中有继续执行(Resume)菜单项，跳过(Step Over)一行代码，进入函数(Step Into)等。


![](https://www.runoob.com/wp-content/uploads/2014/12/debug_program_5.jpg)

以上图片中显示了 Resume, Step Into 和 Step Over 等关联的快捷键操作。








	  AI 思考中...





			** [Eclipse Debug 配置](https://www.runoob.com/eclipse-debug-configuration.html)
			[Eclipse 首选项(Preferences)](https://www.runoob.com/eclipse-preferences.html) **













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