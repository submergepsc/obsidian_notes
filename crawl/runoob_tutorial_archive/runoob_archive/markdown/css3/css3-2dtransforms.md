# CSS3 2D 转换

- Source: https://www.runoob.com/css3/css3-2dtransforms.html

---


## CSS3 转换


CSS3 转换可以对元素进行移动、缩放、转动、拉长或拉伸。


![CSS3 Transforms](https://www.runoob.com/images/transforms.gif)
## 它是如何工作？


转换的效果是让某个元素改变形状，大小和位置。


您可以使用 2D 或 3D 转换来转换您的元素。


鼠标移动到以下元素上，查看 2D 和 3D 的转换效果：


2D 转换
3D 转换


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


紧跟在 -webkit-, -ms- 或 -moz- 前的数字为支持该前缀属性的第一个浏览器版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| transform | 36.04.0 -webkit- | 10.09.0 -ms- | 16.03.5 -moz- | 3.2 -webkit- | 23.015.0 -webkit-12.110.5 -o- |
| transform-origin(two-value syntax) | 36.04.0 -webkit- | 10.09.0 -ms- | 16.03.5 -moz- | 3.2 -webkit- | 23.015.0 -webkit-12.110.5 -o- |


Internet Explorer 10, Firefox, 和 Opera支持transform 属性.


Chrome 和 Safari 要求前缀 -webkit- 版本.


**注意：** Internet Explorer 9 要求前缀 -ms- 版本.


---


## 2D 转换


在本章您将了解2D变换方法：


- translate()
- rotate()
- scale()
- skew()
- matrix()


在下一章中您将了解3D转换。


![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


```css
div
{
transform: rotate(30deg);
-ms-transform: rotate(30deg); /* IE 9 */
-webkit-transform: rotate(30deg); /* Safari and Chrome */
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_transform1)


---


## translate() 方法

![Translate](https://www.runoob.com/images/transform_translate.gif)
translate()方法，根据左(X轴)和顶部(Y轴)位置给定的参数，从当前元素位置移动。


![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


```css
div
{
transform: translate(50px,100px);
-ms-transform: translate(50px,100px); /* IE 9 */
-webkit-transform: translate(50px,100px); /* Safari and Chrome */
}
```





[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_transform_translate)


translate值（50px，100px）是从左边元素移动50个像素，并从顶部移动100像素。


---


## rotate() 方法


![Rotate](https://www.runoob.com/images/transform_rotate.gif)
rotate()方法，在一个给定度数顺时针旋转的元素。负值是允许的，这样是元素逆时针旋转。


![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


```css
div
{
transform: rotate(30deg);
-ms-transform: rotate(30deg); /* IE 9 */
-webkit-transform: rotate(30deg); /* Safari and Chrome */
}
```





[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_transform_rotate)


rotate值（30deg）元素顺时针旋转30度。


---


## scale() 方法


![Scale](https://www.runoob.com/images/transform_scale.gif)
scale()方法，该元素增加或减少的大小，取决于宽度（X轴）和高度（Y轴）的参数：


![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


```css
-ms-transform:scale(2,3); /* IE 9 */
-webkit-transform: scale(2,3); /* Safari */
transform: scale(2,3); /* 标准语法 */
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_transform_scale)


scale（2,3）转变宽度为原来的大小的2倍，和其原始大小3倍的高度。


---


## skew() 方法


### 语法


```
transform:skew(<angle> [,<angle>]);
```


包含两个参数值，分别表示X轴和Y轴倾斜的角度，如果第二个参数为空，则默认为0，参数为负表示向相反方向倾斜。


- skewX();表示只在X轴(水平方向)倾斜。
- skewY();表示只在Y轴(垂直方向)倾斜。


![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


```css
div
{
transform: skew(30deg,20deg);
-ms-transform: skew(30deg,20deg); /* IE 9 */
-webkit-transform: skew(30deg,20deg); /* Safari and Chrome */
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_transform_skew)


skew(30deg,20deg)** 元素在 **X** 轴和 **Y** 轴上倾斜 20 度 30 度。


---


## matrix() 方法


![Rotate](https://www.runoob.com/images/transform_rotate.gif)
matrix()方法和2D变换方法合并成一个。


matrix 方法有六个参数，包含旋转，缩放，移动（平移）和倾斜功能。


![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


利用matrix()方法旋转div元素30°


```css
div
{
transform:matrix(0.866,0.5,-0.5,0.866,0,0);
-ms-transform:matrix(0.866,0.5,-0.5,0.866,0,0); /* IE 9 */
-webkit-transform:matrix(0.866,0.5,-0.5,0.866,0,0); /* Safari and Chrome */
}
```





[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_transform_matrix1)


---


## 新转换属性


以下列出了所有的转换属性:


| Property | 描述 | CSS |
| --- | --- | --- |
| transform | 适用于2D或3D转换的元素 | 3 |
| transform-origin | 允许您更改转化元素位置 | 3 |


## 2D 转换方法


| 函数 | 描述 |
| --- | --- |
| matrix(n,n,n,n,n,n) | 定义 2D 转换，使用六个值的矩阵。 |
| translate(x,y) | 定义 2D 转换，沿着 X 和 Y 轴移动元素。 |
| translateX(n) | 定义 2D 转换，沿着 X 轴移动元素。 |
| translateY(n) | 定义 2D 转换，沿着 Y 轴移动元素。 |
| scale(x,y) | 定义 2D 缩放转换，改变元素的宽度和高度。 |
| scaleX(n) | 定义 2D 缩放转换，改变元素的宽度。 |
| scaleY(n) | 定义 2D 缩放转换，改变元素的高度。 |
| rotate(angle) | 定义 2D 旋转，在参数中规定角度。 |
| skew(x-angle,y-angle) | 定义 2D 倾斜转换，沿着 X 和 Y 轴。 |
| skewX(angle) | 定义 2D 倾斜转换，沿着 X 轴。 |
| skewY(angle) | 定义 2D 倾斜转换，沿着 Y 轴。 |








	  AI 思考中...





			** [CSS3 字体](https://www.runoob.com/css3-fonts.html)
			[CSS3 3D 转换](https://www.runoob.com/css3-3dtransforms.html) **