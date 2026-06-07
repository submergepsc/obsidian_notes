# Bootstrap 列表组

- Source: https://www.runoob.com/bootstrap/bootstrap-list-group.html

本章我们将讲解列表组。列表组件用于以列表形式呈现复杂的和自定义的内容。创建一个基本的列表组的步骤如下：


- 向元素  添加 class **.list-group**。
- 向  添加 class **.list-group-item**。


下面的实例演示了这点：


## 实例


```css
<ul class="list-group">
    <li class="list-group-item">免费域名注册</li>
    <li class="list-group-item">免费 Window 空间托管</li>
    <li class="list-group-item">图像的数量</li>
    <li class="list-group-item">24*7 支持</li>
    <li class="list-group-item">每年更新成本</li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-listgroup-basic)

结果如下所示：


	![基本的列表组](https://www.runoob.com/wp-content/uploads/2014/06/basiclistgroup_demo.jpg)


## 向列表组添加徽章


我们可以向任意的列表项添加徽章组件，它会自动定位到右边。只需要在  元素中添加 ** 即可。下面的实例演示了这点：


## 实例


```css
<ul class="list-group">
    <li class="list-group-item">免费域名注册</li>
    <li class="list-group-item">免费 Window 空间托管</li>
    <li class="list-group-item">图像的数量</li>
    <li class="list-group-item">
        <span class="badge">新</span>
        24*7 支持
    </li>
    <li class="list-group-item">每年更新成本</li>
    <li class="list-group-item">
        <span class="badge">新</span>
        折扣优惠
    </li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-listgroup-badges)

结果如下所示：


	![列表组中的徽章](https://www.runoob.com/wp-content/uploads/2014/06/badgeslistgroup_demo.jpg)


## 向列表组添加链接


通过使用锚标签代替列表项，我们可以向列表组添加链接。我们需要使用  代替  元素。下面的实例演示了这点：


## 实例


```css
<a href="#" class="list-group-item active">
    免费域名注册
</a>
<a href="#" class="list-group-item">24*7 支持</a>
<a href="#" class="list-group-item">免费 Window 空间托管</a>
<a href="#" class="list-group-item">图像的数量</a>
<a href="#" class="list-group-item">每年更新成本</a>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-listgroup-links)

结果如下所示：


	![列表组中的链接](https://www.runoob.com/wp-content/uploads/2014/06/linkslistgroup_demo.jpg)


## 向列表组添加自定义内容


我们可以向上面已添加链接的列表组添加任意的 HTML 内容。下面的实例演示了这点：


## 实例


```css
<div class="list-group">
    <a href="#" class="list-group-item active">
        <h4 class="list-group-item-heading">
            入门网站包
        </h4>
    </a>
    <a href="#" class="list-group-item">
        <h4 class="list-group-item-heading">
            免费域名注册
        </h4>
        <p class="list-group-item-text">
            您将通过网页进行免费域名注册。
        </p>
    </a>
    <a href="#" class="list-group-item">
        <h4 class="list-group-item-heading">
            24*7 支持
        </h4>
        <p class="list-group-item-text">
            我们提供 24*7 支持。
        </p>
    </a>
</div>
<div class="list-group">
    <a href="#" class="list-group-item active">
        <h4 class="list-group-item-heading">
            商务网站包
        </h4>
    </a>
    <a href="#" class="list-group-item">
        <h4 class="list-group-item-heading">
            免费域名注册
        </h4>
        <p class="list-group-item-text">
            您将通过网页进行免费域名注册。
        </p>
    </a>
    <a href="#" class="list-group-item">
        <h4 class="list-group-item-heading">24*7 支持</h4>
        <p class="list-group-item-text">我们提供 24*7 支持。</p>
    </a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-listgroup-customcontent)

结果如下所示：


	![列表组中的自定义内容](https://www.runoob.com/wp-content/uploads/2014/06/customcontentlistgroup_demo.jpg)


---


## 水平列表


上面实例中列表都是按垂直显示的，如果我们需要一个水平列表，可以通过以下代码实现：


## 实例


```css
.list-group-horizontal .list-group-item {
    display: inline-block;
}
.list-group-horizontal .list-group-item {
    margin-bottom: 0;
    margin-left:-4px;
    margin-right: 0;
}
.list-group-horizontal .list-group-item:first-child {
    border-top-right-radius:0;
    border-bottom-left-radius:4px;
}
.list-group-horizontal .list-group-item:last-child {
    border-top-right-radius:4px;
    border-bottom-left-radius:0;
}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-listgroup-horizontal)

结果如下所示：


	![列表组中的自定义内容](https://www.runoob.com/wp-content/uploads/2014/06/08748939-837B-4F72-AB13-057B9E79F984.jpg)








	  AI 思考中...





			** [Bootstrap 多媒体对象](https://www.runoob.com/bootstrap-media-object.html)
			[Bootstrap 面板](https://www.runoob.com/bootstrap-panels.html) **













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