# HTML 标签

- Source: https://www.runoob.com/tags/tag-ol.html

**
## 实例


2 个不同的有序列表实例：


```
<ol>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>

<ol start="50">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_lists)


---


## 浏览器支持


| 元素 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Yes | Yes | Yes | Yes | Yes |


---


## 标签定义及使用说明


 标签定义了一个有序列表. 列表排序以数字来显示。


使用[](https://www.runoob.com/tag-li.html) 标签来定义列表选项。


---


## 提示和注释


提示: **可以使用 CSS 来渲染，详细查看 [CSS 列表](https://www.runoob.com/../css/css-list.html)。


**提示:**无序列表，可以使用 [](https://www.runoob.com/tag-ul.html) 标签。


---


## HTML 4.01 与 HTML5中的差异


"reversed" 属性是 HTML5 中的新属性。


在HTML 4.01中"compact" 属性已经废弃,在 HTML5中不支持该属性。


---


## 属性


New：HTML5 新属性。


| 属性 | 值 | 描述 |
| --- | --- | --- |
| compact | compact | HTML5 中不支持，不赞成使用。请使用样式取代它。 规定列表呈现的效果比正常情况更小巧。 |
| reversedNew | reversed | 指定列表倒序(9,8,7...) |
| start | number | 一个整数值属性，指定了列表编号的起始值。这个属性在 HTML4中弃用，但是在 HTML5 中被重新引入。 |
| type | a 表示小写英文字母编号 A 表示大写英文字母编号 i 表示小写罗马数字编号 I 表示大写罗马数字编号 1 表示数字编号（默认） | 规定列表的类型。不赞成使用。请使用样式代替。 |

**
---


## 更多实例


## 实例


设置不同的列表样式(使用 CSS):


```
<ol style="list-style-type:upper-roman">
<li>Coffee</li>
<li>Tea</li>
<li>Milk</li>
</ol>

<ol style="list-style-type:lower-alpha">
<li>Coffee</li>
<li>Tea</li>
<li>Milk</li>
</ol>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_ol_type_css)


## 实例


使用 CSS 显示不同的列表样式:


```
ol.a {list-style-type: armenian;}
ol.b {list-style-type: cjk-ideographic;}
ol.c {list-style-type: decimal;}
ol.d {list-style-type: decimal-leading-zero;}
ol.e {list-style-type: georgian;}
ol.f {list-style-type: hebrew;}
ol.g {list-style-type: hiragana;}
ol.h {list-style-type: hiragana-iroha;}
ol.i {list-style-type: katakana;}
ol.j {list-style-type: katakana-iroha;}
ol.k {list-style-type: lower-alpha;}
ol.l {list-style-type: lower-greek;}
ol.m {list-style-type: lower-latin;}
ol.n {list-style-type: lower-roman;}
ol.o {list-style-type: upper-alpha;}
ol.p {list-style-type: upper-latin;}
ol.q {list-style-type: upper-roman;}
ol.r {list-style-type: none;}
ol.s {list-style-type: inherit;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_ol_type_all_css)


## 实例


列表嵌套:


```
<ol>
  <li>Coffee</li>
  <li>Tea
    <ul>
      <li>Black tea</li>
      <li>Green tea</li>
    </ul>
  </li>
  <li>Milk</li>
</ol>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_ol_nested)


---


## 全局属性


 标签支持全局属性，查看完整属性表 [HTML全局属性](https://www.runoob.com/ref-standardattributes.html)。


---


## 事件属性


 标签支持所有 [HTML事件属性](https://www.runoob.com/ref-eventattributes.html)。


---


## 相关文章


HTML 教程：[HTML 列表](https://www.runoob.com/../html/html-lists.html)








	  AI 思考中...





			** [HTML  标签](https://www.runoob.com/tag-optgroup.html)
			[HTML  标签](https://www.runoob.com/tag-object.html) **













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

      : · [HTML ASCII 字符集](https://www.runoob.com/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/html-colorpicker.html)

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