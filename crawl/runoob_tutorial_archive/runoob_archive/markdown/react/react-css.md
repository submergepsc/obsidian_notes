# React 使用 CSS 样式

- Source: https://www.runoob.com/react/react-css.html

在 React 应用程序中使用 CSS 有多种方法。

以下是一些常见的方式以及如何在 React 中实现这些方法的详细说明。


### 内联样式

在 React 中直接在元素内使用 CSS 样式是通过内联样式来实现的。

内联样式是将 CSS 样式直接作为一个对象传递给元素的 style 属性。每个样式属性都以驼峰命名法表示，而不是传统的 CSS 属性名称。


直接在元素内部使用：


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';

const Header = () => {
  return (
    <>
      <h1 style={{color: "red"}}>Hello Style!</h1>
      <p>Add a little style!</p>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Header />);
```


您还可以创建一个具有样式信息的对象，并在样式属性中引用它：


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom';

const MyComponent = () => {
  // 定义内联样式对象
  const containerStyle = {
    padding: '20px',
    backgroundColor: '#f0f0f0'
  };

  const titleStyle = {
    fontSize: '24px',
    color: '#333'
  };

  return (
    <div style={containerStyle}>
      <h1 style={titleStyle}>Hello, world!</h1>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyComponent />);
```


在上面的示例中，containerStyle 和 titleStyle 是两个内联样式对象，分别应用于 div 和 h1 元素。以下是关键点：


- 使用驼峰命名法表示 CSS 属性（例如，`backgroundColor` 而不是 `background-color`）。
- 所有样式属性值都作为字符串传递（除了数字值可以直接使用，React 会自动添加单位）。


内联样式还可以根据组件的状态动态变化：


## 实例


```javascript
import React, { useState } from 'react';
import ReactDOM from 'react-dom';

const MyComponent = () => {
  const [isHighlighted, setIsHighlighted] = useState(false);

  const containerStyle = {
    padding: '20px',
    backgroundColor: isHighlighted ? '#ffff99' : '#f0f0f0'
  };

  const titleStyle = {
    fontSize: '24px',
    color: '#333'
  };

  return (
    <div style={containerStyle}>
      <h1 style={titleStyle}>Hello, world!</h1>
      <button onClick={() => setIsHighlighted(!isHighlighted)}>
        Toggle Highlight
      </button>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyComponent />);
```


### 通过样式文件

您可以在单独的文件中编写 CSS 样式，只需使用 **.css** 文件扩展名保存该文件，然后将其导入您的应用程序即可。


创建一个名为 App.css 的样式文件，并加入以下 CSS 代码：


## 实例


```javascript
body {
  background-color: #282c34;
  color: white;
  padding: 40px;
  font-family: Sans-Serif;
  text-align: center;
}
```


在的应用程序中导入样式 App.css：


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import './App.css';

const Header = () => {
  return (
    <>
      <h1>Hello Style!</h1>
      <p>Add a little style!.</p>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Header />);
```


### CSS 模块

向应用程序添加样式的另一种方法是使用 CSS 模块。

CSS 模块是一种局部作用域的 CSS 文件命名规范，通过这种方法，CSS 类名和动画名称默认都作用于局部作用域。


CSS 模块对于放置在单独文件中的组件非常方便。


使用 **.module.css** 扩展名创建 CSS 模块，例如：MyComponent.module.css。


## 实例


```javascript
/* MyComponent.module.css */
.container {
  padding: 20px;
  background-color: #f0f0f0;
}

.title {
  font-size: 24px;
  color: #333;
}
```


在应用中导入样式表：


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import styles from './MyComponent.module.css';

const MyComponent = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Hello, world!</h1>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyComponent />);
```










	  AI 思考中...





			** [React Memo](https://www.runoob.com/react-memo.html)
			[React Sass](https://www.runoob.com/react-sass.html) **













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