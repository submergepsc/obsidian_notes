# ASP Drive 对象

- Source: https://www.runoob.com/asp/asp-ref-drive.html

---


Drive 对象用于返回关于本地磁盘驱动器或者网络共享驱动器的信息。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[取得指定驱动器的总容量](https://www.runoob.com/try/showasp.php?filename=demo_totalsize)** 本例演示如何使用 TotalSize 属性来获得指定驱动器的总容量。


[取得指定驱动器的可用空间数](https://www.runoob.com/try/showasp.php?filename=demo_availablespace) 本例演示如何首先创建一个 FileSystemObject 对象，然后使用 AvailableSpace 属性来获得指定驱动器的可用空间。


[取得指定驱动器的剩余空间容量](https://www.runoob.com/try/showasp.php?filename=demo_freespace) 本例演示如何使用 FreeSpace 空间属性来取得指定驱动器的剩余空间。


[取得指定驱动器的驱动器字母](https://www.runoob.com/try/showasp.php?filename=demo_driveletter) 本例演示如何使用 DriveLetter 属性来获得指定驱动器的驱动器字母。


[取得指定驱动器的驱动器类型](https://www.runoob.com/try/showasp.php?filename=demo_drivetype) 本例演示如何使用 DriveType 属性来获得指定驱动器的驱动器类型。


[取得指定驱动器的文件系统信息](https://www.runoob.com/try/showasp.php?filename=demo_filesystem) 本例演示如何使用 FileSystem 来取得指定驱动器的文件系统信息。


[驱动器是否已就绪？](https://www.runoob.com/try/showasp.php?filename=demo_isready) 本例演示如何使用 IsReady 属性来检查指定的驱动器是否已就绪。


[取得指定驱动器的路径](https://www.runoob.com/try/showasp.php?filename=demo_path) 本例演示如何使用 Path 属性来取得指定驱动器的路径。


[取得指定驱动器的根文件夹](https://www.runoob.com/try/showasp.php?filename=demo_rootfolder) 本例演示如何使用 RootFolder 属性来取得指定驱动器的根文件夹。


[取得指定驱动器的序列号](https://www.runoob.com/try/showasp.php?filename=demo_serialnumber) 本例演示如何使用 Serialnumber 属性来取得指定驱动器的序列号。


---


## Drive 对象


Drive 对象用于返回关于本地磁盘驱动器或者网络共享驱动器的信息。Drive 对象可以返回有关驱动器的文件系统类型、剩余容量、序列号、卷标名等信息。


注释：**您无法通过 Drive 对象返回有关驱动器内容的信息。要达到这个目的，请使用 Folder 对象。


如需操作 Drive 对象的相关属性，您需要通过 FileSystemObject 对象来创建 Drive 对象的实例。首先，创建一个 FileSystemObject 对象，然后通过 FileSystemObject 对象的 GetDrive 方法或者 Drives 属性来实例化 Drive 对象。


Drive 对象的属性描述如下：


### 属性


| 属性 | 描述 |
| --- | --- |
| AvailableSpace | 向用户返回在指定的驱动器或网络共享驱动器上的可用空间容量。 |
| DriveLetter | 返回识别本地驱动器或网络共享驱动器的大写字母。 |
| DriveType | 返回指定驱动器的类型。 |
| FileSystem | 返回指定驱动器所使用的文件系统。 |
| FreeSpace | 向用户返回在指定的驱动器或网络共享驱动器上的剩余空间容量。 |
| IsReady | 如果指定驱动器已就绪，则返回 true。否则返回 false。 |
| Path | 返回其后有一个冒号的大写字母，用来指示指定驱动器的路径名。 |
| RootFolder | 返回一个文件夹对象，该文件夹代表指定驱动器的根文件夹。 |
| SerialNumber | 返回指定驱动器的序列号。 |
| ShareName | 返回指定驱动器的网络共享名。 |
| TotalSize | 返回指定的驱动器或网络共享驱动器的总容量。 |
| VolumeName | 设置或者返回指定驱动器的卷标名。 |

**







	  AI 思考中...





			** [ASP TextStream 对象](https://www.runoob.com/asp-ref-textstream.html)
			[ASP File 对象](https://www.runoob.com/asp-ref-file.html) **













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