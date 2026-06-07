# HTML 标签

- Source: https://www.runoob.com/tags/tag-form.html

## 实例


带有两个输入字段和一个提交按钮的 HTML 表单：


```
<form action="demo_form.php" method="get">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="提交">
</form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_form_submit)
（更多实例见页面底部）


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif) ![Firefox](https://www.runoob.com/images/compatible_firefox.gif) ![Opera](https://www.runoob.com/images/compatible_opera.gif) ![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif) ![Safari](https://www.runoob.com/images/compatible_safari.gif)


所有主流浏览器都支持  标签。


---


## 标签定义及使用说明


 标签用于创建供用户输入的 HTML 表单。


 元素包含一个或多个如下的表单元素：


-
-
-
-
-
-
-
-


---


## HTML 4.01 与 HTML5之间的差异


HTML5 新增了两个新的属性：autocomplete 和 novalidate，同时不再支持 HTML 4.01 中的某些属性。


---


## HTML 与 XHTML 之间的差异


在 XHTML 中，name 属性已被废弃。使用全局 id 属性代替。


---


## 属性


New ：HTML5 中的新属性。


| 属性 | 值 | 描述 |
| --- | --- | --- |
| accept | MIME_type | HTML5 不支持。规定服务器接收到的文件的类型。（文件是通过文件上传提交的） |
| accept-charset | character_set | 规定服务器可处理的表单数据字符集。 |
| action | URL | 规定当提交表单时向何处发送表单数据。 |
| autocompleteNew | onoff | 规定是否启用表单的自动完成功能。 |
| enctype | application/x-www-form-urlencoded multipart/form-data text/plain | 规定在向服务器发送表单数据之前如何对其进行编码。（适用于 method="post" 的情况） |
| method | get post | 规定用于发送表单数据的 HTTP 方法。 |
| name | text | 规定表单的名称。 |
| novalidateNew | novalidate | 如果使用该属性，则提交表单时不进行验证。 |
| target | _blank _self _parent _top | 规定在何处打开 action URL。 |


---


## 全局属性


 标签支持 [HTML 的全局属性](https://www.runoob.com/ref-standardattributes.html)。


---


## 事件属性


 标签支持 [HTML 的事件属性](https://www.runoob.com/ref-eventattributes.html)。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)

## 尝试一下 - 实例


[带有复选框的表单](https://www.runoob.com/try/try.php?filename=tryhtml_form_checkbox) 此表单包含两个复选框和一个提交按钮。


[带有单选按钮的表单](https://www.runoob.com/try/try.php?filename=tryhtml_form_radio) 此表单包含两个单选框和一个提交按钮。


---


## 相关文章


HTML 教程：[HTML 表单和输入](https://www.runoob.com/html-forms.html)


HTML DOM 参考手册： [Form 对象](https://www.runoob.com/../jsref/dom-obj-form.html)








	  AI 思考中...





			** [HTML  标签](https://www.runoob.com/tag-footer.html)
			[HTML  标签](https://www.runoob.com/tag-frame.html) **