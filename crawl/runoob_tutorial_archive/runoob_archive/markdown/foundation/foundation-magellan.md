# Foundation 麦哲伦（Magellan）导航

- Source: https://www.runoob.com/foundation/foundation-magellan.html

*

---


## 如何创建麦哲伦导航


麦哲伦导航就是一个导航索引，创建方式如下:


### 实例


```
<div data-magellan-expedition="fixed">  <dl class="sub-nav">
  <dd data-magellan-arrival="page1"><a href="#page1">Page 1</a></dd>
  <dd data-magellan-arrival="page2"><a href="#page2">Page 2</a></dd>
  </dl></div><h3 data-magellan-destination="page1">Page1</h3>
  <a name="page1"></a>...
  <h3 data-magellan-destination="page2">Page2</h3>
  <a name="page2"></a>...<!-- Initialize Foundation JS --><script>$(document).ready(function() {
  $(document).foundation();})</script>
```

**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_magellan)


### 实例解析


在  元素上添加 `data-magellan-expedition="fixed"` 属性来创建麦哲伦导航。


然后在 `: ` 或 `` 上添加 `data-magellan-arrival="value*"` 属性，后面添加一个与该属性值一样的链接(page1)。 使用 `data-magellan-destination="value"` 属性来控制麦哲伦导航的目标, 后面紧跟的 `` 元素添加 `name="*value*"` 属性。两个属性的值必须与 `data-magellan-arrival` 的值一致 (page1**)。 最后，初始化 Foundation JS ，用户在滚动页面时导航就会根据当前显示的内容自动切换。 --- ## 麦哲伦导航头部工具条 麦哲伦导航使用头部工具条实例： ### 实例
```
<div data-magellan-expedition="fixed">  <nav class="top-bar" data-topbar>
  ...    <section class="top-bar-section">
  <ul class="left">        <li data-magellan-arrival="page1"><a
  href="#page1">Page 1</a></li>
  <li data-magellan-arrival="page2"><a href="#page2">Page 2</a></li>
  </ul>    </section>  </nav></div><h3 data-magellan-destination="page1">Page1</h3>
  <a name="page1"></a>...
  <h3 data-magellan-destination="page2">Page2</h3>
  <a name="page2"></a>...
```
 ** [尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_magellan_topbar) --- ## 麦哲伦导航内边距 默认情况下，麦哲伦导航的 `` 元素有 10px 的内边距。可以使用 CSS 移除它： ### 实例
```
[data-magellan-expedition], [data-magellan-expedition-clone] {    padding: 0;}
```
 [尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_magellan_topbar2) --- ## 麦哲伦导航选项 使用 data-options 属性修改麦哲伦导航的设置, 例如 ``: | 名称 | 类型 | 默认 | 描述 | 实例 | | --- | --- | --- | --- | --- | | active_class | string | active | 指定激活链接的类 | 尝试一下 | | threshold | number | 0 | 指定导航在什么时候需要固定位置。会根据滚动条滚动计算，默认为 0 (auto)。 | 尝试一下 | | destination_threshold | number | 20 | 设该值设定了导航链接显示为激活（蓝色背景）时导航列表距离顶部的值。 | 尝试一下 | | fixed_top | number | 0 | 指定了导航条距离头部的像素值 | 尝试一下 | AI 思考中... ** [Foundation 滑动导航(Off-Canvas)](https://www.runoob.com/foundation-off-canvas.html) [Foundation 表单](https://www.runoob.com/foundation-forms.html) ** ### 点我分享笔记 ** 取消 * * 分享笔记 - 昵称昵称 (必填) - 邮箱邮箱 (必填) - 引用地址引用地址 **在线实例** ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

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