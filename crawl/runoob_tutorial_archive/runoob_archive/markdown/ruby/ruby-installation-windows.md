# Ruby 安装 - Windows

- Source: https://www.runoob.com/ruby/ruby-installation-windows.html

下面列出了在 Windows 机器上安装 Ruby 的步骤。


下载地址：


- 官网：[http://rubyinstaller.org/downloads/](http://rubyinstaller.org/downloads/)
- 国内：[https://rubyinstaller.cn/](https://rubyinstaller.cn/)


**注意：**在安装时，您可能有不同的可用版本。


- Window 系统下，我们可以使用 RubyInstaller 来安装 Ruby 环境，下载地址为：[请点击这里下载](http://rubyinstaller.org/downloads/)。
- 下载 rubyinstaller 之后，解压到新创建的目录下：
- 双击 rubyinstaller-2.2.3.exe 文件，启动 Ruby 安装向导。
- 点击 Next，继续向导，记得勾选 **Add Ruby executables to your PATH**，直到 Ruby 安装程序完成 Ruby 安装为止。


如果您的安装没有适当地配置环境变量，接下来您可能需要进行环境变量的配置。


- 如果您使用的是 Windows 9x，那么请在您的 c:\autoexec.bat 中添加：set PATH="D:\(ruby 安装目录)\bin;%PATH%"
- Windows NT/2000 用户需要修改注册表。 点击控制面板|系统性能|环境变量。
- 在系统变量下，选择 Path，并点击 EDIT。
- 在变量值列表的末尾添加 Ruby 目录，并点击 OK。
- 在系统变量下，选择 PATHEXT，并点击 EDIT。
- 添加 .RB 和 .RBW 到变量值列表中，并点击 OK。


- 安装后，通过在命令行中输入以下命令来确保一切工作正常：


```
$ ruby -v
ruby 2.2.3
```


- 如果一切工作正常，将会输出所安装的 Ruby 解释器的版本，如上所示。如果您安装了其他版本，则会显示其他不同的版本。








	  AI 思考中...





			** [Ruby 安装 – Linux](https://www.runoob.com/ruby-installation-unix.html)
			[Ruby 命令行选项](https://www.runoob.com/ruby-command-line-options.html) **













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