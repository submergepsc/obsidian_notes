# React 条件判断

- Source: https://www.runoob.com/react/react-conditional.html

在 React 中，可以通过 JavaScript 的条件语句来动态渲染组件或元素。

以下是几种常用的在 React 中处理条件渲染的方法：


### 1. 使用 if 语句

在 render 方法或函数组件的返回值中使用 if 语句来决定渲染内容。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';

class MyComponent extends React.Component {
  render() {
    const isLoggedIn = this.props.isLoggedIn;
    let content;

    if (isLoggedIn) {
      content = <h1>Welcome back!</h1>;
    } else {
      content = <h1>Please sign up.</h1>;
    }

    return (
      <div>
        {content}
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyComponent isLoggedIn={true} />);
```


### 2. 使用三元运算符


在 JSX 中，可以使用三元运算符进行简洁的条件渲染。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';

const MyComponent = (props) => {
  const isLoggedIn = props.isLoggedIn;

  return (
    <div>
      {isLoggedIn ? <h1>Welcome back!</h1> : <h1>Please sign up.</h1>}
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyComponent isLoggedIn={true} />);
```


### 3. 使用逻辑与 (&&) 运算符


在 JSX 中，可以使用逻辑与运算符来进行条件渲染。如果条件为 true，则渲染后面的元素。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';

const MyComponent = (props) => {
  const isLoggedIn = props.isLoggedIn;

  return (
    <div>
      {isLoggedIn && <h1>Welcome back!</h1>}
      {!isLoggedIn && <h1>Please sign up.</h1>}
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyComponent isLoggedIn={true} />);
```


### 4. 使用 switch 语句

在需要处理多个条件时，可以在 render 方法中使用 switch 语句。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';

class MyComponent extends React.Component {
  render() {
    const userRole = this.props.userRole;
    let content;

    switch (userRole) {
      case 'admin':
        content = <h1>Welcome, Admin!</h1>;
        break;
      case 'user':
        content = <h1>Welcome, User!</h1>;
        break;
      case 'guest':
        content = <h1>Welcome, Guest!</h1>;
        break;
      default:
        content = <h1>Who are you?</h1>;
    }

    return (
      <div>
        {content}
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyComponent userRole="admin" />);
```


### 小结


- **`if` 语句**：适合在 `render` 方法或函数组件的返回值中使用来决定渲染内容。
- **三元运算符**：适合在 JSX 中进行简洁的条件渲染。
- **逻辑与 (`&&`) 运算符**：适合在 JSX 中条件渲染，当条件为 `true` 时渲染元素。
- **`switch` 语句**：适合处理多个条件，进行不同内容的渲染。








	  AI 思考中...





			** [React 安装(CDN)](https://www.runoob.com/react-install-cdn.html)
			[React 路由](https://www.runoob.com/react-router.html) **













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