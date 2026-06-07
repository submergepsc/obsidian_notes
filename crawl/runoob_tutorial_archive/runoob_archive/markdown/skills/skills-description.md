# Skills 描述

- Source: https://www.runoob.com/skills/skills-description.html

技能描述（description）是技能最重要的部分，它决定了代理能否正确识别何时应该激活该技能。本节将教你如何编写有效的技能描述。


---


## 为什么描述很重要


技能描述在代理加载技能的过程中扮演着关键角色：


- 在发现阶段，代理只加载每个技能的名称和描述
- 描述是代理判断是否激活技能的主要依据
- 一个好的描述可以提高技能的激活准确率


如果描述写得不好，代理可能会：


- 在不需要时激活技能（误报）
- 在需要时忘记激活技能（漏报）
- 激活错误的技能


**

提示：技能描述的质量直接影响技能的可用性。投入时间优化描述是值得的。


---


## 描述的基本结构


一个好的技能描述应该包含两个部分：


- **功能说明**：描述技能能做什么
- **触发条件**：说明在什么情况下使用


```
description: 从 PDF 文件中提取文本和表格，填写 PDF 表单，合并多个 PDF。处理 PDF 文档或用户提及 PDF、表单或文档提取时使用。
#                         ↑ 功能说明                                      ↑ 触发条件
```


---


## 编写有效描述的技巧


### 1. 包含具体的触发关键词


在描述中包含用户可能使用的具体词汇和短语。这些关键词帮助代理识别相关任务。


好的描述：


```
description: 提取 PDF 文本和表格，填写表单，合并 PDF。使用场景：处理 PDF 文件、提取文档内容、填写 PDF 表单、合并多个 PDF、用户提及「PDF」「提取」「表单」「合并」等关键词。
```


### 2. 描述要具体而非笼统


避免使用过于宽泛的描述，这会导致代理无法准确判断。


```
# 不好的描述 - 太笼统
description: 帮助处理各种文件。

# 好的描述 - 具体明确
description: 处理图像文件，包括调整大小、转换格式、应用滤镜。使用场景：处理图片、调整图像尺寸、转换图片格式。
```


### 3. 说明多个使用场景


列出技能可能适用的不同场景，帮助代理更准确地匹配。


```
description: 执行代码审查，检查安全漏洞、代码质量和性能问题。使用场景：代码审查、PR 审查、代码检查、安全扫描、质量评估、用户要求「review」「检查代码」「安全性」等。
```


### 4. 区分相似技能


如果你有多个相关技能，确保它们的描述有明显区别。


```
# 技能 1：PDF 文本提取
name: pdf-extract
description: 从 PDF 文件中提取文本内容和表格数据。使用场景：提取 PDF 文字、读取 PDF 内容、PDF 转文本、用户提及「PDF 提取」「读取 PDF」等。

# 技能 2：PDF 表单处理
name: pdf-form
description: 填写 PDF 表单字段，提取表单数据。使用场景：填写 PDF 表单、填充表单字段、PDF 表单数据处理、用户提及「PDF 表单」「填写表单」等。
```


---


## 描述长度控制


description 字段的最大长度是 1024 字符。但这不是目标，描述应该简洁而准确。


| 情况 | 建议长度 |
| --- | --- |
| 简单技能 | 50-100 字符 |
| 中等复杂度技能 | 100-200 字符 |
| 复杂技能 | 200-400 字符 |


> 注意：描述不是越长越好。过长的描述可能包含过多无关信息，反而干扰代理的判断。


---


## 测试和优化描述


创建技能后，你应该测试描述是否能够正确触发技能。以下是测试步骤：


### 1. 基本功能测试


使用描述中包含的关键词进行测试，确认技能能够被激活。


### 2. 边界情况测试


测试一些可能触发但不应该触发的场景。


### 3. 迭代优化


根据测试结果调整描述：


- 如果误报增加：在描述中添加更多限定条件
- 如果漏报增加：在描述中添加更多可能的触发词
- 如果激活错误：确保描述与其他相似技能有足够区分度


优化示例：


```
# 初始版本 - 可能漏报
description: 提取 PDF 文本。

# 优化版本 - 减少漏报
description: 从 PDF 文件中提取文本内容和表格数据。使用场景：提取 PDF 文字、读取 PDF 内容、PDF 转文本。

# 最终版本 - 进一步优化
description: 从 PDF 文件中提取文本内容和表格数据。使用场景：提取 PDF 文字、读取 PDF 内容、PDF 转文本、用户提及「PDF 提取」「读取 PDF」「PDF 文字」「PDF 内容」等关键词时使用。
```


---


## 常见问题和解决方案


### 问题 1：技能总是被激活


这说明描述过于宽泛。解决方法是添加更多限定条件和使用场景。

解决方案：


```
# 修改前 - 太宽泛
description: 处理文本。

# 修改后 - 更具体
description: 使用正则表达式处理和转换文本字符串。使用场景：文本匹配、字符串替换、模式提取、数据清洗。
```


### 问题 2：技能从未被激活


这说明描述中缺少用户可能使用的关键词。解决方法是添加更多触发词。


解决方案：


```
# 修改前 - 关键词太少
description: 优化数据库查询。

# 修改后 - 添加更多触发词
description: 优化 SQL 查询性能，分析执行计划，添加索引。使用场景：SQL 优化、查询慢、数据库性能、调优索引、执行计划分析。
```


### 问题 3：激活了错误的技能


这说明多个技能的描述过于相似。解决方法是让描述更具区分度。


> 提示：定期测试和优化你的技能描述是一个好习惯。随着使用场景的增多，你可能会发现描述需要调整。









	  AI 思考中...





			** [SKILL.md 文件](https://www.runoob.com/skill-md-file.html)
			[Skills 脚本扩展](https://www.runoob.com/skills-scripts.html) **













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

                  : · [VS Code 创建与...](https://www.runoob.com/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/skills-first.html)




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