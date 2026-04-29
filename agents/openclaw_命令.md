openclaw onboard: 初始化




 
 


	 
行，这里给你一份**真正能用的 OpenClaw CLI 命令全览（按功能分组）**，不是零散列举，而是帮你形成一套“脑子里的操作体系”。
# 🧠 一、核心入口（你最常用）
### ▶ 启动交互
```bash
openclaw
```
👉 启动 CLI + agent（默认 Crestodian）
### ▶ 查看状态（你刚用的）
```bash
openclaw status
openclaw status --deep
```
👉 检查：
- Gateway
- 模型
- 插件
- memory
- sessions
### ▶ 调 agent（核心用法）
```bash
openclaw talk
```
👉 进入“正常 AI 对话模式”
# 🤖 二、Agent 系统
	### ▶ 查看 agent
```bash
openclaw agents list
```
### ▶ 添加 agent
```bash
openclaw agents add <name>
```
### ▶ 删除 agent
```bash
openclaw agents remove <name>
```
# 💬 三、Session（会话管理）
### ▶ 查看 session
```bash
openclaw sessions list
```
### ▶ 切换 session
```bash
openclaw sessions use <name>
```
### ▶ 新建 session
```bash
openclaw sessions new <name>
```
# ⚙️ 四、配置系统（很关键）
### ▶ 初始化配置
```bash
openclaw init
```
### ▶ 编辑配置
```bash
openclaw config edit
```
👉 修改：
- 模型来源（copilot / openai / ollama）
- agent 默认行为
- 插件开关
### ▶ 查看配置
```bash
openclaw config show
```
# 🌐 五、Gateway（通信核心）
### ▶ 启动 gateway（一般自动）
```bash
openclaw gateway start
```
### ▶ 停止
```bash
openclaw gateway stop
```
# 🧩 六、插件系统（你现在有 warning）
### ▶ 查看插件
```bash
openclaw plugins list
```
### ▶ 安装插件
```bash
openclaw plugins install <name>
```
### ▶ 移除插件
```bash
openclaw plugins remove <name>
```
# 🧠 七、Memory / 向量库
### ▶ 查看状态
```bash
openclaw memory status
```
### ▶ 重建索引
```bash
openclaw memory rebuild
```
👉 解决：
- 向量错误
- 检索异常
# 🔍 八、诊断 & 调试（高级）
### ▶ 深度检测
```bash
openclaw status --deep
```
### ▶ 日志
```bash
openclaw logs
```
或直接看：
```bash
~/.openclaw/logs/
```
# 🚀 九、任务系统（后台执行）
### ▶ 查看任务
```bash
openclaw tasks list
```
### ▶ 清空任务
```bash
openclaw tasks clear
```
# 🧪 十、本地模式 / 推理模式
### ▶ 本地推理（你之前用过）
```bash
openclaw infer_mode run --local
```
👉 用于：
- 不走云
- 本地 agent 调度
# 📦 十一、Onboarding（你刚跑的）
```bash
openclaw onboard
```
👉 初始化：
- Node 环境
- gateway
- 默认 agent
# 🧠 十二、一个你必须知道的命令（最重要）
```bash
openclaw talk
```
👉 所有复杂功能最终都归到它：
- agent 调用
- 模型推理
- 插件触发
- memory 检索
# 🧩 总结一张“命令地图”
```
openclaw
 ├── status
 ├── talk
 ├── agents
 ├── sessions
 ├── config
 ├── plugins
 ├── memory
 ├── gateway
 ├── tasks
 ├── logs
 ├── onboard
 └── infer_mode
```
# ⚠️ 给你一个现实提醒（很重要）
OpenClaw：
👉 不是一个“命令很多的工具”  
👉 而是一个：
**👉 用少量命令控制复杂 AI 系统的框架**
# 🎯 给你一个最实用组合（建议你记住）
日常你只需要：
```bash
openclaw status --deep
openclaw talk
openclaw plugins list
openclaw config edit
```
就够用了。
# 🚀 如果你想更狠一点
我可以帮你：
👉 做一个你的专属：
- alias 快捷命令
- tmux + openclaw 自动启动
- 一键 agent 启动脚本
甚至👇  
🔥 把 openclaw 变成你系统级 AI（像 Copilot 一样全局用）
要不要继续升级？