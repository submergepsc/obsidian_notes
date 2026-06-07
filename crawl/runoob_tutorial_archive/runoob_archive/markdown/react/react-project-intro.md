# React 项目说明

- Source: https://www.runoob.com/react/react-project-intro.html

一个典型的 React 项目由多个文件和文件夹组成，每个部分都有其特定的作用。

本章节将对 React 项目代码做基本的说明，帮助大家理解项目的结构和各个部分的功能。

- React 项目由多个文件和文件夹组成，核心文件包括 `index.html`、`index.js` 和 `App.js`。
- React 组件是应用的基本构建块，可以是函数组件或类组件。
- JSX 是 React 的核心语法，用于描述 UI。
- Props 和 State 是 React 组件中管理数据的主要方式。


### 项目结构

一个 React 项目通常包含以下文件和文件夹：


```
my-react-app/
├── node_modules/       # 项目依赖的第三方库
├── public/             # 静态资源文件夹
│   ├── index.html      # 应用的 HTML 模板
│   └── ...             # 其他静态资源（如图片、字体等）
├── src/                # 项目源代码
│   ├── App.js          # 主组件
│   ├── App.css         # 主组件的样式
│   ├── index.js        # 项目入口文件
│   ├── index.css       # 全局样式
│   └── ...             # 其他组件和资源
├── package.json        # 项目配置和依赖管理
├── package-lock.json   # 依赖的精确版本锁定文件
└── README.md           # 项目说明文档
```


---


## 核心文件解析


### public/index.html

**public/index.html** 是 React 应用的 HTML 模板文件。


React 会将组件渲染到 `` 中。


React 会将组件渲染到  中。


## 实例


```javascript
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React App</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```


### src/index.js

**src/index.js** 是 React 应用的入口文件。


**src/index.js** 负责将根组件（通常是 App）渲染到 index.html 中的 div#root 中。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```


### src/App.js

**src/App.js** 是 React 应用的根组件。


**src/App.js** 通常包含应用的主要逻辑和结构。


## 实例


```javascript
import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Hello, React!</h1>
    </div>
  );
}

export default App;
```


### src/App.css


**src/App.css **是 App 组件的样式文件。


## 实例


```javascript
.App {
  text-align: center;
  margin-top: 50px;
}
```


### src/index.css

**src/index.css** 是全局样式文件，通常用于定义全局样式或重置浏览器默认样式。


## 实例


```javascript
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
```


### package.json


**package.json** 这是项目的配置文件，包含项目的元数据、依赖和脚本。


## 实例


```javascript
{
  "name": "my-react-app",
  "version": "1.0.0",
  "scripts": {
    "start": "react-scripts start", // 启动开发服务器
    "build": "react-scripts build", // 构建生产环境代码
    "test": "react-scripts test",   // 运行测试
    "eject": "react-scripts eject"  // 弹出配置（高级用法）
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  }
}
```


---


## React 组件的基本结构


React 组件是 React 应用的核心构建块。

一个组件通常包含以下部分：


### 1、函数组件


使用函数定义的组件。


## 实例


```javascript
import React from 'react';

function MyComponent() {
  return (
    <div>
      <h2>这是一个函数定义的组件</h2>
    </div>
  );
}

export default MyComponent;
```


**说明：**


- **`import React from 'react';`**: 导入了 React 库，React 是一个用于构建用户界面的 JavaScript 库。
- **`function MyComponent() { ... }`**: 这是一个函数组件。函数组件是一个返回 JSX 的 JavaScript 函数。
- **`return (...)`**: 组件的 `return` 语句返回一个 JSX 元素。JSX 是 JavaScript 的语法扩展，允许你在 JavaScript 中编写类似 HTML 的代码。
- **`export default MyComponent;`**: 将 `MyComponent` 组件导出为默认导出。这样，其他文件可以通过 `import MyComponent from './MyComponent';` 来导入并使用这个组件。


### 2、类组件

使用类定义的组件（现在较少使用，推荐使用函数组件）。


## 实例


```javascript
import React, { Component } from 'react';

class MyComponent extends Component {
  render() {
    return (
      <div>
        <h2>这是一个类组件</h2>
      </div>
    );
  }
}

export default MyComponent;
```


**说明：**


- **`import React from 'react';`**: 导入 React 库，这是使用 React 的基础。
- **`import { Component } from 'react';`**: 从 React 库中导入 `Component` 类。`Component` 是 React 类组件的基类，所有类组件都需要继承它。
- **`class MyComponent extends Component { ... }`**: 定义了一个名为 `MyComponent` 的类组件。它继承了 `Component` 类，因此可以使用 React 类组件的特性（如生命周期方法、状态管理等）。
- **`render() { ... }`**: `render` 是类组件中必须实现的方法。它负责返回组件的 UI 结构（JSX）。**`return (...)`**: 返回一个 JSX 元素，描述组件的 UI。
- **`这是一个类组件`**: 这是一个简单的 JSX 结构，包含一个 `div` 和一个 `h2` 标题。


**`export default MyComponent;`**: 将 `MyComponent` 组件导出为默认导出。这样，其他文件可以通过 `import MyComponent from './MyComponent';` 来导入并使用这个组件。


### 3、JSX

JSX 是 JavaScript 的语法扩展，允许在 JavaScript 中编写类似 HTML 的代码。


## 实例


```javascript
const element = <h1>Hello, JSX!</h1>;
```


### 4、Props

Props 是组件的输入参数，用于从父组件向子组件传递数据。


## 实例


```javascript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return <Welcome name="React" />;
}
```


### 5、State

State 是组件的内部状态，用于管理组件的数据。


## 实例（使用 useState Hook）


```javascript
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default Counter;
```


---


## React 项目的运行流程


### 启动开发服务器


运行 **npm start** 或 **yarn start**，启动开发服务器。


打开浏览器访问 http://localhost:3000，查看应用。


### 构建生产环境代码


运行 **npm run build** 或 **yarn build**，生成优化后的生产环境代码。


### 运行测试


运行 **npm test** 或 **yarn test**，执行项目的测试用例。








	  AI 思考中...





			** [React 创建第一个项目](https://www.runoob.com/react-creact-first-app.html)
			[React 测验](https://www.runoob.com/react-quiz.html) **













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