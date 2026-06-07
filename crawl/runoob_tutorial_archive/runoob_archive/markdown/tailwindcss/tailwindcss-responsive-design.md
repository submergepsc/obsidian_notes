# Tailwind CSS 响应式设计

- Source: https://www.runoob.com/tailwindcss/tailwindcss-responsive-design.html

响应式设计是现代网页开发的重要组成部分，它确保网页在不同的屏幕尺寸上都有良好的显示效果。


Tailwind CSS 提供了非常方便的工具来实现响应式布局，其响应式设计主要通过 **断点** 和 **前缀** 来控制不同屏幕尺寸下的样式应用。

---


## 使用响应式工具类构建自适应用户界面

Tailwind CSS 中的每一个工具类都可以通过断点条件化应用，使得在 HTML 中构建复杂的响应式界面变得轻而易举。


### 1、确保视口设置正确


在开始之前，确保你已经在 HTML 文档的 `` 部分添加了以下视口元标签：


```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```


这一步确保网页内容在移动设备上可以正确缩放和显示。


### 2、通过断点前缀应用工具类

为了在某个断点上生效某工具类，只需要在类名前加上断点名称并用 **:** 分隔即可。


## 实例


```css
<!-- 默认宽度为 16，中等屏幕为 32，大屏幕为 48 -->
<img class="w-16 md:w-32 lg:w-48" src="...">
```


- 在屏幕宽度小于 768px 时，图片宽度为 `16`（`w-16`）。
- 在中等屏幕（768px 或更大）时，图片宽度变为 `32`（`md:w-32`）。
- 在大屏幕（1024px 或更大）时，图片宽度变为 `48`（`lg:w-48`）。


### 3、默认提供的五个断点

Tailwind CSS 默认支持以下五个断点，这些断点灵感来源于常见的设备分辨率：

| 断点名称 | 最小宽度 | 前缀 | 常用设备 |
| --- | --- | --- | --- |
| sm | 640px | sm: | 小屏幕（例如手机的横屏模式） |
| md | 768px | md: | 中等屏幕（例如平板设备） |
| lg | 1024px | lg: | 大屏幕（例如小型笔记本电脑） |
| xl | 1280px | xl: | 超大屏幕（例如台式显示器） |
| 2xl | 1536px | 2xl: | 超宽屏（例如更高分辨率的显示器） |


---


## 如何实现响应式设计


### 1、响应式布局控制


在 Tailwind 中，可以使用响应式前缀调整布局、字体、颜色、间距等。


## 实例


```css
<div class="text-center sm:text-left md:text-right">
  This text will be center-aligned on small screens, left-aligned on medium screens, and right-aligned on larger screens.
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_rd1)




解释**：

- 在小屏幕（`sm`）下，文本居中对齐（`text-center`）。
- 在中等屏幕（`md`）下，文本左对齐（`text-left`）。
- 在大屏幕及以上（`lg`）下，文本右对齐（`text-right`）。



### 2、响应式网格布局


通过使用响应式工具类，可以定义在不同屏幕尺寸下的列布局。


## 实例


```css
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4">
  <div class="bg-red-500">Item 1</div>
  <div class="bg-green-500">Item 2</div>
  <div class="bg-blue-500">Item 3</div>
  <div class="bg-yellow-500">Item 4</div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_rd2)


解释**：

- 在默认设置下，网格为单列（`grid-cols-1`）。
- 在小屏幕（640px 或更大）时，网格调整为两列（`sm:grid-cols-2`）。
- 在大屏幕（1024px 或更大）时，网格调整为四列（`lg:grid-cols-4`）。


### 3、自定义响应式断点


除了默认的五个断点，Tailwind 允许你通过 `tailwind.config.js` 自定义断点，以满足具体的项目需求。


## 实例


```css
module.exports = {
  theme: {
    screens: {
      'xs': '480px', // 超小屏幕
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
  },
}
```


自定义的断点可以和默认断点一样使用：


## 实例


```css
<div class="xs:text-sm sm:text-base lg:text-xl">
  Responsive text size.
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_rd3)



### 4、媒体查询类


Tailwind 提供自定义媒体查询，例如：


- **最小宽度**：`min-[...]`。
- **最大宽度**：`max-[...]`。


## 实例


```css
<div class="min-[640px]:bg-blue-500 max-[640px]:bg-red-500">
  This div changes color based on screen width.
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_rd4)


### 5、响应式隐藏和显示


通过类如 `hidden` 和 `block`，结合响应式前缀，可以隐藏或显示内容：


## 实例


```css
<div class="hidden sm:block md:hidden lg:block">
  在较大的屏幕尺寸上，该内容才会显示！！！
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_rd5)










	  AI 思考中...





			** [Tailwind CSS 状态处理](https://www.runoob.com/tailwindcss-state.html)
			[Tailwind CSS 深色模式](https://www.runoob.com/tailwindcss-darkmode.html) **













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