# C++ AI 编程助手

- Source: https://www.runoob.com/cplusplus/fitten-code-cpp.html

这两年 AI 发展迅猛，作为开发人员，我们总是追求更快、更高效的工作方式，AI 的出现可以说改变了很多人的编程方式。


AI 对我们来说就是一个可靠的编程助手，给我们提供了实时的建议和解决方案，无论是快速修复错误、提升代码质量，或者查找关键文档和资源，AI 作为编程助手都能让你事半功倍。


今天为大家推荐一款适配了 Visual Studio(本文使用)，VS Code(本文使用)，JetBrains系列以及Vim等多种编译器环境的插件 Fitten Code，Fitten Code 是由非十大模型驱动的 AI 编程助手，它可以自动生成代码，提升开发效率，帮您调试 Bug，节省您的时间，另外还可以对话聊天，解决您编程碰到的问题。


![](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/mazeGame.png)


以上是使用 Fitten Code 的 Agent 功能模拟的C语言和C++地形生成算法在控制台上的可视化效果。只需要输入简单的命令就能快速看到复杂的算法呈现的效果！


除此之外，Fitten Code 不仅免费，它还支持 80 多种语言：Python、C、Javascript、Typescript、Java 等。


**一、VS Code 版本**


- 1. 安装
- 2. 智能补全
- 3. Agent 自主编程智能体
- 4. AI问答


**二、Visual studio 版本**

- 1. 安装
- 2. 智能补全
- 3. AI问答
- 4. 生成代码
- 5. 代码翻译
- 6. 生成注释
- 7. 解释代码
- 8. 生成测试
- 9. 检查 BUG
- 10. 编辑代码


## 一、VS Code版本


### 1、安装


如果您已经安装 VS Code 且版本大于等于1.68.0，请直接跳过此步骤，否则请点击[下载](https://code.visualstudio.com/download)前往官网下载安装 VS Code。


打开 VS Code，点击左侧 Extensions（扩展）按钮：


![](https://www.runoob.com/wp-content/uploads/2024/04/img_256-9.png)


在搜索框中搜索关键字 Fitten Code：


![](https://www.runoob.com/wp-content/uploads/2024/04/img_256-10.png)


在搜索结果中点击Install：


![](https://www.runoob.com/wp-content/uploads/2024/04/img_256-11.png)


登录注册后即可开始使用：


![](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/image4.jpg)

### 2、智能补全


打开代码文件，输入一段代码，Fitten Code 就会为您自动补全代码：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-5.png)


按下 Tab 键接受所有补全建议：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-6.png)


按下 Ctrl+→ 键(mac系统为Command+→)接收单个词补全建议：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-7.png)


按下 **Esc** 键取消补全建议：


代码智能补全分为三种：普通补全、整项目感知补全、编辑式补全。


具体更详细的补全用法的技巧可详见以下视频：


*


### Agent 自主编程智能体


自主编程智能体具备强大的主动执行能力：


- 根据任务需求智能调用工具，主动分析背景信息；
- 自主拆解复杂问题，通过多步骤迭代精准完成任务；
- 显著提升编程自动化效率与精细度。


在使用该功能时，只需要输入需要完成的开发任务，例如"将此函数拆分成多个文件并放入当前文件夹下"、"批量优化该文件夹下所有代码文件中的代码"等，智能体就可以根据任务调用不同工具逐步完成开发任务。


![](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/agent基础用法.jpg)


在 Agent 执行的过程中，涉及到创建和修改文件、执行终端命令的操作时，点击"同意"或"拒绝"即可。


![](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/同意或拒绝.jpg)


需要和智能体结束对话时，点击右上角菜单中的："回到首页" 即可。


![](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/回到首页.jpg)


更多关于 Agent 的使用技巧和方法可以参考以下视频：


#### 添加Rules


在开发程序时，用户项目往往有着各种各样的要求，例如 "文件名统一用大驼峰"、"本项目使用C++17标准，不要使用C++20或C++23的新特性"、"除非必要，否则不要使用union" 等等要求，如果Agent不知道用户项目定制化的特殊要求，用户可以将这些要求写入规则文件，进而增强Agent的代码生成规范和行为规范。


例如：在Rules中添加项目的背景介绍和技术栈，Agent在执行文件创建、重命名时能够更加符合项目规范。或者在Rules中添加代码风格要求、Agent在生成代码时能够更加定制化。您甚至可以告诉Agent、每次在执行任务前都先阅读一遍指定目录下的所有README文档，进而更改Agent的行为。


![](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/添加rules方法.png)


添加rules后，会自动出现Rules文件编辑界面，在此处写入文字，每次调用Agent智能体时，智能体将自动读取已写好的rules文件。进而增强对当前整个项目的理解能力，生成更规范、符合项目要求的代码和回答。


更多关于rules的使用方法可以参考如下视频：


#### 添加MCP


用户可以使用MCP功能来给Agent增加额外的自定义工具。例如"Excel读取工具"、"github服务"、"bing搜索服务"等。使得Agent具有自动操作并修改Excel等非代码文件的能力、自动调研开源框架和新技术栈的能力、联网搜索某新概念的能力等等。


关于MCP的详细使用方法、以及实战技巧可参考以下视频：


通过MCP和Rules的组合使用，可以极大地提高Agent的能力，使得Agent能够像一个智能助手一样完成庞大项目的功能开发任务。


### 3、AI 问答


#### 基础用法


点击首页左下角的 Chat 模式，开始进行对话。


![](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/chat模式.jpg)


当用户选中文件中的代码段再进行对话时，Fitten Code 会自动引用用户所选中的代码段，此时可直接针对该代码段进行问询等操作：


![](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/chat模式选中代码.png)


#### 右键代码快速询问


用户可能选中代码后经常会进行一些高频的提问，例如"这段代码是什么意思"、"帮我给这段代码添加注释"、"帮我优化这段代码"等等。因此用户可以直接通过选中代码后右键，找到FittenCode右键选项点击即可立刻调用FittenCode智能对话。


![IMG_277](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/右键菜单.png)


通过这些常用对话的右键快速调用，可以极大地提高开发效率。


#### 常用语快速输入


Fitten Code 对话框中具有一项特色功能：常用语，它可以让用户快速地在对话框中输入用户经常重复输入的内容，进而构建一个更加强效的提示词、更加全面的上下文环境。


具体关于常用语的实战技巧可以观看如下视频：


### 常见问题


如果 VSCode 远程服务器 remote 无法连接外网时，请点击左下角 `⚙` 按钮，再点击设置：


![IMG_277](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/image27.png)


然后在设置页面点击右上角 \"打开设置(JSON)\":


![IMG_278](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/image28.png)


最后只需在在弹出的 settings.json 文件中添加以下内容即可:


```
"remote.extensionKind": { "FittenTech.Fitten-Code": ["ui"] }
```


![IMG_279](https://static.jyshare.com/images/re/fittencode/202509/cplusplus/image29.png)


更多内容参考官网：[https://code.fittentech.com/](https://code.fittentech.com/)


支持以下 4 种编辑器与开发环境：


- VS Code：本文会详细介绍
- [JetBrains IDE 系列（包括 PyCharm）](https://code.fittentech.com/tutor_jetbrains_zh#1)
- [Visual Studio](https://code.fittentech.com/tutor_vs_zh#1)：本文会详细介绍
- [Vim](https://code.fittentech.com/tutor_vim_zh#1)


---

## 二、Visual Studio版本


### 1、安装


点击上方工具栏拓展选项，选择管理拓展选项


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-28.png)


接着在联机页面中搜索"FItten Code"，并点击下载，下载完成后重启Visual Studio


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-29.png)


在扩展选项中选中fitten，选择Open Chat Window进入登录界面，完成注册登录


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-30.png)

### 2、智能补全


打开代码文件，输入一段代码，Fitten Code 就会为您自动补全代码：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-31.png)


按下 Tab 键接受所有补全建议：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-32.png)


按下 Ctrl+→ 键接收单个词补全建议：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-33.png)

