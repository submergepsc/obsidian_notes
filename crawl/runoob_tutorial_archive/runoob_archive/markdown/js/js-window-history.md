# JavaScript Window History

- Source: https://www.runoob.com/js/js-window-history.html

---


window.history 对象包含浏览器的历史。


---


## Window History


**window.history**对象在编写时可不使用 window 这个前缀。


为了保护用户隐私，对 JavaScript 访问该对象的方法做出了限制。


一些方法：


- history.back() - 与在浏览器点击后退按钮相同
- history.forward() - 与在浏览器中点击向前按钮相同


---


## Window history.back()


history.back() 方法加载历史列表中的前一个 URL。


这与在浏览器中点击后退按钮是相同的：


## 实例


在页面上创建后退按钮：


```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<head>
<script>
function goBack()
{
    window.history.back()
}
</script>
</head>
<body>

<input type="button" value="Back" onclick="goBack()">

</body>
</html>
```


以上代码输出为：


```javascript

```


---


## Window history.forward()


history forward() 方法加载历史列表中的下一个 URL。


这与在浏览器中点击前进按钮是相同的：


## 实例


在页面上创建一个向前的按钮：


```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
function goForward()
{
    window.history.forward()
}
</script>
</head>
<body>

<input type="button" value="Forward" onclick="goForward()">

</body>
</html>
```


以上代码输出为：


```javascript

```










	  AI 思考中...





			** [JavaScript Window Location](https://www.runoob.com/js-window-location.html)
			[JavaScript Window Navigator](https://www.runoob.com/js-window-navigator.html) **