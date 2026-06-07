# Bootstrap4 折叠

- Source: https://www.runoob.com/bootstrap4/bootstrap4-collapse.html

Bootstrap4 折叠可以很容易的实现内容的显示与隐藏。


## 实例


```css
<button data-toggle="collapse" data-target="#demo">折叠</button>

<div id="demo" class="collapse">
Lorem ipsum dolor text....
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_collapsible)

### 实例解析


**.collapse** 类用于指定一个折叠元素 (实例中的 ); 点击按钮后会在隐藏与显示之间切换。


控制内容的隐藏与显示，需要在  或  元素上添加 **data-toggle="collapse"** 属性。 **data-target="#id"** 属性是对应折叠的内容 ()。


注意:**  元素上你可以使用 **href** 属性来代替 **data-target** 属性:


## 实例


```css
<a href="#demo" data-toggle="collapse">Collapsible</a>

<div id="demo" class="collapse">
Lorem ipsum dolor text....
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_collapsible2)


默认情况下折叠的内容是隐藏的，你可以添加 **.show** 类让内容默认显示:


## 实例


```css
<div id="demo" class="collapse show">
Lorem ipsum dolor text....
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_collapsible_in)

以下实例通过扩展卡片组件来显示简单的手风琴。


注意:** 使用 **data-parent** 属性来确保所有的折叠元素在指定的父元素下，这样就能实现在一个折叠选项显示时其他选项就隐藏。


## 实例


```css
<div id="accordion">
<div class="card">
  <div class="card-header">
    <a class="card-link" data-toggle="collapse" href="#collapseOne">
      选项一
    </a>
  </div>
  <div id="collapseOne" class="collapse show" data-parent="#accordion">
    <div class="card-body">
      #1 内容：菜鸟教程 -- 学的不仅是技术，更是梦想！！！
    </div>
  </div>
</div>
<div class="card">
  <div class="card-header">
    <a class="collapsed card-link" data-toggle="collapse" href="#collapseTwo">
    选项二
  </a>
  </div>
  <div id="collapseTwo" class="collapse" data-parent="#accordion">
    <div class="card-body">
      #2 内容：菜鸟教程 -- 学的不仅是技术，更是梦想！！！
    </div>
  </div>
</div>
<div class="card">
  <div class="card-header">
    <a class="collapsed card-link" data-toggle="collapse" href="#collapseThree">
      选项三
    </a>
  </div>
  <div id="collapseThree" class="collapse" data-parent="#accordion">
    <div class="card-body">
      #3 内容：菜鸟教程 -- 学的不仅是技术，更是梦想！！！
    </div>
  </div>
</div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_collapsible_accordion)








	  AI 思考中...





			** [Bootstrap4 下拉菜单](https://www.runoob.com/bootstrap4-dropdowns.html)
			[Bootstrap4 导航](https://www.runoob.com/bootstrap4-navs.html) **













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