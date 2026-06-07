# AI 开发平台 MonkeyCode

- Source: https://www.runoob.com/ai-agent/ai-monkeycode.html

MonkeyCode 是由长亭科技推出的企业级 AI 开发平台，致力于为开发者提供更专业、更可靠、更可扩展的 AI Coding 体验。


MonkeyCode 不只是一个 AI 编程工具，而是一个面向专业团队的 AI 研发基础设施，它覆盖了 需求 → 设计 → 开发 → Review 全流程，提供了安全、隔离、可并行的开发环境。

---


## 注册与登录


  **


    **
      首次使用 MonkeyCode，先完成账号注册。
      点击
      [进入官网](https://monkeycode-ai.com/?ic=019d94af-c5d0-7207-a923-89d7ccf67d91)
      ，右上角注册或直接登录，成功后会自动进入主界面开始使用。
    **



进入页面后，点击右上角 **注册** 创建新账号；已有账号可直接登录使用。


![](https://www.runoob.com/wp-content/uploads/2026/04/4fd1470f-fa02-4d34-851d-e3060c080a88.png)


注册完成后，系统会自动跳转至主界面，无需额外操作。


![](https://www.runoob.com/wp-content/uploads/2026/04/39fa238f-e55e-4b9b-858e-fe61e99a1316.png)

可以看到，这里还有很多 Skills 可以用：

![](https://www.runoob.com/wp-content/uploads/2026/04/3f93ec50-9d38-4408-8d6a-ab3255079bf6.png)


### 在线制作个简单的应用


测试个应用，输入以下内容：


```
制作一个工作留痕记录的在线工具，记录每一天的工作进展，建立完整的工作轨迹档案
```


还提供了很多模型，MiniMax2.7 还是免费的：


![](https://www.runoob.com/wp-content/uploads/2026/04/03bc3ed0-0441-4d0d-9316-88f81f8867d7.png)


接下来就会开始启动制作：


![](https://www.runoob.com/wp-content/uploads/2026/04/fe1ed4f0-7203-4a9a-90d3-1ff1d1ffa9c8.png)

制作完成后直接在线访问：


![](https://www.runoob.com/wp-content/uploads/2025/12/276bfbe7-433a-4acf-8ffc-ce05536af665.png)


效果如下：


![](https://www.runoob.com/wp-content/uploads/2026/04/05b49078-0aa8-4356-a7f7-c0519c648062.png)


添加功能测试：


![](https://www.runoob.com/wp-content/uploads/2026/04/748bab54-8f28-4a6a-9f8f-ab2c330461c9.png)


效果如下：


![](https://www.runoob.com/wp-content/uploads/2026/04/8d36f53a-e23b-409b-a97c-473b0f48442d.png)


---


## 配置说明

在执行具体任务前，需完成平台基础配置，包括仓库、大模型、系统镜像及宿主机的绑定操作，配置入口位于平台左下角。


### 1、Git 平台身份凭证绑定


需先在对应 Git 平台完成代码仓库的创建，再在 MonkeyCode 中选择目标平台完成凭证绑定，确保仓库地址与权限配置准确，为后续代码操作提供基础支撑。


![](https://www.runoob.com/wp-content/uploads/2026/04/4de73e17-c0b1-4a48-9e86-37184699476b.png)


注意账号中要有公开仓库，才能够进行绑定。


### 2、大模型绑定


**默认推荐：**若无特殊业务需求，可直接使用平台内置的免费模型 MiniMax-M2.7，该模型为平台综合对比国内主流大模型后，筛选出的效果均衡、适配性强的版本。

专业版模型：提供了 gpt、minimax、glm、kimi、mimo、deepseek 等多种模型，使用时会消耗账号点数。左下角点击积分可以进行充值。


![](https://www.runoob.com/wp-content/uploads/2026/04/73bcfa56-177f-4636-a96e-fd1b579a9b0e.png)


** 自定义绑定：**若需使用其他大模型，可在对应配置模块填写模型 API Token 完成绑定，支持主流大模型的接入适配。


![](https://www.runoob.com/wp-content/uploads/2026/04/c7bb6339-cc18-4857-b9e8-6af504bfb424.png)


在此处填写API token即可。


### 3、系统镜像与宿主机绑定，开发环境创建


针对有特定运行环境需求的项目，可通过该模块配置独立的开发环境，适配不同技术栈、系统版本的项目诉求：


选择目标环境模板，初始化环境配置：


![](https://www.runoob.com/wp-content/uploads/2026/04/9efd2f27-c662-4fd6-8c2d-3238fc55469b.png)


确认环境参数，完成个性化开发环境的创建：


![](https://www.runoob.com/wp-content/uploads/2026/04/b3e70cbd-b39d-4333-a419-a1985fd91be9.png)


![](https://www.runoob.com/wp-content/uploads/2026/04/7abde5d7-c245-4c5a-88f2-decdd6347e78.png)


---


## 执行任务

平台支持两种任务启动方式，可根据实际场景选择，核心目标为通过自然语言需求驱动代码开发、调试等操作。

基础版支持运行同时执行 1 个任务，专业版支持同时执行 3 个任务。


![](https://www.runoob.com/wp-content/uploads/2026/04/ab790f99-3f76-4d6b-ba71-fdb9dd4b0090.png)


### 启动方式一：直接输入需求


在主界面对话框中精准描述任务需求（如功能开发、Bug 修复、代码优化等），并可根据项目类型选择匹配的技能模板，提交后平台将自动解析需求并执行。


![](https://www.runoob.com/wp-content/uploads/2026/04/43f050b1-486c-436a-a075-33c1899ce548.png)


### 启动方式二：绑定仓库项目执行


- 在左侧栏选择"添加项目"；
- 确认目标仓库地址、分支信息（需确保仓库地址配置正确，且平台账号具备足够的仓库操作权限）；
- 提交任务需求，平台将基于指定仓库分支执行操作。


![](https://www.runoob.com/wp-content/uploads/2026/04/9d0983be-010f-4049-be5d-0dd12608497b.png)


选定后可以看到仓库相关信息，修改完配置后，点击 "启动 AI" 即可开始任务。


![](https://www.runoob.com/wp-content/uploads/2026/04/e534b438-c0c9-471f-9601-afc40e8baaa8.png)


开始前选择需要使用的模型与环境。免费版默认 minimax2.7，专业版可以切换更多模型。


![](https://www.runoob.com/wp-content/uploads/2026/04/fe26f04d-a46a-4fef-8bd8-955d07f3c0e1.png)


---


## 平台使用说明


### 界面交互说明

**实时交互：**任务执行过程中，可在对话框中补充需求、调整指令，平台将实时响应并优化执行结果；右下角可以看到执行时间，左上角为其他功能按键。


![](https://www.runoob.com/wp-content/uploads/2026/04/b6d20593-ce02-4c17-9370-d56a287bdfb1.png)


** 进度可视化：**任务执行期间，界面将展示详细的执行步骤、各步骤耗时，右侧面板可查看项目文件结构、变更文件预览等核心信息。在"文件"中上传或下载需要文件，在"终端"采用终端命令的方式进行测试。


![](https://www.runoob.com/wp-content/uploads/2026/04/120e1018-368e-4094-b655-aff818a38641.png)


### 功能操作说明

环境时长已进行优化，正常执行开发任务的过程中，开发环境会长期保留，不再需要手动续期；普通版可同时运行一个任务，专业版至多支持三个。


在线预览：除文件内容预览外，平台支持项目在线运行预览，点击「预览」按钮即可通过开发端口查看项目运行效果。


![](https://www.runoob.com/wp-content/uploads/2026/04/b4120c0e-ba57-4713-a9d6-c4e9571f28c9.png)


结果保存：任务执行结束后，平台将提示修改文件数量及保存（文件列表中会以红点标注），推送至远端仓库。也可以手动下载至本地。


![](https://www.runoob.com/wp-content/uploads/2026/04/0b0a23a0-d5a5-405f-9c5a-0e17c5711793.png)








	  AI 思考中...





			** [Hermes Agent 配置](https://www.runoob.com/hermes-agent-setup.html)
			[推理与规划（Reasoning & Planning）](https://www.runoob.com/reasoning-planning.html) **













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