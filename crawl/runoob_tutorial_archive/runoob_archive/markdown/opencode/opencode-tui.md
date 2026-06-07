# OpenCode 终端界面

- Source: https://www.runoob.com/opencode/opencode-tui.html

OpenCode 提供了一个交互式终端界面（TUI，Terminal User Interface），用于在命令行中与 AI 进行高效协作开发。


**TUI 是 OpenCode 的核心使用方式**，所有代码分析、修改、执行都通过这个界面完成。


**OpenCode TUI 本质是一个可执行命令的 AI 对话终端，它把开发、命令行和 AI 融合在一起。**


---


## 一、启动 TUI


### 1、在当前目录启动


```
opencode
```


**

如果出现 EACCES: permission denied, open ''** 是权限问题，我们可以修复目录权限：


```
sudo chown -R $(whoami) ~/.local
```


然后执行：


```
chmod -R 755 ~/.local
```


也可以暴力一点，直接用 **sudo**：


```
sudo opencode
```


会自动加载当前项目作为工作目录：


![](https://www.runoob.com/wp-content/uploads/2026/04/f0d7fd3e-9f67-4c55-ab21-bd08ebc9a09e.png)


---


### 2、指定项目目录启动


```
opencode /path/to/project
```


适用于快速切换项目


---


## 二、基本交互


进入 TUI 后，你可以直接输入自然语言：


```
帮我快速总结这个项目的结构
```


OpenCode 会结合项目代码给出分析结果:


![](https://www.runoob.com/wp-content/uploads/2026/04/5f622be8-8579-45a1-8f4e-47ed0a17e8da.png)


---


## 三、文件引用（核心功能）


你可以使用 ****@**** 来引用项目中的文件：


```
这个项目的认证逻辑是如何实现的？查看 @packages/functions/src/api/index.ts
```


**特点：**


- 支持模糊搜索文件路径
- 自动读取文件内容
- 无需复制代码


非常适合阅读陌生代码


---


## 四、执行 Bash 命令


按下 ****!**** 会切换到 shell 模式，该模式下的内容会作为 shell 命令执行：


```
!
```


执行命令：


```
ls -la
```


![](https://www.runoob.com/wp-content/uploads/2026/04/5f622be8-8579-45a1-8f4e-47ed0a17e8da-1.png)


执行结果会自动加入对话上下文。


这样我们可以边问 AI，边执行系统命令。


---


## 五、斜杠命令（/ 命令）


输入 ****/**** 可以执行内置命令，例如：


```
/help
```


打开帮助面板。


### 常用命令一览


| 命令 | 说明 |
| --- | --- |
| /connect | 配置模型 API |
| /models | 查看可用模型 |
| /init | 初始化项目配置（生成 AGENTS.md） |
| /new | 新建会话 |
| /sessions | 切换会话 |
| /undo | 撤销修改（含代码） |
| /redo | 重做修改 |
| /share | 分享当前对话 |
| /export | 导出对话为 Markdown |
| /exit | 退出 OpenCode |


---


## 六、快捷键（效率提升）


OpenCode 支持快捷键操作：


| 功能 | 快捷键 |
| --- | --- |
| 命令面板 | Ctrl + X → H |
| 新建会话 | Ctrl + X → N |
| 撤销 | Ctrl + X → U |
| 重做 | Ctrl + X → R |
| 模型列表 | Ctrl + X → M |


**说明：**


- Ctrl + X 是默认"前导键"
- 类似 Vim 的快捷键模式


---


## 七、编辑器集成（/editor）


你可以使用外部编辑器编写复杂提示：


```
/editor
```


需要提前配置：


```
export EDITOR="code --wait"
```


**支持编辑器：**


- VS Code（code）
- Cursor（cursor）
- Vim / Neovim
- Nano


---


## 八、会话管理


### 查看会话


```
/sessions
```


### 新建会话


```
/new
```


可以在多个任务之间切换


---


## 九、撤销与重做（重要）


### 撤销


```
/undo
```


作用：


- 撤销消息
- 回滚代码修改


### 重做


```
/redo
```


**注意：**


- 依赖 Git 管理代码变更
- 建议项目开启 Git


---


## 十、TUI 配置


可以通过配置文件自定义行为：


```
opencode.json
```


示例：


```
{
  "tui": {
    "scroll_speed": 3,
    "scroll_acceleration": {
      "enabled": true
    }
  }
}
```


**说明：**


- scroll_speed：滚动速度
- scroll_acceleration：平滑滚动（推荐开启）


---


## 十一、使用建议


- 多使用 **@** 引用文件，提高准确率
- 复杂任务先用计划模式，使用 **Tab** 键切换模式。
- 小步迭代，不要一次做太复杂。
- 重要操作前确保 Git 已提交。










	  AI 思考中...





			** [VS Code 安装 OpenCode](https://www.runoob.com/opencode-vscode.html)
			[OpenCode CLI 使用](https://www.runoob.com/opencode-cli.html) **













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