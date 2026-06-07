# JavaScript HTML DOM 集合(Collection)

- Source: https://www.runoob.com/js/js-htmldom-collections.html

本章节介绍 DOM 集合的使用。


---


## HTMLCollection 对象



getElementsByTagName() 方法返回 [HTMLCollection](https://www.runoob.com/../jsref/dom-htmlcollection.html) 对象。


HTMLCollection 对象类似包含 HTML 元素的一个数组。


以下代码获取文档所有的  元素：


## 实例


```javascript
var x = document.getElementsByTagName("p");
```


集合中的元素可以通过索引(以 0 为起始位置)来访问。


访问第二个  元素可以是以下代码:


```javascript
y = x[1];
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_dom_htmlcollection)


---


## HTMLCollection 对象 length 属性


HTMLCollection 对象的 length 属性定义了集合中元素的数量。


## 实例


```javascript
var myCollection = document.getElementsByTagName("p");
document.getElementById("demo").innerHTML = myCollection.length;
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_dom_htmlcollection_length)


### 实例解析


获取  元素的集合：


```
var myCollection = document.getElementsByTagName("p");
```


显示集合元素个数：


```
document.getElementById("demo").innerHTML = myCollection.length;
```


集合 length 属性常用于遍历集合中的元素。


## 实例


修改所有  元素的背景颜色:


```javascript
var myCollection = document.getElementsByTagName("p");
var i;
for (i = 0; i < myCollection.length; i++) {
    myCollection[i].style.backgroundColor = "red";
}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_dom_htmlcollection_loop)


### 注意


HTMLCollection 不是一个数组！**


HTMLCollection 看起来可能是一个数组，但其实不是。


你可以像数组一样，使用索引来获取元素。


HTMLCollection 无法使用数组的方法： valueOf(), pop(), push(), 或 join() 。










	  AI 思考中...





			** [JavaScript 验证 API](https://www.runoob.com/js-validation-api.html)
			[JavaScript HTML DOM 节点列表](https://www.runoob.com/js-htmldom-nodelist.html) **