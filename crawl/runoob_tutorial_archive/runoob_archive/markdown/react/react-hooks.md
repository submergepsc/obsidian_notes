# React Hooks

- Source: https://www.runoob.com/react/react-hooks.html

React Hooks 是 React 16.8 引入的一项重要特性，它使函数组件能够拥有类组件的一些特性，例如状态管理和生命周期方法的使用。

通过 Hooks，可以更加简洁和灵活地编写 React 组件。


### 1. 什么是 React Hooks？


React Hooks 是一种函数式组件的增强机制，它允许你在不编写类组件的情况下使用 React 的特性。主要的 Hooks 包括 `useState`, `useEffect`, `useContext`, `useReducer`, `useCallback`, `useMemo`, `useRef`, 和 `useImperativeHandle` 等。这些 Hooks 提供了访问 React 特性的方式，使得你可以更好地组织和重用你的代码。


### 2. 主要的 React Hooks


`useState`


`useState` Hook 允许你在函数组件中使用局部状态。它返回一个状态值和更新该状态值的函数。


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


`useEffect`


`useEffect` Hook 允许你在函数组件中执行副作用操作（如数据获取、订阅管理、DOM 操作等）。它在每次渲染后都会执行。


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


以下是一些主要的 React Hooks 及其用途：


**useState **- 用于在函数组件中添加 state，你可以使用它来跟踪随时间变化的数据。


```
const [state, setState] = useState(initialState);
```


**useEffect** - 用于执行副作用操作，比如数据获取、订阅或手动更改 DOM，它与类组件中的 componentDidMount、componentDidUpdate 和 componentWillUnmount 生命周期类似。


```
useEffect(() => {
  // 执行副作用操作
  return () => {
    // 清理操作
  };
}, [dependencies]); // 依赖数组
```


**useContext** - 用于访问 React context 在组件树中传递的数据，而不必通过每个组件传递 props。


```
const value = useContext(MyContext);
```


**useReducer** - 用于更复杂的 state 逻辑，它接收一个 reducer 函数和初始状态，然后返回当前的状态和派发 action 的 dispatch 函数。


```
const [state, dispatch] = useReducer(reducer, initialState);
```


**useCallback** - 用于返回一个 memoized 版本的回调函数，防止不必要的渲染。


```
const memoizedCallback = useCallback(
  () => {
    // 回调函数体
  },
  [dependencies] // 依赖数组
);
```


**useMemo** - 用于对计算结果进行记忆，避免在每次渲染时重复计算。


```
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```


**useRef** - 用于创建对 DOM 元素或值的引用，可以在渲染之间保持状态。


```
const refContainer = useRef(initialValue);
```


**useImperativeHandle** - 用于使用 ref 时暴露 DOM 元素的方法。


```
useImperativeHandle(ref, () => ({
  // 暴露的方法
}));
useLayoutEffect - 与 useEffect 类似，但它在所有的 DOM 变更之后同步执行。这在需要读取 DOM 布局并同步触发重渲染时非常有用。

useLayoutEffect(() => {
  // 副作用操作
}, [dependencies]);
```


**useDebugValue** - 用于在 React 开发者工具中显示自定义 hook 的标签。


```
useDebugValue(value);
```



### 3. 使用 React Hooks 的好处


- **更简洁的组件逻辑**：无需编写类组件，可以使用函数组件和 Hooks 来管理状态和生命周期。
- **提高代码复用性**：Hooks 可以帮助你将逻辑提取到可重用的函数中，减少重复代码。
- **更好的性能优化**：使用 `useEffect`, `useCallback`, `useMemo` 等 Hooks 可以更精确地控制副作用和性能消耗。


### 4. 注意事项


- **仅在顶层使用 Hooks**：不要在循环、条件或嵌套函数中调用 Hook，确保 Hooks 在每次渲染时都以相同的顺序被调用。
- **使用 ESLint 插件**：React 官方提供了 eslint-plugin-react-hooks 插件来帮助你检查 Hook 的使用是否正确。


### 5. 实例


以下是一个使用多个 React Hooks 的示例：


## 实例


```javascript
import React, { useState, useEffect } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `You clicked ${count} times`;
  }, [count]); // 仅在 count 发生变化时更新标题

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  );
}

export default Example;
```


以上代码，我们使用了 useState 来管理 count 的状态，useEffect 来更新页面标题，以及一个简单的按钮来增加 count。


使用 Hooks，你可以编写更简洁、更可重用的组件代码。

Hooks 也使得组件逻辑的测试变得更简单，因为你可以单独测试每个 hook 的逻辑，而不需要包装在一个组件中。

此外，Hooks 还支持自定义，你可以编写自己的 Hooks 来封装复杂的逻辑，然后在多个组件中重用。








	  AI 思考中...





			** [React Tailwind CSS](https://www.runoob.com/react-tailwind.html)
			[React 参考手册](https://www.runoob.com/react-reference.html) **













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