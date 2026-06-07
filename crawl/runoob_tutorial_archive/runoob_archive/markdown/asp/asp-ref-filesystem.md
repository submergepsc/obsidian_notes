# ASP FileSystemObject 对象

- Source: https://www.runoob.com/asp/asp-ref-filesystem.html

---


FileSystemObject 对象用于访问服务器上的文件系统。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[指定的文件存在吗？](https://www.runoob.com/try/showasp.php?filename=demo_fileexists)** 本例演示如何检查某个文件是否存在。


[指定的文件夹存在吗？](https://www.runoob.com/try/showasp.php?filename=demo_folderexists) 本例演示如何检查某个文件夹是否存在。


[指定的驱动器存在吗？](https://www.runoob.com/try/showasp.php?filename=demo_driveexists) 本例演示如何检查某个驱动器是否存在。


[取得某个指定驱动器的名称](https://www.runoob.com/try/showasp.php?filename=demo_getdrivename) 本例演示如何获取某个指定的驱动器的名称。


[取得某个指定路径的父文件夹的名称](https://www.runoob.com/try/showasp.php?filename=demo_getparentfoldername) 本例演示如何获取某个指定的路径的父文件夹的名称。


[取得文件名](https://www.runoob.com/try/showasp.php?filename=demo_getfilename) 本例演示如何获取指定的路径中的最后一个成分的文件名。


[取得文件扩展名](https://www.runoob.com/try/showasp.php?filename=demo_getextensionname) 本例演示如何获取指定的路径中的最后一个成分的文件扩展名。


[取得文件或文件夹的基名称](https://www.runoob.com/try/showasp.php?filename=demo_getbasename) 本例演示如何获取指定的路径中文件或者文件夹的基名称。


---


## FileSystemObject 对象


FileSystemObject 对象用于访问服务器上的文件系统。


此对象可对文件、文件夹和目录路径进行操作。也可通过此对象获取文件系统的信息。


下面的代码会创建一个文本文件 (c:\test.txt)，然后向这个文件写一些文本：


<%

dim fs,fname

set fs=Server.CreateObject("Scripting.FileSystemObject")

set fname=fs.CreateTextFile("c:\test.txt",true)

fname.WriteLine("Hello World!")

fname.Close

set fname=nothing

set fs=nothing

%>


FileSystemObject 对象的属性和方法描述如下：


### 属性


| 属性 | 描述 |
| --- | --- |
| Drives | 返回本地计算机上所有驱动器对象的集合。 |


### 方法


| 方法 | 描述 |
| --- | --- |
| BuildPath | 将一个名称追加到已有的路径后。 |
| CopyFile | 从一个位置向另一个位置拷贝一个或多个文件。 |
| CopyFolder | 从一个位置向另一个位置拷贝一个或多个文件夹。 |
| CreateFolder | 创建新文件夹。 |
| CreateTextFile | 创建文本文件，并返回一个可以读取或者写入文件的 TextStream 对象。 |
| DeleteFile | 删除一个或者多个指定的文件。 |
| DeleteFolder | 删除一个或者多个指定的文件夹。 |
| DriveExists | 检查指定的驱动器是否存在。 |
| FileExists | 检查指定的文件是否存在。 |
| FolderExists | 检查指定的文件夹是否存在。 |
| GetAbsolutePathName | 针对指定的路径返回从驱动器根部起始的完整路径。 |
| GetBaseName | 返回指定文件或者文件夹的基名称。 |
| GetDrive | 返回指定路径中所对应的驱动器的 Drive 对象。 |
| GetDriveName | 返回指定的路径的驱动器名称。 |
| GetExtensionName | 返回在指定的路径中最后一个成分的文件扩展名。 |
| GetFile | 返回一个针对指定路径的 File 对象。 |
| GetFileName | 返回在指定的路径中最后一个成分的文件名或者文件夹名。 |
| GetFolder | 返回一个针对指定路径的 Folder 对象。 |
| GetParentFolderName | 返回在指定的路径中最后一个成分的父文件夹名称。 |
| GetSpecialFolder | 返回某些 Windows 的特殊文件夹的路径。 |
| GetTempName | 返回一个随机生成的文件或文件夹。 |
| MoveFile | 从一个位置向另一个位置移动一个或多个文件。 |
| MoveFolder | 从一个位置向另一个位置移动一个或多个文件夹。 |
| OpenTextFile | 打开文件，并返回一个用于访问此文件的 TextStream 对象。 |










	  AI 思考中...





			** [ASP ASPError 对象](https://www.runoob.com/asp-ref-error.html)
			[ASP TextStream 对象](https://www.runoob.com/asp-ref-textstream.html) **













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