# React 参考手册

- Source: https://www.runoob.com/react/react-reference.html

React 手册包含了各种核心 API、Hooks、组件生命周期方法等。


以下是一份完整的 React 参考手册，内容覆盖从基础到高级的所有核心概念（基于 React 18+ 现代实践，优先函数组件 + Hooks），每个表格包含**概念/语法**、**描述**、**示例代码** 和 **注意事项**。


### 1、JSX 基础


| 概念/语法 | 描述 | 示例代码 | 注意事项 |
| --- | --- | --- | --- |
| JSX 基本结构 | 类似 HTML 的语法，编译为 React.createElement | return Hello; | 必须有单个根元素，可用 碎片 |
| 表达式嵌入 | 用 {} 嵌入 JS 表达式（只能表达式，不能语句） | {name.toUpperCase()} | 支持计算、变量、三元等 |
| 属性绑定 | class → className，for → htmlFor |  | 驼峰命名（如 tabIndex） |
| 自闭合标签 | 所有标签必须闭合 |  | 无子元素的标签必须自闭合 |
| 条件渲染 | 三元运算符或 && | {isLogin ? : }{count > 0 && {count}} | && 用于"存在则渲染" |
| 列表渲染 | 用 map()，必须加 key | {items.map(item => {item.name})} | key 必须唯一稳定，避免用 index |
| 注释 | 用 {/* */} | {/* 这是一个注释 */} | 放在 JSX 内 |
| 碎片（Fragment） | 空标签，避免额外 DOM | 12 或 | 短语法 更常用 |


### 2、 组件基础


| 概念/语法 | 描述 | 示例代码 | 注意事项 |
| --- | --- | --- | --- |
| 函数组件（推荐） | 首字母大写，返回 JSX | function App() { return Hello; } | 现代首选，无 this |
| 类组件（遗留） | 使用 class 继承 React.Component | class App extends React.Component { render() { return ; } } | 仅用于理解旧代码 |
| Props 传递 | 单向数据流，从父传子 | 子组件：function Child({name}) {...} | 只读，不可修改 |
| 默认 Props | defaultProps（函数组件用参数默认值） | function Child({name = 'Guest'}) {...} | ES6 默认参数更简洁 |
| Props 类型检查 | PropTypes（或 TypeScript） | Child.propTypes = { name: PropTypes.string.isRequired } | 开发模式警告，生产移除 |
| 组件组合 | 嵌套、children | Title父：{props.children} | children 是特殊 Prop |


### 3、状态与 Hooks（核心）


| Hook / 概念 | 描述 | 示例代码 | 注意事项 |
| --- | --- | --- | --- |
| useState | 声明状态变量 | const [count, setCount] = useState(0); setCount(c => c+1)}> | set 函数式更新避免陈旧状态 |
| useEffect | 副作用（挂载、更新、清理） | useEffect(() => { ... }, [dep]);返回清理函数 | 空数组 [] 只挂载一次 |
| useRef | 保存可变值或 DOM 引用 | const inputRef = useRef(null);inputRef.current.focus(); | 不触发重渲染 |
| useContext | 消费 Context，避免 Prop Drilling | const theme = useContext(ThemeContext); | 与 Context.Provider 配合 |
| useReducer | 复杂状态逻辑（类似 Redux） | const [state, dispatch] = useReducer(reducer, initial); | 用于多相关状态 |
| useMemo | 缓存计算结果 | const memoValue = useMemo(() => compute(), [dep]); | 避免昂贵计算重执行 |
| useCallback | 缓存函数引用 | const handle = useCallback(() => {...}, [dep]); | 优化子组件 Props |
| 自定义 Hook | 封装可复用逻辑 | function useFetch(url) { ... return data; } | 以 use 开头 |


### 4、生命周期（类组件 vs Hooks）


| 阶段 | 类组件方法 | Hooks 等价 | 注意事项 |
| --- | --- | --- | --- |
| 挂载（Mount） | constructor → render → componentDidMount | useEffect(() => {…}, []) | 初始化状态/API 调用 |
| 更新（Update） | shouldComponentUpdate → render → componentDidUpdate | useEffect(() => {…}, [dep]) + memo | 依赖变化触发 |
| 卸载（Unmount） | componentWillUnmount | useEffect 返回清理函数 | 清除定时器/订阅 |
| 错误处理 | componentDidCatch | ErrorBoundary 组件 | Hooks 无直接等价 |


### 5、上下文与全局状态


| 概念 | 描述 | 示例代码 | 注意事项 |
| --- | --- | --- | --- |
| Context API | 全局数据共享 | const ThemeContext = createContext(); | 避免过度使用，性能消耗 |
| useContext | 在函数组件消费 | const theme = useContext(ThemeContext); | 简洁替代 Consumer |


