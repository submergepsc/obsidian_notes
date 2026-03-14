---
tags: [AI, Coze, AgentOps, 开发者工具]
date: 2026-03-14
---
# 🧠 扣子 (Coze) 生态架构导览

> [!abstract] 架构速览
> Coze (扣子) 生态由三个核心层级构成，分别对应了 AI 智能体的**前端交互**、**底层代码沙箱**以及**运维监控**。

## 1. 💬 应用层：前端交互与编排台
- **官方入口**: [https://www.coze.cn](https://www.coze.cn)    
- **核心定位**: 在线聊天软件与低代码编排中心。
- **技术解析**: 表面上看是一个 C 端的在线对话窗口，但本质上它是 Agent 的“总装车间”。在这里可以通过可视化界面配置 Prompt、外挂知识库 (RAG) 和组装现成的第三方插件，并实时进行对话测试。

## 2. 💻 基础设施层：云端开发沙箱
- **官方入口**: [https://code.coze.cn](https://code.coze.cn)
- **核心定位**: 在线 IDE (云端集成开发环境)。
- **技术解析**: 当拖拽式组件无法满足需求时，这里就是硬核极客的 Serverless 战场。它允许你跳出纯文本框架，直接编写 Node.js 或 Python 代码，管理 `package.json`，徒手搓出底层的自定义技能（Skills）来操控外部 API 或系统资源。

## 3. 🧭 运维层：扣子罗盘 (Coze Loop)
- **官方入口**: [https://loop.coze.cn](https://loop.coze.cn)
- **核心定位**: 额度查询与全链路可观测性平台 (AgentOps)。
- **技术解析**: 官方称为“扣子罗盘”。除了作为直观的“额度查询页面”用来监控 API 消耗外，它更是排障的核心观测塔。当复杂的 AI 链路崩溃或出现幻觉时，可以在这里查看每一条 Log、追踪底层调用的 Trace 链路，评估系统的整体稳定性。




# coze沙盘结构
根目录 **/** 对应的是localhost,*/workspace/projects* 对应5000端口；
**/workspace/projects/workspace/skills/一堆skills目录/(skills.md / *.py)**





# linux简单命令
**命令+【参数】+对象**
### 命令
#### 基本目录与文件
- pwd: print working directory.
- cd : change directory
- ls : list 
	- -l : 详细信息 ，long
	- -a: 显示 .log 等隐藏文件
	- -h: humman readable , 大小显示乘kb,mb
- mkdir : make dir 
	-  mkdir -p a/b/c :多层
- rm : rm file.txt :删除文件
	- rm -rf dir 删除目录
- cp: copy
	- cp a.txt b.txt (a->b)
	- cp -r a b (目录a->b )
- mv : move 
	- mv old.name new.name(==rename)
	- mv file.txt /tmp/dir

#### 文件查看与文本处理
- cat 


