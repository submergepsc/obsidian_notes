# 环境搭建

- Source: https://www.runoob.com/vue3/vue3-taskhub-config.html

我们将使用 Vite 快速构建项目 **TaskHub**，Vite 内容参考：[Vite 教程](https://www.runoob.com/vite-tutorial.html)。


### 1. 创建项目


打开终端，执行以下命令创建 Vite + Vue3 项目（选择 Script Setup 语法）：


```
# npm 命令
npm create vite@latest task-hub -- --template vue

# yarn 命令
yarn create vite task-hub --template vue

# pnpm 命令（推荐，速度更快）
pnpm create vite task-hub -- --template vue
```


执行成功后，输出如下：


![](https://www.runoob.com/wp-content/uploads/2026/01/42c3e0f7-05d6-4488-a356-f9ab783f3f38.png)


启动成功后，访问终端提示的本地地址（默认 http://localhost:5173/），即可看到 Vue3 初始页面。


![](https://www.runoob.com/wp-content/uploads/2026/01/1a466aa2-86bf-4384-9e4a-169795b965f2.png)


2. 项目目录


我们可以进入目录：


```
cd task-hub
```


如果安装了 VS Code，可以使用 VS Code 的 code 命令打开目录，VS Code 内容参考：[VS Code 教程](https://www.runoob.com/../vscode/vscode-tutorial.html)。


```
code .
```


启动后目录结构如下：


![](https://www.runoob.com/wp-content/uploads/2026/01/6afd1bea-4a92-417c-b522-2b8d737dcd2f.png)


其他相关命令：


```
# 安装依赖
npm install

# 启动
npm run dev
# 清理默认代码
```


### 2. 清理默认代码


删除 src/components/HelloWorld.vue。



清空 src/style.css。


修改 src/App.vue，代码如下：


## 实例


```javascript
<script setup>
// JS 逻辑
</script>

<template>
  <div>
    <h1>TaskHub</h1>
  </div>
</template>
```


### 引入 Tailwind CSS

安装并配置原子化 CSS 框架。


```
npm install tailwindcss @tailwindcss/vite
```


修改 vite.config.js：


## 实例


```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'
import path from 'path'

export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(), // 激活 Tailwind v4 引擎
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'), // 配置路径别名
    },
  },
})
```


在 v4 中，Tailwind 作为一个 Vite 插件运行，它会自动扫描你的 .vue 文件。


在 src/style.css 中引入：


在 Tailwind v4 中，所有的配置（主题、变量）都直接写在 CSS 里。 重置 src/style.css 如下：


## 实例


```javascript
@import "tailwindcss";

/* v4 定义主题变量的方式 */
@theme {
  --color-brand: #3b82f6;
  --radius-xl: 1rem;
}

/* 全局基础样式 */
@layer base {
  body {
    @apply bg-slate-50 text-slate-900 antialiased;
  }
}
```









	  AI 思考中...





			** [Vue3 任务管理系统](https://www.runoob.com/vue3-taskhub.html)
			[核心业务开发](https://www.runoob.com/vue3-taskhub-task.html) **













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