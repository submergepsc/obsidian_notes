# HTML 标签

- Source: https://www.runoob.com/tags/tag-template.html

**
## 实例


使用  标签在页面加载时该标签中的内容不会显示，加载后可以使用 JavaScript 来显示它：


```
<button onclick="showContent()">显示隐藏内容</button>

<template>
  <h2>logo</h2>
  <img src="https://static.jyshare.com/images/runoob-logo.png" >
</template>

<script>
function showContent() {
  var temp = document.getElementsByTagName("template")[0];
  var clon = temp.content.cloneNode(true);
  document.body.appendChild(clon);
}
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_template)


---


## 浏览器支持


表格中的数字表示支持该元素的第一个浏览器的版本号。


| 元素 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 26.0 | 13.0 | 22.0 | 8.0 | 15.0 |


---


## 标签定义及使用说明


 标签定义在页面加载时隐藏的一些内容，该标签中的内容可以稍后使用 JavaScript 呈现。


如果您有一些需要重复使用的 HTML 代码，则可以使用 `` 设置为公用的模板。


---


## 更多实例


## 实例


实例中的每个数组元素都使用一个新的 div 元素来填充网页。每个 div 元素的 HTML 代码都在 template 元素内：：


```
<template>
  <div class="myClass">我喜欢: </div>
</template>

<script>
var myArr = ["Google", "Runoob", "Taobao", "Wiki", "Zhihu", "Baidu"];
function showContent() {
  var temp, item, a, i;
  temp = document.getElementsByTagName("template")[0];
  item = temp.content.querySelector("div");
  for (i = 0; i < myArr.length; i++) {
    a = document.importNode(item, true);
    a.textContent += myArr[i];
    document.body.appendChild(a);
  }
}
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_template2)


## 实例


查看浏览器是否支持 template 标签：


```
if (document.createElement("template").content) {
  document.write("您的浏览器支持 template 标签！");
} else {
  document.write("您的浏览器不支持 template 标签！");
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml5_template3)


---


## 全局属性


 标签支持 [HTML 的全局属性](https://www.runoob.com/ref-standardattributes.html)。









	  AI 思考中...





			** [HTML source srcset 属性](https://www.runoob.com/att-source-srcset.html)
			[HTML 国家/地区参考手册](https://www.runoob.com/ref-country-codes.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/../skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/../skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/../skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/../skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/../skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/../skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/../skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)

      : · [免责声明](https://www.runoob.com/../disclaimer/index.html)

      : · [关于我们](https://www.runoob.com/../aboutus/index.html)

      : · [文章归档](https://www.runoob.com/../archives/index.html)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/../index/index.html)**
    **[runoob.com](https://www.runoob.com/../index/index.html)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **