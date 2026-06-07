# Claude Code 环境变量

- Source: https://www.runoob.com/claude-code/claude-code-env.html

环境变量是控制 Claude Code 行为的重要方式，无需编辑配置文件即可灵活调整各项设置。本章详细介绍 Claude Code 支持的所有环境变量、它们的用途、配置方式以及常见使用场景。


---


## 环境变量概述


Claude Code 使用环境变量来控制行为，这些变量可以通过以下方式设置：


- 直接在 shell 中 `export`
- 在 `~/.claude/settings.json` 的 `env` 字段中配置
- 在项目级 `.claude/settings.json` 中配置
- 通过 IDE 插件的设置界面配置


**
环境变量优先级从高到低：命令行 > 项目级 settings.json > 用户级 settings.json > shell 环境变量。在 settings.json 中配置的变量会自动传递给 Claude 进程。


---


## 认证相关变量


| 变量名 | 说明 | 值 |
| --- | --- | --- |
| ANTHROPIC_API_KEY | Claude API 密钥（从 claude.ai 获取） | API 密钥字符串 |
| ANTHROPIC_BASE_URL | API 请求的目标地址（用于代理或自定义端点） | URL 地址 |
| ANTHROPIC_AUTH_TOKEN | 认证令牌（用于 VS Code 插件等场景） | 令牌字符串 |


### 配置示例


## 实例


```
# 在 shell 中设置
export ANTHROPIC_API_KEY="sk-ant-xxxxx"
export ANTHROPIC_BASE_URL="https://api.anthropic.com"
```


## 实例


```
// 在 settings.json 中配置
{
  "env": {
    "ANTHROPIC_API_KEY": "sk-ant-xxxxx",
    "ANTHROPIC_BASE_URL": "https://custom-proxy.com/v1"
  }
}
```


---


## 模型配置变量


| 变量名 | 说明 | 值 |
| --- | --- | --- |
| ANTHROPIC_MODEL | 默认使用的模型 | claude-opus-4-5、claude-sonnet-4-5、claude-haiku-3-5 等 |
| ANTHROPIC_SMALL_FAST_MODEL | 快速响应模式使用的模型（用于简单任务） | 模型名称 |
| CLAUDE_CODE_SUBAGENT_MODEL | 统一设置所有子代理使用的模型 | 模型名称 |
| CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS | 使用 Bedrock 或 Vertex 的 Anthropic Messages 格式时禁用实验性功能 | 1 |


### 使用场景


子代理默认继承主对话的模型。通过 `CLAUDE_CODE_SUBAGENT_MODEL` 可以统一设置，将简单任务交给 Haiku，将复杂分析交给 Sonnet，从而优化成本：


## 实例


```
# 主对话用 Opus 做复杂推理，子代理统一用 Sonnet
export ANTHROPIC_MODEL="claude-opus-4-5"
export CLAUDE_CODE_SUBAGENT_MODEL="claude-sonnet-4-5"
```


---


## 工具与命令变量


| 变量名 | 说明 | 值 |
| --- | --- | --- |
| CLAUDE_CODE_DISABLE_SLASH_COMMANDS | 禁用所有斜杠命令 | 1 |
| CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS | 禁用内置的 Git 相关系统提示词（优先级高于 settings.json 中的 includeGitInstructions） | 1 |
| CLAUDE_CODE_USE_POWERSHELL_TOOL | 在 Windows 上启用 PowerShell 工具（需要配合 defaultShell: "powershell" 设置） | 1 |
| CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL | 跳过自动安装 IDE 扩展（替代 autoInstallIdeExtension 设置） | 1 |
| CLAUDE_CODE_DISABLE_BACKGROUND_TASKS | 禁用后台任务功能 | 1 |


---


## 权限与安全变量


