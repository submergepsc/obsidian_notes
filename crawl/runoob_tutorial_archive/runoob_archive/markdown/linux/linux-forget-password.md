# Linux 忘记密码解决方法

- Source: https://www.runoob.com/linux/linux-forget-password.html

很多朋友经常会忘记Linux系统的root密码，linux系统忘记root密码的情况该怎么办呢？重新安装系统吗？当然不用！进入单用户模式更改一下root密码即可。

步骤如下：


### 重启linux系统


![](https://www.runoob.com/wp-content/uploads/2014/06/4_21.png)


3 秒之内要按一下回车，出现如下界面


![](https://www.runoob.com/wp-content/uploads/2014/06/4_22.png)


然后输入e


![](https://www.runoob.com/wp-content/uploads/2014/06/4_23.png)


在 第二行最后边输入 single，有一个空格。具体方法为按向下尖头移动到第二行，按"e"进入编辑模式


![](https://www.runoob.com/wp-content/uploads/2014/06/4_24.png)

在后边加上single 回车


![](https://www.runoob.com/wp-content/uploads/2014/06/4_25.png)


最后按"b"启动，启动后就进入了单用户模式了


![](https://www.runoob.com/wp-content/uploads/2014/06/4_26.png)


此时已经进入到单用户模式了，你可以更改root密码了。更密码的命令为 passwd


![](https://www.runoob.com/wp-content/uploads/2014/06/4_27.png)


【**使用系统安装光盘的救援模式**】


救援模式即rescue ，这个模式主要是应用于，系统无法进入的情况。如，grub损坏或者某一个配置文件修改出错。如何使用rescue模式呢？


光盘启动，按F5 进入rescue模式


![](https://www.runoob.com/wp-content/uploads/2014/06/4_28.png)


输入linux rescue 回车


![](https://www.runoob.com/wp-content/uploads/2014/06/4_29.png)


选择语言，笔者建议你选择英语


![](https://www.runoob.com/wp-content/uploads/2014/06/4_30.png)


选择us 键盘


![](https://www.runoob.com/wp-content/uploads/2014/06/4_31.png)


![](https://www.runoob.com/wp-content/uploads/2014/06/4_32.png)


这里问你是否启动网络，有时候可能会联网调试。我们选no


![](https://www.runoob.com/wp-content/uploads/2014/06/4_33.png)


这里告诉我们，接下来会把系统挂载在/mnt/sysimage 中。

其中有三个选项:


- Continue 就是挂载后继续下一步。
- Read-Only 挂载成只读，这样更安全，有时文件系统损坏时，只读模式会防止文件系统进一步损坏。
- Skip就是不挂载，进入一个命令窗口模式。

这里我们选择Continue。


![](https://www.runoob.com/wp-content/uploads/2014/06/4_34.png)


至此，系统已经挂载到了/mnt/sysimage中。接下来回车，输入chroot /mnt/sysimage 进入管理员环境。


![](https://www.runoob.com/wp-content/uploads/2014/06/4_35.png)


**提示：** 其实也可以到rescue模式下更改root的密码的。这个rescue模式和windows PE系统很相近。


当运行了chroot /mnt/sysimage/ 后，再ls 看到目录结构和原来系统中的目录结构是一样的。

没错！现在的环境和原来系统的环境是一模一样的。你可以输入exit 或者按Ctrl + D退出这个环境。然后你再ls 看一下


![](https://www.runoob.com/wp-content/uploads/2014/06/4_36.png)


这个目录其实就是rescue模式下的目录结构，而我们的系统文件全部在 /mnt/sysimage目录下。








	  AI 思考中...





			** [Linux 系统目录结构](https://www.runoob.com/linux-system-contents.html)
			[Linux 远程登录](https://www.runoob.com/linux-remote-login.html) **













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