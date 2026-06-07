# ionic 表单和输入框

- Source: https://www.runoob.com/ionic/ionic-form-input.html

list 类同样可以用于 input 元素。item-input 和 item 类指定了文本框及其标签。


### 输入框属性：placeholder


以下实例中，默认为100%宽度（左右两侧没有边框），并使用 placeholder 属性设置输入字段预期值的提示信息。
```
<div class="list">
  <label class="item item-input">
    <input type="text" placeholder="First Name">
  </label>
  <label class="item item-input">
    <input type="text" placeholder="Last Name">
  </label>
  <label class="item item-input">
    <textarea placeholder="Comments"></textarea>
  </label>
</div>
```
 [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_item_input)


### 输入框属性：input-label


使用 input-label 将标签放置于输入框 input 的左侧。


```
<div class="list">
  <label class="item item-input">
    <span class="input-label">用户名：</span>
    <input type="text">
  </label>
  <label class="item item-input">
    <span class="input-label">密码：</span>
    <input type="password">
  </label>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_item_input-label)


---


## 堆叠标签


堆叠标签通常位于输入框的头部。每个选项使用 item-stacked-label 类指定。 每个输入框需要指定 input-label。以下实例也使用了 placeholder 属性来设置信息输入提示。


```
<div class="list">
  <label class="item item-input item-stacked-label">
    <span class="input-label">First Name</span>
    <input type="text" placeholder="John">
  </label>
  <label class="item item-input item-stacked-label">
    <span class="input-label">Last Name</span>
    <input type="text" placeholder="Suhr">
  </label>
  <label class="item item-input item-stacked-label">
    <span class="input-label">Email</span>
    <input type="text" placeholder="[email protected]">
  </label>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_item-stacked-label)


---


## 浮动标签


浮动标签类似于堆叠标签，但浮动标签有一个动画的效果，每个选项需要指定 item-floating-label 类，输入标签需要指定 input-label。


```
<div class="list">
  <label class="item item-input item-floating-label">
    <span class="input-label">First Name</span>
    <input type="text" placeholder="First Name">
  </label>
  <label class="item item-input item-floating-label">
    <span class="input-label">Last Name</span>
    <input type="text" placeholder="Last Name">
  </label>
  <label class="item item-input item-floating-label">
    <span class="input-label">Email</span>
    <input type="text" placeholder="Email">
  </label>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_item-floating-label)


---


## 内嵌表单


默认情况下每个输入域宽度都是100%，但我们可以使用 list list-inset 或 card 类设置表单的内边距(padding)， card 类带有阴影。


```
<div class="list list-inset">
  <label class="item item-input">
    <input type="text" placeholder="First Name">
  </label>
  <label class="item item-input">
    <input type="text" placeholder="Last Name">
  </label>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_item-input_list-inset)


---


## 内嵌输入域


使用 list-inset 设置内嵌实体列表。 使用 item-input-inset 样式可以内嵌一个按钮。


```
<div class="list">

  <div class="item item-input-inset">
    <label class="item-input-wrapper">
      <input type="text" placeholder="Email">
    </label>
    <button class="button button-small">
      Submit
    </button>
  </div>

</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_item-input-inset)


---


## 带图标的输入框


item-input 输入框可以很简单的添加图标。 图标可以在  前添加。


```
<div class="list list-inset">
  <label class="item item-input">
    <i class="icon ion-search placeholder-icon"></i>
    <input type="text" placeholder="Search">
  </label>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_item-input-search)


---


## 头部输入框


输入框可放置在头部，并可添加提交或取消按钮。


```
<div class="bar bar-header item-input-inset">
  <label class="item-input-wrapper">
    <i class="icon ion-ios-search placeholder-icon"></i>
    <input type="search" placeholder="搜索">
  </label>
  <button class="button button-clear">
    取消
  </button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_header_item-input-search)








	  AI 思考中...





			** [ionic 卡片](https://www.runoob.com/ionic-card.html)
			[ionic toggle(切换开关)](https://www.runoob.com/ionic-toggle.html) **













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