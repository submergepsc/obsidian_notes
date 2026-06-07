# Next.js 教程

- Source: https://www.runoob.com/nextjs/nextjs-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/02/nextjs.png)


Next.js 是一个基于 React 的开源框架，用于构建快速、现代化的 Web 应用程序。


Next.js 用于构建高性能的服务器端渲染（SSR）和静态生成（Static Generation）的现代 Web 应用。

Next.js 由 Vercel 公司开发和维护，旨在简化 React 应用的开发流程，同时提供强大的性能优化和开发体验。。


## 与 React 的关系

React 是一个用于构建用户界面的 JavaScript 库，而 Next.js 是在 React 上构建的框架。

React 关注于构建 UI 组件，而 Next.js 提供了更多的功能和结构，帮助开发者解决一些在 React 中较为繁琐的开发问题，如路由、数据获取、页面渲染等。


## 谁适合阅读本教程？


只要您具备 HTML 和 CSS 的基础知识，您就可以阅读本教程，进而开发出自己的网站。


Next.js 不仅适合个人开发者快速搭建项目，也适合大型团队构建复杂的全栈应用。


Next.js 的入门门槛较低，它基于 React 构建，而 React 是目前最流行的前端框架之一。

如果你已经对 React 有一定的了解，学习 Next.js 会更加轻松。


## 阅读本教程前，您需要了解的知识：


在您开始阅读本教程之前，您必须具备 HTML 、 CSS 和 JavaScript 的基础知识。如果您还不了解这些概念，那么建议您先阅读我们的这些教程: - [HTML 教程](https://www.runoob.com/../html/html-tutorial.html) - [CSS 教程](https://www.runoob.com/../css/css-tutorial.html) - [JavaScript 教程](https://www.runoob.com/../js/js-tutorial.html) - [Node.js 教程](https://www.runoob.com/../nodejs/nodejs-tutorial.html) ## Next.js 实例 默认情况下，Next.js 会在 pages 文件夹中创建一个 index.js 文件，这是应用的首页，我们可以把这个文件的代码修改为如下内容：


## Next.js 实例


```javascript
export default function Home() {
  return <div>Hello, World!</div>;
}
```


## 主要特性

- **文件系统路由：** Next.js 使用文件系统来自动化路由的创建。你只需要在 `pages` 目录下创建文件，它就会自动映射为相应的路由，不需要额外的路由配置。
- **静态生成（SSG）与服务端渲染（SSR）：** Next.js 支持这两种渲染方式，可以根据需要灵活选择。静态生成适用于大多数情况，尤其是内容不会频繁变化的页面，而 SSR 适用于需要动态获取数据的页面。
- **API 路由：** Next.js 允许你在应用中直接创建 API 路由，可以在 `pages/api` 目录下轻松创建后端 API 端点，处理前后端逻辑。
- **自动代码拆分：** 每个页面只会加载它所需的 JavaScript 代码，确保应用启动速度更快，减少不必要的资源消耗。
- **优化图片：** Next.js 内置了图片优化功能，使用 `next/image` 组件可以自动为图像选择最佳格式、压缩、懒加载等，以提升页面加载性能。
- **支持 TypeScript：** Next.js 默认支持 TypeScript，可以让开发者在开发过程中享受更强的类型检查。


## 参考链接

Next.js 官网：[https://nextjs.org/](https://nextjs.org/)

Next.js 官方文档：[https://nextjs.org/docs](https://nextjs.org/docs)


Github 源码：[https://github.com/vercel/next.js](https://github.com/vercel/next.js)








	  AI 思考中...






			[Next.js 简介](https://www.runoob.com/nextjs-intro.html) **













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