| 变量名 | 说明 | 值 |
| --- | --- | --- |
| CLAUDE_CODE_PERMISSION_MODE | 设置默认权限模式（详见子代理章节） | default、acceptEdits、dontAsk、bypassPermissions、plan |
| CLAUDE_CODE_ALLOWED_TOOLS | 允许 Claude 使用的工具白名单（逗号分隔） | 工具列表 |
| CLAUDE_CODE_DISALLOWED_TOOLS | 禁止 Claude 使用的工具黑名单 | 工具列表 |


### 权限模式详解


- `default`：正常权限提示，每次操作前询问
- `acceptEdits`：自动接受文件编辑，无需确认
- `dontAsk`：自动拒绝未授权操作，不中断执行
- `bypassPermissions`：跳过所有权限检查（仅限完全可信环境）
- `plan`：只读规划模式，不执行写操作


## 实例


```
# 在 CI 环境中使用只读模式
export CLAUDE_CODE_PERMISSION_MODE="plan"
export CLAUDE_CODE_ALLOWED_TOOLS="Read,Grep,Glob,Bash(gh *)"
```


---


## 日志与调试变量


| 变量名 | 说明 | 值 |
| --- | --- | --- |
| CLAUDE_CODE_DEBUG | 启用调试输出 | 1 |
| CLAUDE_CODE_ENABLE_TELEMETRY | 启用遥测数据收集 | 1 |
| OTEL_METRICS_EXPORTER | OpenTelemetry 指标导出器 | otlp 等 |


---


## 会话与历史变量


| 变量名 | 说明 | 值 |
| --- | --- | --- |
| CLAUDE_CODE_DISABLE_HISTORY | 禁用对话历史保存 | 1 |
| CLAUDE_CODE_SESSION_TIMEOUT | 会话超时时间（秒） | 数字 |
| CLAUDE_CODE_MAX_SESSIONS | 最大保存的会话数量 | 数字 |


---


## MCP 相关变量


当 Claude Code 执行 MCP 工具时，会设置以下环境变量：


| 变量名 | 说明 | 值 |
| --- | --- | --- |
| CLAUDE_CODE_MCP_SERVER_NAME | MCP 服务器名称 | 字符串 |
| CLAUDE_CODE_MCP_TOOL_NAME | 正在调用的 MCP 工具名称 | 字符串 |
| CLAUDE_CODE_MCP_TOOL_ARGS | 传递给 MCP 工具的参数 | JSON 字符串 |


---


## 工作流相关变量


| 变量名 | 说明 | 值 |
| --- | --- | --- |
| CLAUDE_CODE_WORKTREE_CLEANUP_PERIOD_DAYS | 孤立 worktree 的自动清理周期 | 天数 |
| CLAUDE_CODE_DISABLE_WORKTREE_AUTO_CLEANUP | 禁用 worktree 自动清理 | 1 |


---


## GitHub Actions 专用变量


| 变量名 | 说明 | 值 |
| --- | --- | --- |
| ANTHROPIC_VERTEX_PROJECT_ID | Vertex AI 项目 ID（使用 Vertex 时由认证步骤设置） | GCP 项目 ID |
| CLOUD_ML_REGION | Vertex AI 区域 | 区域代码（如 us-east5） |


---


## settings.json 配置方式


所有环境变量都可以在 `settings.json` 中配置，这种方式更加声明式和可移植：


## 实例


```
{
  "env": {
    "ANTHROPIC_MODEL": "claude-sonnet-4-5",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claude-haiku-3-5",
    "CLAUDE_CODE_PERMISSION_MODE": "plan",
    "CLAUDE_CODE_ALLOWED_TOOLS": "Read,Grep,Glob,Bash",
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp"
  }
}
```


### VS Code 插件配置


在 VS Code 中使用 Claude Code 插件时，可以通过 `environmentVariables` 设置：


## 实例


