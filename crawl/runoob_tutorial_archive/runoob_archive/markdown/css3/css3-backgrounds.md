# CSS3 背景

- Source: https://www.runoob.com/css3/css3-backgrounds.html

---


## CSS3 背景


CSS3 中包含几个新的背景属性，提供更大背景元素控制。


在本章您将了解以下背景属性：


- background-image
- background-size
- background-origin
- background-clip


您还将学习如何使用多重背景图像。


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


紧跟在 -webkit-, -ms- 或 -moz- 前的数字为支持该前缀属性的第一个浏览器版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| background-image(with multiple backgrounds) | 4.0 | 9.0 | 3.6 | 3.1 | 11.5 |
| background-size | 4.01.0 -webkit- | 9.0 | 4.03.6 -moz- | 4.13.0 -webkit- | 10.510.0 -o- |
| background-origin | 1.0 | 9.0 | 4.0 | 3.0 | 10.5 |
| background-clip | 4.0 | 9.0 | 4.0 | 3.0 | 10.5 |


---


## CSS3 background-image属性


CSS3中可以通过background-image属性添加背景图片。


不同的背景图像和图像用逗号隔开，所有的图片中显示在最顶端的为第一张。


## 实例



```css
#example1 {
    background-image: url(img_flwr.gif), url(paper.gif);
    background-position: right bottom, left top;
    background-repeat: no-repeat, repeat;
}
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_background_multiple)


---


可以给不同的图片设置多个不同的属性


## 实例



```css
#example1 {
    background: url(img_flwr.gif) right bottom no-repeat, url(paper.gif) left top repeat;
}
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_background_multiple2)


---


## CSS3 background-size 属性


background-size指定背景图像的大小。CSS3以前，背景图像大小由图像的实际大小决定。


CSS3中可以指定背景图片，让我们重新在不同的环境中指定背景图片的大小。您可以指定像素或百分比大小。


你指定的大小是相对于父元素的宽度和高度的百分比的大小。


![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例 1


重置背景图像：


```css
div
{
    background:url(img_flwr.gif);
    background-size:80px 60px;
    background-repeat:no-repeat;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_background-size)


![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例 2


伸展背景图像完全填充内容区域：


```css
div
{
    background:url(img_flwr.gif);
    background-size:100% 100%;
    background-repeat:no-repeat;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_background-size2)


---


## CSS3 的 background-origin 属性


background-origin 属性指定了背景图像的位置区域。


content-box, padding-box,和 border-box区域内可以放置背景图像。


![](https://www.runoob.com/images/background-origin.gif)

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


在 content-box 中定位背景图片：


```css
div
{
    background:url(img_flwr.gif);
    background-repeat:no-repeat;
    background-size:100% 100%;
    background-origin:content-box;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_background-origin)


---


| ## CSS3 多个背景图像 |  |
| --- | --- |
| CSS3 允许你在元素上添加多个背景图像。 |  |

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


在 body 元素中设置两个背景图像：


```css
body
{
    background-image:url(img_flwr.gif),url(img_tree.gif);
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_background_multiple)


---


## CSS3 background-clip属性


CSS3中background-clip背景剪裁属性是从指定位置开始绘制。


## 实例



```css
#example1 {
    border: 10px dotted black;
    padding: 35px;
    background: yellow;
    background-clip: content-box;
}
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_background-clip)


---


## 新的背景属性


| 顺序 | 描述 | CSS |
| --- | --- | --- |
| background-clip | 规定背景的绘制区域。 | 3 |
| background-origin | 规定背景图片的定位区域。 | 3 |
| background-size | 规定背景图片的尺寸。 | 3 |








	  AI 思考中...





			** [CSS3 边框](https://www.runoob.com/css3-borders.html)
			[CSS3 文本效果](https://www.runoob.com/css3-text-effects.html) **