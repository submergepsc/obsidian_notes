# Bootstrap5 模态框

- Source: https://www.runoob.com/bootstrap5/bootstrap5-modal.html

模态框（Modal）是覆盖在父窗体上的子窗体。通常，目的是显示来自一个单独的源的内容，可以在不离开父窗体的情况下有一些互动。子窗体可提供信息交互等。


---


## 如何创建模态框


以下实例创建了一个简单的模态框效果 ：


## 实例


```css
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
  打开模态框
</button>

<!-- 模态框 -->
<div class="modal" id="myModal">
  <div class="modal-dialog">
    <div class="modal-content">

      <!-- 模态框头部 -->
      <div class="modal-header">
        <h4 class="modal-title">模态框标题</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>

      <!-- 模态框内容 -->
      <div class="modal-body">
        模态框内容..
      </div>

      <!-- 模态框底部 -->
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">关闭</button>
      </div>

    </div>
  </div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_modal)


---


## 添加动画


使用 .fade 类可以设置模态框弹出或关闭的效果:


## 实例


```css
<!-- 添加动画效果 -->
<div class="modal fade"></div>

<!-- 不使用动画效果 -->
<div class="modal"></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_modal_fade)


---


## 模态框尺寸


我们可以通过添加 **.modal-sm** 类来创建一个小模态框，**.modal-lg** 类可以创建一个大模态框。


尺寸类放在 ****元素的 **.modal-dialog** 类后 :


## 实例 - 小模态框


```css
<div class="modal-dialog modal-sm">
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_modal_sm)

## 实例 - 大模态框


```css
<div class="modal-dialog modal-lg">
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_modal_lg)

## 实例 - 超大模态框


```css
<div class="modal-dialog modal-xl">
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_modal_xl)

### 全屏幕显示


使用 **.modal-fullscreen** 类可以让模态框全屏幕显示:


## 实例 - 全屏幕显示


```css
<div class="modal-dialog modal-fullscreen">
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_modal_fullscreen)


使用 **.modal-fullscreen-*-*** 类可以控制在什么尺寸下全屏幕显示:


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .modal-fullscreen-sm-down | 576px 以下尺寸全屏幕显示 | 尝试一下 |
| .modal-fullscreen-md-down | 768px 以下尺寸全屏幕显示 | 尝试一下 |
| .modal-fullscreen-lg-down | 992px 以下尺寸全屏幕显示 | 尝试一下 |
| .modal-fullscreen-xl-down | 1200px 以下尺寸全屏幕显示 | 尝试一下 |
| .modal-fullscreen-xxl-down | 1400px 以下尺寸全屏幕显示 | 尝试一下 |


---


## 模态框居中显示


使用 **.modal-dialog-centered** 类可以设置模态框水平和垂直方向都居中显示:


## 实例


```css
<div class="modal-dialog modal-dialog-centered">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_modal_centered)


---


## 模态框滚动条


默认情况下模态框如果包含很多内容，页面会自动生成一个滚动，模态框随着页面的滚动而滚动:


## 实例


```css
<div class="modal-dialog">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_modal_scroll)

如果我们只想在模态框里头设置一个滚动条，可以使用 **.modal-dialog-scrollable** 类：


## 实例


```css
<div class="modal-dialog modal-dialog-scrollable">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_modal_scroll2)








	  AI 思考中...





			** [Bootstrap5 轮播](https://www.runoob.com/bootstrap5-carousel.html)
			[Bootstrap5 提示框](https://www.runoob.com/bootstrap5-tooltip.html) **













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