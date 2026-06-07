# Next.js 页面和路由

- Source: https://www.runoob.com/nextjs/nextjs-pages-router.html

Next.js 使用文件系统路由，意味着你应用中的页面是由文件系统的结构来自动决定的，每个文件和文件夹都与一个路由相对应，而不需要像传统的 React 路由那样显式地配置每个路径，这使得开发过程更加直观和简便。


- **页面与路由的关系：**在 Next.js 中，每个页面都是由 app/ 或 pages/ 目录中的文件自动映射到一个路由，每个文件的路径和文件名决定了该页面的 URL。
- **基本页面结构：**在 Next.js 中，一个 页面 是任何 app/ 或 pages/ 目录下的 .tsx 或 .js 文件，每个页面的文件都会自动成为应用的一个路由。


Next.js 的路由系统非常灵活，支持静态页面、动态路由以及嵌套路由，使得开发者可以轻松实现复杂的应用结构。


- **文件系统路由**：页面和路由是通过 `app/` 或 `pages/` 目录中的文件结构自动映射的。
- **动态路由**：可以通过方括号 (`[ ]`) 来创建动态路由，处理 URL 中的动态参数。
- **嵌套路由**：可以通过子目录来创建嵌套路由，实现多级路由结构。
- **路由导航**：使用 `next/link` 组件实现页面间的导航。


**

Next.js 13 引入了新的 app 目录，它与传统的 pages 目录共存，并提供了更灵活的路由和布局组织方式。


假设项目目录结构如下：


```
app/
├── page.tsx             # 对应根路径 /
├── about/
│   └── page.tsx         # 对应 /about
├── [slug]/
│   └── page.tsx         # 对应动态路径，如 /[slug]
```


- **`page.tsx`** 文件：每个页面都会有一个 `page.tsx` 文件，这个文件就是该路由对应的组件内容。
- **动态路由**：如果页面路径中有动态参数，你可以使用方括号（`[ ]`）来定义动态路由。例如 `[slug]` 表示该路径可以接受任何值来作为 `slug` 参数。


### 默认的页面和路由

Next.js 自动为你的 app/ 或 pages/ 文件夹中的文件创建路由。

以下是一些常见的路由示例：

- `app/page.tsx` 对应 `/` 路径。
- `app/about/page.tsx` 对应 `/about` 路径。
- `app/[slug]/page.tsx` 对应 `/[slug]`，会匹配任何 URL 路径，如 `/post/1` 或 `/product/xyz`。


### 动态路由

动态路由允许你根据 URL 中的不同部分动态渲染页面。

在 Next.js 中，你可以通过创建带有方括号的文件夹或文件来实现动态路由。


例如，假设你希望根据不同的文章 ID 来渲染不同的内容，你可以这样做：


```
app/
├── [id]/
│   └── page.tsx        # 动态路由，匹配任何 `/[id]` 的路径
```


`[id]` 是动态路由的占位符，它可以匹配任何 URL 中的 `id` 参数。



### 获取动态路由参数

在 Next.js 中，可以通过 useParams 钩子来访问动态路由参数。例如：


## 实例


```javascript
'use client';

import { useParams } from 'next/navigation';

export default function Post() {
  const params = useParams();
  const { id } = params;  // 获取动态路由参数 `id`

  return <div>Post ID: {id}</div>;
}
```


当用户访问 /post/123 时，id 会被自动赋值为 123，并在页面中显示。


### 嵌套路由

Next.js 还支持嵌套路由，即在某个路由下创建子路由。例如：


```
app/
├── about/
│   ├── page.tsx          # /about 路由页面
│   ├── team/
│   │   └── page.tsx      # /about/team 子路由页面
│   └── contact/
│       └── page.tsx      # /about/contact 子路由页面
```


这种方式使得你的应用具有层级结构，同时保留了 URL 路径的可读性。


### 自定义路由规则

如果你希望自定义路由的行为，可以通过 next.config.js 文件来配置。但大部分常见的路由需求 Next.js 已经提供了开箱即用的功能，无需额外配置。


### 特殊的页面和路由功能

- **`_app.js` 和 `_document.js`**：在 Next.js 中，`_app.js` 是应用的根组件，允许你为所有页面提供公共的布局和状态。`_document.js` 主要用于修改 HTML 文档的结构（例如 `head` 和 `body` 标签）。
- **`_error.js`**：可以自定义错误页面，处理 404 或其他类型的错误。


---


## 实例

### 创建静态页面

让我们以创建一个简单的静态页面为例，创建一个 about/page.tsx 文件，内容如下：


## 实例


```javascript
export default function AboutPage() {
  return <h1>About Us</h1>;
}
```


访问 /about 路径时，Next.js 会自动渲染该页面。


![](https://www.runoob.com/wp-content/uploads/2025/02/18d8f74d-f4e7-46d0-b877-df17b9e5fa35.png)


### 动态路由的使用


假设你要根据文章 ID 渲染页面，创建一个 app/[id]/page.tsx 文件，内容如下：


## 实例


```javascript
import { useParams } from 'next/navigation';

export default function PostPage() {
  const { id } = useParams();

  return <h1>Post ID: {id}</h1>;
}
```


访问 /123 会显示 Post ID: 123。


### 路由导航

Next.js 使用 next/link 提供的组件来进行路由导航。你可以在页面中添加链接，跳转到其他页面。


## 实例


```javascript
import Link from 'next/link';

export default function HomePage() {
  return (
    <div>
      <h1>Welcome to Next.js!</h1>
      <Link href="/about">About Us</Link>
    </div>
  );
}
```


`` 组件用于在页面之间导航，并保持单页面应用（SPA）的体验。









	  AI 思考中...





			** [Next.js 目录结构](https://www.runoob.com/nextjs-layouts-and-pages.html)
			[Next.js 数据获取](https://www.runoob.com/nextjs-getdata.html) **













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