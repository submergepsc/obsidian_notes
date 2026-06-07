# Tailwind CSS 背景颜色

- Source: https://www.runoob.com/tailwindcss/tailwindcss-backgrounds.html

在 Tailwind CSS 中，**背景颜色**（Background Color）是最常用的工具类之一，它允许你快速为元素设置背景颜色。

Tailwind 提供了多种颜色选项以及不同的色调，确保你能灵活地应用所需的样式。


**背景颜色基本语法**：


```
<div class="bg-{color}">
  <!-- 内容 -->
</div>
```


**常见的背景颜色类**：


| 类名 | 描述 | 例子 |
| --- | --- | --- |
| bg-{color} | 设置背景颜色 | bg-red-500，bg-blue-200 |
| bg-transparent | 设置透明背景颜色 | bg-transparent |
| bg-current | 设置背景颜色为当前文本颜色（常用于图标的背景） | bg-current |
| bg-white | 设置背景颜色为白色 | bg-white |
| bg-black | 设置背景颜色为黑色 | bg-black |
| bg-gray-{n} | 设置背景颜色为灰色，{n} 为灰色的深浅度（从 50 到 900） | bg-gray-100, bg-gray-700 |


**背景颜色的渐变（Gradient）**：


Tailwind CSS 支持背景的线性渐变、径向渐变等。你可以使用 `bg-gradient-to-{direction}` 来指定渐变的方向，并使用 `from-{color}`、`to-{color}` 来设置渐变的起始颜色和结束颜色。


| 类名 | 描述 | 例子 |
| --- | --- | --- |
| bg-gradient-to-{direction} | 设置渐变背景的方向，direction 可以是 t、r、b、l、tr、tl、br、bl等 | bg-gradient-to-r (从左到右渐变) |
| from-{color} | 设置渐变背景的起始颜色 | from-blue-500 |
| to-{color} | 设置渐变背景的结束颜色 | to-green-300 |
| via-{color} | 设置渐变中间的颜色（可选） | via-purple-400 |


## 实例


```css
<div class="bg-gradient-to-r from-blue-500 to-green-300 p-10 text-white">
  渐变背景从蓝色到绿色
</div>
```


**背景颜色透明度**（Opacity）：


Tailwind 也提供了控制背景透明度的工具类，使用 `bg-opacity-{value}` 来设置透明度值，`{value}` 从 0 到 100 的整数表示透明度的百分比。


| 类名 | 描述 | 例子 |
| --- | --- | --- |
| bg-opacity-{n} | 设置背景颜色的透明度 | bg-opacity-50 |
| bg-opacity-0 | 设置背景颜色完全透明 | bg-opacity-0 |
| bg-opacity-100 | 设置背景颜色完全不透明 | bg-opacity-100 |


## 实例


```css
<div class="bg-blue-500 bg-opacity-50 p-10 text-white">
  背景为半透明的蓝色
</div>
```


**使用 Tailwind 配置中的自定义背景颜色**：


你可以在 `tailwind.config.js` 配置文件中自定义背景颜色。通过在 `theme.extend` 部分的 `colors` 属性下定义颜色，你可以扩展默认的颜色集。


## 实例


```css
module.exports = {
  theme: {
    extend: {
      colors: {
        'custom-blue': '#1D4ED8',
        'custom-gray': '#4B5563',
      }
    }
  }
}
```


在 HTML 中使用自定义背景颜色：


## 实例


```css
<div class="bg-custom-blue p-10 text-white">
  使用自定义蓝色背景
</div>
```


### 综合实例


## 实例


```css
<!-- 背景颜色实例 -->
<div class="bg-blue-500 text-white p-6 mb-6">
    <h1 class="text-xl">蓝色背景</h1>
    <p>这是一个拥有蓝色背景的容器，文字颜色为白色。</p>
</div>

<!-- 渐变背景实例 -->
<div class="bg-gradient-to-r from-purple-500 via-pink-500 to-red-500 text-white p-6 mb-6">
    <h1 class="text-xl">渐变背景</h1>
    <p>这是一个线性渐变背景，从紫色到粉色再到红色。</p>
</div>

<!-- 背景透明度实例 -->
<div class="bg-green-500 bg-opacity-50 text-white p-6">
    <h1 class="text-xl">透明度背景</h1>
    <p>这是一个具有半透明绿色背景的容器。</p>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_bg1)

解析：**



**基本背景颜色**：


- `bg-blue-500`：设置背景颜色为蓝色。
- `text-white`：设置文本颜色为白色。



**渐变背景**：


- `bg-gradient-to-r`：设置渐变背景的方向为从左到右。
- `from-purple-500`：设置渐变的起始颜色为紫色。
- `to-red-500`：设置渐变的结束颜色为红色。



**背景透明度**：


- `bg-opacity-50`：设置背景颜色的透明度为 50%（半透明）。










	  AI 思考中...





			** [Tailwind CSS 排版](https://www.runoob.com/tailwindcss-typography.html)
			[Tailwind CSS 边框](https://www.runoob.com/tailwindcss-borders.html) **













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