# Next.js 项目说明

- Source: https://www.runoob.com/nextjs/nextjs-project-intro.html

Next.js 项目由多个文件和文件夹组成，每个部分都有其特定的作用。

以下是对 Next.js 项目代码的基本解析，帮助你理解项目的结构和各个部分的功能。


** 从 Next.js 13 开始，Next.js 引入了基于文件系统的 App Router（app 目录），取代了传统的 pages 目录。新的 app 目录提供了更强大的功能，如嵌套路由、布局、服务器组件等。**

---


## 项目结构

一个使用 app 目录的 Next.js 项目通常包含以下文件和文件夹：


```
my-next-app/
├── node_modules/       # 项目依赖的第三方库
├── public/             # 静态资源文件夹
│   ├── favicon.ico     # 网站图标
│   └── ...             # 其他静态资源（如图片、字体等）
├── app/                # 应用路由目录（核心）
│   ├── layout.js       # 根布局组件
│   ├── page.js         # 首页组件
│   ├── about/          # 关于页面
│   │   └── page.js     # 关于页面组件
│   ├── blog/           # 博客页面
│   │   ├── page.js     # 博客列表页
│   │   └── [slug]/     # 动态路由
│   │       └── page.js # 博客详情页
│   └── ...             # 其他页面和路由
├── components/         # 可复用的 React 组件
├── styles/             # 样式文件
├── utils/              # 工具函数
├── package.json        # 项目配置和依赖管理
├── package-lock.json   # 依赖的精确版本锁定文件
├── next.config.js      # Next.js 配置文件
└── README.md           # 项目说明文档
```


---


## 核心文件解析


### app/layout.js

**app/layout.js** 是根布局文件，用于定义整个应用的布局结构。


**app/layout.js** 包裹所有页面，可以包含全局样式、元数据等。


## 实例


```javascript
export default function RootLayout({ children }) {
  return (
    <html>
      <body>{children}</body>
    </html>
  );
}
```


### app/page.js

**app/page.js** 是首页文件，对应路由 **/**。


## 实例


```javascript
export default function Home() {
  return (
    <div>
      <h1>Welcome to Next.js 13!</h1>
    </div>
  );
}
```


### app/about/page.js

**app/about/page.js** 是关于页面文件，对应路由 /about。


## 实例


```javascript
export default function About() {
  return (
    <div>
      <h1>About Us</h1>
      <p>This is the about page.</p>
    </div>
  );
}
```


### app/blog/[slug]/page.js


**app/blog/[slug]/page.js** 是动态路由文件，用于处理类似 **/blog/:slug** 的路由。


## 实例


```javascript
export default function BlogPost({ params }) {
  return (
    <div>
      <h1>Blog Post: {params.slug}</h1>
    </div>
  );
}
```


### app/loading.js

**app/loading.js** 加载状态文件，用于在页面加载时显示加载状态。


## 实例


```javascript
export default function Loading() {
  return <p>Loading...</p>;
}
```


### app/error.js

**app/error.js** 是错误页面文件，用于捕获并显示错误。


## 实例


```javascript
'use client'; // 标记为客户端组件

export default function Error({ error, reset }) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  );
}
```


### app/not-found.js

**app/not-found.js** 是 404 页面文件，用于显示未找到的页面。


## 实例


```javascript
export default function NotFound() {
  return (
    <div>
      <h2>Page Not Found</h2>
    </div>
  );
}
```


---


## 新特性解析


### 1、服务器组件（Server Components）

Next.js 13 默认使用服务器组件，减少了客户端 JavaScript 的加载量。


服务器组件可以直接访问后端数据，无需额外的 API 调用。


## 实例


```javascript
async function getData() {
  const res = await fetch('https://api.example.com/data');
  return res.json();
}

export default async function Page() {
  const data = await getData();
  return <div>{data.message}</div>;
}
```


### 2、客户端组件（Client Components）

如果需要使用 React 状态或浏览器 API，可以将组件标记为客户端组件。


使用 **'use client'** 指令。


## 实例


```javascript
'use client';

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```


### 3、嵌套布局（Nested Layouts）


可以在 app 目录中创建嵌套布局，每个子目录可以有自己的布局文件。


例如：


**app/dashboard/layout.js**：仪表盘页面的布局。


**app/dashboard/page.js**：仪表盘页面的内容。


### 4、流式渲染（Streaming）

Next.js 13 支持流式渲染，可以在页面加载时逐步渲染内容。


## 实例


```javascript
import { Suspense } from 'react';

export default function Page() {
  return (
    <div>
      <Suspense fallback={<p>Loading...</p>}>
        <SlowComponent />
      </Suspense>
    </div>
  );
}
```


---

## 运行项目


- **启动开发服务器**： - 运行 `npm run dev` 或 `yarn dev`，启动开发服务器。 - 打开浏览器访问 `http://localhost:3000`，查看应用。
- **构建生产环境代码**： - 运行 `npm run build` 或 `yarn build`，生成优化后的生产环境代码。
- **启动生产服务器**： - 运行 `npm run start` 或 `yarn start`，启动生产服务器。








	  AI 思考中...





			** [Next.js 组件与布局](https://www.runoob.com/nextjs-components-layout.html)














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