# OpenClaw 接入飞书

- Source: https://www.runoob.com/ai-agent/openclaw-feishu.html

OpenClaw（原 Clawdbot）是一个开源、本地优先的 AI 代理网关，能让大模型在你的电脑/服务器上 7X24 小时运行，支持直接操作电脑、浏览网页、执行命令，还能无缝接入飞书、Telegram、Discord 等聊天平台。

本章节我们将 OpenClaw 接入飞书，实现消息推送、发图、收文件，审批交互、数据同步等自动化场景。


如果你还没安装 OpenClaw，需要先安装：


使用 npm 命令全局安装：


```
npm install -g openclaw@latest --registry=https://registry.npmmirror.com
```


或使用 pnpm 命令安装：


```
pnpm add -g openclaw@latest
```


OpenClaw 安装可以详细参考：[OpenClaw (Clawdbot) 教程](https://www.runoob.com/openclaw-clawdbot-tutorial.html)。


### 安装飞书官方插件

新版本 OpenClaw 已内置支持，我们可以使用以下命令来启用：


```
openclaw plugins enable feishu
```


接下来我们可以使用 **openclaw plugins list** 命令来查看是否已启用，**disabled** 是禁用，**loaded** 是启用：


![](https://www.runoob.com/wp-content/uploads/2026/03/d2db3e7d-b9e2-4f8e-927a-a9cf8e852c8c.png)


### 在飞书开放平台创建机器人


打开飞书开放平台 [https://open.feishu.cn/app](https://open.feishu.cn/app)
点击"创建企业自建应用"：


![](https://www.runoob.com/wp-content/uploads/2026/03/e3245f89-0e1d-40ec-8af5-fd40b6489d54.png)

填应用名称（如 "我的 OpenClaw AI"），描述 + 图标随意：


![](https://www.runoob.com/wp-content/uploads/2026/03/5661b9b0-93a9-48b2-97ea-7f4c7614ea70.png)

复制凭证 **App ID** 和 **App Secret**，后面要用到：


![](https://www.runoob.com/wp-content/uploads/2026/03/b578b9ef-2e2b-4316-b78c-1c5dddf9bf1d.png)


接下来重新回到终端 输入以下命令配置 channel：


```
openclaw channels add
```


选择 "Feishu/Lark (飞书) (needs app creds)"：


![](https://www.runoob.com/wp-content/uploads/2026/03/add573a5-8342-4332-b2a7-b89362402d62.png)


选择 "Enter App Secret"：


![](https://www.runoob.com/wp-content/uploads/2026/03/967eb1e9-1984-4784-b3b5-ceb8396d71a7.png)


分别输入我们之前在飞书创建应用的 **App Secret** 和 **App ID**：


![](https://www.runoob.com/wp-content/uploads/2026/03/8b4eeaae-2408-424d-9cce-46b250cd01ec-1.png)


设置连接模式，并使用国内域名：


![](https://www.runoob.com/wp-content/uploads/2026/03/6cb56d0d-d0bd-41ad-9516-049e27bbf443.png)


接下来的群聊策略选择 Open，这样可以响应所有的群聊：


![](https://www.runoob.com/wp-content/uploads/2026/03/f7f2db70-2a84-48f3-a3ca-d06e8d84a432.png)


如果选择 Allowlist，只会在白名单的群聊可以响应。

选择往后，回到菜单选择 **Finished** ，然后其他按默认回车即可，这样就就完成了飞书的配置。


![](https://www.runoob.com/wp-content/uploads/2026/03/37057643-fb18-4f2f-b2ac-5fc9325fdd44.png)

回到网页端，查看频道选项，可以看到飞书已经启用：


![](https://www.runoob.com/wp-content/uploads/2026/03/71e55bda-9a30-46c4-b1e3-6355ed766eef.png)


### 启用机器人能力


接下来回到我们飞书创建的应用界面，左侧菜单 → 添加应用能力 → 机器人，点击"添加"按钮，开启机器人能力：


![](https://www.runoob.com/wp-content/uploads/2026/03/7bc95219-1edf-49c5-a6c0-59fdd1289341.png)


配置权限，左侧 → 权限管理 → 批量批量导入/导出权限：


![](https://www.runoob.com/wp-content/uploads/2026/03/564686cc-f2ba-4707-b428-bd21889f354f.png)


粘贴以下 JSON：


```
{
  "scopes": {
    "tenant": [
      "aily:file:read",
      "aily:file:write",
      "application:application.app_message_stats.overview:readonly",
      "application:application:self_manage",
      "application:bot.menu:write",
      "cardkit:card:read",
      "cardkit:card:write",
      "contact:user.employee_id:readonly",
      "corehr:file:download",
      "event:ip_list",
      "im:chat.access_event.bot_p2p_chat:read",
      "im:chat.members:bot_access",
      "im:message",
      "im:message.group_at_msg:readonly",
      "im:message.p2p_msg:readonly",
      "im:message:readonly",
      "im:message:send_as_bot",
      "im:resource"
    ],
    "user": ["aily:file:read", "aily:file:write", "im:chat.access_event.bot_p2p_chat:read"]
  }
}
```


![](https://www.runoob.com/wp-content/uploads/2026/03/fa7bcb68-7a83-4c7f-a265-b60b026e5d27.png)

权限列表：


![](https://www.runoob.com/wp-content/uploads/2026/03/20397c41-14b4-43f2-8f79-3d63bee5e9ba.png)


### 配置事件订阅

接下来我们需要为应用订阅相关事件，在左侧菜单选择事件与回调 → 事件配置：


![](https://www.runoob.com/wp-content/uploads/2026/03/97cec55e-f71c-47d8-af4c-9d19d7cf3e3a.png)

订阅方式使用长连接接收事件（WebSocket）,然后保存。


添加以下事件：

- im.message.receive_v1- 接收消息
- im.message.message_read_v1- 消息已读回执
- im.chat.member.bot.added_v1- 机器人进群
- im.chat.member.bot.deleted_v1- 机器人被移出群


![](https://www.runoob.com/wp-content/uploads/2026/03/0653af62-908e-434e-88e0-0996d130deb4.png)

已添加事件列表：


![](https://www.runoob.com/wp-content/uploads/2026/03/592afc7c-9d22-4d5f-9efe-ef4f5868db04.png)


### 发布应用

左侧 → 版本管理与发布 → 创建版本 → 提交审核 → 发布：


![](https://www.runoob.com/wp-content/uploads/2026/03/c3e8cf93-9f29-4a20-8fd0-755dd665f3a0-scaled.png)


发布信息：


![](https://www.runoob.com/wp-content/uploads/2026/03/ecb7163e-f619-49a7-a703-e740267630ef.png)


### 启动并测试


启动 openclaw：


```
openclaw gateway
或
openclaw gateway --port 18789
```


使用飞书创建一个测试群：


![](https://www.runoob.com/wp-content/uploads/2026/03/39189684-47f7-4545-bd27-9530b46da3a1.png)


在群组的设置中添加我们刚才创建的机器人：


![](https://www.runoob.com/wp-content/uploads/2026/03/2b385605-dfd8-43bd-aa1e-cd833a82fd85.png)

接下来我们就可以和 OpenClaw 开始聊天， 可以 @ 它让它介绍下自己，正常回复说明流程跑通了：


![](https://www.runoob.com/wp-content/uploads/2026/03/b0bf785c-660e-4c8b-865e-e2d7b695166e.png)








	  AI 思考中...





			** [AI Agent 问答实例](https://www.runoob.com/ai-agent-answer-demo.html)
			[OpenCode Coding Plan](https://www.runoob.com/opencode-coding-plan.html) **


















    **















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