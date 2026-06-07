# VS Code 创建与使用 Skill

- Source: https://www.runoob.com/skills/vs-code-skill.html

本教程将带你从头开始创建一个 Agent Skill，并在 VS Code + GitHub Copilot 中实际运行它。


我们将创建一个掷骰子 Skill，让 Agent 学会通过终端命令生成随机数。


---


## 准备工作


### 环境要求


- 安装 [VS Code](https://code.visualstudio.com/)
- 安装 [GitHub Copilot 扩展](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) ![](https://www.runoob.com/wp-content/uploads/2026/04/6cc36f45-f6a8-4e1a-9b78-9a56a2460a6b.png)


**
本教程使用 VS Code，但 Agent Skills 是开放格式。相同的 Skill 也可以在 Claude Code、OpenCode、OpenAI Codex 等兼容工具中使用。


更多 VS Code 内容可以参考：[VS Code 教程](https://www.runoob.com/../vscode/vscode-tutorial.html)。


---


## 创建 Skill 目录和文件


VS Code 默认在项目的 **.agents/skills/** 目录下查找 Skill。


首先在你的项目中创建以下目录结构：


## 创建目录结构


```
# 在项目根目录执行
mkdir -p .agents/skills/roll-dice
```


然后在 **.agents/skills/roll-dice/SKILL.md** 中创建以下文件：


## 实例：SKILL.md 完整内容


```
---
name: roll-dice
description: 使用随机数生成器掷骰子。当用户要求掷骰子（d6、d20 等）或生成随机骰子点数时使用。
---

# 掷骰子方法

使用以下 shell 命令生成 1 到指定面数之间的随机数：

## macOS / Linux

```bash
echo $((RANDOM % <sides> + 1))
```

## Windows PowerShell

```powershell
Get-Random -Minimum 1 -Maximum (<sides> + 1)
```

**用法说明：**
将 `<sides>` 替换为用户指定的骰子面数：
- d6：将 `<sides>` 替换为 6
- d20：将 `<sides>` 替换为 20
- 其他面数以此类推

**输出：** 直接返回随机结果数字即可，无需额外解释。
```


一个文件、不到 20 行，就完成了一个完整的 Skill。


![](https://www.runoob.com/wp-content/uploads/2026/04/113748f7-8f18-4eeb-97b1-42724b8bf495.png)


---


## 文件结构解析


让我们逐部分理解这个文件的作用。


### YAML 头部（Frontmatter）


| 字段 | 作用 | 说明 |
| --- | --- | --- |
| name | Skill 的唯一标识 | 必须与文件夹名称完全一致，使用小写字母和连字符 |
| description | 触发条件描述 | 告诉 Agent 什么时候应该使用这个 Skill，这是 Agent 决定是否激活的关键字段 |


### 正文（Markdown Body）


正文是 Agent 激活 Skill 后实际遵循的指令。


这里我们告诉 Agent：当用户要求掷骰子时，使用操作系统的随机数命令，并把骰子面数传入命令中。


我们同时提供了 macOS/Linux 和 Windows 两种平台的命令，Agent 会根据当前环境自动选择。


---


## 测试你的 Skill


创建好文件后，按以下步骤验证：


- 用 VS Code 打开你的项目
- 打开 Copilot Chat 面板（快捷键 Ctrl+Shift+I 或 Cmd+Shift+I），或者点击右上角的按钮： ![](https://www.runoob.com/wp-content/uploads/2026/04/34d70eba-a6d8-42a6-b2a2-c8db13cee663.png)
- 在聊天面板底部选择 **Agent** 模式
- 输入 **/skills** 命令，确认 roll-dice 出现在 Skill 列表中 ![](https://www.runoob.com/wp-content/uploads/2026/04/50037cde-8856-4e94-9ae0-19c405864ffd.png)
- 可以看到技能列表有 roll-dice： ![](https://www.runoob.com/wp-content/uploads/2026/04/05bde6d6-a75e-44a2-ac0d-424439af19d6.png)


> 如果在 /skills 列表中看不到 roll-dice，请检查文件路径是否正确：**.agents/skills/roll-dice/SKILL.md**，注意 SKILL.md 必须大写。


确认 Skill 已加载后，在聊天中输入：


```
Roll a d20
```


Agent 应该会自动激活 roll-dice Skill，运行终端命令并返回 1 到 20 之间的随机数。


![](https://www.runoob.com/wp-content/uploads/2026/04/23fd0b3b-6f04-46ff-a25d-42daf6be2d93.png)


---


## 背后的工作过程


当你在 Copilot Chat 中使用这个 Skill 时，底层经历了三个步骤：


### 步骤一：发现


聊天会话开始时，Agent 扫描默认 Skill 目录（.agents/skills/），找到了 roll-dice。


它只读取了 name 和 description，知道了"这个 Skill 是用来掷骰子的"。


### 步骤二：激活


当你输入 "Roll a d20" 时，Agent 将你的问题与 roll-dice 的 description 进行了匹配。


匹配成功后，Agent 将完整的 SKILL.md 正文加载到了上下文中。


### 步骤三：执行


Agent 按照正文中的指令，识别出你用的是 macOS（或 Linux），选择了 bash 命令。


它将 d20 对应的 20 替换到命令中，执行 **echo $((RANDOM % 20 + 1))**，然后把结果返回给你。


---


## 常见问题排查


| 问题 | 可能原因 | 解决方法 |
| --- | --- | --- |
| /skills 列表为空 | SKILL.md 文件路径不正确 | 确认文件在项目的 .agents/skills/roll-dice/ 目录下 |
| Agent 没有运行命令 | 模型工具调用可靠性差异 | 尝试更换模型，或更明确地说"帮我掷一个 d20" |
| 命令执行失败 | Shell 环境差异 | 确认在 macOS/Linux 终端中能正常执行 $RANDOM 命令 |


---


## 跨工具使用提示


虽然本教程使用 VS Code，但 Skill 同样可以用于其他工具：


| 工具 | Skill 存放位置 |
| --- | --- |
| VS Code + Copilot | .agents/skills/ 或 .github/copilot/ |
| Claude Code | .claude/skills/ 或 ~/.claude/skills/ |
| OpenAI Codex | .codex/skills/ |


不同的工具可能使用不同的默认目录，但 Skill 本身的格式和文件结构是通用的。









	  AI 思考中...





			** [Skills 脚本扩展](https://www.runoob.com/skills-scripts.html)














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