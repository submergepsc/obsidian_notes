# CSS Display(显示) 与 Visibility（可见性）

- Source: https://www.runoob.com/css/css-display-visibility.html

---


display属性设置一个元素应如何显示，visibility属性指定一个元素应可见还是隐藏。


Box 1**
![](https://www.runoob.com/images/klematis_small.jpg)


Box 2

![](https://www.runoob.com/images/klematis2_small.jpg)


Box 3

![](https://www.runoob.com/images/klematis3_small.jpg)


---


## 隐藏元素 - display:none或visibility:hidden


隐藏一个元素可以通过把display属性设置为"none"，或把visibility属性设置为"hidden"。但是请注意，这两种方法会产生不同的结果。


visibility:hidden可以隐藏某个元素，但隐藏的元素仍需占用与未隐藏之前一样的空间。也就是说，该元素虽然被隐藏了，但仍然会影响布局。


## 实例


```css
h1.hidden {visibility:hidden;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_visibility_hidden)


display:none可以隐藏某个元素，且隐藏的元素不会占用任何空间。也就是说，该元素不但被隐藏了，而且该元素原本占用的空间也会从页面布局中消失。


## 实例


```css
h1.hidden {display:none;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_display_none)


---


## CSS Display - 块和内联元素


块元素是一个元素，占用了全部宽度，在前后都是换行符。


块元素的例子：


-
-
- 内联元素只需要必要的宽度，不强制换行。


内联元素的例子：


-
-


---


## 如何改变一个元素显示


可以更改内联元素和块元素，反之亦然，可以使页面看起来是以一种特定的方式组合，并仍然遵循web标准。


下面的示例把列表项显示为内联元素：


## 实例


```css
li {display:inline;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_display_inline_list)


下面的示例把span元素作为块元素：


## 实例


```css
span {display:block;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_display_block2)


注意：**变更元素的显示类型看该元素是如何显示，它是什么样的元素。例如：一个内联元素设置为display:block是不允许有它内部的嵌套块元素。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[如何显示元素的内联元素。](https://www.runoob.com/try/try.php?filename=trycss_display)


这个例子演示了如何显示一个元素的内联元素。


[如何显示元素的块元素。](https://www.runoob.com/try/try.php?filename=trycss_display_block)


这个例子演示了如何显示一个元素的块元素。


[如何使用一个表的collapse属性。](https://www.runoob.com/try/try.php?filename=trycss_visibility_collapse)


这个例子演示了如何使用表的collapse属性。








	  AI 思考中...





			** [CSS 尺寸 (Dimension)](https://www.runoob.com/css-dimension.html)
			[CSS Position(定位)](https://www.runoob.com/css-positioning.html) **