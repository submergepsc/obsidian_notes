# CSS !important 规则

- Source: https://www.runoob.com/css/css-important.html

### 什么是 !important


CSS 中的 !important 规则用于增加样式的权重。


**!important** 与优先级无关，但它与最终的结果直接相关，使用一个 !important 规则时，此声明将覆盖任何其他声明。


## 实例


```css
#myid {
  background-color: blue;
}

.myclass {
  background-color: gray;
}

p {
  background-color: red !important;
}
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_important)


以上实例中，尽管 ID 选择器和类选择器具有更高的优先级，但三个段落背景颜色都显示为红色，因为 !important 规则会覆盖 background-color 属性。


### 重要说明


使用 !important 是一个坏习惯，应该尽量避免，因为这破坏了样式表中的固有的级联规则 使得调试找 bug 变得更加困难了。

当两条相互冲突的带有 !important 规则的声明被应用到相同的元素上时，拥有更大优先级的声明将会被采用。


以下实例我们在查看 CSS 源码时就不是很清楚哪种颜色最重要：


## 实例


```css
#myid {
  background-color: blue !important;
}

.myclass {
  background-color: gray !important;
}

p {
  background-color: red !important;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_important2)

使用建议：**


- **一定**要优先考虑使用样式规则的优先级来解决问题而不是 `!important`
- **只有**在需要覆盖全站或外部 CSS 的特定页面中使用 `!important`
- **永远不要**在你的插件中使用 `!important`
- **永远不要**在全站范围的 CSS 代码中使用 `!important`


### 何时使用 !important


如果要在你的网站上设定一个全站样式的 CSS 样式可以使用 !important。


比如我们要让网站上所有按钮的样式都一样：


## 实例


```css
.button {
  background-color: #8c8c8c;
  color: white;
  padding: 5px;
  border: 1px solid black;
}
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_important3)

如果我们将按钮放在另一个具有更优先级的元素中，按钮的外观就会发生变化，并且属性会发生冲突，如下实例：


## 实例


```css
.button {
  background-color: #8c8c8c;
  color: white;
  padding: 5px;
  border: 1px solid black;
}

#myDiv a {
  color: red;
  background-color: yellow;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_important4)

如果想要设置所有按钮具有相同的外观，我们可以将 !important 规则添加到按钮的样式属性中，如下所示：


## 实例


```css
.button {
  background-color: #8c8c8c !important;
  color: white !important;
  padding: 5px !important;
  border: 1px solid black !important;
}

#myDiv a {
  color: red;
  background-color: yellow;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_important5)







	  AI 思考中...





			** [CSS 网页布局](https://www.runoob.com/css-website-layout.html)
			[CSS AI 编程](https://www.runoob.com/fitten-code-css.html) **













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

      : ·[CSS 实例](https://www.runoob.com/css-examples.html)

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