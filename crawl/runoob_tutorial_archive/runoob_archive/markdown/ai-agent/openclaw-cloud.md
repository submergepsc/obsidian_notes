# OpenClaw 一键部署

- Source: https://www.runoob.com/ai-agent/openclaw-cloud.html

现在各大平台都已经支持这个智能体，如果不想安装在本机，可以一键部署云上 OpenClaw：





        [** 字节 ArkClaw 火山引擎云端部署方案，快速体验智能体](https://www.volcengine.com/product/arkclaw?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=runoob)


        [** 阿里云 OpenClaw 一键部署云端智能体，无需本地安装](https://www.aliyun.com/activity/ecs/clawdbot?userCode=i5mn5r7m)



Token 可以通过购买 Coding plan 包更划算：


---


## ArkClaw 一键部署


**ArkClaw** 是火山引擎提供的云端 AI 智能体（Agent）服务，可帮助开发者**一键部署 OpenClaw 到云端**，免去本地安装与复杂运维配置。





        [** 字节 ArkClaw 火山引擎云端部署方案，快速体验智能体](https://www.volcengine.com/product/arkclaw?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=runoob)



使用 ArkClaw，您将获得：


- **专属独立 ECS 资源**，一对一隔离部署
- **7 × 24 小时在线运行**，随时可用
- **零门槛开箱即用**，无需手动配置环境
- **无缝接入方舟 Coding Plan**，直接使用订阅额度
- **告别 Token 按量计费焦虑**，开发成本更可控


### 创建并使用 ArkClaw

	订阅套餐后我们就可以：


- 登录[火山方舟体验中心](https://console.volcengine.com/ark/region:ark+cn-beijing/experience??utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=runoob)。
- 在左侧目录选择 **Agent > ArkClaw**。
- 单击立即开始按钮，提交创建申请。


![](https://www.runoob.com/wp-content/uploads/2026/02/79aa72e4-4b49-46c5-a804-c879c604d348.png)


待创建成功后，即可在方舟中与 ArkClaw 进行对话:


![](https://www.runoob.com/wp-content/uploads/2026/02/79aa72e4-4b49-46c5-a804-c879c604d348.png)


---


## 阿里云部署 OpenClaw


本章节将详细介绍如何使用阿里云部署 OpenClaw，访问 [https://www.aliyun.com/activity/ecs/clawdbot](https://www.aliyun.com/activity/ecs/clawdbot?userCode=i5mn5r7m)，选择一键购买并部署：


[![](https://www.runoob.com/wp-content/uploads/2026/02/ab4d1d52-43f3-4525-9728-6ae85ee7a304.png)](https://www.aliyun.com/activity/ecs/clawdbot?userCode=i5mn5r7m)


如果手速快的，可以每天 9.9 抢服务器。


云服务器部署优势还是很明显的：


[![](https://www.runoob.com/wp-content/uploads/2026/01/c6da4d06-b50f-4b11-aebc-bdea5c5db859-scaled.png)](https://www.aliyun.com/activity/ecs/clawdbot?userCode=i5mn5r7m)


套餐已经包含了服务器与大模型：
[![](https://www.runoob.com/wp-content/uploads/2026/02/7fdb80c6-7af8-4cb0-8757-638a88cfefe6.png)](https://www.aliyun.com/activity/ecs/clawdbot?userCode=i5mn5r7m)

我们可以使用它们的镜像，一键安装：

![](https://www.runoob.com/wp-content/uploads/2026/02/53ea9fb0-d4ea-4582-a16f-38e7d6906880.png)


购买完成后就可以到控制台配置 OpenClaw：

[![](https://www.runoob.com/wp-content/uploads/2026/02/aliyun-openclaw-setup.png)](https://www.runoob.com/wp-content/uploads/2026/02/aliyun-openclaw-setup.png)


---


## 配置 OpenClaw

OpenClaw 执行过程中默认调用百炼模型，模型调用的主要计费方式有两种：


- **Coding Plan AI 编码套餐（推荐）：**采用固定月费模式，提供月度请求额度，超出时段限额的调用会报错且不计费用，可避免产生超出预期的费用，目前支持 qwen3.5-plus、kimi-k2.5、MiniMax-M2.5、glm-5等模型。
- **按 Token 用量计费：**OpenClaw 2026.2.26 版本默认使用 qwen3.5-plus 模型作为文本和图像处理模型，如果用的多这个就不划算了。





我们可以先使用阿里云主账号访问百炼模型服务平台：[https://bailian.console.aliyun.com/](https://bailian.console.aliyun.com/)，然后点击右上角登录，登录成功后点击右上角的齿轮⚙️图标，选择 API key，然后复制 API key，如果没有也可以创建 API key：


![](https://www.runoob.com/wp-content/uploads/2025/09/83536c84-3956-4679-ad14-99d53e697692-scaled.png)


![](https://www.runoob.com/wp-content/uploads/2025/09/p994209.png)


开通阿里云百炼不会产生费用，仅模型调用（超出免费额度后）、模型部署、模型调优会产生相应计费。


OpenClaw 还是比较消耗 token 的，如果要长期使用，我们可以先购买个最便宜的包：[阿里云百炼大模型服务平台](https://cn.aliyun.com/benefit?from_alibabacloud=&userCode=i5mn5r7m)。


[![](https://www.runoob.com/wp-content/uploads/2025/09/f9be5f87-2ed0-4d85-b2a4-ad8542312d6f.png)](https://dashi.aliyun.com/activity/ydsbl?userCode=i5mn5r7m)


### Coding Plan
**
Coding Plan 基本太难抢， 也要下架，阿里现在都改为 Token Plan 了，查看：[**阿里云百炼 Token Plan**](https://www.aliyun.com/benefit/scene/tokenplan?source=5176.29345612&userCode=i5mn5r7m)


- OpenAI 兼容：**https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1**
- Anthropic 兼容：**https://token-plan.cn-beijing.maas.aliyuncs.com/apps/anthropic**


另外，使用百炼的 Coding Plan 套餐更便宜：[https://www.aliyun.com/benefit/scene/codingplan](https://www.aliyun.com/benefit/scene/codingplan?source=5176.29345612&userCode=i5mn5r7m)


![](https://www.runoob.com/wp-content/uploads/2026/02/55f28438-580a-45a3-b1c0-d621d8d674fd.png)


购买完 Coding Plan 套餐，可以在 [Coding Plan](https://bailian.console.aliyun.com/cn-beijing/?userCode=i5mn5r7m&tab=coding-plan#/efm/detail) 页面，获取 Coding Plan 专属 API Key（格式为 sk-sp-xxxxx）。


后续需在 AI 工具中配置以下其中一个 Base URL（因工具而异）：

- OpenAI 兼容协议（OpenClaw 可使用）：https://coding.dashscope.aliyuncs.com/v1
- Anthropic 兼容协议：https://coding.dashscope.aliyuncs.com/apps/anthropic


> 说明：**Coding Plan 专属的 API Key 和 Base URL 与百炼按量计费的 API Key（sk-xxxxx）和Base URL（https://dashscope.aliyuncs.com/xxxxxx）不互通，请勿混用。如果抢不到，可以直接购买资源包：[https://cn.aliyun.com/benefit?from_alibabacloud=&userCode;=i5mn5r7m](https://cn.aliyun.com/benefit?from_alibabacloud=&userCode=i5mn5r7m)


在[服务器页面](https://swasnext.console.aliyun.com/servers)，单击服务器卡片中的实例 ID，进入服务器概览页面。


单击应用详情页签，配置 OpenClaw。


![](https://www.runoob.com/wp-content/uploads/2026/02/clawbot-233.png)


- ** 端口放通：**需要放通对应端口的防火墙，单击一键放通即可。
- **配置 OpenClaw：**单击执行命令，输入百炼的 API-Key，单击下一步。
- **访问控制页面：**单击执行命令可获取 Clawdbot 对话的地址。
- **查看 Token: **在帮助  Config。
- 在 Config 页面左侧导航栏单击 Gateway，切换至 Http 页签，在 Responses 区域将 Enabled 切换至开启，单击 Save。


![](https://www.runoob.com/wp-content/uploads/2026/02/clawbot-23333-scaled.png)


### （可选）配置联网搜索功能


目前中国内地地域（除香港）暂不支持联网搜索。香港和海外地域若需使用联网功能，可参考 [OpenClaw 官网配置](https://docs.openclaw.ai/brave-search)。








	  AI 思考中...





			** [Skills 教程](https://www.runoob.com/skills-agent.html)
			[Trae Solo](https://www.runoob.com/trae-solo.html) **













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