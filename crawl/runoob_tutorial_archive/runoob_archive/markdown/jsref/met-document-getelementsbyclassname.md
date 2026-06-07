# HTML DOM getElementsByClassName() 方法

- Source: https://www.runoob.com/jsref/met-document-getelementsbyclassname.html

[![Document 对象参考手册](https://www.runoob.com/images/up.gif) Document 对象](https://www.runoob.com/dom-obj-document.html)


## 实例


获取所有指定类名的元素：


```
var x =
	document.getElementsByClassName("example");
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjsref_document_getelementsbyclassname)


---


## 定义和使用


getElementsByClassName() 方法返回文档中所有指定类名的元素集合，作为 NodeList 对象。


NodeList 对象代表一个有顺序的节点列表。NodeList 对象 我们可通过节点列表中的节点索引号来访问列表中的节点(索引号由0开始)。


提示：** 你可以使用 NodeList 对象的[length](https://www.runoob.com/prop-nodelist-length.html) 属性来确定指定类名的元素个数，并循环各个元素来获取你需要的那个元素。


---


## 浏览器支持


表格中的数字表示支持该方法的第一个浏览器的版本号。


| 方法 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| getElementsByClassName() | 4.0 | 9.0 | 3.0 | 3.1 | 9.5 |


---


## 语法


document.getElementsByClassName(*classname*)


## 参数


| 参数 | 类型 | Description |
| --- | --- | --- |
| classname | String | 必须。你需要获取的元素类名。 多个类名使用空格分隔，如 "test demo"。 |


## 技术描述


| DOM 版本: | Core Level 1 Document Object |
| --- | --- |
| 返回值： | NodeList 对象，表示指定类名的元素集合。元素在集合中的顺序以其在代码中的出现次序排序。 |


---


![实例](https://www.runoob.com/images/tryitimg.gif)

## 更多实例


## 实例


获取包含 "example" 和 "color" 类名的所有元素，并修改它的颜色:


```
var x =
	document.getElementsByClassName("example color");
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjsref_document_getelementsbyclassname2)


## 实例


查看文档中有多少个样式 class="example" 的元素 (使用 NodeList 对的 length 属性):


```
var x =
	document.getElementsByClassName("example").length;
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjsref_document_getelementsbyclassname_length)


## 实例


修改所有样式 class="example" 元素的背景颜色：


```
var x = document.getElementsByClassName("example");var i;for (i = 0;
	i < x.length; i++) {    x[i].style.backgroundColor =
	"red";}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjsref_document_getelementsbyclassname_loop)


---


## 相关页面


CSS 教程: [CSS 选择器](https://www.runoob.com/../css/css-selectors.html)


CSS 参考手册: [CSS *.class* 选择器](https://www.runoob.com/../cssref/sel-class.html)


HTML DOM 参考手册: [*element*.getElementsByClassName()](https://www.runoob.com/met-element-getelementsbyclassname.html)


HTML DOM 参考手册: [className 属性](https://www.runoob.com/prop-html-classname.html)


HTML DOM 参考手册: [HTML DOM classList 属性](https://www.runoob.com/prop-element-classlist.html)


HTML DOM 参考手册: [HTML DOM Style 对象](https://www.runoob.com/dom-obj-style.html)


---


[![Document 对象参考手册](https://www.runoob.com/images/up.gif) Document 对象](https://www.runoob.com/dom-obj-document.html)








	  AI 思考中...





			** [HTML DOM hasFocus() 方法](https://www.runoob.com/met-document-hasfocus.html)
			[HTML DOM getElementsByClassName() 方法](https://www.runoob.com/met-element-getelementsbyclassname.html) **













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

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

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