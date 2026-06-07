# Foundation 输入框尺寸

- Source: https://www.runoob.com/foundation/foundation-input-sizing.html

*

使用网格的列来设置输入框的大小，如 `.large-6`, `.medium-6`, 等。


更多网格系统知识，可以点击 [网格系统](https://www.runoob.com/foundation-grid-system.html) 教程。


### 实例


```
<form>
  <div class="row">    <div class="large-10 medium-7 columns">

  <label>large-10 medium-7 (100% on small)        <input type="text"
  placeholder="Name">      </label>    </div>  </div>  <div class="row">
      <div class="small-5 columns">      <label>small-5        <input type="text"
  placeholder="Name">      </label>    </div>  </div>  <div class="row">
      <div class="medium-3 columns">      <label>medium-3 (100% on small)        <input
  type="text" placeholder="Name">      </label>    </div>  </div>
  </form>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms_sizing)


---


## 相等大小列


以下演示了相等大小列的实例:


### 实例


```
<form>
  <div class="row">    <div class="medium-4 columns">      <label>medium-4 (100% on small, stacked)        <input type="text" placeholder="Name">      </label>
  </div>    <div class="medium-4 columns">      <label>medium-4 (100% on small, stacked)        <input type="text" placeholder="Name">      </label>    </div>    <div class="medium-4 columns">      <label>medium-4 (100% on small, stacked)        <input type="text" placeholder="Name">      </label>    </div>  </div>
  </form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms_sizing2)


---


## 内联标签


如果你希望你的标签内容显示在左边（不是上边），可以将标签元素 label 放在输入框左边的不同的列上，并使用 `.inline` 类来设置垂直居中:


### 实例


```
<form>
  <div class="row">    <div class="small-8">      <div
  class="row">        <div class="small-3 columns">
  <label for="name" class="inline right">Name</label>        </div>        <div class="small-9 columns">
  <input type="text" id="name" placeholder="First Name..">        </div>      </div>    </div>  </div>
  </form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms_label_inline)


---


## 前置和后置标签


你可以在 `` 中添加前置和后置标签，元素为： `` 或 ``。可以使用网格系统来设置前置和后置标签的大小：


### 实例


```
<form>
  <div class="row">    <div class="large-6 columns">      <div class="row collapse prefix-radius">
  <div class="small-3 columns">
  <span class="prefix">Prefix</span>        </div>        <div class="small-9 columns">
  <input type="text" placeholder="Value">
  </div>      </div>    </div>    <div
  class="large-6 columns">      <div class="row collapse
  postfix-radius">        <div class="small-9
  columns">          <input type="text"
  placeholder="Value">        </div>
  <div class="small-3 columns">
  <span class="postfix">Postfix</span>        </div>
  </div>    </div>  </div>
  </form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms_prepostfix)


### 前置和后置标签按钮


可以使用 `` 元素添加 `.button` 类来设置前置和后置按钮:


### 实例


```
<a href="#" class="postfix button">Go</a>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms_prepostfix2)


### 前置和后置标签圆角按钮


### 实例


```
<form>  <div class="row">    <div class="large-6
  columns">      <div class="row collapse
  prefix-radius">        <div
  class="small-3 columns">
  <span class="prefix">Prefix</span>
  </div>        <div class="small-9
  columns">          <input
  type="text" placeholder="Value">
  </div>      </div>    </div>
  <div class="large-6 columns">      <div
  class="row collapse postfix-radius">
  <div class="small-9 columns">
  <input type="text" placeholder="Value">
  </div>        <div class="small-3
  columns">          <span
  class="postfix">Postfix</span>
  </div>      </div>    </div>
  </div>  <div class="row">    <div class="large-6
  columns">      <div class="row collapse
  prefix-round">        <div
  class="small-3 columns">
  <a href="#" class="button prefix">Go</a>
  </div>        <div class="small-9
  columns">          <input
  type="text" placeholder="Value">
  </div>      </div>    </div>
  <div class="large-6 columns">      <div
  class="row collapse postfix-round">
  <div class="small-9 columns">
  <input type="text" placeholder="Value">
  </div>        <div class="small-3
  columns">          <a href="#"
  class="button postfix">Go</a>
  </div>      </div>    </div>
  </div></form>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_forms_prepostfix3)








	  AI 思考中...





			** [Foundation 表单](https://www.runoob.com/foundation-forms.html)
			[Foundation 开关](https://www.runoob.com/foundation-switches.html) **













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