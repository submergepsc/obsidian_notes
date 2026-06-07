# Bootstrap5 表格

- Source: https://www.runoob.com/bootstrap5/bootstrap5-tables.html

Bootstrap 5 的表格（Table）组件提供了一系列功能和样式，使得表格更加易于构建、响应式和美观。


我们可以轻松地创建带有不同样式、排序功能、分页和响应式布局的表格。


## Bootstrap5 基础表格


在 Bootstrap 5 中，创建表格的基础结构很简单，只需要使用标准的 HTML `` 元素，并加上 `table` 类。


Bootstrap5 通过 **.table** 类来设置基础表格的样式，实例如下:


## 实例


```css
<table class="table">
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
</table>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_basic)


---


## 条纹表格


通过添加 **.table-striped** 类，您将在 ** 内的行上看到条纹，如下面的实例所示：


## 实例


```css
<table class="table table-striped">
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
</table>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_striped)

---


## 带边框表格


**.table-bordered** 类可以为表格添加边框


## 实例


```css
<table class="table table-bordered">
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_bordered)

---


## 鼠标悬停状态表格


**.table-hover** 类可以为表格的每一行添加鼠标悬停效果（灰色背景）：


## 实例


```css
<table class="table table-hover">
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_hover)


---


## 黑色背景表格


**.table-dark** 类可以为表格添加黑色背景：


## 实例


```css
<table class="table table-dark">
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_inverse)


---


## 黑色条纹表格


联合使用 **.table-dark** 和 **.table-striped** 类可以创建黑色的条纹表格：


## 实例


```css
<table class="table table-dark table-striped">
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_dark_striped)


---


## 鼠标悬停效果 - 黑色背景表格


联合使用 **.table-dark** 和 **.table-hover** 类可以设置黑色背景表格的鼠标悬停效果：


## 实例


```css
<table class="table table-dark table-hover">
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_dark_hover)

---


## 无边框表格


**.table-borderless** 类可以设置一个无边框的表格：


## 实例


```css
<table class="table table-borderless">
    <thead>
        <tr>
            <th>Firstname</th>
            <th>Lastname</th>
            <th>Email</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John</td>
            <td>Doe</td>
            <td>[email protected]</td>
        </tr>
        <tr>
            <td>Mary</td>
            <td>Moe</td>
            <td>[email protected]</td>
        </tr>
        <tr>
            <td>July</td>
            <td>Dooley</td>
            <td>[email protected]</td>
        </tr>
    </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_borderless)


---


## 指定意义的颜色类


通过指定意义的颜色类可以为表格的行或者单元格设置颜色：


## 实例


```css
<table class="table">
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Default</td>
        <td>Defaultson</td>
        <td>[email protected]</td>
      </tr>
      <tr class="table-primary">
        <td>Primary</td>
        <td>Joe</td>
        <td>[email protected]</td>
      </tr>
      <tr class="table-success">
        <td>Success</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr class="table-danger">
        <td>Danger</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr class="table-info">
        <td>Info</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
      <tr class="table-warning">
        <td>Warning</td>
        <td>Refs</td>
        <td>[email protected]</td>
      </tr>
      <tr class="table-active">
        <td>Active</td>
        <td>Activeson</td>
        <td>[email protected]</td>
      </tr>
      <tr class="table-secondary">
        <td>Secondary</td>
        <td>Secondson</td>
        <td>[email protected]</td>
      </tr>
      <tr class="table-light">
        <td>Light</td>
        <td>Angie</td>
        <td>[email protected]</td>
      </tr>
      <tr class="table-dark text-dark">
        <td>Dark</td>
        <td>Bo</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_contextual)

下表列出了表格颜色类的说明:


| 类名 | 描述 |
| --- | --- |
| .table-primary | 蓝色: 指定这是一个重要的操作 |
| .table-success | 绿色: 指定这是一个允许执行的操作 |
| .table-danger | 红色: 指定这是可以危险的操作 |
| .table-info | 浅蓝色: 表示内容已变更 |
| .table-warning | 橘色: 表示需要注意的操作 |
| .table-active | 灰色: 用于鼠标悬停效果 |
| .table-secondary | 灰色: 表示内容不怎么重要 |
| .table-light | 浅灰色，可以是表格行的背景 |
| .table-dark | 深灰色，可以是表格行的背景 |


---


## 表头颜色


我们也可以设置表头的颜色，例如 **.table-dark** 类用于给表头添加黑色背景， **.table-light** 类用于给表头添加灰色背景:


## 实例


```css
<table class="table">
    <thead class="table-dark">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
  </table>
  <table class="table">
    <thead class="table-light">
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_head)


---


## 较小的表格


**.table-sm** 类用于通过减少内边距来设置较小的表格:


## 实例


```css
<table class="table table-bordered table-sm">
    <thead>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John</td>
        <td>Doe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>Mary</td>
        <td>Moe</td>
        <td>[email protected]</td>
      </tr>
      <tr>
        <td>July</td>
        <td>Dooley</td>
        <td>[email protected]</td>
      </tr>
    </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_sm)

---


## 响应式表格


**.table-responsive** 类用于创建响应式表格：在屏幕宽度小于 992px 时会创建水平滚动条，如果可视区域宽度大于 992px 则显示不同效果（没有滚动条）:


## 实例


```css
<div class="table-responsive">
<table class="table">
    <thead>
      <tr>
        <th>#</th>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
        <th>City</th>
        <th>Country</th>
        <th>Sex</th>
        <th>Example</th>
        <th>Example</th>
        <th>Example</th>
        <th>Example</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>Anna</td>
        <td>Pitt</td>
        <td>35</td>
        <td>New York</td>
        <td>USA</td>
        <td>Female</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
      </tr>
    </tbody>
</table>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_table_responsive)


你可以通过以下类设定在指定屏幕宽度下显示滚动条：


| 类名 | 屏幕宽度 |
| --- | --- |
| .table-responsive-sm |







	  AI 思考中...





			** [Bootstrap5 颜色](https://www.runoob.com/bootstrap5-colors.html)
			[Bootstrap5 图像形状](https://www.runoob.com/bootstrap5-images.html) **













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