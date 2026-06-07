# Bootstrap5 表单验证

- Source: https://www.runoob.com/bootstrap5/bootstrap5-form-validation.html

我们可以使用不同的验证类来设置表单的验证功能。


**.was-validated** 或 **.needs-validation** 添加到  元素中，input 输入字段将具有绿色（有效）或红色（无效）边框效果，用于说明表单是否需要输入内容。


**.valid-feedback** 或 **.invalid-feedback** 类用来告诉用户缺少什么信息，或者在提交表单之前需要完成什么。


## 实例


使用 .was-validated 类显示表单在提交之前需要填写的内容：


```css
<form action="" class="was-validated">
  <div class="form-group">
    <label for="uname">Username:</label>
    <input type="text" class="form-control" id="uname" placeholder="Enter username" name="uname" required>
    <div class="valid-feedback">验证成功！</div>
    <div class="invalid-feedback">请输入用户名！</div>
  </div>
  <div class="form-group">
    <label for="pwd">Password:</label>
    <input type="password" class="form-control" id="pwd" placeholder="Enter password" name="pswd" required>
    <div class="valid-feedback">验证成功！</div>
    <div class="invalid-feedback">请输入密码！</div>
  </div>
  <div class="form-group form-check">
    <label class="form-check-label">
      <input class="form-check-input" type="checkbox" name="remember" required> 同意协议
      <div class="valid-feedback">验证成功！</div>
      <div class="invalid-feedback">同意协议才能提交。</div>
    </label>
  </div>
  <button type="submit" class="btn btn-primary">提交</button>
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_validation_was)


## 实例


使用 .needs-validation，它将在表单提交之后验证缺少的内容。这里需要添加一些 JavaScript 代码才能使代码正常工作：


```css
<form action="" class="needs-validation" novalidate>
  <div class="form-group">
    <label for="uname">Username:</label>
    <input type="text" class="form-control" id="uname" placeholder="Enter username" name="uname" required>
    <div class="valid-feedback">验证成功！</div>
    <div class="invalid-feedback">请输入用户名！</div>
  </div>
  <div class="form-group">
    <label for="pwd">Password:</label>
    <input type="password" class="form-control" id="pwd" placeholder="Enter password" name="pswd" required>
    <div class="valid-feedback">验证成功！</div>
    <div class="invalid-feedback">请输入密码！</div>
  </div>
  <div class="form-group form-check">
    <label class="form-check-label">
      <input class="form-check-input" type="checkbox" name="remember" required> 同意协议
      <div class="valid-feedback">验证成功！</div>
      <div class="invalid-feedback">同意协议才能提交。</div>
    </label>
  </div>
  <button type="submit" class="btn btn-primary">提交</button>
</form>

<script>
// 如果验证不通过禁止提交表单
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // 获取表单验证样式
    var forms = document.getElementsByClassName('needs-validation');
    // 循环并禁止提交
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();
</script>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs5_form_validation_needs)







	  AI 思考中...





			** [Bootstrap5 表单浮动标签](https://www.runoob.com/bootstrap5-form-floating-labels.html)
			[Bootstrap5 消息弹窗(Toasts)](https://www.runoob.com/bootstrap5-toasts.html) **













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