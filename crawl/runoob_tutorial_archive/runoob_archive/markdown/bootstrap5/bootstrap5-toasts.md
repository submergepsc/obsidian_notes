# Bootstrap5 消息弹窗(Toasts)

- Source: https://www.runoob.com/bootstrap5/bootstrap5-toasts.html

Bootstrap5 弹窗 (Toasts) 是一种轻量级的通知组件，用于在页面的角落或底部显示临时性的信息、通知或警告。

弹窗通常用于向用户显示短期消息，比如成功消息、错误消息、警告或其他通知。


弹窗可以在页面的不同位置显示，包括左上角、右上角、左下角、右下角以及页面底部中央。


### 如何创建弹窗

要创建弹窗可以使用 **.toast** 类，并在该类里添加 .toast-header 和 .toast-body 类来表示标题和内容。


**注意：**弹窗默认是关闭的，可以使用 **.show ** 来设置显示，关闭弹窗可以在 元素上添加 **data-bs-dismiss="toast"**:


## 实例


```css
<div class="toast show">
  <div class="toast-header">
    弹窗标题
    <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
  </div>
  <div class="toast-body">
    这是一个Bootstrap 5弹窗示例。
  </div>
</div>
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_toasts)


要通过点击按钮显示弹窗，您需要使用 JavaScript 对其进行初始化：通过 ID 获取指定元素的点击事件并调用 **toast()** 方法。


当点击按钮时，以下代码将显示页面中的所有 **toast** 类：


## 实例


```css
document.getElementById("toastbtn").onclick = function() {
  var toastElList = [].slice.call(document.querySelectorAll('.toast'))
  var toastList = toastElList.map(function(toastEl) {
    return new bootstrap.Toast(toastEl)
  })
  toastList.forEach(toast => toast.show())
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_toasts1)


将弹窗显示在右下角：


## 实例


```css
<div class="container mt-5">
    <button class="btn btn-primary" onclick="showToast()">显示弹窗</button>
</div>

<div class="position-fixed bottom-0 end-0 p-3">
    <div id="toast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
            <strong class="me-auto">Bootstrap Toast</strong>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            这是一个Bootstrap 5弹窗示例。
        </div>
    </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_toasts2)
设置多个消息弹窗：


## 实例


```css
<!--显示多个弹窗 -->

<div aria-live="polite" aria-atomic="true" class="position-relative">
    <!-- Position it: -->
    <!-- - `.toast-container` 设置弹窗直接的空隙 -->
    <!-- - `top-0` & `end-0` 设置弹窗显示位置-->
    <!-- - `.p-3` 设置外边距  -->
    <div class="toast-container top-0 end-0 p-3">

    <!-- 这里设置多个弹窗代码 -->
    <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
        <svg class="bd-placeholder-img rounded me-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#007aff"></rect></svg>
        <strong class="me-auto">弹窗实例</strong>
        <small class="text-muted">刚刚</small>
        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
        这是第二个消息
        </div>
    </div>

    <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
        <div class="toast-header">
        <svg class="bd-placeholder-img rounded me-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#007aff"></rect></svg>
        <strong class="me-auto">弹窗实例</strong>
        <small class="text-muted">2 秒前</small>
        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
        这是第一个消息
        </div>
    </div>
    </div>
</div>

<!-- 显示多个弹窗 结束 -->
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_toasts3)







	  AI 思考中...





			** [Bootstrap5 表单验证](https://www.runoob.com/bootstrap5-form-validation.html)














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