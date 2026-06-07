# CC Switch 一键切换 API

- Source: https://www.runoob.com/ai-agent/cc-switch.html

随着 Claude Code、OpenAI Codex、Gemini CLI 等 AI 编程工具的流行，开发者往往需要在多个 API 提供商之间频繁切换——官方 API、国内镜像、第三方代理……每次手动修改配置文件既繁琐又容易出错。


CC Switch 就是解决这个痛点的桌面工具，它提供一个统一的图形界面，让你可以：


| 功能 | 说明 |
| --- | --- |
| 🔄 一键切换 Provider | 保存多套 API 配置，点一下即可切换，无需手动编辑 JSON |
| 🖥️ 多应用统一管理 | 同时管理 Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw 五款工具 |
| 🛡️ 本地 API 代理 | 内置高性能 HTTP 代理，支持自动故障转移与请求监控 |
| 🔌 MCP 服务器管理 | 可视化添加、编辑和同步 MCP 服务器配置 |
| 📊 用量统计 | 实时查看 Token 消耗与 API 费用 |
| 💾 备份与恢复 | 自动备份配置，防止误操作导致数据丢失 |


### 支持管理的应用


- 🤖 **Claude Code**（Anthropic）
- ⚡ **Codex**（OpenAI）
- ✨ **Gemini CLI**（Google）
- 🧩 **OpenCode**（开源）
- 🦅 **OpenClaw**（第五款应用，v3.11.0 新增）


---


## 安装


