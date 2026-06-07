# Claude Code 检查点

- Source: https://www.runoob.com/claude-code/claude-code-checkpointing.html

检查点是 Claude Code 的**代码安全回退工具**，能自动跟踪 Claude 对文件的编辑操作，帮你快速撤销不需要的更改，避免代码改坏后难以恢复。


## 检查点的工作原理


检查点会在你使用 Claude Code 时**自动后台运行**，全程无需手动配置：


- **自动创建**：每次发送用户提示后，都会自动创建一个检查点，记录当前的代码状态
- **持久保存**：检查点会在会话之间保留，即使关闭会话，下次恢复后仍能访问历史检查点
- **自动清理**：超过 30 天的检查点会自动删除（清理时间可配置）

**

注意：仅跟踪 Claude 通过文件编辑工具** 做出的直接修改，其他方式的更改不会被记录。


---


## 如何使用检查点回退更改


### 1. 打开回退菜单


有两种触发方式，任选其一：


- 快捷键：按两次 `Esc`（`Esc` + `Esc`）
- 斜杠命令：输入 `/rewind`


### 2. 选择回退类型


打开菜单后，可根据需求选择三种回退模式：


| 回退类型 | 效果 | 适用场景 |
| --- | --- | --- |
| 仅对话 | 回退到历史对话内容，保留当前代码更改 | 觉得对话方向跑偏，想重新提问，但代码改得没问题 |
| 仅代码 | 恢复文件到历史状态，保留当前对话 | 代码改坏了，但想继续基于当前对话调整 |
| 代码和对话 | 同时回退代码和对话到之前的状态 | 想彻底推倒重来，回到某个满意的节点 |

---


## 常见用例


检查点特别适合以下开发场景：


- **探索多种方案**：尝试不同的代码实现思路，不满意就一键回退到起点，再换另一种方案
- **快速修复失误**：当 Claude 的修改引入 bug 或破坏功能时，快速回退到修改前的可用状态
- **迭代功能开发**：对功能做多次变体实验，随时恢复到某个稳定的中间版本

---


## 重要限制


检查点是**临时安全网**，不是万能的，要注意它的边界：



**不跟踪 Bash 命令的更改****像 `rm` `mv` `cp` 这类通过 Bash 工具执行的文件操作，不会被检查点记录，无法回退。



不跟踪外部更改****只有当前会话内 Claude 编辑过的文件才会被跟踪。你在 VS Code、终端等外部工具里手动改的文件，或者其他会话的修改，都不会被捕获。



不能替代版本控制工具****检查点仅用于会话级的临时回退**，不适合长期项目管理和团队协作。


- 长期历史记录、分支管理 → 用 Git 等版本控制工具
- 检查点 = 本地临时撤销，Git = 永久项目历史









	  AI 思考中...





			** [Claude Code 斜杠 / 命令](https://www.runoob.com/claude-code-slash-commands.html)
			[Claude Code 插件参考手册](https://www.runoob.com/claude-code-plugin-ref.html) **













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