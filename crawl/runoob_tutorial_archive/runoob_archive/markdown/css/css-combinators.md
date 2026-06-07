# CSS 组合选择符

- Source: https://www.runoob.com/css/css-combinators.html

---


## CSS 组合选择符


|  | 组合选择符说明了两个选择器之间的关系。 |
| --- | --- |


CSS组合选择符包括各种简单选择符的组合方式。


在 CSS3 中包含了四种组合方式:


- 后代选择器(以空格 ** ** 分隔)
- 子元素选择器(以大于 **>** 号分隔）
- 相邻兄弟选择器（以加号 **+** 分隔）
- 普通兄弟选择器（以波浪号 **～** 分隔）


---


## 后代选择器


后代选择器用于选取某元素的后代元素。


以下实例选取所有  元素插入到  元素中:


## 实例


```css
div p
{
  background-color:yellow;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_sel_element_element)


---


## 子元素选择器


与后代选择器相比，子元素选择器（Child selectors）只能选择作为某元素直接/一级子元素的元素。


以下实例选择了元素中所有直接子元素  ：


## 实例


```css
div>p
{
  background-color:yellow;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_sel_element_gt)


---


## 相邻兄弟选择器


相邻兄弟选择器（Adjacent sibling selector）可选择紧接在另一元素后的元素，且二者有相同父元素。


如果需要选择紧接在另一个元素后的元素，而且二者有相同的父元素，可以使用相邻兄弟选择器（Adjacent sibling selector）。


以下实例选取了所有位于  元素后的第一个  元素:


## 实例


```css
div+p
{
  background-color:yellow;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_sel_element_pluss)


---


## 后续兄弟选择器


后续兄弟选择器选取所有指定元素之后的相邻兄弟元素。


以下实例选取了所有  元素之后的所有相邻兄弟元素  :


## 实例


```css
div~p
{
  background-color:yellow;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_sel_element_tilde)








	  AI 思考中...





			** [CSS 实例](https://www.runoob.com/css-examples.html)
			[响应式 Web 设计 – 介绍](https://www.runoob.com/css-rwd-intro.html) **