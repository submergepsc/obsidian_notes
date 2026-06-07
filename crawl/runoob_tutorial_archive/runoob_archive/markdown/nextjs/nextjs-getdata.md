# Next.js 数据获取

- Source: https://www.runoob.com/nextjs/nextjs-getdata.html

Next.js 提供了多种数据获取方式，允许你在不同的渲染阶段（例如，服务器端渲染、静态生成和客户端渲染）获取和展示数据。


## 客户端数据获取

有时你希望在页面加载后从客户端获取数据，而不是在构建时或服务器端获取，你可以使用 React 的 useEffect 钩子来处理客户端数据获取。


### 使用 useEffect 和 fetch

在 React 组件中使用 useEffect 钩子和 fetch API 获取数据。


useEffect 会在组件挂载后执行，可以在其中发起 API 请求并更新状态。


## app/posts/page.tsx 文件代码：


```javascript
// app/posts/page.tsx
'use client';
import { useEffect, useState } from 'react';

export default function PostsPage() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      const res = await fetch('https://jsonplaceholder.typicode.com/posts');
      const data = await res.json();
      setPosts(data);
    };

    fetchPosts();
  }, []);

  return (
    <div>
      <h1>RUNOOB 测试</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}
```


访问 http://localhost:3000/posts，显示结构如下：


![](https://www.runoob.com/wp-content/uploads/2025/02/fdc5ff5e-3b05-4797-88a2-fae0cade1bbd.png)

useEffect 会在客户端渲染后执行，适用于客户端渲染的数据。


- 在客户端获取数据，适合不需要在服务端渲染的内容。
- 可以根据用户交互或时间等因素动态获取数据。


**使用场景：**


- 动态加载的数据，比如无限滚动或分页。
- 用户操作后才获取的数据，比如点击按钮后获取数据。

---


## 服务端数据获取

服务端数据可以使用以下方式获取数据：


- fetch API
- ORM 或数据库


### 使用 fetch API


要使用 fetch API 获取数据，需要将你的组件转换为异步函数，并使用 await 来等待 fetch 调用。示例如下：


## app/posts/page.tsx 文件代码：


```javascript
// app/posts/page.tsx
export default async function Page() {
  const data = await fetch('https://jsonplaceholder.typicode.com/posts')
  const posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```


### 使用 ORM 或数据库

你也可以通过 ORM 或数据库来获取数据，只需将组件转换为异步函数，并等待数据库调用：


## app/posts/page.tsx 文件代码：


```javascript
// app/posts/page.tsx
import { db, posts } from '@/lib/db'

export default async function Page() {
  const allPosts = await db.select().from(posts)
  return (
    <ul>
      {allPosts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```









	  AI 思考中...





			** [Next.js 页面和路由](https://www.runoob.com/nextjs-pages-router.html)
			[Next.js CSS 样式](https://www.runoob.com/nextjs-css-styles.html) **













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