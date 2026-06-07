# HTML Emoji

- Source: https://www.runoob.com/tags/html-emoji.html

Emoji 是来自 UTF-8 字符集的字符: 😄 😍 💗。


表情符号（英语：emoji，日语：絵文字／えもじ emoji），是使用在网页和聊天中的形意符号，最初是日本在无线通信中所使用的视觉情感符号（图画文字）。表情意指面部表情，图标则是图形标志的意思，可用来代表多种表情，如笑脸表示笑、蛋糕表示食物等。 Emoji 看起来像一张图片或图标，其实不是。


Emoji 实际上是 UTF-8 (Unicode) 字符集上的字符。


UTF-8 几乎涵盖了世界上所有的字符和符号。


### HTML charset 属性

想要正常显示一个 HTML 页面，浏览器就需要知道网页使用的字符集。
网页中的字符集使用 [](https://www.runoob.com/tag-meta.html) 标签来指定：


```
<meta charset="UTF-8">
```


**

注：**如果我们没有刻意指定 meta 属性，默认的字符集编码也是 UTF-8。

更多 UTF-8 编码可以参考：[HTML Unicode（UTF-8） 参考手册](https://www.runoob.com/../charsets/ref-html-utf8.html)

## UTF-8 字符


很多 UTF-8 字符无法在键盘上输入，但我们可以使用数字（称为实体编号）来表示：


- A 为 65
- B 为 66
- C 为 67


## 实例


```
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>

<p>显示结果： A B C</p>
<p>显示结果： &#65; &#66; &#67;</p>

</body>
</html>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_emoji)


实例解析：**

**** 定义来字符集。


A, B, 和 C 也可以使用 65, 66, 和 67 来表示。


实体编号需要以 &#