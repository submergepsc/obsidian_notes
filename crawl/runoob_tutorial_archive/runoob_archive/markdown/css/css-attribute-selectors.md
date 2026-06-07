# CSS 属性 选择器

- Source: https://www.runoob.com/css/css-attribute-selectors.html

---


CSS 属性选择器用于根据元素的属性或属性值来选择 HTML 元素。

属性选择器可以帮助你在不需要为元素添加类或 ID 的情况下对其进行样式化。


**注意：**IE7 和 IE8 需声明 **!DOCTYPE** 才支持属性选择器！IE6 和更低的版本不支持属性选择器。


以下是常见的 CSS 属性选择器：


### 1、[attribute]

选择带有指定属性的所有元素（无论属性值是什么）。


```
/* 选择所有具有 `type` 属性的元素 */
[type] {
  border: 1px solid red;
}
```


### 2、[attribute="value"]

选择具有指定属性和值完全匹配的元素。


```
/* 选择所有 `type` 属性等于 `text` 的元素 */
[type="text"] {
  background-color: yellow;
}
```


### 3、[attribute~="value"]

选择属性值中包含指定词（用空格分隔的词列表之一）的元素。


```
/* 选择属性值中包含 `button` 的元素 */
[class~="button"] {
  font-weight: bold;
}
```


### 4、[attribute|="value"]

选择具有指定值或者以指定值开头并紧跟着连字符 - 的属性值的元素，常用于语言代码。


```
/* 选择所有 `lang` 属性是 `en` 或者以 `en-` 开头的元素 */
[lang|="en"] {
  color: green;
}
```


### 5、[attribute^="value"]

选择属性值以指定值开头的元素。


```
/* 选择所有 `href` 属性以 `https` 开头的链接 */
[href^="https"] {
  text-decoration: none;
}
```


### 6、[attribute$="value"]


选择属性值以指定值结尾的元素。


```
/* 选择所有 src 属性以 .jpg 结尾的图片 */
[src$=".jpg"] {
  border: 2px solid blue;
}
```


### 7、[attribute*="value"]

选择属性值中包含指定值的元素。


```
/* 选择所有 `title` 属性中包含 `tutorial` 的元素 */
[title*="tutorial"] {
  font-style: italic;
}
```


通过属性选择器，你可以轻松选择元素并基于它们的属性设置特定样式，增加了灵活性和可维护性。


---


## 属性选择器


下面的例子是把包含标题（title）的所有元素变为蓝色：


## 实例


```css
[title]
{
    color:blue;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_attselector_att)


---


## 属性和值选择器


下面的实例改变了标题title='runoob'元素的边框样式:


## 实例


```css
[title=runoob]
{
    border:5px solid green;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_attselector_value)


---


## 属性和值的选择器 - 多值


下面是包含指定值的title属性的元素样式的例子，使用（~）分隔属性和值:


## 实例


```css
[title~=hello] { color:blue; }
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_attselector_valuelist_space)


下面是包含指定值的lang属性的元素样式的例子，使用（|）分隔属性和值:


## 实例


```css
[lang|=en] { color:blue; }
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_attselector_valuelist_hyphen)


---


## 表单样式


属性选择器样式无需使用class或id的形式:


## 实例


```css
input[type="text"]
{
    width:150px;
    display:block;
    margin-bottom:10px;
    background-color:yellow;
}
input[type="button"]
{
    width:120px;
    margin-left:35px;
    display:block;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_attselector_form)








	  AI 思考中...





			** [CSS 媒体类型](https://www.runoob.com/css-mediatypes.html)
			[CSS 总结](https://www.runoob.com/css-summary.html) **