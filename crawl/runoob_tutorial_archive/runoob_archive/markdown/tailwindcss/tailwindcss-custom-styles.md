# Tailwind CSS 自定义样式

- Source: https://www.runoob.com/tailwindcss/tailwindcss-custom-styles.html

Tailwind CSS 的自定义样式使用主要通过修改 tailwind.config.js 配置文件来实现。

Tailwind 提供了多种方式来进行自定义，包括自定义颜色、间距、字体、屏幕断点以及其他配置选项。


通过以下命令可以创建 tailwind.config.js 文件：


```
npx tailwindcss init
```


该命令将在项目根目录下生成一个默认配置文件。


### 自定义主题（theme）


在 tailwind.config.js 文件的 theme 部分，你可以定义颜色、字体、间距等。

例如，扩展默认的颜色或添加新的颜色：


```
module.exports = {
  theme: {
    extend: {
      colors: {
        cyan: '#9cdbff',
      }
    }
  }
}
```


这将添加一个名为 cyan 的新颜色，你可以在项目中使用 bg-cyan 或 text-cyan 这样的类名。


## 实例


```css
<div class="bg-cyan">自定义颜色</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_cs1)


### 自定义颜色 (Colors)

Tailwind 提供了一个默认的颜色系统，但你可以通过 **theme.extend** 来为项目添加或修改颜色。


```
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'custom-blue': '#1c64f2',
        'custom-gray': '#3a3a3a',
      },
    },
  },
};
```


```
在上面的例子中，custom-blue 和 custom-gray 被添加到了颜色系统中，你可以在 HTML 中像使用默认颜色一样使用它们：
```


## 实例


```css
<div class="bg-custom-blue text-white">自定义蓝色背景</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_cs2)


### 自定义间距 (Spacing)

Tailwind 的间距系统包括 m- (margin) 和 p- (padding) 类，默认的间距值可以通过 **theme.extend.spacing** 来进行扩展：


```
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      spacing: {
        '128': '32rem',  // 定义一个自定义的间距值
        '144': '36rem',
      },
    },
  },
};
```


这将允许你在 HTML 中使用自定义的间距：


## 实例


```css
<div class="p-128">自定义的内边距</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_cs3)


### 自定义字体 (Fonts)

Tailwind 也允许你自定义字体系列。你可以通过 **fontFamily** 来扩展字体设置：


```
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Helvetica', 'Arial', 'sans-serif'],
        'custom': ['"Open Sans"', 'Arial', 'sans-serif'],
      },
    },
  },
};
```


之后你可以使用 font-custom 类来应用自定义字体：


## 实例


```css
<div class="font-custom">这是自定义的字体</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_cs4)


### 自定义断点 (Breakpoints)

Tailwind 提供了五个响应式断点（sm, md, lg, xl, 2xl）。

你可以在 tailwind.config.js 中修改这些断点，或者添加自定义的断点：


```
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      screens: {
        'xs': '475px',  // 添加一个新的小屏幕断点
        'xxl': '1600px',  // 添加一个超大屏幕断点
      },
    },
  },
};
```


此时你可以使用 xs:w-64 或 xxl:w-96 类来设置不同断点下的宽度：


## 实例


```css
<div class="xs:w-64 xxl:w-96">自适应宽度</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_cs5)


### 自定义阴影 (Box Shadows)

你可以通过 boxShadow 属性来扩展阴影效果。


```
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      boxShadow: {
        'custom': '0 10px 15px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.1)',
      },
    },
  },
};
```


然后，你可以在 HTML 中应用这个自定义阴影：


## 实例


```css
<div class="shadow-custom">带有自定义阴影的元素</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_cs6)


---


## 使用插件扩展 Tailwind

除了修改配置文件，Tailwind 还允许你使用插件扩展功能，以便在项目中使用更多的工具类。


### 使用 Tailwind 插件

你可以安装第三方插件来添加额外的功能：


```
npm install @tailwindcss/forms
```


然后，在 tailwind.config.js 中添加插件：


```
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/forms'),
  ],
};
```


该插件为你提供了许多用于表单控件的实用工具类。


---


## 使用 @apply 来复用样式

如果你发现自己在多个地方使用相同的组合样式，可以通过 @apply 指令来复用它们。

例如，创建一个自定义类，将多个实用类组合在一起：


```
@tailwind base;
@tailwind components;
@tailwind utilities;

/* 在你的 CSS 文件中 */
.avatar {
  @apply w-16 h-16 rounded-full border-2 border-white;
}
```


编译 Tailwind CSS：


```
npx tailwindcss -i ./styles.css -o ./output.css --watch
```


编译后生成的 output.css 文件会将 @apply 替换为具体的 CSS 样式。


你可以将 .avatar 类应用到多个元素中，而不需要重复写所有的工具类：


## 实例


```css
<img class="avatar" src="image1.jpg" alt="头像1">
<img class="avatar" src="image2.jpg" alt="头像2">
```


---


## 使用 @layer 来定义自定义组件

Tailwind 允许你使用 @layer 指令来定义自定义的组件类。

例如，创建一个带有 Tailwind 样式的自定义按钮：


```
/* 在你的 CSS 文件中 */
@layer components {
  .btn {
    @apply px-4 py-2 bg-blue-500 text-white font-semibold rounded-lg;
  }

  .btn-danger {
    @apply px-4 py-2 bg-red-500 text-white font-semibold rounded-lg;
  }
}
```


然后在 HTML 中使用自定义按钮类：


## 实例


```css
<button class="btn">Primary Button</button>
<button class="btn-danger">Danger Button</button>
```


---


## 使用 variants 来扩展状态修饰符

在 tailwind.config.js 中，你可以使用 variants 来配置 Tailwind 是否应该为特定的状态生成工具类。

例如，为 hover 和 focus 状态添加更多的样式变体：


```
// tailwind.config.js
module.exports = {
  variants: {
    extend: {
      backgroundColor: ['active', 'disabled'],
      textColor: ['group-hover'],
    },
  },
};
```


这将生成更多的工具类，例如 bg-red-500 active:bg-blue-500，在活动状态下切换背景色。








	  AI 思考中...





			** [Tailwind CSS 重用样式](https://www.runoob.com/tailwindcss-reusing-styles.html)
			[Tailwind CSS 指令与函数](https://www.runoob.com/tailwindcss-functions-and-directives.html) **













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