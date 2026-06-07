# Bootstrap 插件概览

- Source: https://www.runoob.com/bootstrap/bootstrap-plugins-overview.html

在前面 **布局组件** 章节中所讨论到的组件仅仅是个开始。Bootstrap 自带 12 种 jQuery 插件，扩展了功能，可以给站点添加更多的互动。即使您不是一名高级的 JavaScript 开发人员，您也可以着手学习 Bootstrap 的 JavaScript 插件。利用 Bootstrap 数据 API（Bootstrap Data API），大部分的插件可以在不编写任何代码的情况下被触发。


站点引用 Bootstrap 插件的方式有两种：


- **单独引用**：使用 Bootstrap 的个别的 **.js* 文件。一些插件和 CSS 组件依赖于其他插件。如果您单独引用插件，请先确保弄清这些插件之间的依赖关系。
- **编译（同时）引用**：使用 *bootstrap.js* 或压缩版的 *bootstrap.min.js*。![](https://www.runoob.com/images/quote.png)不要尝试同时引用这两个文件，因为 *bootstrap.js* 和 *bootstrap.min.js* 都包含了所有的插件。

***所有的插件依赖于 jQuery。所以必须在插件文件之前引用 jQuery。请访问 [bower.json](https://github.com/twbs/bootstrap/blob/v3.0.2/bower.json) 查看 Bootstrap 当前支持的 jQuery 版本。***


## data 属性


- 你可以仅仅通过 data 属性 API 就能使用所有的 Bootstrap 插件，无需写一行 JavaScript 代码。这是 Bootstrap 中的一等 API，也应该是你的首选方式。
- 话又说回来，在某些情况下可能需要将此功能关闭。因此，我们还提供了关闭 data 属性 API 的方法，即解除以 *data-api* 为命名空间并绑定在文档上的事件。就像下面这样：
```
$(document).off('.data-api')
```

- 如需关闭一个特定的插件，只需要在 data-api 命名空间前加上该插件的名称作为命名空间即可，如下所示：
```
$(document).off('.alert.data-api')
```


## 编程方式的 API


我们为所有 Bootstrap 插件提供了纯 JavaScript 方式的 API。所有公开的 API 都是支持单独或链式调用方式，并且返回其所操作的元素集合（注：和jQuery的调用形式一致）。例如：


```
$(".btn.danger").button("toggle").addClass("fat")
```


所有的方法都可以接受一个可选的选项对象作为参数，或者一个代表特定方法的字符串，或者不带任何参数（这种情况下，将会初始化插件为默认行为），如下所示：


```
// 初始化为默认行为
$("#myModal").modal()
 // 初始化为不支持键盘
$("#myModal").modal({ keyboard: false })
// 初始化并立即调用 show
$("#myModal").modal('show')
```


每个插件在 **Constructor** 属性上也暴露了其原始的构造函数：*$.fn.popover.Constructor*。如果您想获取某个特定插件的实例，可以直接通过页面元素获取：


```
$('[rel=popover]').data('popover').
```


## 避免命名空间冲突


某些时候 Bootstrap 插件可能需要与其他 UI 框架一起使用。在这种情况下，可能会发生命名空间冲突。如果不幸发生了这种情况，你可以通过调用插件的 **.noConflict** 方法恢复其原始值。


```
// 返回 $.fn.button 之前所赋的值
var bootstrapButton = $.fn.button.noConflict()
// 为 $().bootstrapBtn 赋予 Bootstrap 功能
$.fn.bootstrapBtn = bootstrapButton
```


## 事件


Bootstrap 为大多数插件的独特行为提供了自定义事件。一般来说，这些事件有两种形式：


- **动词不定式**：这会在事件开始时被触发。例如 *ex: show*。动词不定式事件提供了 *preventDefault* 功能。这使得在事件开始前可以停止操作的执行。
```
$('#myModal').on('show.bs.modal', function (e) {
// 阻止模态框的显示
  if (!data) return e.preventDefault()
})
```

- **过去分词形式**：这会在动作执行完毕之后被触发。例如 *ex: shown*。








	  AI 思考中...





			** [Bootstrap Well](https://www.runoob.com/bootstrap-wells.html)
			[Bootstrap 过渡效果（Transition）插件](https://www.runoob.com/bootstrap-transition-plugin.html) **













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