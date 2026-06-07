# Next.js Tailwind CSS

- Source: https://www.runoob.com/nextjs/nextjs-tailwindcss.html

在 Next.js 项目中使用 Tailwind CSS 是一个很流行的选择，因为它提供了一种实用工具优先的方法来编写 CSS，使得你可以直接在类名中应用样式，这种方法使得样式编写更加简洁和直观。


Tailwind CSS 教程：[https://www.runoob.com/tailwindcss/tailwindcss-tutorial.html](https://www.runoob.com/../tailwindcss/tailwindcss-tutorial.html)


Tailwind CSS 官网：[https://tailwindcss.com/](https://tailwindcss.com/)


Github 地址：[https://github.com/tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)


Tailwind CSS 是一个功能强大的 CSS 框架，它通过实用工具优先的方法使得样式编写更加简洁和模块化。与传统的基于类的 CSS 框架不同，Tailwind 提供了一组低级实用工具类，这些类可以直接在 HTML 元素上使用，以便快速、灵活地构建自定义设计。


以下是如何在 Next.js 项目中使用 Tailwind CSS 的详细步骤。


### 1. 安装 Tailwind CSS

如果你是从零开始创建一个新的 Next.js 项目，可以使用 create-react-app，如果你已经有一个现有的 React 项目，可以跳过项目创建步骤。


** 创建新的 Next.js 项目：**


```
npx create-next-app@latest my-next-app
```


创建的时候，就会提示是否安装 Tailwind CSS，我们可以选 Yes：


```
...
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
...
```


** 安装 Tailwind CSS**

页可以在你的项目目录中运行以下命令来安装 Tailwind CSS 及其所需的依赖项：


```
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```


这将创建一个 tailwind.config.ts 文件和一个 postcss.config.mjs 文件。


### 2. 配置 Tailwind CSS

在 Tailwind 配置文件 tailwind.config.ts 中，添加将使用 Tailwind 类名的文件路径。


一般默认情况下，都配置好了，我们无需修改：


## 实例


```javascript
import type { Config } from "tailwindcss";

export default {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",  // 注意添加了  app  目录。
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
    },
  },
  plugins: [],
} satisfies Config;
```


我们无需修改 postcss.config.mjs 文件。


### 3. 添加 Tailwind 的基础样式

将 Tailwind CSS 指令添加到应用程序的全局样式表中，Tailwind 会使用这些指令来注入它生成的样式。


在你的项目中，打开 app/globals.css 文件，并添加以下内容来包含 Tailwind 的基础样式、组件样式和实用工具样式：


```
/* app/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```


在根布局 app/layout.tsx 中导入 globals.css 样式表，将样式应用到应用中的每个路由：


## 实例


```javascript
// app/layout.tsx
// 这些样式会应用到应用中的每个路由
import './globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>{children}</body>
    </html>
  )
}
```


### 4. 使用 Tailwind CSS 编写样式

安装 Tailwind CSS 并添加全局样式后，你可以在应用中使用 Tailwind 的实用工具类：


## app/page.tsx 文件代码：


```javascript
// app/page.tsx
export default function Home() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-lg">
        <h1 className="text-2xl font-bold text-gray-900">Hello, RUNOOB!</h1>
        <p className="mt-4 text-gray-600">菜鸟教程，学的不仅是技术，更是梦想！</p>
        <button className="mt-6 bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700">
         点我试试
        </button>
      </div>
    </div>
  );
}
```


运行：


```
npm run dev
```


然后打开你的浏览器并导航到 http://localhost:3000，你应该会看到一个使用 Tailwind CSS 样式的简单 React 应用。


![](https://www.runoob.com/wp-content/uploads/2024/06/a933248c846c774e03ef8f4976d5675d.png)


通过以上步骤，你已经成功地在 Next.js 项目中集成了 Tailwind CSS，并使用它来编写样式。Tailwind CSS 的实用工具类名使得你可以快速地为你的组件添加样式，同时保持样式代码的简洁和模块化。








	  AI 思考中...





			** [Next.js CSS 样式](https://www.runoob.com/nextjs-css-styles.html)
			[Next.js 图片和字体](https://www.runoob.com/nextjs-images-and-fonts.html) **













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