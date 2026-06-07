# React 路由

- Source: https://www.runoob.com/react/react-router.html

React 路由通常使用 react-router 库来实现，它是一个功能强大的库，用于在 React 应用程序中实现客户端路由。以下是关于如何在 React 中使用 React Router 的详细说明：


## 安装 React Router

首先，你需要安装 react-router-dom 包，这是用于在浏览器环境中实现路由的包。


```
npm install react-router-dom
```


## 基本用法

以下是使用 React Router 设置基本路由的步骤和示例代码。


### 1. 创建基础路由组件


首先，创建一些简单的组件，它们将被路由渲染。


## 实例


```javascript
import React from 'react';

const Home = () => {
  return <h2>Home</h2>;
};

export default Home;

// About.js
import React from 'react';

const About = () => {
  return <h2>About</h2>;
};

export default About;

// Contact.js
import React from 'react';

const Contact = () => {
  return <h2>Contact</h2>;
};

export default Contact;
```


### 2. 设置路由

在你的主应用组件中，使用 react-router-dom 的组件来设置路由。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from 'react-router-dom';

import Home from './Home';
import About from './About';
import Contact from './Contact';

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/contact">Contact</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </Router>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```


## 嵌套路由


React Router 允许你创建嵌套路由，这样可以在一个组件内渲染更多的路由。


## 实例


```javascript
// Dashboard.js
import React from 'react';
import { Link, Outlet } from 'react-router-dom';

const Dashboard = () => {
  return (
    <div>
      <h2>Dashboard</h2>
      <nav>
        <ul>
          <li>
            <Link to="profile">Profile</Link>
          </li>
          <li>
            <Link to="settings">Settings</Link>
          </li>
        </ul>
      </nav>
      <Outlet />
    </div>
  );
};

export default Dashboard;
```


## 实例


```javascript
// Profile.js
import React from 'react';

const Profile = () => {
  return <h2>Profile</h2>;
};

export default Profile;
```


## 实例


```javascript
// Settings.js
import React from 'react';

const Settings = () => {
  return <h2>Settings</h2>;
};

export default Settings;
```


在主应用组件中设置嵌套路由：


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from 'react-router-dom';

import Home from './Home';
import About from './About';
import Contact from './Contact';
import Dashboard from './Dashboard';
import Profile from './Profile';
import Settings from './Settings';

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/contact">Contact</Link>
            </li>
            <li>
              <Link to="/dashboard">Dashboard</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/dashboard" element={<Dashboard />}>
            <Route path="profile" element={<Profile />} />
            <Route path="settings" element={<Settings />} />
          </Route>
        </Routes>
      </div>
    </Router>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```


## 动态路由

可以在路径中包含动态参数。


## 实例


```javascript
// User.js
import React from 'react';
import { useParams } from 'react-router-dom';

const User = () => {
  const { userId } = useParams();
  return <h2>User ID: {userId}</h2>;
};

export default User;
```


在主应用组件中设置动态路由：


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from 'react-router-dom';

import Home from './Home';
import About from './About';
import Contact from './Contact';
import Dashboard from './Dashboard';
import Profile from './Profile';
import Settings from './Settings';
import User from './User';

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/contact">Contact</Link>
            </li>
            <li>
              <Link to="/dashboard">Dashboard</Link>
            </li>
            <li>
              <Link to="/user/1">User 1</Link>
            </li>
            <li>
              <Link to="/user/2">User 2</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/dashboard" element={<Dashboard />}>
            <Route path="profile" element={<Profile />} />
            <Route path="settings" element={<Settings />} />
          </Route>
          <Route path="/user/:userId" element={<User />} />
        </Routes>
      </div>
    </Router>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```


## 404 页面

可以使用 React Router 提供的 Navigate 组件来实现 404 页面重定向。


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  Navigate
} from 'react-router-dom';

import Home from './Home';
import About from './About';
import Contact from './Contact';
import Dashboard from './Dashboard';
import Profile from './Profile';
import Settings from './Settings';
import User from './User';

const NotFound = () => {
  return <h2>404 Page Not Found</h2>;
};

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
            <li>
              <Link to="/contact">Contact</Link>
            </li>
            <li>
              <Link to="/dashboard">Dashboard</Link>
            </li>
            <li>
              <Link to="/user/1">User 1</Link>
            </li>
            <li>
              <Link to="/user/2">User 2</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/dashboard" element={<Dashboard />}>
            <Route path="profile" element={<Profile />} />
            <Route path="settings" element={<Settings />} />
          </Route>
          <Route path="/user/:userId" element={<User />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </Router>
  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```


### 小结

通过使用 React Router，你可以轻松地在 React 应用中实现路由功能，包括基本路由、嵌套路由、动态路由以及 404 页面等。通过这种方式，你可以创建一个功能强大且用户友好的单页应用程序 (SPA)。








	  AI 思考中...





			** [React 条件判断](https://www.runoob.com/react-conditional.html)
			[React Memo](https://www.runoob.com/react-memo.html) **













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