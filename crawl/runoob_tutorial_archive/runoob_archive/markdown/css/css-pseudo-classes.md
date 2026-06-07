# CSS 伪类(Pseudo-classes)

- Source: https://www.runoob.com/css/css-pseudo-classes.html

---


CSS伪类是用来添加一些选择器的特殊效果。


---


## 语法


伪类的语法：


selector:pseudo-class {property:value;}


CSS类也可以使用伪类：


selector.class:pseudo-class {property:value;}
**
---


## anchor伪类


在支持 CSS 的浏览器中，链接的不同状态都可以以不同的方式显示


## 实例


```css
a:link {color:#FF0000;} /* 未访问的链接 */
a:visited {color:#00FF00;} /* 已访问的链接 */
a:hover {color:#FF00FF;} /* 鼠标划过链接 */
a:active {color:#0000FF;} /* 已选中的链接 */
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_link)


注意：** 在CSS定义中，a:hover 必须被置于 a:link 和 a:visited 之后，才是有效的。


**注意：** 在 CSS 定义中，a:active 必须被置于 a:hover 之后，才是有效的。


**注意：**伪类的名称不区分大小写。


---


## 伪类和CSS类


伪类可以与 CSS 类配合使用：


```css
a.red:visited {color:#FF0000;}

<a class="red" href="css-syntax.html">CSS 语法</a>
```


如果在上面的例子的链接已被访问，它会显示为红色。


---


## CSS :first-child 伪类


您可以使用 :first-child 伪类来选择父元素的第一个子元素。


**注意：**在IE8的之前版本必须声明[](https://www.runoob.com/../tags/tag-doctype.html) ，这样 :first-child 才能生效。


## 匹配第一个 元素


在下面的例子中，选择器匹配作为任何元素的第一个子元素的  元素：


## 实例


```css
p:first-child
{
    color:blue;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_first-child1)


---


## 匹配所有 元素中的第一个 元素


在下面的例子中，选择相匹配的所有元素的第一个  元素：


## 实例


```css
p > i:first-child
{
    color:blue;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_first-child2)


---


## 匹配所有作为第一个子元素的 元素中的所有 元素


在下面的例子中，选择器匹配所有作为元素的第一个子元素的  元素中的所有  元素：


## 实例


```css
p:first-child i
{
    color:blue;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_first-child3)


---


## CSS - :lang 伪类


:lang 伪类使你有能力为不同的语言定义特殊的规则


注意：**IE8必须声明[](https://www.runoob.com/../tags/tag-doctype.html)才能支持;lang伪类。


在下面的例子中，:lang 类为属性值为 no 的q元素定义引号的类型：


## 实例


```css
q:lang(no) {quotes: "~" "~";}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_lang)


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[为超链接添加不同样式](https://www.runoob.com/try/try.php?filename=trycss_link2) 这个例子演示了如何为超链接添加其他样式。


[使用 :focus](https://www.runoob.com/try/try.php?filename=trycss_link_focus) 这个例子演示了如何使用 :focus伪类。


---


## 所有CSS伪类/元素


| 选择器 | 示例 | 示例说明 |
| --- | --- | --- |
| :checked | input:checked | 选择所有选中的表单元素 |
| :disabled | input:disabled | 选择所有禁用的表单元素 |
| :empty | p:empty | 选择所有没有子元素的p元素 |
| :enabled | input:enabled | 选择所有启用的表单元素 |
| :first-of-type | p:first-of-type | 选择的每个 p 元素是其父元素的第一个 p 元素 |
| :in-range | input:in-range | 选择元素指定范围内的值 |
| :invalid | input:invalid | 选择所有无效的元素 |
| :last-child | p:last-child | 选择所有p元素的最后一个子元素 |
| :last-of-type | p:last-of-type | 选择每个p元素是其母元素的最后一个p元素 |
| :not(selector) | :not(p) | 选择所有p以外的元素 |
| :nth-child(n) | p:nth-child(2) | 选择所有 p 元素的父元素的第二个子元素 |
| :nth-last-child(n) | p:nth-last-child(2) | 选择所有p元素倒数的第二个子元素 |
| :nth-last-of-type(n) | p:nth-last-of-type(2) | 选择所有p元素倒数的第二个为p的子元素 |
| :nth-of-type(n) | p:nth-of-type(2) | 选择所有p元素第二个为p的子元素 |
| :only-of-type | p:only-of-type | 选择所有仅有一个子元素为p的元素 |
| :only-child | p:only-child | 选择所有仅有一个子元素的p元素 |
| :optional | input:optional | 选择没有"required"的元素属性 |
| :out-of-range | input:out-of-range | 选择指定范围以外的值的元素属性 |
| :read-only | input:read-only | 选择只读属性的元素属性 |
| :read-write | input:read-write | 选择没有只读属性的元素属性 |
| :required | input:required | 选择有"required"属性指定的元素属性 |
| :root | root | 选择文档的根元素 |
| :target | #news:target | 选择当前活动#news元素(点击URL包含锚的名字) |
| :valid | input:valid | 选择所有有效值的属性 |
| :link | a:link | 选择所有未访问链接 |
| :visited | a:visited | 选择所有访问过的链接 |
| :active | a:active | 选择正在活动链接 |
| :hover | a:hover | 把鼠标放在链接上的状态 |
| :focus | input:focus | 选择元素输入后具有焦点 |
| :first-letter | p:first-letter | 选择每个 元素的第一个字母 |
| :first-line | p:first-line | 选择每个 元素的第一行 |
| :first-child | p:first-child | 选择器匹配属于任意元素的第一个子元素的 元素 |
| :before | p:before | 在每个元素之前插入内容 |
| :after | p:after | 在每个元素之后插入内容 |
| :lang(language) | p:lang(it) | 为元素的lang属性选择一个开始值 |








	  AI 思考中...





			** [CSS 布局 – 水平 & 垂直对齐](https://www.runoob.com/css-align.html)
			[CSS 伪元素](https://www.runoob.com/css-pseudo-elements.html) **