前往 [GitHub Releases: https://github.com/farion1231/cc-switch/releases/latest](https://github.com/farion1231/cc-switch/releases/latest) 下载对应平台的安装包。

拉到网页最底部，资源包部分，下载对应平台的安装包：


![](https://www.runoob.com/wp-content/uploads/2026/03/31595d37-9f05-4d9d-90d9-c17c2b119da6.png)


### 系统要求


| 系统 | 最低版本 | 架构 |
| --- | --- | --- |
| Windows | Windows 10 及以上 | x64 |
| macOS | macOS 10.15 (Catalina) 及以上 | Intel (x64) / Apple Silicon (arm64) |
| Linux | 见下表 | x64 / arm64 |


### Windows


| 文件 | 说明 |
| --- | --- |
| CC-Switch-vX.X.X-Windows.msi | ✅ 推荐——MSI 安装包，支持自动更新 |
| CC-Switch-vX.X.X-Windows-Portable.zip | 便携版，解压即用，不写注册表 |


双击 MSI 文件，按向导完成安装后，在开始菜单搜索"CC Switch"启动即可。

**

⚠️ Windows 版本已禁用"一键安装"功能，以避免协议处理器的副作用。如需安装 Claude Code 等工具，请手动安装后再通过 CC Switch 管理。


### macOS


方式一：直接下载（推荐）**


- 下载 `CC-Switch-vX.X.X-macOS.zip`
- 解压后将 `CC Switch.app` 拖入「应用程序」文件夹
- 首次启动时右键点击 → 打开，或前往「系统设置 → 隐私与安全性 → 仍要打开」

**

⚠️ 由于作者没有 Apple 开发者账号，macOS 可能提示"未知开发者"。关闭提示后，前往「系统设置 → 隐私与安全性」点击「仍要打开」，之后每次均可正常启动。


方式二：Homebrew**


```
# 添加 tap 并安装
brew tap farion1231/ccswitch
brew install --cask cc-switch
# 更新
brew upgrade --cask cc-switch
```


### Linux


根据发行版选择对应格式：


| 发行版 | 推荐格式 | 安装命令 |
| --- | --- | --- |
| Ubuntu / Debian / Mint | .deb | sudo apt install ./CC-Switch-*.deb |
| Fedora / RHEL / Rocky | .rpm | sudo dnf install ./CC-Switch-*.rpm |
| openSUSE | .rpm | sudo zypper install ./CC-Switch-*.rpm |
| Arch / Manjaro / 其他 | .AppImage | 见下方 |


AppImage 使用方式：


```
chmod +x CC-Switch-*.AppImage
./CC-Switch-*.AppImage
```


---


## 快速上手


安装完成后，按以下步骤完成首次配置：


**第一步：启动 CC Switch**


首次启动时，CC Switch 会自动检测已安装的 CLI 工具并尝试导入现有配置，系统托盘中会出现 CC Switch 图标。


**第二步：选择要管理的应用**


主界面顶部是应用切换栏，点击对应图标（Claude Code / Codex / Gemini CLI 等）即可切换当前管理的应用，你可以在设置中隐藏不需要的应用。


![](https://www.runoob.com/wp-content/uploads/2026/03/3f634726-617d-43a7-9040-a4acaaca9433.png)


**第三步：添加第一个 Provider**


点击右上角的 **+** ，从内置预设中选择（如官方 Anthropic API、DeepSeek、阿里百炼等），或手动填写以下信息：


![](https://www.runoob.com/wp-content/uploads/2026/03/6e4e3a28-1f43-446a-a939-c08eb195ba43.png)


- **名称**：便于区分的备注名
- **API Key**：服务商提供的密钥
- **Base URL**（可选）：自定义代理地址
- **模型**：指定默认使用的模型名称
- **API 格式**：Anthropic Messages 原生格式 或 OpenAI Chat Completions 兼容格式


![](https://www.runoob.com/wp-content/uploads/2026/03/11305e0d-1ca7-46f6-83d6-cec24c4f46bd.png)


**第四步：切换 Provider**


在列表中点击目标 Provider，再点击「启用」，CC Switch 会自动将配置写入对应 CLI 工具的配置文件:


![](https://www.runoob.com/wp-content/uploads/2026/03/0d05c29d-f2c4-4c42-8afc-88ed80937a30.png)


在终端直接运行 `**claude**` 命令时，即会使用新配置。


**第五步：验证配置（可选）**


点击 Provider 旁的「健康检查」按钮，发送一个测试请求验证 API Key 和网络连通性。


![](https://www.runoob.com/wp-content/uploads/2026/03/a0a56b4b-ee98-42db-8e26-13a46b112455.png)

**

💡 按 `Cmd/Ctrl + ,` 快速打开设置；按 `ESC` 关闭当前面板。


---


## 进阶功能


![](https://www.runoob.com/wp-content/uploads/2026/03/856e0b03-c02d-4213-b4e8-ea52dba3c5fa.png)


### MCP 服务器管理


在「MCP」面板中，可视化添加、编辑和删除 MCP（Model Context Protocol）服务器。配置自动同步到对应 CLI 工具，支持从已安装的应用一键导入现有 MCP 配置。


![](https://www.runoob.com/wp-content/uploads/2026/03/60c0a1c3-73c2-4749-a567-34c5f4587360.png)


### Skills 管理


Skills 是 Claude Code 的提示词增强功能。CC Switch 支持：


- 从 GitHub 仓库安装 Skills（内置 `baoyu-skills` 等预设仓库）
- 从本地 ZIP 文件安装
- 管理 Claude Code 和 Codex 的 Skills


![](https://www.runoob.com/wp-content/uploads/2026/03/667edee0-4fcb-4d17-ae1d-233f2ab5c4d6.png)


### 会话管理器（Session Manager）


在「会话」页面，可浏览全部五个应用的历史对话记录，支持目录导航和会话内搜索，并自动按当前应用过滤显示。


![](https://www.runoob.com/wp-content/uploads/2026/03/2e35294b-31e0-4777-8fe4-20116a0ee801.png)


### 备份管理


CC Switch 会定期自动备份数据库，在数据库迁移前也会自动备份。在「设置 → 备份管理」中可以：查看所有备份、重命名、删除，以及手动创建备份。


### 用量统计与计费


「用量」页面展示 Token 消耗统计，支持自动刷新、缓存命中率分析，以及按模型和 Provider 分类查看费用，帮助掌控 API 开支。


### Claude Rectifier（思考签名修复）


当使用某些第三方 API 网关时，Claude 的 thinking block 格式可能不兼容。开启 Rectifier 后，代理层会自动修复此问题。可在「设置 → 高级」中开关。


### WebDAV 自动同步


支持将数据库同步到 WebDAV 服务（如坚果云），实现多设备间的配置共享。内置大文件保护机制，防止误传。








	  AI 思考中...





			** [OpenClaw 配置目录](https://www.runoob.com/openclaw-setup.html)
			[QoderWork 教程](https://www.runoob.com/qoderwork.html) **













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