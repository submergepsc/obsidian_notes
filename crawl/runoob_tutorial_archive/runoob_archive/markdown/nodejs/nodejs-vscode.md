# 使用 VS Code 开发 Node.js

- Source: https://www.runoob.com/nodejs/nodejs-vscode.html

Visual Studio Code（简称 VS Code）是微软开发的免费开源代码编辑器， 是目前最受欢迎的 Node.js 开发编辑器之一。


### 主要优势


- **内置 Node.js 支持**：提供智能代码补全、调试等功能
- **丰富的扩展**：可通过扩展市场安装各种 Node.js 开发工具
- **集成终端**：直接在编辑器中运行 Node.js 程序
- **轻量快速**：启动速度快，资源占用低


### 安装 VS Code


- 访问 [VS Code 官网](https://code.visualstudio.com/)
- 下载对应操作系统的版本
- 按照安装向导完成安装
- VS Code 完整教程：[https://www.runoob.com/vscode/vscode-tutorial.html](https://www.runoob.com/../vscode/vscode-tutorial.html)


另外国内阿里与字节也有基于 VS Code 开发的 AI IDE：


  [阿里 Qoder 阿里推出的 AI 编程 IDE，基于 VS Code 深度定制 访问 →](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)


  [字节 Trae 字节跳动推出的新一代 AI 原生开发环境 访问 →](https://www.trae.com.cn/?utm_source=advertising&utm_medium=runoob_ug_cpa&utm_term=hw_trae_runoob)


### 扩展推荐


- **Node.js Extension Pack**：包含多个 Node.js 相关插件的集合包
- **JavaScript (ES6) code snippets**：提供 ES6+ 代码片段
- **Auto Rename Tag**：自动重命名 HTML/XML 标签
- **ESLint**：代码质量检查工具
- **Prettier**：代码格式化工具
- **npm Intellisense**：npm 包自动补全
- **Path Intellisense**：文件路径自动补全


---


## 创建第一个 Node.js 项目


### 初始化项目


- 打开终端（VS Code 中按 Ctrl+`）
- 创建项目文件夹并进入：
```
mkdir my-node-app
cd my-node-app
```

- 初始化 npm 项目：
```
npm init -y
```
 会生产一个 package.json 的文件： ![](https://www.runoob.com/wp-content/uploads/2025/05/b6cae63f-df15-47de-b379-6fd9bc39eae8-1.png)


### 创建主文件


- 在 VS Code 中创建 `app.js` 文件
- 输入以下代码： ## 实例
```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end(' RUNOOB Node Test ~ Hello, Node.js!\n');
});

const port = 3000;
server.listen(port, () => {
  console.log(`服务器运行地址：http://localhost:${port}/`);
});
```


### 运行项目


- 在终端中执行：
```
node app.js
```
 ![](https://www.runoob.com/wp-content/uploads/2025/05/7223c8bb-7f91-44ec-9acf-f8492fdb6442-1.png)
- 打开浏览器访问 `http://localhost:3000` ![](https://www.runoob.com/wp-content/uploads/2025/05/30681c6b-e938-4c98-b738-d66ab1a3caf2-1.png)


请注意我们在输入 **console.** 时，VS Code 的智能感知可以提供代码的建议：


![](https://www.runoob.com/wp-content/uploads/2025/05/consoleintellisense.png)


---


## 调试 Node.js 应用


VS Code 提供了强大的调试功能：


### 配置调试


- 点击左侧活动栏的"运行和调试"图标
- 点击"创建 launch.json 文件"
- 选择"Node.js"环境


![](https://www.runoob.com/wp-content/uploads/2025/05/39634704-c2ef-4521-8e19-c15014879534.png)


### 设置断点


- 在代码行号左侧点击设置断点
- 按 F5 启动调试
- 使用调试工具栏控制执行流程


### 调试控制


- **继续(F5)**：继续执行到下一个断点
- **单步跳过(F10)**：执行当前行，不进入函数
- **单步调试(F11)**：进入函数内部
- **重启(Ctrl+Shift+F5)**：重新开始调试
- **停止(Shift+F5)**：结束调试









	  AI 思考中...





			** [Node.js async/await](https://www.runoob.com/nodejs-async-await.html)
			[Node.js 内置模块](https://www.runoob.com/nodejs-buildin-modules.html) **













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