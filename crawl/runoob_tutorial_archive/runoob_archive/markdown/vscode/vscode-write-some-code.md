# VSCode 编写代码

- Source: https://www.runoob.com/vscode/vscode-write-some-code.html

VS Code 内置了对 JavaScript、TypeScript、HTML、CSS 等多种语言的支持。

在本章节中，我们将创建一个 JavaScript 代码文件，并使用 VS Code 提供的一些代码编辑功能。


VS Code 支持多种编程语言，在后面的章节中，我们还会安装 [Python 的语言扩展](https://www.runoob.com/vscode-extensions.html)，为其他语言添加支持。


### 1、创建 JavaScript 文件并编写代码

在资源管理器（Explorer）视图中，创建一个名为 app.js 的新文件，并输入以下 JavaScript 代码：


## 实例


```
function sayHello(name) {
  console.log('Hello, ' + name);
}

sayHello('VS Code');
```


**代码自动补全（IntelliSense）：**当您开始输入代码时，会弹出代码补全建议，使用方向键 **↑** 或 **↓**（上下键） 导航建议项，按 **Tab** 键选择并插入选中的建议。


**语法高亮：**注意代码的格式化显示（语法高亮），这有助于区分代码的不同部分，提高可读性。


![](https://www.runoob.com/wp-content/uploads/2024/12/javascript-intellisense.gif)


### 使用代码操作（Code Actions）

将光标放在字符串 'Hello,' 上时，您会看到一个小灯泡图标，表示可以应用代码操作（Code Action）。


您也可以使用快捷键 **⌃Space** 打开灯泡菜单。

点击灯泡图标，然后选择 Convert to template string（转换为模板字符串）。


![](https://www.runoob.com/wp-content/uploads/2024/12/code-action-template-string.png)


代码操作为您的代码提供了快速修复建议。

在本例中，Code Action 将字符串拼接：


```
"Hello, " + name
```


转换为模板字符串：


```
`Hello, ${name}`
```


模板字符串是 JavaScript 中一种特殊的语法，可以在字符串中嵌入表达式。


转化后的代码如下：


![](https://www.runoob.com/wp-content/uploads/2024/12/8ba7d8e0-91e0-4dee-bb37-1fd7fa7ee896.png)








	  AI 思考中...





			** [VS Code 设置](https://www.runoob.com/vscode-settings.html)
			[VSCode 版本控制](https://www.runoob.com/vscode-source-control.html) **













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