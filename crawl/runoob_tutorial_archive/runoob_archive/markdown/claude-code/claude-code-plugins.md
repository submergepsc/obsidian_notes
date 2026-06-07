# Claude Code 插件

- Source: https://www.runoob.com/claude-code/claude-code-plugins.html

插件（Plugin）是 Claude Code 中**最高级别的扩展机制**，用于将命令、代理、Skills、钩子、MCP、LSP 等能力**打包、版本化、共享和分发**。


**插件 = 一组可复用的 Claude Code 扩展能力集合**


一个插件可以包含：


- 斜杠命令（Slash Commands）
- 子代理（Agents）
- Skills（能力说明）
- Hooks（事件钩子）
- MCP 服务器（外部工具/服务）
- LSP 服务器（代码智能）


**
插件的核心目标只有一个：


让 Claude Code 的能力像工具箱"一样被复用，而不是每个项目重复配置**


---


## 插件 vs 独立配置（如何选择）


Claude Code 支持两种扩展方式：


| 方式 | 命令形式 | 适合场景 |
| --- | --- | --- |
| 独立配置（.claude/） | /hello | 个人使用、单项目、快速实验 |
| 插件（.claude-plugin/） | /plugin-name:hello | 团队共享、跨项目、版本化 |


### 什么时候用独立配置？


- 只在当前项目使用
- 个人工作流
- 尚未稳定的实验性配置
- 想要简短命令名（如 `/review`）


### 什么时候用插件？


- 要在**多个项目复用**
- 要**分享给团队或社区**
- 需要**版本控制、升级、回滚**
- 计划通过市场分发
- 可以接受命名空间命令（避免冲突）


**
最佳实践：**


先在 `.claude/` 中迭代 → 稳定后打包为插件


---


## 插件的最小结构（必须记住）


```
my-plugin/
├── .claude-plugin/
│   └── plugin.json     # 插件清单（必需）
├── commands/           # 斜杠命令
├── agents/             # 子代理
├── skills/             # Skills
├── hooks/              # 钩子
├── .mcp.json           # MCP 配置
└── .lsp.json           # LSP 配置
```


**重要规则**


- `.claude-plugin/` 目录中**只能放 `plugin.json`**
- 其他目录必须在插件根目录


---


## 插件清单（plugin.json）


插件的"身份证"，决定：


- 插件名称
- 命令命名空间
- 版本
- 作者信息


示例：


```
{
  "name": "my-first-plugin",
  "description": "A greeting plugin to learn the basics",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```


关键字段说明：


| 字段 | 作用 |
| --- | --- |
| name | 唯一标识 + 命令命名空间 |
| description | 插件市场中展示 |
| version | 语义化版本控制 |
| author | 可选，归属说明 |


---


## 斜杠命令（最常用插件能力）


### 1、命令定义方式


- 位于 `commands/` 目录
- 每个命令 = 一个 Markdown 文件
- 文件名 = 命令名


示例：


```
commands/hello.md
```


对应命令：


```
/my-first-plugin:hello
```


### 2、命令内容示例


```
---
description: Greet the user with a friendly message
---

Greet the user warmly and ask how you can help them today.
```


### 3、命令参数


使用 `$ARGUMENTS` 捕获用户输入：


```
Greet the user named "$ARGUMENTS" warmly.
```


调用：


```
/my-first-plugin:hello Alex
```


---


## 本地测试插件（开发必会）


使用 `--plugin-dir` 直接加载插件目录：


```
claude --plugin-dir ./my-plugin
```


特点：


- 不需要安装
- 修改后需重启 Claude Code
- 支持同时加载多个插件


```
claude --plugin-dir ./plugin-a --plugin-dir ./plugin-b
```


---


## 插件还能做什么


| 能力 | 用途 |
| --- | --- |
| Commands | 自定义斜杠命令 |
| Agents | 专用子代理 |
| Skills | 教会 Claude 何时用某种能力 |
| Hooks | 自动化（写完文件后执行命令等） |
| MCP | 连接外部服务（GitHub、DB、API） |
| LSP | 代码智能（跳转、类型检查） |


---


## 插件市场（Plugin Marketplace）


插件通过**市场**分发，本质是一个插件目录仓库。


### 官方市场


- 默认已添加
- 运行 `/plugin` → **Discover**


![](https://www.runoob.com/wp-content/uploads/2026/01/9019efba-efb3-4311-8286-a784ad0e6356.png)


安装插件：


```
/plugin install plugin-name@claude-plugins-official
```


---


## 插件安装范围


| 范围 | 说明 |
| --- | --- |
| 用户范围 | 仅你自己，所有项目 |
| 项目范围 | 当前仓库，团队共享 |
| 本地范围 | 当前仓库，仅你 |


推荐：


- 团队工具 → **项目范围**
- 个人效率工具 → **用户范围**


---


## 典型插件分类


### 1、代码智能（LSP）


- TypeScript、Python、Go、Rust 等
- 提供跳转定义、引用、类型错误


需要本地安装对应语言服务器


### 2、外部集成（MCP）


- GitHub / GitLab
- Jira / Notion
- Slack / Figma
- Vercel / Supabase

**

本质：插件 = MCP 服务器 + 配置**


### 3、开发工作流


- Git 提交、PR
- 代码审查代理
- 插件开发工具


---


## 插件管理常用命令


```
/plugin                # 打开插件管理器
/plugin install         # 安装插件
/plugin uninstall       # 卸载
/plugin enable/disable  # 启用 / 禁用
/plugin marketplace add # 添加市场
/plugin marketplace rm  # 移除市场
```


---


## 从 .claude/ 迁移到插件（核心思路）


| 原来 | 迁移后 |
| --- | --- |
| .claude/commands | plugin/commands |
| .claude/agents | plugin/agents |
| settings.json hooks | plugin/hooks/hooks.json |


迁移后：


- 插件版本优先生效
- 可删除旧 `.claude/` 配置避免重复


---


## 什么时候你一定要用插件？


- 你已经有**稳定的 Claude 工作流**
- 你在**反复复制 `.claude/`**
- 团队成员开始问你："这个怎么配置？"
- 你希望 Claude 像 IDE 插件一样可控

**

插件，是 Claude Code 从"个人 AI 助手"走向"工程化工具"的分水岭**










	  AI 思考中...





			** [Claude Code 子代理](https://www.runoob.com/claude-code-subagent.html)
			[Claude Code 输出样式](https://www.runoob.com/claude-code-outputstyles.html) **













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