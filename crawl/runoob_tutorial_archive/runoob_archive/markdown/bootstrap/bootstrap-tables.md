# Bootstrap 表格

- Source: https://www.runoob.com/bootstrap/bootstrap-tables.html

Bootstrap 提供了一个清晰的创建表格的布局。下表列出了 Bootstrap 支持的一些表格元素：


| 标签 | 描述 |
| --- | --- |
|  | 为表格添加基础样式。 |
|  | 表格标题行的容器元素（），用来标识表格列。 |
|  | 表格主体中的表格行的容器元素（）。 |
|  | 一组出现在单行上的表格单元格的容器元素（ 或 ）。 |
|  | 默认的表格单元格。 |
|  | 特殊的表格单元格，用来标识列或行（取决于范围和位置）。必须在 内使用。 |
|  | 关于表格存储内容的描述或总结。 |


### 表格类


下表样式可用于表格中：


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .table | 为任意 添加基本样式 (只有横向分隔线) | 尝试一下 |
| .table-striped | 在 内添加斑马线形式的条纹 ( IE8 不支持) | 尝试一下 |
| .table-bordered | 为所有表格的单元格添加边框 | 尝试一下 |
| .table-hover | 在 内的任一行启用鼠标悬停状态 | 尝试一下 |
| .table-condensed | 让表格更加紧凑 | 尝试一下 |
| 联合使用所有表格类 | 尝试一下 |  |


### , 和 类


下表的类可用于表格的行或者单元格：


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .active | 将悬停的颜色应用在行或者单元格上 | 尝试一下 |
| .success | 表示成功的操作 | 尝试一下 |
| .info | 表示信息变化的操作 | 尝试一下 |
| .warning | 表示一个警告的操作 | 尝试一下 |
| .danger | 表示一个危险的操作 | 尝试一下 |


## 基本的表格


如果您想要一个只带有内边距（padding）和水平分割的基本表，请添加 class *.table*，如下面实例所示：


## 实例


```css
<table class="table">
  <caption>基本的表格布局</caption>
  <thead>
    <tr>
      <th>名称</th>
      <th>城市</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tanmay</td>
      <td>Bangalore</td>
    </tr>
    <tr>
      <td>Sachin</td>
      <td>Mumbai</td>
    </tr>
  </tbody>
</table>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-table-basic)


结果如下所示：


![基本的表格](https://www.runoob.com/wp-content/uploads/2014/06/basictable_demo.jpg)


## 可选的表格类


除了基本的表格标记和 .table class，还有一些可以用来为标记定义样式的类。下面将向您介绍这些类。


### 条纹表格


通过添加 *.table-striped* class，您将在  内的行上看到条纹，如下面的实例所示：


## 实例


```css
<table class="table table-striped">
  <caption>条纹表格布局</caption>
  <thead>
    <tr>
      <th>名称</th>
      <th>城市</th>
      <th>邮编</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tanmay</td>
      <td>Bangalore</td>
      <td>560001</td>
    </tr>
    <tr>
      <td>Sachin</td>
      <td>Mumbai</td>
      <td>400003</td>
    </tr>
    <tr>
      <td>Uma</td>
      <td>Pune</td>
      <td>411027</td>
    </tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-table-striped)


结果如下所示：


![条纹表格](https://www.runoob.com/wp-content/uploads/2014/06/18444836-F51F-4F09-8EC4-F5239AFDD1F5.jpg)


### 边框表格


通过添加 *.table-bordered* class，您将看到每个元素周围都有边框，且占整个表格是圆角的，如下面的实例所示：


## 实例


```css
<table class="table table-bordered">
  <caption>边框表格布局</caption>
  <thead>
    <tr>
      <th>名称</th>
      <th>城市</th>
      <th>邮编</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tanmay</td>
      <td>Bangalore</td>
      <td>560001</td>
    </tr>
    <tr>
      <td>Sachin</td>
      <td>Mumbai</td>
      <td>400003</td>
    </tr>
    <tr>
      <td>Uma</td>
      <td>Pune</td>
      <td>411027</td>
    </tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-table-bodered)


结果如下所示：


![边框表格](https://www.runoob.com/wp-content/uploads/2014/06/8E9EA630-DDD7-4A27-A638-70A9586E185F.jpg)


### 悬停表格


通过添加 *.table-hover* class，当指针悬停在行上时会出现浅灰色背景，如下面的实例所示：


## 实例


```css
<table class="table table-hover">
  <caption>悬停表格布局</caption>
  <thead>
    <tr>
      <th>名称</th>
      <th>城市</th>
      <th>邮编</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tanmay</td>
      <td>Bangalore</td>
      <td>560001</td>
    </tr>
    <tr>
      <td>Sachin</td>
      <td>Mumbai</td>
      <td>400003</td>
    </tr>
    <tr>
      <td>Uma</td>
      <td>Pune</td>
      <td>411027</td>
    </tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-table-hover)


