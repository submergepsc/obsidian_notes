# JavaScript HTML DOM 节点列表

- Source: https://www.runoob.com/js/js-htmldom-nodelist.html

**NodeList** 对象是一个从文档中获取的节点列表 (集合) 。


NodeList 对象类似 [HTMLCollection](https://www.runoob.com/js-htmldom-elements.html) 对象。


一些旧版本浏览器中的方法（如：**getElementsByClassName()**）返回的是 NodeList 对象，而不是 HTMLCollection 对象。


所有浏览器的 **childNodes** 属性返回的是 NodeList 对象。


大部分浏览器的 **querySelectorAll()** 返回 NodeList 对象。


以下代码选取了文档中所有的  节点：


## 实例


```javascript
var myNodeList = document.querySelectorAll("p");
```


NodeList 中的元素可以通过索引(以 0 为起始位置)来访问。


访问第二个  元素可以是以下代码:


```javascript
y = myNodeList[1];
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_dom_nodelist)


---


## NodeList 对象 length 属性


NodeList 对象 length 属性定义了节点列表中元素的数量。


## 实例


```javascript
var myNodelist = document.querySelectorAll("p");
document.getElementById("demo").innerHTML = myNodelist.length;
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_dom_nodelist_length)


### 实例解析


获取  元素的集合：


```
var myNodelist = document.querySelectorAll("p");
```


显示节点列表的元素个数：


```
document.getElementById("demo").innerHTML = myNodelist.length;
```


length 属性常用于遍历节点列表。


## 实例


修改节点列表中所有  元素的背景颜色:


```javascript
var myNodelist = document.querySelectorAll("p");
var i;
for (i = 0; i < myNodelist.length; i++) {
    myNodelist[i].style.backgroundColor = "red";
}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_dom_nodelist_loop)


---


## HTMLCollection 与 NodeList 的区别


[HTMLCollection](https://www.runoob.com/js-htmldom-collections.html) 是 HTML 元素的集合。


NodeList 是一个文档节点的集合。


NodeList 与 HTMLCollection 有很多类似的地方。


NodeList 与 HTMLCollection 都与数组对象有点类似，可以使用索引 (0, 1, 2, 3, 4, ...) 来获取元素。


NodeList 与 HTMLCollection 都有 length 属性。


HTMLCollection 元素可以通过 name，id 或索引来获取。


NodeList 只能通过索引来获取。


只有 NodeList 对象有包含属性节点和文本节点。


> 节点列表不是一个数组！**
> 节点列表看起来可能是一个数组，但其实不是。
> 你可以像数组一样，使用索引来获取元素。
> 节点列表无法使用数组的方法： valueOf(), pop(), push(),
> 或 join() 。










	  AI 思考中...





			** [JavaScript HTML DOM 集合(Collection)](https://www.runoob.com/js-htmldom-collections.html)
			[JavaScript let 和 const](https://www.runoob.com/js-let-const.html) **