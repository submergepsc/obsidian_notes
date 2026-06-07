# Bootstrap4 文字排版

- Source: https://www.runoob.com/bootstrap4/bootstrap4-typography.html

---


## Bootstrap 4 默认设置


Bootstrap 4 默认的 **font-size** 为 16px, **line-height** 为 1.5。


默认的 **font-family** 为 "Helvetica Neue", Helvetica, Arial, sans-serif。


此外，所有的 **** 元素 **margin-top: 0** 、 **margin-bottom: 1rem** (16px)。


---


## -


Bootstrap 中定义了所有的 HTML 标题（h1 到 h6）的样式。请看下面的实例：


## 实例


```css
<div class="container">
  <h1>h1 Bootstrap 标题 (2.5rem = 40px)</h1>
  <h2>h2 Bootstrap 标题 (2rem = 32px)</h2>
  <h3>h3 Bootstrap 标题 (1.75rem = 28px)</h3>
  <h4>h4 Bootstrap 标题 (1.5rem = 24px)</h4>
  <h5>h5 Bootstrap 标题 (1.25rem = 20px)</h5>
  <h6>h6 Bootstrap 标题 (1rem = 16px)</h6>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_txt_hn)

### Display 标题类


Bootstrap 还提供了四个 Display 类来控制标题的样式: .display-1, .display-2, .display-3, .display-4。


## 实例


```css
<div class="container">
  <h1>Display 标题</h1>
  <p>Display 标题可以输出更大更粗的字体样式。</p>
  <h1 class="display-1">Display 1</h1>
  <h1 class="display-2">Display 2</h1>
  <h1 class="display-3">Display 3</h1>
  <h1 class="display-4">Display 4</h1>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_txt_display)

---


##


在 Bootstrap 4 中 HTML **** 元素用于创建字号更小的颜色更浅的文本:


## 实例


```css
<div class="container">
  <h1>更小文本标题</h1>
  <p>small 元素用于字号更小的颜色更浅的文本:</p>
  <h1>h1 标题 <small>副标题</small></h1>
  <h2>h2 标题 <small>副标题</small></h2>
  <h3>h3 标题 <small>副标题</small></h3>
  <h4>h4 标题 <small>副标题</small></h4>
  <h5>h5 标题 <small>副标题</small></h5>
  <h6>h6 标题 <small>副标题</small></h6>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_txt_small)
---


##


Bootstrap 4 定义 **** 为黄色背景及有一定的内边距:


## 实例


```css
<div class="container">
  <h1>高亮文本</h1>
  <p>使用 mark 元素来 <mark>高亮</mark> 文本。</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_txt_mark)

---


##


Bootstrap 4 定义 HTML **** 元素的样式为显示在文本底部的一条虚线边框:


## 实例


```css
<div class="container">
  <h1>Abbreviations</h1>
  <p>The abbr element is used to mark up an abbreviation or acronym:</p>
  <p>The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_txt_abbr)

---


##


对于引用的内容可以在 **** 上添加 **.blockquote** 类 :


## 实例


```css
<div class="container">
  <h1>Blockquotes</h1>
  <p>The blockquote element is used to present content from another source:</p>
  <blockquote class="blockquote">
    <p>For 50 years, WWF has been protecting the future of nature. The world's leading conservation organization, WWF works in 100 countries and is supported by 1.2 million members in the United States and close to 5 million globally.</p>
    <footer class="blockquote-footer">From WWF's website</footer>
  </blockquote>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_txt_blockquote)

---


##


Bootstrap 4 定义 HTML **** 元素的样式如下:


## 实例


```css
<div class="container">
  <h1>Description Lists</h1>
  <p>The dl element indicates a description list:</p>
  <dl>
    <dt>Coffee</dt>
    <dd>- black hot drink</dd>
    <dt>Milk</dt>
    <dd>- white cold drink</dd>
  </dl>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_txt_dl)


---


##


Bootstrap 4 定义 HTML **** 元素的样式如下:


## 实例


```css
<div class="container">
  <h1>代码片段</h1>
  <p>可以将一些代码元素放到 code 元素里面:</p>
  <p>以下 HTML 元素: <code>span</code>, <code>section</code>, 和 <code>div</code> 用于定义部分文档内容。</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_txt_code)


##


Bootstrap 4 定义 HTML **** 元素的样式如下:


## 实例


```css
<div class="container">
  <h1>Keyboard Inputs</h1>
  <p>To indicate input that is typically entered via the keyboard, use the kbd element:</p>
  <p>Use <kbd>ctrl + p</kbd> to open the Print dialog box.</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_txt_kbd)


---


##


Bootstrap 4 定义 HTML **** 元素的样式如下:


## 实例


```css
<div class="container">
<h1>Multiple Code Lines</h1>
<p>For multiple lines of code, use the pre element:</p>
<pre>
Text in a pre element
is displayed in a fixed-width
font, and it preserves
both      spaces and
line breaks.
</pre>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_txt_pre)

---


## 更多排版类

下表提供了 Bootstrap4 更多排版类的实例：


| 类名 | 描述 | 实例 |
| --- | --- | --- |
| .font-weight-bold | 加粗文本 | 尝试一下 |
| .font-weight-normal | 普通文本 | 尝试一下 |
| .font-weight-light | 更细的文本 | 尝试一下 |
| .font-italic | 斜体文本 | 尝试一下 |
| .lead | 让段落更突出 | 尝试一下 |
| .small | 指定更小文本 (为父元素的 85% ) | 尝试一下 |
| .text-left | 左对齐 | 尝试一下 |
| .text-center | 居中 | 尝试一下 |
| .text-right | 右对齐 | 尝试一下 |
| .text-justify | 设定文本对齐,段落中超出屏幕部分文字自动换行 | 尝试一下 |
| .text-nowrap | 段落中超出屏幕部分不换行 | 尝试一下 |
| .text-lowercase | 设定文本小写 | 尝试一下 |
| .text-uppercase | 设定文本大写 | 尝试一下 |
| .text-capitalize | 设定单词首字母大写 | 尝试一下 |
| .initialism | 显示在 元素中的文本以小号字体展示，且可以将小写字母转换为大写字母 | 尝试一下 |
| .list-unstyled | 移除默认的列表样式，列表项中左对齐 ( 和 中)。 这个类仅适用于直接子列表项 (如果需要移除嵌套的列表项，你需要在嵌套的列表中使用该样式) | 尝试一下 |
| .list-inline | 将所有列表项放置同一行 | 尝试一下 |
| .pre-scrollable | 使 元素可滚动，代码块区域最大高度为340px,一旦超出这个高度,就会在Y轴出现滚动条 | 尝试一下 |









	  AI 思考中...





			** [Bootstrap4 网格系统](https://www.runoob.com/bootstrap4-grid-basic.html)
			[Bootstrap4 颜色](https://www.runoob.com/bootstrap4-colors.html) **













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