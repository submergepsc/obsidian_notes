# CSS3 文本效果

- Source: https://www.runoob.com/css3/css3-text-effects.html

---


## CSS3 文本效果


CSS3中包含几个新的文本特征。


在本章中您将了解以下文本属性：


- text-shadow
- box-shadow
- text-overflow
- word-wrap
- word-break


---


## 浏览器支持


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| text-shadow | 4.0 | 10.0 | 3.5 | 4.0 | 9.5 |
| box-shadow | 10.04.0 -webkit- | 9.0 | 4.03.5 -moz- | 5.13.1 -webkit- | 10.5 |
| text-overflow | 4.0 | 6.0 | 7.0 | 3.1 | 11.09.0 -o- |
| word-wrap | 23.0 | 5.5 | 3.5 | 6.1 | 12.1 |
| word-break | 4.0 | 5.5 | 15.0 | 3.1 | 15.0 |


---


## CSS3 的文本阴影


CSS3 中，text-shadow属性适用于文本阴影。


![阴影效果!](https://www.runoob.com/images/text_shadow_effect.gif)


您指定了水平阴影，垂直阴影，模糊的距离，以及阴影的颜色：

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


给标题添加阴影:


```css
h1
{
    text-shadow: 5px 5px 5px #FF0000;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_text-shadow_tut)


---


## CSS3 box-shadow属性


CSS3 中 CSS3 box-shadow 属性适用于盒子阴影


## 实例



```css
div {
    box-shadow: 10px 10px 5px #888888;
}
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_box-shadow)


---


## 接下来给阴影添加颜色


## 实例



```css
div {
    box-shadow: 10px 10px grey;
}
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_box-shadow2)


---


## 接下来给阴影添加一个模糊效果


## 实例



```css
div {
    box-shadow: 10px 10px 5px grey;
}
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_box-shadow3)


---


## 你也可以在 ::before 和 ::after 两个伪元素中添加阴影效果



## 实例



```css
#boxshadow {
    position: relative;
    box-shadow: 1px 2px 4px rgba(0, 0, 0, .5);
    padding: 10px;
    background: white;
}
#boxshadow img {
     width: 100%;
     border: 1px solid #8a4419;
     border-style: inset;
}
#boxshadow::after {
    content: '';
    position: absolute;
    z-index: -1; /* hide shadow behind image */
    box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3);
    width: 70%;
    left: 15%; /* one half of the remaining 30% */
    height: 100px;
    bottom: 0;
}
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_box-shadow6)


---


## 阴影的一个使用特例是卡片效果



## 实例



```css
div.card {
    width: 250px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    text-align: center;
}
```



[文字卡片 »](https://www.runoob.com/try/try.php?filename=trycss3_box-shadow4)
[图片卡片 »](https://www.runoob.com/try/try.php?filename=trycss3_box-shadow5)


---


## CSS3 Text Overflow属性


CSS3文本溢出属性指定应向用户如何显示溢出内容


## 实例



```css
p.test1 {
    white-space: nowrap;
    width: 200px;
    border: 1px solid #000000;
    overflow: hidden;
    text-overflow: clip;
}

p.test2 {
    white-space: nowrap;
    width: 200px;
    border: 1px solid #000000;
    overflow: hidden;
    text-overflow: ellipsis;
}
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_text-overflow)


---


## CSS3的换行


如果某个单词太长，不适合在一个区域内，它扩展到外面：


CSS3中，自动换行属性允许您强制文本换行 - 即使这意味着分裂它中间的一个字：


CSS代码如下：

![Opera](https://www.runoob.com/images/compatible_opera2020.gif)![Safari](https://www.runoob.com/images/compatible_safari2020.gif)![Chrome](https://www.runoob.com/images/compatible_chrome2020.gif)![Firefox](https://www.runoob.com/images/compatible_firefox2020.gif)![Internet Explorer](https://www.runoob.com/images/compatible_ie2020.gif)
## 实例


允许长文本换行:


```css
p {word-wrap:break-word;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_word-wrap)


---


## CSS3 单词拆分换行


CSS3 单词拆分换行属性指定换行规则：


CSS代码如下：


## 实例



```css
p.test1 {
    word-break: keep-all;
}

p.test2 {
    word-break: break-all;
}
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_word-break)


---


## 新文本属性


| 属性 | 描述 | CSS |
| --- | --- | --- |
| hanging-punctuation | 规定标点字符是否位于线框之外。 | 3 |
| punctuation-trim | 规定是否对标点字符进行修剪。 | 3 |
| text-align-last | 设置如何对齐最后一行或紧挨着强制换行符之前的行。 | 3 |
| text-emphasis | 向元素的文本应用重点标记以及重点标记的前景色。 | 3 |
| text-justify | 规定当 text-align 设置为 "justify" 时所使用的对齐方法。 | 3 |
| text-outline | 规定文本的轮廓。 | 3 |
| text-overflow | 规定当文本溢出包含元素时发生的事情。 | 3 |
| text-shadow | 向文本添加阴影。 | 3 |
| text-wrap | 规定文本的换行规则。 | 3 |
| word-break | 规定非中日韩文本的换行规则。 | 3 |
| word-wrap | 允许对长的不可分割的单词进行分割并换行到下一行。 | 3 |








	  AI 思考中...





			** [CSS3 背景](https://www.runoob.com/css3-backgrounds.html)
			[CSS3 字体](https://www.runoob.com/css3-fonts.html) **