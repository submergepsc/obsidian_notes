# R XML 文件

- Source: https://www.runoob.com/r/r-input-xml-file.html

XML 指的是可扩展标记语言（eXtensible Markup Language），XML 被设计用来传输和存储数据。


如果你对 XML 还不了解，可以先查阅：[XML 教程](https://www.runoob.com/../xml/xml-tutorial.html)


R 语言读写 XML 文件需要安装扩展包，我们可以在 R 到控制台输入以下命令来安装：


```
install.packages("XML", repos = "https://mirrors.ustc.edu.cn/CRAN/")
```


查看是否安装成功：


```
> any(grepl("XML",installed.packages()))
[1] TRUE
```


创建 sites.xml 文件，xml 文件与测试脚本同一目录下，代码如下：


## 实例


```r
<sites>
    <site>
        <id>1</id>
        <name>Google</name>
        <url>www.google.com</url>
        <likes>111</likes>
    </site>

    <site>
        <id>2</id>
        <name>Runoob</name>
        <url>www.runoob.com</url>
        <likes>222</likes>
    </site>

    <site>
        <id>3</id>
        <name>Taobao</name>
        <url>www.taobao.com</url>
        <likes>333</likes>
    </site>
</sites>
```


接下来我们可以使用 XML 包来载入 xml 文件的数据：


## 实例


```r
# 载入 XML 包
library("XML")

# 设置文件名
result <- xmlParse(file = "sites.xml")

# 输出结果
print(result)
```


统计 xml 数据量：


## 实例


```r
# 载入 XML 包
library("XML")

# 设置文件名
result <- xmlParse(file = "sites.xml")

# 提取根节点
rootnode <- xmlRoot(result)

# 统计数据量
rootsize <- xmlSize(rootnode)

# 输出结果
print(rootsize)
```


执行以上代码输出结果为：


```
[1] 3
```


查看节点数据，某一行使用 **[ ]**, 指定的行和列使用 **[[ ]]**:


## 实例


```r
# 载入 XML 包
library("XML")

# 设置文件名
result <- xmlParse(file = "sites.xml")

# 提取根节点
rootnode <- xmlRoot(result)

# 查看第 2 个节点数据
print(rootnode[2])

# 查看第 2 个节点的第  1 个数据
print(rootnode[[2]][[1]])

# 查看第 2 个节点的第 3 个数据

print(rootnode[[2]][[3]])
```


执行以上代码输出结果为：


```
$site
<site>
  <id>2</id>
  <name>Runoob</name>
  <url>www.runoob.com</url>
  <likes>222</likes>
</site>

attr(,"class")
[1] "XMLInternalNodeList" "XMLNodeList"
<id>2</id>
<url>www.runoob.com</url>
```


### XML 转为数据列表

以上代码对输出都是 xml 格式，我们使用 xmlToList() 函数可以将文件对数据转为列表格式，更方便读取：


## 实例


```r
# 载入 XML 包
library("XML")

# 设置文件名
result <- xmlParse(file = "sites.xml")

# 转为列表
xml_data <- xmlToList(result)

print(xml_data)
print("============================")

# 输出第一行第二列的数据
print(xml_data[[1]][[2]])
```


执行以上代码输出结果为：


```
$site
$site$id
[1] "1"

$site$name
[1] "Google"

$site$url
[1] "www.google.com"

$site$likes
[1] "111"


$site
$site$id
[1] "2"

$site$name
[1] "Runoob"

$site$url
[1] "www.runoob.com"

$site$likes
[1] "222"


$site
$site$id
[1] "3"

$site$name
[1] "Taobao"

$site$url
[1] "www.taobao.com"

$site$likes
[1] "333"


[1] "============================"
[1] "Google"
```


### XML 转为数据框

XML 文件数据可以转为数据框类型，这样我们就更方便对数据进行操作：


## 实例


```r
# 载入 XML 包
library("XML")

# xml 文件数据转为数据框
xmldataframe <- xmlToDataFrame("sites.xml")
print(xmldataframe)
```


执行以上代码输出结果为：


```
id   name            url likes
1  1 Google www.google.com   111
2  2 Runoob www.runoob.com   222
3  3 Taobao www.taobao.com   333
```










	  AI 思考中...





			** [R Excel 文件](https://www.runoob.com/r-input-excel-file.html)
			[R JSON 文件](https://www.runoob.com/r-input-json-file.html) **













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