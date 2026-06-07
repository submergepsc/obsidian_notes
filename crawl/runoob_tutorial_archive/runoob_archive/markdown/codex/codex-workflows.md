# Codex 工作流模式

- Source: https://www.runoob.com/codex/codex-workflows.html

Codex 可以融入各种开发工作流，从日常编码到复杂重构，都能显著提升效率。


---


## 日常开发工作流


日常开发是最常见的工作流模式，适合构建新功能或小规模修改。


### 工作流步骤


| 步骤 | 操作 | Codex 交互 |
| --- | --- | --- |
| 1 | 明确需求 | 描述你想要实现的功能 |
| 2 | Codex 分析 | Codex 理解项目结构和规范 |
| 3 | 方案讨论 | 与 Codex 确认实现方案 |
| 4 | 代码生成 | Codex 编写代码并修改文件 |
| 5 | 验证测试 | 运行测试确认功能正确 |
| 6 | 迭代优化 | 根据反馈调整代码 |


### 示例：添加新 API 端点


## 日常开发流程


```
# 步骤 1：描述需求
"在 /api/users 路径添加一个 GET 端点，返回用户列表，
支持分页参数 page 和 limit"

# 步骤 2-3：Codex 分析并确认方案
Codex 会分析现有 API 结构，确认：
- 路由定义位置
- 数据库查询方式
- 响应格式规范

# 步骤 4：代码生成
Codex 自动创建：
- 路由定义
- 数据查询逻辑
- 错误处理
- 响应格式化

# 步骤 5：验证测试
"运行测试并检查新端点"

# 步骤 6：迭代优化
"添加缓存支持，响应时间应小于 100ms"
```


---


## 代码理解工作流


当你需要理解遗留代码或陌生项目时，使用这个工作流。


### 探索式工作流


- 从入口点开始，让 Codex 解释整体架构
- 逐步深入关键模块，理解核心逻辑
- 追踪数据流和调用链
- 总结关键点和注意事项


## 理解遗留项目


```
# 整体架构
"分析这个项目的整体架构，解释主要模块和它们的关系"

# 核心模块
"解释 src/auth 模块的工作原理，包括认证流程和权限检查"

# 数据流追踪
"追踪用户登录后从请求到响应的完整流程"

# 关键总结
"总结这个项目的核心设计模式和需要注意的地方"
```


### 快速上手新项目


## 新项目上手指南


```
# 项目概览
"这是什么项目？它的主要功能和技术栈是什么？"

# 开发指南
"如何本地启动开发环境？如何运行测试？"

# 代码规范
"这个项目的代码规范是什么？有什么约定？"

# 模块导航
"如果要添加 X 功能，应该修改哪些文件？"
```


---


## 重构工作流


重构需要谨慎处理，Codex 可以帮助你系统性地改进代码结构。


### 重构原则


- 先理解现有代码结构
- 小步重构，逐步改进
- 每步验证，确保功能不变
- 保持测试覆盖


### 重构工作流步骤


| 步骤 | 说明 |
| --- | --- |
| 识别问题 | Codex 分析代码，识别需要改进的部分 |
| 制定方案 | 讨论重构方案，确认改进方向 |
| 分步执行 | 小规模修改，每次修改后验证 |
| 测试验证 | 运行全部测试确保功能正确 |
| 清理优化 | 删除冗余代码，优化命名 |


## 重构示例


```
# 识别问题
"分析 src/utils 模块，识别代码重复和不合理的设计"

# 制定方案
"讨论如何重构这个模块，保持向后兼容"

# 分步执行
"第一步：提取公共函数到 utils/common.py"

# 测试验证
"运行所有测试，确认重构没有破坏功能"

# 继续下一步
"第二步：简化复杂的函数，拆分成更小的单元"
```


**
重构时使用 /plan 模式先制定计划，然后分步执行，避免一次性大改动。


---


## Bug 修复工作流


Codex 可以帮助你快速定位和修复 Bug。


### 修复流程


