# React Memo

- Source: https://www.runoob.com/react/react-memo.html

`React.memo` 是一个高阶组件（Higher Order Component, HOC），用于优化函数组件的性能。它通过记忆组件的渲染输出，在组件的 props 没有变化时跳过重新渲染，从而提高性能。以下是 `React.memo` 的详细介绍和使用方法。


## 1. 基本使用


`React.memo` 的基本使用方法是将一个函数组件作为参数传递给 `React.memo`，并返回一个记忆化的组件。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom';

const MyComponent = React.memo((props) => {
  console.log('Rendering MyComponent');
  return <div>{props.text}</div>;
});

const App = () => {
  const [count, setCount] = React.useState(0);
  const [text, setText] = React.useState('Hello, world!');

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Increment Count</button>
      <MyComponent text={text} />
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```


在这个示例中，即使 `count` 状态发生变化，`MyComponent` 也不会重新渲染，因为它的 `props` 没有变化。


## 2. 使用自定义比较函数


默认情况下，`React.memo` 只会对比前后的 `props`，如果没有变化则不会重新渲染。你可以通过传递一个自定义比较函数来更精确地控制重新渲染的逻辑。


### 自定义比较函数的签名：


```
function areEqual(prevProps, nextProps) {
  // 返回 true 表示相等，不需要重新渲染
  // 返回 false 表示不相等，需要重新渲染
}
```


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom';

const MyComponent = React.memo((props) => {
  console.log('Rendering MyComponent');
  return <div>{props.text}</div>;
}, (prevProps, nextProps) => {
  return prevProps.text === nextProps.text;
});

const App = () => {
  const [count, setCount] = React.useState(0);
  const [text, setText] = React.useState('Hello, world!');

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Increment Count</button>
      <MyComponent text={text} />
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```



在这个示例中，自定义比较函数检查 `text` 是否发生变化。如果 `text` 没有变化，`MyComponent` 不会重新渲染。


## 3. 实际应用场景


`React.memo` 非常适用于以下场景：


- **静态数据展示**：组件接收的 `props` 很少变化，但组件本身较为复杂，重新渲染成本高。
- **性能优化**：在大列表或表格中，每个项目都是独立的组件，使用 `React.memo` 可以避免不必要的重新渲染。
- **避免深度相等检查**：自定义比较函数可以避免深度相等检查，特别是在 `props` 包含大量数据时。


## 4. 注意事项


- **浅比较**：默认情况下，`React.memo` 进行浅比较，这意味着它只会比较 `props` 的一级内容，嵌套对象需要自定义比较函数。
- **状态和上下文**：`React.memo` 只关注 `props` 的变化，组件内部的状态和上下文的变化不会触发重新渲染。


## 5. 与 useMemo 和 useCallback 的区别


- **`React.memo`**：用于记忆化整个组件，优化组件的渲染。
- **`useMemo`**：用于记忆化函数组件内部的值或计算结果。
- **`useCallback`**：用于记忆化函数组件内部的回调函数，避免不必要的重新创建。


## 实例


```javascript
import React, { useState, useMemo, useCallback } from 'react';
import ReactDOM from 'react-dom';

const ChildComponent = React.memo(({ onClick, count }) => {
  console.log('Rendering ChildComponent');
  return <button onClick={onClick}>Count: {count}</button>;
});

const App = () => {
  const [count, setCount] = useState(0);

  const increment = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  const doubledCount = useMemo(() => count * 2, [count]);

  return (
    <div>
      <p>Doubled Count: {doubledCount}</p>
      <ChildComponent onClick={increment} count={count} />
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```


在这个示例中，`useCallback` 和 `useMemo` 用于优化函数和计算结果，`React.memo` 用于优化子组件的渲染。


### 小结


`React.memo` 是一个强大的工具，可以有效地提高函数组件的性能，避免不必要的重新渲染。通过合理使用 `React.memo` 和自定义比较函数，你可以在不影响应用逻辑的情况下显著优化应用性能。









	  AI 思考中...





			** [React 路由](https://www.runoob.com/react-router.html)
			[React 使用 CSS 样式](https://www.runoob.com/react-css.html) **













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