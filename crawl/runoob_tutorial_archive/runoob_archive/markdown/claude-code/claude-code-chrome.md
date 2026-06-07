# Claude Code 控制 Chrome 浏览器

- Source: https://www.runoob.com/claude-code/claude-code-chrome.html

Claude Code 的 Chrome 集成功能，让你可以直接从命令行（CLI）或 VS Code 扩展中控制浏览器。Claude 能够：


- 打开网页、点击按钮、填写表单
- 读取浏览器控制台日志（console errors、network requests、DOM 状态）
- 与任何你已登录的网站交互（Gmail、Notion、Google Docs 等）
- 录制浏览器操作为 GIF 文件
- 在多个标签页之间协同工作


**核心优势**：Claude 共享你浏览器的登录状态，无需额外的 API 密钥或重新认证。


**
这个功能目前处于 Beta 阶段，允许你在终端（CLI）或 VS Code 中用自然语言指令，让 Claude 直接控制你的 Chrome 浏览器，进行导航、点击、输入、调试、数据提取等操作，无需手动切换窗口。

---


## 安装与准备


### 前置条件


使用该功能前，你需要满足以下要求：


| 条件 | 说明 |
| --- | --- |
| Claude Code 版本 | v2.0.73 或更高 |
| Chrome 扩展版本 | Claude in Chrome v1.0.36 或更高 |
| Anthropic 账户 | 需要直接付费计划（Pro、Max、Teams 或 Enterprise） |
| 不支持的渠道 | 通过 Amazon Bedrock、Google Vertex AI、Microsoft Foundry 访问的用户不可用 |


### 安装步骤



1. 安装浏览器扩展**：


- 打开 Chrome/Edge，访问 [Chrome Web Store - Claude](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)。
- 点击"添加至 Chrome"并安装。
- 安装后建议重启浏览器，确保 Native Messaging Host 正确加载。


![](https://www.runoob.com/wp-content/uploads/2026/03/8f9ff3fd-6d17-4058-9e37-97cbc03445a3.png)


**2. 安装/更新 Claude Code**：


- 按照官方快速入门安装 Claude Code（CLI 或 VS Code 扩展）。



**3. 权限与连接**：


- 首次运行时，扩展会自动安装 Native Messaging Host。
- 常见路径（macOS 示例）：`~/Library/Application Support/Google/Chrome/NativeMessagingHosts/com.anthropic.claude_code_browser_extension.json`


---


## 如何启动并连接


#### 在 CLI 中启动


- **推荐方式**：直接带 Chrome 启动
```
claude --chrome
```

- 或在已有会话中启用：
```
/chrome
```
 然后选择启用或重新连接。
- **设为默认**（方便但会增加上下文消耗）： 在 `/chrome` 菜单中选择 "Enabled by default"。


### 在 VS Code 中使用


- 在提示框中输入 `**@browser**` + 你的指令，例如：
```
@browser 打开 localhost:3000，检查控制台是否有错误
```


### 检查连接状态


在 Claude Code 会话中输入 `/chrome`，可以查看状态、管理权限、重新连接扩展。

---


## 基本使用方法


Claude Code 通过**自然语言提示**控制浏览器，无需编写复杂代码。Claude 会自动解析你的指令，执行相应操作，并返回结果（包括截图、控制台日志、提取的数据等）。


**核心能力**：


- 导航：打开网址
- 交互：点击元素、输入文字、滚动页面
- 读取：查看 DOM、控制台错误、网络请求
- 自动化：表单填写、数据提取、跨标签页操作
- 其他：录制 GIF 演示、保存 CSV 等


**提示技巧**：


- 描述要清晰、逐步（例如"先打开网址，然后点击搜索框，输入 XXX 并告诉我结果"）。
- 可以结合本地文件（如读取 CSV 批量操作）。
- 长任务时，Claude 会分步执行并报告进度。

---

## 实用示例


**示例 1：简单导航与交互**


```
去到 https://www.baidu.com，点击搜索框，输入 "python"，告诉我出现的搜索结果。
```


**示例 2：本地网页测试与调试**


```
我刚更新了登录表单验证。请打开 localhost:3000，用无效数据提交表单，检查错误消息是否正确显示，并查看控制台日志。
```


**示例 3：表单自动化（结合本地文件）**


```
我有一个 contacts.csv 文件，里面有客户联系方式。对于每一行，打开 crm.example.com，点击“添加联系人”，填写姓名、邮箱和电话，然后提交。
```


**示例 4：Google Docs 等已登录网站操作**


```
根据最近的 Git 提交，起草一份项目更新，并添加到我的 Google Doc（网址：docs.google.com/document/d/abc123）。
```


**示例 5：数据提取与保存**


```
打开产品列表页面，提取每个商品的名称、价格和库存状态，保存为 CSV 文件。
```


**示例 6：录制演示 GIF**


```
录制一个 GIF，展示从购物车添加商品到结账确认的完整流程。
```


**示例 7：多站点工作流**


```
查看我明天的日历，对于每个有外部参会者的会议，查找他们公司的网站并添加备注。
```









	  AI 思考中...





			** [Claude Code 项目目录结构](https://www.runoob.com/claude-code-project.html)
			[CLAUDE.md 使用指南](https://www.runoob.com/claude-code-claudemd.html) **













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