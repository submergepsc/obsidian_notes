# Go 语言开发工具

- Source: https://www.runoob.com/go/go-ide.html

---


## VSCode


VScode 安装教程参见：[https://www.runoob.com/w3cnote/vscode-tutorial.html](https://www.runoob.com/w3cnote/vscode-tutorial.html)


然后我们打开 VSCode 的扩展（**Ctrl+Shift+P**）：


![](https://www.runoob.com/wp-content/uploads/2015/06/go-vscode-1.jpeg)


搜索 **go**：


![](https://www.runoob.com/wp-content/uploads/2015/06/go-vscode-2.jpeg)


点击安装，安装完成后我们就可以使用代码提示、测试、调试等功能了。


![](https://static.jyshare.com/images/mix/completion-signature-help.gif)


---


## GoLand


GoLand 是 Jetbrains 家族的 Go 语言 IDE，有 30 天的免费试用期。


安装也很简单访问 [Goland 的下载页面](https://www.jetbrains.com/go/)，根据你当期的系统环境三大平台（Mac、Linux、Windows）下载对应的软件。


![](https://www.runoob.com/wp-content/uploads/2015/06/GoLand-01.jpg)


---


## LiteIDE


LiteIDE 是一款开源、跨平台的轻量级 Go 语言集成开发环境（IDE）。


### 支持的 操作系统


- Windows x86 (32-bit or 64-bit)
- Linux x86 (32-bit or 64-bit)


下载地址 ：[http://sourceforge.net/projects/liteide/files/](http://sourceforge.net/projects/liteide/files/)

源码地址 ：[https://github.com/visualfc/liteide](https://github.com/visualfc/liteide)


![](https://www.runoob.com/wp-content/uploads/2015/06/1.4.liteide.png)

---


## Eclipse


Eclipse 也是非常常用的开发利器，以下介绍如何使用 Eclipse 来编写 Go 程序。
![1.4.eclipse1](https://www.runoob.com/wp-content/uploads/2015/06/1.4.eclipse1.pngrawtrue)


Eclipse 编辑 Go 的主界面


- 首先下载并安装好 [Eclipse](http://www.eclipse.org/)
- 下载 [goclipse](http://goclipse.github.io/) 插件 [https://github.com/GoClipse/goclipse/blob/latest/documentation/Installation.md#installation](https://github.com/GoClipse/goclipse/blob/latest/documentation/Installation.md#installation)
- 下载 gocode，用于 go 的代码补全提示 gocode 的 github 地址：
```
https://github.com/nsf/gocode
```
 在 Windows下要安装 git，通常用 [msysgit](https://gitforwindows.org/)。 再在 cmd 下安装：
```
go get -u github.com/nsf/gocode
```
 也可以下载代码，直接用 go build 来编译，会生成 gocode.exe
- 下载 [MinGW](http://sourceforge.net/projects/mingw/files/MinGW/) 并按要求装好
- 配置插件 Windows->Reference->Go (1)、配置 Go 的编译器 ![1.4.eclipse2](https://www.runoob.com/wp-content/uploads/2015/06/1.4.eclipse2.pngrawtrue) 设置 Go 的一些基础信息 (2)、配置 Gocode（可选，代码补全），设置 Gocode 路径为之前生成的 gocode.exe 文件 ![1.4.eclipse3](https://www.runoob.com/wp-content/uploads/2015/06/1.4.eclipse3.pngrawtrue) 设置 gocode 信息 (3)、配置 GDB（可选，做调试用），设置 GDB 路径为 MingW 安装目录下的 gdb.exe 文件![1.4.eclipse4](https://www.runoob.com/wp-content/uploads/2015/06/1.4.eclipse4.pngrawtrue)设置 GDB 信息
- 测试是否成功 新建一个 go 工程，再建立一个 hello.go。如下图： ![1.4.eclipse5](https://www.runoob.com/wp-content/uploads/2015/06/1.4.eclipse5.pngrawtrue) 新建项目编辑文件 调试如下（要在 console 中用输入命令来调试）： ![1.4.eclipse6](https://www.runoob.com/wp-content/uploads/2015/06/1.4.eclipse6.pngrawtrue) 图 1.16 调试 Go 程序








	  AI 思考中...





			** [Go 错误处理](https://www.runoob.com/go-error-handling.html)
			[Go 并发](https://www.runoob.com/go-concurrent.html) **













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