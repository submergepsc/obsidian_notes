# Claude Code Skills 使用实例

- Source: https://www.runoob.com/claude-code/claude-code-ui-ux-pro-max-skill.html

在上一章节 [Agent Skills（智能体技能）](https://www.runoob.com/claude-agent-skills.html) 中我们已经了解了 Skills 的基本概念，本章节我们将结合一个具体的 Skills 来开发一个项目。


**
现在市面上已经有很多现成的 skills，我么可以直接拿来使用，我们可以在 [https://skills.sh/](https://skills.sh/) 查找更多的 skill。


安装方式：


```
npx skills add <owner/repo>
```


npx 安装 ui-ux-pro-max 可参考：[OpenCode skills 使用](https://www.runoob.com/../ai-agent/opencode-skills-intro.html)。

注：**如果对 npx 不了解，可以参阅：[npx 入门教程](https://www.runoob.com/../nodejs/npx-intro.html)


本章节我们将介绍一个支持多平台、多框架的专业级 UI/UX SKILL 插件 - UI UX Pro Max。

UI UX Pro Max 旨在为跨平台和多框架开发提供专业的 UI/UX 设计智能支持。


UI UX Pro Max 本质上是一个可检索的设计数据库，包含样式、色板、字体、组件建议及 UX 准则，专门喂给 Cursor、Claude Code、Windsurf等这些 AI 编码助手。


** 核心亮点：**


- 67 种 UI 风格（从 Minimalism 到 Brutalism、Glassmorphism、Bento Grid、AI-Native 等）
- 96 个行业调色盘（SaaS、Fintech、Healthcare、Beauty、EdTech…）
- 57 组字体搭配（Google Fonts 精选组合）
- 25 种常用图表类型（适合 dashboard）
- 99 条 UX 指导原则（包含可访问性、性能、交互规范）
- 100 条行业专项推理规则（包含反面模式 Anti-patterns）
- 支持 13 个技术栈：React / Next.js / Vue / Tailwind / Flutter / SwiftUI / HTML+CSS / Electron 等

**工作原理：**


- 提出需求：构建、设计、实现、优化或评审 UI / UX
- 技能自动触发：AI 会在内部搜索 UI 风格、配色、字体和 UX 规范数据库
- 智能设计推荐：根据产品类型与使用场景匹配合适的设计体系
- 直接生成代码：按最佳实践输出包含正确配色、字体、间距和结构的 UI 实现


开源地址：[https://github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)


官方文档：[https://ui-ux-pro-max-skill.nextlevelbuilder.io/](https://ui-ux-pro-max-skill.nextlevelbuilder.io/)


### 安装方式

1、通过 Claude Marketplace（Claude Code）安装


在 Claude Code 中执行以下两条命令即可直接安装。


注册插件市场源：


```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
```


![](https://www.runoob.com/wp-content/uploads/2026/01/5cd82658-5a31-4653-ad1d-e8b0d7335744.png)


安装插件：


```
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```


安装成功后重启 Claude Code 就可以使用了:


![](https://www.runoob.com/wp-content/uploads/2026/01/a818e0e6-b4f9-437f-8031-8fc4fb2c25c9.png)


2、使用 CLI（推荐）


全局安装 CLI：


```
npm install -g uipro-cli

# 进入你的项目目录
cd /path/to/your/project

# 为对应 AI 助手安装
uipro init --ai claude      # Claude Code
uipro init --ai cursor      # Cursor
uipro init --ai windsurf    # Windsurf
uipro init --ai antigravity # Antigravity (.agent + .shared)
uipro init --ai copilot     # GitHub Copilot
uipro init --ai kiro        # Kiro
uipro init --ai codex       # Codex CLI
uipro init --ai qoder       # Qoder
uipro init --ai roocode     # Roo Code
uipro init --ai gemini      # Gemini CLI
uipro init --ai trae        # Trae
uipro init --ai all         # 所有助手
```


3、其他 CLI 命令：


```
uipro versions              # 查看可用版本
uipro update                # 更新到最新版本
uipro init --version v1.0.0 # 安装指定版本
```


2、使用 npx


```
npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max
```


5、安装指定版本

安装完后，假设在 Claude 中使用，执行以下命令：


```
uipro init --ai claude
```


**
搜索脚本需要使用 Python 3.x：


```
# 查看 Python  是否已经安装
python3 --version

# macOS
brew install python3

# Ubuntu/Debian
sudo apt update && sudo apt install python3

# Windows
winget install Python.Python.3.12
```


安装完成后输出如下：


![](https://www.runoob.com/wp-content/uploads/2026/01/ui-ux-pro-runoob.webp)


然后启用输入命令进入 Claude：


```
claude
```


我们可以使用 **/plugin** 命令查看已经安装的创建：


![](https://www.runoob.com/wp-content/uploads/2026/01/15b4de08-8b55-40eb-81f3-4b6eec604738.png)


按 **Esc** 按键退出。


注意：通过插件安装的 Skill，目录放在 **～/.claude/plugins/marketplaces**。


---


## 如何使用


接下来我们就可以直接输入需求：



```
为宠物美容服务搭建一个着陆页，风格活泼亲和，并设置预约类行动召唤按钮。
```


会提示是否使用我们安装的 skill 来设计，一路回车就好了：


![](https://www.runoob.com/wp-content/uploads/2026/01/6832cf20-057a-40d9-8693-06f205d1777e.png)


一路回车就好了，会提示完成的功能：


![](https://www.runoob.com/wp-content/uploads/2026/01/89a8159c-41bb-454a-b63e-0c743ee5d23d.png)


然后查看最终效果，好看很多：


![](https://www.runoob.com/wp-content/uploads/2026/01/a9d18e1c-ae82-4dfa-bb9f-f7fe30a01cb7-scaled.png)









	  AI 思考中...





			** [Claude Code 操作说明](https://www.runoob.com/claude-code-symbols.html)
			[VS Code 安装 Claude Code](https://www.runoob.com/vscode-install-claude-code.html) **













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