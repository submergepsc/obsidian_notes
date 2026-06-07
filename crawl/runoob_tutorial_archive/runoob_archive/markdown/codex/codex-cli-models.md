# Codex CLI 模型选择

- Source: https://www.runoob.com/codex/codex-cli-models.html

Codex 支持多种 AI 模型，不同模型在速度、能力、和成本方面各有特点。本节详细介绍如何选择合适的模型。


---


## 可用模型


![](https://www.runoob.com/wp-content/uploads/2026/04/04fc0d37-4102-4fd8-bb85-aaec07b27e11.png)


### 推荐模型


| 模型 | 特点 | 适用场景 |
| --- | --- | --- |
| gpt-5.4 | 最新旗舰模型，最强编码能力 | 复杂软件工程、专业工作 |
| gpt-5.4-mini | 快速高效的轻量模型 | 响应式编码任务、子代理 |
| gpt-5.3-codex | 行业领先的编码模型 | 复杂软件工程任务 |


**对于大多数 Codex 任务，建议从 gpt-5.4 开始。它将强大的编码、推理、原生计算机使用和更广泛的专业工作流结合在一个模型中。


### 替代模型


| 模型 | 特点 | 适用场景 |
| --- | --- | --- |
| gpt-5.2 | 之前用于编码和代理任务的通用模型 | 需要深度思考的复杂调试任务 |


---


## 选择建议


### 日常编码任务


使用 `gpt-5.4` 作为默认选择。它在各种编码任务中表现出色。


### 简单/快速任务


使用 `gpt-5.4-mini` 当你想要更快、更低成本的选项来处理轻量编码任务或子代理。


### 复杂推理任务


当遇到需要深入思考的困难调试任务时，可以尝试 `gpt-5.2`。


---


## 配置默认模型


你可以在配置文件中设置默认使用的模型：


## 配置默认模型


```
# ~/.codex/config.toml

# 设置默认模型
model = "gpt-5.4"
```


> 如果不指定模型，Codex 应用、CLI 或 IDE 扩展会默认使用推荐模型。


---


## 临时更改模型


### 使用命令行参数


## 命令行指定模型


```
# 使用特定模型启动
codex -m gpt-5.4

# 使用 exec 命令
codex exec -m gpt-5.4 "fix this bug"
```


### 在会话中切换


## 会话中切换模型


```
# 在 Codex 中输入
/model gpt-5.4-mini

# 或者使用 /model 命令
/model gpt-5.2
```


### IDE 扩展中切换


在 IDE 扩展中，使用输入框下方的模型选择器来切换模型。


---


## 推理配置


Codex 支持调整推理工作量（reasoning effort）：


| 配置值 | 说明 |
| --- | --- |
| minimal | 最小推理 |
| low | 低推理 |
| medium | 中等推理（默认） |
| high | 高推理 |
| xhigh | 极高推理（取决于模型） |


## 配置推理强度


```
# 配置默认推理强度
model_reasoning_effort = "medium"

# 为计划模式设置特定推理强度
plan_mode_reasoning_effort = "high"
```


> 更高的推理工作量会产生更深思熟虑的响应，但可能会更慢并消耗更多资源。


---


## 推理摘要


你可以控制推理摘要的详细程度：


| 配置值 | 说明 |
| --- | --- |
| auto | 自动选择 |
| concise | 简洁摘要 |
| detailed | 详细摘要 |
| none | 禁用摘要 |


## 配置推理摘要


```
# 选择推理摘要详细程度
model_reasoning_summary = "auto"
```


---


## 自定义模型提供商


除了 OpenAI 的模型，你还可以配置其他模型提供商：


## 配置自定义提供商


```
[model_providers.custom]
# 提供商显示名称
name = "My Custom Provider"

# API 基础 URL
base_url = "https://api.example.com/v1"

# API 密钥环境变量
env_key = "CUSTOM_PROVIDER_API_KEY"

# 其他配置
http_headers = {
    "X-Custom-Header": "value"
}
```


> 支持任何支持 Chat Completions 或 Responses API 的模型和提供商。


---


## 服务层级


Codex 支持不同的服务层级：


| 服务层级 | 说明 |
| --- | --- |
| flex | 灵活层级，优化成本 |
| fast | 快速层级，优先速度 |


## 配置服务层级


```
# 设置首选服务层级
service_tier = "fast"
```


---


## 模型选择最佳实践


### 开始新项目


使用 `gpt-5.4` 以获得最佳整体体验。


### 简单任务


使用 `gpt-5.4-mini` 节省成本。


### 复杂调试


考虑使用 `gpt-5.2` 进行深度调试。


### 子代理


子代理使用 `gpt-5.4-mini` 以提高效率。


> 定期检查更新，因为新模型和改进会不断推出。


---


## 常见问题


### Q: 哪个模型最适合日常编码？


gpt-5.4 是日常编码任务的最佳选择，提供强大的能力和合理速度的平衡。


### Q: 为什么建议子代理使用 mini 模型？


子代理执行较简单的任务，mini 模型可以更快地完成，同时节省成本。


### Q: 可以使用自己的模型吗？


是的，可以通过配置 model_providers 来使用任何支持 Responses API 的模型。


### Q: 模型选择影响成本吗？


是的，不同模型有不同的定价。查看定价页面了解详细信息。








	  AI 思考中...





			** [Codex 子代理（Subagents）](https://www.runoob.com/codex-subagents.html)
			[Codex MCP 服务器配置](https://www.runoob.com/codex-mcp.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#97f6f3fafef9d7e5e2f9f8f8f5b9f4f8fa)

      : · [免责声明](https://www.runoob.com/disclaimer)

      : · [关于我们](https://www.runoob.com/aboutus)

      : · [文章归档](https://www.runoob.com/archives)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/)**
    **[runoob.com](https://www.runoob.com/)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **