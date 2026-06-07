# HTML 表格

- Source: https://www.runoob.com/html/html-tables.html

---


HTML 表格由 **** 标签来定义。


HTML 表格是一种用于展示结构化数据的标记语言元素。


每个表格均有若干行（由 **** 标签定义），每行被分割为若干单元格（由 **** 标签定义），表格可以包含标题行（****）用于定义列的标题。



- **tr**：tr 是 table row 的缩写，表示表格的一行。
- **td**：td 是 table data 的缩写，表示表格的数据单元格。
- **th**：th 是 table header的缩写，表示表格的表头单元格。


数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。


HTML 表格生成器：[https://www.jyshare.com/front-end/7688/](https://www.jyshare.com/front-end/7688/)。


### 以下是一个简单的 HTML 表格实例:


## 实例


```html
<table>
  <thead>
    <tr>
      <th>列标题1</th>
      <th>列标题2</th>
      <th>列标题3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>行1，列1</td>
      <td>行1，列2</td>
      <td>行1，列3</td>
    </tr>
    <tr>
      <td>行2，列1</td>
      <td>行2，列2</td>
      <td>行2，列3</td>
    </tr>
  </tbody>
</table>
```


以上的表格实例代码中， 元素表示整个表格，它包含两个主要部分： 和 。


- ** 用于定义表格的标题部分:** 在  中，使用  元素定义列的标题，以上实例中列标题分别为"列标题1"，"列标题2"和"列标题3"。
- ** 用于定义表格的主体部分:** 在  中，使用  元素定义行，并在每行中使用  元素定义单元格数据，以上实例中有两行数据，每行包含三个单元格。


通过使用  元素定义列标题，可以使其在表格中以粗体显示，与普通单元格区分开来。


HTML 表格还可以具有其他部分，如  （表格页脚）和  （表格标题）， 可用于在表格的底部定义摘要、统计信息等内容。  可用于为整个表格定义标题。

HTML 表格还支持合并单元格和跨行/跨列的操作，以及其他样式和属性的应用，以满足各种需求。

我们也可以使用 CSS 来进一步自定义表格的样式和外观。


---

![Examples](https://www.runoob.com/images/tryitimg.gif)
## 在线实例


## 实例


```html
<h4>一列:</h4>
<table border="1">
  <tr>
    <td>100</td>
  </tr>
</table>

<h4>一行三列:</h4>
<table border="1">
  <tr>
    <td>100</td>
    <td>200</td>
    <td>300</td>
  </tr>
</table>

<h4>两行三列:</h4>
<table border="1">
  <tr>
    <td>100</td>
    <td>200</td>
    <td>300</td>
  </tr>
  <tr>
    <td>400</td>
    <td>500</td>
    <td>600</td>
  </tr>
</table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_tables)
（可以在本页底端找到更多实例。）


## 表格实例


## 实例


```html
<table border="1">
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```


在浏览器显示如下：:


![](https://www.runoob.com/wp-content/uploads/2013/07/4AEE0F4B-669C-4BBC-BEC4-6953E1B0E278.jpg)


---

## HTML 表格和边框属性


如果不定义边框属性，表格将不显示边框。有时这很有用，但是大多数时候，我们希望显示边框。


使用边框属性来显示一个带有边框的表格：


## 实例


```html
<table border="1">
    <tr>
        <td>Row 1, cell 1</td>
        <td>Row 1, cell 2</td>
    </tr>
</table>
```


---

## HTML 表格表头


表格的表头使用  标签进行定义。


大多数浏览器会把表头显示为粗体居中的文本：


## 实例


```html
<table border="1">
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
    </tr>
    <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
    </tr>
</table>
```


在浏览器显示如下：


![](https://www.runoob.com/wp-content/uploads/2013/07/CB476DA7-7279-4892-A424-657772E385BA.jpg)


---

![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[没有边框的表格](https://www.runoob.com/try/try.php?filename=tryhtml_tables3) 本例演示一个没有边框的表格。


[表格中的表头(Heading)](https://www.runoob.com/try/try.php?filename=tryhtml_table_headers) 本例演示如何显示表格表头。


[带有标题的表格](https://www.runoob.com/try/try.php?filename=tryhtml_tables2) 本例演示一个带标题 (caption) 的表格


[跨行或跨列的表格单元格](https://www.runoob.com/try/try.php?filename=tryhtml_table_span) 本例演示如何定义跨行或跨列的表格单元格。


[表格内的标签](https://www.runoob.com/try/try.php?filename=tryhtml_table_elements) 本例演示如何在不同的元素内显示元素。


[单元格边距(Cell padding)](https://www.runoob.com/try/try.php?filename=tryhtml_table_cellpadding) 本例演示如何使用 Cell padding 来创建单元格内容与其边框之间的空白。


[单元格间距(Cell spacing)](https://www.runoob.com/try/try.php?filename=tryhtml_table_cellspacing) 本例演示如何使用 Cell spacing 增加单元格之间的距离。


[漂亮的表格](https://www.jyshare.com/codedemo/3187)


---

## HTML 表格标签


| 标签 | 描述 |
| --- | --- |
|  | 定义表格 |
|  | 定义表格的表头 |
|  | 定义表格的行 |
|  | 定义表格单元 |
|  | 定义表格标题 |
|  | 定义表格列的组 |
|  | 定义用于表格列的属性 |
|  | 定义表格的页眉 |
|  | 定义表格的主体 |
|  | 定义表格的页脚 |








	  AI 思考中...





			** [HTML 图像](https://www.runoob.com/html-images.html)
			[HTML 列表](https://www.runoob.com/html-lists.html) **