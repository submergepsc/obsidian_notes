# Foundation Joyride

- Source: https://www.runoob.com/foundation/foundation-joyride.html

Joyride 是一个功能向导的 JavaScript 效果，创建实例如下：


### 实例


```
<!-- Elements that control the tour stops --><h3 id="first">First
	stop!</h3><h3 id="second">Second stop!</h3>
	<!-- The joyride: must be placed at the bottom of your page, but inside
	<body> --><ol class="joyride-list" data-joyride>  <li data-id="first">
	<p>First stop. The ride has begun!</p>  </li>  <li data-id="second">
	<h4>Second Stop</h4>    <p>Any valid HTML will work
	inside the Joyride.</p>  </li>  <li data-button="End">
	<h4>End Stop</h4>    <p>The tour is over. You can either
	go back to the previous stop or close it.</p>  </li></ol>
	<!-- Start Joyride Upon Initialization --><script>
	$(document).ready(function() {    $(document).foundation('joyride',
	'start');})
	</script>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_joyride)


### 实例解析


以上实例中，我们创建了两个元素，每个元素都有独立的 ID。 两个元素设置了 joyride 开始和结束的位置。


我们在 `` 或 `` 元素上添加 `data-joyride` 属性和 `.joyride-list` 类来创建 joyride。你需要在文档头部定义它 (在 `` 内的头部)。在每个列表上使用 `` 元素，每个元素添加 `data-id="*value*"` 属性。属性的 *value* 必须与之前元素的 id 相同。所以第一个功能导航 `` 元素使用 id="first" 必须与  元素的 data-id="first" 值一致。


如果你没有管理停止的 id，将显示一个模态框。


最后，Joyride 需要使用 JavaScript 初始化它，代码为： `$(document).foundation('joyride', 'start');`








	  AI 思考中...





			** [Foundation 模态框](https://www.runoob.com/foundation-modal.html)
			[Foundation 均衡器(Equalizer)](https://www.runoob.com/foundation-equalizer.html) **













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