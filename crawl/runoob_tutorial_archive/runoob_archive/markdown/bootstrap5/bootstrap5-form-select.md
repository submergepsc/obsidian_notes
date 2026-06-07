# Bootstrap5 下拉菜单

- Source: https://www.runoob.com/bootstrap5/bootstrap5-form-select.html

下拉菜单可以是单选下拉菜单，也可以是多选的下拉菜单。


**单选下拉菜单：**


![](https://www.runoob.com/wp-content/uploads/2022/02/F7B60B45-FC3A-4A6C-9035-9BCB97588159.jpg)


**多选下拉菜单：**


![](https://www.runoob.com/wp-content/uploads/2022/02/25B5A044-7996-4704-A020-142BE4457FCF.jpg)


在 Bootstrap5 中下拉菜单 **** 元素可以使用 **.form-select** 类来渲染 :


## 实例


```css
<select class="form-select">
  <option>1</option>
  <option>2</option>
  <option>3</option>
  <option>4</option>
</select>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_form_select)

下拉菜单通过 **.form-select-lg** 或 **.form-select-sm** 类来修改大小：


## 实例


```css
<select class="form-select form-select-lg">
<select class="form-select">
<select class="form-select form-select-sm">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_form_select_size)

效果如下图：


![](https://www.runoob.com/wp-content/uploads/2022/02/74421F87-C10B-4726-B3C2-71174DA53508.jpg)


**disabled** 属性可以禁止下拉菜单被选择：


## 实例


```css
<select class="form-select" disabled>
  <option>1</option>
  <option>2</option>
  <option>3</option>
  <option>4</option>
</select>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_form_select_disabled)

## 数据列表


Bootstrap 也可以通过 datalist 标签为  元素设置下拉菜单：


以下实例从列表中选择一个网站：


## 实例


```css
<label for="browser" class="form-label">选择你喜欢的网站：</label>
<input class="form-control" list="sites" name="site" id="site">
<datalist id="sites">
  <option value="Google">
  <option value="Runoob">
  <option value="Taobao">
  <option value="Wiki">
  <option value="Zhihu">
</datalist>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_form_select_datalist)

效果如下图：


![](https://www.runoob.com/wp-content/uploads/2022/02/90FD79CC-090E-40EA-9D05-9231BD5B2843.jpg)








	  AI 思考中...





			** [Bootstrap5 表单](https://www.runoob.com/bootstrap5-forms.html)
			[Bootstrap5 复选框与单选框](https://www.runoob.com/bootstrap5-form-check-radio.html) **













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