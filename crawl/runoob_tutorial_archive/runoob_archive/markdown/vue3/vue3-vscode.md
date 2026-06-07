# 使用 VSCode 开发 Vue

- Source: https://www.runoob.com/vue3/vue3-vscode.html

Visual Studio Code（简称 VS Code）是一个由微软开发的免费、开源的代码编辑器，支持多种编程语言，并提供了代码高亮、智能代码补全、代码重构、调试等功能。


Visual Studio Code 内置支持 Vue.js 的核心构建块：HTML、CSS 和 JavaScript。


VS Code 内置终端，可以直接在编辑器中运行命令行工具，如 npm、yarn 等，方便项目构建和管理。

如果你希望拥有更丰富的 Vue.js 开发环境，可以安装 Volar 和 Volar for TypeScript 扩展，这些扩展提供了 Vue.js 的智能提示


**
如果你还不了解 VS Code 或者还未安装，可以参考：[VSCode 教程](https://www.runoob.com/../vscode/vscode-tutorial.html)。


---

## 创建 Vue 项目


打开终端或命令提示符，输入以下命令：


```
npm create vue@latest
```


系统会提示输入项目名称，我这边输入 **runoob-vue3-app**：


```
Vue.js - The Progressive JavaScript Framework

? 请输入项目名称： › runoob-vue3-app
```


之后会有一些选项，可以根据自己的需求选择，或者一路回车：


```
Vue.js - The Progressive JavaScript Framework

> 请输入项目名称： … runoob-vue3-app
> 是否使用 TypeScript 语法？ … 否 / 是
> 是否启用 JSX 支持？ … 否 / 是
> 是否引入 Vue Router 进行单页面应用开发？ … 否 / 是
> 是否引入 Pinia 用于状态管理？ … 否 / 是
> 是否引入 Vitest 用于单元测试？ … 否 / 是
> 是否要引入一款端到端（End to End）测试工具？ › 不需要
> 是否引入 ESLint 用于代码质量检测？ › 否

正在初始化项目 /Users/tianqixin/runoob-vue3-app...

项目初始化完成，可执行以下命令：

  cd runoob-vue3-app
  npm install
  npm run dev
```


项目创建完成后，进入项目文件夹并安装依赖：


```
cd runoob-vue3-app
npm install
```


安装依赖可能也需要几分钟。


输入以下命令快速启动你的 Vue 应用：


```
npm run dev
```


![](https://www.runoob.com/wp-content/uploads/2024/12/5b86495e-b6ab-4e7d-ad42-7830f404cb52.png)


在浏览器中打开 http://localhost:5173，显示如下：


![](https://www.runoob.com/wp-content/uploads/2024/12/welcome-to-vue.png)


按下 Ctrl+C 可以停止 vue-cli-service 服务器。


---


## 在 VS Code 中打开 Vue 项目

从终端或命令提示符中进入我们创建的 Vue 项目文件夹 runoob-vue3-app，然后使用 **code** 命令让项目在 VS Code 中打开：


```
cd runoob-vue3-app
code .
```


VS Code 将启动并在文件资源管理器中显示你的 Vue 项目，显示如下：


![](https://www.runoob.com/wp-content/uploads/2024/12/ca088f16-c443-444d-b5ec-45d95f153817.png)


接下来展开 src 文件夹，选择 App.vue 文件，状态栏右下角也会提示安装 Vue - Official 扩展来支持 .vue 文件：

![](https://www.runoob.com/wp-content/uploads/2024/12/3658c9c1-9e77-4aa5-90f4-3ce2f2784c1e.png)

选择安装它即可。


安装完成后，.vue 文件被识别为 Vue.js 文件类型，并支持以下语言特性：

- **语法高亮**
- **括号匹配**
- **悬停描述**


![](https://www.runoob.com/wp-content/uploads/2024/12/vue-language-features.png)


### 智能提示 (IntelliSense)

在 App.vue 中输入代码时，你会看到 HTML、CSS 和 Vue.js 特有语法（如 v-bind、v-for）的智能提示。


![](https://www.runoob.com/wp-content/uploads/2024/12/suggestions.png)


在脚本部分，还可以看到 Vue.js 相关的 JavaScript 特性提示，比如 computed 属性。


### 跳转到定义、查看定义

通过安装的 Volar 扩展，VS Code 支持 Vue.js 语言服务。


放置光标在 App 上，右键选择 Peek Definition 查看定义信息，或者按下快捷键 **⌥F12**。


你会看到一个弹出的窗口展示 App 的定义信息。


![](https://www.runoob.com/wp-content/uploads/2024/12/peek-definition.png)


按下 **Esc** 按键关闭查看窗口。


### 修改并运行 "Hello World"


在 App.vue 中，将 HelloWorld 组件的 msg 自定义属性文本替换为 "Hello World!"：


## 实例


```javascript
<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="Hello World!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>
</template>
```


保存 App.vue 文件（快捷键 **⌘S** 或 **Ctrl+S**），然后通过以下命令重启服务器：


```
npm run dev
```


在浏览器中你将看到页面显示 "Hello World!"。


![](https://www.runoob.com/wp-content/uploads/2024/12/hello-world-vue-vscode.png)









	  AI 思考中...





			** [Vue3 声明式渲染](https://www.runoob.com/vue3-declarative-rendering.html)
			[Vue3 全局 API](https://www.runoob.com/vue3-global-api.html) **













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