# jQuery Mobile 过渡

- Source: https://www.runoob.com/jquerymobile/jquerymobile-transitions.html

---


jQuery Mobile 包含 CSS3 效果让您选择页面打开的方式。


---


## jQuery Mobile 页面切换效果


jQuery Mobile 提供了各种页面切换到下一个页面的效果。


**注意：**为了实现页面切换效果，浏览器必须支持 CSS3 3D 切换：


|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 12.0 | 10.0 | 16.0 | 4.0 | 15.0 |


表格中的数字为支持 3D 旋转的最小浏览器版本号。


页面过渡效果可被应用于任何使用 data-transition 属性的链接或表单：


页面切换效果可被应用于任何使用 data-transition 属性的链接或表单提交：


```
<a href="#anylink" data-transition="slide">切换到第二个页面</a>
```


下面的表格显示了通过使用 data-transition 属性后可用的页面切换：


| 过渡 | 描述 | 页面 | 对话框 |
| --- | --- | --- | --- |
| fade | 默认。淡入到下一页 | 尝试一下 | 尝试一下 |
| flip | 从后向前翻转到下一页 | 尝试一下 | 尝试一下 |
| flow | 抛出当前页，进入下一页 | 尝试一下 | 尝试一下 |
| pop | 像弹出窗口那样转到下一页。 | 尝试一下 | 尝试一下 |
| slide | 从右向左滑动到下一页。 | 尝试一下 | 尝试一下 |
| slidefade | 从右向左滑动并淡入到下一页。 | 尝试一下 | 尝试一下 |
| slideup | 从下到上滑动到下一页。 | 尝试一下 | 尝试一下 |
| slidedown | 从上到下滑动到下一页。 | 尝试一下 | 尝试一下 |
| turn | 转向下一页。 | 尝试一下 | 尝试一下 |
| none | 无过渡效果。 | 尝试一下 | 尝试一下 |

**
|  | 在 jQuery Mobile 的所有链接上，默认使用淡入淡出的效果（如果浏览器支持）。 |
| --- | --- |


提示：**上面的所有效果支持后退行为。例如，如果您想要页面从左向右滑动，而不是从右向左滑动，请使用带有 "reverse" 值的 data-direction 属性。在后退按钮上这是默认的。


## 实例


```javascript
<a href="#pagetwo" data-transition="slide"
	data-direction="reverse">切换</a>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_trans_reverse)








	  AI 思考中...





			** [jQuery Mobile 列表内容](https://www.runoob.com/jquerymobile-list-content.html)
			[jQuery Mobile 按钮](https://www.runoob.com/jquerymobile-buttons.html) **













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