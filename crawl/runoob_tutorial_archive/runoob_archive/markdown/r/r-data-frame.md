# R 数据框

- Source: https://www.runoob.com/r/r-data-frame.html

数据框（Data frame）可以理解成我们常说的"表格"。


数据框是 R 语言的数据结构，是特殊的二维列表。


数据框每一列都有一个唯一的列名，长度都是相等的，同一列的数据类型需要一致，不同列的数据类型可以不一样。


![](https://static.jyshare.com/images/mix/data-frame.svg)


R 语言数据框使用 data.frame() 函数来创建，语法格式如下：


```
data.frame(…, row.names = NULL, check.rows = FALSE,
           check.names = TRUE, fix.empty.names = TRUE,
           stringsAsFactors = default.stringsAsFactors())
```


- **…**: 列向量，可以是任何类型（字符型、数值型、逻辑型），一般以 tag = value 的形式表示，也可以是 value。
- **row.names**: 行名，默认为 NULL，可以设置为单个数字、字符串或字符串和数字的向量。
- **check.rows**: 检测行的名称和长度是否一致。
- **check.names**: 检测数据框的变量名是否合法。
- **fix.empty.names**: 设置未命名的参数是否自动设置名字。
- **stringsAsFactors**: 布尔值，字符是否转换为因子，factory-fresh 的默认值是 TRUE，可以通过设置选项（stringsAsFactors=FALSE）来修改。


以下创建一个简单的数据框，包含姓名、工号、月薪：


## 实例


```r
table = data.frame(
    姓名 = c("张三", "李四"),
    工号 = c("001","002"),
    月薪 = c(1000, 2000)

)
print(table) # 查看 table 数据
```


执行以上代码输出结果为：


```
姓名 工号 月薪
1 张三  001 1000
2 李四  002 2000
```


数据框的数据结构可以通过 **str()** 函数来展示：


## 实例


```r
table = data.frame(
    姓名 = c("张三", "李四"),
    工号 = c("001","002"),
    月薪 = c(1000, 2000)
)
# 获取数据结构
str(table)
```


执行以上代码输出结果为：


```
'data.frame':   2 obs. of  3 variables:
 $ 姓名: chr  "张三" "李四"
 $ 工号: chr  "001" "002"
 $ 月薪: num  1000 2000
```


**summary()** 可以显示数据框的概要信息：


## 实例


```r
table = data.frame(
    姓名 = c("张三", "李四"),
    工号 = c("001","002"),
    月薪 = c(1000, 2000)

)
# 显示概要
print(summary(table))
```


执行以上代码输出结果为：


```
姓名               工号                月薪
Length:2           Length:2           Min.   :1000
Class :character   Class :character   1st Qu.:1250
Mode  :character   Mode  :character   Median :1500
                                      Mean   :1500
                                      3rd Qu.:1750
                                      Max.   :2000
```


我们也可以提取指定的列：


## 实例


```r
table = data.frame(
    姓名 = c("张三", "李四"),
    工号 = c("001","002"),
    月薪 = c(1000, 2000)
)
# 提取指定的列
result <- data.frame(table$姓名,table$月薪)
print(result)
```


执行以上代码输出结果为：


```
table.姓名 table.月薪
1       张三       1000
2       李四       2000
```


以下形式显示前面两行：


## 实例


```r
table = data.frame(
    姓名 = c("张三", "李四","王五"),
    工号 = c("001","002","003"),
    月薪 = c(1000, 2000,3000)
)
print(table)
# 提取前面两行
print("---输出前面两行----")
result <- table[1:2,]
print(result)
```


执行以上代码输出结果为：


```
姓名 工号 月薪
1 张三  001 1000
2 李四  002 2000
3 王五  003 3000
[1] "---输出前面两行----"
  姓名 工号 月薪
1 张三  001 1000
2 李四  002 2000
```


我们可以通过类似坐标的形式读取指定行的某一列的数据，以下我们读取第 2 、3 行的第 1 、2 列数据：：


## 实例


```r
table = data.frame(
    姓名 = c("张三", "李四","王五"),
    工号 = c("001","002","003"),
    月薪 = c(1000, 2000,3000)
)
# 读取第 2 、3 行的第 1 、2 列数据：
result <- table[c(2,3),c(1,2)]
print(result)
```


执行以上代码输出结果为：


```
姓名 工号
2 李四  002
3 王五  003
```


### 扩展数据框


我们可以对已有的数据框进行扩展，以下实例我们添加部门列：


## 实例


```r
table = data.frame(
    姓名 = c("张三", "李四","王五"),
    工号 = c("001","002","003"),
    月薪 = c(1000, 2000,3000)
)
# 添加部门列
table$部门 <- c("运营","技术","编辑")

print(table)
```


执行以上代码输出结果为：


```
姓名 工号 月薪 部门
1 张三  001 1000 运营
2 李四  002 2000 技术
3 王五  003 3000 编辑
```


我们可以使用 **cbind()** 函数将多个向量合成一个数据框：



## 实例


```r
# 创建向量
sites <- c("Google","Runoob","Taobao")
likes <- c(222,111,123)
url <- c("www.google.com","www.runoob.com","www.taobao.com")

# 将向量组合成数据框
addresses <- cbind(sites,likes,url)

# 查看数据框
print(addresses)
```


执行以上代码输出结果为：


```
sites    likes url
[1,] "Google" "222" "www.google.com"
[2,] "Runoob" "111" "www.runoob.com"
[3,] "Taobao" "123" "www.taobao.com"
```


如果要对两个数据框进行合并可以使用 **rbind()** 函数：


## 实例


```r
table = data.frame(
    姓名 = c("张三", "李四","王五"),
    工号 = c("001","002","003"),
    月薪 = c(1000, 2000,3000)
)
newtable = data.frame(
    姓名 = c("小明", "小白"),
    工号 = c("101","102"),
    月薪 = c(5000, 7000)
)
# 合并两个数据框
result <- rbind(table,newtable)
print(result)
```


执行以上代码输出结果为：


```
姓名 工号 月薪
1 张三  001 1000
2 李四  002 2000
3 王五  003 3000
4 小明  101 5000
5 小白  102 7000
```










	  AI 思考中...





			** [R 因子](https://www.runoob.com/r-factor.html)
			[R 包](https://www.runoob.com/r-package.html) **













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