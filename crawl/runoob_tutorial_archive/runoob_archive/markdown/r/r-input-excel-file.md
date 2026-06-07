# R Excel 文件

- Source: https://www.runoob.com/r/r-input-excel-file.html

Excel 格式的文件主要是 xls 或 xlsx，这两种文件可以在 R 语言中导入 xlsx 库来实现直接的读取。


R 语言读写 Excel 文件需要安装扩展包，我们可以在 R 到控制台输入以下命令来安装：


```
install.packages("xlsx", repos = "https://mirrors.ustc.edu.cn/CRAN/")
```
 安装过程如下：![](https://www.runoob.com/wp-content/uploads/2020/07/4C19EC49-38CA-4C21-9A11-B15995728BCD.jpg)


事实上，几乎所有的 Excel 软件与大多数表格软件一样支持 CSV 格式的数据，所以完全可以通过 CSV 与 R 交互，没必要再使用 Excel。


查看 xlsx 是否安装成功：


## 实例


```r
# 验证包是否安装
any(grepl("xlsx",installed.packages()))
# 载入包
library("xlsx")
library("xlsx")
```


执行以上代码输出结果为：


```
[1] TRUE
Loading required package: rJava
Loading required package: methods
Loading required package: xlsxjars
```


Excel 文件数据：


![](https://www.runoob.com/wp-content/uploads/2020/07/55596D4D-4122-4605-B40E-1826D638A572.jpg)


点击链接下载 Excel 测试数据：[https://static.jyshare.com/download/sites.xlsx](https://static.jyshare.com/download/sites.xlsx)


接下来，我们可以使用 read.xlsx() 函数来读取 Excel 数据：


## 实例


```r
# 读取 sites.xlsx 第一个工作表数据
data <- read.xlsx("sites.xlsx", sheetIndex = 1)
print(data)
```









	  AI 思考中...





			** [R CSV 文件](https://www.runoob.com/r-input-csv-file.html)
			[R XML 文件](https://www.runoob.com/r-input-xml-file.html) **













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