# Bootstrap5 表单浮动标签

- Source: https://www.runoob.com/bootstrap5/bootstrap5-form-floating-labels.html

默认情况下，标签内容一般显示在 input 输入框的上方：


![](https://www.runoob.com/wp-content/uploads/2022/02/436F03D1-1AFF-42E4-BC14-2B1BD219B0CD.jpg)

使用浮动标签，可以在 input 输入框内插入标签，在单击 input 输入框时使它们浮动到上方

![](https://www.runoob.com/wp-content/uploads/2022/02/E96D77B7-61C6-410A-9021-995D8E9697A6.jpg)


## Bootstrap 实例


```css
<div class="form-floating mb-3 mt-3">
  <input type="text" class="form-control" id="email" placeholder="Enter email" name="email">
  <label for="email">Email</label>
</div>

<div class="form-floating mt-3 mb-3">
  <input type="text" class="form-control" id="pwd" placeholder="Enter password" name="pswd">
  <label for="pwd">Password</label>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs_form_floating_labels)


注意事项：**  元素必须在  元素之后，并且每个  元素都需要 placeholder 属性。


## 文本框

文本框 textarea 也可以有浮动效果：


## Bootstrap 实例


```css
<div class="form-floating">
  <textarea class="form-control" id="comment" name="text" placeholder="Comment goes here"></textarea>
  <label for="comment">Comments</label>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs_form_textarea_floating_labels)


## 选择框


我们可以在选择菜单上使用浮动标签，它将始终显示在选择菜单的左上角，不会有点击浮动效果：


## Bootstrap 实例


```css
<div class="form-floating">
  <select class="form-select" id="sel1" name="sellist">
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
  </select>
  <label for="sel1" class="form-label">Select list (select one):</label>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs_form_select_floating_labels)








	  AI 思考中...





			** [Bootstrap5 输入框组](https://www.runoob.com/bootstrap5-form-input-group.html)
			[Bootstrap5 表单验证](https://www.runoob.com/bootstrap5-form-validation.html) **













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