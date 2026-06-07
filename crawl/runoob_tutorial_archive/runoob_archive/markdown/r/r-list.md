# R 列表

- Source: https://www.runoob.com/r/r-list.html

列表是 R 语言的对象集合，可以用来保存不同类型的数据，可以是数字、字符串、向量、另一个列表、矩阵、数据框等，当然还可以包含矩阵和函数。


列表是一种灵活的数据结构，可以存储和操作多种类型的数据对象。


### 创建列表


R 语言创建列表使用 **list()** 函数。

如下实例，我们创建一个列表，包含了字符串、向量和数字：


## 实例


```r
list_data <- list("runoob", "google", c(11,22,33), 123, 51.23, 119.1)
print(list_data)
```


执行以上代码输出结果为：


```
[[1]]
[1] "runoob"

[[2]]
[1] "google"

[[3]]
[1] 11 22 33

[[4]]
[1] 123

[[5]]
[1] 51.23

[[6]]
[1] 119.1
```


我们也可以使用 **c()** 函数来创建列表，也可以使用该函数将多个对象合并为一个列表，例如：


```
my_list <- c(object1, object2, object3)
```


## 实例


```r
# 创建包含数字的向量
numbers <- c(1, 2, 3, 4, 5)

# 创建包含字符的向量
characters <- c("apple", "banana", "orange")

# 合并两个数字向量
merged_vector <- c(numbers, c(6, 7, 8))

# 合并两个字符向量
merged_characters <- c(characters, c("grape", "melon"))
```


我们可以使用 **names()** 函数给列表的元素命名：


## 实例


```r
# 列表包含向量、矩阵、列表
list_data <- list(c("Google","Runoob","Taobao"), matrix(c(1,2,3,4,5,6), nrow = 2),
   list("runoob",12.3))

# 给列表元素设置名字
names(list_data) <- c("Sites", "Numbers", "Lists")

# 显示列表
print(list_data)
```


执行以上代码输出结果为：


```
$Sites
[1] "Google" "Runoob" "Taobao"

$Numbers
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6

$Lists
$Lists[[1]]
[1] "runoob"

$Lists[[2]]
[1] 12.3
```


### 访问列表

列表中的元素可以使用索引来访问，如果使用来 **names()** 函数命名后，我们还可以使用对应名字来访问：


## 实例


```r
# 列表包含向量、矩阵、列表
list_data <- list(c("Google","Runoob","Taobao"), matrix(c(1,2,3,4,5,6), nrow = 2),
   list("runoob",12.3))

# 给列表元素设置名字
names(list_data) <- c("Sites", "Numbers", "Lists")

# 显示列表
print(list_data[1])

# 访问列表的第三个元素
print(list_data[3])

# 访问第一个向量元素
print(list_data$Numbers)
```


执行以上代码输出结果为：


```
$Sites
[1] "Google" "Runoob" "Taobao"

$Lists
$Lists[[1]]
[1] "runoob"

$Lists[[2]]
[1] 12.3


     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6
```


### 操作列表元素

我们可以对列表进行添加、删除、更新的操作，如下实例：


## 实例


```r
# 列表包含向量、矩阵、列表
list_data <- list(c("Google","Runoob","Taobao"), matrix(c(1,2,3,4,5,6), nrow = 2),
   list("runoob",12.3))

# 给列表元素设置名字
names(list_data) <- c("Sites", "Numbers", "Lists")

# 添加元素
list_data[4] <- "新元素"
print(list_data[4])

# 删除元素
list_data[4] <- NULL

# 删除后输出为 NULL
print(list_data[4])

# 更新元素
list_data[3] <- "我替换来第三个元素"
print(list_data[3])
```


执行以上代码输出结果为：


```
[[1]]
[1] "新元素"

$<NA>
NULL

$Lists
[1] "我替换来第三个元素"
```


使用 **for** 循环遍历列表时：


## 实例


```r
# 创建一个包含数字和字符的列表
my_list <- list(1, 2, 3, "a", "b", "c")

# 使用 for 循环遍历列表中的每个元素
for (element in my_list) {
  print(element)
}
```


在以上代码中，for 循环会依次遍历列表 my_list 中的每个元素，并将每个元素存储在变量 element 中。然后，我们可以在循环体内对每个元素执行特定的操作，例如使用 print() 函数打印元素的值。


for 循环遍历列表时，每次循环都将当前元素赋值给变量 element。因此，在循环体内可以对 element 进行任何需要的操作，例如计算、条件判断等。


需要注意的是，使用 for 循环遍历列表时，循环变量 element 将依次取到列表中的每个元素，但不能直接修改列表元素本身。如果需要修改列表中的元素值，可以通过索引来实现，例如 **my_list[[index]]







	  AI 思考中...





			** [R 向量](https://www.runoob.com/r-vector.html)
			[R 矩阵](https://www.runoob.com/r-matrix.html) **













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