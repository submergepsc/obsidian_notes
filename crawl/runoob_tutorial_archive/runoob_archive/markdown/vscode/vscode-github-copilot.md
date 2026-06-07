# VS Code GitHub Copilot

- Source: https://www.runoob.com/vscode/vscode-github-copilot.html

GitHub Copilot 是由 GitHub 和 OpenAI 联合开发的 AI 编码助手，能够基于上下文自动补全代码、生成函数、优化逻辑，甚至是编写整段的代码模块，帮助开发者更高效地编码。


GitHub Copilot 集成在 VS Code、Visual Studio、JetBrains 等多种 IDE 中，让你在写代码时感觉仿佛有一位经验丰富的搭档随时协助你。


![](https://www.runoob.com/wp-content/uploads/2025/05/Screenshot-GitHub-Copilot.png)


---


## 核心功能


### 代码自动补全


GitHub Copilot 能够根据你的代码上下文和注释，实时提供代码建议。它可以：


- 补全整行代码
- 生成完整函数
- 根据描述性注释生成代码


### 代码解释


Copilot 可以帮助你理解不熟悉的代码：


- 解释复杂代码段的功能
- 提供代码优化建议
- 识别潜在问题


### 多语言支持


支持几乎所有主流编程语言，包括：


- JavaScript/TypeScript
- Python
- Java
- C++
- Go
- Ruby 等


---


## 安装与设置


### 安装步骤


- **前置要求** - VS Code 已正确安装，建议版本在 `1.57` 以上。 - GitHub 账号，并且需要启用 GitHub Copilot 订阅（个人版、团队版、企业版均可）。
- **安装扩展** - 打开 VS Code，进入扩展市场（Extensions Marketplace）。 - 搜索 `GitHub Copilot`。 - 点击 `安装(Install)` 安装。![](https://www.runoob.com/wp-content/uploads/2025/05/f13e57a7-7c73-40e2-9ce1-6e921546a3a2.png) 安装完成后，点击右上角的小图标就可以调出 Copilot 聊天窗口： ![](https://www.runoob.com/wp-content/uploads/2025/05/6dd666d4-9a5f-4d98-b8b1-a15c6e33a875.png) 也可以点击右下角的图标： ![](https://www.runoob.com/wp-content/uploads/2025/05/setup-copilot-status-bar.png)
- **登录 GitHub 账号** - 安装完成后，VS Code 会提示你进行 GitHub 账号登录。 - 点击 `Sign in to GitHub`，浏览器会跳转 GitHub 授权页面，授权后自动返回 VS Code。 ![](https://www.runoob.com/wp-content/uploads/2025/05/setup-copilot-sign-in.png)
- **启用 GitHub Copilot** - 在 VS Code 中按下 `Ctrl + Shift + P`，输入 `Copilot: Enable`。 - 确认启用后，即可开始使用。


安装后，打开 VS Code 的设置，搜索 Copilot,在这里我们可以在 VS Code 设置中调整：


- 建议触发方式（自动或手动）
- 建议显示位置
- 语言偏好设置


![](https://www.runoob.com/wp-content/uploads/2025/05/155ed010-5e90-4dba-be77-7da1758ecd05.png)


---


## 使用技巧


### 智能补全


当你开始输入代码时，GitHub Copilot 会自动给出建议，例如：


```
function fetchData(url) {
    // Copilot 会自动给出一个基于 fetch API 的实现
}
```


![](https://www.runoob.com/wp-content/uploads/2025/05/c19bcfca-81c8-499b-a885-1564b9e31863.png)


我们可以按下 Tab 键接受建议。



- 如果有多种建议，可按 **Ctrl + ]** 或 **Ctrl + [** 切换。
- 如果不想使用建议，按 **Esc** 取消。


### 基于注释生成代码


直接写注释，Copilot 会帮你实现：


```
# 实现一个快速排序算法
```


![](https://www.runoob.com/wp-content/uploads/2025/05/2d1f4fc4-ce73-42ab-965b-eea172d5ba2f.png)


## 实例


```
# 实现一个快速排序算法
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```


### 生成测试用例


你甚至可以直接写注释让 Copilot 帮你生成测试：


```
// 为 quicksort 函数生成单元测试
```


![](https://www.runoob.com/wp-content/uploads/2025/05/0bce8ebb-14e2-476a-a5c3-f3e45419747c.png)


另外我们可以在编辑器中右击鼠标，选择 Copilot，调出需要的功能：


![](https://www.runoob.com/wp-content/uploads/2025/05/a56d7837-5db3-448b-9ff5-464d67e48066.png)


快捷键说明：


| 快捷键 | 功能描述 |
| --- | --- |
| Tab | 接受建议 |
| Esc | 忽略建议 |
| Ctrl + ] | 查看下一个建议 |
| Ctrl + [ | 查看上一个建议 |
| Ctrl + Enter | 打开 Copilot 面板 |
| Ctrl + Shift + P | 启用/禁用 Copilot |


---


## 在 VS Code 中使用聊天功能


在 Visual Studio Code 中使用聊天功能，可以通过自然语言询问有关代码库的问题，或者在项目中进行多文件编辑。聊天功能可以根据你的需求在不同的模式下运行，从提问、进行多文件编辑到启动代理式编码工作流，都能满足你的需求。


你可以在以下场景中使用 VS Code 的聊天功能：


- **理解代码**：例如，"解释这个身份验证中间件是如何工作的？"
- **调试问题**：例如，"为什么我在这个循环中得到一个空引用？"
- **获取代码建议**：例如，"展示如何用 Python 实现二叉搜索树？"
- **优化性能**：例如，"帮我提高这个数据库查询的效率？"
- **学习最佳实践**：例如，"处理异步函数中的错误有什么推荐的方法？"
- **获取 VS Code 小贴士**：例如，"如何自定义键盘快捷键？"


**提示**：如果你还没有 Copilot 订阅，可以通过注册 Copilot 免费计划来免费使用 Copilot，每月有限制的补全和聊天交互次数。


### 聊天模式


根据你的具体需求，你可以选择不同的聊天模式：


| 模式 | 描述 | 场景 |
| --- | --- | --- |
| 提问 (Ask) | 询问有关代码库或技术概念的问题。 | 在稳定版或预览版中打开。理解代码片段的工作原理、头脑风暴软件设计想法或探索新技术。 |
| 编辑 (Edit) | 在代码库中进行多文件编辑。 | 在稳定版或预览版中打开。直接在项目中应用代码编辑，用于实现新功能、修复错误或重构代码。 |
| 代理 (Agent) | 启动代理式编码工作流。 | 在稳定版或预览版中打开。在极少的指导下，自主实现新功能或项目的高级需求，调用工具执行专业任务，并在出现问题时迭代解决。 |


通过在聊天视图中使用模式下拉菜单，可以在不同的聊天模式之间切换。


![](https://www.runoob.com/wp-content/uploads/2025/05/chat-mode-dropdown.png)








	  AI 思考中...





			** [VS Code 活动栏](https://www.runoob.com/vscode-activity-bar.html)
			[VSCode 数据库客户端扩展](https://www.runoob.com/vscode-db-extensions.html) **













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