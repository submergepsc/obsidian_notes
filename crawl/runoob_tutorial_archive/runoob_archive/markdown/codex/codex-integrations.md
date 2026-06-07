# Codex 集成与连接

- Source: https://www.runoob.com/codex/codex-integrations.html

Codex 支持与多种开发工具和平台集成，扩展其能力和应用场景。


---


## GitHub 集成


Codex 与 GitHub 深度集成，可以在 PR 中直接进行代码审查。


### 功能概览


| 功能 | 说明 |
| --- | --- |
| PR 审查 | 在 PR 评论中 @codex review 获取审查 |
| 自动审查 | 每个新 PR 自动触发审查 |
| CI 修复 | @codex fix the CI failures |
| 云端任务 | 其他 @codex 指令启动云端任务 |


### 设置 GitHub 集成


- 配置 Codex Cloud
- 前往设置页面开启 Code Review
- 授权访问你的 GitHub 仓库
- 选择要启用的仓库


### 请求审查


## PR 中使用


```
# 在 PR 评论中输入
@codex review

# 指定审查重点
@codex review for security issues

# 审查性能问题
@codex review for performance regressions
```


### Codex 响应


Codex 会：


- 对 PR 反应 👀
- 分析代码变更
- 发布审查意见
- 标记发现的问题（默认 P0 和 P1）


### 审查指南定制


在仓库的 AGENTS.md 中定义审查规则：


## 审查指南


```
## Review guidelines

- Don't log PII (个人身份信息)
- Verify authentication middleware wraps every route
- Check for SQL injection vulnerabilities
- Ensure error messages don't leak sensitive info
- Treat typos in docs as P1 issues
```


**
Codex 默认只标记 P0 和 P1 问题，可在 AGENTS.md 中调整。


---


## Slack 集成


通过 Slack 集成，团队成员可以在频道中直接使用 Codex。


### 设置 Slack 集成


- 前往 Codex 设置页面
- 找到 Integrations 部分
- 添加 Slack 应用
- 授权访问 Slack 工作区


### 使用方式


## Slack 中使用


```
# 在 Slack 频道中
@codex review this PR: https://github.com/xxx/pull/123

# 解释代码
@codex explain this function

# 下发任务
@codex fix the bug in auth module
```


### 适用场景


- 团队协作讨论时快速获取 AI 辅助
- 远程团队成员委派任务
- 异步工作场景


---


## Linear 集成


Linear 是项目管理工具，Codex 可以与之联动处理 Issue。


### 设置 Linear 集成


- 前往 Codex 设置页面
- 添加 Linear 集成
- 授权访问 Linear 工作区
- 配置 Issue 处理规则


### 使用场景


| 场景 | 说明 |
| --- | --- |
| Issue 处理 | 根据 Issue 自动创建代码修改 |
| 审查结果同步 | 将审查发现添加到 Issue |
| 状态更新 | 自动更新 Issue 状态 |
| 评论回复 | 在 Issue 评论中 @codex |


---


## MCP（Model Context Protocol）


MCP 是连接 Codex 与外部工具的协议。


### MCP 概述


- **STDIO 服务器**：本地进程，通过标准输入输出通信
- **HTTP 服务器**：远程服务器，通过 HTTP API 通信


### 配置 MCP 服务器


## MCP 配置


```
# ~/.codex/config.toml

# STDIO 服务器
[mcp_servers.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "./docs"]

# HTTP 服务器
[mcp_servers.api]
url = "https://api.example.com/mcp"
bearer_token_env_var = "API_TOKEN"
```


### 常用 MCP 服务器


| 服务器 | 功能 |
| --- | --- |
| filesystem | 文件系统访问 |
| github | GitHub API |
| postgres | PostgreSQL 数据库 |
| fetch | 网页抓取 |
| openai-docs | OpenAI 文档 |


### MCP 工具权限


## 工具权限配置


```
# 工具白名单
[mcp_servers.filesystem]
enabled_tools = ["read_file", "write_file"]

# 工具黑名单
disabled_tools = ["delete_file"]

# 工具审批模式
[mcp_servers.filesystem.tools.write_file]
approval_mode = "ask"  # ask | approve | deny
```


---


## OAuth 认证配置


某些 MCP 服务器需要 OAuth 认证：


## OAuth 配置


```
[mcp_servers.figma]
url = "https://api.figma.com/mcp"
scopes = ["file:read"]
oauth_resource = "codex-integration"

# OAuth 回调端口
mcp_oauth_callback_port = 8080

# 凭证存储
mcp_oauth_credentials_store = "keyring"
```


---


## 常见问题


### Q: GitHub 集成需要什么计划？


需要 Codex Cloud 订阅（Plus 或以上）。


### Q: 可以限制 Codex 访问的仓库吗？


可以在设置中选择性授权仓库。


### Q: MCP 服务器如何安装？


大多数 MCP 服务器通过 npm 安装，Codex 会自动管理。


### Q: 支持其他集成吗？


Codex 持续添加新集成，关注官方更新。








	  AI 思考中...





			** [Codex 云端版本](https://www.runoob.com/codex-web.html)
			[Codex 自动化与 CI/CD](https://www.runoob.com/codex-automation.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#6f0e0b0206012f1d1a0100000d410c0002)

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