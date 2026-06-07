# CSS 提示工具(Tooltip)

- Source: https://www.runoob.com/css/css-tooltip.html

本文我们为大家介绍如何使用 HTML 与 CSS 来创建提示工具。


提示工具在鼠标移动到指定元素后触发，先看以下四个实例：


| 头部显示 提示框文本 | 右边显示 提示框文本 | 底部显示 提示框文本 | 左边显示 提示框文本 |
| --- | --- | --- | --- |


---


## 基础提示框(Tooltip)


提示框在鼠标移动到指定元素上显示：


## HTML 代码：


```css
<style>
```

/* Tooltip 容器 */
.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black; /* 悬停元素上显示点线 */
}

/* Tooltip 文本 */
.tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: black;
    color: #fff;
    text-align: center;
    padding: 5px 0;
    border-radius: 6px;

    /* 定位 */
    position: absolute;
    z-index: 1;
}

/* 鼠标移动上去后显示提示框 */
.tooltip:hover .tooltiptext {
    visibility: visible;
}</style>

<div class="tooltip">鼠标移动到这
  <span class="tooltiptext">提示文本</span>
</div>

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_tooltip)


### 实例解析


HTML)** 使用容器元素 (like ) 并添加 **"tooltip"** 类。在鼠标移动到  上时显示提示信息。


提示文本放在内联元素上(如 ) 并使用**class="tooltiptext"**。


**CSS)****tooltip** 类使用 **position:relative**, 提示文本需要设置定位值 **position:absolute**。 **注意: ** 接下来的实例会显示更多的定位效果。


**tooltiptext** 类用于实际的提示文本。模式是隐藏的，在鼠标移动到元素显示 。设置了一些宽度、背景色、字体色等样式。


CSS3 **border-radius** 属性用于为提示框添加圆角。


**:hover** 选择器用于在鼠标移动到到指定元素  上时显示的提示。


---


## 定位提示工具


以下实例中，提示工具显示在指定元素的右侧(**left:105%**) 。

注意 **top:-5px** 同于定位在容器元素的中间。使用数字 **5** 因为提示文本的顶部和底部的内边距（padding）是 5px。

如果你修改 padding 的值，top 值也要对应修改，这样才可以确保它是居中对齐的。

在提示框显示在左边的情况也是这个原理。


## 显示在右侧：


```css
.tooltip .tooltiptext {
    top: -5px;
    left: 105%;
}
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_tooltip_right)


## 显示在左侧：


```css
.tooltip .tooltiptext {
    top: -5px;
    right: 105%;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_tooltip_left)


如果你想要提示工具显示在头部和底部。我们需要使用 margin-left** 属性，并设置为 -60px。 这个数字计算来源是使用宽度的一半来居中对齐，即： width/2 (120/2 = 60)。


## 显示在头部：


```css
.tooltip .tooltiptext {
    width: 120px;
    bottom: 100%;
    left: 50%;
    margin-left: -60px; /* 使用一半宽度 (120/2 = 60) 来居中提示工具 */
}
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_tooltip_top)


## 显示在底部：


```css
.tooltip .tooltiptext {
    width: 120px;
    top: 100%;
    left: 50%;
    margin-left: -60px; /* 使用一半宽度 (120/2 = 60) 来居中提示工具 */
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_tooltip_bottom)


---


## 添加箭头


我们可以用CSS 伪元素 ::after 及 content 属性为提示工具创建一个小箭头标志，箭头是由边框组成的，但组合起来后提示工具像个语音信息框。


以下实例演示了如何为显示在顶部的提示工具添加底部箭头：


## 顶部提示框/底部箭头：


```css
.tooltip .tooltiptext::after {
    content: " ";
    position: absolute;
    top: 100%; /* 提示工具底部 */
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: black transparent transparent transparent;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_tooltip_arrow_bottom)


### 实例解析


在提示工具内定位箭头: top: 100%** , 箭头将显示在提示工具的底部。**left: 50%** 用于居中对齐箭头。


**注意：****border-width** 属性指定了箭头的大小。如果你修改它，也要修改 **margin-left** 值。这样箭头才能居中显示。


**border-color** 用于将内容转换为箭头。设置顶部边框为黑色，其他是透明的。如果设置了其他的也是黑色则会显示为一个黑色的四边形。


以下实例演示了如何在提示工具的头部添加箭头，注意设置边框颜色：


## 底部提示框/顶部箭头：


```css
.tooltip .tooltiptext::after {
    content: " ";
    position: absolute;
    bottom: 100%;  /* 提示工具头部 */
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: transparent transparent black transparent;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_tooltip_arrow_top)


以下两个实例是左右两边的箭头实例：


## 右侧提示框/左侧箭头：


```css
.tooltip .tooltiptext::after {
    content: " ";
    position: absolute;
    top: 50%;
    right: 100%; /* 提示工具左侧 */
    margin-top: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: transparent black transparent transparent;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_tooltip_arrow_left)


## 左侧提示框/右侧箭头：


```css
.tooltip .tooltiptext::after {
    content: " ";
    position: absolute;
    top: 50%;
    left: 100%; /* 提示工具右侧 */
    margin-top: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: transparent transparent transparent black;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_tooltip_arrow_right)


---


## 淡入效果


我们可以使用 CSS3 transition 属性及 opacity 属性来实现提示工具的淡入效果:


## 淡入效果：


```css
.tooltip .tooltiptext {
    opacity: 0;
    transition: opacity 1s;
}

.tooltip:hover .tooltiptext {
    opacity: 1;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_tooltip_transition)


---


## 更多实例


[漂亮的 CSS 提示框](https://c.runoob.com/codedemo/2747)









	  AI 思考中...





			** [CSS 下拉菜单](https://www.runoob.com/css-dropdowns.html)
			[CSS 布局 Overflow](https://www.runoob.com/css-overflow.html) **