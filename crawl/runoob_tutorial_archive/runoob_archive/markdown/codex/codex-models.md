# Codex 模型选择

- Source: https://www.runoob.com/codex/codex-models.html

Codex 支持多种模型，了解各模型特点，根据场景选择合适的模型。


---


## 可用模型


Codex 目前支持以下模型：


| 模型 | 类型 | 特点 | 适用场景 |
| --- | --- | --- | --- |
| gpt-5.4 | 旗舰 | 最强能力、深度推理 | 复杂任务、架构设计 |
| gpt-5.4-mini | 轻量 | 快速响应、成本较低 | 简单任务、快速迭代 |
| gpt-5.3-codex | 专业 | 编程优化、代码专精 | 代码编写、Bug 修复 |
| gpt-5.3-codex-spark | 快速 | 极速响应、高频交互 | 实时协作、快速问答 |


---


## 模型特点详解


### GPT-5.4


旗舰模型，具备最强的推理和创作能力。


| 特点 | 说明 |
| --- | --- |
| 推理深度 | 深度分析复杂问题 |
| 上下文理解 | 理解大型代码库结构 |
| 多步骤任务 | 处理复杂工作流 |
| 准确性 | 高准确率，减少返工 |


### 适用场景


- 架构设计和重构
- 复杂 Bug 分析和修复
- 多模块协调开发
- 代码审查和质量分析


---


### GPT-5.4-mini


轻量模型，响应快速，适合日常开发。


| 特点 | 说明 |
| --- | --- |
| 响应速度 | 比旗舰模型更快 |
| 成本效益 | token 消耗较少 |
| 日常任务 | 适合常规开发操作 |


### 适用场景


- 简单功能实现
- 代码格式化和重构
- 文档编写
- 快速问答


---


### GPT-5.3-Codex


专门针对编程任务优化的模型。


| 特点 | 说明 |
| --- | --- |
| 代码专精 | 专为编程任务训练 |
| 语言覆盖 | 支持多种编程语言 |
| 代码质量 | 生成的代码质量高 |


### 适用场景


- 代码编写和生成
- Bug 修复和调试
- 代码重构
- 测试编写


---


### GPT-5.3-Codex-Spark


极速响应模型，适合高频交互场景。


| 特点 | 说明 |
| --- | --- |
| 极速响应 | 最快的响应速度 |
| 实时协作 | 适合交互式开发 |
| Pro 专属 | 仅 Pro 计划可用 |


### 适用场景


- 实时代码问答
- 快速原型验证
- 高频迭代开发


---


## 推理强度配置


可以调整模型的推理强度，平衡速度和深度。


### 推理强度级别


| 级别 | 说明 | 特点 |
| --- | --- | --- |
| minimal | 最小推理 | 最快响应，适合简单任务 |
| low | 低推理强度 | 快速但有一定分析 |
| medium | 中等推理 | 平衡速度和深度（默认） |
| high | 高推理强度 | 深度分析，适合复杂任务 |
| xhigh | 超高推理 | 最强推理，最慢响应 |


### 配置推理强度


## 推理强度设置


```
# CLI 指定
codex --reasoning-effort high

# 配置文件
[mycode4 type="toml"]
model_reasoning_effort = "high"

# 会话中切换
/model gpt-5.4 --reasoning-effort xhigh
[/mycode4]
```


---


## 推理摘要


控制 Codex 显示推理过程的详细程度。


### 摘要模式


| 模式 | 说明 |
| --- | --- |
| auto | 自动决定详细程度（默认） |
| concise | 简要摘要 |
| detailed | 详细推理过程 |
| none | 不显示推理摘要 |


## 推理摘要设置


```
# ~/.codex/config.toml
model_reasoning_summary = "detailed"
```


---


## 模型切换


在不同场景切换使用不同模型。


### 切换方式


## 切换模型


```
# CLI 斜杠命令
/model gpt-5.4
/model gpt-5.4-mini
/model gpt-5.3-codex

# 带推理强度
/model gpt-5.4 --reasoning-effort high

# App 中切换
点击模型选择器，选择目标模型
```


### 场景切换建议


| 场景 | 推荐模型 | 推理强度 |
| --- | --- | --- |
| 架构设计 | gpt-5.4 | high/xhigh |
| 复杂重构 | gpt-5.4 | high |
| Bug 修复 | gpt-5.3-codex | medium |
| 日常编码 | gpt-5.4-mini | low/medium |
| 快速问答 | gpt-5.4-mini | minimal |
| 实时协作 | gpt-5.3-codex-spark | minimal |


---


## 服务层级


选择不同的服务层级影响响应优先级。


### 服务层级选项


| 层级 | 说明 |
| --- | --- |
| flex | 弹性服务，响应可能稍慢（默认） |
| fast | 优先服务，更快响应 |


## 服务层级设置


```
# ~/.codex/config.toml
service_tier = "fast"
```


---


## 模型与计划


不同计划对模型的支持有差异：


| 计划 | 可用模型 |
| --- | --- |
| Free | 基础模型 |
| Plus | gpt-5.4, gpt-5.4-mini, gpt-5.3-codex |
| Pro | 全部模型 + Spark + 更高限额 |
| API Key | 按 token 计费，支持主流模型 |


---


## 成本考量


### Token 消耗对比


| 模型 | 相对成本 |
| --- | --- |
| gpt-5.4 | 最高 |
| gpt-5.3-codex | 中高 |
| gpt-5.4-mini | 较低 |
| gpt-5.3-codex-spark | 低 |


### 成本优化建议


- 简单任务使用 mini 或 Spark 模型
- 日常开发使用 medium 推理强度
- 仅在复杂任务使用旗舰模型和高推理强度
- 使用 /compact 压缩上下文减少 token 消耗


---


## 最佳实践


### 模型选择原则


- 根据任务复杂度选择模型
- 平衡响应速度和推理深度
- 复杂任务优先准确性
- 高频交互优先响应速度


### 配置建议


## 推荐配置


```
# 日常开发配置
model = "gpt-5.4-mini"
model_reasoning_effort = "medium"
model_reasoning_summary = "auto"

# 复杂任务临时切换
# /model gpt-5.4 --reasoning-effort high
```


---


## 常见问题


### Q: 哪个模型最适合代码编写？


gpt-5.3-codex 专为编程任务优化，适合大多数代码编写场景。


### Q: 如何平衡速度和质量？


日常任务使用 gpt-5.4-mini + medium 推理强度，复杂任务切换到 gpt-5.4 + high 推理强度。


### Q: Spark 模型有什么优势？


Spark 模型响应最快，适合高频交互和实时协作，仅 Pro 计划可用。


### Q: 推理强度如何影响结果？


更高的推理强度意味着 Codex 会进行更深入的分析，但响应时间会更长。








	  AI 思考中...





			** [Codex 安全与企业管理](https://www.runoob.com/codex-security.html)
			[Codex CLI 配置](https://www.runoob.com/codex-config.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#f49590999d9ab486819a9b9b96da979b99)

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