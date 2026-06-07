# R 绘图 - 中文支持

- Source: https://www.runoob.com/r/r-charts-cn.html

不同系统的字体库目录：


- Linux 一般在 **/usr/share/fonts** 下，我们可以使用 **fc-list** 命令查看：
```
# fc-list
/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf: DejaVu Serif:style=Bold
/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf: DejaVu Sans Mono:style=Book
/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf: DejaVu Sans:style=Book
/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf: DejaVu Sans:style=Bold
/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf: DejaVu Sans Mono:style=Bold
/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf: DejaVu Serif:style=Book
```

- Windows 字体在 **C:\Windows\Fonts\** 文件下，直接打开就能看到了。
- mac OS 字体在 **/System/Library/Fonts** 和 **/Library/Fonts** 目录下。


系统支持的字体库，可以通过安装 showtext 来查看：


```
> install.packages("showtext", repos = "https://mirrors.ustc.edu.cn/CRAN/")  # 安装 showtext
...
> font_files()   # 查看字体
            path              file           family    face       version
1 /Library/Fonts Arial Unicode.ttf Arial Unicode MS Regular Version 1.01x
         ps_name
1 ArialUnicodeMS
```


看到有 ArialUnicodeMS，我们就可以用了：


```
pie3D(info,labels = names,explode = 0.1, main = "3D 图",family = "ArialUnicodeMS")
```


### 载入自定义字体

系统的字体库有时候不是支持的很好， showtext() 函数可以载入我们自定义的字体，可以下载字体包 ttf，然后使用 font_add() 函数添加。


这里我们使用思源黑体，思源黑体是 Adobe 与 Google 推出的一款开源字体。


官网：[https://source.typekit.com/source-han-serif/cn/](https://source.typekit.com/source-han-serif/cn/)


GitHub 地址：[https://github.com/adobe-fonts/source-han-sans/tree/release/OTF/SimplifiedChinese](https://github.com/adobe-fonts/source-han-sans/tree/release/OTF/SimplifiedChinese)


打开链接后，在里面选一个就好了：


![](https://www.runoob.com/wp-content/uploads/2020/07/134652C4-1164-466B-ACA2-ECE8B7E6F2AF.jpg)


你也可以在网盘下载: [https://pan.baidu.com/s/14cRhgYvvYotVIFkRVd71fQ](https://pan.baidu.com/s/14cRhgYvvYotVIFkRVd71fQ) 。


可以下载个 OTF 字体，比如 SourceHanSansSC-Bold.otf，将该文件文件放在当前执行的代码文件中：


柱形图使用字体库：


## 实例


```r
# 载入 showtext
library(showtext);
# 第一个参数设置字体名称，第二个参数为字体库路径，同目录下，我们写字体库名就可以了
font_add("SyHei", "SourceHanSansSC-Bold.otf");

# 设置文件名，输出为 png
png(file = "runoob-bar-cn.png")

cvd19 = c(83534,2640626,585493)
#加载字体
showtext_begin();
barplot(cvd19,
    main="新冠疫情条形图",
    col=c("#ED1C24","#22B14C","#FFC90E"),
    names.arg=c("中国","美国","印度"),
    family='SyHei'     # 设置字体库
)
# 去掉字体
showtext_end();
```


![](https://www.runoob.com/wp-content/uploads/2020/07/runoob-bar-cn.png)


3D 饼图使用中文：


## 实例


```r
library(plotrix)
library(showtext);
# 第一个参数设置字体名称，第二个参数为字体库路径，同目录下，我们写字体库名就可以了
font_add("SyHei", "SourceHanSansSC-Bold.otf");
# 数据准备
info = c(1, 2, 4, 8)

# 命名
names = c("Google", "Runoob", "Taobao", "Weibo")

# 涂色（可选）
cols = c("#ED1C24","#22B14C","#FFC90E","#3f48CC")

# 设置文件名，输出为 png
png(file = "3d_pie_chart.png")

#加载字体
showtext_begin();

# 绘制 3D 图
pie3D(info,labels = names,explode = 0.1, main = "我测试一下 SyHei 字体",family = "SyHei")

# 去掉字体
showtext_end();
# 关闭图形设备
dev.off();
```


![](https://www.runoob.com/wp-content/uploads/2020/07/syht.png)









	  AI 思考中...





			** [R 绘图 – 饼图](https://www.runoob.com/r-pie-charts.html)
			[R 绘图 – 条形图](https://www.runoob.com/r-bar-charts.html) **













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