### 6、高级特性（React 18+）


| 概念 | 描述 | 示例代码 | 注意事项 |
| --- | --- | --- | --- |
| Concurrent Mode | 可中断渲染，提升响应性 | + Transitions | 自动批处理更新 |
| Suspense | 懒加载/数据获取等待 | }> | 与 lazy 配合 |
| React.lazy | 代码分割懒加载 | const Lazy = React.lazy(() => import('./Comp')); | 需 Suspense 包裹 |
| startTransition | 标记非紧急更新 | startTransition(() => setQuery(e.target.value)); | 保持 UI 响应性 |
| useDeferredValue | 延迟非紧急值 | const deferred = useDeferredValue(query); | 输入防抖类似 |


### 7、性能优化


| 技巧 | 描述 | 示例代码 | 注意事项 |
| --- | --- | --- | --- |
| React.memo | 浅比较 Props，避免不必要渲染 | export default React.memo(Component); | 函数组件专用 |
| useMemo / useCallback | 缓存值/函数 | 如上 | 防止子组件重渲染 |
| 键（key）优化 | 稳定唯一 key | 如列表渲染 | 避免 index |
| 虚拟列表 | 长列表优化（react-window） |  | 第三方库 |


### 8、常见生态工具


| 工具 | 用途 | 安装/用法 | 注意事项 |
| --- | --- | --- | --- |
| React Router v6 | 路由导航 | npm i react-router-dom}/> | 嵌套路由、Outlet |
| Redux Toolkit | 全局状态管理 | npm i @reduxjs/toolkit react-redux | RTK Query 数据获取 |
| React Hook Form | 表单处理 | useForm() | 性能高，验证简单 |
| Axios / Fetch | 数据请求 | fetch('/api') | useEffect 中使用 |
| Tailwind / MUI | UI 样式 | npm i tailwindcss 或 mui | 快速美化 |


### 9、调试与最佳实践


| 项目 | 描述 | 工具/方法 |
| --- | --- | --- |
| 调试工具 | 查看组件树、Props、Hooks | React DevTools（浏览器插件） |
| Strict Mode | 发现潜在问题 |  |
| ESLint + Prettier | 代码规范 | VS Code 插件 |
| 测试 | Jest + React Testing Library | npm i --save-dev jest |


以下是一些常见的函数和方法，以及它们的简要说明：


## React 核心 API


**createElement(type, [props], [...children])** - 创建一个 React 元素或组件。


## 实例


```javascript
import React from 'react';

const element = React.createElement('div', { className: 'container' }, 'Hello, World!');
// React.createElement 返回一个 React 元素
```


**cloneElement(element, [props], [...children])** - 克隆并返回一个 React 元素，可以传递新的 props 和子元素。


## 实例


```javascript
import React, { cloneElement } from 'react';

const parentElement = <div>Hello</div>;
const clonedElement = cloneElement(parentElement, { className: 'child' });
// clonedElement 是一个克隆的 React 元素，带有新的 className
```


**createFactory(type)** - 创建一个工厂函数，用于创建指定类型的 React 元素。


## 实例


```javascript
import React from 'react';

const factory = React.createFactory('button');
const buttonElement = factory({ onClick: () => console.log('Button clicked') }, 'Click me');
// buttonElement 是一个工厂创建的 React 元素，一个可点击的按钮
```


**isValidElement(element)** - 判断一个对象是否是有效的 React 元素。


## 实例


```javascript
import React, { isValidElement } from 'react';

const element = <div>Hello</div>;
console.log(isValidElement(element)); // true
```


**Children.map(children, function[(thisArg)])** - 遍历和映射 React 子元素。


## 实例


```javascript
import React, { Children } from 'react';

const parentElement = (
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
);

const mappedChildren = Children.map(parentElement.props.children, child => (
  <li>{child}</li>
));
// mappedChildren 是映射后的子元素列表
```


## React 组件生命周期方法

**constructor(props)** - 构造函数，在组件创建时调用，用于初始化 state 和绑定方法。


## 实例


```javascript
import React, { Component } from 'react';

class MyComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  render() {
    return <div>{this.state.count}</div>;
  }
}
```


**componentDidMount()** - 组件挂载后调用，通常用于数据获取、订阅等副作用操作。


## 实例


```javascript
import React, { Component } from 'react';

class MyComponent extends Component {
  componentDidMount() {
    // 在组件挂载后订阅数据
    this.subscription = subscribeToData(data => {
      this.setState({ data });
    });
  }

  componentWillUnmount() {
    // 在组件卸载前取消订阅
    this.subscription.unsubscribe();
  }

  render() {
    return <div>{this.state.data}</div>;
  }
}
```


**componentDidUpdate(prevProps, prevState)** - 组件更新后调用，通常用于响应 props 或 state 的变化。


