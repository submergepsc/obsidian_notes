# R 字符串

- Source: https://www.runoob.com/r/r-string.html

R 语言中，字符串是一种表示文本数据的数据类型，它由字符（字符向量）组成，可以包含字母、数字、符号和空格等字符。


R 语言字符串可以使用一对单引号 **' '** 或一对双引号 **" "** 来表示。


- 单引号字符串中可以包含双引号。
- 单引号字符串中不可以包含单引号。
- 双引号字符串中可以包含单引号。
- 双引号字符串中不可以包含双引号。


** 创建字符串：**您可以使用单引号或双引号来创建字符串。

以下实例演示来字符串的使用：


## 实例


```r
a <- '使用单引号'
print(a)

b <- "使用双引号"
print(b)

c <- "双引号字符串中可以包含单引号（'） "
print(c)

d <- '单引号字符串中可以包含双引号（"） '
print(d)
```


执行以上代码输出结果为：


```
[1] "使用单引号"
[1] "使用双引号"
[1] "双引号字符串中可以包含单引号（'） "
[1] "单引号字符串中可以包含双引号（\"） "
```


---


## 字符串操作


R 语言提供了多种操作字符串的函数和操作符，使得处理和操作文本数据变得方便。


以下我们来看下 R 语言一些内置函数对字符串对操作。


### paste() 函数


paste() 函数用于使用指定对分隔符来对字符串进行连接，默认的分隔符为空格。


语法格式：


```
paste(..., sep = " ", collapse = NULL)
```


参数说明：


- ... ： 字符串列表
- sep ： 分隔符，默认为空格
- collapse ： 两个或者更多字符串对象根据元素对应关系拼接到一起，在字符串进行连接后，再使用 collapse 指定对连接符进行连接


## 实例


```r
a <- "Google"
b <- 'Runoob'
c <- "Taobao"

print(paste(a,b,c))

print(paste(a,b,c, sep = "-"))

print(paste(letters[1:6],1:6, sep = "", collapse = "="))
paste(letters[1:6],1:6, collapse = ".")
```


执行以上代码输出结果为：


```
[1] "Google Runoob Taobao"
[1] "Google-Runoob-Taobao"
[1] "a1=b2=c3=d4=e5=f6"
[1] "a 1.b 2.c 3.d 4.e 5.f 6"
```


### format() 函数


format() 函数用于格式化字符串，format() 可作用于字符串或数字。


语法格式：


```
format(x, digits, nsmall, scientific, width, justify = c("left", "right", "centre", "none"))
```


参数说明：


- x ： 输入对向量
- digits ： 显示的位数
- nsmall ： 小数点右边显示的最少位数
- scientific ： 设置科学计数法
- width ： 通过开头填充空白来显示最小的宽度
- justify：设置位置，显示可以是左边、右边、中间等。


## 实例


```r
# 显示 9 位，最后一位四舍五入
result <- format(23.123456789, digits = 9)
print(result)

# 使用科学计数法显示
result <- format(c(6, 13.14521), scientific = TRUE)
print(result)

# 小数点右边最小显示 5 位，没有的以 0 补充
result <- format(23.47, nsmall = 5)
print(result)

# 将数字转为字符串
result <- format(6)
print(result)

# 宽度为 6 位，不够的在开头添加空格
result <- format(13.7, width = 6)
print(result)

# 左对齐字符串
result <- format("Runoob", width = 9, justify = "l")
print(result)

# 居中显示
result <- format("Runoob", width = 10, justify = "c")
print(result)
```


执行以上代码输出结果为：


```
[1] "23.1234568"
[1] "6.000000e+00" "1.314521e+01"
[1] "23.47000"
[1] "6"
[1] "  13.7"
[1] "Runoob   "
[1] "  Runoob  "
```


### nchar() 函数


nchar() 函数用于计数字符串或数字列表的长度。


语法格式：


```
nchar(x)
```


参数说明：


- x ： 向量或字符串


## 实例


```r
result <- nchar("Google Runoob Taobao")
print(result)
```


执行以上代码输出结果为：


```
[1] 20
```


### toupper() & tolower() 函数


toupper() & tolower() 函数用于将字符串的字母转化为大写或者小写。


语法格式：


```
toupper(x)
tolower(x)
```


参数说明：


- x ： 向量或字符串


# 转大写

## 实例


```r
result <- toupper("Runoob")
print(result)

# 转小写
result <- tolower("Runoob")
print(result)
```


执行以上代码输出结果为：


```
[1] "RUNOOB"
[1] "runoob"
```


### substring() 函数


substring() 函数用于截取字符串。


语法格式：


```
substring(x,first,last)
```


参数说明：


- x ： 向量或字符串
- first ： 开始截取的位置
- last： 结束截取的位置


## 实例


```r
# 从第 2 位截取到第 5 位
result <- substring("Runoob", 2, 5)
print(result)
```


执行以上代码输出结果为：


```
[1] "unoo"
```


### 字符串替换

使用 **gsub()** 函数来替换字符串中的特定字符或模式。


## 实例


```r
str <- "Hello, World!"
new_str <- gsub("World", "R", str)
# 输出： "Hello, R!"
```


### 字符串拆分

使用 **strsplit()** 函数将字符串拆分为子字符串。


## 实例


```r
str <- "Hello, World!"
split_str <- strsplit(str, ",")
# 输出： List of 1
#         [[1]]
#         [1] "Hello"   " World!"
```


以上只列举了一小部分的 R 语言字符串操作实例，R 有大量的字符串处理函数和操作符，例如模式匹配、大小写转换、字符串比较等，您可以查阅 R 语言的官方文档获得更多字符串操作函数列表和使用说明。








	  AI 思考中...





			** [R 函数](https://www.runoob.com/r-functions.html)
			[R 向量](https://www.runoob.com/r-vector.html) **













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