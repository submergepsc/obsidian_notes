# VSCode code 命令

- Source: https://www.runoob.com/vscode/vscode-code-command.html

在 Visual Studio Code 中，code 命令是一个命令行工具，用于快速打开 VS Code 并执行一些与代码相关的操作。


code 命令直接可以帮助开发者从终端或命令提示符中直接启动 VS Code 或处理特定的任务。


最常用的方式就是使用 **code** 命令直接从命令行中打开文件目录，此时需要先安装 code 命令。


Windows 系统安装 VS Code 后，code 命令会自动注册到系统环境变量中，如果未注册，可以手动添加 VS Code 的安装路径到 PATH 环境变量中。


启用 VSCode 的 code 命令 非常简单，先打开命令面板：



- macOS 系统快捷键：**⇧⌘P（command + shift + p）**
- Windows/Linux 快捷键: **Ctrl + Shift + P**


搜索安装** >shell command**:


![](https://www.runoob.com/wp-content/uploads/2024/12/525b3be6-bc44-4043-acaa-3874afbba399.png)

然后选择 **在 PATH 中 安装"code"命令 - Shell Command: Install 'code' command in PATH** 即可为系统 PATH 路径添加了 **code** 命令的引用。

我们可以通过命令行打开文件、安装扩展、修改显示语言，甚至查看诊断信息。


![](https://www.runoob.com/wp-content/uploads/2024/12/hero.png)


以下是一些常用的命令行选项，可以通过 **code --help** 命令查看：


![](https://www.runoob.com/wp-content/uploads/2024/12/command-line-help.png)


我们可以在命令行中使用 **code .** 命令让文件夹在 VS Code 中打开：


![](https://www.runoob.com/wp-content/uploads/2024/12/launch-vscode.png)


| 命令 | 功能说明 |
| --- | --- |
| code | 打开文件或文件夹 |
| code . | 打开当前目录作为工作区 |
| code --new-window | 在新窗口中打开 |
| code --diff | 对比两个文件的内容 |
| code --wait | 等待窗口关闭后再返回终端 |
| code --disable-extensions | 禁用所有扩展运行 VS Code |
| code --install-extension | 安装指定扩展 |
| code --list-extensions | 列出所有已安装的扩展 |
| code --uninstall-extension | 卸载指定扩展 |


### code 命令的常用功能


**1. 打开文件或文件夹**


```
code <文件路径>
```


例如打开 app.js 文件：


```
code app.js
```


打开文件夹（以工作区的方式）：


```
code <文件夹路径>
```


例如打开 my-project 文件夹：


```
code my-project
```


**2. 创建新文件**

如果指定的文件不存在，code 会创建该文件并打开它：


```
code newfile.js
```


** 3. 以当前目录为工作区打开 VS Code**

直接运行 code 命令会以当前终端所在目录为工作区启动 VS Code：


```
code .
```


**4. 对比文件**

code 命令支持文件内容对比：


```
code --diff <文件1> <文件2>
```


示例：


```
code --diff index.html index-backup.html
```


**5. 查看帮助**


查看 code 命令的所有可用选项：


```
code --help
```


---


## 使用 code 命令打开 vue 项目


### 创建 vue 项目


打开终端或命令提示符，输入以下命令创建 vue 项目：


```
npm create vue@latest
```


系统会提示输入项目名称，我这边输入 **runoob-vue3-app**：


```
Vue.js - The Progressive JavaScript Framework

? 请输入项目名称： › runoob-vue3-app
```


之后会有一些选项，可以根据自己的需求选择，或者一路回车：


```
Vue.js - The Progressive JavaScript Framework

> 请输入项目名称： … runoob-vue3-app
> 是否使用 TypeScript 语法？ … 否 / 是
> 是否启用 JSX 支持？ … 否 / 是
> 是否引入 Vue Router 进行单页面应用开发？ … 否 / 是
> 是否引入 Pinia 用于状态管理？ … 否 / 是
> 是否引入 Vitest 用于单元测试？ … 否 / 是
> 是否要引入一款端到端（End to End）测试工具？ › 不需要
> 是否引入 ESLint 用于代码质量检测？ › 否

正在初始化项目 /Users/Runoob/runoob-vue3-app...

项目初始化完成，可执行以下命令：

  cd runoob-vue3-app
  npm install
  npm run dev
```


项目创建完成后，进入项目文件夹并安装依赖：


```
cd runoob-vue3-app
npm install
```


安装依赖可能也需要几分钟。


输入以下命令快速启动你的 Vue 应用：


```
npm run dev
```


![](https://www.runoob.com/wp-content/uploads/2024/12/5b86495e-b6ab-4e7d-ad42-7830f404cb52.png)


在浏览器中打开 http://localhost:5173，显示如下：


![](https://www.runoob.com/wp-content/uploads/2024/12/welcome-to-vue.png)


按下 Ctrl+C 可以停止 vue-cli-service 服务器。


### 使用 code 命令打开 vue 项目


从终端或命令提示符中进入我们创建的 Vue 项目文件夹 runoob-vue3-app，然后使用 **code** 命令让项目在 VS Code 中打开：


```
cd runoob-vue3-app
code .
```


VS Code 将启动并在文件资源管理器中显示你的 Vue 项目，显示如下：


![](https://www.runoob.com/wp-content/uploads/2024/12/ca088f16-c443-444d-b5ec-45d95f153817.png)









	  AI 思考中...





			** [VSCode 运行和调试代码](https://www.runoob.com/vscode-run-and-debug.html)
			[VSCode 快捷键大全](https://www.runoob.com/vscode-shortcut-keys.html) **













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