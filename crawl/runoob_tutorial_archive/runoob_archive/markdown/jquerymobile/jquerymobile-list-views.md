# jQuery Mobile 列表视图

- Source: https://www.runoob.com/jquerymobile/jquerymobile-list-views.html

---

*

**
---


## jQuery Mobile 列表视图


jQuery Mobile 中的列表视图是标准的HTML 列表; 有序() 和 无序().


列表视图是jQuery Mobile中功能强大的一个特性。它会使标准的无序或有序列表应用更广泛。应用方法就是在ul或ol标签中添加data-role="listview"属性。在每个项目()中添加链接，用户可以点击它：


## 实例


```javascript
<ol data-role="listview">  <li><a href="#">列表项m</a></li>
	</ol><ul data-role="listview">

	<li><a href="#">列表项</a></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_views)


列表样式的圆角和边缘，使用 data-inset="true" 属性设置:


## 实例


```javascript
<ul data-role="listview" data-inset="true">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_inset)


|  | 默认情况下，列表项的链接会自动变成一个按钮 (不需要 data-role="button")。 |
| --- | --- |


---


## 列表分隔


列表项也可以转化为列表分割项，用来组织列表，使列表项成组。


指定列表分割，给列表项元素添加 data-role="list-divider" 属性即可：


## 实例


```javascript
<ul data-role="listview"> <li data-role="list-divider">欧洲</li>
	<li><a href="#">法国</a></li>  <li><a href="#">德国</a></li>
	</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_dividers)


如果你有一个字母顺序排列的列表，（例如一个电话簿）通过  或者 元素的 data-autodividers="true" 属性设置可以配置为自动生成的项目的分隔:


## 实例


```javascript
<ul data-role="listview" data-autodividers="true">  <li><a href="#">Adele</a></li>
	<li><a href="#">Agnes</a></li>  <li><a href="#">Billy</a></li>
	<li><a href="#">Calvin</a></li>  ...</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_autodividers)


|  | data-autodividers="true" 可以配置为自动生成的项目的分隔。默认情况下，创建的分隔文本是列表项文本的第一个大写字母。 |
| --- | --- |


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[只读列表](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_readonly) 如何创建一个不带链接的列表 (不会是个按钮且不可点击)。


[面板](https://www.runoob.com/try/tryit.php?filename=tryjqmob_lists_panel) 如何在列表中插入面板








	  AI 思考中...





			* [jQuery Mobile 页面](https://www.runoob.com/jquerymobile-pages.html)
			[jQuery Mobile 列表内容](https://www.runoob.com/jquerymobile-list-content.html) **













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