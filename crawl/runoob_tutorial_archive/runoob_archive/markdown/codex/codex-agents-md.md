# Codex AGENTS.md

- Source: https://www.runoob.com/codex/codex-agents-md.html

AGENTS.md 是 Codex 的自定义指令文件，允许你为 Codex 设置全局指导和工作流规范。本节详细介绍如何创建和使用 AGENTS.md。


---


## 什么是 AGENTS.md？


AGENTS.md 是 Codex 在执行任何工作之前读取的指令文件，允许你：


- 设置全局编码规范
- 定义项目特定的工作流程
- 为不同目录提供不同的指导
- 标准化团队的开发实践


**通过 AGENTS.md，你可以确保 Codex 在整个代码库中遵循一致的规范。


---


## Codex 如何发现指南


Codex 按以下优先级构建指令链：


### 优先级顺序


- **全局范围**：读取 `~/.codex/AGENTS.override.md` 或 `~/.codex/AGENTS.md`
- **项目范围**：从项目根目录到当前目录，逐层检查 `AGENTS.override.md` 和 `AGENTS.md`
- **就近优先**：更接近当前目录的文件会覆盖之前的指导


> 靠近当前目录的指令会覆盖之前的指导，这样可以在子目录中为特定模块提供专门的规则。


---


## 创建全局指导


### 基础配置


## 创建全局 AGENTS.md


```
# 创建全局配置目录
mkdir -p ~/.codex

# 创建全局指导文件
touch ~/.codex/AGENTS.md
```


### 全局指导示例


## 全局指导内容


```
# Codex 全局指导

## 编码规范
- 使用 4 空格缩进
- 每行最多 100 个字符
- 始终使用 const/let，不使用 var

## 代码质量
- 所有导出的函数必须包含 JSDoc 注释
- 添加适当的错误处理
- 避免使用 console.log，使用项目中的日志库

## 测试要求
- 新功能必须包含测试
- 使用项目指定的测试框架

## Git 提交
- 使用 Conventional Commits 格式
- 提交信息必须描述性地说明"为什么"
```


### 临时覆盖


使用 `~/.codex/AGENTS.override.md` 设置临时全局覆盖：


## 临时覆盖


```
# 临时覆盖 - 调试模式

## 特殊规则
- 启用详细日志输出
- 添加调试注释
- 跳过性能优化以加快迭代速度
```


> AGENTS.override.md 用于临时覆盖，不会影响正常的 AGENTS.md 配置。


---


## 项目级指导


### 仓库级配置


在仓库根目录创建 `AGENTS.md`：


## 项目 AGENTS.md


```
# 项目编码规范

## 技术栈
- 前端：React + TypeScript
- 后端：Python FastAPI
- 数据库：PostgreSQL

## 前端规范
- 使用函数组件，不使用类组件
- 使用 Tailwind CSS 进行样式
- 组件文件以 .tsx 结尾

## 后端规范
- 使用 Pydantic 进行数据验证
- 所有 API 端点必须有类型注解
- 使用 async/await 处理异步操作

## 数据库
- 使用 SQLAlchemy ORM
- 避免原始 SQL 查询
- 所有表必须有 created_at 和 updated_at 字段
```


### 子目录覆盖


在子目录中创建 `AGENTS.override.md` 提供专门的规则：


## 子目录配置


```
# src/auth/ 模块特定规则

## 安全要求
- 所有密码必须 bcrypt 加密
- 实现速率限制
- 添加审计日志

## 额外审查
- 强制代码审查
- 检查 SQL 注入
- 验证认证流程
```


> 子目录的规则会覆盖父目录的规则，确保模块特定的规范优先。


---


## 自定义回退文件名


如果你的项目使用其他文件名，可以配置回退：


## 配置回退文件名


```
# 支持其他命名约定
project_doc_fallback_filenames = [
    "TEAM_GUIDE.md",
    "CONTRIBUTING.md",
    ".codex.md"
]
```


---


## 代码审查指南


在 AGENTS.md 中添加审查指南：


## 审查指南


```
## Review guidelines

- Don't log PII (个人身份信息)
- Verify that authentication middleware wraps every route
- Check for SQL injection vulnerabilities
- Ensure error messages don't leak sensitive information
- Treat documentation typos as P1 issues
```


### 问题优先级


| 优先级 | 说明 |
| --- | --- |
| P0 | 严重问题 - 安全漏洞、崩溃、数据丢失 |
| P1 | 重要问题 - 功能错误、性能问题 |
| P2 | 次要问题 - 代码风格、文档问题 |


> 在 GitHub 集成中，Codex 默认只标记 P0 和 P1 问题。


---


## 验证与故障排除


### 验证配置


## 验证 AGENTS.md


```
# 测试 AGENTS.md 配置
codex --ask-for-approval never "Summarize the current instructions."
```


### 检查日志


查看 Codex 日志确认加载：


```
tail -f ~/.codex/log/codex-tui.log
```


### 常见问题


| 问题 | 原因 | 解决方案 |
| --- | --- | --- |
| 指令不生效 | 文件为空 | 确保文件包含实际内容 |
| 被隐藏覆盖 | 存在 override 文件 | 检查 AGENTS.override.md |
| 内容被截断 | 超过 32 KiB 限制 | 精简内容或拆分文件 |


> Codex 默认会在组合大小达到 32 KiB 时停止读取。


---


## 最佳实践


- **保持简洁**：只包含必要的规则
- **分层设计**：全局 -> 项目 -> 模块
- **团队同步**：将项目 AGENTS.md 提交到版本控制
- **定期审查**：更新规则以适应项目变化


> 好的 AGENTS.md 配置可以让整个团队受益，确保 Codex 的行为符合团队期望。


---


## 常见问题


### Q: AGENTS.md 文件多大合适？


建议控制在几 KB 以内，过大的文件会被截断（默认 32 KiB）。


### Q: 可以禁用项目级 AGENTS.md 吗？


可以，使用 `project_doc_fallback_filenames = []` 配置为空数组。


### Q: 子目录和父目录的规则冲突怎么办？


子目录的规则会覆盖父目录的规则。


### Q: 如何临时覆盖项目规则？


使用 `AGENTS.override.md` 文件进行临时覆盖。








	  AI 思考中...





			** [Codex 非交互模式](https://www.runoob.com/codex-noninteractive.html)
			[Codex GitHub 集成](https://www.runoob.com/codex-github.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#452421282c2b0537302b2a2a276b262a28)

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