```
{
  "claudeCode.environmentVariables": [
    {
      "name": "ANTHROPIC_BASE_URL",
      "value": "https://custom-proxy.com/api"
    },
    {
      "name": "ANTHROPIC_AUTH_TOKEN",
      "value": "your-token-here"
    },
    {
      "name": "ANTHROPIC_MODEL",
      "value": "claude-sonnet-4-5"
    }
  ]
}
```


---


## 常见使用场景


### 场景一：使用代理或自定义 API 端点


## 实例


```
# 通过企业内部代理访问 Claude API
export ANTHROPIC_BASE_URL="https://proxy.company.com/anthropic/v1"
export ANTHROPIC_API_KEY="your-api-key"
```


### 场景二：优化成本配置


## 实例


```
# 主对话用 Sonnet，子代理统一用 Haiku
export ANTHROPIC_MODEL="claude-sonnet-4-5"
export CLAUDE_CODE_SUBAGENT_MODEL="claude-haiku-3-5"
```


### 场景三：CI/CD 环境安全配置


## 实例


```
# CI 环境中使用只读模式
export CLAUDE_CODE_PERMISSION_MODE="plan"
export CLAUDE_CODE_DISABLE_HISTORY="1"
export CLAUDE_CODE_ALLOWED_TOOLS="Read,Grep,Glob,Bash(gh *)"
```


### 场景四：Windows PowerShell 环境


## 实例


```
# Windows 上启用 PowerShell
$env:CLAUDE_CODE_USE_POWERSHELL_TOOL = "1"
# 在 settings.json 中设置 defaultShell
```


---


## 优先级与覆盖


环境变量的优先级（从高到低）：


- 命令行 `export` 设置
- 项目级 `.claude/settings.json`
- 用户级 `~/.claude/settings.json`
- Claude Code 默认值


> 在 `settings.json` 中配置的变量会覆盖同名的 shell 环境变量。这是因为 settings.json 在 Claude Code 进程启动时被显式读取，优先级更高。


---


## 查看当前配置


使用 `/config` 命令可以查看当前的完整配置：


```
/config
```


这会显示所有当前生效的设置，包括环境变量和 settings.json 中的配置。


---


## 最佳实践


### 1、敏感信息处理


- API 密钥等敏感信息不要硬编码在 settings.json 中
- 使用环境变量或 shell 配置文件（`~/.bashrc`、`~/.zshrc`）
- 确保包含敏感信息的文件不在 git 版本控制中


### 2、按环境配置


- 本地开发：使用更宽松的权限模式
- CI/CD：使用只读模式 `plan`
- 生产调试：启用 `CLAUDE_CODE_DEBUG`


### 3、集中管理


- 通用配置放在 `~/.claude/settings.json`
- 项目特有配置放在项目目录的 `.claude/settings.json`
- 敏感配置通过 shell 环境变量或 CI Secrets 提供


---


## 常见问题


Q：环境变量和 settings.json 哪个优先？**


在 settings.json 中配置的变量优先级更高，会覆盖同名的 shell 环境变量。


**Q：如何让 Claude Code 使用不同的 API 端点？**


设置 `ANTHROPIC_BASE_URL` 环境变量指向你的代理或自定义端点。


**Q：子代理如何控制使用的模型？**


可以通过 `CLAUDE_CODE_SUBAGENT_MODEL` 统一设置所有子代理的模型，也可以在每个子代理的 frontmatter 中单独指定。


**Q：在 Windows 上如何启用 PowerShell？**


设置环境变量 `CLAUDE_CODE_USE_POWERSHELL_TOOL=1`，同时在 settings.json 中设置 `defaultShell: "powershell"`。


**Q：如何禁用所有斜杠命令？**


设置 `CLAUDE_CODE_DISABLE_SLASH_COMMANDS=1` 环境变量。









	  AI 思考中...





			** [Claude Code 自定义斜杠命令](https://www.runoob.com/claude-code-custom-slash.html)
			[Claude Code Git 工作流](https://www.runoob.com/claude-code-git-workflow.html) **













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