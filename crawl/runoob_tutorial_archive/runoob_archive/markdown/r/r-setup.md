# R 环境安装

- Source: https://www.runoob.com/r/r-setup.html

R 语言的开发环境本身具备了图形开发环境，这与其他很多工程语言是不同的，所以开发环境最好安装在为桌面个人计算机设计的操作系统上（如 Windows, macOS 或 Ubuntu 桌面版 等）。


首先，我们需要下载 R 语言环境的安装包：


### Windows


- 官方地址：[https://cloud.r-project.org/bin/windows/base/](https://cloud.r-project.org/bin/windows/base/)
- USTC 镜像：[https://mirrors.ustc.edu.cn/CRAN/bin/windows/base/](https://mirrors.ustc.edu.cn/CRAN/bin/windows/base/)
- TUNA 镜像：[https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/windows/base/](https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/windows/base/)


### Linux


- 官方地址：[https://cloud.r-project.org/bin/linux/](https://cloud.r-project.org/bin/linux/)
- USTC 镜像：[https://mirrors.ustc.edu.cn/CRAN/bin/linux/](https://mirrors.ustc.edu.cn/CRAN/bin/linux/)
- TUNA 镜像：[https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/linux/](https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/linux/)


### macOS


- 官方地址：[https://cloud.r-project.org/bin/macosx/](https://cloud.r-project.org/bin/macosx/)
- USTC 镜像：[https://mirrors.ustc.edu.cn/CRAN/bin/macosx/](https://mirrors.ustc.edu.cn/CRAN/bin/macosx/)
- TUNA 镜像：[https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/macosx/](https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/macosx/)


以上的版本有可能是过时的，如果你需要最新版本，可以访问：

- 清华大学源： [https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/](https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/)
- 官网：[https://cloud.r-project.org/bin/](https://cloud.r-project.org/bin/)


---


## Windows 操作系统


Windows 安装很简单，下载安装包后，双击下载的安装包，开始安装向导：


![](https://www.runoob.com/wp-content/uploads/2020/07/r-setup-1.png)


![](https://www.runoob.com/wp-content/uploads/2020/07/r-setup-2.png)


![](https://www.runoob.com/wp-content/uploads/2020/07/r-setup-3.png)


**注意：**这里使用的操作系统是 64 位的，但现在仍有少数的计算机使用的是 32 位的操作系统，如果你的操作系统是 32 位的，请在此步骤选择"32-bit 用户安装"选项。


![](https://www.runoob.com/wp-content/uploads/2020/07/r-setup-4.png)


![](https://www.runoob.com/wp-content/uploads/2020/07/r-setup-5.png)


当我们在交互式的命令窗口输入以下代码：


```
print("Hello, world")
```


输出结果为：


```
"Hello, world"
```


**

## Linux


### Ubuntu 安装


执行以下命令安装 R 语言执行环境：


```
# sudo apt update
# sudo apt -y upgrade
# sudo apt -y install r-base
```


安装成功后，执行 **R** 命令就可以进入交互式的编程窗口了：


![](https://www.runoob.com/wp-content/uploads/2020/07/AA1FF155-B2EB-48F9-8660-DB32706A134B.jpg)


### Centos 安装


```
# sudo yum install R
```


输入以下命令，查看安装的版本：


```
# R --version
```


交互式命令可以通过输入 q() 来退出：


```
> q()
Save workspace image? [y/n/c]: y
```


## macOS 安装

macOS 安装 R 语言环境类似 Windows，下载 pkg 安装包，双击安装包打开，然后按安装向导安装：


![](https://www.runoob.com/wp-content/uploads/2020/07/R-setup-macos-1.jpg)


![](https://www.runoob.com/wp-content/uploads/2020/07/R-setup-macos-2.jpg)


![](https://www.runoob.com/wp-content/uploads/2020/07/R-setup-macos-3.jpg)


![](https://www.runoob.com/wp-content/uploads/2020/07/R-setup-macos-4.jpg)


安装成功后，执行 **R** 命令就可以进入交互式的编程窗口了：


![](https://www.runoob.com/wp-content/uploads/2020/07/AA89F11A-9180-4BD0-8A6A-4BE2FD5F1E8E.jpg)


交互式命令可以通过输入 q() 来退出：


```
> q()
Save workspace image? [y/n/c]: y
```


![](https://www.runoob.com/wp-content/uploads/2020/07/DDF9B88F-3BBC-4679-9D93-565E4D0ABBAB.jpg)


### 脚本执行


在 R 语言中，可以在命令行中使用 **Rscript** 命令来执行 R 脚本文件。

**Rscript** 命令允许您直接从命令行运行 R 脚本，而无需打开 R 控制台。。


要使用 **Rscript**命令 执行 R 脚本文件，可以按照以下步骤进行操作：

创建一个 R 脚本文件，其中包含要执行的R代码。例如，将以下代码保存为 script.R** 文件：


## script.R 文件代码：


```r
# script.R
x <- 1:10
y <- x^2
print(y)
```


打开终端或命令行界面，进入当前文件 **script.R** 所在目录，在命令行中使用 **Rscript** 命令来执行脚本文件：


```
Rscript script.R
```


执行以上命令后，R 脚本文件将被 Rscript 解释器读取和执行。










	  AI 思考中...





			** [R 语言教程](https://www.runoob.com/r-tutorial.html)
			[R 基础语法](https://www.runoob.com/r-basic-syntax.html) **













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