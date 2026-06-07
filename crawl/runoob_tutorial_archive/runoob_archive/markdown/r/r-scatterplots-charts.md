# R 绘图 - 散点图

- Source: https://www.runoob.com/r/r-scatterplots-charts.html

散点图是将所有的数据以点的形式展现在直角坐标系上，以显示变量之间的相互影响程度，点的位置由变量的数值决定，每个点对应一个 X 和 Y 轴点坐标。

散点图可以使用 plot() 函数来绘制，语法格式如下：


```
plot(x, y, type="p", main, xlab, ylab, xlim, ylim, axes)
```


- **x** 横坐标 x 轴的数据集合
- **y** 纵坐标 y 轴的数据集合
- type：绘图的类型，p 为点、l 为直线， o 同时绘制点和线，且线穿过点。
- **main** 图表标题。
- **xlab、ylab** x 轴和 y 轴的标签名称。
- **xlim、ylim** x 轴和 y 轴的范围。
- **axes** 布尔值，是否绘制两个 x 轴。


type 参数可选择值：


- p：点图
- l：线图
- b：同时绘制点和线
- c：仅绘制参数 b 所示的线
- o：同时绘制点和线，且线穿过点
- h：绘制出点到横坐标轴的垂直线
- s：阶梯图，先横后纵
- S：阶梯图，先纵后竖

创建一个简单的线图：


## 实例


```r
x<-c(10,40)
y<-c(20,60)
# 生成 png 图片
png(file = "runnob-test-plot2.png")

plot(x, y, "l")
```


![](https://www.runoob.com/wp-content/uploads/2020/07/runnob-test-plot2.png)


创建一个简单的线图，type 使用 o 参数，同时绘制点和线，且线穿过点：


## 实例


```r
x<-c(10,40)
y<-c(20,60)
# 生成 png 图片
png(file = "runnob-test-plot.png")

plot(x, y, "o")
```


接下来我们使用 R 语言的内置数据集 mtcars 来进行测试。

![](https://www.runoob.com/wp-content/uploads/2020/07/runnob-test-plot.png)


我们使用 mtcars 数据集的 wt 和 mpg 列：


## 实例


```r
input <- mtcars[,c('wt','mpg')]
print(head(input))
```


输出结果为：


```
wt  mpg
Mazda RX4         2.620 21.0
Mazda RX4 Wag     2.875 21.0
Datsun 710        2.320 22.8
Hornet 4 Drive    3.215 21.4
Hornet Sportabout 3.440 18.7
Valiant           3.460 18.1
```


接着我们使用以上数据生存一个散点图
：

## 实例


```r
# 数据
input <- mtcars[,c('wt','mpg')]

# 生成 png 图片
png(file = "scatterplot.png")

# 设置坐标 x 轴范围 2.5 到 5, y 轴范围 15 到 30.
plot(x = input$wt,y = input$mpg,
   xlab = "Weight",
   ylab = "Milage",
   xlim = c(2.5,5),
   ylim = c(15,30),
   main = "Weight vs Milage"
)
```


![](https://www.runoob.com/wp-content/uploads/2020/07/scatterplot.png)


### 散点图矩阵

散点图矩阵是借助两变量散点图的作图方法，它可以看作是一个大的图形方阵，其每一个非主对角元素的位置上是对应行的变量与对应列的变量的散点图。而主对角元素位置上是各变量名，这样，借助散点图矩阵可以清晰地看到所研究多个变量两两之间的相关关系。

散点图矩阵就是把数据集中的每个数值变量两两绘制散点图。


R 语言使用以下函数创建散点图矩阵：


```
pairs(formula, data)
```


参数：


- **formula** 变量系列
- **data** 变量的数据集


## 实例


```r
# 输出图片
png(file = "scatterplot_matrices.png")

# 4 个变量绘制矩阵，12 个图

pairs(~wt+mpg+disp+cyl,data = mtcars, main = "Scatterplot Matrix")
```


![](https://www.runoob.com/wp-content/uploads/2020/07/scatterplot_matrices.png)








	  AI 思考中...





			** [R 绘图 – 函数曲线图](https://www.runoob.com/r-line_charts.html)
			[Java 中操作 R](https://www.runoob.com/r-java.html) **













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