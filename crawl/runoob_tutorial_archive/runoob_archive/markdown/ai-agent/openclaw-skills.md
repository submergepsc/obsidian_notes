# OpenClaw Skills -- ClawHub

- Source: https://www.runoob.com/ai-agent/openclaw-skills.html

OpenClaw Skills 是包含指令代码的 Markdown 文件，用于帮助 Agent 执行特定任务或优化工作流功能。


真正让 OpenClaw 从聊天机器人变成超级助手的，其实是它的 Skills 生态 —— 相当于 AI 的 App Store。


简单理解：


```
OpenClaw = iPhone 手机
Skills = App Store
```


没有 Skill 的 AI 只能聊天，有 Skill 的 AI 才能 搜索、自动化、操作系统、调用 API、执行脚本。


一个典型的 Skill 目录结构如下：


```
my-skill/
├── SKILL.md        # 主说明文件（含 YAML frontmatter + Markdown 指令）
├── script.py       # 可选：Skill 依赖的脚本
└── config.json     # 可选：配置文件
```


更多 skills 内容可以参考：[https://www.runoob.com/ai-agent/skills-agent.html](https://www.runoob.com/skills-agent.html)


---


## ClawHub -- 安装与使用 Skills

ClawHub 是 OpenClaw 的 Skills 市场，可以把它理解成 OpenClaw 的 App Store。


OpenClaw 的 App Store 叫 ClawHub -- [https://clawhub.ai/](https://clawhub.ai/) ，目前已经汇聚了上万个社区 Skills。


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-skills-runoob-1.png)


**类比：**


```
OpenClaw = 操作系统

Agent = 大脑

ClawHub = 应用商店
```


ClawHub 是 OpenClaw 的公共技能注册表，用于发现、安装、更新和备份 Skills。


- 官方地址：[https://clawhub.ai/](https://clawhub.ai/)
- 国内镜像地址（速度更快）：[https://skillhub.tencent.com/](https://skillhub.tencent.com/)


ClawHub 提供功能：



- 浏览 Skills
- 搜索 Skills
- 安装 Skills
- 更新 Skills
- 发布 Skills


执行过程：


```
用户提需求 → Agent 做决策 → ClawHub 找工具 → Skill 去执行 → 返回结果
```


![](https://www.runoob.com/wp-content/uploads/2026/03/runoob-clawhub-scaled.png)


### 第一步：安装 ClawHub CLI


```
npm i -g clawhub
clawhub --version
```


### 第二步：搜索并安装 Skill


```
# 搜索 Skill（支持自然语言）
clawhub search "send emails automatically"

# 安装 Skill
clawhub install <slug>
```


默认情况下，CLI 会把 Skill 安装到当前工作目录下的 ./skills 文件夹。

如果配置了 OpenClaw workspace，clawhub 会回退到该 workspace，除非你通过 --workdir 参数或 CLAWHUB_WORKDIR 环境变量覆盖路径。

OpenClaw 会从 /skills 加载 Skill，并在下一个 Session 中生效。


### 第三步：重启 OpenClaw Session


```
openclaw chat
# 新 Session 启动后，Skill 自动加载生效
```


更新 Skill:


```
clawhub sync     # 更新当前 workdir 下的所有 Skill
```


### 使用国内镜像


国内镜像地址 [https://skillhub.tencent.com/](https://skillhub.tencent.com/)，用这个安装速度更快。


![](https://www.runoob.com/wp-content/uploads/2026/03/openclaw-skills-runoob-2.png)


在终端中执行以下命令，即可安装 SkillHub CLI，并且优先采用 SkillHub 加速安装技能：


```
curl -fsSL https://skillhub-1388575217.cos.ap-guangzhou.myqcloud.com/install/install.sh | bash
```


比如我们安装搜索功能：


```
skillhub install tavily-search
```


安装完成后，我们可以再后台看到该 Skill 已安装：


![](https://www.runoob.com/wp-content/uploads/2026/03/31d4bf49-b6a9-4c71-ac6b-b249c2f8fc5f.png)


---


## 常用 Skills

如果你刚上手OpenClaw，强烈建议的安装顺序是：


- 先装 Skill Vetter 保底安全
- 再装 self-improving-agent 或其变种，让AI开始长记性
- 根据需求补 Summarize / Agent Browser / Gog / Github / Multi Search Engine 这几个万金油


安装方式超级简单：


1、先安装 clawhub CLI


```
npm i -g clawhub
```


2、然后安装这些 Skills：


```
clawhub install self-improving-agent
clawhub install summarize
# 批量更新全部
clawhub update --all
```


常用的 Skills 列表如下：


| # | Skill | 说明 | 适用场景 | 安装 |
| --- | --- | --- | --- | --- |
| 1 | self-improving-agent | 记录失败与纠正并复盘优化 | 失败复盘 / 多次出错 / 用户纠正 | clawhub install self-improving-agent |
| 2 | summarize | 多格式内容总结（网页/PDF/视频等） | 长文阅读 / 文档提炼 | clawhub install summarize |
| 3 | agent-browser | 自动浏览器操作（点/输/抓） | 爬取 / 表单 / 自动化 | clawhub install agent-browser |
| 4 | skill-vetter | 安装前安全检测 | 检测权限 / 风险插件 | clawhub install skill-vetter |
| 5 | github | 通过 gh 操作 GitHub | PR / Issue / CI | clawhub install github |
| 6 | gog | Google Workspace 集成 | 邮件 / 文档 / 表格 | clawhub install gog |
| 7 | ontology | 结构化知识图谱记忆 | 项目 / 多任务管理 | clawhub install ontology |
| 8 | proactive-agent | 主动执行与调度 | 定时任务 / 自动执行 | clawhub install proactive-agent |
| 9 | multi-search-engine | 多引擎搜索聚合 | 调研 / 对比 | clawhub install multi-search-engine |
| 10 | humanizer | 优化文本更自然 | 文案 / 润色 | clawhub install humanizer |
| 11 | nano-pdf | 自然语言编辑 PDF | 合同 / 文档修改 | clawhub install nano-pdf |
| 12 | notion | 管理页面与数据库 | 笔记 / 知识库 | clawhub install notion |
| 13 | obsidian | Markdown 笔记自动化 | 整理 / 沉淀 | clawhub install obsidian |
| 14 | api-gateway | 连接 100+ API | 系统集成 | clawhub install api-gateway |
| 15 | automation-workflows | 设计执行自动化流程 | 副业 / 自动化 | clawhub install automation-workflows |
| 16 | auto-updater | 自动更新 Skills | 长期运行 | clawhub install auto-updater |
| 17 | openai-whisper | 本地语音转文字 | 会议记录 | clawhub install openai-whisper |
| 18 | nano-banana-pro | 图像生成与编辑 | 海报 / 图片 | clawhub install nano-banana-pro |
| 19 | stock-analysis | 股票与加密分析 | 趋势 / 分析 | clawhub install stock-analysis |
| 20 | weather | 天气查询与预测 | 日常查询 | clawhub install weather |


---


## 制作自己的 Skill

下面是一个最简单的 SKILL.md 示例：


```
---
name: my-skill
description: Does a thing with an API.
---

# My Skill

## Rules
- Always confirm with the user before making destructive changes.
- Use the credentials from environment variable MY_API_KEY.

## Usage
When the user asks to "do the thing", call the API endpoint at
https://api.example.com/action with the provided payload.
```


写好后，执行发布命令：


```
clawhub publish ~/.openclaw/skills/my-skill \
  --slug my-skill \
  --name "My Skill" \
  --version 1.0.0 \
  --tags latest
```


发布需要一个至少注册满一周的 GitHub 账号。--slug 是 Skill 在 ClawHub 上的唯一标识符，在整个注册表中必须唯一。








	  AI 思考中...





			** [QoderWork 教程](https://www.runoob.com/qoderwork.html)
			[OpenClaw 卸载指南](https://www.runoob.com/openclaw-uninstall.html) **













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