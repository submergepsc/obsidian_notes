# Vue3 目录结构

- Source: https://www.runoob.com/vue3/vue3-directory-structure.html

上一章节中我们使用了 npm 安装项目(Vue-cli 和 Vite)，我们在 IDE（Vscode、Atom 等） 中打开该目录，结构如下所示：


**命令行工具 vue-cli（runoob-vue3-test）：**


![](https://www.runoob.com/wp-content/uploads/2021/02/7C26D06C-4B1B-4E80-BBE1-E407C3E945B3.jpg)


**Vite（runoob-vue3-test2）**


![](https://www.runoob.com/wp-content/uploads/2021/02/7C797674-06CF-4E87-B344-63990EF519B6.jpg)


一个标准的 Vue 3 项目，通常可以拆成三层：


- **项目根目录：**构建工具与工程配置
- **public 目录：**不参与构建的静态资源
- **src 目录：**几乎所有业务代码都在这里，平时开发基本在这个目录里面。


典型的 Vue 项目结构：


```
vue-project/
├── public/                  # 静态资源，直接复制到构建输出目录
│   └── favicon.ico          # 网站图标
├── src/
│   ├── assets/              # 静态资源（如图片、字体、CSS）
│   │   └── logo.png
│   ├── components/          # 可复用的通用组件
│   │   └── CommonHeader.vue
│   ├── composables/         # 可复用的 Composition API 逻辑（可选）
│   │   └── useFetch.js
│   ├── router/              # 路由配置
│   │   └── index.js
│   ├── stores/              # Pinia 状态管理（或 store/ 用于 Vuex）
│   │   └── index.js
│   ├── utils/               # 工具函数（如请求封装、格式化）
│   │   └── request.js
│   ├── views/               # 页面级组件（对应路由页面）
│   │   ├── HomeView.vue
│   │   └── AboutView.vue
│   ├── App.vue              # 根组件
│   └── main.js              # 入口文件（创建 Vue 应用）
├── index.html               # HTML 入口模板
├── vite.config.js           # Vite 配置文件
├── package.json             # 项目依赖与脚本
├── .gitignore               # Git 忽略文件
├── .env                     # 环境变量（开发）
├── .env.production          # 环境变量（生产）
└── README.md                # 项目说明
```


### 目录解析


| 路径 | 描述 |
| --- | --- |
| public/ | 存放不会被构建工具处理的静态资源，直接复制到 dist 目录，常用于 favicon、robots.txt 等 |
| public/favicon.ico | 网站图标（favicon） |
| src/ | 项目源代码主目录，所有开发代码放在这里 |
| src/assets/ | 存放图片、字体、全局 CSS 等静态资源，会被 Vite 处理（支持导入） |
| src/components/ | 存放可复用的通用组件（如按钮、卡片、布局组件） |
| src/composables/ | 存放可复用的 Composition API 逻辑函数（Vue 3 推荐的代码复用方式） |
| src/router/ | Vue Router 配置目录，通常包含 index.js 定义路由表 |
| src/stores/ | Pinia 状态管理目录（Vue 3 官方推荐），存放各个 store 模块 |
| src/utils/ | 存放工具函数，如 axios 封装、时间格式化、常量等 |
| src/views/ | 存放页面级组件，通常与路由一一对应（路由页面） |
| src/App.vue | Vue 应用的根组件，包含 等入口渲染点 |
| src/main.js | 项目入口文件，创建 Vue 应用实例、挂载插件（router、pinia 等）并挂载到 #app |
| index.html | HTML 模板文件，包含 挂载点 |
| vite.config.js | Vite 构建工具配置文件，可自定义插件、别名、代理等 |
| package.json | 项目依赖、脚本命令（如 dev、build、preview） |
| .gitignore | Git 忽略文件，通常忽略 node_modules、dist、.env 等 |
| .env / .env.production | 环境变量文件，用于不同环境配置 API 地址等（Vite 以 VITE_ 开头变量） |
| README.md | 项目说明文档 |


随着项目变大，还可能需要添加这些文件夹：


- **src/layouts/**：不同页面布局（如 AdminLayout.vue、GuestLayout.vue）。
- **src/plugins/**：自定义 Vue 插件（如全局组件自动注册）。
- **src/directives/**：自定义指令（如 v-loading）。
- **src/types/**：全局 TypeScript 类型声明。
- **tests/** 或 **tests**/：单元/E2E 测试（Vitest + Vue Test Utils）。
- **src/api/**：分离 API 接口调用模块（比 utils/request 更细粒度）。


接下来，我们以 runoob-vue3-test2 为例，打开目录下的 src/APP.vue 文件，代码如下（解释在注释中）：


## src/APP.vue 文件代码


```javascript
<!-- 展示模板 -->
<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Hello Vue 3.0 + Vite" />
</template>
<!-- Vue 代码 -->
<script>
/* 从 src/components/HelloWorld.vue 中引入 HelloWorld 组件 */
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>
```


接下来我们可以尝试修改下初始化的项目，将 src/APP.vue 修改为以下代码：


## src/APP.vue 文件代码


```javascript
<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="欢迎来到菜鸟教程！" />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>
```


打开页面 **http://localhost:3000/**，一般修改后会自动刷新，显示效果如下所示:


![](https://www.runoob.com/wp-content/uploads/2021/02/EB317E30-0502-4EFD-A2BC-26FD3B0B6EDE.png)








	  AI 思考中...





			** [Vue3 安装](https://www.runoob.com/vue3-install.html)
			[Vue3 起步](https://www.runoob.com/vue3-intro.html) **













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