### 3、AI 问答


用户可通过点击左上角工具栏中的"Fitten Code – 开始新对话"打开对话窗口进行对话：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-34.png)

### 4、生成代码


可在Fitten Code工具栏中选择"Fitten Code - 生成代码"，然后在输入框中输入指令即可生成代码


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-35.png)


利用注释后的自动补全功能生成代码


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-36.png)


也可以利用对话功能生成代码


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-37.png)

### 5、代码翻译


Fitten Code可以实现代码的语义级翻译，并支持多种编程语言之间的互译。有以下两种方法可以实现。


（1）选中需要进行翻译的代码段，右键选择"Fitten Code – 重构选择代码"，然后在输入框中输入需求即可完成转换


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-38.png)


（2）选中需要进行翻译的代码段，点击左侧工具栏中的"Fitten Code – 开始新对话"。然后在输入框中输入需求即可完成转换


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-39.png)

### 6、生成注释


Fitten Code 能够根据您的代码自动生成相关注释，通过分析您的代码逻辑和结构，为您的代码提供清晰易懂的解释和文档，不仅提高代码的可读性，还方便其他开发人员理解和使用您的代码。先选中需要生成注释的代码段，然后右键选择 "Fitten Code – 生成注释"：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-40.png)


也可以通过对话功能实现


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-41.png)

### 7、解释代码


Fitten Code 可以对一段代码进行解释，可以通过选中代码段然后右键选择 "Fitten Code – 解释代码" 进行解释，如下图所示：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-42.png)


也可以通过对话功能实现


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-43.png)

### 8、生成测试


Fitten Code 拥有自动生成单元测试的功能，可以根据代码自动产生相应的测试用例，提高代码质量和可靠性。通过选中代码段后右键选择 "Fitten Code – 生成函数单元测试" 来实现，如下图所示：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-44.png)


也可以通过对话功能实现


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-45.png)

### 9、检查 BUG


在开始新对话窗口向Fitten Code提问代码bug查找后，Fitten Code可以智能完成debug工作


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-46.png)

### 10、编辑代码


在开始新对话窗口向FittenCode提供需要编辑的代码段，并输入需求，Fitten可以完成代码编辑工作：


![](https://www.runoob.com/wp-content/uploads/2024/04/word-image-25346-47.png)


更多内容参考官网：[https://code.fittentech.com/](https://code.fittentech.com/)


支持以下 4 种编辑器与开发环境：


- [VS Code](https://code.fittentech.com/tutor_vscode_zh)：本文已详细介绍
- [JetBrains IDE 系列（包括PyCharm）](https://code.fittentech.com/tutor_jetbrains_zh)
- [Visual Studio](https://code.fittentech.com/tutor_vs_zh)：本文会详细介绍
- [Vim](https://code.fittentech.com/tutor_vim_zh)








	  AI 思考中...





			* [C++ 测验](https://www.runoob.com/../quiz/cpp-quiz.html)
			[C++ vector 容器](https://www.runoob.com/cpp-vector.html) **













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