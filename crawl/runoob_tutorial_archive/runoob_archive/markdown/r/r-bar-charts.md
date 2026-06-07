# R 绘图 - 条形图

- Source: https://www.runoob.com/r/r-bar-charts.html

条形图，也称为柱状图条形图，是一种以长方形的长度为变量的统计图表。

条形图可以是水平或垂直的，每个长方形可以有不同的颜色。

R 语言使用 barplot() 函数来创建条形图，格式如下：


```
barplot(H,xlab,ylab,main, names.arg,col,beside)
```


参数说明：


- **H** 向量或矩阵，包含图表用的数字值，每个数值表示矩形条的高度。
- **xlab** x 轴标签。
- **ylab** y 轴标签。
- **main** 图表标题。
- **names.arg** 每个矩形条的名称。
- **col** 每个矩形条的颜色。


接下来我们创建一个简单的条形图：


## 实例


```r
# 准备一个向量
cvd19 = c(83534,2640626,585493)

# 显示条形图
barplot(cvd19)
```


执行绘图程序，会在当前目录下生存一个 PDF 文件（Rplots.pdf）,打开文件可以看到图形效果如下：


![](https://www.runoob.com/wp-content/uploads/2020/07/r-bar-1.png)


为了更好地表达信息，我们可以在图表上添加标题、颜色及每个矩形条的名称。


以下我们创建 2020 年 7 月 1 日中国、美国和印度的新冠疫情确诊人数统计图。


中文字体需要设置字体参数 **family='GB1'**：


## 实例


```r
cvd19 = c(83534,2640626,585493)

barplot(cvd19,
    main="新冠疫情条形图",
    col=c("#ED1C24","#22B14C","#FFC90E"),
    names.arg=c("中国","美国","印度"),
    family='GB1'
)
```


![](https://www.runoob.com/wp-content/uploads/2020/07/r-bar-2.png)


barplot 中的数据既可以是向量，也可以是矩阵，现在我们生成一张新冠疫情 6 月和 7 月对比图。


首先准备数据：


|  | 中国 | 美国 | 印度 |
| --- | --- | --- | --- |
| 6 月 | 83017 | 1794546 | 190535 |
| 7 月 | 83534 | 2640626 | 585493 |


转换成矩阵，生成条形图，按并排格式显示，而且要显示颜色样本。


这里我们设置了自己的字体库，详细内容可以参考 [R 绘图 - 中文支持](https://www.runoob.com/r-charts-cn.html)


## 实例


```r
library(showtext);
font_add("SyHei", "SourceHanSansSC-Bold.otf");
cvd19 = matrix(
  c(83017, 83534, 1794546, 2640626, 190535, 585493),
  2, 3
)

# 设置文件名，输出为 png
png(file = "runoob-bar-1.png")

#加载字体
showtext_begin();

colnames(cvd19) = c("中国", "美国", "印度")
rownames(cvd19) = c("6月", "7月")
barplot(cvd19, main = "新冠疫情条形图", beside=TRUE, legend=TRUE,  family='SyHei')

# 去掉字体
showtext_end();
```


以下代码会在当前程序目录下生存一个 runoob-bar-1.png 文件，如下所示：


![](https://www.runoob.com/wp-content/uploads/2020/07/runoob-bar-1.png)


我们设置的颜色样本将是每各组的颜色样本：


## 实例


```r
library(plotrix)
library(showtext);
font_add("SyHei", "SourceHanSansSC-Bold.otf");
cvd19 = matrix(
  c(83017, 83534, 1794546, 2640626, 190535, 585493),
  2, 3
)

# 设置文件名，输出为 png
png(file = "runoob-bar-2.png")
#加载字体
showtext_begin();
colnames(cvd19) = c("中国", "美国", "印度")
rownames(cvd19) = c("6月", "7月")

barplot(cvd19, main = "新冠疫情条形图", beside=TRUE, legend=TRUE,col=c("blue","green"),  family='SyHei')
# 去掉字体
showtext_end();
```


以下代码会在当前程序目录下生存一个 runoob-bar-2.png 文件，如下所示：

![](https://www.runoob.com/wp-content/uploads/2020/07/runoob-bar-2.png)


### beside 参数

beside 设置矩形条堆叠的方式，默认为 FALSE：


## 实例


```r
library(showtext);
font_add("SyHei", "SourceHanSansSC-Bold.otf");
cvd19 = matrix(
  c(83017, 83534, 1794546, 2640626, 190535, 585493),
  2, 3
)

# 设置文件名，输出为 png
png(file = "runoob-bar-3.png")
#加载字体
showtext_begin();
colnames(cvd19) = c("中国", "美国", "印度")
rownames(cvd19) = c("6月", "7月")

barplot(cvd19, main = "新冠疫情条形图", beside=FALSE, legend=TRUE,col=c("blue","green"),  family='SyHei')
# 去掉字体
showtext_end();
```


以下代码会在当前程序目录下生存一个 runoob-bar-3.png 文件，如下所示：


![](https://www.runoob.com/wp-content/uploads/2020/07/runoob-bar-3.png)








	  AI 思考中...





			** [R 绘图 – 中文支持](https://www.runoob.com/r-charts-cn.html)
			[R 绘图 – 函数曲线图](https://www.runoob.com/r-line_charts.html) **













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