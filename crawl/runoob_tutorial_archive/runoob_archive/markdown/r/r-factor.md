# R 因子

- Source: https://www.runoob.com/r/r-factor.html

因子用于存储不同类别的数据类型，例如人的性别有男和女两个类别，年龄来分可以有未成年人和成年人。


R 语言创建因子使用 factor() 函数，向量作为输入参数。


factor() 函数语法格式：


```
factor(x = character(), levels, labels = levels,
       exclude = NA, ordered = is.ordered(x), nmax = NA)
```


参数说明：


- x：向量。
- levels：指定各水平值, 不指定时由x的不同值来求得。
- labels：水平的标签, 不指定时用各水平值的对应字符串。
- exclude：排除的字符。
- ordered：逻辑值，用于指定水平是否有序。
- nmax：水平的上限数量。


以下实例把字符型向量转换成因子：


## 实例


```r
x <- c("男", "女", "男", "男",  "女")
sex <- factor(x)
print(sex)
print(is.factor(sex))
```


执行以上代码输出结果为：


```
[1] 男 女 男 男 女
Levels: 男 女
[1] TRUE
```


以下实例设置因子水平为 **c('男','女')**：


## 实例


```r
x <- c("男", "女", "男", "男",  "女",levels=c('男','女'))
sex <- factor(x)
print(sex)
print(is.factor(sex))
```


执行以上代码输出结果为：


```
levels1 levels2
男      女      男      男      女      男      女
Levels: 男 女
[1] TRUE
```


### 因子水平标签


接下来我们使用 labels 参数为每个因子水平添加标签，labels 参数的字符顺序，要和 levels 参数的字符顺序保持一致，例如：


## 实例


```r
sex=factor(c('f','m','f','f','m'),levels=c('f','m'),labels=c('female','male'),ordered=TRUE)
print(sex)
```


执行以上代码输出结果为：


```
[1] female male   female female male
Levels: female < male
```


### 生成因子水平

我们可以使用 **gl()** 函数来生成因子水平，语法格式如下：


```
gl(n, k, length = n*k, labels = seq_len(n), ordered = FALSE)
```


参数说明：


- **n**: 设置 level 的个数
- **k**: 设置每个 level 重复的次数
- **length**: 设置长度
- **labels**: 设置 level 的值
- **ordered**: 设置是否 level 是排列好顺序的，布尔值。


## 实例


```r
v <- gl(3, 4, labels = c("Google", "Runoob","Taobao"))
print(v)
```


执行以上代码输出结果为：


```
[1] Google Google Google Google Runoob Runoob Runoob Runoob Taobao Taobao
[11] Taobao Taobao
Levels: Google Runoob Taobao
```









	  AI 思考中...





			** [R 数组](https://www.runoob.com/r-array.html)
			[R 数据框](https://www.runoob.com/r-data-frame.html) **













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