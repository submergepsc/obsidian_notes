# 使用 Qoder 开发 React

- Source: https://www.runoob.com/react/react-qoder.html

Qoder 是基于 VSCode 开源框架打造的 AI 编程平台，本章节我们将介绍使用 Qoder 开发 React。


Qoder（/ˈkoʊdər/）是一款面向真实软件开发的 Agentic 编码平台,通过增强上下文工程与智能体无缝结合，全面理解你的代码库，并以系统化方式推进开发任务。


Qoder 提供代码智能生成、智能问答、多文件修改、编程智能体等能力，思考更深入、编码更高效、构建更出色，为开发者带来高效、流畅的编码体验。


**Qoder 个人版目前向所有用户提供免费试用。**


---


## 1、注册并安装 Qoder


**我们访问 [**https://qoder.com/**](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz) 注册 QoderWork 账号（免费试用 Pro 版并获赠 300 个 Credits）：**


![](https://www.runoob.com/wp-content/uploads/2026/03/6c1e7ac0-4c98-4438-9c17-e8a5f15cc922.png)


**注册完成后点击右上角的**下载**按钮，根据你的电脑系统，下载安装程序。**


![](https://www.runoob.com/wp-content/uploads/2026/01/1d73bf5c-6bb9-417c-abbf-75987b0b4459.png)


下载后，双击文件开始安装，然后，双击 Qoder IDE 图标启动 Qoder。


相关链接：


- Qoder 官网：[https://qoder.com/](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)
- Qoder 文档：[https://docs.qoder.com/zh/quick-start](https://docs.qoder.com/zh/quick-start)
- Qoder 命令行工具：[https://docs.qoder.com/zh/cli/quick-start](https://docs.qoder.com/zh/cli/quick-start)


---


## 2、登录 Qoder


在 Qoder IDE 右上角，点击用户图标，或使用键盘快捷键（⌘ ⇧ ,（macOS）或 Ctrl Shift ,（Windows）），然后选择 登录。


![](https://www.runoob.com/wp-content/uploads/2026/01/6936bbe1-f329-47c3-b45c-f6dab7dadcdb.png)


如果还没账号，可以在打开的网页中点击底部的**立即注册**链接注册个账号，或使用 Google 或 GitHub 账号直接注册。


![](https://www.runoob.com/wp-content/uploads/2026/01/3afcda57-995c-4540-b22e-7c8527b3ccde.png)


登录成功后，就会返回 Qoder IDE 后，然后我们可以自由使用所有功能。


![](https://www.runoob.com/wp-content/uploads/2026/01/6d00865f-8911-4277-b635-26b50fc8e14b.png)


整个界面上看，Qoder 操作上跟 VS Code 基本也没区别，本身 Qoder 是基于 VSCode 打造的，所以熟悉 VS Code 的用起来也轻车熟路。


### 打开你的 React 项目


- 打开 Qoder。
- 方法一：菜单 **文件 → 打开文件夹**，选择你的项目文件夹（例如 `my-first-react-app`）。
- 方法二（推荐）：在终端进入项目目录，然后一键打开：
```
cd my-first-react-app
qoder .
```
 `**qoder .**` 命令会直接用 Qoder 打开当前文件夹。


现在你看到左侧文件 explorer，显示项目结构（如 src、public 等）。

![](https://www.runoob.com/wp-content/uploads/2026/01/b6cca786-b5ea-4e92-93b2-716db8033250.png)


---


## 3、开始新聊天


### 打开智能会话面板


要开始 AI 对话，登录 Qoder，然后在右上角切换次级侧边栏。


![](https://www.runoob.com/wp-content/uploads/2026/01/829fc8c3-60dd-4569-a7a1-835a19a831ae.png)


或者使用键盘快捷键打开，macOS 快捷键为 **⌘ L**，Windows 快捷键为 **Ctrl L**。


**选择模式：**


- **智能问答：**一个简单的问答模式，用于解答编程问题，它会基于上下文提供解决方案和建议，但不会修改代码。
- **智能体：**一种自主的编码任务执行模式，具备自我决策、环境感知和工具使用能力，可根据开发者的编码需求，借助项目搜索、制定计划、编辑文件、终端操作等工具，端到端完成编码任务。还支持开发者可配置的 MCP（Model Context Protocol）工具，确保编码工作流与个人开发流程高度契合。 ​


![](https://www.runoob.com/wp-content/uploads/2026/01/58735712-581e-47fe-aaf0-5d05acfd7ef7.png)


接下来，我们使用**智能体**模式让它帮我们优化整个项目的样式：


```
优化整个项目的样式
```


![](https://www.runoob.com/wp-content/uploads/2026/01/7dedd340-01e6-4b67-9954-9d12c5011ac1.png)


然后 Qoder 就一顿操作，开始修改，完成后，我们点**接受**按钮即可：


![](https://www.runoob.com/wp-content/uploads/2026/01/8430b48b-9411-487f-872f-1497069f5afa.png)


之后，Qoder 就弹出了完成的效果：


![](https://www.runoob.com/wp-content/uploads/2026/01/1a436e3f-adcc-4480-bf83-9824254e1aa1.png)


另外 Qoder 还有个 Quest 模式，它是 Qoder 的自主编程功能，让 Agent 端到端完成开发任务，我们只需描述目标，Quest 会自主澄清需求、规划方案、执行代码、验证结果——无需持续人工介入。

要使用 Quest 模式只需要在左上交切换即可：


![](https://www.runoob.com/wp-content/uploads/2026/01/32cbb97a-9dc0-43d7-a718-853381f6e532.png)


---


## 4、安装必备插件（Extensions）


Qoder 同样也支持安装插件，点击左侧活动栏的 **Extensions** 图标（四个方块），或按快捷键 `Ctrl+Shift+X`（macOS: `Cmd+Shift+X`）打开扩展市场。


![](https://www.runoob.com/wp-content/uploads/2026/01/cd758197-58cb-46f7-9b1e-fb2a4beabf6e.png)


搜索并安装以下插件（点击 Install）：


![](https://www.runoob.com/wp-content/uploads/2026/01/77aacbb9-a80e-449e-938f-b69e4b5653f5.png)


- **ESLint**（作者：Microsoft） 实时检查代码规范，React 官方推荐。
- 安装后会在代码中标红错误。




**Prettier - Code formatter**（作者：Prettier）


- 自动格式化代码，保持风格统一。




**ES7+ React/Redux/React-Native snippets**（作者：dsznajder）


- 代码片段神器！输入快捷键快速生成组件。
- 常见片段： `rafce` → 生成箭头函数组件 + export default
- `rfc` → 生成函数组件
- `useState` → 快速生成 useState






**Path Intellisense**（作者：Christian Kohler）


- 导入路径自动补全（import 时超级好用）。




**Bracket Pair Colorizer 2** 或内置括号着色


- 括号颜色区分，便于阅读嵌套 JSX。




**GitLens**（可选，但强烈推荐）


- Git 增强，查看代码提交历史。




**React 专属推荐**（可选进阶）：


- **Tailwind CSS IntelliSense**（如果用 Tailwind）
- **React Developer Tools**（浏览器插件已安装，这里不需要）


安装完成后，重启 Qoder（或按 `Ctrl+Shift+P` → Reload Window）。








	  AI 思考中...





			** [使用 VSCode 开发 React](https://www.runoob.com/react-vscode.html)
			[React 在线生成](https://www.runoob.com/react-online.html) **













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