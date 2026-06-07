# HTML5 MathML

- Source: https://www.runoob.com/html/html5-mathml.html

HTML5 可以在文档中使用 MathML 元素，对应的标签是 ... 。


MathML 是数学标记语言，是一种基于XML（标准通用标记语言的子集）的标准，用来在互联网上书写数学符号和公式的置标语言。


**
注意：**目前只有 Firefox 或 Safari 浏览器支持，大部分浏览器还不支持 MathML 标签，如果你的浏览器不支持该标签，可以使用最新版的 Firefox 或 Safari 浏览器查看。


另外我们可以使用第三方的样式库来支持数学标记，本章节使用的样式库可以点击下面按钮下载：


[下载 mathml.zip](https://static.jyshare.com/assets/js/mathml/mathml.zip)


---


## MathML 实例


以下是一个简单的 MathML 实例：


## 实例


```html
<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8">
      <title>菜鸟教程(runoob.com)</title>
   </head>

   <body>

      <math xmlns="http://www.w3.org/1998/Math/MathML">

         <mrow>
            <msup><mi>a</mi><mn>2</mn></msup>
            <mo>+</mo>

            <msup><mi>b</mi><mn>2</mn></msup>
            <mo>=</mo>

            <msup><mi>c</mi><mn>2</mn></msup>
         </mrow>

      </math>

   </body>
</html>
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_mathml)

使用第三方库来支持：


## 实例


```html
<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8">
      <title>菜鸟教程(runoob.com)</title>
      <script type="text/javascript" src="https://static.jyshare.com/assets/js/mathml/mspace.js"></script>
   </head>

   <body>

      <math xmlns="http://www.w3.org/1998/Math/MathML">

         <mrow>
            <msup><mi>a</mi><mn>2</mn></msup>
            <mo>+</mo>

            <msup><mi>b</mi><mn>2</mn></msup>
            <mo>=</mo>

            <msup><mi>c</mi><mn>2</mn></msup>
         </mrow>

      </math>

   </body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_mathml_css1)

运行结果图，如下所示：


![](https://www.runoob.com/wp-content/uploads/2015/12/mathml1.jpg)


以下实例添加了一些运算符：


## 实例


```html
<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8">
      <title>菜鸟教程(runoob.com)</title>
   </head>

   <body>

      <math xmlns="http://www.w3.org/1998/Math/MathML">

         <mrow>
            <mrow>

               <msup>
                  <mi>x</mi>
                  <mn>2</mn>
               </msup>

               <mo>+</mo>

               <mrow>
                  <mn>4</mn>
                  <mo>⁢</mo>
                  <mi>x</mi>
               </mrow>

               <mo>+</mo>
               <mn>4</mn>

            </mrow>

            <mo>=</mo>
            <mn>0</mn>

         </mrow>
      </math>

   </body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_mathml1)

使用第三方库来支持：


## 实例


```html
<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8">
      <title>菜鸟教程(runoob.com)</title>
      <script type="text/javascript" src="https://static.jyshare.com/assets/js/mathml/mspace.js"></script>
   </head>

   <body>

      <math xmlns="http://www.w3.org/1998/Math/MathML">

         <mrow>
            <mrow>

               <msup>
                  <mi>x</mi>
                  <mn>2</mn>
               </msup>

               <mo>+</mo>

               <mrow>
                  <mn>4</mn>
                  <mi>x</mi>
               </mrow>

               <mo>+</mo>
               <mn>4</mn>

            </mrow>

            <mo>=</mo>
            <mn>0</mn>

         </mrow>
      </math>

   </body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_mathml_css2)

运行结果图，如下所示：


![](https://www.runoob.com/wp-content/uploads/2015/12/mathml2-1.jpg)


以下实例是一个 2×2 矩阵，可以在 Firefox 3.5 以上版本查看到效果：


## 实例


```html
<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8">
      <title>菜鸟教程(runoob.com)</title>
   </head>

   <body>
      <math xmlns="http://www.w3.org/1998/Math/MathML">

         <mrow>
            <mi>A</mi>
            <mo>=</mo>

            <mfenced open="[" close="]">

               <mtable>
                  <mtr>
                     <mtd><mi>x</mi></mtd>
                     <mtd><mi>y</mi></mtd>
                  </mtr>

                  <mtr>
                     <mtd><mi>z</mi></mtd>
                     <mtd><mi>w</mi></mtd>
                  </mtr>
               </mtable>

            </mfenced>
         </mrow>
      </math>

   </body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_mathml2)


使用第三方库来支持：


## 实例


```html
<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8">
      <title>菜鸟教程(runoob.com)</title>
      <script type="text/javascript" src="https://static.jyshare.com/assets/js/mathml/mspace.js"></script>
   </head>

   <body>
      <math xmlns="http://www.w3.org/1998/Math/MathML">

         <mrow>
            <mi>A</mi>
            <mo>=</mo>

            <mfenced open="[" close="]">

               <mtable>
                  <mtr>
                     <mtd><mi>x</mi></mtd>
                     <mtd><mi>y</mi></mtd>
                  </mtr>

                  <mtr>
                     <mtd><mi>z</mi></mtd>
                     <mtd><mi>w</mi></mtd>
                  </mtr>
               </mtable>

            </mfenced>
         </mrow>
      </math>

   </body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_mathml_css3)


运行结果图，如下所示：


![](https://www.runoob.com/wp-content/uploads/2015/12/mathml3.jpg)









	  AI 思考中...





			** [HTML5 浏览器支持](https://www.runoob.com/html5-browsers.html)
			[HTML5 Web SQL 数据库](https://www.runoob.com/html5-web-sql.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html-examples.html)

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