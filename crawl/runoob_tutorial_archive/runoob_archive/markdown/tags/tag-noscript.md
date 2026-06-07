# HTML 标签

- Source: https://www.runoob.com/tags/tag-noscript.html

**
## 实例


 标签的使用：


```
<script>
document.write("Hello World!")
</script>
<noscript>抱歉，你的浏览器不支持 JavaScript!</noscript>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_noscript)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif) ![Firefox](https://www.runoob.com/images/compatible_firefox.gif) ![Opera](https://www.runoob.com/images/compatible_opera.gif) ![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif) ![Safari](https://www.runoob.com/images/compatible_safari.gif)


目前大多数浏览器支持  标签。


---


## 标签定义及使用说明


noscript 元素用来定义在脚本未被执行时的替代内容（文本）。


此标签可被用于可识别  标签但无法支持其中的脚本的浏览器。

---


## 提示和注释


提示：**如果浏览器支持脚本，那么它不会显示出 noscript 元素中的文本。


**注释：**无法识别  标签的浏览器会把标签的内容显示到页面上。为了避免浏览器这样做，您应当在注释标签中隐藏脚本。老式的（无法识别  标签的）浏览器会忽略注释，这样就不会把标签的内容写到页面上，而新式的浏览器则懂得执行这些脚本，即使它们被包围在注释标签中！


```
<script>
<!--
function displayMsg()
{
    alert("Hello World!")
}
//-->
</script>
```


---


## 在HTML 4.01 与 HTML5 之间的差异


在 HTML 4.01 中， 标签只允许插入到  元素中。


在 HTML5 中， 标签可以插入到  和  区域中。


---


## 在HTML 与 XHTML 之间的差异


XHTML 不支持  标签。

---


## 全局属性


 标签支持全局属性，查看完整属性表 [HTML全局属性](https://www.runoob.com/ref-standardattributes.html)。

---


## 相关文章


HTML 教程：[HTML 脚本](https://www.runoob.com/../html/html-scripts.html)








	  AI 思考中...





			** [HTML  标签](https://www.runoob.com/tag-object.html)
			[HTML  标签](https://www.runoob.com/tag-noframes.html) **