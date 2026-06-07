# Bootstrap 徽章（Badges）

- Source: https://www.runoob.com/bootstrap/bootstrap-badges.html

本章将讲解 Bootstrap 徽章（Badges）。徽章与标签相似，主要的区别在于徽章的边角更加圆滑。


徽章（Badges）主要用于突出显示新的或未读的项。如需使用徽章，只需要把 **** 添加到链接、Bootstrap 导航等这些元素上即可。


下面的实例演示了这点：


## 实例


展示未读邮件：


```css
<a href="#">Mailbox <span class="badge">50</span></a>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-badges)


结果如下所示：


![徽章（Badges）](https://www.runoob.com/wp-content/uploads/2014/06/badges_demo.jpg)


当没有新的或未读的项时，通过 CSS 的 :empty** 选择器，徽章会折叠起来，表示里边没有内容。


## 实例


展示未读消息：


```css
<div class="container">
    <h2>徽章</h2>
    <p>.badge 类指定未读消息的数量:</p>
    <p><a href="#">收件箱 <span class="badge">21</span></a></p>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trybs_ref_comp_badge&basepath=0)


---


## 激活导航状态


您可以在激活状态的胶囊式导航和列表导航中放置徽章。通过使用 ** 来激活链接，如下面的实例所示：


## 实例


```css
<h4>胶囊式导航中的激活状态</h4>
<ul class="nav nav-pills">
    <li class="active">
        <a href="#">首页
            <span class="badge">42</span>
        </a>
    </li>
    <li>
        <a href="#">简介</a>
    </li>
    <li>
        <a href="#">消息
            <span class="badge">3</span>
        </a>
    </li>
</ul>
<br>
<h4>列表导航中的激活状态</h4>
<ul class="nav nav-pills nav-stacked" style="max-width: 260px;">
    <li class="active">
        <a href="#">
            <span class="badge pull-right">42</span>首页</a>
        </li>
    <li>
        <a href="#">简介</a>
    </li>
    <li>
        <a href="#">
            <span class="badge pull-right">3</span>消息
        </a>
    </li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-badges-activestate)


结果如下所示：


![激活导航状态](https://www.runoob.com/wp-content/uploads/2014/06/badgesactivestate_demo.jpg)









	  AI 思考中...





			** [Bootstrap 标签](https://www.runoob.com/bootstrap-labels.html)
			[Bootstrap 超大屏幕](https://www.runoob.com/bootstrap-jumbotron.html) **













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