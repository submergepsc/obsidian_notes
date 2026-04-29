
codex logout: 推出当前账号codex






我给你一份**Codex CLI 真正可用的命令体系（精简但全）**，不是乱列，而是按“你实际用法”整理的。
# 🧠 一、核心入口（最重要）
### ▶ 启动 Codex
```bash
codex
```
👉 进入交互界面（TUI） ([MachineLearningMastery.com][1])
### ▶ 带提示启动
```bash
codex "帮我分析这个项目"
```
### ▶ 非交互模式（自动执行）
```bash
codex exec "写一个快速排序"
```
👉 用于脚本 / 自动化 ([微软学习][2])
# ⚙️ 二、基础 CLI 命令
### ▶ 查看版本
```bash
codex --version
```
### ▶ 帮助
```bash
codex --help
```
# 💬 三、交互模式里的“斜杠命令”（重点）
👉 Codex 最核心不是 shell 命令
👉 是 **交互里的 `/命令`**
## 🔍 状态类
### ▶ 查看使用量 / 状态
```bash
/status
```
👉 看：
* token 使用
* 限额
* 当前模型 ([Nathan Onn][3])
## 📁 项目 / 文件
### ▶ 让它读代码
```bash
分析这个项目结构
```
（不是命令，是自然语言）
👉 Codex 会：
* 扫描目录
* 建立上下文 ([OpenAI 开发者][4])
## 🧠 agent 行为控制
### ▶ 切换模式（取决于版本）
```bash
/approve
```
👉 手动批准操作
```bash
/auto
```
👉 自动执行（危险）
## 🔧 操作类
### ▶ 执行任务
```bash
修复这个报错
```
👉 它会：
* 修改代码
* 运行命令
* 提交 patch
# 🧩 四、配置系统
配置文件：
```bash
~/.codex/config.toml
```
👉 控制：
* 模型
* provider（openai / azure）
* 权限
# 🧠 五、重要运行模式
Codex 有 3 个核心模式：

| 模式          | 行为      |
| ----------- | ------- |
| chat        | 只聊天     |
| agent       | 可以改代码   |
| full-access | 全自动（危险） |
([微软学习][2])
# 📂 六、AGENTS.md（隐藏大杀器）
```bash
~/.codex/AGENTS.md
```
👉 相当于：
👉 **给 Codex 写“人格设定 + 行为规则”**
# 🚀 七、你真正会用的命令（精简版）
记住这几个就够：
```bash
codex
codex exec "任务"
codex --version
```
进入后：
```bash
/status
```
剩下全部用自然语言。
# 🧠 和 openclaw 的区别（你一定要搞清）
| 项目   | codex   | openclaw |
| ---- | ------- | -------- |
| 命令数量 | 很少      | 很多       |
| 控制方式 | 自然语言    | CLI      |
| 架构   | 单 agent | 多 agent  |
| 目标   | 写代码     | AI系统     |
# ⚠️ 一个很多人不知道的关键点
👉 Codex CLI：
**几乎没有复杂命令体系**
因为：
👉 **命令 ≠ 功能**
👉 真正功能靠：
* 自然语言
* agent 推理
# 🧩 最真实总结
👉 Codex CLI =
```text
一个 shell + AI
而不是一个命令行工具
```
# 🚀 如果你想进阶（建议你做）
我可以帮你：
👉 把 Codex + tmux + bash alias 整合成：
```bash
c "修复bug"
c "写脚本"
```
甚至👇
🔥 让它变成你的“系统级 Copilot”（任何目录自动工作）
要不要我帮你搞一套你这种 Linux 环境的最强配置？
[1]: https://machinelearningmastery.com/understanding-openai-codex-cli-commands/?utm_source=chatgpt.com "Understanding OpenAI Codex CLI Commands"
[2]: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/codex?utm_source=chatgpt.com "Codex with Azure OpenAI in Microsoft Foundry Models"
[3]: https://www.nathanonn.com/the-latest-codex-cli-commands-that-will-save-your-sanity-and-your-rate-limits/?utm_source=chatgpt.com "The Latest Codex CLI Commands That Will Save Your ..."
[4]: https://developers.openai.com/codex/cli?utm_source=chatgpt.com "Codex CLI"
