# Claude Code 控制与模式

- Source: https://www.runoob.com/claude-code/claude-code-control.html

Claude Code 交互模式的核心能力包括**键盘快捷键**、**Vim 编辑模式**、**命令历史管理**和**后台 Bash 命令运行**，以下是提炼后的关键内容：

---


## 一、 键盘快捷键


快捷键效果因终端和系统而异，macOS 用户需将 Option 键配置为 Meta（不同终端配置路径见原文），按 `?` 可查看当前环境可用快捷键。


| 分类 | 快捷键/操作 | 核心功能 |
| --- | --- | --- |
| 常规控制 | Ctrl+C | 取消当前输入/生成 |
|  | Ctrl+D | 退出会话 |
|  | Ctrl+L | 清屏（保留历史） |
|  | Ctrl+O | 切换详细输出（显示工具执行日志） |
|  | Ctrl+R | 反向搜索命令历史 |
|  | Option+P/Alt+P | 切换模型（不清空提示） |
| 文本编辑 | Ctrl+K/Ctrl+U | 删除到行尾/删除整行（删除内容可粘贴） |
|  | Ctrl+Y | 粘贴 Ctrl+K/Ctrl+U 删除的内容 |
|  | Alt+B/Alt+F | 光标按单词前后移动（需 Meta 键配置） |
| 主题显示 | Ctrl+T | 切换代码块语法高亮（仅 /theme 菜单内有效） |
| 多行输入 | \+Enter / Shift+Enter` | 换行输入（Shift+Enter 在 iTerm2/WezTerm 等终端免配置） |
|  | Ctrl+J | 多行换行符 |
| 快速命令 | / 开头 | 触发斜杠命令（详见斜杠命令文档） |
|  | ! 开头 | 直接运行 Bash 命令（输出计入会话） |
|  | @ | 触发文件路径自动补全 |

---


## 二、 Vim 编辑器模式


通过 `/vim` 临时启用，或 `/config` 永久配置，支持 Vim 核心操作逻辑。


**1、模式切换**


| 命令 | 操作 | 触发场景 |
| --- | --- | --- |
| Esc | 进入 NORMAL 模式 | INSERT 模式下 |
| i/I | 光标前/行首插入 | NORMAL 模式下 |
| a/A | 光标后/行尾插入 | NORMAL 模式下 |
| o/O | 下方/上方新开一行 | NORMAL 模式下 |


**2、核心操作（NORMAL 模式）**


- **导航**：`h/j/k/l` 上下左右移动；`w/e/b` 按单词跳转；`gg/G` 跳转到输入开头/结尾
- **编辑**：`dd` 删除行；`yy` 复制行；`p/P` 光标后/前粘贴；`>>/







	  AI 思考中...





			** [Claude Code CLI 参考手册](https://www.runoob.com/claude-code-cli-ref.html)
			[Claude Code 斜杠 / 命令](https://www.runoob.com/claude-code-slash-commands.html) **













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