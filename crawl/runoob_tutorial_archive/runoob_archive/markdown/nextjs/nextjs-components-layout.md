# Next.js 组件与布局

- Source: https://www.runoob.com/nextjs/nextjs-components-layout.html

Next.js 的组件与布局功能为开发者提供了强大的工具，帮助构建模块化、可维护的 Web 应用。


| 功能 | 说明 |
| --- | --- |
| 组件 | 页面组件、UI 组件、功能组件，用于构建应用的各个部分。 |
| 布局 | 全局布局、嵌套布局、动态布局，用于定义页面结构和公共元素。 |
| 特殊文件(旧版本) | _app.js、_document.js、_error.js，用于定义全局布局和文档结构。 |


在 Next.js 13 中，app 目录替代了传统的 pages 目录，用于管理路由和页面结构。app 目录引入了更灵活的布局、路由、数据获取机制，以及增强的并行渲染能力。


app 目录结构示例:


```
├── app/
│   ├── page.js           # 默认首页
│   ├── about/
│   │   ├── page.js       # About 页
│   └── layout.js         # 根布局
└── public/                # 静态文件目录
```


---


## 组件


组件是构建 Next.js 应用的基本单元。它们可以是页面组件、UI 组件或功能组件。

在 Next.js 中，所有页面和布局基本上都是 React 组件。你可以像在任何 React 应用中一样创建和使用组件。


### 页面组件

页面组件是 Next.js 中路由的基础，每个页面组件对应一个路由。


页面组件通常存放在 app 或 pages 目录下。


## 实例


```javascript
// pages/about.js 或 app/about/page.js
export default function About() {
  return <div>About Page</div>;
}
```


### UI 组件

UI 组件是可复用的界面元素，例如按钮、卡片、导航栏等。


UI 组件通常存放在 components 目录下。


## 实例


```javascript
// components/Button.js
export default function Button({ children }) {
  return <button>{children}</button>;
}
```


### 功能组件

功能组件是实现特定功能的组件，例如数据获取、状态管理等。


功能组件通常存放在 hooks 或 utils 目录下。


## 实例


```javascript
// hooks/useData.js
import { useEffect, useState } from 'react';

export default function useData(url) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(url)
      .then((res) => res.json())
      .then((data) => setData(data));
  }, [url]);

  return data;
}
```


### 实例


**创建组件：**在 app/components/ 目录下创建 Hello.js，代码如下：


## 实例


```javascript
// app/components/Hello.js
const Hello = () => {
  return <h1>Hello, Next.js 13!</h1>;
};

export default Hello;
```


**使用组件：**在 app 目录下，页面组件会从 page.js 中导出，你可以在其中使用组件：


## 实例


```javascript
// app/page.js
import Hello from './components/Hello';

export default function Home() {
  return (
    <div>
      <Hello />
    </div>
  );
}
```


---


## 布局

布局是用于定义页面结构的组件，通常包含页眉、页脚、导航栏等公共元素。


### 全局布局

全局布局适用于整个应用程序，通常定义在 app/layout.js或 _app.js 中。


## 实例


```javascript
// pages/_app.js 或 app/layout.js
import Header from '../components/Header';
import Footer from '../components/Footer';

export default function Layout({ children }) {
  return (
    <div>
      <Header />
      <main>{children}</main>
      <Footer />
    </div>
  );
}
```


---


### 嵌套布局

嵌套布局允许为不同的路由段定义不同的布局。


在 app 目录中，每个路由段可以包含一个 layout.js 文件。


```
app/
├── layout.js        // 根布局
├── about/
│   ├── layout.js    // /about 的布局
│   └── page.js      // /about 页面
└── dashboard/
    ├── layout.js    // /dashboard 的布局
    └── page.js      // /dashboard 页面
```


## 实例


```javascript
// app/dashboard/layout.js
export default function DashboardLayout({ children }) {
  return (
    <div>
      <h1>Dashboard Layout</h1>
      {children}
    </div>
  );
}
```


### 动态布局


动态布局允许根据条件动态选择布局。


## 实例


```javascript
// app/layout.js
export default function Layout({ children, isDashboard }) {
  return (
    <div>
      {isDashboard ? <DashboardLayout>{children}</DashboardLayout> : <MainLayout>{children}</MainLayout>}
    </div>
  );
}
```


---


## 特殊文件（旧版本）


Next.js 提供了一些特殊文件，用于定义全局布局、文档结构和错误页面。


### _app.js

_app.js 是 Next.js 的全局组件，用于包装所有页面组件。


## 实例


```javascript
// pages/_app.js
import Layout from '../components/Layout';

export default function MyApp({ Component, pageProps }) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  );
}
```


### _document.js

_document.js 用于自定义 HTML 文档结构。


## 实例


```javascript
// pages/_document.js
import { Html, Head, Main, NextScript } from 'next/document';

export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
```


### _error.js

_error.js 用于自定义错误页面。


## 实例


```javascript
// pages/_error.js
export default function Error({ statusCode }) {
  return (
    <div>
      <h1>{statusCode} Error</h1>
      <p>Sorry, something went wrong.</p>
    </div>
  );
}
```









	  AI 思考中...





			** [Next.js 图片和字体](https://www.runoob.com/nextjs-images-and-fonts.html)
			[Next.js 项目说明](https://www.runoob.com/nextjs-project-intro.html) **













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