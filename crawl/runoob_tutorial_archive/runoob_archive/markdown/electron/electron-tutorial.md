# Electron 教程

- Source: https://www.runoob.com/electron/electron-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/10/652fc697b821a12c35538d52_1.jpg)

Electron（原名 Atom Shell） 是由 GitHub 开发的一个 开源跨平台桌面应用开发框架。


Electron 是一个开源的框架，专门用于使用 Web 技术（HTML、CSS 和 JavaScript）来构建跨平台的桌面应用程序。


Electron 让我们可以像写网页一样写桌面应用，比如 Windows 的 .exe、macOS 的 .app、Linux 的可执行文件。


**Electron = Chromium（浏览器引擎） + Node.js（后端能力） + 桌面应用壳。**


---


## 学习 Electron 需要的基础知识？


学习 Electron 前，掌握这几样就够了：


- **会点 [JavaScript](https://www.runoob.com/../js/js-tutorial.html)**。
- **会用 [Node.js](https://www.runoob.com/../nodejs/nodejs-tutorial.html) 和 [npm](https://www.runoob.com/../nodejs/nodejs-npm.html)** 来运行脚本。
- **懂点 [HTML](https://www.runoob.com/../html/html-tutorial.html) 和选择器**（比如 `#id`、`.class`）；
- **能用终端** 跑命令。


---


## 核心概念


想象一下，你平时用浏览器访问网站时，看到的是由 HTML 构建的页面，用 CSS 美化样式，用 JavaScript 实现交互功能。Electron 就像是把一个浏览器打包"起来，让它能够独立运行，不再需要用户手动打开浏览器。


**技术组成**：


- **Chromium**：提供页面渲染引擎，确保你的应用界面能够正常显示
- **Node.js**：提供系统级的 API，让你能够访问文件系统、网络等底层功能
- **Native APIs**：允许调用操作系统的原生功能，如菜单、对话框等


---


## 为什么选择 Electron？


### 开发优势


**1. 技术栈统一**


- 使用熟悉的 Web 技术开发
- 前端开发者可以快速上手
- 丰富的 Web 生态资源可用


**2. 跨平台支持**


- 一次开发，多平台运行
- 支持 Windows、macOS、Linux
- 界面和功能在不同系统上保持一致


**3. 开发效率高**


- 热重载功能，实时预览修改效果
- 调试工具完善，可以使用 Chrome DevTools
- 社区活跃，问题解决快速


---


## 实例

假设我们想做一个记事本应用。


在 Electron 中，你只需要：


```
npm install electron
```


创建一个 main.js：


## 实例


```
const { app, BrowserWindow } = require('electron');

app.whenReady().then(() => {
  const win = new BrowserWindow({
    width: 800,
    height: 600
  });
  win.loadFile('index.html'); // 这里就是你的网页界面
});
```


然后 index.html 就是普通网页：


## 实例


```
<h1>我的桌面记事本</h1>
<textarea></textarea>
```


运行：


```
npx electron .
```


这样我们的网页就变身为桌面应用啦！


---


## 参考资源


- [Electron 官网](https://www.electronjs.org)
- [Electron 官方文档](https://www.electronjs.org/docs)
- [Electron Fiddle](https://electronjs.org/fiddle) - 实验和分享 Electron 代码片段的工具
- [awesome-electron](https://github.com/sindresorhus/awesome-electron) - Electron 资源合集








	  AI 思考中...






			[Electron 简介](https://www.runoob.com/electron-intro.html) **













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