## 实例


```javascript
import React, { Component } from 'react';

class MyComponent extends Component {
  componentDidUpdate(prevProps, prevState) {
    // 当 props 或 state 变化时更新数据
    if (this.props.userID !== prevProps.userID) {
      this.fetchData(this.props.userID);
    }
  }

  render() {
    return <div>{this.props.userID}</div>;
  }
}
```


**componentWillUnmount()** - 组件将被卸载前调用，用于清理定时器、取消订阅等资源释放。


## 实例


```javascript
import React, { Component } from 'react';

class MyComponent extends Component {
  componentWillUnmount() {
    // 在组件卸载前清理资源
    clearInterval(this.timerID);
  }

  render() {
    return <div>{this.state.time}</div>;
  }
}
```


**static getDerivedStateFromProps(props, state)** - 用于替代 componentWillReceiveProps，在 props 变化时更新 state。


## 实例


```javascript
import React, { Component } from 'react';

class MyComponent extends Component {
  static getDerivedStateFromProps(nextProps, prevState) {
    if (nextProps.userID !== prevState.userID) {
      return { userID: nextProps.userID };
    }
    return null;
  }

  render() {
    return <div>{this.state.userID}</div>;
  }
}
```


## React Hooks


**useState(initialState)** - 声明一个状态变量及其更新函数。


## 实例


```javascript
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  );
}
```


**useEffect(callback, [dependencies])** - 声明一个副作用操作，类似于 componentDidMount 和 componentDidUpdate 的组合。


## 实例


```javascript
import React, { useState, useEffect } from 'react';

function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setSeconds(seconds => seconds + 1);
    }, 1000);

    return () => clearInterval(interval);
  }, []); // 空数组作为第二个参数表示仅在组件挂载和卸载时执行

  return <p>Timer: {seconds} seconds</p>;
}
```


**useContext(context)** - 获取并订阅一个 React context。


## 实例


```javascript
import React, { useContext } from 'react';

const MyContext = React.createContext('default');

function MyComponent() {
  const contextValue = useContext(MyContext);
  return <p>Context value: {contextValue}</p>;
}
```


**useReducer(reducer, initialState)** - 声明一个复杂状态逻辑的 reducer 和 dispatch 函数。


## 实例


```javascript
import React, { useReducer } from 'react';

const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>Increment</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>Decrement</button>
    </div>
  );
}
```


**useCallback(callback, [dependencies])** - 缓存一个回调函数，以便在依赖项变化时避免重复创建。


## 实例


```javascript
import React, { useState, useCallback } from 'react';

function ParentComponent() {
  const [count, setCount] = useState(0);

  const increment = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  return (
    <div>
      <ChildComponent onClick={increment} />
    </div>
  );
}

function ChildComponent({ onClick }) {
  return <button onClick={onClick}>Increment Count</button>;
}
```


**useMemo(factory, [dependencies])** - 缓存计算值，以便在依赖项变化时避免重复计算。


## 实例


```javascript
import React, { useMemo } from 'react';

function ExpensiveComponent({ data }) {
  const expensiveValue = useMemo(() => {
    return computeExpensiveValue(data);
  }, [data]);

  return <div>Expensive value: {expensiveValue}</div>;
}
```


**useRef(initialValue)** - 创建一个持久化的引用，可用于访问 DOM 元素或缓存任何可变值。


## 实例


```javascript
import React, { useRef, useEffect } from 'react';

function TextInputWithFocusButton() {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return (
    <>
      <input ref={inputRef} type="text" />
      <button onClick={() => inputRef.current.focus()}>Focus Input</button>
    </>
  );
}
```


## 其他常见函数

**ReactDOM.render(element, container[, callback])** - 将 React 元素渲染到指定的 DOM 节点。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom';

const element = <h1>Hello, World!</h1>;
ReactDOM.render(element, document.getElementById('root'));
```


**ReactDOM.createRoot(container[, options])** - 创建一个 React 根实例，支持并发渲染特性。


## 实例


```javascript
import ReactDOM from 'react-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```


**ReactDOM.unmountComponentAtNode(container)** - 卸载指定 DOM 节点上的 React 组件。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.unmountComponentAtNode(document.getElementById('root'));
```


**ReactDOMServer.renderToString(element)** - 将 React 元素渲染为静态 HTML 字符串，用于服务器端渲染。


## 实例


```javascript
import React from 'react';
import ReactDOMServer from 'react-dom/server';

const element = <div>Hello, World!</div>;
const htmlString = ReactDOMServer.renderToString(element);
```










	  AI 思考中...





			** [React Hooks](https://www.runoob.com/react-hooks.html)
			[React 创建第一个项目](https://www.runoob.com/react-creact-first-app.html) **













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