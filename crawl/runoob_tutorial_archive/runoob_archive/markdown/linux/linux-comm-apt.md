# Linux apt 命令

- Source: https://www.runoob.com/linux/linux-comm-apt.html

apt（Advanced Packaging Tool）是一个在 Debian 和 Ubuntu 中的 Shell 前端软件包管理器。


apt 命令提供了查找、安装、升级、删除某一个、一组甚至全部软件包的命令，而且命令简洁而又好记。


apt 命令执行需要超级管理员权限(root)。


### apt 语法


```
apt [options] [command] [package ...]
```


- **options：**可选，选项包括 -h（帮助），-y（当安装过程提示选择全部为"yes"），-q（不显示安装的过程）等等。
- **command：**要进行的操作。
- **package**：安装的包名。


---

## apt 常用命令


- 列出所有可更新的软件清单命令：**sudo apt update**
- 升级软件包：**sudo apt upgrade** 列出可更新的软件包及版本信息：**apt list --upgradable** 升级软件包，升级前先删除需要更新软件包：**sudo apt full-upgrade**
- 安装指定的软件命令：**sudo apt install
** 安装多个软件包：**sudo apt install ** - 更新指定的软件命令：**sudo apt update ** - 显示软件包具体信息,例如：版本号，安装大小，依赖关系等等：**sudo apt show ** - 删除软件包命令：**sudo apt remove ** - 清理不再使用的依赖和库文件: **sudo apt autoremove** - 移除软件包及配置文件: **sudo apt purge ** - 查找软件包命令： **sudo apt search ** - 列出所有已安装的包：**apt list --installed** - 列出所有已安装的包的版本信息：**apt list --all-versions** ### 实例 查看一些可更新的包：


```
sudo apt update
```


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples.png)


升级安装包：


```
sudo apt upgrade
```


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples-1.png)


在以上交互式输入字母 **Y** 即可开始升级。


可以将以下两个命令组合起来，一键升级：


```
sudo apt update && sudo apt upgrade -y
```


安装 mplayer 包：


```
sudo apt install mplayer
```


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples-3.png)


如过不太记得完整的包名，我们可以只输入前半部分的包名，然后按下 **Tab** 键，会列出相关的包名：


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples-2.png)


以上实例我们输入来 **reds**，然后按下 **Tab** 键，输出来四个相关的包。


如果我们想安装一个软件包，但如果软件包已经存在，则不要升级它，可以使用 **–no-upgrade** 选项:


```
sudo apt install <package_name> --no-upgrade
```


安装 mplayer 如果存在则不要升级：


```
sudo apt install mplayer --no-upgrade
```


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples-4.png)


如果只想升级，不要安装可以使用 **--only-upgrade** 参数：


```
sudo apt install <package_name> --only-upgrade
```


只升级 mplayer，如果不存在就不要安装它：


```
sudo apt install mplayer --only-upgrade
```


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples-5.png)


如果需要设置指定版本，语法格式如下：


```
sudo apt install <package_name>=<version_number>
```


**package_name** 为包名，**version_number** 为版本号。


移除包可以使用 remove 命令：


```
sudo apt remove mplayer
```


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples-6-e1499720021872.png)


查找名为 libimobile 的相关包：


```
apt search libimobile
```


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples-8.png)


查看 pinta 包的相关信息：


```
apt show pinta
```


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples-7.png)


列出可更新的软件包：


```
apt list --upgradeable
```


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples-9.png)


清理不再使用的依赖和库文件：


```
sudo apt autoremove
```


![](https://www.runoob.com/wp-content/uploads/2020/09/apt-commands-examples-10.png)


在以上交互式输入字母 **Y** 即可开始清理。








	  AI 思考中...





			** [Linux pkill 命令](https://www.runoob.com/linux-comm-pkill.html)
			[Linux man 命令](https://www.runoob.com/linux-comm-man.html) **













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