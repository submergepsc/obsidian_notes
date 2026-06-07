# OpenCode 配置

- Source: https://www.runoob.com/opencode/opencode-setup.html

通过 OpenCode，你可以接入任意 LLM（大语言模型）提供商，例如 OpenAI、Claude、DeepSeek、阿里百炼等，从而获得更强的 AI 编程能力。


如果你是第一次使用，建议优先选择 **OpenCode Zen**，它是 OpenCode 官方精选的一组模型，已经过测试和优化，开箱即用，适合新手。

**OpenCode Zen** 里面也包含了大量的免费大模型，所以基本上可以直接用，不用充钱。


---


### 步骤 1：启动配置


直接运行：


```
opencode
```

**

如果出现 EACCES: permission denied, open ''** 是权限问题，请使用管理员权限执行，比如：


```
sudo opencode
```


你会看到终端界面（TUI）:


![](https://www.runoob.com/wp-content/uploads/2026/04/f0d7fd3e-9f67-4c55-ab21-bd08ebc9a09e.png)


在 OpenCode 终端界面中输入：


```
/connect
```


![](https://www.runoob.com/wp-content/uploads/2026/04/53b109ec-a51f-44b6-b20f-04889c867e54.png)


然后选择：**opencode**


![](https://www.runoob.com/wp-content/uploads/2026/04/2c25238f-debb-4590-94cb-1244533a2df0.png)


如果有其他的大模型 Key，你也可以通过这个列表选择配置。


### 步骤 2：获取 API Key


打开以下页面并登录： [https://opencode.ai/auth](https://opencode.ai/auth)


- 登录账号
- 添加账单信息
- 创建 API Key


### 步骤 3：粘贴 API Key


回到终端，将获取到的 API Key 粘贴进去：


![](https://www.runoob.com/wp-content/uploads/2026/04/b6d2084f-4a4c-478a-9355-4f1cc15b989c.png)


完成后，即可开始使用 OpenCode。


我们可以按下 Ecs 退出配置 LLM 提供商，然后在对话窗口输入 **/model** 命令来查看支持的模型：


![](https://www.runoob.com/wp-content/uploads/2026/04/1f43d28d-65b0-4ac0-a5e1-52faa7e069d7.png)


看到有 Free 字样的就是免费的模型：


![](https://www.runoob.com/wp-content/uploads/2026/04/666d0340-63fe-4ad2-891b-edd8da69dfae.png)


选择完成后按下 Ecs 退出配置，就可以看到当前用的大模型：


![](https://www.runoob.com/wp-content/uploads/2026/04/db7d55c8-29f3-472f-a9b5-f07fac8f23f4.png)


### 国内 Coding Plan 套餐


现在市面上有很多大模型厂商， 国外的有 Anthropic、Open AI、Grok、Gemini等，但是访问国外现在不方便，国内的有 DeepSeek、千问、ZLM、Minimax 等。

我们使用Claude Code 写代码最费钱的就是 token 了，海外的访问不方便，而且还贵，国内的现在都有包月套餐，如果长期用建议买包月套餐划算。


---


## 接入阿里百炼

OpenCode 是开源的 AI 编程工具，可配合阿里云百炼提供的模型推理服务实现高效代码开发。


我们可以先使用阿里云主账号访问百炼模型服务平台 [https://bailian.console.aliyun.com/](https://bailian.console.aliyun.com/cn-beijing/?userCode=i5mn5r7m&tab=globalset#/efm/api_key)，然后点击右上角登录，登录成功后点击右上角的齿轮⚙️图标，选择 API key，然后复制 API key，如果没有也可以创建 API key：


![](https://www.runoob.com/wp-content/uploads/2025/09/83536c84-3956-4679-ad14-99d53e697692-scaled.png)


![](https://www.runoob.com/wp-content/uploads/2025/09/p994209.png)


**
可以直接购买资源包，这样用起来更划算：[https://cn.aliyun.com/benefit?from_alibabacloud=&userCode;=i5mn5r7m](https://cn.aliyun.com/benefit?from_alibabacloud=&userCode=i5mn5r7m)


### 在 OpenCode 中设置


在输入框输入 **/connect** 并单击 Enter。


在 Connect a Provider **列表的搜索框中输入 **alibaba** 进行搜索，选中 Alibaba (China) 并单击 Enter。


![](https://www.runoob.com/wp-content/uploads/2026/04/p1052260.png)


输入我们申请的 API Key 后按 Enter：


![](https://www.runoob.com/wp-content/uploads/2026/03/58b6aaed-203d-4f12-ba6b-8a62990465ba.png)


然后我们可以输入 **/model** 查看阿里支持的模型，并选择需要的：


![](https://www.runoob.com/wp-content/uploads/2026/04/c7e1315e-11dc-491c-9b4c-d1eaf89d3410.png)

**
本文档仅适用于按量付费模式，Coding Plan 用户请使用专属 Base URL 和 API Key 接入，详情请参考 [OpenCode Coding Plan](https://www.runoob.com/../ai-agent/opencode-coding-plan.html) 说明文档进行配置。


---

## 国内 API 配置

国内厂商 API 申请地址：


| 厂商/品牌 | 简介 | API 申请入口（点击即达） |
| --- | --- | --- |
| DeepSeek（国产高性价比） | 官方模型：deepseek-chat / deepseek-reasoner | https://platform.deepseek.com/api_keys |
| 火山方舟 Coding Plan | 支持在最新版 Doubao-Seed-2.0-pro/lite/Code、Doubao-Seed-Code、MiniMax-M2.5、Kimi-K2.5、GLM-4.7、Deepseek-V3.2 多种模型中自由切换，或使用Auto模式调度。 | https://www.volcengine.com/activity/codingplan |
| 阿里百炼（通义千问） | 阿里云大模型统一入口，支持千问、GLM、Kimi 、MiniMax 等最新版本模型 | https://bailian.console.aliyun.com |
| GLM（智谱清言） | 清华系 ChatGLM 系列，支持 GLM-4、GLM-3-Turbo 等 | https://open.bigmodel.cn |
| MiniMax | 国产多模态，支持文本、语音、图像混合调用 | https://platform.minimaxi.com |


进入对应控制台后，注册/登录 → 完成实名认证 → 创建 API Key 即可开始调用。



### API 管理工具


平台一多，配置起来就麻烦，我们可以使用第三方工具 CC Switch 可以帮我们轻松管理这几个热门工具的 API 配置：[https://github.com/farion1231/cc-switch/](https://github.com/farion1231/cc-switch/)，Windows / macOS / Linux 全支持。

CC Switch 是一个 Claude Code / Codex / Gemini CLI 的全方位辅助工具。

CC Switch 可以帮我们轻松管理这几个热门工具的 API 配置，就好比给你的开发工具箱来了个智能整理助手，所有工具的配置都能在它这有序管理。


![](https://www.runoob.com/wp-content/uploads/2026/03/3f634726-617d-43a7-9040-a4acaaca9433.png)


各平台安装包下载地址：[https://github.com/farion1231/cc-switch/releases](https://github.com/farion1231/cc-switch/releases)。


![](https://www.runoob.com/wp-content/uploads/2025/12/claude-code-runoob2.png)


具体的操作设置参考文章：[https://www.runoob.com/ai-agent/cc-switch.html](https://www.runoob.com/../ai-agent/cc-switch.html)


如果你不闲麻烦，可以参照下文，自行配置。









	  AI 思考中...





			** [OpenCode 安装](https://www.runoob.com/opencode-install.html)
			[OpenCode 第一次使用](https://www.runoob.com/opencode-first-usage.html) **













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