# Codex IDE 扩展

- Source: https://www.runoob.com/codex/codex-ide.html

Codex IDE 扩展让你在熟悉的开发环境中直接使用 Codex，无缝融入日常编码工作流。


---


## 支持的 IDE


Codex 官方支持以下 IDE：


| IDE | 扩展 ID | 安装方式 |
| --- | --- | --- |
| VS Code | openai.chatgpt | vscode:extension/openai.chatgpt |
| VS Code Insiders | openai.chatgpt | 扩展市场 |
| Cursor | openai.chatgpt | cursor:extension/openai.chatgpt |
| Windsurf | openai.chatgpt | windsurf:extension/openai.chatgpt |


---


## 安装扩展


### VS Code 安装


## VS Code 安装


```
# 方法一：命令行安装
code --install-extension openai.chatgpt

# 方法二：在 VS Code 中
# 1. 打开扩展面板 (Cmd+Shift+X)
# 2. 搜索 "Codex" 或 "ChatGPT"
# 3. 点击安装
```


### Cursor 安装


## Cursor 安装


```
# 方法一：命令行
cursor --install-extension openai.chatgpt

# 方法二：在 Cursor 中
# 1. 打开扩展面板
# 2. 搜索 "Codex"
# 3. 点击安装
```


**
安装后需要使用 ChatGPT 账号或 OpenAI API Key 登录才能使用。


---


## 核心功能


### 自动上下文


IDE 扩展自动将以下内容作为上下文传递给 Codex：


- 当前打开的文件列表
- 编辑器中选中的文本范围
- 当前工作目录信息


### AI 对话


在 IDE 中直接与 Codex 对话：


- 打开 Codex 面板（快捷键或侧边栏）
- 输入问题或任务描述
- Codex 分析当前文件和项目后回复


### 代码操作


选中代码后右键可执行：


| 操作 | 功能 |
| --- | --- |
| 解释 | Codex 解释选中代码的功能 |
| 重写 | 按需求重写选中代码 |
| 审查 | 检查代码问题和改进建议 |
| 生成测试 | 为选中代码生成单元测试 |


---


## 斜杠命令


在 Codex 面板中使用斜杠命令：


| 命令 | 功能 |
| --- | --- |
| /explain | 解释选中代码 |
| /fix | 修复选中代码的问题 |
| /test | 为选中代码生成测试 |
| /review | 审查选中代码 |
| /plan | 先规划再执行 |


## 斜杠命令示例


```
# 解释代码
/explain

# 修复 Bug
/fix this function throws error for null input

# 规划新功能
/plan implement user authentication with JWT
```


---


## 模型选择


在输入框下方可以切换模型：


| 模型 | 特点 |
| --- | --- |
| GPT-5.4 | 旗舰模型，适合复杂任务 |
| GPT-5.4-mini | 轻量快速，适合简单任务 |
| GPT-5.3-Codex | 专业编码模型 |


---


## 快捷键


| 快捷键 | 功能 |
| --- | --- |
| Cmd+Shift+C | 打开 Codex 面板 |
| Cmd+Shift+Enter | 代码补全 |
| Cmd+Shift+R | 重写选中代码 |
| Cmd+Shift+E | 解释选中代码 |


> 快捷键可在 IDE 设置中自定义，避免与其他扩展冲突。


---


## 云端任务委派


从 IDE 扩展启动云端任务：


- 选择 Cloud 模式创建线程
- 任务在云端隔离环境运行
- 完成后通过通知或 PR 查看结果


### 适用场景


- 需要并行处理多个任务
- 从低配置设备委派大型任务
- 跨设备协同工作


---


## IDE 配置


### 设置文件打开方式


## 配置文件打开


```
# ~/.codex/config.toml

# 指定打开文件的编辑器
file_opener = "vscode"
# 可选值: vscode, vscode-insiders, windsurf, cursor, none
```


### 设置默认模型


## 配置默认模型


```
# ~/.codex/config.toml

model = "gpt-5.4"
```


---


## 使用技巧


### 选择代码作为上下文


选中代码后，Codex 自动将其作为上下文。


选中的代码越多，Codex 的回复越准确。


### 多文件操作


打开多个文件时，Codex 可以同时处理。


在面板中描述需要修改的文件即可。


### 使用内置终端


IDE 内置终端可以直接运行 Codex CLI。


这样可以享受 CLI 的完整功能。


---


## 常见问题


### Q: 扩展无法连接？


确保已登录 Codex 账号，检查网络连接和代理设置。


### Q: 快捷键与其他扩展冲突？


在 IDE 设置中搜索 "Codex"，自定义快捷键。


### Q: 如何更新扩展？


扩展随 Codex 自动更新，或在 IDE 扩展面板手动更新。


### Q: IDE 扩展与 App 的区别？


IDE 扩展深度集成开发环境，自动读取文件上下文；App 提供完整功能和多项目管理。








	  AI 思考中...





			** [Codex 桌面应用](https://www.runoob.com/codex-app.html)
			[Codex 命令行工具](https://www.runoob.com/codex-cli.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#ea8b8e878384aa989f84858588c4898587)

      : · [免责声明](https://www.runoob.com/disclaimer)

      : · [关于我们](https://www.runoob.com/aboutus)

      : · [文章归档](https://www.runoob.com/archives)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/)**
    **[runoob.com](https://www.runoob.com/)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **