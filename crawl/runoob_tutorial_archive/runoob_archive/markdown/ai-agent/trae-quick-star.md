# TRAE 教程

- Source: https://www.runoob.com/ai-agent/trae-quick-star.html

Trae（读作 /treɪ/）是字节跳动推出的一款 AI 原生集成开发环境（IDE），深度集成 Claude 和 GPT-4o 等大模型，提供智能问答、代码补全和 AI 自动编程能力。


Trae 基于 VS Code 内核开发，界面友好使用与 [VS Code](https://www.runoob.com/../vscode/vscode-code-command.html) 差不多。


Trae 主要特点包括：


- **全中文界面**，无需安装汉化插件，开箱即用
- **内置 AI 助手**，支持 Chat（问答）和 Builder（项目构建）两种模式
- **兼容 VS Code 生态**，可一键导入插件、快捷键、配置文件
- **支持多平台**：Windows 和 macOS，Linux 版本可预约
- **完全免费**，无需付费订阅即可使用 AI 功能


---


## 安装 Trae


### 1. 下载安装包


  **


    **访问 Trae 国内官网：**
    [Trae 官网](https://www.trae.com.cn/?utm_source=advertising&utm_medium=runoob_ug_cpa&utm_term=hw_trae_runoob)



官网会自动识别你的操作系统并推荐对应版本。你也可以手动选择：


| 操作系统 | 下载版本 |
| --- | --- |
| Windows | .exe 安装包 |
| macOS（Intel） | .dmg 安装包 |
| macOS（Apple Silicon） | .dmg ARM 版本 |


![](https://www.runoob.com/wp-content/uploads/2026/03/ae8fb1d3-c3bd-4166-abe7-780a5c3213f9.png)


### 2. 安装步骤


下载完成后，双击安装包，按照提示完成安装，整个过程与安装普通软件无异，约 1~2 分钟即可完成。


### 3. 初始配置


首次启动 Trae 时，会进入初始配置向导：


**第一步：选择主题****可选项为「暗色」、「亮色」或「深蓝」，根据个人喜好选择即可，后续可在设置中随时更改。


第二步：选择显示语言****可选「简体中文」或「English」。中文开发者直接选简体中文，界面将完全本地化显示。


![](https://www.runoob.com/wp-content/uploads/2025/03/174728b890ea4f90be5e161686237b87tplv-10qhjjqwgv-quality_q75-scaled.webp)


第三步：迁移现有配置（可选）****如果你之前使用 VS Code 或 Cursor，可以点击「从 VS Code 导入」或「从 Cursor 导入」，Trae 会自动同步：


- 已安装的插件
- IDE 设置与偏好
- 快捷键绑定

![](https://www.runoob.com/wp-content/uploads/2025/03/c6bb117726d740ccba115c49779332a3tplv-10qhjjqwgv-quality_q75.webp)


这让你几乎无缝地从原有工具切换到 Trae，学习成本极低。


第四步：安装命令行工具（推荐）****点击「安装 `trae` 命令」并完成授权后，你可以在终端使用以下命令：


```
# 快速唤起 Trae
trae

# 在 Trae 中打开指定项目
trae my-react-app
```


![](https://www.runoob.com/wp-content/uploads/2025/03/e5590494264a4c77931cbf679b36ba3ftplv-10qhjjqwgv-quality_q75-scaled.webp)


第五步：登录账号****使用手机号或稀土掘金账号登录。完成登录后，才可以在 Trae 中使用 AI 服务。

![](https://www.runoob.com/wp-content/uploads/2025/03/952f011bda5b44acbf1fa94c68a1f3ebtplv-goo7wpa0wc-quality_q75.webp)


---


## 界面布局


Trae 的界面与 VS Code 高度相似，主要分为以下几个区域：


```
┌─────────────────────────────────────────────┐
│  菜单栏（文件 / 编辑 / 视图 / 帮助…）            │
├──────┬──────────────────────┬───────────────┤
│      │                      │               │
│ 侧边栏│    代码编辑区          │  AI 助手面板  │
│      │                      │               │
│（文件 │                      │（Chat / Builder│
│ 资源  │                      │  对话界面）    │
│ 管理器│                      │               │
│ 等）  │                      │               │
├──────┴──────────────────────┴───────────────┤
│  终端（底部面板）                               │
└─────────────────────────────────────────────┘
```


![](https://www.runoob.com/wp-content/uploads/2026/03/2ac3816f-57e9-4b11-9cc2-6c9051e30dca.png)


- **侧边栏**：文件资源管理器、搜索、版本控制、插件市场等
- **代码编辑区**：主要的代码书写区域，支持语法高亮、多文件标签
- **AI 助手面板**：右侧的 AI 交互区域，支持 Chat 和 Builder 两种模式
- **终端面板**：底部集成终端，可直接运行命令


---


## 打开与管理项目


### 打开已有项目


有以下几种方式：


- 菜单栏选择「文件」→「打开文件夹」，选择本地项目目录
- 在终端执行 `**trae 项目路径**` 直接打开
- 从欢迎页面选择「最近打开的项目」


终端使用唤起 Trae 使用以下命令：


```
trae
```


使用 Trae 打开当前目录命令：


```
trae .
```


指定目录路径使用以下命令：


```
trae ~/runoob-test     # 打开指定目录的项目
```


### 克隆 Git 仓库


在欢迎页点击「克隆 Git 仓库」，输入仓库地址即可将远程项目拉取到本地并自动打开。


### 新建文件与项目


- 右键文件资源管理器中的文件夹 → 「新建文件」，Trae 会根据文件扩展名自动识别类型
- 菜单栏「文件」→「新建项目」，可选择空白项目或通过 Builder 模式用 AI 生成


---


## 使用 AI 助手


这是 Trae 最核心的功能，提供两种模式：


![](https://www.runoob.com/wp-content/uploads/2026/03/f43dd8ab-ceca-41e1-9b21-95ab176fc148.png)


### Chat 模式（智能问答）


Chat 模式适合在开发过程中随时提问，是一个了解当前代码的"智能搭档"。


常见用法：**


- 解释某段代码的作用
- 查找 Bug 并给出修复方案
- 询问某个 API 的用法
- 让 AI 帮你优化代码逻辑


**如何使用上下文：**


与 AI 对话时，可以指定代码、文件、文件夹作为上下文，让 AI 的回答更加精准。例如，在 Chat 输入框中使用 `@文件名` 来引用具体文件。


### Builder 模式（项目构建）


Builder 模式适合从零开始构建一个项目。你只需用自然语言描述想要什么应用，AI 会自动调用工具、分析需求、生成文件并执行命令。


**使用示例：**


```
请帮我创建一个 React 待办事项应用，支持添加、删除和标记完成功能
```


![](https://www.runoob.com/wp-content/uploads/2026/03/75d2f0b2-6e5c-49e3-be3a-3b89ca7706c5.png)


Builder 模式会自动：


- 创建项目目录结构
- 生成所有必要的代码文件
- 安装依赖包
- 运行项目进行预览

**

注意（Windows 用户）**：使用 Builder 模式需要配置 PowerShell 6 或更高版本。可在「设置」→ 终端配置文件中选择带有 `\PowerShell\{版本号}\` 字样的配置。


### 处理 AI 生成的代码变更


AI 生成代码后，你可以选择接受或拒绝：


| 操作 | macOS 快捷键 | Windows 快捷键 |
| --- | --- | --- |
| 接受当前文件所有变更 | Command + Enter | Ctrl + Enter |
| 拒绝当前文件所有变更 | Command + Backspace | Ctrl + Backspace |
| 批量接受全部变更 | 点击输入框上方「全部接受」按钮 | 同左 |
| 批量拒绝全部变更 | 点击输入框上方「全部拒绝」按钮 | 同左 |


### 内嵌对话（Inline Chat）


除了侧边 AI 面板，你还可以在编辑器内直接唤起 AI：


- **快捷键**：`Command + I`（macOS）/ `Ctrl + I`（Windows）
- 选中一段代码后按快捷键，可对选中内容直接提问或要求修改
- 当代码出现报错时，也可以点击错误提示旁的「AI 修复」按钮，让 AI 自动分析并修复


---


## 代码补全


Trae 内置 AI 代码补全功能，在你书写代码时会实时给出建议。无需额外配置，打开项目后即可使用：


- 当 AI 给出补全建议时，按 `Tab` 键接受
- 按 `Esc` 键忽略建议
- 补全范围涵盖单行代码、整个函数体甚至跨文件的逻辑


![](https://www.runoob.com/wp-content/uploads/2026/03/7e80f772-7f45-4dd1-ab78-b5a63836ee3c.png)


---


## 插件管理


Trae 兼容 VS Code 插件生态，安装插件的方法：


- 点击左侧侧边栏的「插件」图标（或按 `Ctrl+Shift+X`）
- 在搜索框中输入插件名称，点击「安装」即可
- 如果已从 VS Code 导入配置，原有插件会自动同步，无需重新安装


![](https://www.runoob.com/wp-content/uploads/2026/03/80cb02ba-e03d-4352-b3f5-0341636d6c49.png)


---


## 版本控制


Trae 内置 Git 集成，侧边栏的「源代码管理」面板提供可视化的版本控制操作：


- 查看文件变更、暂存文件
- 提交代码、推送/拉取远程仓库
- 查看提交历史和 Diff 对比


对于习惯命令行的开发者，底部的集成终端同样可以直接运行 Git 命令。


---


##







	  AI 思考中...





			** [Qoder Quest 模式](https://www.runoob.com/qoder-quest-mode.html)
			[Token (词元)](https://www.runoob.com/token-intro.html) **













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