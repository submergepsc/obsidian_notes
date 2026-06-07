# R 绘图 - 饼图

- Source: https://www.runoob.com/r/r-pie-charts.html

R 语言提供来大量的库来实现绘图功能。

饼图，或称饼状图，是一个划分为几个扇形的圆形统计图表，用于描述量、频率或百分比之间的相对关系。


R 语言使用 pie() 函数来实现饼图，语法格式如下：


```
pie(x, labels = names(x), edges = 200, radius = 0.8,
    clockwise = FALSE, init.angle = if(clockwise) 90 else 0,
    density = NULL, angle = 45, col = NULL, border = NULL,
    lty = NULL, main = NULL, …)
```


- x: 数值向量，表示每个扇形的面积。
- labels: 字符型向量，表示各扇形面积标签。
- edges: 这个参数用处不大，指的是多边形的边数（圆的轮廓类似很多边的多边形）。
- radius: 饼图的半径。
- main: 饼图的标题。
- clockwise: 是一个逻辑值,用来指示饼图各个切片是否按顺时针做出分割。
- angle: 设置底纹的斜率。
- density: 底纹的密度。默认值为 NULL。
- col: 是表示每个扇形的颜色，相当于调色板。


绘制饼状图要做这些准备：反映数量的向量、各部分的标签、各部分的颜色（可选）。


接下来我们绘制一个简单的饼图：


## 实例


```r
# 数据准备
info = c(1, 2, 4, 8)

# 命名
names = c("Google", "Runoob", "Taobao", "Weibo")

# 涂色（可选）
cols = c("#ED1C24","#22B14C","#FFC90E","#3f48CC")

# 绘图
pie(info, labels=names, col=cols)
```


执行绘图程序，会在当前目录下生存一个 PDF 文件（Rplots.pdf）,打开文件可以看到图形效果如下：


![](https://www.runoob.com/wp-content/uploads/2020/07/CE239EAD-2217-4623-A99C-6BB2DB7C72D9.jpg)


我们也可以使用 png()、jpeg()、bmp() 函数设置输出的文件格式为图片：


## 实例


```r
# 数据准备
info = c(1, 2, 4, 8)

# 命名
names = c("Google", "Runoob", "Taobao", "Weibo")

# 涂色（可选）
cols = c("#ED1C24","#22B14C","#FFC90E","#3f48CC")

# 设置输出图片
png(file='runoob-pie.png', height=300, width=300)
# 绘图
pie(info, labels=names, col=cols)
```


接下来我们给饼图设置标题，中文字体需要设置字体参数 **family='GB1'**，也可以自己设置字体库，详细参考：[R 绘图 - 中文支持](https://www.runoob.com/r-charts-cn.html)。


## 实例


```r
# 数据准备
info = c(1, 2, 4, 8)

# 命名
names = c("Google", "Runoob", "Taobao", "Weibo")

# 涂色（可选）
cols = c("#ED1C24","#22B14C","#FFC90E","#3f48CC")
# 计算百分比
piepercent = paste(round(100*info/sum(info)), "%")
# 绘图
pie(info, labels=piepercent, main = "网站分析", col=cols, family='GB1')
# 添加颜色样本标注
legend("topright", names, cex=0.8, fill=cols)
```


![](https://www.runoob.com/ https://www.runoob.com/wp-content/uploads/2020/07/065BA223-69F9-4AF5-A3D4-D92A6A895D89.jpg)


如果要绘制 3D 的饼图，可以使用 plotrix 库的 pie3D() 函数，使用前我们需要先安装：


```
install.packages("plotrix", repos = "https://mirrors.ustc.edu.cn/CRAN/")
```


## 实例


```r
# 载入 plotrix
library(plotrix)
# 数据准备
info = c(1, 2, 4, 8)

# 命名
names = c("Google", "Runoob", "Taobao", "Weibo")

# 涂色（可选）
cols = c("#ED1C24","#22B14C","#FFC90E","#3f48CC")

# 设置文件名，输出为 png
png(file = "3d_pie_chart.png")

# 绘制 3D 图，family 要设置你系统支持的中文字体库
pie3D(info,labels = names,explode = 0.1, main = "3D 图",family = "STHeitiTC-Light")
```


生成图片如下所示：


![](https://www.runoob.com/wp-content/uploads/2020/07/3d_pie_chart.png)









	  AI 思考中...





			** [R MySQL 连接](https://www.runoob.com/r-mysql-connect.html)
			[R 绘图 – 中文支持](https://www.runoob.com/r-charts-cn.html) **













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