# Foundation 滑动导航(Off-Canvas)

- Source: https://www.runoob.com/foundation/foundation-off-canvas.html

---


## 侧边栏导航


Off-Canvas 滑动导航现在逐渐在移动页面变得越来越流行了 (点击菜单按钮菜单从左侧滑出):

*

---


## 创建滑动导航


创建滑动导航实例如下：


### 实例


```
<!-- 最外层div：页面布局 --><div class="off-canvas-wrap"
	data-offcanvas>  <!-- 内部元素: "工具栏" 内容 (图标, 链接,
	描述内容等)-->  <div class="inner-wrap">
	<nav class="tab-bar">      <section
	class="left-small">        <a
	class="left-off-canvas-toggle menu-icon" href="#"><span></span></a>
	</section>      <section class="middle
	tab-bar-section">        <h1
	class="title">Off-canvas Example</h1>
	</section>    </nav>    <!-- 滑动菜单 -->    <aside
	class="left-off-canvas-menu">      <!-- Add
	links or other stuff here -->      <ul
	class="off-canvas-list test">
	<li><label>Heading</label></li>
	<li><a href="#">Link 1</a></li>
	<li><a href="#">Link 2</a></li>
	...      </ul>    </aside>
	    <!-- 主要内容 -->    <section
	class="main-section">      <h3>Lorem Ipsum</h3>
	<p>....</p>    </section>    <!--
	关闭菜单 -->    <a
	class="exit-off-canvas"></a>  </div> <!-- 结束内部内容 -->
	</div> <!-- 结束滑动菜单 --><!-- 初始化 Foundation JS --><script>
	$(document).ready(function() {
	$(document).foundation();})
	</script>
```

**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_off-canvas)









	  AI 思考中...





			* [Foundation 侧边栏](https://www.runoob.com/foundation-sidenav.html)
			[Foundation 麦哲伦（Magellan）导航](https://www.runoob.com/foundation-magellan.html) **













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