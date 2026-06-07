# Bootstrap5 复选框与单选框

- Source: https://www.runoob.com/bootstrap5/bootstrap5-form-check-radio.html

如果您希望用户从预设选项列表中选择任意数量的选项，可以使用复选框：


![](https://www.runoob.com/wp-content/uploads/2022/02/C3F06C67-DE9C-4060-8C85-F598E562C52F.jpg)


## 实例


```css
<div class="form-check">
  <input class="form-check-input" type="checkbox" id="check1" name="option1" value="something" checked>
  <label class="form-check-label">Option 1</label>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_form_check)

复选框通过使用 class="form-check" 来确保标签和复选框有适当边距。

.form-check-label 类添加到标签元素，.form-check 容器内添加 .form-check-input 类来设置复选框的样式。


checked 属性用于设置默认选中的选项。

## 单选框


如果您希望用户从预设选项列表中选择一个选项，可以使用单选框：


![](https://www.runoob.com/wp-content/uploads/2022/02/7FDE4661-A6DE-4456-8253-3739E702CBF0.jpg)


## 实例


```css
<div class="form-check">
  <input type="radio" class="form-check-input" id="radio1" name="optradio" value="option1" checked>Option 1
  <label class="form-check-label" for="radio1"></label>
</div>
<div class="form-check">
  <input type="radio" class="form-check-input" id="radio2" name="optradio" value="option2">Option 2
  <label class="form-check-label" for="radio2"></label>
</div>
<div class="form-check">
  <input type="radio" class="form-check-input" disabled>Option 3
  <label class="form-check-label"></label>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_form_radio)

## 切换开关


如果你想把复选框变成一个可切换的开关，可以在 .form-check** 容器内使用 **.form-switch** 类:


![](https://www.runoob.com/wp-content/uploads/2022/02/75BDEBD9-2649-42C3-8EF8-A67984588B13.jpg)


## 实例


```css
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" id="mySwitch" name="darkmode" value="yes" checked>
  <label class="form-check-label" for="mySwitch">Dark Mode</label>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_form_switch)







	  AI 思考中...





			** [Bootstrap5 下拉菜单](https://www.runoob.com/bootstrap5-form-select.html)
			[Bootstrap5 选择区间](https://www.runoob.com/bootstrap5-form-range.html) **













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