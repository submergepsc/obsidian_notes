# Ruby 环境变量

- Source: https://www.runoob.com/ruby/ruby-environment-variables.html

Ruby 解释器使用下列环境变量来控制它的行为。ENV 对象包含了所有当前设置的环境变量列表。


| 变量 | 描述 |
| --- | --- |
| DLN_LIBRARY_PATH | 动态加载模块搜索的路径。 |
| HOME | 当没有参数传递给 Dir::chdir 时，要移动到的目录。也用于 File::expand_path 来扩展 "~"。 |
| LOGDIR | 当没有参数传递给 Dir::chdir 且未设置环境变量 HOME 时，要移动到的目录。 |
| PATH | 执行子进程的搜索路径，以及在指定 -S 选项后，Ruby 程序的搜索路径。每个路径用冒号分隔（在 DOS 和 Windows 中用分号分隔）。 |
| RUBYLIB | 库的搜索路径。每个路径用冒号分隔（在 DOS 和 Windows 中用分号分隔）。 |
| RUBYLIB_PREFIX | 用于修改 RUBYLIB 搜索路径，通过使用格式 path1;path2 或 path1path2，把库的前缀 path1 替换为 path2。 |
| RUBYOPT | 传给 Ruby 解释器的命令行选项。在 taint 模式时被忽略（其中，$SAFE 大于 0）。 |
| RUBYPATH | 指定 -S 选项后，Ruby 程序的搜索路径。优先级高于 PATH。在 taint 模式时被忽略（其中，$SAFE 大于 0）。 |
| RUBYSHELL | 指定执行命令时所使用的 shell。如果未设置该环境变量，则使用 SHELL 或 COMSPEC。 |


对于 Unix，使用 **env** 命令来查看所有环境变量的列表。


```
HOSTNAME=ip-72-167-112-17.ip.secureserver.net
RUBYPATH=/usr/bin
SHELL=/bin/bash
TERM=xterm
HISTSIZE=1000
SSH_CLIENT=122.169.131.179 1742 22
SSH_TTY=/dev/pts/1
USER=amrood
JRE_HOME=/usr/java/jdk/jre
J2RE_HOME=/usr/java/jdk/jre
PATH=/usr/local/bin:/bin:/usr/bin:/home/guest/bin
MAIL=/var/spool/mail/guest
PWD=/home/amrood
INPUTRC=/etc/inputrc
JAVA_HOME=/usr/java/jdk
LANG=C
HOME=/root
SHLVL=2
JDK_HOME=/usr/java/jdk
LOGDIR=/usr/log/ruby
LOGNAME=amrood
SSH_CONNECTION=122.169.131.179 1742 72.167.112.17 22
LESSOPEN=|/usr/bin/lesspipe.sh %s
RUBYLIB=/usr/lib/ruby
G_BROKEN_FILENAMES=1
_=/bin/env
```









	  AI 思考中...





			** [Ruby 命令行选项](https://www.runoob.com/ruby-command-line-options.html)
			[Ruby 语法](https://www.runoob.com/ruby-syntax.html) **













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