结果如下所示：


![悬停表格](https://www.runoob.com/wp-content/uploads/2014/06/87CF7351-2AA4-4375-9ED1-5017B0B4610B.jpg)


### 精简表格


通过添加 *.table-condensed * class，行内边距（padding）被切为两半，以便让表看起来更紧凑，如下面的实例所示。这在想让信息看起来更紧凑时非常有用。


## 实例


```css
<table class="table table-condensed">
  <caption>精简表格布局</caption>
  <thead>
    <tr>
      <th>名称</th>
      <th>城市</th>
      <th>邮编</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Tanmay</td>
      <td>Bangalore</td>
      <td>560001</td></tr>
    <tr>
      <td>Sachin</td>
      <td>Mumbai</td>
      <td>400003</td></tr>
    <tr>
      <td>Uma</td>
      <td>Pune</td>
      <td>411027</td></tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-table-condensed)


结果如下所示：


![精简表格](https://www.runoob.com/wp-content/uploads/2014/06/F32D49C5-2EF8-42A6-ACF4-5205B6B0C6DD.jpg)


## 上下文类


下表中所列出的上下文类允许您改变表格行或单个单元格的背景颜色。


| 类 | 描述 |
| --- | --- |
| .active | 对某一特定的行或单元格应用悬停颜色 |
| .success | 表示一个成功的或积极的动作 |
| .warning | 表示一个需要注意的警告 |
| .danger | 表示一个危险的或潜在的负面动作 |


这些类可被应用到 、 或 。


## 实例


```css
<table class="table">
  <caption>上下文表格布局</caption>
  <thead>
    <tr>
      <th>产品</th>
      <th>付款日期</th>
      <th>状态</th></tr>
  </thead>
  <tbody>
    <tr class="active">
      <td>产品1</td>
      <td>23/11/2013</td>
      <td>待发货</td></tr>
    <tr class="success">
      <td>产品2</td>
      <td>10/11/2013</td>
      <td>发货中</td></tr>
    <tr class="warning">
      <td>产品3</td>
      <td>20/10/2013</td>
      <td>待确认</td></tr>
    <tr class="danger">
      <td>产品4</td>
      <td>20/10/2013</td>
      <td>已退货</td></tr>
  </tbody>
</table>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-table-contextual)


结果如下所示：


![上下文类](https://www.runoob.com/wp-content/uploads/2014/06/contextualtable_demo.jpg)


## 响应式表格


通过把任意的 *.table* 包在 *.table-responsive* class 内，您可以让表格水平滚动以适应小型设备（小于 768px）。当在大于 768px 宽的大型设备上查看时，您将看不到任何的差别。


## 实例


```css
<div class="table-responsive">
  <table class="table">
    <caption>响应式表格布局</caption>
    <thead>
      <tr>
        <th>产品</th>
        <th>付款日期</th>
        <th>状态</th></tr>
    </thead>
    <tbody>
      <tr>
        <td>产品1</td>
        <td>23/11/2013</td>
        <td>待发货</td></tr>
      <tr>
        <td>产品2</td>
        <td>10/11/2013</td>
        <td>发货中</td></tr>
      <tr>
        <td>产品3</td>
        <td>20/10/2013</td>
        <td>待确认</td></tr>
      <tr>
        <td>产品4</td>
        <td>20/10/2013</td>
        <td>已退货</td></tr>
    </tbody>
  </table>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-table-responsive)


结果如下所示：


![响应式表格](https://www.runoob.com/wp-content/uploads/2014/06/responsive_demo.jpg)








	  AI 思考中...





			** [Bootstrap 代码](https://www.runoob.com/bootstrap-code.html)
			[Bootstrap 表单](https://www.runoob.com/bootstrap-forms.html) **













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