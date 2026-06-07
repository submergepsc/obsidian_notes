# DOM HTMLCollection

- Source: https://www.runoob.com/jsref/dom-htmlcollection.html

HTMLCollection 是 HTML 元素的集合。


HTMLCollection 对象类似一个包含 HTML 元素的数组列表。


[getElementsByTagName()](https://www.runoob.com/met-element-getelementsbytagname.html) 方法返回的就是一个 HTMLCollection 对象。


---


## 属性和方法


下表列出了 HTMLCollection 对象中的属性和方法：


| 属性 / 方法 | 描述 |
| --- | --- |
| item() | 返回 HTMLCollection 中指定索引的元素。 |
| length | 返回 HTMLCollection 中元素的数量。 |
| namedItem() | 返回 HTMLCollection 中指定 ID 或 name 属性的元素。 |


---


## 实例


返回所有 p 元素的集合，该集合是一个 HTMLCollection 对象：


## 实例


```
var x = document.getElementsByTagName("p");
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_htmlcollection1)


计算文档中 p 元素的数量：


## 实例


```
var x = document.getElementsByTagName("P");
document.write(x.length);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_htmlcollection2)


循环输出 HTMLCollection 对象中的所有元素：


## 实例


```
var x, i, l;
x = document.getElementsByTagName("*");
l = x.length;
for (i = 0; i < l; i++) {
  document.write(x[i].tagName + "<br>");
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_htmlcollection3)










	  AI 思考中...





			** [HTML DOM children 属性](https://www.runoob.com/prop-element-children.html)
			[HTMLCollection item() 方法](https://www.runoob.com/met-htmlcollection-item.html) **













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