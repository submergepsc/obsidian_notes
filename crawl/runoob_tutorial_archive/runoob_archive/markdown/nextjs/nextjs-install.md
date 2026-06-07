# Next.js 安装

- Source: https://www.runoob.com/nextjs/nextjs-install.html

在开始之前，确保你已经安装了 Node.js 和 npm，你可以通过以下命令检查它们是否已经安装：


```
node -v
npm -v
```


如果你的系统还不支持 Node.js 及 NPM 可以参考我们的 [Node.js 教程](https://www.runoob.com/../nodejs/nodejs-tutorial.html)。


国内使用 npm 速度很慢，你可以使用淘宝定制的 cnpm (gzip 压缩支持) 命令行工具代替默认的 npm:


```
$ npm install -g cnpm --registry=https://registry.npmmirror.com
$ npm config set registry https://registry.npmmirror.com
```


这样就可以使用 cnpm 命令来安装模块了：


```
$ cnpm install [name]
```


更多信息可以查阅：[http://npm.taobao.org/](http://npm.taobao.org/)。


---


## 使用 create-react-app 快速构建 Next.js 开发环境


Next.js 提供了一个官方的脚手架工具 create-next-app，用于快速搭建项目。


create-react-app 是来自于 Facebook，通过该命令我们无需配置就能快速构建 Next.js 开发环境。


create-react-app 自动创建的项目是基于 Webpack + ES6 。


执行以下命令创建项目：


```
npx create-next-app@latest my-next-app
```


安装时，您将看到以下提示，一路回车即可：


```
Would you like to use TypeScript? No / Yes
Would you like to use ESLint? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to use Turbopack for `next dev`?  No / Yes
Would you like to customize the import alias (`@/*` by default)? No / Yes
What import alias would you like configured? @/*
```


- 使用 `create-next-app` 脚手架工具创建一个新的 Next.js 项目。
- `my-next-app` 是项目的名字，你可以根据需要修改为任何名称。
- 它会自动安装项目所需的依赖。


运行该命令后，create-next-app 会自动完成以下操作：



- 创建一个名为 my-next-app 的文件夹。
- 初始化项目，安装必要的依赖。
- 创建基本的项目结构，包括 app 文件夹、public 文件夹、package.json 文件等。


![](https://www.runoob.com/wp-content/uploads/2025/02/646a5876-b3cd-4c98-bd34-936f2dd6cb49.png)


创建完成后，进入项目目录：


```
cd my-next-app
```


在项目目录中，运行以下命令启动开发服务器：


```
npm run dev
```


或者如果你使用 yarn：


```
yarn dev
```


开发服务器默认运行在 **http://localhost:3000**，打开浏览器，访问** http://localhost:3000**，你应该会看到 Next.js 的默认欢迎页面。


![](https://www.runoob.com/wp-content/uploads/2025/02/6193c250-7fc6-4005-8393-ab40d919fe7f.png)


我们可以修改 app 目录下的 page.tsx 文件，修改后的代码为：


## app/page.tsx


```javascript
export default function Home() {
    return <div>Hello, World!</div>;
}
```


访问** http://localhost:3000**，显示如下：


```
Hello, World!
```


---


## 手动安装 Next.js

要手动创建一个新的 Next.js 应用，首先安装所需的包：


```
npm install next@latest react@latest react-dom@latest
```


接下来，打开你的 package.json 文件并添加以下脚本：


## package.json 文件：


```javascript
{
  "scripts": {
    "dev": "next dev",        // 以开发模式启动 Next.js
    "build": "next build",    // 构建应用以供生产使用
    "start": "next start",    // 启动 Next.js 生产环境服务器
    "lint": "next lint"       // 配置 Next.js 的内置 ESLint
  }
}
```


这些脚本代表了开发应用程序的不同阶段：


- **dev**：运行 `next dev`，以开发模式启动 Next.js。
- **build**：运行 `next build`，为生产环境构建应用。
- **start**：运行 `next start`，启动 Next.js 生产服务器。
- **lint**：运行 `next lint`，设置 Next.js 的内置 ESLint 配置。


### 创建应用目录

Next.js 使用文件系统路由，这意味着应用程序的路由由文件结构决定。

创建一个 app 文件夹，然后添加一个 layout.tsx 和一个 page.tsx 文件。当用户访问应用根路径 **/** 时，这些文件会被渲染。


#### 创建根布局文件


在 `app/layout.tsx` 中创建根布局文件，包含所需的 `` 和 `` 标签：


## 实例


```javascript
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```


#### 创建首页文件

最后，在 app/page.tsx 中创建一个主页文件，加入初始内容：


## 实例


```javascript
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```


### 注意事项


- 如果你忘记创建 `layout.tsx`，Next.js 会在运行开发服务器（`next dev`）时自动创建这个文件。
- 你可以选择性地在项目根目录中使用 `src` 目录，将应用代码与配置文件分开。


### 创建 public 文件夹（可选）


你可以选择在项目根目录创建一个 `public` 文件夹，用于存储静态资源，如图片、字体等。`public` 文件夹中的文件可以通过 `/` 路径来引用。


这样，你就完成了手动安装并初始化一个基本的 Next.js 项目结构。


### 运行开发服务器

运行以下命令启动开发服务器：


```
npm run dev
```


访问 http://localhost:3000 查看应用。


编辑 **app/page.tsx** 文件并保存，之后可以在浏览器中看到更新后的结果。








	  AI 思考中...





			** [Next.js 简介](https://www.runoob.com/nextjs-intro.html)
			[Next.js 目录结构](https://www.runoob.com/nextjs-layouts-and-pages.html) **













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