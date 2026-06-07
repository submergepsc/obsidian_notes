# OpenClaw 配置目录

- Source: https://www.runoob.com/ai-agent/openclaw-setup.html

OpenClaw（也称 Clawdbot）的所有配置、状态数据、工作区和技能均集中在用户主目录下的 ~/.openclaw/（Linux/macOS）或 %USERPROFILE%\.openclaw\（Windows）这个核心目录中。


**~/.openclaw/** 是整个系统的根配置目录，首次安装/运行 **openclaw onboard** 或 **openclaw onboard --install-daemon** 时会自动创建。


```
~/.openclaw/
├── openclaw.json                 # 主配置文件（JSON/JSON5）
├── workspace/                    # 你的 AI “灵魂”文件夹（推荐 git 版本控制）
│   ├── SOUL.md                   # 人格设定（语气、风格）
│   ├── USER.md                   # 你的个人信息（让 AI 更懂你）
│   ├── MEMORY.md                 # 长期记忆（手动可编辑）
│   ├── IDENTITY.md               # Agent 名称、形象
│   ├── AGENTS.md                 # 多 Agent 路由规则
│   ├── BOOT.md                   # 启动提示词
│   ├── HEARTBEAT.md              # 每日检查清单
│   └── skills/                   # 已安装技能（每个技能一个子文件夹）
├── agents/<cid>/                 # 每个 Agent 的独立状态
├── memory/<cid>.sqlite           # 向量记忆库
├── credentials/                  # API Key、OAuth（旧版）
├── skills/                       # 全局技能包
└── secrets.json                  # 加密凭证（可选）
```


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-setup-runoob-2.svg)


**最重要文件**：


- `openclaw.json`：全局设置（模型、渠道、端口、安全策略）
- `workspace/` 下所有 `.md` 文件：**直接用 VS Code 编辑即可实时生效**！


查看/修改配置命令：


```
openclaw configure      # 交互式配置向导
openclaw config file          # 显示完整路径
openclaw config get agent.model
openclaw config set agent.model "anthropic/claude-3-5-sonnet"
openclaw config validate      # 校验合法性
```


| 路径 | 用途说明 |
| --- | --- |
| ~/.openclaw/openclaw.json | 主配置文件（最重要！）存储全局设置（模型、Gateway 模式、绑定地址、Agents 默认值、插件等）。可用命令查看/修改：• openclaw config file（显示完整路径）• openclaw config get • openclaw config set |
| ~/.openclaw/workspace/ | 默认工作区（Agent 的"灵魂"所在地）存放以下 Markdown 文件（可直接编辑生效）：• SOUL.md：AI 人格/语气设定• USER.md：你的个人偏好和背景• MEMORY.md：长期记忆记录• AGENTS.md：指令说明• IDENTITY.md：名称/主题• BOOT.md：启动配置• HEARTBEAT.md：定期检查清单 |
| ~/.openclaw/agents// | 单个智能体（Agent）的状态目录（ 为实例 ID） |
| ~/.openclaw/agents//agent/auth-profiles.json | API Key & OAuth 凭证（新版推荐位置）旧版可能在 ~/.openclaw/credentials/ |
| ~/.openclaw/memory/.sqlite | 向量索引存储（记忆搜索用） |
| ~/.openclaw/skills/ | 全局技能目录通过 openclaw skills install 或 clawhub install 安装的技能包均放在这里（每个技能是一个子文件夹，内含 SKILL.md） |
| ~/.openclaw/memory/ | 长期记忆相关文件（SQLite + 向量嵌入） |
| /tmp/openclaw/*.log | Gateway 服务日志（调试用） |


### 1. 主配置文件


**路径:** `~/.openclaw/openclaw.json`


**说明:** OpenClaw 的核心配置文件,包含所有系统级设置。


**主要配置项:**


- **gateway** - 网关服务配置 `mode`: 网关模式(如 "local")
- `port`: 网关端口号(默认 18789)
- `bind`: 绑定地址(默认 127.0.0.1)
- `token`: 访问令牌,用于 Web UI 认证


    **models** - AI 模型配置
- 默认模型设置
- API 认证信息


    **messages** - 消息处理配置
- TTS(文本转语音)设置
- 消息格式配置




**示例配置片段:**


```
{
  "gateway": {
    "mode": "local",
    "port": 18789,
    "bind": "127.0.0.1",
    "token": "c9917c5a066beeb26266d09baed99495e7563b33c771e89a"
  }
}
```


**操作建议:**


- 首次安装后通过 `openclaw onboard` 向导自动生成
- 修改配置后需重启网关服务生效
- token 值用于 Web UI 访问,请妥善保管


### 2. 工作区目录


**路径:** `~/.openclaw/workspace/`


**说明:** OpenClaw 的默认工作目录,所有 AI 生成的文件、临时文件和用户请求的输出文件都保存在此。


**主要用途:**


- AI 智能体读写文件的默认位置
- 代码执行输出存储
- 文档生成和编辑
- 临时数据存储


**权限说明:**


- 默认情况下,AI 只能访问此目录及其子目录
- 若需访问其他路径,需要配置 `filesystem-mcp` 技能并授予额外权限
- Windows 用户可能需要将文件从工作区复制到其他位置


**使用建议:**


- 定期清理不需要的临时文件
- 重要输出建议备份到工作区外
- 可以在此建立项目子目录进行组织管理


### 3. 智能体状态目录


**路径:** `~/.openclaw/agents//`


**说明:** 每个会话(Conversation)的智能体状态和配置存储目录。`` 是会话 ID,每个会话都有独立的配置空间。


**目录结构:**


```
~/.openclaw/agents/<cid>/
├── agent/
│   ├── auth-profiles.json    # 该会话的 OAuth 和 API 密钥
│   └── ...
└── ...
```


**auth-profiles.json 说明:**


- 存储该智能体使用的 API 认证信息
- 包含各个服务的 OAuth token
- 新版本使用此路径,旧版本存储在 `~/.openclaw/credentials/`


**数据隔离:**


- 每个会话的认证信息相互独立
- 可以为不同会话配置不同的 API 密钥
- 支持多智能体并行运行


### 4. 认证凭据目录(旧版)


**路径:** `~/.openclaw/credentials/`


**说明:** 旧版本 OpenClaw 的凭据存储位置。


**迁移说明:**


- 新版本已迁移至 `~/.openclaw/agents//agent/auth-profiles.json`
- 旧版本用户升级后,凭据可能需要重新配置
- 建议使用 `openclaw models auth setup` 重新设置


### 5. 记忆存储目录


**路径:** `~/.openclaw/memory/`


**说明:** OpenClaw 的持久化记忆系统存储位置,包含向量索引和对话历史。


**主要文件:**


- **`.sqlite`** - 向量索引数据库 存储对话的语义向量
- 支持语义搜索功能
- 用于长期记忆检索




**`YYYY-MM-DD.md`** - 每日对话日志


- 以日期命名的 Markdown 文件
- 记录当天所有对话内容
- 便于人工查看和归档




**记忆功能:**


- **向量搜索:** 使用 `memory search "关键词"` 搜索历史对话
- **上下文关联:** 支持跨会话的上下文理解
- **长期记忆:** 智能体会"记住"用户的偏好和习惯


**维护建议:**


- 定期备份 memory 目录
- 大型数据库可能影响性能,可考虑定期归档
- 日志文件可用于审计和问题排查


### 6. 技能目录


**路径:** `~/.openclaw/skills/`


**说明:** 全局共享技能(Skills)的安装位置。技能是扩展 OpenClaw 功能的插件。


**技能管理:**


- **安装技能:** `npx clawhub install `
- **列出技能:** `openclaw skills list`
- **搜索技能:** `npx clawhub search `


**常用技能示例:**


- `filesystem-mcp` - 文件系统操作
- `github` - GitHub 集成
- `nano-pdf` - PDF 编辑
- `notion` / `obsidian` - 笔记同步
- `weather` - 天气查询
- `summarize` - 内容摘要生成


**技能生态:**


- 社区技能库 ClawHub 提供 500+ 技能
- 支持自定义技能开发
- 技能可访问外部 API 和系统资源


**配置说明:**


- 每个技能可能需要单独的 API Key 配置
- 部分技能依赖系统工具(如 GitHub CLI)
- macOS 专有技能在 Windows/Linux 上不可用


### 7. 网关日志目录


**路径:** `/tmp/openclaw/*.log`


**说明:** 网关服务的运行日志,存储在系统临时目录。


**日志类型:**


- 网关启动/停止日志
- API 请求/响应日志
- 错误和异常日志
- 性能监控信息


**日志管理:**


- 临时目录的日志可能在系统重启后清除
- 使用 `openclaw gateway --verbose` 可以查看详细日志
- 排查问题时应首先检查日志文件


**网关服务管理:**


```
openclaw gateway start    # 启动网关
openclaw gateway status   # 查看状态
openclaw gateway stop     # 停止网关
```


---


## 其他重要文件


### USER.md


**路径:** 通常位于工作区或用户自定义位置


**说明:** 用户信息文件,包含关于用户的个性化信息,帮助 AI 更好地理解用户需求。


**内容示例:**


- 用户偏好设置
- 常用工作流程
- 项目背景信息
- 自定义指令

---


## 配置文件管理最佳实践


### 1. 备份策略


**关键目录备份:**


```
# 备份整个配置目录
tar -czf openclaw-backup-$(date +%Y%m%d).tar.gz ~/.openclaw/

# 仅备份核心配置
cp ~/.openclaw/openclaw.json ~/backups/
cp -r ~/.openclaw/memory/ ~/backups/memory/
```


**建议备份频率:**


- 主配置文件:每次修改后
- 记忆数据库:每周一次
- 技能配置:安装新技能后


### 2. 安全建议


**敏感信息保护:**


- `openclaw.json` 包含网关 token,不应公开
- `auth-profiles.json` 包含 API 密钥,需加密保护
- 定期更换 API 密钥
- 不要将配置文件提交到版本控制系统


**权限设置:**


```
# 确保配置目录仅用户可访问
chmod 700 ~/.openclaw/
chmod 600 ~/.openclaw/openclaw.json
chmod 600 ~/.openclaw/agents/*/agent/auth-profiles.json
```


### 3. 迁移和升级


**版本升级注意事项:**


- 升级前备份整个 `~/.openclaw/` 目录
- 检查 release notes 了解配置变更
- 旧版本凭据可能需要迁移


**跨设备同步:**


- 可以同步配置文件实现多设备一致性
- 注意路径差异(Windows vs Unix)
- 敏感信息建议独立配置


### 4. 故障排查


**配置问题诊断:**


```
# 检查配置文件语法
cat ~/.openclaw/openclaw.json | json_pp

