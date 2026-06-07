# Claude Code 入门教程

- Source: https://www.runoob.com/ai-agent/claude-code.html

Claude Code 是 Anthropic 官方 CLI 级智能体工具。


Claude Code 定位不是聊天，而是 在本地代码仓库中执行高权限、可上下文感知的工程任务。


**
Claude Code 是 Agent，不是 Chat。


详细教程参见：[https://www.runoob.com/claude-code/claude-code-tutorial.html](https://www.runoob.com/../claude-code/claude-code-tutorial.html)


核心能力：


- 直接读取整个项目目录
- 理解真实代码结构
- 执行多文件修改
- 严格遵循指令而非对话取悦


![](https://www.runoob.com/wp-content/uploads/2025/12/whats-claude-code-v0-f1vrmqb645le1.webp)


### 安装配置

MacOS/Linux:**


```
curl -fsSL https://claude.ai/install.sh | bash
```


**Homebrew (MacOS):**


```
brew install --cask claude-code
```


**Windows:**


```
irm https://claude.ai/install.ps1 | iex
```


**NPM:**


使用 npm 安装 请确保你的系统的安装了 Node.js，版本需在 v18 或更高。


```
npm install -g @anthropic-ai/claude-code
```


**接下来就可以开始进入你创建的项目目录，开始使用 Claude Code：**


```
cd your-project
claude
```


### 登录您的账户

使用 claude 命令启动交互式会话时，您需要登录：


```
claude
# 首次使用时会提示您登录
/login
# 按照提示使用您的账户登录
```


![](https://www.runoob.com/wp-content/uploads/2025/12/dabcedd3-5857-4090-870a-47805307e534.png)


如果你可以正常使用 Anthropic 的账号，就可以开始使用，如果没有国内可以使用 DeepSeek 或 GLM 等。


---


## DeepSeek 接入 Claude Code

安装 Claude Code 后，我们在终端中设置以下环境变量：


```
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN=${DEEPSEEK_API_KEY} # 这里记得设置你申请的 API key
export API_TIMEOUT_MS=600000
export ANTHROPIC_MODEL=deepseek-chat
export ANTHROPIC_SMALL_FAST_MODEL=deepseek-chat
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
```


**参数说明：**


- `API_TIMEOUT_MS=600000`：设置 10 分钟超时，防止输出过长触发客户端超时
- `ANTHROPIC_MODEL`：指定使用 deepseek-chat 模型
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`：禁用非必要流量


然后进入项目目录，执行 claude 命令，即可开始使用了。


```
cd my-project
claude
```


![](https://www.runoob.com/wp-content/uploads/2025/12/aebe4b0f-78f1-40fc-87ce-05f889af4c8e.png)


参考文档：[https://api-docs.deepseek.com/zh-cn/guides/anthropic_api](https://api-docs.deepseek.com/zh-cn/guides/anthropic_api)


---

## 阿里百炼接入 Claude Code

阿里云百炼的通义千问系列模型支持 Anthropic API 兼容接口，通过修改以下参数，即可在 Claude Code 中调用通义千问系列模型。


- ANTHROPIC_API_KEY（或 ANTHROPIC_AUTH_TOKEN）：替换为百炼 API Key，申请地址：[https://bailian.console.aliyun.com/cn-beijing/?tab=model#/api-key](https://bailian.console.aliyun.com/cn-beijing/?userCode=i5mn5r7m&tab=model#/api-key)。
- ANTHROPIC_BASE_URL：替换为百炼的兼容端点地址 **https://dashscope.aliyuncs.com/apps/anthropic**。
- 模型名称：替换为百炼支持的模型名称（例如 qwen3-max、qwen3-coder-plus等）


**macOS/Linux：**


创建并打开配置文件 **~/.claude/settings.json**。


**~** 代表用户主目录，如果 **.claude** 目录不存在，需要先行创建，可在终端执行 **mkdir -p ~/.claude **来创建。


编辑配置文件：


```
vim ~/.claude/settings.json
```


将 YOUR_API_KEY 替换为专属 API Key。





```
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
        "ANTHROPIC_BASE_URL": "https://dashscope.aliyuncs.com/apps/anthropic",
        "ANTHROPIC_MODEL": "qwen3-coder-plus"
    }
}
```


重新打开一个新的终端使环境变量配置生效。


**Windows：**

在 CMD 中运行以下命令，设置环境变量：





```
setx ANTHROPIC_AUTH_TOKEN "YOUR_API_KEY"
setx ANTHROPIC_BASE_URL "https://dashscope.aliyuncs.com/apps/anthropic"
setx ANTHROPIC_MODEL "qwen3-coder-plus"
```


用套餐专属 API Key 替换 YOUR_API_KEY。


打开一个新的 CMD 窗口，运行以下命令，检查环境变量是否生效。


```
echo %ANTHROPIC_AUTH_TOKEN%
echo %ANTHROPIC_BASE_URL%
echo %ANTHROPIC_MODEL%
```


在 PowerShell 中运行以下命令，设置环境变量：


```
# 用套餐专属 API Key 替换 YOUR_API_KEY
[Environment]::SetEnvironmentVariable("ANTHROPIC_AUTH_TOKEN", "YOUR_API_KEY", [EnvironmentVariableTarget]::User)
[Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://dashscope.aliyuncs.com/apps/anthropic", [EnvironmentVariableTarget]::User)
[Environment]::SetEnvironmentVariable("ANTHROPIC_MODEL", "qwen3-coder-plus", [EnvironmentVariableTarget]::User)
```


打开一个新的 PowerShell 窗口，运行以下命令，检查环境变量是否生效。


```
echo $env:ANTHROPIC_AUTH_TOKEN
echo $env:ANTHROPIC_BASE_URL
echo $env:ANTHROPIC_MODEL
```


### 在 Claude Code 中接入通义千问系列模型


对话期间，执行 **/model ** 命令切换模型。




```
/model qwen3-coder-plus
```


也可以在项目根目录创建 **.claude/settings.json** 文件中，并写入模型配置信息永久配置。


![](https://www.runoob.com/wp-content/uploads/2026/01/6a97af64-c4a5-425b-99a0-3aaf9dc59dbd.png)




```
{
  "env": {
    "ANTHROPIC_MODEL": "qwen3-coder-plus",
    "ANTHROPIC_SMALL_FAST_MODEL": "qwen-flash"
  }
}
```


启动 Claude，可以看到配置信息：


![](https://www.runoob.com/wp-content/uploads/2026/01/d811c5e3-f30f-4c1b-9107-774db34b330c.png)


---

## 智谱大模型接入 Claude Code

这部分我们使用 ~/.claude/settings.json 文件来配置大模型，开始前需要到官方平台获取 API key：[GLM Coding Plan](https://www.bigmodel.cn/claude-code?ic=EMWK7IPUCE)。


编辑或新增 Claude Code 配置文件 ~/.claude/settings.json ，新增或修改里面的 env 字段


```
# 注意替换里面的your_zhipu_api_key 为您上一步获取到的 API Key
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "your_zhipu_api_key",
        "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",
        "API_TIMEOUT_MS": "3000000",
        "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": 1
    }
}
```


运行 claude 启动 Claude Code，输入 **/status** 确认模型状态：


![](https://www.runoob.com/wp-content/uploads/2025/12/5617ff6d-7997-4819-a2eb-300346548c61.png)


如果不是可以输入 **/config** 来切换模型。


![](https://www.runoob.com/wp-content/uploads/2025/12/98fa9dc0-efab-4afc-a100-350ad114937c.png)


**
大模型一多，配置起来就麻烦，可以使用第三方工具 CC Switch 可以帮我们轻松管理这几个热门工具的 API 配置：[https://github.com/farion1231/cc-switch/](https://github.com/farion1231/cc-switch/)，Windows / macOS / Linux 全支持。


![](https://www.runoob.com/wp-content/uploads/2025/12/claude-code-ccswitch.png)


各平台安装包下载地址：[https://github.com/farion1231/cc-switch/releases](https://github.com/farion1231/cc-switch/releases)。


![](https://www.runoob.com/wp-content/uploads/2025/12/claude-code-runoob2.png)


---


## VS Code 安装 Claude Code

如果不喜欢使用 Claude Code 的命令行模型，我们可以在 VS Code 编辑器中安装 Claude Code。


打开 VS Code，进入扩展市场，搜索 Claude Code** 安装：


![](https://www.runoob.com/wp-content/uploads/2025/12/cc-runoob-1.png)


安装完成后，点击右上角 Claude Code 图标，即可进入 Claude Code 页面：


![](https://www.runoob.com/wp-content/uploads/2025/12/cc-runoob-2.png)


这样有账号的可以使用 /login 登录：


![](https://www.runoob.com/wp-content/uploads/2025/12/cc-runoob-3.png)

也可以在对话框输入 /config 进入设置，勾选 Disable Login Prompt 配置来关闭登录页面:


![](https://www.runoob.com/wp-content/uploads/2025/12/cc-runoob-4.png)


---


## 相关命令参考


### Claude Code 内置命令列表


| 命令 | 说明 |
| --- | --- |
| /add-dir | 添加额外的工作目录 |
| /agents | 管理专用 AI 子代理 |
| /bashes | 列出和管理后台任务 |
| /bug | 报告 bug(将对话发送给 Anthropic) |
| /clear | 清除对话历史 |
| /compact [指令] | 压缩对话,可选择性添加重点指令 |
| /config | 打开设置界面(配置选项卡) |
| /context | 以彩色网格可视化当前上下文使用情况 |
| /cost | 显示 token 使用统计 |
| /doctor | 检查 Claude Code 安装健康状况 |
| /exit | 退出 REPL |
| /export [文件名] | 导出当前对话到文件或剪贴板 |
| /help | 获取使用帮助,显示所有可用命令 |
| /hooks | 管理工具事件的钩子配置 |
| /ide | 管理 IDE 集成并显示状态 |
| /init | 使用 CLAUDE.md 指南初始化项目 |
| /install-github-app | 为仓库设置 Claude GitHub Actions |
| /login | 切换 Anthropic 账户 |
| /logout | 从 Anthropic 账户登出 |
| /mcp | 管理 MCP 服务器连接和 OAuth 认证 |
| /memory | 编辑 CLAUDE.md 记忆文件 |
| /model | 选择或更改 AI 模型 |
| /output-style [样式] | 直接设置输出样式或从选择菜单中选择 |
| /permissions | 查看或更新权限 |
| /plugin | 管理 Claude Code 插件 |
| /pr-comments | 查看 PR 评论 |
| /privacy-settings | 查看和更新隐私设置 |
| /release-notes | 查看发布说明 |
| /resume | 恢复对话 |
| /review | 请求代码审查 |
| /rewind | 回退对话和/或代码 |
| /sandbox | 启用沙盒 bash 工具,具有文件系统和网络隔离 |
| /security-review | 对当前分支的待处理更改进行安全审查 |
| /status | 打开设置界面(状态选项卡),显示版本、模型、账户和连接状态 |
| /statusline | 设置 Claude Code 的状态行 UI |
| /terminal-setup | 安装 Shift+Enter 换行键绑定(仅限 iTerm2 和 VSCode) |
| /todos | 列出当前待办事项 |
| /usage | 显示计划使用限制和速率限制状态(仅订阅计划) |
| /vim | 进入 vim 模式,交替插入和命令模式 |


### 自定义命令类型


| 命令类型 | 位置 | 说明 |
| --- | --- | --- |
| 项目命令 | .claude/commands/ | 存储在仓库中,与团队共享 |
| 个人命令 | ~/.claude/commands/ | 跨所有项目可用 |
| 插件命令 | 插件的 commands/ 目录 | 通过插件市场分发 |
| MCP 命令 | 由 MCP 服务器提供 | 格式: /mcp____ |


### Shell 命令(非会话中)


| 命令 | 说明 |
| --- | --- |
| claude | 启动 Claude Code 交互式会话 |
| claude -p "查询" | 非交互模式,打印结果后退出 |
| claude --dangerously-skip-permissions | 跳过所有权限检查(危险模式) |
| claude --debug | 启用调试模式 |
| claude --mcp-debug | MCP 调试模式 |
| claude mcp add | 添加 MCP 服务器 |
| claude mcp list | 列出已配置的 MCP 服务器 |
| claude mcp remove | 移除 MCP 服务器 |


### 特殊功能


**自定义命令支持:**


- `$ARGUMENTS` - 捕获所有参数
- `$1, $2, $3...` - 访问单个位置参数
- `@文件名` - 引用文件内容
- `!命令` - 执行 bash 命令并包含输出


**命令前置元数据(Frontmatter):**


- `allowed-tools` - 命令可使用的工具列表
- `argument-hint` - 参数提示说明
- `description` - 命令简短描述
- `model` - 指定模型
- `disable-model-invocation` - 防止 SlashCommand 工具调用


更多相关信息可以通过 `/help` 查看完整的可用命令列表(包括您自定义的命令)。


---


## 相关资源



- Claude Code 教程：[https://www.runoob.com/claude-code/claude-code-tutorial.html](https://www.runoob.com/../claude-code/claude-code-tutorial.html)
- 开源地址：[https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)
- 官方文档：[https://code.claude.com/docs/zh-CN/overview](https://code.claude.com/docs/zh-CN/overview)
- DeepSeek Anthropic API：[https://api-docs.deepseek.com/zh-cn/guides/anthropic_api](https://api-docs.deepseek.com/zh-cn/guides/anthropic_api)
- 智谱大模型接入 Claude Code：[https://docs.bigmodel.cn/cn/coding-plan/tool/claude#claude-code](https://docs.bigmodel.cn/cn/coding-plan/tool/claude#claude-code)










	  AI 思考中...





			** [LangChain 制作智能体](https://www.runoob.com/langchain-agent.html)
			[OpenCode 入门教程](https://www.runoob.com/opencode-coding-agent.html) **













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