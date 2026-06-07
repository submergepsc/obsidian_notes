# React 安装(Vite)

- Source: https://www.runoob.com/react/react-vite.html

Vite 是一个现代化的前端构建工具，旨在通过利用现代浏览器的原生 ES 模块支持，提供快速的开发体验。


Vite 是当前 React 官方推荐的首选工具，比传统的 Create React App 更快、更轻量、开发体验更好。


Vite 基于原生 ES Modules，支持秒级热更新（HMR），启动时间通常只需几百毫秒。

Vite 详细内容查看： [Vite 教程](https://www.runoob.com/../vue3/vite-tutorial.html)。


![](https://www.runoob.com/wp-content/uploads/2026/01/495bc3f1-b14f-4e50-afe0-0aa282fbb90c.png)


### 为什么选择 Vite + React？


- **极速启动**：开发服务器秒开，热更新几乎实时。
- **现代特性**：开箱支持 JSX、TypeScript、CSS Modules、PostCSS 等。
- **轻量灵活**：配置文件简单，可轻松自定义。
- **生产优化**：内置 Rollup 构建，输出体积小、性能高。
- **官方背书**：React 官方文档已将 Vite 作为默认推荐。


---


## 创建你的第一个 Vite + React 项目


打开终端（Windows: PowerShell/Command Prompt；macOS/Linux: Terminal）。


使用 npm 安装：


```
npm create vite@latest my-first-react-app -- --template react
```


**推荐命令（使用 pnpm，最快最省磁盘）**：


```
pnpm create vite@latest my-first-react-app -- --template react
```


其他包管理器命令：


使用 yarn 安装：


```
yarn create vite my-first-react-app --template react
```


命令解释：


- `create vite@latest`：使用最新版 Vite 创建工具。
- `my-first-react-app`：你的项目名称（小写字母 + 连字符推荐）。
- `-- --template react`：指定 React 模板。


**交互过程**（会提示选择）：


- 项目名称：直接回车确认或修改。
- 选择框架：选择 **React**。
- 选择变体： **JavaScript**（推荐入门，先用纯 JS）。
- **TypeScript**（进阶推荐，类型安全更好，后续可切换）。




我们这里选择 **JavaScript**。


等待几秒钟，项目骨架就创建好了！


### 安装依赖并启动项目

进入项目目录 **cd my-first-react-app**，安装依赖：


```
npm install
```


启动开发服务器：


```
npm run dev
```


浏览器会自动打开 http://localhost:5173（Vite 默认端口）。

你会看到一个欢迎页面，带有 Vite + React 的 Logo 和计数器示例，这就是你的第一个 React 应用在运行！


![](https://www.runoob.com/wp-content/uploads/2026/01/1_A1h_j70-G1JobvNDLsbzGw.jpg)


热模块替换（HMR）体验：修改任何代码（后面会教），保存后页面自动更新，无需刷新！这就是 Vite 的魔法。


### 项目结构详解


打开项目文件夹（推荐用 VS Code：**code .** 命令一键打开）。


```
cd my-first-react-app
code .
```


![](https://www.runoob.com/wp-content/uploads/2026/01/228451dd-af97-4301-a338-d5161bed0d39.png)


典型结构如下：


```
my-first-react-app/
├── public/              # 静态资源（直接复制到构建输出）
│   └── vite.svg         # Vite Logo
├── src/                 # 源码主目录（重点！）
│   ├── assets/          # 图片等资源
│   │   └── react.svg
│   ├── App.jsx          # 主组件（应用入口）
│   ├── main.jsx         # 入口文件（挂载根组件）
│   ├── index.css        # 全局样式
│   └── vite-env.d.ts    # TypeScript 声明（JS 项目可忽略）
├── .gitignore
├── index.html           # HTML 入口模板
├── package.json         # 依赖和脚本
├── vite.config.js       # Vite 配置文件（目前为空，可自定义）
└── README.md
```


关键文件解释：


- **index.html**：页面入口，`` 是 React 挂载点。
- **src/main.jsx**：React 启动文件，使用 React 18 的新 API 创建根节点。
- **src/App.jsx**：你的主组件，默认带有一个计数器示例。


### 修改代码：你的第一个 React 组件


打开 `src/App.jsx`，替换全部内容为以下代码（我们从一个简单问候开始）：


## 实例


```javascript
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>你好，React + Vite！</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          当前计数：{count}
        </button>
      </div>
      <p>
        编辑 <code>src/App.jsx</code> 并保存体验热更新！
      </p>
    </div>
  )
}

export default App
```


保存后，页面自动更新！你已经写了一个完整的函数组件：


- `import { useState } from 'react'`：引入 Hook。
- `useState(0)`：声明状态变量 `count`，初始值 0。
- `onClick` 事件：点击按钮更新状态，触发重渲染。
- JSX 语法：看起来像 HTML，但其实是 JavaScript。


**小练习**：


- 把标题改成你的名字：`你好，[你的名字]！`
- 添加一个新按钮：显示减法计数。
```
<button onClick={() => setCount(count - 1)}>
  减一
</button>
```


### 理解入口文件：src/main.jsx


打开 `src/main.jsx`：


## 实例


```javascript
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
```


解释：


- `ReactDOM.createRoot`：React 18 新 API，启用并发特性。
- ``：渲染你的主组件。
- ``：开发模式下严格检查，帮助发现问题。


### 添加新组件（组件化实践）


在 `src/` 下创建新文件 `components/HelloWorld.jsx`（先手动创建文件夹）：


![](https://www.runoob.com/wp-content/uploads/2026/01/f22dec7c-e83f-41f6-9ba7-119ae628fe66.png)


```
// src/components/HelloWorld.jsx
function HelloWorld({ name }) {
  return <h2>欢迎，{name || '陌生人'}！</h2>
}

export default HelloWorld
```


在 `App.jsx` 中引入并使用：


```
import HelloWorld from './components/HelloWorld.jsx'

// 在 return 中添加：
<HelloWorld name="Runoob" />
```


保存刷新，你会看到新组件渲染。这就是 **组件化** 的魅力：复用、可组合！


### 样式与资源处理


- **CSS**：直接 import `./App.css`，支持普通 CSS。
- **图片**：import 后作为变量使用（Vite 自动优化）。
- **进阶**：支持 CSS Modules（文件名 `.module.css`）、Tailwind CSS（后续可配置）。


### 构建生产版本


开发完成后，构建用于部署的静态文件：


```
npm run build
```


输出在 `dist/` 文件夹：纯 HTML/CSS/JS，可上传到 Vercel、Netlify 等。









	  AI 思考中...





			** [React 简介](https://www.runoob.com/react-intro.html)
			[使用 VSCode 开发 React](https://www.runoob.com/react-vscode.html) **













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