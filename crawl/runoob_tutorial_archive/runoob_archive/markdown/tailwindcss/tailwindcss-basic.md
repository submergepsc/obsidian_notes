# Tailwind CSS 基础概念

- Source: https://www.runoob.com/tailwindcss/tailwindcss-basic.html

Tailwind CSS 是一个高度可定制的 CSS 框架，它提供了一套预定义的工具类，允许开发者快速构建和设计用户界面。


以下是 Tailwind CSS 的一些基础概念和用法：


| 概念 | 说明 |
| --- | --- |
| 工具类 (Utility-First) | Tailwind CSS 的核心是工具类，用于快速设置样式，直接应用到 HTML 元素上。 |
| 响应式前缀 | 使用如 sm:, md:, lg:, xl: 的前缀来控制不同屏幕尺寸下的样式。 |
| 颜色和尺寸 | 提供了预定义的颜色（如 bg-red-500）和尺寸（如 text-lg）来快速设置样式。 |
| 间距 (Spacing) | 通过 p-, m-, pt-, pr- 等类控制内边距和外边距。 |
| 布局 (Layout) | 提供 flex, grid, float 等类来实现布局控制。 |
| 文本样式 | 包括文本对齐、字体样式、颜色和转换的实用类，如 text-center, font-bold, uppercase。 |
| 背景和边框 | 提供背景颜色、背景图片、边框样式和颜色的工具类，如 bg-gray-200, border-red-500。 |
| 悬停和状态 | 使用 hover:, focus:, active: 等前缀为交互状态定义样式。 |
| 尺寸 (Sizing) | 使用 w-, h- 类控制宽度和高度，如 w-64, h-screen。 |
| 可见性 (Visibility) | 使用 visible, invisible 等类控制元素的可见性。 |
| 栅格系统 (Grid System) | 提供基于 CSS Grid 的工具类，如 grid, grid-cols-3, col-span-2，实现响应式网格布局。 |
| 自定义配置 | 通过 tailwind.config.js 自定义颜色、间距、字体大小等，以适应项目需求。 |
| 暗色模式 (Dark Mode) | 支持暗色模式，通过 dark: 前缀设置样式，并可在配置中启用暗色模式功能。 |
| 插件 (Plugins) | 通过插件扩展功能，添加自定义的工具类或功能。 |
| 指令 (Directives) | 在 CSS 文件中使用 @tailwind 指令引入不同层次的样式，如 base, components, utilities。 |


## 概念详解


### 1. 工具类（Utility-First）


Tailwind 的工具类可以让开发者快速定义样式，无需手动编写 CSS。


## 实例


```css
<div class="text-center text-blue-500 font-bold">
  Tailwind Utility Classes
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic1)


解析：


- `text-center`：居中对齐。
- `text-blue-500`：蓝色文字。
- `font-bold`：加粗字体。


---


### 2. 响应式前缀


通过前缀设置不同屏幕尺寸下的样式。


## 实例


```css
<div class="bg-red-500 sm:bg-green-500 md:bg-blue-500 lg:bg-yellow-500">
  Responsive Example
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic2)


解析：


- 默认：红色背景。
- 小屏幕（≥640px）：绿色背景。
- 中屏幕（≥768px）：蓝色背景。
- 大屏幕（≥1024px）：黄色背景。


---


### 3. 颜色和尺寸


Tailwind 提供了丰富的预定义颜色和尺寸，便于快速应用。


## 实例


```css
<p class="text-lg text-gray-600">
  Text with pre-defined size and color
</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic3)


解析：


- `text-lg`：文字大小。
- `text-gray-600`：灰色文字。


---


### 4. 间距（Spacing）


通过间距工具类设置元素的内外边距。


## 实例


```css
<div class="p-4 m-8">
  Padding and Margin Example
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic4)


解析：


- `p-4`：内边距为 1rem。
- `m-8`：外边距为 2rem。


---


### 5. 布局（Layout）


提供的类可以快速实现灵活的布局方式，如 Flexbox 和 Grid。


## 实例


```css
<div class="flex justify-between items-center">
  <div>Item 1</div>
  <div>Item 2</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic5-1)


Grid 实例：**


## 实例


```css
<div class="grid grid-cols-3 gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic5-2)


---


### 6. 文本样式


控制文本的对齐、颜色、大小和其他样式。


## 实例


```css
<p class="text-center font-semibold text-red-500">
  Centered Bold Text
</p>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic6)


---


### 7. 背景和边框


通过工具类设置背景颜色、图片和边框样式。


## 实例


```css
<div class="bg-yellow-200 border border-gray-400">
  Background and Border Example
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic7)


---


### 8. 悬停和状态


为交互元素设置状态样式。


## 实例


```css
<button class="bg-blue-500 hover:bg-blue-700 text-white">
  Hover Me
</button>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic8)


---


### 9. 尺寸（Sizing）


设置元素的宽度和高度。


## 实例


```css
<div class="w-64 h-32 bg-gray-300">
  Width and Height
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic9)


---


### 10. 可见性（Visibility）


控制元素的显示与隐藏。


## 实例


```css
<div class="invisible sm:visible">
  Visible only on small screens
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic10)


---


### 11. 栅格系统（Grid System）


使用 Tailwind 的 Grid 工具类创建网格布局。


## 实例


```css
<div class="grid grid-cols-3 gap-2">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic11)


---


### 12. 自定义配置


通过配置文件自定义设计系统。


## 实例


```css
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#1D4ED8',
      },
    },
  },
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic12)


---


### 13. 暗色模式


启用暗模式并定义样式。


## 实例


```css
<div class="bg-white dark:bg-black text-black dark:text-white">
  Dark Mode Example
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_basic13)


---


### 14. 插件


通过插件扩展 Tailwind 的功能。


## 实例


```css
// tailwind.config.js
const plugin = require('tailwindcss/plugin')
module.exports = {
  plugins: [
    plugin(function({ addUtilities }) {
      addUtilities({
        '.rotate-45': {
          transform: 'rotate(45deg)',
        },
      })
    }),
  ],
}
```


---


### 15. 指令（Directives）


通过 `@tailwind` 指令加载 Tailwind 的不同层。


## 实例


```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```










	  AI 思考中...





			** [Tailwind CSS3 安装(NPM)](https://www.runoob.com/tailwindcss-installbynpm.html)
			[Tailwind CSS 配置](https://www.runoob.com/tailwindcss-config.html) **













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