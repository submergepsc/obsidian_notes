# Bootstrap4 自定义表单

- Source: https://www.runoob.com/bootstrap4/bootstrap4-forms-custom.html

Bootstrap4 可以自定义一些表单的样式来替换浏览器默认的样式。


---


## 自定义复选框


如果要自定义一个复选框，可以设置 **** 为父元素，类为 **.custom-control** 和 **.custom-checkbox**，复选框作为子元素放在该 **** 里头，然后复选框设置为 **type="checkbox"**，类为 **.custom-control-input**。


复选框的文本使用 **label** 标签，标签使用 **.custom-control-label** 类，**label** 的 **for** 属性值需要匹配复选框的 id。


## Bootstrap4 实例


```css
<form>
  <div class="custom-control custom-checkbox">
    <input type="checkbox" class="custom-control-input" id="customCheck" name="example1">
    <label class="custom-control-label" for="customCheck">自定义复选框</label>
  </div>
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_form_custom_checkbox)


---


## 自定义单选框


如果要自定义一个单选框，可以设置 ** 为父元素，类为 **.custom-control** 和 **.custom-radio**，单选框作为子元素放在该 **** 里头，然后单选框设置为 **type="radio"**，类为 **.custom-control-input**。


单选框的文本使用 **label** 标签，标签使用 **.custom-control-label** 类，**label** 的 **for** 属性值需要匹配单选框的 **id**。


## Bootstrap4 实例


```css
<form>
  <div class="custom-control custom-radio">
    <input type="radio" class="custom-control-input" id="customRadio" name="example1" value="customEx">
    <label class="custom-control-label" for="customRadio">自定义单选框</label>
  </div>
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_form_custom_radio)


---


## 自定义控件显示在同一行


我们可以在外部元素上使用 **.custom-control-inline** 类来包裹自定义表单控件，这样自定义表单控件就能显示在同一行：


## Bootstrap4 实例


```css
<form>
  <div class="custom-control custom-radio custom-control-inline">
    <input type="radio" class="custom-control-input" id="customRadio" name="example" value="customEx">
    <label class="custom-control-label" for="customRadio">自定义单选框 1</label>
  </div>
  <div class="custom-control custom-radio custom-control-inline">
    <input type="radio" class="custom-control-input" id="customRadio2" name="example" value="customEx">
    <label class="custom-control-label" for="customRadio2">自定义单选框 2</label>
  </div>
</form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_form_custom_inline)


---


## 自定义选择菜单


创建自定义选择菜单可以在 ** 元素上添加 **.custom-select** 类:


## Bootstrap4 实例


```css
<form>
  <select name="cars" class="custom-select-sm">
    <option selected>自定义选择菜单</option>
    <option value="Google">Google</option>
    <option value="Runoob">Runoob</option>
    <option value="Taobao">Taobao</option>
  </select>
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_form_custom_select)


如果我们要设置自定义选择菜单大小，可以使用 **.custom-select-sm**、**.custom-select-lg** 来设置它们的大小:


## Bootstrap4 实例


```css
<form>
  <!-- 小 -->
  <select name="cars" class="custom-select-sm">
    <option selected>比较小的自定义选择菜单</option>
    <option value="Google">Google</option>
    <option value="Runoob">Runoob</option>
    <option value="Taobao">Taobao</option>
  </select>

  <!-- 大 -->
  <select name="cars" class="custom-select-lg">
    <option selected>比较大的自定义选择菜单</option>
    <option value="Google">Google</option>
    <option value="Runoob">Runoob</option>
    <option value="Taobao">Taobao</option>
  </select>
</form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_form_custom_select_size)


---


## 自定义滑块控件


我们可以在 input** 为 **type="range"** 的输入框中添加 **.custom-range** 类来设置自定义滑块控件:


## Bootstrap4 实例


```css
<form>
  <label for="customRange">自定义滑块控件</label>
  <input type="range" class="custom-range" id="customRange" name="points1">
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_form_custom_range)


---

## 自定义文件上传控件


我们可以在父元素添加 .custom-file** 类，然后在 **input** 设置为 **type="file"** 并添加 **.custom-file-input**:


上传控件的文本使用 **label** 标签，标签使用 **.custom-file-label** 类，**label** 的 **for** 属性值需要匹配上传控件 **id**。


## Bootstrap4 实例


```css
<form>
  <div class="custom-file">
    <input type="file" class="custom-file-input" id="customFile">
    <label class="custom-file-label" for="customFile">选择文件</label>
  </div>
</form>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_form_custom_file)








	  AI 思考中...





			** [Bootstrap4 输入框组](https://www.runoob.com/bootstrap4-forms-input-group.html)
			[Bootstrap4 面包屑导航（Breadcrumb）](https://www.runoob.com/bootstrap4-breadcrumb.html) **













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