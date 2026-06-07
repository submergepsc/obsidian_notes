# Codex CLI 沙箱与安全

- Source: https://www.runoob.com/codex/codex-sandbox.html

Codex CLI 内置了沙箱机制和安全策略，确保在帮助你编程的同时保护系统和数据安全。本节详细介绍这些安全机制以及如何配置它们。


---


## 沙箱机制


Codex 在一个隔离的沙箱环境中执行命令和操作文件。这种设计确保：


- 对你的项目文件的修改是可控的
- 潜在危险的命令需要你的确认
- 敏感数据不会意外泄露


**
沙箱是 Codex 安全策略的第一道防线，它确保 AI 的操作不会超出你的预期范围。


---


## 执行策略


Codex 使用执行策略（Execution Policy）来控制不同类型操作的行为：


### 策略类型


| 策略 | 行为 | 适用场景 |
| --- | --- | --- |
| ask | 每次执行前询问确认 | 日常开发（默认） |
| approve | 自动批准执行 | 完全信任的环境 |
| deny | 拒绝所有可能产生副作用的操作 | 只读模式 |


### 需要确认的操作


以下类型的操作会触发确认请求：


- 执行 Shell 命令（特别是 `rm`、`kill` 等）
- 修改或删除文件
- 创建新文件
- 访问敏感目录（如 `~/.ssh/`、`/etc/`）
- 网络请求（特定情况下）


### 配置执行策略


## 在配置中设置执行策略


```
[exec]
default_policy = "ask"
```


> 出于安全考虑，不建议将默认策略设置为 `approve`，除非你完全理解潜在的风险。


---


## 确认对话框


当 Codex 需要执行敏感操作时，会显示确认对话框：


```
══════════════════════════════════════════════════════
  确认执行
══════════════════════════════════════════════════════

  Codex 计划执行以下操作：

  命令: rm -rf node_modules/
  目录: /path/to/project

  这将永久删除目录及其所有内容

  [Y] 确认执行  [N] 取消  [A] 始终允许此类操作
══════════════════════════════════════════════════════
```


### 选项说明


| 选项 | 说明 |
| --- | --- |
| Y | 只执行这一次 |
| N | 取消操作 |
| A | 添加规则，之后自动批准 |


> 选择"始终允许"时要小心，确保该操作确实是安全的。


---


## 文件访问控制


### 受保护的目录


某些系统目录默认受到保护，Codex 访问这些目录时会额外确认：


| 目录 | 说明 |
| --- | --- |
| ~/.ssh/ | SSH 密钥和配置 |
| ~/.aws/ | AWS 凭证 |
| /etc/ | 系统配置 |
| ~/.git-credentials | Git 凭证存储 |


### 自定义保护规则


你可以在配置中添加自定义的保护规则：


## 配置文件访问规则


```
[sandbox]
# 允许访问的目录
allowed_paths = [
    "~/projects/*",
    "/workspace/*"
]

# 受保护的目录（需要额外确认）
protected_paths = [
    "~/.ssh/*",
    "~/secrets/*"
]
```


---


## 网络访问控制


Codex 可以限制网络请求的访问范围：


## 配置网络访问


```
[network]
# 允许的域名
allowed_domains = [
    "github.com",
    "api.openai.com"
]

# 是否允许本地网络访问
allow_localhost = false

# 是否允许私有网络
allow_private_network = false
```


> 限制网络访问可以防止 Codex 意外连接到不受信任的服务。


---


## 工作目录限制


你可以限制 Codex 只能在特定目录中操作：


## 限制工作目录


```
[sandbox]
# Codex 只能在这些目录中操作
working_directories = [
    "~/projects/*",
    "/workspace/*"
]

# 超出目录时的行为：warn（警告）或 deny（拒绝）
out_of_bounds = "deny"
```


---


## 命令白名单/黑名单


### 白名单模式（推荐）


只允许执行明确列出的命令：


## 命令白名单


```
[commands]
# 白名单模式
whitelist_enabled = true
allowed_commands = [
    "git",
    "npm",
    "node",
    "python",
    "cargo"
]
```


### 黑名单模式


禁止执行特定命令：


## 命令黑名单


```
[commands]
# 黑名单模式
blacklist_enabled = true
blocked_commands = [
    "rm -rf /",
    "dd",
    "mkfs"
]
```


> 白名单模式更加安全，建议在生产环境或处理敏感项目时使用。


---


## 敏感数据处理


### 自动屏蔽


Codex 会自动检测并屏蔽敏感信息：


- API 密钥和密码
- 令牌和认证信息
- 个人身份信息（PII）


### 环境变量保护


某些环境变量会被自动隐藏：


```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
OPENAI_API_KEY
DATABASE_URL
```


### 手动指定敏感数据


你可以在配置中手动标记需要保护的内容：


## 自定义敏感数据模式


```
[sensitive]
# 需要屏蔽的正则表达式模式
patterns = [
    "password\\s*=\\s*[^\\s]+",
    "api_key\\s*=\\s*[^\\s]+",
    "secret\\s*=\\s*[^\\s]+"
]
```


---


## 审计日志


Codex 可以记录所有操作的审计日志：


## 启用审计日志


```
[audit]
enabled = true
log_file = "~/.codex/log/audit.log"
```


### 日志内容


审计日志记录以下信息：


- 时间戳
- 操作类型
- 涉及的文件或命令
- 操作结果（成功/失败）
- 用户确认状态


## 查看审计日志


```
# 查看最近的审计日志
tail -f ~/.codex/log/audit.log
```


> 审计日志对于安全审计和问题排查非常重要，特别是在团队环境中。


---


## 安全最佳实践


### 开发环境


- 使用默认的执行策略（ask）
- 启用审计日志
- 配置命令白名单


### 生产环境


- 限制工作目录
- 使用白名单模式
- 禁用不必要的网络访问
- 启用完整的审计日志


### 敏感项目


- 使用最严格的保护规则
- 仔细审查每一个确认请求
- 定期检查审计日志


---


## 常见问题


### Q: 执行策略在哪里配置？


执行策略主要通过 `~/.codex/config.toml` 配置文件进行设置。部分设置也可以通过环境变量配置。


### Q: 误点了"始终允许"怎么办？


删除配置文件中的相关规则，或删除整个配置文件后重新启动 Codex，规则会被重置。


### Q: Codex 能访问我的 GitHub 令牌吗？


Codex 会请求访问 GitHub 的必要权限来执行操作。你可以随时在 GitHub 设置中撤销这些权限。


### Q: 如何完全禁用文件修改？


将执行策略设置为 `deny`，这将禁止 Codex 执行任何可能修改文件系统的操作。








	  AI 思考中...





			** [Codex CLI Skills](https://www.runoob.com/codex-cli-skills.html)
			[Codex CLI 实用示例](https://www.runoob.com/codex-examples.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#dabbbeb7b3b49aa8afb4b5b5b8f4b9b5b7)

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