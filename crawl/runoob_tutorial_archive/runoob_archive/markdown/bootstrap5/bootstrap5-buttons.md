# Bootstrap5 按钮

- Source: https://www.runoob.com/bootstrap5/bootstrap5-buttons.html

Bootstrap 5 提供了不同样式的按钮。


## 实例


```css
<button type="button" class="btn">基本按钮</button>
<button type="button" class="btn btn-primary">主要按钮</button>
<button type="button" class="btn btn-secondary">次要按钮</button>
<button type="button" class="btn btn-success">成功</button>
<button type="button" class="btn btn-info">信息</button>
<button type="button" class="btn btn-warning">警告</button>
<button type="button" class="btn btn-danger">危险</button>
<button type="button" class="btn btn-dark">黑色</button>
<button type="button" class="btn btn-light">浅色</button>
<button type="button" class="btn btn-link">链接</button>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_button_styles)

按钮类可用于 ****, ****, 或 **** 元素上:


## 实例


```css
<a href="#" class="btn btn-info" role="button">链接按钮</a>
<button type="button" class="btn btn-info">按钮</button>
<input type="button" class="btn btn-info" value="输入框按钮">
<input type="submit" class="btn btn-info" value="提交按钮">
<input type="reset" class="btn btn-info" value="重置按钮">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_button_elements)

---


## 按钮设置边框

Bootstrap 5 也可以设置按钮多边框，鼠标移动到按钮上添加突出到效果：


## 实例


```css
<button type="button" class="btn btn-outline-primary">主要按钮</button>
<button type="button" class="btn btn-outline-secondary">次要按钮</button>
<button type="button" class="btn btn-outline-success">成功</button>
<button type="button" class="btn btn-outline-info">信息</button>
<button type="button" class="btn btn-outline-warning">警告</button>
<button type="button" class="btn btn-outline-danger">危险</button>
<button type="button" class="btn btn-outline-dark">黑色</button>
<button type="button" class="btn btn-outline-light text-dark">浅色</button>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_button_outline)


---


## 不同大小的按钮


Bootstrap 5 可以设置按钮的大小，使用 **.btn-lg** 类设置大按钮，使用 **.btn-sm** 类设置小按钮：


## 实例


```css
<button type="button" class="btn btn-primary btn-lg">大号按钮</button>
<button type="button" class="btn btn-primary">默认按钮</button>
<button type="button" class="btn btn-primary btn-sm">小号按钮</button>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_button_sizes)

---


## 块级按钮


通过添加 **.btn-block** 类可以设置块级按钮，**.d-grid** 类设置在父级元素中：


## 实例


```css
<div class="d-grid">
    <button type="button" class="btn btn-primary btn-block">按钮 1</button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_button_block)


如果有多个块级按钮，你可以使用用 **.gap-*** 类来设置：


## 实例


```css
<div class="d-grid gap-3">
  <button type="button" class="btn btn-primary btn-block">100% 宽度的按钮</button>
  <button type="button" class="btn btn-primary btn-block">100% 宽度的按钮</button>
  <button type="button" class="btn btn-primary btn-block">100% 宽度的按钮</button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_button_many_block)


---


## 激活和禁用的按钮


按钮可设置为激活或者禁止点击的状态。


**.active** 类可以设置按钮是可用的， **disabled** 属性可以设置按钮是不可点击的。 注意  元素不支持 disabled 属性，你可以通过添加 **.disabled** 类来禁止链接的点击。


## 实例


```css
<button type="button" class="btn btn-primary active">点击后的按钮</button>
<button type="button" class="btn btn-primary" disabled>禁止点击的按钮</button>
<a href="#" class="btn btn-primary disabled">禁止点击的链接</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_button_active)


---


## 加载按钮


我们也可以设置一个正在加载的按钮。


## 实例


```css
<button class="btn btn-primary">
  <span class="spinner-border spinner-border-sm"></span>
</button>

<button class="btn btn-primary">
  <span class="spinner-border spinner-border-sm"></span>
  Loading..
</button>

<button class="btn btn-primary" disabled>
  <span class="spinner-border spinner-border-sm"></span>
  Loading..
</button>

<button class="btn btn-primary" disabled>
  <span class="spinner-grow spinner-grow-sm"></span>
  Loading..
</button>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_spinners_buttons)










	  AI 思考中...





			** [Bootstrap5 信息提示框](https://www.runoob.com/bootstrap5-alerts.html)
			[Bootstrap5 按钮组](https://www.runoob.com/bootstrap5-button-groups.html) **













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