# Bootstrap 辅助类

- Source: https://www.runoob.com/bootstrap/bootstrap-helper-classes.html

本章将讨论 Bootstrap 中的一些可能会派上用场的辅助类。


## 文本


以下不同的类展示了不同的文本颜色。如果文本是个链接鼠标移动到文本上会变暗：


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .text-muted | "text-muted" 类的文本样式 | 尝试一下 |
| .text-primary | "text-primary" 类的文本样式 | 尝试一下 |
| .text-success | "text-success" 类的文本样式 | 尝试一下 |
| .text-info | "text-info" 类的文本样式 | 尝试一下 |
| .text-warning | "text-warning" 类的文本样式 | 尝试一下 |
| .text-danger | "text-danger" 类的文本样式 | 尝试一下 |


## 背景


以下不同的类展示了不同的背景颜色。 如果文本是个链接鼠标移动到文本上会变暗：


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .bg-primary | 表格单元格使用了 "bg-primary" 类 | 尝试一下 |
| .bg-success | 表格单元格使用了 "bg-success" 类 | 尝试一下 |
| .bg-info | 表格单元格使用了 "bg-info" 类 | 尝试一下 |
| .bg-warning | 表格单元格使用了 "bg-warning" 类 | 尝试一下 |
| .bg-danger | 表格单元格使用了 "bg-danger" 类 | 尝试一下 |


## 其他


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .pull-left | 元素浮动到左边 | 尝试一下 |
| .pull-right | 元素浮动到右边 | 尝试一下 |
| .center-block | 设置元素为 display:block 并居中显示 | 尝试一下 |
| .clearfix | 清除浮动 | 尝试一下 |
| .show | 强制元素显示 | 尝试一下 |
| .hidden | 强制元素隐藏 | 尝试一下 |
| .sr-only | 除了屏幕阅读器外，其他设备上隐藏元素 | 尝试一下 |
| .sr-only-focusable | 与 .sr-only 类结合使用，在元素获取焦点时显示(如：键盘操作的用户) | 尝试一下 |
| .text-hide | 将页面元素所包含的文本内容替换为背景图 | 尝试一下 |
| .close | 显示关闭按钮 | 尝试一下 |
| .caret | 显示下拉式功能 | 尝试一下 |


---


## 更多实例


### 关闭图标


使用通用的关闭图标来关闭模态框和警告框。使用 class **close** 得到关闭图标。


## 实例


```css
<p>关闭图标实例
  <button type="button" class="close" aria-hidden="true">
    &times;
  </button>
</p>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-helper-closeicon)


结果如下所示：


![关闭图标](https://www.runoob.com/wp-content/uploads/2014/06/1FF31647-9EE1-4B64-BE42-D248FDDAF876.jpg)


> **aria-hidden="true"** 主要是帮助残障人士（如失明）使用识读设备（自动读取内容并自动播放出来），播放到带此属性的内容时会自动跳过，以免残障人士混淆！


### 插入符


使用插入符表示下拉功能和方向。使用带有 class caret** 的  元素得到该功能。


## 实例


```css
<p>插入符实例
  <span class="caret"></span>
</p>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-helper-caret)


结果如下所示：


![插入符](https://www.runoob.com/wp-content/uploads/2014/06/caret_demo.jpg)


### 快速浮动


您可以分别使用 class pull-left** 或 **pull-right** 来把元素向左或向右浮动。下面的实例演示了这点。


## 实例


```css
<div class="pull-left">
  向左快速浮动
</div>
<div class="pull-right">
  向右快速浮动
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-helper-quickfloat)


结果如下所示：


![快速浮动](https://www.runoob.com/wp-content/uploads/2014/06/quickfloat_demo.jpg)


如需对齐导航栏中的组件，请使用 .navbar-left** 或 **.navbar-right** 代替。请查看 [Bootstrap 导航栏](https://www.runoob.com/bootstrap-navbar.html)。


### 内容居中


使用 class **center-block** 来居中元素。


## 实例


```css
<div class="row">
  <div class="center-block" style="width:200px;background-color:#ccc;">
    这是 center-block 实例
  </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-helper-centercontentblock)


结果如下所示：


![居中内容块](https://www.runoob.com/wp-content/uploads/2014/06/centercontentblock_demo.jpg)


### 清除浮动


如需清除元素的浮动，请使用 .clearfix** class。


## 实例


```css
<div class="clearfix"  style="background: #D8D8D8;border: 1px solid #000;padding: 10px;">
  <div class="pull-left" style="background:#58D3F7;">
    向左快速浮动
  </div>
  <div class="pull-right" style="background: #DA81F5;">
    向右快速浮动
  </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-helper-clearfix)


结果如下所示：


![清除浮动](https://www.runoob.com/wp-content/uploads/2014/06/clearfix_demo.jpg)


### 显示和隐藏内容


您可以通过使用 class .show** 和 **.hidden** 来强行设置元素显示或隐藏（包括屏幕阅读器）。


## 实例


```css
<div class="row" style="padding: 91px 100px 19px 50px;">
  <div class="show" style="margin-left:10px;width:300px;background-color:#ccc;">
    这是 show class 的实例
  </div>
  <div class="hidden" style="width:200px;background-color:#ccc;">
    这是 hide class 的实例
  </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-helper-showhide)


结果如下所示：


![显示和隐藏内容](https://www.runoob.com/wp-content/uploads/2014/06/showhide_demo.jpg)


### 屏幕阅读器


您可以通过使用 class .sr-only** 来把元素对所有设备隐藏，除了屏幕阅读器。


## 实例


```css
<div class="row" style="padding: 91px 100px 19px 50px;">
  <form class="form-inline" role="form">
    <div class="form-group">
      <label class="sr-only" for="email">Email 地址</label>
      <input type="email" class="form-control" placeholder="Enter email">
    </div>
    <div class="form-group">
      <label class="sr-only" for="pass">密码</label>
      <input type="password" class="form-control" placeholder="Password">
    </div>
  </form>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-helper-screenreader)


结果如下所示：


![屏幕阅读器](https://www.runoob.com/wp-content/uploads/2014/06/screenreader_demo.jpg)


在这里，我们看到两个 input 类型的 label 标签都带有 class sr-only**，因此标签将只对屏幕阅读器可见。








	  AI 思考中...





			** [Bootstrap 图片](https://www.runoob.com/bootstrap-images.html)
			[Bootstrap 响应式实用工具](https://www.runoob.com/bootstrap-responsive-utilities.html) **













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