# Tailwind CSS4 安装(NPM)

- Source: https://www.runoob.com/tailwindcss/tailwindcss4-installbynpm.html

在开始之前，确保你已经安装了 Node.js 和 npm，你可以通过以下命令检查它们是否已经安装：


```
node -v
npm -v
```


如果你的系统还不支持 Node.js 及 NPM 可以参考我们的 [Node.js 教程](https://www.runoob.com/httsp://www.runoob.com/nodejs/nodejs-tutorial.html)。


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


## 安装 Tailwind CSS


与 Tailwind CSS 3 相比较，Tailwind CSS 4 自动检测 HTML 和 JavaScript 等文件，省去了手动配置内容源的麻烦。


### npm 安装


从零开始使用 Tailwind CSS 的最简单和最快方法是通过 Tailwind CLI 工具。


通过 npm 安装 在本地项目中安装并配置 Tailwind CSS：


```
npm install tailwindcss @tailwindcss/cli
```


**1、在 CSS 中导入 Tailwind**: 在 CSS 文件中添加** @import "tailwindcss";**。


比如在 src/input.css 文件开头导入：


## src/input.css 文件


```css
@import "tailwindcss";
```


**2、启动 Tailwind CLI 构建流程**：运行 CLI 工具以扫描源文件中的类并构建 CSS。


```
npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch
```


**3、在 HTML 中开始使用 Tailwind**：将编译后的 CSS 文件添加到  中，并开始使用 Tailwind 的实用类来设置内容的样式。


## src/index.html 文件


```css
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="./output.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```


### 作为 Vite 插件安装

Vite 是一个现代化的前端构建工具，旨在通过利用现代浏览器的原生 ES 模块支持，提供快速的开发体验。
Vite 详细内容可以参见：[Vite 教程](https://www.runoob.com/../vue3/vite-tutorial.html)。


将 Tailwind CSS 作为 Vite 插件安装是将其与 Laravel、SvelteKit、React Router、Nuxt 和 SolidJS 等框架集成的最无缝的方式。


**1、安装 Tailwind CSS**

通过 npm 安装 tailwindcss 和 @tailwindcss/vite：


```
npm install tailwindcss @tailwindcss/vite
```


**2、配置 Vite 插件**

在 Vite 配置文件 **vite.config.ts** 中添加 @tailwindcss/vite 插件：


## vite.config.ts 文件


```css
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
})
```


**3、导入 Tailwind CSS**


在的 CSS 文件中添加 **@import** 以导入 Tailwind CSS：


```
@import "tailwindcss";
```


**4、启动构建流程**

运行构建流程，使用 **npm run dev** 或你在 package.json 文件中配置的其他命令：


```
npm run dev
```


** 5、在 HTML 中开始使用 Tailwind**

确保编译后的 CSS 已包含在  中（框架可能会自动处理），然后开始使用 Tailwind 的实用类来设置内容的样式。


## 实例


```css
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="/src/styles.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```


### 作为 PostCSS 插件安装

将 Tailwind CSS 作为 PostCSS 插件安装可以将其与 Next.js 和 Angular 等框架无缝结合。


**1、安装 Tailwind CSS**

通过 npm 安装 tailwindcss、@tailwindcss/postcss 和 postcss。


```
npm install tailwindcss @tailwindcss/postcss postcss
```


**2、将 Tailwind 添加到 PostCSS 配置中**

在项目的 postcss.config.mjs 文件中（或任何配置 PostCSS 的地方）添加 @tailwindcss/postcss。


## postcss.config.mjs 文件


```css
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  }
}
```


**3、导入 Tailwind CSS**

在 CSS 文件中添加 @import 以导入 Tailwind CSS。


```
@import "tailwindcss";
```


**4、启动构建流程**

运行构建流程，使用 npm run dev 或你在 package.json 文件中配置的其他命令。


```
npm run dev
```


**5、在 HTML 中开始使用 Tailwind**

确保编译后的 CSS 已包含在  中（框架可能会自动处理），然后开始使用 Tailwind 的实用类来设置内容的样式。


## 实例


```css
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="/dist/styles.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```









	  AI 思考中...





			** [Tailwind CSS 边框](https://www.runoob.com/tailwindcss-borders.html)
			[tailwind CSS 阴影](https://www.runoob.com/tailwindcss-shadow.html) **













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