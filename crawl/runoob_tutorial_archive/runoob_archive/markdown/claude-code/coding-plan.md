# Coding Plan

- Source: https://www.runoob.com/claude-code/coding-plan.html

现在市面上有很多大模型厂商， 国外的有 Anthropic、Open AI、Grok、Gemini等，但是访问国外现在不方便，国内的有 DeepSeek、千问、ZLM、Minimax 等。

我们使用Claude Code 写代码最费钱的就是 token 了，海外的访问不方便，而且还贵，国内的现在都有包月套餐，如果长期用建议买包月套餐划算。


很多厂商都退出了 Coding Plan，它专为 AI 编程工具设计的订阅制服务，整合了千问（Qwen）、GLM、Kimi、MiniMax 等顶级大模型，兼容主流 AI 编程助手（如 Cursor、Claude Code、OpenClaw 等），采用固定月费模式，成本远低于按量计费 API，且彻底杜绝欠费风险。


** Coding Plan 核心优势：**


- **顶级模型一键接入**：无需自己调用百炼 API，直接在熟悉的编程工具里使用最强模型。
- **成本极低**：固定月费（Lite ¥40/月，Pro ¥200/月），首月限时优惠仅 7.9 元 / 39.9 元。
- **安全无忧**：禁止 API 直连，仅限交互式编程工具使用，避免滥用封禁风险。
- **图片理解支持**：qwen3.5-plus、kimi-k2.5 支持上传截图/设计图直接生成代码。


Coding Plan 支持以下工具：Cursor、Claude Code、OpenClaw、OpenCode、Cline（VS Code 扩展）、Kilo Code / Kilo CLI、Qwen Code、Codex 等。


---


## 订阅方舟 Coding Plan


