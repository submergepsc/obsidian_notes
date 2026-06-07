# Bootstrap 下拉菜单（Dropdowns）

- Source: https://www.runoob.com/bootstrap/bootstrap-dropdowns.html

本章将重点介绍 Bootstrap 下拉菜单。下拉菜单是可切换的，是以列表格式显示链接的上下文菜单。这可以通过与 [下拉菜单（Dropdown） JavaScript 插件](https://www.runoob.com/bootstrap-dropdown-plugin.html) 的互动来实现。


如需使用下拉菜单，只需要在 class **.dropdown** 内加上下拉菜单即可。下面的实例演示了基本的下拉菜单：


## 实例


```css
<div class="dropdown">
    <button type="button" class="btn dropdown-toggle" id="dropdownMenu1" data-toggle="dropdown">主题
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">Java</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据挖掘</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据通信/网络</a>
        </li>
        <li role="presentation" class="divider"></li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">分离的链接</a>
        </li>
    </ul>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-dropdown-basic&basepath=0)


结果如下所示：


![基本的下拉菜单（Dropdowns）](https://www.runoob.com/wp-content/uploads/2014/06/basicdropdown_demo.jpg)


## 选项


### 对齐


通过向 .dropdown-menu** 添加 class **.pull-right** 来向右对齐下拉菜单。下面的实例演示了这点：


## 实例


```css
<div class="dropdown">
    <button type="button" class="btn dropdown-toggle" id="dropdownMenu1" data-toggle="dropdown">主题
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu pull-right" role="menu" aria-labelledby="dropdownMenu1">
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">Java</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据挖掘</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据通信/网络</a>
        </li>
        <li role="presentation" class="divider"></li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">分离的链接</a>
        </li>
    </ul>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-dropdown-alignright)


结果如下所示：


![向右对齐下拉菜单](https://www.runoob.com/wp-content/uploads/2014/06/dropdownalignright_demo.jpg)


### 标题


您可以使用 class dropdown-header** 向下拉菜单的标签区域添加标题。下面的实例演示了这点：


## 实例


```css
<div class="dropdown">
    <button type="button" class="btn dropdown-toggle" id="dropdownMenu1" data-toggle="dropdown">主题
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
        <li role="presentation" class="dropdown-header">下拉菜单标题</li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">Java</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据挖掘</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据通信/网络</a>
        </li>
        <li role="presentation" class="divider"></li>
        <li role="presentation" class="dropdown-header">下拉菜单标题</li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">分离的链接</a>
        </li>
    </ul>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-dropdown-header)


结果如下所示：


![下拉菜单标题](https://www.runoob.com/wp-content/uploads/2014/06/dropdownheader_demo.jpg)


---


## 更多实例


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .dropdown | 指定下拉菜单，下拉菜单都包裹在 .dropdown 里 | 尝试一下 |
| .dropdown-menu | 创建下拉菜单 | 尝试一下 |
| .dropdown-menu-right | 下拉菜单右对齐 | 尝试一下 |
| .dropdown-header | 下拉菜单中添加标题 | 尝试一下 |
| .dropup | 指定向上弹出的下拉菜单 | 尝试一下 |
| .disabled | 下拉菜单中的禁用项 | 尝试一下 |
| .divider | 下拉菜单中的分割线 | 尝试一下 |








	  AI 思考中...





			** [Bootstrap 字体图标(Glyphicons)](https://www.runoob.com/bootstrap-glyphicons.html)
			[Bootstrap 按钮组](https://www.runoob.com/bootstrap-button-groups.html) **













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