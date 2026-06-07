# CSS 计数器

- Source: https://www.runoob.com/css/css-counters.html

CSS 计数器通过一个变量来设置，根据规则递增变量。


---


## 使用计数器自动编号


CSS 计数器根据规则来递增变量。


CSS 计数器使用到以下几个属性：


- `counter-reset` - 创建或者重置计数器
- `counter-increment` - 递增变量
- `content` - 插入生成的内容
- `counter()` 或 `counters()` 函数 - 将计数器的值添加到元素


要使用 CSS 计数器，得先用 counter-reset 创建：


以下实例在页面创建一个计数器 (在 body 选择器中)，每个  元素的计数值都会递增，并在每个  元素前添加 "Section :"


## CSS 实例


```css
body {
  counter-reset: section;
}

h2::before {
  counter-increment: section;
  content: "Section " counter(section) ": ";
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_counters1)

---


## 嵌套计数器


以下实例在页面创建一个计数器，在每一个  元素前添加计数值 "Section .", 嵌套的计数值则放在  元素的前面，内容为 ".":


## CSS 实例


```css
body {
  counter-reset: section;
}

h1 {
  counter-reset: subsection;
}

h1::before {
  counter-increment: section;
  content: "Section " counter(section) ". ";
}

h2::before {
  counter-increment: subsection;
  content: counter(section) "." counter(subsection) " ";
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_counters2)


计数器也可用于列表中，列表的子元素会自动创建。这里我们使用了 `counters()` 函数在不同的嵌套层级中插入字符串:


## CSS 实例


```css
ol {
  counter-reset: section;
  list-style-type: none;
}

li::before {
  counter-increment: section;
  content: counters(section,".") " ";
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_counters3)


---


## CSS 计数器属性



| 属性 | 描述 |
| --- | --- |
| content | 使用 ::before 和 ::after 伪元素来插入自动生成的内容 |
| counter-increment | 递增一个或多个值 |
| counter-reset | 创建或重置一个或多个计数器 |








	  AI 思考中...





			** [CSS 表单](https://www.runoob.com/css-form.html)
			[CSS 网页布局](https://www.runoob.com/css-website-layout.html) **













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