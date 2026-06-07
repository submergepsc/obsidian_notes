# CSS id 和 class

- Source: https://www.runoob.com/css/css-id-class.html

---


## id 和 class 选择器


如果你要在HTML元素中设置CSS样式，你需要在元素中设置"id" 和 "class"选择器。


---


## id 选择器


id 选择器可以为标有特定 id 的 HTML 元素指定特定的样式。


HTML元素以id属性来设置id选择器,CSS 中 id 选择器以 "#" 来定义。


以下的样式规则应用于元素属性 id="para1":


## 实例


```css
#para1
{
    text-align:center;
    color:red;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_syntax_id)


![Remark](https://www.runoob.com/images/lamp.gif) ID属性不要以数字开头，数字开头的ID在 Mozilla/Firefox 浏览器中不起作用。


---


## class 选择器


class 选择器用于描述一组元素的样式，class 选择器有别于id选择器，class可以在多个元素中使用。


class 选择器在 HTML 中以 class 属性表示, 在 CSS 中，类选择器以一个点 **.** 号显示：


在以下的例子中，所有拥有 center 类的 HTML 元素均为居中。


## 实例


```css
.center {text-align:center;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_syntax_class)


你也可以指定特定的 HTML 元素使用 class。


在以下实例中, 所有的 p 元素使用 class="center" 让该元素的文本居中:


## 实例


```css
p.center {text-align:center;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_syntax_element_class)


多个 class 选择器可以使用空格分开：


## 实例


```css
.center { text-align:center; }
.color { color:#ff0000; }
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_syntax_class2)


![Remark](https://www.runoob.com/images/lamp.gif) 类名的第一个字符不能使用数字！它无法在 Mozilla 或 Firefox 中起作用。








	  AI 思考中...





			** [CSS 语法](https://www.runoob.com/css-syntax.html)
			[CSS 创建](https://www.runoob.com/css-howto.html) **