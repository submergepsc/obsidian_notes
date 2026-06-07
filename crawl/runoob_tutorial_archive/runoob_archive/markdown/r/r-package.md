# R 包

- Source: https://www.runoob.com/r/r-package.html

包是 R 函数、实例数据、预编译代码的集合，包括 R 程序，注释文档、实例、测试数据等。

R 语言相关的包一般存储安装目录下对 "library" 目录，默认情况在 R 语言安装完成已经自带来一些常用对包，当然我们也可以在后期自定义添加一些要使用的包。

R 语言完整的相关包可以查阅：[https://cran.r-project.org/web/packages/available_packages_by_name.html](https://cran.r-project.org/web/packages/available_packages_by_name.html)


接下来我们主要介绍如何安装 R 语言的包。


### 查看 R 包的安装目录


我们可以使用以下函数来查看 R 包的安装目录：


## 实例


```r
> .libPaths()
[1] "/Library/Frameworks/R.framework/Versions/4.0/Resources/library"
>
```


### 查看已安装的包


我们可以使用以下函数来查看已安装的包：


```
library()
```


输出结果如下：


```
base                    The R Base Package
boot                    Bootstrap Functions (Originally by Angelo Canty
                        for S)
class                   Functions for Classification
cluster                 "Finding Groups in Data": Cluster Analysis
                        Extended Rousseeuw et al.
codetools               Code Analysis Tools for R
compiler                The R Compiler Package
datasets                The R Datasets Package
foreign                 Read Data Stored by 'Minitab', 'S', 'SAS',
                        'SPSS', 'Stata', 'Systat', 'Weka', 'dBase', ...
graphics                The R Graphics Package
grDevices               The R Graphics Devices and Support for Colours
                        and Fonts
grid                    The Grid Graphics Package
KernSmooth              Functions for Kernel Smoothing Supporting Wand
                        & Jones (1995)
lattice                 Trellis Graphics for R
MASS                    Support Functions and Datasets for Venables and
                        Ripley's MASS
```


### 查看已载入的包


我们可以使用以下函数来查看编译环境已载入的包：


## 实例


```r
> search()
[1] ".GlobalEnv"        "package:stats"     "package:graphics"
[4] "package:grDevices" "package:utils"     "package:datasets"
[7] "package:methods"   "Autoloads"         "package:base"
```


---


## 安装新包


安装新包可以使用 **install.packages()** 函数，格式如下：


```
install.packages("要安装的包名")
```


我们可以直接设置包名，从 [CRAN](https://cran.r-project.org/web/packages/available_packages_by_name.html) 网站上获取包，如下实例我们载入 XML 包：


```
# 安装 XML 包
install.packages("XML")
```


或者我们可以直接在 [CRAN](https://cran.r-project.org/web/packages/available_packages_by_name.html) 上下载相关包，直接在本地安装：


```
install.packages("./XML_3.98-1.3.zip")
```


我们国内一般建议大家使用国内镜像，以下实例使用中国科学技术大学源进行安装：


```
# 安装 XML 包
install.packages("XML", repos = "https://mirrors.ustc.edu.cn/CRAN/")
```


CRAN (The Comprehensive R Archive Network) 镜像源配置文件之一是 .Rprofile (linux 下位于 ~/.Rprofile )。


在文末添加如下语句:


```
options("repos" = c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
```


打开 R 即可使用该 CRAN 镜像源安装 R 软件包。


### 使用包


新安装的包需要先载入 R 编译环境中才可以使用，格式如下：


```
library("包名")
```


以下实例载入 XML 包：


```
library("XML")
```









	  AI 思考中...





			** [R 数据框](https://www.runoob.com/r-data-frame.html)
			[R CSV 文件](https://www.runoob.com/r-input-csv-file.html) **













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