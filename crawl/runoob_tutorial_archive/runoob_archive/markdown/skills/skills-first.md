# 第一个 Skill

- Source: https://www.runoob.com/skills/skills-first.html

让我们暂时忘掉复杂的创建过程，先从 **使用一个现成的 Skill** 开始，感受它带来的便利。


本文的演示基于 Claude Code，如果你还没安装，可以参考我们的 [Claude Code 教程](https://www.runoob.com/claude-code/claude-code-tutorial.html)。


### 创建 Skill 目录


Skills 存放在 **~/.claude/skills/**（个人全局）或项目目录下的 **.claude/skills/**（项目专用）。


本章节再项目目录下测试，先创建个目录 claude-test:


```
mkdir claude-test
```


进入该目录，创建 skills 的目录与文件：


```
mkdir -p .claude/skills/python-naming-standard
```


### 编写配置文件 SKILL.md


在目录下创建 SKILL.md，这是 Skill 的大脑 ，告诉 Claude 什么时候用它。


```
---
name: Python 内部命名规范技能
description: 当用户要求重构、审查或编写 Python 代码时，请参考此规范。
---

## 指令
1. 所有的内部辅助函数必须以 `_internal_` 前缀命名。
2. 如果发现不符合此规则的代码，请自动提出修改建议。
3. 在执行 `claude commit` 前，必须检查此规范。

## 参考示例
- 正确：`def _internal_calculate_risk():`
- 错误：`def _calculate_risk():`
```


字段要求：

- **name**：必须仅使用小写字母、数字和连字符（最多 64 个字符）
- **description**：Skill 的简要描述及其使用时机（最多 1024 个字符）


创建完后文件结构如下：


![](https://www.runoob.com/wp-content/uploads/2026/01/7d0592b4-61f8-4170-a639-6e83f6740cb6.png)


你的项目现在看起来应该是这样的：


```
my-project/
├─ src/
│  └─ test.py              # 项目源码
├─ .claude/
│  ├─ skills/
│  │  └─ hello-world/
│  │     ├─ skill.md       # Skill 定义（YAML + Instructions，机器可执行）
│  │     └─ README.md      # Skill 说明（人类阅读，可选）
│  └─ config.yml           # Claude 项目级配置（可选）
├─ .gitignore
└─ README.md               # 项目整体说明
```


接下来我们再终端执行以下命令启动 Claude Code：


```
claude
```



输入任务：


```
帮我写一个计算用户折扣的函数
```


Claude 就会会扫描已安装的 Skills，发现你的请求涉及 "Python 代码编写"，匹配了 python-naming-standard。


![](https://www.runoob.com/wp-content/uploads/2026/01/1527ed0b-d1a9-420a-8f25-c71231e23c05.png)


它会根据 SKILL.md 中的要求，生成如下代码：


```
def _internal_get_discount(user_score):
    # 计算逻辑...
    return discount
```


### 添加资源文件（可选）


另外我们可以在 **.claude/skills/** 下添加以下目录：


在同一文件夹添加：


- `examples/`：存放示例文件。
- `references/`：存放参考文档。
- `scripts/`：存放可执行脚本（例如 Python 处理 PDF）。


然后在 SKILL.md 中引用：


```
查看示例 commit：./examples/good-commit.txt
运行脚本：使用工具执行 ./scripts/process.py
```


---


## 官方市场


除了自己编写，你还可以利用 2025 年末发布的 Agent Skills 开放标准：


- 官方市场：访问 [https://github.com/anthropics/skills](https://github.com/anthropics/skills) 仓库下载预设的技能（如：React 优化器、SQL 调优工具）。
- Skill Creator：你可以对 Claude 说："帮我把我刚才教你的关于 Docker 的配置逻辑总结成一个 Skill"，它会自动在相应目录为你生成文件。


我们可以将本仓库注册为 Claude Code 的插件市场，只需在 Claude Code 中执行以下命令：


```
/plugin marketplace add anthropics/skills
```


![](https://www.runoob.com/wp-content/uploads/2026/01/780e9cce-ff89-4960-ab36-be41428a3899.png)


然后就可以使用 **/plugin **查看：


![](https://www.runoob.com/wp-content/uploads/2026/01/00814d49-4942-45b4-87e7-c14d682a7af5.png)


**安装指定技能集的步骤：**


- 浏览并安装插件（Browse and install plugins）
- 选择 anthropic-agent-skills 插件源
- 选择 document-skills（文档技能） 或 example-skills（示例技能）![](https://www.runoob.com/wp-content/uploads/2026/01/8c5a3a09-2943-49e0-b073-aa5385826510.png)
- 点击立即安装（Install now）![](https://www.runoob.com/wp-content/uploads/2026/01/45288835-7200-48a8-90f0-b9ce408a059d.png)


我们也可直接通过命令安装上述两类插件：


```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```


**注意：**使用插件安装的 skills 目录在 **～/claude/plugins/marketplaces/** 下。


插件安装完成后，需要重启一下 Claude Code。


使用的时候只需在指令中提及技能名称即可调用，例如安装 document-skills 插件后，可向 Claude Code 下达指令：


```
使用 PDF 技能提取 path/to/some-file.pdf 文件中的表单字段
```


或者创建一个 PPT：


```
创建一个 Agent Skill 的演示文稿
```


可以看到，调用了 **/document-skills:pptx**：


![](https://www.runoob.com/wp-content/uploads/2026/01/74f0eea5-9416-4a27-a827-2378896805c5.png)


开始生成：


![](https://www.runoob.com/wp-content/uploads/2026/01/f5a9c860-9291-4d3f-b72e-7af1ad80a528.png)

之后就会告诉你生成的文件位置：


![](https://www.runoob.com/wp-content/uploads/2026/01/dc42fb40-b5ad-476d-aa64-bdec040f752e.png)








	  AI 思考中...





			** [Skills 基本结构](https://www.runoob.com/skills/skills-structure.html)
			[Skills 工作原理](https://www.runoob.com/skills/how-skills-work.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#c3a2a7aeaaad83b1b6adacaca1eda0acae)

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