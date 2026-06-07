# Vue3 创建项目

- Source: https://www.runoob.com/vue3/vue3-create-project.html

在上一章节 [Vue3 安装](https://www.runoob.com/vue3-install.html) 我们使用了 **npm init** 命令创建过一个项目，本章节我们主要介绍 **npm create** 命令创建项目以及使用 **vue ui** 命令打开图形化的安装界面。


Vue 开发推荐的 IDE 配置是 [Visual Studio Code + Vue - Official 扩展](https://www.runoob.com/vue3-vscode.html)：


![](https://www.runoob.com/wp-content/uploads/2021/12/vue-office.png)


其他的 IDE 支持如下：


- Sublime Text 通过 [LSP-Volar](https://github.com/sublimelsp/LSP-volar) 支持。
- vim / Neovim 通过 [coc-volar](https://github.com/yaegassy/coc-volar) 支持。
- emacs 通过 [lsp-mode](https://emacs-lsp.github.io/lsp-mode/page/lsp-volar/) 支持。


---

## npm create 命令


使用 npm create 命令来创建 Vue 项目，通常是通过 Vite（Vue 官方推荐的构建工具）来创建 Vue 应用。

在 Vite 中，npm create 是用来执行脚手架工具（如 vite@latest）来快速生成一个新的项目模板。

Vite 详细内容可以参考：[Vite 教程](https://www.runoob.com/vite-tutorial.html)。


**npm create** 命令创建项目语法格式如下：


```
npm create vite@latest <project-name> --template vue
```


**说明：**


- `npm create` ：用于执行项目模板的命令，它会创建一个新的项目，并从给定的模板中初始化。
- `vite@latest` ：vite 是创建 Vue 3 项目的工具，`@latest` 是指定使用最新版的 Vite，确保你创建的项目是基于最新版本的 Vite。如果没有 `@latest`，`npm` 会尝试使用当前安装的版本。
- `
`：新创建项目的文件夹名称。命令会创建一个文件夹，并将模板代码放入其中。例如，运行 `npm create vite@latest my-vue-app --template vue` 会在当前目录下创建一个名为 `my-vue-app` 的文件夹，并将 Vue 项目的模板文件放入其中。 - `--template vue`：`--template vue` 指定了要使用的模板类型。Vite 支持多种模板，`vue` 是专门为 Vue 3 提供的模板。还有其他模板，如 `vanilla`、`react`、`svelte` 等。 接下来我们创建 runoob-vue3-app 项目：


```
npm create vite@latest
```


执行以上命令会让你先输入项目名，并选择一个框架：


```
> Project name: … runoob-vue3-app
? Select a framework: › - Use arrow-keys. Return to submit.
❯   Vanilla
    Vue
    React
    Preact
    Lit
    Svelte
    Solid
    Qwik
    Angular
    Others
```


Vite 支持多个模板，常见的有：


- `vue`: Vue 3 项目（默认使用 Vue 3）
- `vanilla`: 无框架的基本模板
- `react`: React 项目
- `svelte`: Svelte 项目
- `preact`: Preact 项目
- 还可以根据具体需求选择其他模板。


可以使用方向键来选择，我们选择 Vue，然后出现选项变体界面，我们可以选择 JavaScript 快速开始：


```
> Project name: … runoob-vue3-app
> Select a framework: › Vue
> Select a variant: › JavaScript

Scaffolding project in /Users/runoob/runoob-test/runoob-vue3-app...

Done. Now run:

  cd runoob-vue3-app
  npm install
  npm run dev
```


安装完成后，我们进入项目目录：


```
cd runoob-vue3-app
```


整个目录结构如下图：


![](https://www.runoob.com/wp-content/uploads/2021/12/npm-creat-vue-vite.png)


安装依赖，并启动应用：


```
npm install
npm run dev
```


然后打开 **http://localhost:5173/**，就可以看到应用界面了：


![](https://www.runoob.com/wp-content/uploads/2021/12/53627B96-0166-4FE1-B055-F8A3C3817B95.jpg)


另外我们可以在 **vite.config.js** 文件中设置自己的端口，比如以下设置端口后为 3000：


## 实例


```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],

  server: {
    port: 3000, // 自己规定的端口号
  },
})
```


---


## vue ui 命令


除了使用 **vue create** 命令创建项目，我们还可以使用可视化创建工具来创建项目。


运行命令：


```
$ vue ui
->  Starting GUI...
->  Ready on http://localhost:8000
...
```


执行以上命令，会在浏览器弹出一个项目管理的界面：


![](https://www.runoob.com/wp-content/uploads/2021/12/6C6FBF13-54BF-4DBC-8019-6442A51C03F3.jpg)


我们可以点击**"创建"**选项来创建一个项目，选择底部"在此创建项目"，页面上方也可以选择路径：


![](https://www.runoob.com/wp-content/uploads/2021/12/E13FFC51-7F39-4510-83DC-948772041083.jpeg)

然后输入我们的项目名称，选择包管理工具为 npm，然后点击下一步：

![](https://www.runoob.com/wp-content/uploads/2021/12/33B0E553-7AD4-4A5A-AF5C-20305C0F5793.jpeg)


配置选择默认即可:


![](https://www.runoob.com/wp-content/uploads/2021/12/69A83D7A-C7FB-478B-8DA0-40BF673F160F.jpeg)


接下来就等待完成安装，安装完成管理界面如下：


![](https://www.runoob.com/wp-content/uploads/2021/12/4AE552A2-2AE4-4B23-AECA-90CE7D29C047-scaled.jpeg)









	  AI 思考中...





			** [Vue3 项目打包](https://www.runoob.com/vue3-build.html)
			[Vue3 组合式 API](https://www.runoob.com/vue3-composition-api.html) **













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