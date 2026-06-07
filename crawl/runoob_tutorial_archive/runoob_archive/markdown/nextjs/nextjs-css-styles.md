# Next.js CSS 样式

- Source: https://www.runoob.com/nextjs/nextjs-css-styles.html

在 Next.js 中，样式的使用非常灵活，我们可以选择多种方式来为你的应用添加样式。


---


## 全局样式


全局样式是影响整个应用的 CSS 样式，它通常用于设置页面的基础样式，如字体、颜色、布局等。


Next.js 通过 app/layout.tsx 中引入全局 CSS 文件。

默认情况下 app 目录已经有了全局样式 **globals.css** 文件，如果不存在，你也可以创建一个新的 CSS 文件。


在 styles 目录下创建**globals.css** 文件，然后在 app/layout.tsx 中引入。


## app/globals.css 文件代码：


```javascript
/* app/globals.css */
body {
  padding: 20px 20px 60px;
  max-width: 680px;
  font-size:64px;
  margin: 0 auto;
  background-color: #F5F5FB;
  color: #333;
}
```


然后，在根布局（app/layout.tsx）中导入该文件，以便将样式应用到应用中每个路由：


## app/layout.tsx 文件代码：


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


**注意事项：**全局样式可以导入到 app 目录中的任何布局、页面或组件中。然而，由于 Next.js 使用 React 的内置样式表支持来与 Suspense 集成，当前的内置支持在你在路由之间导航时并不会移除样式表。因此，我们建议将 全局样式 用于真正的全局 CSS，而将 CSS 模块 用于作用域 CSS。


app/page.tsx 代码如下：


## 实例


```javascript
export default function Home() {
  return <div>Hello, Runoob!</div>;
}
```


访问 http://localhost:3000/，测试显示效果如下：


![](https://www.runoob.com/wp-content/uploads/2025/02/04d98673-f006-4f7a-b4c3-a208f4ece4cf.png)


---


## Sass

Next.js 还支持 Sass，这是一种更加功能丰富的 CSS 预处理器。


如果你更喜欢使用 Sass 来编写样式，可以通过安装相应的依赖来启用 Sass 内容可以参见 [Sass 教程](https://www.runoob.com/../sass/sass-tutorial.html)。


安装：


```
npm install sass
```


Next.js 与 Sass 集成，支持 .scss 和 .sass 扩展名及语法。

你还可以通过 CSS 模块使用组件级别的 Sass，扩展名为 .module.scss 或 .module.sass。


### 自定义 Sass 配置

如果你想配置 Sass 的选项，可以在 next.config.js 中使用 sassOptions 选项。


## 实例


```javascript
// next.config.ts
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  sassOptions: {
    additionalData: `$var: red;`, // 在每个 Sass 文件中自动注入这些样式
  },
}

export default nextConfig
```


通过这种方式，你可以配置一些默认的 Sass 数据，或者进行其他自定义设置。


创建一个 SCSS 文件，如 styles/Button.module.scss：


## 实例


```javascript
/* styles/Button.module.scss */
.button {
  padding: 10px 20px;
  background-color: #0070f3;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
```


在组件中使用 SCSS 模块：


## 实例


```javascript
// app/components/Button.tsx
import styles from '../styles/Button.module.scss';

export default function Button() {
  return <button className={styles.button}>Click Me</button>;
}
```









	  AI 思考中...





			** [Next.js 数据获取](https://www.runoob.com/nextjs-getdata.html)
			[Next.js Tailwind CSS](https://www.runoob.com/nextjs-tailwindcss.html) **













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