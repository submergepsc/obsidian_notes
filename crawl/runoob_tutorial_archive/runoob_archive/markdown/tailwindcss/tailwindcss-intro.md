# Tailwind CSS 简介

- Source: https://www.runoob.com/tailwindcss/tailwindcss-intro.html

Tailwind CSS 是一个实用优先的 CSS 框架，与传统的框架（如 Bootstrap、Foundation）不同，它没有预定义的组件，而是提供了一系列原子化的 CSS 类，允许你直接在 HTML 中应用样式。


Tailwind CSS 是一个工具优先的框架，意味着它提供了大量的预定义类，而不是预设的组件,这使得开发者可以构建几乎任何设计，而不需要编写 CSS。


Tailwind CSS 适合那些喜欢直接在 HTML 中使用类来控制样式的开发者，它使得快速原型制作和开发定制设计变得简单快捷。然而，它的这种"无预设"的方法也意味着需要更多的类名记忆和可能的陡峭学习曲线。


![](https://www.runoob.com/wp-content/uploads/2024/11/tailwindcss-intro1.png)


**核心特点：**


- **工具类优先（Utility-First）**：遵循工具类优先的流程，使用具有约束性的基本工具类来构建复杂的组件。
- **响应式设计**：使用响应式布局标识符（responsive modifiers），构建完全支持响应式布局的用户界面，以适应任何大小的屏幕。
- **鼠标悬停、聚焦以及其他状态**：使用条件标识符（conditional modifiers），可以为处于交互状态（如鼠标悬停、聚焦等）中的元素设置样式。
- **夜间模式（Dark Mode）**：通过在HTML代码中添加夜间模式标识符（dark mode modifier），直接让你的网站支持夜间模式。
- **重用样式**：通过创建可重用的抽象来管理冗余并保持项目的可维护性。
- **自定义整个框架**：通过自定义整个框架使其匹配你的需求，使用你的自定义样式对其进行扩展。


以下是一个简单的 Tailwind CSS 实例：`` 元素显示为一个蓝色背景、白色文字、中等内边距和大圆角的框，内容为 "Hello, Tailwind CSS!"。


## Tailwind CSS 实例


```css
<div class="bg-blue-500 text-white p-4 rounded-lg">
  Hello, Tailwind CSS!
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_default)

说明：**


- `bg-blue-500`：设置背景颜色为蓝色（blue），具体是蓝色调色板中的第500级。
- `text-white`：设置文本颜色为白色。
- `p-4`：设置内边距（padding）为中等大小（16px）。
- `rounded-lg`：设置圆角为大尺寸（8px）。


Tailwind CSS 与传统的框架（如 Bootstrap、Foundation）不同，它没有预定义的组件，而是提供了一系列原子化的 CSS 类，允许你直接在 HTML 中应用样式。


| 特性 | Tailwind CSS | Bootstrap |
| --- | --- | --- |
| 样式方式 | 原子化类名 | 组件化结构 |
| 定制化 | 强大且灵活 | 依赖变量，扩展较复杂 |
| 学习成本 | 较低，理解类名即可 | 需要熟悉组件和网格系统 |
| 社区生态 | 增长迅速，插件丰富 | 成熟但略显传统 |
| 体积优化 | 支持 PurgeCSS 移除未用样式 | 需手动优化 |

---


## Tailwind CSS 的核心理念



**实用类优先**


- 每个类只完成一个具体任务，比如 `text-center` 是居中，`mt-4` 是添加上边距。
- 类名简单直观，几乎不用记忆复杂的 CSS 属性。



**无组件限制**


- 不提供像按钮、导航栏这样的现成组件。所有样式都通过类名组合实现。
- 提供极大的自由度，适用于自定义设计需求。



**快速开发**


- 在 HTML 中直接写样式，不需要频繁切换到 CSS 文件。
- 减少样式覆盖和冗余 CSS 的问题。

---


## Tailwind CSS 的适用场景


- **快速原型开发** 快速设计和调整页面，无需关心样式的重构问题。
- **团队协作** 统一使用配置文件，避免样式冲突，维护成本低。
- **响应式布局** 内置响应式设计支持，轻松实现多设备兼容。
- **大中型项目** 配合工具（如 PurgeCSS）优化输出 CSS 文件，适应复杂项目需求。









	  AI 思考中...





			** [Tailwind CSS 教程](https://www.runoob.com/tailwindcss-tutorial.html)
			[Tailwind CSS 安装(CDN)](https://www.runoob.com/tailwindcss-installbycdn.html) **













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