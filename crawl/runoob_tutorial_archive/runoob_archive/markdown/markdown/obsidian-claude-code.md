# Obsidian + Claude Code

- Source: https://www.runoob.com/markdown/obsidian-claude-code.html

Obsidian 是一款本地优先的 Markdown 笔记软件，其所有数据均存储在本地文件夹（称为Vault 库），以纯文本格式（.md）保存，既保证隐私安全，又支持离线使用，同时具备强大的双向链接、插件扩展能力，是编程爱好者管理代码、整理学习笔记的首选工具，尤其适合需要长期沉淀、频繁查阅代码片段和技术笔记的场景。

Claude Code 是 Anthropic 公司推出的 AI 编程助手，基于 Claude 大模型优化而来，主打代码理解、调试、优化、生成等核心能力。


我么可以在 Obsidian 中安装 Claude Code，让 AI 帮我们写文档、整理我办和项目进度、自动推送当天 AI 热点资讯等功能


关于 Obsidian 和 Claude Code 详细内容参考：

- Obsidian 教程：[https://www.runoob.com/markdown/md-tutorial.html](https://www.runoob.com/md-tutorial.html)
- Claude Code 教程：[https://www.runoob.com/claude-code/claude-code-tutorial.html](https://www.runoob.com/../claude-code/claude-code-tutorial.html)


### 1、Obsidian 下载

我们需要先去 Obsidian 官方网站 [https://obsidian.md/download](https://obsidian.md/download) 下载 Obsidian，提供了各种系统版本:


![](https://www.runoob.com/wp-content/uploads/2026/02/500d33bf-7b0d-4faa-9a8c-6ed906569a99.png)


### 2、安装 Claude Code


终端执行（全局安装一次就好）：


```
npm install -g @anthropic-ai/claude-code
```


安装完成后，运行一次授权：


```
claude
```


它会让你登录 Claude 账号，完成 OAuth 授权（只需要做一次）。

** 注意：**如果没有 Claude 账号，我们也可以用国内的大模型代替，参考：[Claude Code API 配置](https://www.runoob.com/../claude-code/claude-code-setup.html)。


### 3、安装 Obsidian 社区插件 Claudian


我们可以从 GitHub Release [https://github.com/YishenTu/claudian/releases/latest](https://github.com/YishenTu/claudian/releases/latest) 下载 **main.js、manifest.json 和 styles.css** 这三个文件：


![](https://www.runoob.com/wp-content/uploads/2026/02/1e16e925-9c4f-427d-b083-1264dc5bb0e1.png)


在你的 Obsidian 库的插件文件夹 **plugins** 中（如果没有创建一个），新建一个名为 **claudian** 的文件夹，路径示例：


```
/path/to/vault/.obsidian/plugins/claudian/
```


**注：****/path/to/vault/** 需替换为你自己的 Obsidian 库实际路径。


仓库管理菜单可以看到详细的路径：


![](https://www.runoob.com/wp-content/uploads/2026/02/37ad34de-46b4-4881-b7e4-62e3c3c3f43a.png)


将下载好的三个文件复制到这个 **claudian/plugins/** 文件夹中。


```
.obsidian/
└── plugins/
    └── claudian/
        ├── main.js         # 插件的编译后 JavaScript 主文件（包含所有逻辑）
        ├── manifest.json   # 插件元数据（ID、名称、版本、描述、最低 Obsidian 版本等）
        └── styles.css      # 插件的 CSS 样式
```


![](https://www.runoob.com/wp-content/uploads/2026/02/9617d366-9cb9-4f03-9df0-abb838fac4b6.png)


在 Obsidian 中启用该插件：设置 → 社区插件 → 开启「Claudian」插件开关。


![](https://www.runoob.com/wp-content/uploads/2026/02/c4dd25ea-a49a-46ae-9442-267d8b212e4f.png)


---


## 第一次使用 Claudian

打开任意笔记，左侧边栏会出现一个 机器人图标（或用命令面板 Ctrl/Cmd+P 输入 Claudian: Open Chat）:


![](https://www.runoob.com/wp-content/uploads/2026/02/2333faf8-13a6-4e06-8207-f7a5043836e3.png)


第一次打开会提示你选择 Claude 模型（可以设置国内的大模型），输入框打 / 会出现所有可用技能（skills）：


![](https://www.runoob.com/wp-content/uploads/2026/02/edd40563-697a-41c8-b62d-ccfc111a5f4e.png)


测试：


```
写一篇新笔记（最常用场景）text帮我写一篇关于「2026年最值得关注的5个AI编程工具」的文献笔记，格式用我 vault 里最常用的文献笔记模板，从今天更新的网页抓取信息
```


接下来就开始正常干活了：


![](https://www.runoob.com/wp-content/uploads/2026/02/6f08996e-ee76-422c-b1a6-8eda20caf63a.png)








	  AI 思考中...





			** [Obsidian 使用教程](https://www.runoob.com/obsidian-tutorial.html)














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