# 深度检查
openclaw doctor --deep

# 查看网关状态
openclaw gateway status
```


**常见问题:**


- **认证失效:** 运行 `openclaw models auth setup` 重新配置
- **网关无法启动:** 检查端口占用,查看日志文件
- **技能无法使用:** 确认技能依赖已安装,检查 API 密钥

---


## 环境变量配置


OpenClaw 支持通过环境变量进行配置:


```
# API 密钥环境变量
export ANTHROPIC_API_KEY="your-key-here"
export OPENAI_API_KEY="your-key-here"
export DEEPSEEK_API_KEY="your-key-here"

# 自定义配置目录
export OPENCLAW_HOME="~/custom-path/.openclaw"
```


**环境变量优先级:**


- 环境变量中的 API Key 会被 onboard 向导自动检测
- 可以覆盖配置文件中的默认值
- 适合 CI/CD 环境和容器化部署

---


## 网络和部署配置


### 本地部署


**默认配置:**


- 绑定地址: 127.0.0.1(仅本机访问)
- 网关端口: 18789


**访问方式:**


```
http://127.0.0.1:18789/#token=<your-token>
```


### 云端部署


OpenClaw 支持部署在云服务器上:


**支持平台:**


- 阿里云:[https://www.aliyun.com/activity/ecs/clawdbot](https://www.aliyun.com/activity/ecs/clawdbot?userCode=i5mn5r7m)
- 腾讯云：[https://cloud.tencent.com/developer/article/2624973](https://cloud.tencent.com/act/cps/redirect?redirect=37925&cps_key=4537fb0f9e70f157220dafdec0f9c750)
- 1Panel
- Docker 容器


**云端配置特点:**


- 需要配置公网访问权限
- 可能需要配置防火墙规则
- 支持域名绑定和 SSL 证书

---


## 集成平台配置


OpenClaw 支持多种即时通讯平台:


### 支持的平台


- **国外:** WhatsApp, Telegram, Discord, Slack, iMessage
- **国内:** 飞书, 钉钉


### 配置位置


聊天渠道配置存储在 `openclaw.json` 中,包含:


- 渠道类型(Slack/飞书等)
- 认证 Token
- 频道白名单/黑名单
- 响应模式(DM/群聊)


### 配置管理


```
# 添加新渠道
openclaw channels add

# 列出已配置渠道
openclaw channels list

# 配对管理
openclaw pairing list
openclaw pairing approve <platform> <code>
```









	  AI 思考中...





			** [OpenClaw 工作原理](https://www.runoob.com/openclaw-how-it-works.html)
			[CC Switch 一键切换 API](https://www.runoob.com/cc-switch.html) **













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