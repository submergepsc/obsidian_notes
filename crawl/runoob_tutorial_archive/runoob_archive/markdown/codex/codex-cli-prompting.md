# Codex CLI 提示词技巧

- Source: https://www.runoob.com/codex/codex-cli-prompting.html

掌握有效的提示词技巧是充分利用 Codex CLI 的关键。本节详细介绍如何编写高效的提示词来获得最佳结果。


---


## 提示词基础


你通过发送提示词（prompt）与 Codex 交互，描述你想要它完成的任务。


### 基本示例


## 基础提示词


```
# 解释代码功能
"Explain how the transform module works and how other modules use it."

# 添加新功能
"Add a new command-line option `--json` that outputs JSON."

# 修复 bug
"Fix the error in the login function"
```


### 提示词工作原理


当你提交提示词时，Codex 按以下循环工作：


![Codex 提示词工作流程](https://www.runoob.com/wp-content/uploads/2026/04/prompting-flow.svg)
图：Codex 提示词工作流程


- 调用语言模型
- 执行模型输出指示的操作（读取文件、编辑文件、运行工具等）
- 重复直到任务完成或你取消


**理解这个循环有助于你更好地设计提示词，因为 Codex 会在每个步骤中基于上下文做出决策。


---


## 编写有效提示词的技巧


### 技巧 1：包含验证步骤


Codex 在能够验证工作时会产生更高质量的输出。包含验证步骤可以帮助 Codex 确保正确性：


## 包含验证的提示词


```
# 不推荐
"Write a function to sort a list"

# 推荐 - 包含验证
"Write a function to sort a list. Include test cases to verify it handles empty lists, already-sorted lists, reverse-sorted lists, and lists with duplicates. Run the tests to confirm they pass."
```


### 技巧 2：将复杂任务拆分为小步骤


Codex 处理较小的、专注的任务时表现更好。小任务更容易测试和审查：


## 拆分任务


```
# 不推荐 - 任务太大
"Create a complete user authentication system with login, registration, password reset, and OAuth"

# 推荐 - 拆分为小步骤
"Step 1: Create a user model with email and password fields
Step 2: Add a registration endpoint
Step 3: Add a login endpoint with JWT
Step 4: Add password reset functionality
Let me know when Step 1 is done before moving to Step 2"
```


### 技巧 3：提供上下文


提供 Codex 可以使用的上下文，如相关文件和图像的引用：


## 提供上下文


```
# 不推荐
"Fix this bug"

# 推荐 - 包含详细信息
"Fix the bug in src/auth.py where users can't log in with special characters in their password. I've attached a screenshot of the error message and the relevant code section."
```


### 技巧 4：明确输出格式


告诉 Codex 你期望的输出格式：


## 指定输出格式


```
# 指定代码风格
"Write a function to calculate Fibonacci numbers. Use TypeScript, include JSDoc comments, and follow functional programming principles."

# 指定输出结构
"Explain the codebase structure. Organize your answer with: 1) Overview 2) Key directories 3) Main entry points"
```


> 越具体的提示词通常会产生越好的结果。Codex 擅长理解意图，但你提供的信息越多，它的表现越好。


---


## 线程（Threads）


线程是单个会话：你的提示词加上后续的模型输出和工具调用。一个线程可以包含多个提示词。


### 本地线程 vs 云端线程


| 类型 | 说明 | 优势 |
| --- | --- | --- |
| 本地线程 | 在你的机器上运行 | 可以读写文件、使用现有工具 |
| 云端线程 | 在隔离环境中运行 | 并行运行、从其他设备委派任务 |


### 恢复会话


## 恢复之前的会话


```
# 打开会话选择器
codex resume

# 直接跳转到最近会话
codex resume --last

# 恢复指定会话
codex resume <SESSION_ID>
```


### 会话管理


运行中的线程可以并行，但避免两个线程同时修改同一文件。你也可以稍后通过继续另一个提示词来恢复线程。


---


## 上下文管理


当你提交提示词时，包含 Codex 可以使用的上下文，例如对相关文件和图像的引用。IDE 扩展会自动将打开的文件列表和选中的文本范围作为上下文。


### 上下文窗口


线程中的所有信息必须适合模型的上下文窗口。Codex 会监控并报告剩余空间。


### 自动压缩


对于较长的任务，Codex 可能会自动压缩上下文，通过总结相关信息并丢弃不太相关的细节。Codex 可以在多个步骤中继续处理复杂任务。


### 手动管理上下文


你可以通过以下方式帮助 Codex 管理上下文：


- 专注于当前任务
- 避免在一个提示词中混合多个独立任务
- 定期开始新会话（使用 `/new`）


> 当 Codex 报告上下文使用量较高时，考虑开始一个新的会话或减少历史消息。


---


## 高级提示技巧


### 使用计划模式


对于复杂任务，使用计划模式让 Codex 先规划再执行：


## 计划模式


```
# 使用 /plan 命令
/plan 实现用户认证系统

# 或者在提示词中包含 "plan"
"Plan and implement a REST API with CRUD operations for a blog"
```


### 使用审查模式


请求 Codex 审查代码而非直接修改：


## 审查模式


```
# 使用 /review 命令
/review src/auth.py

# 或者描述审查需求
"Review this code for potential security vulnerabilities and suggest improvements"
```


### 限制修改范围


明确告诉 Codex 可以修改什么：


## 限制修改范围


```
# 只读模式
"Explain what this function does, don't make any changes"

# 限定文件范围
"Add logging only to the auth module, don't touch other files"

# 逐步确认
"Let me know the proposed changes before you make them"
```


---


## 提示词模板


以下是一些常用的提示词模板：


### 代码生成


```
Write a [语言] function that [功能描述].
Requirements:
- [需求1]
- [需求2]
Include:
- 详细的文档注释
- 错误处理
- 测试用例
```


### 代码审查


```
Review the [文件/模块] for:
- Potential bugs
- Security issues
- Performance problems
- Code style violations

Provide:
- Issue list with severity
- Suggested fixes
- Overall quality score (1-10)
```


### Bug 修复


```
Fix the bug in [文件:行号/函数名].
Error: [错误信息]
Expected behavior: [期望行为]
Steps to reproduce: [复现步骤]
```


### 重构


```
Refactor [文件/函数] to [目标].
Current issues:
- [问题1]
- [问题2]

Constraints:
- 保持功能不变
- 不要改变 API 接口
- 添加单元测试
```


> 熟能生巧。多练习编写提示词，你会逐渐掌握如何获得最佳结果。


---


## 常见问题


### Q: Codex 没有理解我的提示词怎么办？


尝试：1) 更具体地描述 2) 提供更多上下文 3) 分解为更小的步骤 4) 使用示例说明期望的输出


### Q: 提示词应该用英文还是中文？


Codex 支持多语言，但英文通常效果最好。如果你用中文描述，确保描述足够详细和明确。


### Q: 如何让 Codex 只分析而不修改代码？


明确告诉它 "只读" 或 "don't make any changes"，它就会只提供分析而不修改。


### Q: 上下文窗口满了怎么办？


开始一个新的会话（使用 /new），或者让 Codex 压缩历史记录（它会自动处理）。








	  AI 思考中...





			** [Codex CLI 实用示例](https://www.runoob.com/codex-examples.html)
			[Codex 子代理（Subagents）](https://www.runoob.com/codex-subagents.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#dbbabfb6b2b59ba9aeb5b4b4b9f5b8b4b6)

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