| 步骤 | 操作 |
| --- | --- |
| 描述问题 | 说明 Bug 的表现和触发条件 |
| 提供信息 | 分享错误信息、日志、截图 |
| 定位根因 | Codex 分析并找到根本原因 |
| 生成修复 | Codex 提出修复方案 |
| 验证修复 | 运行测试确认问题解决 |
| 防止复发 | 添加测试覆盖该场景 |


## Bug 修复示例


```
# 描述问题
"用户登录时偶尔出现 500 错误，错误日志显示：
TypeError: Cannot read property 'id' of undefined"

# 提供信息
"这是完整的错误堆栈：[粘贴堆栈信息]"

# 定位根因
Codex 分析后发现问题：用户对象在某些情况下为 null

# 生成修复
"修复这个问题，并确保不会影响正常登录流程"

# 验证修复
"运行登录相关的所有测试"

# 防止复发
"添加一个测试覆盖用户对象为 null 的场景"
```


### 截图辅助调试


使用截图帮助 Codex 理解问题：


## 图片输入


```
# CLI 中附加截图
codex -i error-screenshot.png "解释这个错误并修复"

# IDE 中粘贴截图
直接在对话中粘贴截图，描述问题
```


---


## 代码审查工作流


Codex 可以审查代码变更，发现问题并提供改进建议。


### 审查模式


| 模式 | 触发方式 | 适用场景 |
| --- | --- | --- |
| Review Mode | App 中启用 | 审查本地未提交变更 |
| /review 命令 | CLI/IDE 中使用 | 审查指定范围变更 |
| GitHub 集成 | PR 中 @codex review | 审查 Pull Request |


### 本地审查


## Review Mode


```
# App 中启用 Review Mode
点击工具栏的眼睛图标

# 或在 CLI 中使用
/review

# 指定审查范围
/review src/auth/

# 审查特定提交
/review HEAD~3..HEAD
```


### 审查重点定制


## 指定审查重点


```
# 安全审查
/review for security issues

# 性能审查
/review for performance regressions

# 代码风格
/review for code style consistency

# 综合审查
/review --detailed
```


---


## 测试编写工作流 Codex 可以帮助你编写和维护测试代码。 ### 新功能测试 编写测试


```
# 为新功能编写测试
"为 src/api/users.py 的 GET 端点编写单元测试，
覆盖正常响应、空列表、分页边界等场景"

# 验证测试
"运行新编写的测试"

# 补充覆盖
"检查测试覆盖率，补充未覆盖的边界情况"
```


### 测试修复


## 修复失败测试


```
# 分析失败测试
"测试 test_user_login 失败了，分析原因并修复"

# 批量修复
"运行所有测试，修复失败的测试"
```


---


## 文档生成工作流


Codex 可以帮助生成和更新文档。


### 生成文档


## 文档生成


```
# API 文档
"为 src/api 模块生成 API 文档，包括每个端点的请求格式和响应格式"

# README 更新
"更新 README.md，添加新功能的说明和使用示例"

# 内联注释
"为复杂的函数添加注释，解释关键逻辑"
```


---


## 最佳实践


### 工作流选择


- 日常开发：持续交互，逐步完善
- 重构：先规划后执行，小步验证
- Bug 修复：提供充分信息，验证根因
- 审查：定期进行，关注安全问题


### 效率技巧


- 使用 AGENTS.md 定义项目规范，减少重复说明
- 利用 Skills 封装常用工作流
- 使用 Worktree 隔离不同任务
- 配置合理的 Approval 策略


---


## 常见问题


### Q: 如何处理大型重构？


使用 /plan 模式制定分步计划，每步完成后验证。


### Q: Bug 修复后如何防止复发？


添加专门的测试覆盖该场景，并在 AGENTS.md 中添加相关检查规则。


### Q: 如何让 Codex 理解项目规范？


创建 AGENTS.md 文件，定义项目的技术栈、代码规范、测试要求等。


### Q: 审查结果如何与团队共享？


使用 GitHub 集成在 PR 中审查，结果会自动添加为评论。








	  AI 思考中...





			** [Codex 自动化与 CI/CD](https://www.runoob.com/codex-automation.html)
			[Codex 提示词最佳实践](https://www.runoob.com/codex-prompting.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#b5d4d1d8dcdbf5c7c0dbdadad79bd6dad8)

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