访问方舟 [Coding Plan 活动](https://www.volcengine.com/activity/codingplan?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=runoob)，按需订阅套餐，用量不大用 Lite 版本就可以了, 如果用量非常大可以使用 Pro 版本。


![](https://www.runoob.com/wp-content/uploads/2026/03/e7f85ed4-d824-42ed-b43e-27afe21ee029.png)


**方舟 Coding Plan** 是面向开发者的 AI 编码订阅服务，助力高效开发，核心优势如下：


- **模型丰富**：支持主流大语言模型与 Embedding 模型，覆盖 Doubao、DeepSeek、Kimi、GLM、MiniMax 等热门系列。
- **工具兼容广**：适配 Claude Code、Cursor、Cline、OpenCode、Codex CLI 等主流 AI 编码工具。
- **额度共享**：多工具共用套餐额度，灵活切换，适配不同开发场景。
- **套餐灵活**：提供 Lite / Pro 多档方案，满足轻度到高强度开发需求。
- **稳定高可用**：多租户隔离与资源调度保障，高峰期依然稳定流畅。


不同的工具配置的 Base URL 根据兼容的协议会有不同：

- 兼容 Anthropic 接口协议工具：**https://ark.cn-beijing.volces.com/api/coding**
- 兼容 OpenAI 接口协议工具：**https://ark.cn-beijing.volces.com/api/coding/v3**


**

注意：**请勿使用 https://ark.cn-beijing.volces.com/api/v3 ：该 Base URL 不会消耗您的 Coding Plan 额度，而是会产生额外费用。


### 配置 Claude Code


完成 Claude Code 安装后，还需配置以下信息：


- **ANTHROPIC_BASE_URL**：`**https://ark.cn-beijing.volces.com/api/coding**`
- **ANTHROPIC_AUTH_TOKEN**：[获取您的 API Key](https://console.volcengine.com/ark/region:ark+cn-beijing/apikey?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=runoob)
- **ANTHROPIC_MODEL**：支持两种配置方式 配置具体模型名称（如 `kimi-k2.5`），可实时切换模型
- 配置 `ark-code-latest`，通过控制台切换模型



**

具体模型有：doubao-seed-2.0-code、doubao-seed-2.0-pro、doubao-seed-2.0-lite、doubao-seed-code、minimax-m2.5、glm-4.7、deepseek-v3.2、kimi-k2.5。


配置 settings.json**


编辑或新建 `settings.json` 文件，内容如下：


```
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "<ARK_API_KEY>",
    "ANTHROPIC_BASE_URL": "https://ark.cn-beijing.volces.com/api/coding",
    "ANTHROPIC_MODEL": "<Model_Name>"
  }
}
```


请替换以下内容：


- ``：替换为您的 API Key
- ``：替换为所需模型名称，例如 `kimi-k2.5`


settings.json 文件路径：


- **MacOS / Linux**：`~/.claude/settings.json`
- **Windows**：`C:\Users\\.claude\settings.json`

**配置 .claude.json：**


编辑或新建 `.claude.json` 文件，添加以下内容：


```
{
  "hasCompletedOnboarding": true
}
```


.
claude.json 文件路径：


- **MacOS / Linux**：`~/.claude.json`
- **Windows**：`C:\Users\\.claude.json`


**
详细文档参考：[https://www.volcengine.com/docs/82379/1928262](https://www.volcengine.com/docs/82379/1928262?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=runoob)


---

## 订阅阿里 Coding Plan


> Coding Plan 基本太难抢， 也要下架，阿里现在都改为 Token Plan 了，查看：[**阿里云百炼 Token Plan**](https://www.aliyun.com/benefit/scene/tokenplan?source=5176.29345612&userCode=i5mn5r7m)
>
> - OpenAI 兼容：**https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1**
> - Anthropic 兼容：**https://token-plan.cn-beijing.maas.aliyuncs.com/apps/anthropic**


需要先购买百炼的 Coding Plan 套餐：[百炼的 Coding Plan 活动页面](https://www.aliyun.com/benefit/scene/codingplan?source=5176.29345612&userCode=i5mn5r7m)


如果用量非常大可以使用 Pro 版本，它是 Lite 版本的 5 倍，支持的模型都一样（现在太火，Lite 版本需要在 9:30 开抢）：


[![](https://www.runoob.com/wp-content/uploads/2026/02/55f28438-580a-45a3-b1c0-d621d8d674fd.png)](https://www.aliyun.com/benefit/scene/codingplan?source=5176.29345612&userCode=i5mn5r7m)


购买完 Coding Plan 套餐，可以在 [Coding Plan](https://bailian.console.aliyun.com/cn-beijing/?userCode=i5mn5r7m&tab=coding-plan#/efm/detail) 页面，获取 Coding Plan 专属 API Key（格式为 sk-sp-xxxxx）。


后续需在 AI 工具中配置以下其中一个 Base URL（因工具而异）： - Anthropic 兼容协议：**https://coding.dashscope.aliyuncs.com/apps/anthropic** - OpenAI 兼容协议（OpenClaw 可使用）：**https://coding.dashscope.aliyuncs.com/v1** 更大流行的应用也有对应的文档说明：


![](https://www.runoob.com/wp-content/uploads/2026/03/63d83846-aa4b-4613-a6c7-6ccc7eced39c.png)


> 说明：**Coding Plan 专属的 API Key 和 Base URL 与百炼按量计费的 API Key（sk-xxxxx）和Base URL（https://dashscope.aliyuncs.com/xxxxxx）不互通，请勿混用。
> 如果抢不到，可以直接购买资源包，这样用起来更划算：[https://cn.aliyun.com/benefit?from_alibabacloud=&userCode;=i5mn5r7m](https://cn.aliyun.com/benefit?from_alibabacloud=&userCode=i5mn5r7m)
> ![](https://www.runoob.com/wp-content/uploads/2026/03/f6707868-26b9-4cd4-bf25-47ebe008f679.png)


### Claude Code 配置

完成Claude Code安装后，配置以下信息：

- **ANTHROPIC_BASE_URL**：**https://ark.cn-beijing.volces.com/api/coding**
- **ANTHROPIC_AUTH_TOKEN**：[获取API Key](https://console.volcengine.com/ark/region:ark+cn-beijing/apikey?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=runoob)
- **ANTHROPIC_MODEL**: 支持配置 Model Name （doubao-seed-2.0-code、doubao-seed-2.0-pro、doubao-seed-2.0-lite、doubao-seed-code、minimax-m2.5、glm-4.7、deepseek-v3.2、kimi-k2.5）、配置 ark-code-latest（控制台切换模型）两种方式。


** 配置步骤如下：**

编辑或新增 settings.json 文件，需要修改的配置信息如下：


- ：替换为您自己的 API Key
- ：更新为需要使用的模型信息，如 kimi-k2.5。支持的模型信息参见模型配置。


不同系统配置文件路径不同，具体如下：


- MacOS & Linux：~/.claude/settings.json
- Windows：C:\Users\\.claude\settings.json


```
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "<ARK_API_KEY>",
        "ANTHROPIC_BASE_URL": "https://ark.cn-beijing.volces.com/api/coding",
        "ANTHROPIC_MODEL": "<Model_Name>"
    }
}
```


编辑或新增 .claude.json 文件，修改或新增 hasCompletedOnboarding 字段值为 true。


不同系统配置文件路径不同，具体如下：

MacOS & Linux：~/.claude.json

Windows：C:\Users\\.claude.json


```
{
  "hasCompletedOnboarding": true
}
```


保存配置文件后，在新的终端窗口执行后续命令。


### 在 Claude Code 配置 Coding Plan

在 Claude Code 中接入百炼 Coding Plan，需要配置以下信息：



- **ANTHROPIC_BASE_URL**：设置为 **https://coding.dashscope.aliyuncs.com/apps/anthropic**。
- **ANTHROPIC_AUTH_TOKEN**：设置为 [Coding Plan](https://bailian.console.aliyun.com/cn-beijing/?userCode=i5mn5r7m&tab=coding-plan#/efm/detail) 专属 API Key。
- **ANTHROPIC_MODEL**：设置为 Coding Plan 支持的模型，qwen3.5-plus（支持图片理解）、kimi-k2.5（支持图片理解）、glm-5、MiniMax-M2.5。


### macOS/Linux

创建并打开配置文件 **~/.claude/settings.json**。


**~** 代表用户主目录，如果 **.claude** 目录不存在，需要先行创建，可在终端执行 **mkdir -p ~/.claude** 来创建。


```
vim ~/.claude/settings.json
```


编辑配置文件，将 YOUR_API_KEY 替换为 Coding Plan 专属 API Key。





```
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
        "ANTHROPIC_BASE_URL": "https://coding.dashscope.aliyuncs.com/apps/anthropic",
        "ANTHROPIC_MODEL": "qwen3.5-plus"
    }
}
```


保存配置文件，重新打开一个终端即可生效。


编辑或新增 ~/.claude.json 文件，将 hasCompletedOnboarding 字段的值设置为 true 并保存文件。





```
{
  "hasCompletedOnboarding": true
}
```


hasCompletedOnboarding 作为顶层字段，请勿嵌套于其他字段。

该步骤可避免启动Claude Code时报错：Unable to connect to Anthropic services。


### Windows


创建并打开配置文件 **C:\Users\您的用户名\.claude\settings.json**。


#### 1、CMD 命令方式


创建目录：




```
if not exist "%USERPROFILE%\.claude" mkdir "%USERPROFILE%\.claude"
```


创建并打开文件：




```
notepad "%USERPROFILE%\.claude\settings.json"
```


编辑配置文件，将 YOUR_API_KEY 替换为 Coding Plan 专属 API Key。





```
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
        "ANTHROPIC_BASE_URL": "https://coding.dashscope.aliyuncs.com/apps/anthropic",
        "ANTHROPIC_MODEL": "qwen3.5-plus"
    }
}
```


保存配置文件，重新打开一个终端即可生效。


编辑或新增 C:\Users\您的用户名\.claude.json 文件，将 hasCompletedOnboarding 字段的值设置为 true，并保存文件。




```
{
  "hasCompletedOnboarding": true
}
```


#### 2、PowerShell 命令方式


创建目录：




```
mkdir -Force $HOME\.claude
```


创建并打开文件：




```
notepad $HOME\.claude\settings.json
```


编辑配置文件，将 YOUR_API_KEY 替换为 Coding Plan 专属 API Key。





```
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
        "ANTHROPIC_BASE_URL": "https://coding.dashscope.aliyuncs.com/apps/anthropic",
        "ANTHROPIC_MODEL": "qwen3.5-plus"
    }
}
```


保存配置文件，重新打开一个终端即可生效。


编辑或新增 C:\Users\您的用户名\.claude.json 文件，将hasCompletedOnboarding 字段的值设置为 true，并保存文件。




```
{
  "hasCompletedOnboarding": true
}
```


---


## 使用 Claude Code

打开终端，并进入项目所在的目录，运行以下命令启动程序 Claude Code：




```
cd path/to/your_project
claude
```


启动后，需要授权 Claude Code 执行文件。


![](https://www.runoob.com/wp-content/uploads/2026/03/p1040228.png)


输入/status确认模型、Base URL、API Key 是否配置正确。


![](https://www.runoob.com/wp-content/uploads/2026/03/p1040230.png)


在 Claude Code 中对话。


![](https://www.runoob.com/wp-content/uploads/2026/03/p1054776.png)


### 切换模型


| 切换方式 | 操作说明 | 示例 |
| --- | --- | --- |
| 启动时切换 | 在终端执行 claude --model 指定模型并启动 Claude Code | claude --model qwen3-coder-next |
| 会话期间切换 | 在对话框输入 /model 命令切换模型 | /model qwen3-coder-next |


### 常见命令汇总


| 命令 | 说明 | 示例 |
| --- | --- | --- |
| /init | 在项目根目录生成 CLAUDE.md 文件，用于定义项目级指令和上下文 | /init |
| /status | 查看当前模型、API Key、Base URL 等配置状态 | /status |
| /model | 切换模型 | /model qwen3-coder-next |
| /clear | 清除对话历史，开始全新对话 | /clear |
| /plan | 进入规划模式，仅分析和讨论方案，不修改代码 | /plan |
| /compact | 压缩对话历史，释放上下文窗口空间 | /compact |
| /config | 打开配置菜单，可设置语言、主题等 | /config |


**
更多内容参考：[https://help.aliyun.com/zh/model-studio/coding-plan-quickstart](https://help.aliyun.com/zh/model-studio/coding-plan-quickstart)










	  AI 思考中...





			** [Claude Code 如何工作](https://www.runoob.com/claude-code-how-it-work.html)
			[skill-creator 使用](https://www.runoob.com/skill-creator-usage.html) **













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