# Qoder Quest 模式

- Source: https://www.runoob.com/ai-agent/qoder-quest-mode.html

Quest Mode 是 Qoder 的自主编码功能，能让 AI 智能体端到端地完成开发任务。


我们只需描述你的目标，Quest 会自主进行需求澄清、方案规划、代码执行和结果验证——整个过程几乎无需人工干预。


Qoder 它的核心理念只有两句话：定义目标，审查结果。


与 Agent Mode 不同，Quest Mode 专为复杂、长时间运行的任务而设计——比如实现一个全新功能或修复深层 Bug。


我们提供清晰的需求描述，AI 负责所有的怎么做。


---


## 注册并安装 Qoder


  **


    **
      我们先点击访问
      [Qoder 官网](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)
      注册 Qoder 账号
    **


      免费试用 Pro + 300 Credits




![](https://www.runoob.com/wp-content/uploads/2026/03/6c1e7ac0-4c98-4438-9c17-e8a5f15cc922.png)


**注册完成后点击右上角的**下载**按钮，根据你的电脑系统，下载安装程序。**


![](https://www.runoob.com/wp-content/uploads/2026/01/1d73bf5c-6bb9-417c-abbf-75987b0b4459.png)


下载后，双击文件开始安装，然后，双击 Qoder IDE 图标启动 Qoder。


### Agent Mode vs. Quest Mode：怎么选？


Qoder 提供两种工作模式，适合不同场景：


| 对比维度 | Agent Mode（编辑器模式） | Quest Mode（任务模式） |
| --- | --- | --- |
| 交互方式 | 实时对话，逐步确认 | 委托执行，自主完成 |
| 适合任务 | 短周期调试、学习、小重构 | 复杂功能开发、长时间任务 |
| 人工介入 | 全程参与 | 最小干预 |
| 结果交付 | 边改边看 | 完整交付后审查 |

- Agent Mode 更像一个智能结对编程伙伴，适合快速重构、修 Bug、探索新库这类想随时掌控节奏的场景。
- Quest Mode 则让 Qoder 成为一个自主专家，你定义做什么，AI 负责怎么做。


---


## 切换到 Quest Mode

点击界面左上角的 Editor / Quest 切换按钮即可在两种模式间切换:


![](https://www.runoob.com/wp-content/uploads/2026/03/a2a7fc91-4210-4de8-b6d5-827264c5e61f.png)


界面如下所示：


![](https://www.runoob.com/wp-content/uploads/2026/03/bc1173bd-1f17-4a4f-800a-3c430ff5b5e2.png)


Quest 模式界面如下：

若想将 Quest Mode 设为默认模式，可进入 设置（Settings） > Quest Mode（Quest 模式），开启 "Quest 模式布局" 。


![](https://www.runoob.com/wp-content/uploads/2026/03/41c1d37f-849e-4d89-861b-15407f5b2528.png)


---


## 创建你的第一个 Quest 任务


### 点击 创建 Quest


在左侧任务列表顶部，点击 **创建 Quest** 按钮新建任务。


![](https://www.runoob.com/wp-content/uploads/2026/03/5b41e0e9-3255-4c70-8f10-e827a8a5a8bd.png)


### 2. 选择场景（Scenario）


Quest 提供三种场景，根据需求选择：


| 场景 | 适合场景 | Quest 行为 |
| --- | --- | --- |
| Spec 驱动 | 复杂功能、重构、严格质量控制 | 先对齐范围，设计实现方案和验收标准，再执行 |
| 原型探索 | 0-1 建站、快速原型 | 描述你的网站，Quest 自动搭建页面结构 |
| 创建工具 | 快速验证想法、创意实验 | 从想法出发，Quest 将其变为可运行的原型 |


![](https://www.runoob.com/wp-content/uploads/2026/03/f931adf2-ef7c-4466-bcc4-9d71f6492153.png)

**

小提示**：不确定选哪个？直接留空，Quest 会自动判断最适合的方式。一旦任务开始，场景就无法切换了。


---


## Spec 驱动模式


这是最适合正式开发任务的模式，完整流程如下：


### 第 1 步：需求澄清


输入任务后，Quest 可能会以多选题形式提出澄清问题。你可以让 Quest 自动选择默认答案，也可以手动选择后继续，或者直接跳过进入对话。


### 第 2 步：生成 Spec 文档


Quest 会自动生成一份结构化的 Spec 文档，包含：需求描述、设计方案、任务拆解、验收标准。Spec 文档展示在右侧输出区的 Spec Tab 中，支持流式输出和下载。


### 第 3 步：审查并修改 Spec


在右侧 Spec Tab 中查看完整文档，可通过对话修改 Spec（点击 Run 前都可以调整）。满意后点击 **Run Spec** 开始执行。


### 第 4 步：执行与监控


执行过程中，对话区会实时更新待办列表，输出区的 Changed Files Tab 可查看代码变更。你甚至可以在执行过程中，直接在输入框里追加新需求，Quest 会动态调整计划。


### 第 5 步：审查结果


执行完成后，根据环境不同有以下操作：


- **Local 模式**：Accept（应用所有变更）或 Reject（丢弃所有变更）
- **并行模式**：Apply（合并到主分支）
- **Remote 模式**：Create PR（创建 Pull Request）


---


## 原型探索/创建工具模式


这两种模式专为快速出成品设计，完全跳过 Spec 文档，直接进入执行阶段。


### 怎么描述你的想法？


直接用自然语言描述你想要的效果，例如：


- **网站**：创建一个旅行博客网站，包含首页、文章列表和详情页，使用现代设计风格和响应式布局
- **原型**：构建一个支持增删和标记完成的 Todo 应用，采用卡片式设计和优先级标签


### 后续流程


Quest 会自动选择技术栈，代码完成后自动运行预览。输出区的 Preview Tab 会实时展示运行结果，如果页面出错，Quest 会自动检查并修复。你可以继续对话来迭代调整，比如： 把主色改成蓝色、加一个搜索框、优化移动端显示。


---


## 执行环境选择


Quest 支持三种执行环境：


| 环境 | 特点 | 适合场景 |
| --- | --- | --- |
| Local | 直接修改主工作区，零启动成本 | 简单任务、快速验证 |
| Worktree | 在后台创建隐藏工作区，主分支保持干净 | 中等复杂任务、多任务并行 |
| Remote | 远程容器执行，本机可以关机 | 复杂长时间任务、资源密集型作业（需配置 GitHub 仓库） |


![](https://www.runoob.com/wp-content/uploads/2026/03/3148fa5e-620c-4b85-8018-89d80dcc31e6.png)

**

没有 Git 仓库时，默认只支持 Local 环境。


---


## 界面布局一览


Quest Mode 采用三栏布局：


- **左栏（任务列表）**：管理所有 Quest 任务，状态分为 Running / Action Required / Ready / Error
- **中栏（对话区）**：显示对话历史，执行期间实时更新待办列表
- **右栏（输出区）**：包含 Spec Tab（查看/下载 Spec）、Changed Files Tab（代码变更与 Accept/Reject）、Preview Tab（网站/原型的实时预览）


---


## 相关链接


- Qoder 官网：[https://qoder.com/](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)
- Qoder 文档：[https://docs.qoder.com/zh/quick-start](https://docs.qoder.com/zh/quick-start?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)
- Qoder Quest 模式：[https://docs.qoder.com/zh/user-guide/quest-mode](https://docs.qoder.com/zh/user-guide/quest-mode?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)








	  AI 思考中...





			** [OpenClaw 接入微信](https://www.runoob.com/openclaw-weixin.html)
			[TRAE 教程](https://www.runoob.com/trae-quick-star.html) **













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