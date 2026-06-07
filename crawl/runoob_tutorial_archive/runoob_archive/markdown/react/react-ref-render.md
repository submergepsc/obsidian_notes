# React render() 方法

- Source: https://www.runoob.com/react/react-ref-render.html

[![React 组件生命周期](https://www.runoob.com/images/up.gif) React 组件生命周期](https://www.runoob.com/react-component-life-cycle.html)


在 React 18 中，`ReactDOM.render` 方法被 `ReactDOM.createRoot` 和 `root.render` 取代。新 API 提供了更强大的功能和更好的性能。以下是对这些方法的介绍及其使用方法。


**1、ReactDOM.createRoot**

ReactDOM.createRoot 是 React 18 中引入的新方法，用于创建一个可以控制根组件的根对象。这个方法返回一个根对象，你可以使用它来渲染你的 React 组件树。


** 2、root.render**

使用从 ReactDOM.createRoot 方法返回的根对象的 render 方法来渲染组件树。这种方式替代了旧的 ReactDOM.render 方法。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App'; // 你的主组件

// 获取根元素
const rootElement = document.getElementById('root');

// 创建根
const root = ReactDOM.createRoot(rootElement);

// 渲染组件
root.render(<App />);
```


假设你有一个简单的 App 组件，可以像这样使用 createRoot 来渲染它：


## 实例


```javascript
// App.js
import React from 'react';

function App() {
  return (
    <div>
      <h1>Hello, React 18!</h1>
    </div>
  );
}

export default App;
```


## 实例


```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// 获取根元素
const rootElement = document.getElementById('root');

// 创建根
const root = ReactDOM.createRoot(rootElement);

// 渲染组件
root.render(<App />);
```


### 在线测试实例


以下实例在使用 **render()** 方法在 **id="root"** 的容器中渲染 React 元素 **Header**：


## 实例


```javascript
class Header extends React.Component {
  render() {
    return (
      <h1>菜鸟教程 - 学的不仅是技术，更是梦想！</h1>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Header />, document.getElementById('root'));
```


** [尝试一下 »](https://www.runoob.com/try/try.php?filename=try_react_life_cycle5)


在 React 17 及以前的版本中，你会使用 ReactDOM.render 方法来渲染组件：


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```


在 React 18 中，使用 createRoot 可以更好地支持并发渲染和其他新特性。


React 18 引入了并发特性，使得 React 应用在处理繁重的更新时更加高效。


[![React 组件生命周期](https://www.runoob.com/images/up.gif) React 组件生命周期](https://www.runoob.com/react-component-life-cycle.html)








	  AI 思考中...





			** [React getDerivedStateFromProps() 方法](https://www.runoob.com/react-ref-getderivedstatefromprops.html)
			[React componentDidMount() 方法](https://www.runoob.com/react-ref-componentdidmount.html) **













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