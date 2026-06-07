# React 教程

- Source: https://www.runoob.com/react/react-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2016/02/react.png)

React 是一个用于构建用户界面的 JAVASCRIPT 库。


React 主要用于构建 UI，很多人认为 React 是 MVC 中的 V（视图）。


React 起源于 Facebook 的内部项目，用来架设 Instagram 的网站，并于 2013 年 5 月开源。


React 拥有较高的性能，代码逻辑非常简单，越来越多的人已开始关注和使用它。


---


## React 特点


- **1.声明式设计** −React采用声明范式，可以轻松描述应用。
- ** 2.高效** −React通过对DOM的模拟，最大限度地减少与DOM的交互。
- ** 3.灵活** −React可以与已知的库或框架很好地配合。
- **4.JSX** − JSX 是 JavaScript 语法的扩展。React 开发不一定使用 JSX ，但我们建议使用它。
- **5.组件** − 通过 React 构建组件，使得代码更加容易得到复用，能够很好的应用在大项目的开发中。
- **6.单向响应的数据流** − React 实现了单向响应的数据流，从而减少了重复代码，这也是它为什么比传统数据绑定更简单。


---


## 阅读本教程前，您需要了解的知识：


在开始学习 React 之前，您需要具备以下基础知识：


- [HTML 教程](https://www.runoob.com/../html/html-tutorial.html)
- [CSS 教程](https://www.runoob.com/../css/css-tutorial.html)
- [JavaScript 教程](https://www.runoob.com/../js/js-tutorial.html)
- [ES6 教程](https://www.runoob.com/w3cnote/es6-tutorial.html)


---


## React 第一个实例


在每个章节中，您可以在线编辑实例，然后点击按钮查看结果。


本教程使用了 React 的版本为 18.2.0，你可以在官网 [https://react.dev/](https://react.dev/) 下载最新版。


## React 实例


```javascript
<div id="example"></div>
<script type="text/babel">
// 简单的 React 组件
function App() {
    return <h1>Hello, React!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById("example"));
// 渲染 React 组件到 DOM
root.render(<App />);
</script>
```


** [尝试一下 »](https://www.runoob.com/try/try.php?filename=try_react_hw)

引入外部脚本：**


```
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js" ></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.min.js" ></script>
```


这三行代码分别引入了 React、ReactDOM 和 Babel Standalone 库。


- React 用于构建用户界面。
- ReactDOM 用于在浏览器中渲染 React 组件。
- Babel Standalone 用于在浏览器中即时编译 JSX 语法。


或者使用 create-react-app 工具（下一章节会介绍）创建的 react 开发环境：


## 实例


```javascript
import React from "react";
import ReactDOM from "react-dom/client";

function Hello(props) {
  return <h1>Hello World!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Hello />);
```


这时候浏览器打开 **http://localhost:3000/** 就会输出：


```
Hello World!
```


---


## 参考资料

- React 官网：[https://react.dev/](https://react.dev/)
- React 中文文档：[https://zh-hans.react.dev/](https://zh-hans.react.dev/)
- React Github 源码：[https://github.com/facebook/react](https://github.com/facebook/react)










	  AI 思考中...






			[React 安装(NPM)](https://www.runoob.com/react-install.html) **













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