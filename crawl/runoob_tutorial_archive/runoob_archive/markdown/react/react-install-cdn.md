# React 安装(CDN)

- Source: https://www.runoob.com/react/react-install-cdn.html

React 可以直接下载使用，下载包中也提供了很多学习的实例。


本教程使用了 React 的版本为 18.2.0，你可以在官网 [https://reactjs.org/](https://reactjs.org/) 下载最新版。


使用字节跳动的 React CDN 库，地址如下：


```javascript
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js" ></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.min.js" ></script>
```


使用 Staticfile CDN 的 React CDN 库，地址如下：


```javascript
<script src="https://cdn.staticfile.org/react/18.2.0/umd/react.development.js"></script>
<script src="https://cdn.staticfile.org/react-dom/18.2.0/umd/react-dom.development.js"></script>
<!-- 生产环境中不建议使用 -->
<script src="https://cdn.staticfile.org/babel-standalone/6.26.0/babel.min.js"></script>
```


官方提供的 CDN 地址：


```javascript
<script src="https://unpkg.com/react@16/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
<!-- 生产环境中不建议使用 -->
<script src="https://unpkg.com/[email protected]/babel.min.js"></script>
```


**注意:** 在浏览器中使用 Babel 来编译 JSX 效率是非常低的。


### 使用实例


以下实例输出了 Hello, world!


## React 实例


```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>Hello React!</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js" ></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.min.js" ></script>
</head>
<body>

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

</body>
</html>
</script>

</body>
</html>
```


** [尝试一下 »](https://www.runoob.com/try/try.php?filename=try_react_hw)


实例解析：**


实例中我们引入了三个库： react.production.min.js 、react-dom.production.min.js 和 babel.min.js：


- **react.min.js** - React 的核心库
- **react-dom.min.js** - 提供与 DOM 相关的功能
- **babel.min.js** - Babel 可以将 ES6 代码转为 ES5 代码，这样我们就能在目前不支持 ES6 浏览器上执行 React 代码。Babel 内嵌了对 JSX 的支持。通过将 Babel 和 babel-sublime 包（package）一同使用可以让源码的语法渲染上升到一个全新的水平。


```javascript
// 简单的 React 组件
function App() {
    return <h1>Hello, React!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById("example"));
// 渲染 React 组件到 DOM
root.render(<App />);
```


以上代码将一个 h1 标题，插入 id="example" 节点中。


```
const root = ReactDOM.createRoot(document.getElementById("example"));
```


- **获取 DOM 容器**：`document.getElementById("example")` 获取了一个 id 为 "example" 的 DOM 元素。
- **创建根节点**：`ReactDOM.createRoot` 是 React 18 引入的新方法，用于创建一个 React 根节点。在这个例子中，`root` 变量保存了这个根节点。

**

注意：**


如果我们需要使用 JSX，则  标签的 type 属性需要设置为 text/babel。










	  AI 思考中...





			** [React componentWillUnmount() 方法](https://www.runoob.com/react-ref-componentwillunmount.html)
			[React 条件判断](https://www.runoob.com/react-conditional.html) **













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