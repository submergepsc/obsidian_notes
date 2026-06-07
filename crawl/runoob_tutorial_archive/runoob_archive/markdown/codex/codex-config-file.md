# Codex 配置与定制

- Source: https://www.runoob.com/codex/codex-config-file.html

Codex 提供丰富的配置选项，让你定制 Agent 的行为以适应不同的工作需求。


---


## 配置文件位置


Codex 配置文件分层管理：


| 层级 | 路径 | 作用范围 |
| --- | --- | --- |
| 用户级 | ~/.codex/config.toml | 全局默认配置 |
| 项目级 | .codex/config.toml | 项目特定配置 |
| 托管级 | 企业下发 | 企业统一配置 |


### 配置合并规则


配置按优先级合并：


- 托管配置优先级最高
- 项目配置覆盖用户配置
- 用户配置作为默认值


---


## 基础配置项


## 基础配置


```
# ~/.codex/config.toml

# 默认模型
model = "gpt-5.4"

# 推理强度
model_reasoning_effort = "medium"  # minimal | low | medium | high | xhigh

# 推理摘要详细程度
model_reasoning_summary = "auto"  # auto | concise | detailed | none

# 服务层级
service_tier = "flex"  # flex | fast

# 审批策略
approval_policy = "suggest"  # suggest | auto-edit | full-auto
```


---


## AGENTS.md


AGENTS.md 是项目级的 Agent 指令文件，定义 Codex 在该项目中的行为规范。


### 文件发现顺序


- 读取全局 `~/.codex/AGENTS.md`
- 从项目根目录向下搜索每个目录
- 更近目录的规则覆盖更远的


### AGENTS.md 示例


## 项目 AGENTS.md


```
# 项目开发规范

## 技术栈
- 前端：React + TypeScript
- 后端：Python FastAPI
- 数据库：PostgreSQL

## 代码规范
- 使用 4 空格缩进
- 每行最多 100 字符
- 所有函数必须有类型注解

## 测试要求
- 新功能必须包含测试
- 使用 pytest 运行测试

## Git 提交
- 使用 Conventional Commits 格式
- 提交信息描述"为什么"

## Review guidelines
- Don't log PII
- Verify authentication middleware
- Check for SQL injection
```


### 子目录覆盖


可以在子目录放置 AGENTS.override.md：


## 子目录规则


```
# src/auth/ 模块规则

## 安全要求
- 所有密码必须 bcrypt 加密
- 添加审计日志
- 检查 SQL 注入
```


**
AGENTS.md 大小限制为 32 KiB，超过会被截断。


---


## Skills（技能）


Skills 是可复用的自定义能力，封装常用任务逻辑。


### 技能目录位置


| 位置 | 路径 | 作用 |
| --- | --- | --- |
| REPO | .agents/skills/ | 项目级技能 |
| USER | ~/.agents/skills/ | 用户级技能 |
| ADMIN | /etc/codex/skills/ | 系统级技能 |
| SYSTEM | 内置 | 官方预置技能 |


### 技能结构


```
skill-name/
├── SKILL.md       # 技能定义（必需）
├── scripts/       # 可选脚本
├── references/    # 可选参考文档
└── assets/        # 可选资源
```


### 创建技能


## 技能定义


```
---
name: code-review-standard
description: 执行团队标准代码审查
---

# 代码审查标准

## 审查项目
1. 代码可读性
2. 潜在 Bug
3. 安全漏洞
4. 性能问题
5. 测试覆盖

## 输出格式
- 问题列表（按严重程度）
- 改进建议
- 评分（1-10）
```


### 技能触发


| 触发方式 | 示例 |
| --- | --- |
| 显式调用 | $skill-name 或 /skill-name |
| 隐式匹配 | 任务描述匹配技能 description |


---


## Subagents（子代理）


Subagents 允许将复杂任务拆分给多个 Agent 并行处理。


### 内置代理类型


| 代理 | 功能 |
| --- | --- |
| default | 通用代理 |
| worker | 执行导向，适合实现和修复 |
| explorer | 探索导向，适合代码库分析 |


### 配置子代理


## 子代理配置


```
# ~/.codex/config.toml

[agents]
# 最大并行线程
max_threads = 6

# 最大嵌套深度
max_depth = 1

# 单任务超时
job_max_runtime_seconds = 1800
```


### 自定义代理


## 自定义代理


```
# ~/.codex/agents/reviewer.toml

name = "reviewer"
description = "专注代码审查和质量问题"
nickname_candidates = ["Reviewer", "QualityBot"]

developer_instructions = """
专注于代码质量审查：
- 检查代码风格一致性
- 发现潜在 Bug
- 评估测试覆盖
"""
```


---


## Rules（规则）


Rules 定义命令执行策略，控制哪些命令可以自动执行。


### 规则文件


规则使用 Starlark 语言（类似 Python）：


## 规则定义


```
# ~/.codex/rules/default.rules

# 允许 Git 命令
prefix_rule(
    pattern = ["git"],
    decision = "allow",
    justification = "Git commands are safe"
)

# 禁止 rm -rf /
prefix_rule(
    pattern = ["rm", "-rf", "/"],
    decision = "forbidden",
    justification = "Prevent system damage"
)

# 询问 npm 命令
prefix_rule(
    pattern = ["npm"],
    decision = "prompt",
    justification = "npm may modify dependencies"
)
```


### 决策类型


| 决策 | 行为 |
| --- | --- |
| allow | 自动批准 |
| prompt | 询问确认 |
| forbidden | 禁止执行 |


---


## Hooks（钩子）


Hooks 在特定事件时执行自定义脚本。


### 启用 Hooks


## 启用 Hooks


```
[features]
codex_hooks = true
```


### Hook 事件


| 事件 | 触发时机 |
| --- | --- |
| SessionStart | 会话启动 |
| PreToolUse | 工具调用前 |
| PostToolUse | 工具调用后 |


### 配置 Hook


## Hook 配置


```
{
  "hooks": [
    {
      "event": "PostToolUse",
      "matcher": {
        "toolName": "Bash"
      },
      "hooks": [
        {
          "type": "command",
          "command": "echo 'Command executed'",
          "timeout": 10
        }
      ]
    }
  ]
}
```


---


## 常见问题


### Q: 配置修改后如何生效？


修改配置后需要重启 Codex 才能生效。


### Q: AGENTS.md 应放在哪里？


项目根目录，或需要特殊规则的子目录。


### Q: Skills 和 Rules 的区别？


Skills 定义任务执行逻辑，Rules 控制命令权限。


### Q: 如何查看当前配置？


使用 `/status` 命令查看当前会话配置。








	  AI 思考中...





			** [Codex 基础入门](https://www.runoob.com/codex-usage.html)
			[Codex 速查表](https://www.runoob.com/codex-commands.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#78191c151116380a0d1617171a561b1715)

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