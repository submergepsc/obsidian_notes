# CSS Position(定位)

- Source: https://www.runoob.com/css/css-positioning.html

---


`position` 属性用于指定元素的定位方式。


常见的五种取值如下：


| 值 | 说明 | 锚点 |
| --- | --- | --- |
| static | 默认值，元素按照正常文档流排列，不受 top/right/bottom/left 影响 | 查看示例 |
| relative | 相对自身原始位置进行偏移，不会脱离文档流 | 查看示例 |
| absolute | 相对于最近的已定位祖先元素进行定位（否则相对于 body），脱离文档流 | 查看示例 |
| fixed | 相对于浏览器窗口定位，滚动页面时位置不会改变 | 查看示例 |
| sticky | 在滚动到指定位置前表现为 relative，之后表现为 fixed | 查看示例 |


元素可以通过 `top`、`right`、`bottom` 和 `left` 属性进行位置调整， 但这些属性只有在设置了 `position`（且值不为 `static`）时才会生效。 不同的定位方式会影响这些属性的参照对象和表现形式。


---


## static 定位


HTML 元素的默认值，即没有定位，遵循正常的文档流对象。


静态定位的元素不会受到 top, bottom, left, right影响。


## 实例


```css
div.static {
    position: static;
    border: 3px solid #73AD21;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_position_static)


---


## fixed 定位


元素的位置相对于浏览器窗口是固定位置。


即使窗口是滚动的它也不会移动：


## 实例


```css
p.pos_fixed
{
    position:fixed;
    top:30px;
    right:5px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_position_fixed)


注意：** Fixed 定位在 IE7 和 IE8 下需要描述 !DOCTYPE 才能支持。


Fixed定位使元素的位置与文档流无关，因此不占据空间。


Fixed定位的元素和其他元素重叠。


---


## relative 定位


相对定位元素的定位是相对其正常位置。


## 实例


```css
h2.pos_left
{
    position:relative;
    left:-20px;
}
h2.pos_right
{
    position:relative;
    left:20px;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_position_relative)


移动相对定位元素，但它原本所占的空间不会改变。


## 实例


```css
h2.pos_top
{
    position:relative;
    top:-50px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_position_relative2)


相对定位元素经常被用来作为绝对定位元素的容器块。


---


## absolute 定位


绝对定位的元素的位置相对于最近的已定位父元素，如果元素没有已定位的父元素，那么它的位置相对于:


## 实例


```css
h2
{
    position:absolute;
    left:100px;
    top:150px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_position_absolute)


absolute 定位使元素的位置与文档流无关，因此不占据空间。


absolute 定位的元素和其他元素重叠。


---


## sticky 定位


sticky 英文字面意思是粘，粘贴，所以可以把它称之为粘性定位。


**position: sticky;** 基于用户的滚动位置来定位。


粘性定位的元素是依赖于用户的滚动，在 position:relative** 与 **position:fixed** 定位之间切换。


它的行为就像 **position:relative;** 而当页面滚动超出目标区域时，它的表现就像 **position:fixed;**，它会固定在目标位置。


元素定位表现为在跨越特定阈值前为相对定位，之后为固定定位。


这个特定阈值指的是 top, right, bottom 或 left 之一，换言之，指定 top, right, bottom 或 left 四个阈值其中之一，才可使粘性定位生效。否则其行为与相对定位相同。


**注意: **Internet Explorer, Edge 15 及更早 IE 版本不支持 sticky 定位。 Safari 需要使用 -webkit- prefix (查看以下实例)。


## 实例


```css
div.sticky {
    position: -webkit-sticky; /* Safari */
    position: sticky;
    top: 0;
    background-color: green;
    border: 2px solid #4CAF50;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_position_sticky)


---


## 重叠的元素


元素的定位与文档流无关，所以它们可以覆盖页面上的其它元素


z-index属性指定了一个元素的堆叠顺序（哪个元素应该放在前面，或后面）


一个元素可以有正数或负数的堆叠顺序：


## 实例


```css
img
{
    position:absolute;
    left:0px;
    top:0px;
    z-index:-1;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_zindex)


具有更高堆叠顺序的元素总是在较低的堆叠顺序元素的前面。


注意：** 如果两个定位元素重叠，没有指定z - index，最后定位在HTML代码中的元素将被显示在最前面。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[裁剪元素的外形](https://www.runoob.com/try/try.php?filename=trycss_clip)


此示例演示如何设置元素的外形。该元素被剪裁成这种形状，并显示出来。


[如何使用滚动条来显示元素内溢出的内容](https://www.runoob.com/try/try.php?filename=trycss_overflow)


这个例子演示了overflow属性创建一个滚动条，当一个元素的内容在指定的区域过大时如何设置以适应。


[如何设置浏览器自动溢出处理](https://www.runoob.com/try/try.php?filename=trycss_pos_overflow_auto)


这个例子演示了如何设置浏览器来自动处理溢出。


[更改光标](https://www.runoob.com/try/try.php?filename=trycss_cursor)


这个例子演示了如何改变光标。


---


## 所有的CSS定位属性


"CSS" 列中的数字表示哪个CSS(CSS1 或者CSS2)版本定义了该属性。


| 属性 | 说明 | 值 | CSS |
| --- | --- | --- | --- |
| bottom | 定义了定位元素下外边距边界与其包含块下边界之间的偏移。 | auto length % inherit | 2 |
| clip | 剪辑一个绝对定位的元素 | shape auto inherit | 2 |
| cursor | 显示光标移动到指定的类型 | url auto crosshair default pointer move e-resize ne-resize nw-resize n-resize se-resize sw-resize s-resize w-resize text wait help | 2 |
| left | 定义了定位元素左外边距边界与其包含块左边界之间的偏移。 | auto length % inherit | 2 |
| overflow | 设置当元素的内容溢出其区域时发生的事情。 | auto hidden scroll visible inherit | 2 |
| overflow-y | 指定如何处理顶部/底部边缘的内容溢出元素的内容区域 | auto hidden scroll visible no-display no-content | 2 |
| overflow-x | 指定如何处理右边/左边边缘的内容溢出元素的内容区域 | auto hidden scroll visible no-display no-content | 2 |
| position | 指定元素的定位类型 | absolute fixed relative static inherit | 2 |
| right | 定义了定位元素右外边距边界与其包含块右边界之间的偏移。 | auto length % inherit | 2 |
| top | 定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。 | auto length % inherit | 2 |
| z-index | 设置元素的堆叠顺序 | number auto inherit | 2 |








	  AI 思考中...





			** [CSS Display(显示) 与 Visibility（可见性）](https://www.runoob.com/css-display-visibility.html)
			[CSS Float（浮动）](https://www.runoob.com/css-float.html) **