# TypeScript 安装

- Source: https://www.runoob.com/typescript/ts-install.html

本文介绍 TypeScript 环境的安装。


我们需要使用到 npm 工具安装，如果你还不了解 npm，可以参考我们的[NPM 使用介绍](https://www.runoob.com/../nodejs/nodejs-npm.html)。


### NPM 安装 TypeScript


如果你的本地环境已经安装了 npm 工具，可以使用以下命令来安装。


使用国内镜像：


```
npm config set registry https://registry.npmmirror.com
```


安装 typescript：


```
npm install -g typescript
```


安装完成后我们可以使用 **tsc** 命令来执行 TypeScript 的相关代码，以下是查看版本号：


```
$ tsc -v
Version 3.2.2
```


然后我们新建一个 app.ts 的文件，代码如下：


```javascript
var message:string = "Hello World"
console.log(message)
```


通常我们使用 **.ts** 作为 TypeScript 代码文件的扩展名。


然后执行以下命令将 TypeScript 转换为 JavaScript 代码：


```
tsc app.ts
```


![](https://www.runoob.com/wp-content/uploads/2019/01/typescript_compiler.png)


这时候在当前目录下（与 app.ts 同一目录）就会生成一个 app.js 文件，代码如下：


```javascript
var message = "Hello World";
console.log(message);
```


使用 node 命令来执行 app.js 文件：


```
$ node app.js
Hello World
```


TypeScript 转换为 JavaScript 过程如下图：


![](https://www.runoob.com/wp-content/uploads/2019/01/ts-2020-12-01-1.png)


---


## VS Code 介绍


很多 IDE 都有支持 TypeScript 插件，如：VS Code，Sublime Text 2，WebStorm / PHPStorm，Eclipse 等。


本章节主要介绍 VS Code，VS Code 是一个可以运行于 Mac OS X、Windows 和 Linux 之上的，针对于编写现代 Web 和云应用的跨平台源代码编辑器，由 Microsoft 公司开发。


VS Code 教程：[https://www.runoob.com/vscode/vscode-tutorial.html](https://www.runoob.com/../vscode/vscode-tutorial.html)

**
另外国内阿里与字节也有基于 VS Code 开发的 AI IDE：


- **阿里 Qoder：**[https://qoder.com/](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)
- **字节 Trae：**[https://www.trae.com.cn/](https://www.trae.com.cn/?utm_source=advertising&utm_medium=runoob_ug_cpa&utm_term=hw_trae_runoob)


### Windows 上安装 Visual Studio Code


1、下载 [Visual Studio Code](https://code.visualstudio.com/)。


![](https://www.runoob.com/wp-content/uploads/2019/01/9EDCE892-F34A-4D0C-82BF-03175CFA5F91.jpg)


2、双击 VSCodeSetup.exe 图标 ![](https://www.runoob.com/wp-content/uploads/2019/01/1546508926-7107-launch-setup-process.jpg) 安装。


![](https://www.runoob.com/wp-content/uploads/2019/01/1546508925-5165-setup-wizard.jpg)


3、安装完成后，打开 Visual Studio Code 界面类似如下：


![](https://www.runoob.com/wp-content/uploads/2019/01/1546508924-5187-ide.jpg)


4、 我们可以在左侧窗口中点击当前编辑的代码文件，选择 open in command prompt**（在终端中打开），这时候我们就可以在屏幕的右侧下半部分使用 **tsc** 命令来执行 TypeScript 文件代码了。


![](https://www.runoob.com/wp-content/uploads/2019/01/1546508926-3046-traverse-files-path.jpg)

### Mac OS X 安装 Visual Studio Code


Mac OS X 安装配置 Visual Studio Code 可以查看： [https://code.visualstudio.com/Docs/editor/setup](https://code.visualstudio.com/docs/setup/setup-overview)


### Linux 安装 Visual Studio Code


Linux 安装配置 Visual Studio Code 可以查看： [https://code.visualstudio.com/Docs/editor/setup](https://code.visualstudio.com/docs/setup/setup-overview)








	  AI 思考中...





			** [TypeScript 教程](https://www.runoob.com/ts-tutorial.html)
			[TypeScript 基础语法](https://www.runoob.com/ts-basic-syntax.html) **













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