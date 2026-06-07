# Tailwind CSS 阴影

- Source: https://www.runoob.com/tailwindcss/tailwindcss-shadow.html

在现代网页设计中，阴影效果是创建视觉层次和深度感的重要工具。

Tailwind CSS 提供了一套强大而灵活的阴影工具类，可以轻松实现各种阴影效果。

本文将全面介绍 Tailwind CSS 中的阴影系统，包括 box-shadow（盒阴影）、text-shadow（文字阴影）、阴影颜色和透明度的控制，以及内阴影效果的应用。


---


## 什么是 CSS 阴影？


在深入 Tailwind 的具体实现前，我们先理解 CSS 阴影的基本概念。


CSS 阴影主要分为两种类型：


- **盒阴影 (box-shadow)**：应用于元素的整个盒子模型
- **文字阴影 (text-shadow)**：仅应用于元素的文本内容


阴影效果可以：


- 增强元素的视觉层次
- 创建"浮动"效果
- 模拟光照和深度
- 突出重要内容


---


## Tailwind 中的 box-shadow


Tailwind 提供了一系列预设的 box-shadow 工具类，从细微到强烈共分为 6 个级别：


## 实例


```css
<div class="shadow-sm">小型阴影</div>
<div class="shadow">默认阴影</div>
<div class="shadow-md">中等阴影</div>
<div class="shadow-lg">大型阴影</div>
<div class="shadow-xl">超大阴影</div>
<div class="shadow-2xl">特大型阴影</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_shadow1)


### 阴影级别对比表


| 类名 | 描述 | 适用场景 |
| --- | --- | --- |
| shadow-sm | 非常细微的阴影 | 按钮悬停、轻微提升 |
| shadow | 默认阴影 (中等大小) | 卡片、常规元素 |
| shadow-md | 中等阴影 | 模态框、重要通知 |
| shadow-lg | 大型阴影 | 浮动面板、突出元素 |
| shadow-xl | 超大阴影 | 特殊强调元素 |
| shadow-2xl | 特大型阴影 | 需要非常明显突出的元素 |


### 代码示例与实践


## 实例


```css
<div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-md">
  <div class="text-xl font-medium text-black">Tailwind 阴影示例</div>
  <p class="text-gray-500">这是一个使用 shadow-md 的卡片示例</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_shadow2)


效果说明**：


- 创建了一个白色背景的卡片
- 使用了 `shadow-md` 类添加中等阴影
- 结合圆角 (`rounded-xl`) 使阴影效果更自然


---


## Tailwind 中的 text-shadow


Tailwind 默认不包含 text-shadow 工具类，但可以通过以下方式添加：


### 方法 1：使用插件


安装 `tailwindcss-textshadow` 插件：


## 实例


```css
npm install tailwindcss-textshadow
```


然后在 `tailwind.config.js` 中配置：


## 实例


```css
module.exports = {
  plugins: [
    require('tailwindcss-textshadow')
  ],
  theme: {
    textShadow: {
      'sm': '1px 1px 2px rgba(0, 0, 0, 0.5)',
      'DEFAULT': '2px 2px 4px rgba(0, 0, 0, 0.5)',
      'lg': '4px 4px 8px rgba(0, 0, 0, 0.5)',
    }
  }
}
```


使用示例：


## 实例


```css
<h1 class="text-shadow-lg">带阴影的标题</h1>
```


### 方法 2：自定义工具类


在 CSS 中添加：


## 实例


```css
@layer utilities {
  .text-shadow {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  }
  .text-shadow-sm {
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
  }
}
```


---


## 阴影颜色和透明度控制


Tailwind 允许你通过工具类组合控制阴影的颜色和透明度。


### 1. 使用阴影颜色工具类


## 实例


```css
<div class="shadow-lg shadow-blue-500/50">蓝色半透明阴影</div>
```


语法解析：


- `shadow-{color}`：设置阴影颜色 (如 blue-500)
- `/{opacity}`：设置阴影透明度 (如 50 表示 50%)


### 2. 可用颜色和透明度


Tailwind 支持所有内置颜色和任意透明度值：


## 实例


```css
<div class="shadow-lg shadow-red-400/30">红色半透明阴影</div>
<div class="shadow-lg shadow-emerald-300/80">翡翠绿强阴影</div>
<div class="shadow-lg shadow-purple-600/20">紫色淡阴影</div>
```


### 3. 自定义阴影颜色


在 `tailwind.config.js` 中扩展：


## 实例


```css
module.exports = {
  theme: {
    extend: {
      boxShadow: {
        'custom': '0 4px 6px -1px rgba(156, 39, 176, 0.3)',
      }
    }
  }
}
```


---


## 内阴影效果 (inset)


内阴影可以创建凹陷或压入的效果，常用于按钮、输入框等交互元素。


### 1. 使用预设内阴影类


## 实例


```css
<div class="shadow-inner">内阴影效果</div>
```


### 2. 自定义内阴影


在配置文件中添加：


## 实例


```css
module.exports = {
  theme: {
    extend: {
      boxShadow: {
        'inner-lg': 'inset 0 4px 6px 0 rgba(0, 0, 0, 0.1)',
      }
    }
  }
}
```


### 3. 实际应用示例


## 实例


```css
<button class="px-4 py-2 bg-gray-100 rounded-lg shadow-inner hover:shadow-inner-lg">
  点击按钮
</button>
```


**效果说明**：


- 默认状态有轻微内阴影
- 悬停时内阴影增强 (`hover:shadow-inner-lg`)
- 创建了按钮被按下的视觉效果


---


## 高级技巧与最佳实践


### 1. 组合使用内外阴影


## 实例


```css
<div class="shadow-lg shadow-inner">外阴影+内阴影组合</div>
```


### 2. 响应式阴影


## 实例


```css
<div class="shadow-sm md:shadow-lg">小屏小阴影，大屏大阴影</div>
```


### 3. 悬停和焦点状态


## 实例


```css
<button class="shadow hover:shadow-lg focus:shadow-outline">
  交互按钮
</button>
```


### 4. 阴影动画


## 实例


```css
<button class="shadow-md hover:shadow-xl transition-shadow duration-300">
  带过渡效果的按钮
</button>
```


---


## 练习挑战


- 创建一个卡片组件，默认有中等阴影，悬停时阴影变大并变色
- 设计一个带内阴影的输入框，获得焦点时内阴影消失
- 实现一个文字标题，使用 text-shadow 创造霓虹灯效果
- 组合使用内外阴影创建一个有立体感的按钮


---


## 总结要点


### 核心工具类速查表


| 功能 | 类名示例 | 说明 |
| --- | --- | --- |
| 盒阴影 | shadow, shadow-lg | 不同大小的外阴影 |
| 内阴影 | shadow-inner | 元素内部阴影 |
| 阴影颜色 | shadow-blue-500 | 设置阴影颜色 |
| 阴影透明度 | shadow-blue-500/50 | 设置阴影透明度 |
| 文字阴影 | text-shadow (需自定义) | 为文本添加阴影 |


### 最佳实践建议


- **适度使用**：阴影应该增强设计，而不是分散注意力
- **保持一致**：整个项目中保持相似的阴影层次
- **考虑性能**：过多复杂的阴影可能影响渲染性能
- **结合其他属性**：阴影与圆角、过渡效果配合使用更佳









	  AI 思考中...





			** [Tailwind CSS4 安装](https://www.runoob.com/tailwindcss4-installbynpm.html)
			[Tailwind CSS 交互状态与动画](https://www.runoob.com/tailwindcss-animations.html) **













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