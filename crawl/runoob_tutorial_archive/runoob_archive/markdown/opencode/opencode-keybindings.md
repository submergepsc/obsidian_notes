# OpenCode 快捷键配置详解

- Source: https://www.runoob.com/opencode/opencode-keybindings.html

OpenCode 提供了一套完整的键盘快捷键系统，涵盖应用控制、会话管理、消息浏览、模型切换和输入编辑等各类操作。

所有快捷键均可通过 `tui.json` 文件进行自定义。


---


## 配置文件


快捷键配置写在 `tui.json` 文件的 `keybinds` 字段下，每条记录的键名为操作名称，值为对应的快捷键：


## 实例


```
{
  "$schema": "https://opencode.ai/tui.json",
  "keybinds": {
    "leader": "ctrl+x",          // 前导键设置（见下方说明）
    "session_new": "<leader>n",  // 新建会话：先按前导键，再按 n
    "model_list": "<leader>m",   // 打开模型列表：先按前导键，再按 m
    "session_compact": "none"    // 将值设为 "none" 可禁用该快捷键
  }
}
```


一个操作可以绑定多个快捷键，用英文逗号分隔，任意一个触发即可执行该操作：


## 实例


```
{
  "$schema": "https://opencode.ai/tui.json",
  "keybinds": {
    // 以下写法表示：按 pageup 或按 ctrl+alt+b，都可以向上翻页
    "messages_page_up": "pageup,ctrl+alt+b"
  }
}
```


---


## 前导键（Leader Key）


OpenCode 的大多数快捷键采用**前导键（Leader Key）**机制：先按下前导键，再按功能键，两键组合触发对应操作。这样设计的好处是避免与终端本身的快捷键产生冲突。


默认前导键为 `ctrl+x`。例如，新建会话的快捷键是 `n`，实际操作为：先按 `ctrl+x`，再按 `n`。


你可以将前导键改为任意组合键：


## 实例


```
{
  "$schema": "https://opencode.ai/tui.json",
  "keybinds": {
    "leader": "ctrl+x"    // 修改前导键为其他按键，如 "ctrl+space"、"alt+x" 等
                          // 配置中的 <leader> 占位符会自动替换为这里设置的按键
  }
}
```


**
不一定必须使用前导键机制来设置快捷键——也可以直接绑定普通按键或组合键。但建议优先使用前导键，以避免与终端快捷键冲突。


---


## 禁用快捷键


将任意快捷键的值设为 `"none"` 即可禁用该操作，禁用后按任何键都不会触发它：


## 实例


```
{
  "$schema": "https://opencode.ai/tui.json",
  "keybinds": {
    "session_compact": "none",    // 禁用"压缩会话"快捷键
    "scrollbar_toggle": "none",   // 禁用"切换滚动条"快捷键
    "tips_toggle": "none"         // 禁用"切换提示"快捷键
  }
}
```


---


## 完整快捷键列表


### 1、应用与界面


| 操作名称 | 默认快捷键 | 说明 |
| --- | --- | --- |
| app_exit | ctrl+c, ctrl+d, q | 退出 OpenCode |
| editor_open | e | 用外部编辑器打开当前输入内容 |
| theme_list | t | 打开主题列表，切换界面主题 |
| sidebar_toggle | b | 显示或隐藏侧边栏 |
| scrollbar_toggle | 无（默认禁用） | 显示或隐藏滚动条 |
| username_toggle | 无（默认禁用） | 显示或隐藏用户名 |
| status_view | s | 查看当前状态信息 |
| tool_details | 无（默认禁用） | 查看工具调用详情 |
| command_list | ctrl+p | 打开命令面板，搜索所有可用命令 |
| tips_toggle | h | 显示或隐藏使用提示 |
| display_thinking | 无（默认禁用） | 显示或隐藏模型的思考过程 |
| terminal_suspend | ctrl+z | 挂起终端（将 OpenCode 放到后台，回到 shell；输入 fg 可恢复） |
| terminal_title_toggle | 无（默认禁用） | 显示或隐藏终端标题栏 |


### 2、会话管理


| 操作名称 | 默认快捷键 | 说明 |
| --- | --- | --- |
| session_new | n | 新建一个会话 |
| session_list | l | 查看所有历史会话列表 |
| session_export | x | 导出当前会话内容 |
| session_timeline | g | 查看当前会话的时间线 |
| session_fork | 无（默认禁用） | 从当前位置创建一个分支会话 |
| session_rename | 无（默认禁用） | 重命名当前会话 |
| session_share | 无（默认禁用） | 分享当前会话 |
| session_unshare | 无（默认禁用） | 取消分享当前会话 |
| session_interrupt | escape | 中断当前正在运行的响应 |
| session_compact | c | 压缩当前会话上下文，减少 Token 占用 |
| session_child_first | ↓ | 跳转到第一个子会话 |
| session_child_cycle | → | 在子会话间向前循环切换 |
| session_child_cycle_reverse | ← | 在子会话间向后循环切换 |
| session_parent | ↑ | 返回父会话 |


### 3、消息浏览


| 操作名称 | 默认快捷键 | 说明 |
| --- | --- | --- |
| messages_page_up | pageup, ctrl+alt+b | 向上翻一页消息 |
| messages_page_down | pagedown, ctrl+alt+f | 向下翻一页消息 |
| messages_line_up | ctrl+alt+y | 向上滚动一行 |
| messages_line_down | ctrl+alt+e | 向下滚动一行 |
| messages_half_page_up | ctrl+alt+u | 向上滚动半页 |
| messages_half_page_down | ctrl+alt+d | 向下滚动半页 |
| messages_first | ctrl+g, home | 跳转到最早的第一条消息 |
| messages_last | ctrl+alt+g, end | 跳转到最新的最后一条消息 |
| messages_next | 无（默认禁用） | 跳转到下一条消息 |
| messages_previous | 无（默认禁用） | 跳转到上一条消息 |
| messages_last_user | 无（默认禁用） | 跳转到最后一条用户消息 |
| messages_copy | y | 复制当前消息内容到剪贴板 |
| messages_undo | u | 撤销上一步操作 |
| messages_redo | r | 重做撤销的操作 |
| messages_toggle_conceal | h | 折叠或展开消息中的隐藏内容 |


### 4、模型与代理


| 操作名称 | 默认快捷键 | 说明 |
| --- | --- | --- |
| model_list | m | 打开模型列表，选择切换当前使用的模型 |
| model_cycle_recent | f2 | 在最近使用过的模型中向前循环切换 |
| model_cycle_recent_reverse | shift+f2 | 在最近使用过的模型中向后循环切换 |
| model_cycle_favorite | 无（默认禁用） | 在收藏的模型中向前循环切换 |
| model_cycle_favorite_reverse | 无（默认禁用） | 在收藏的模型中向后循环切换 |
| variant_cycle | ctrl+t | 在当前模型的变体（如 thinking 模式）之间循环切换 |
| agent_list | a | 打开代理列表，选择切换当前使用的代理 |
| agent_cycle | tab | 向前循环切换代理 |
| agent_cycle_reverse | shift+tab | 向后循环切换代理 |


### 5、输入框编辑


| 操作名称 | 默认快捷键 | 说明 |
| --- | --- | --- |
| input_submit | return | 发送当前输入内容 |
| input_newline | shift+return, ctrl+return, alt+return, ctrl+j | 在输入框中插入换行（不发送） |
| input_clear | ctrl+c | 清空输入框内容 |
| input_paste | ctrl+v | 粘贴剪贴板内容到输入框 |
| input_move_left | left, ctrl+b | 光标向左移动一个字符 |
| input_move_right | right, ctrl+f | 光标向右移动一个字符 |
| input_move_up | up | 光标向上移动一行 |
| input_move_down | down | 光标向下移动一行 |
| input_word_forward | alt+f, alt+right, ctrl+right | 光标向前跳过一个单词 |
| input_word_backward | alt+b, alt+left, ctrl+left | 光标向后跳过一个单词 |
| input_line_home | ctrl+a | 移动到当前行的开头 |
| input_line_end | ctrl+e | 移动到当前行的末尾 |
| input_visual_line_home | alt+a | 移动到当前视觉行（换行显示的行）的开头 |
| input_visual_line_end | alt+e | 移动到当前视觉行的末尾 |
| input_buffer_home | home | 跳转到整个输入框内容的最开头 |
| input_buffer_end | end | 跳转到整个输入框内容的最末尾 |
| input_delete_to_line_end | ctrl+k | 删除从光标到当前行末尾的所有内容 |
| input_delete_to_line_start | ctrl+u | 删除从当前行开头到光标的所有内容 |
| input_delete_line | ctrl+shift+d | 删除光标所在的整行 |
| input_backspace | backspace, shift+backspace | 删除光标前一个字符 |
| input_delete | ctrl+d, delete, shift+delete | 删除光标后一个字符 |
| input_delete_word_forward | alt+d, alt+delete, ctrl+delete | 删除光标后一个单词 |
| input_delete_word_backward | ctrl+w, ctrl+backspace, alt+backspace | 删除光标前一个单词 |
| input_undo | ctrl+-, super+z | 撤销输入框中的上一步编辑 |
| input_redo | ctrl+., super+shift+z | 重做撤销的编辑 |


### 6、文本选择


| 操作名称 | 默认快捷键 | 说明 |
| --- | --- | --- |
| input_select_left | shift+left | 向左选中一个字符 |
| input_select_right | shift+right | 向右选中一个字符 |
| input_select_up | shift+up | 向上选中一行 |
| input_select_down | shift+down | 向下选中一行 |
| input_select_word_forward | alt+shift+f, alt+shift+right | 向前选中一个单词 |
| input_select_word_backward | alt+shift+b, alt+shift+left | 向后选中一个单词 |
| input_select_line_home | ctrl+shift+a | 从光标位置选中到当前行开头 |
| input_select_line_end | ctrl+shift+e | 从光标位置选中到当前行末尾 |
| input_select_visual_line_home | alt+shift+a | 从光标位置选中到当前视觉行开头 |
| input_select_visual_line_end | alt+shift+e | 从光标位置选中到当前视觉行末尾 |
| input_select_buffer_home | shift+home | 从光标位置选中到输入框最开头 |
| input_select_buffer_end | shift+end | 从光标位置选中到输入框最末尾 |


### 7、输入历史


| 操作名称 | 默认快捷键 | 说明 |
| --- | --- | --- |
| history_previous | up | 调出上一条历史输入（输入框为空时有效） |
| history_next | down | 调出下一条历史输入 |


---


## 桌面版内置输入快捷键


OpenCode 桌面版的提示词输入框额外内置了一套 Readline / Emacs 风格**的文本编辑快捷键，**这些快捷键为内置功能，无法通过 `tui.json` 修改或禁用**：


| 快捷键 | 操作 |
| --- | --- |
| ctrl+a | 移动到当前行的开头 |
| ctrl+e | 移动到当前行的末尾 |
| ctrl+b | 光标向后移动一个字符 |
| ctrl+f | 光标向前移动一个字符 |
| alt+b | 光标向后移动一个单词 |
| alt+f | 光标向前移动一个单词 |
| ctrl+d | 删除光标所在位置的字符 |
| ctrl+k | 删除从光标到行尾的内容 |
| ctrl+u | 删除从光标到行首的内容 |
| ctrl+w | 删除前一个单词 |
| alt+d | 删除后一个单词 |
| ctrl+t | 交换光标前后两个字符的位置 |
| ctrl+g | 取消当前弹出窗口，或中止正在运行的响应 |


---


## 配置 Shift+Enter 换行


部分终端默认不会将带修饰键的 Enter（如 `Shift+Enter`）作为独立按键发送，导致在 OpenCode 中按 `Shift+Enter` 无法换行而是直接发送消息。需要在终端中手动配置该按键的转义序列。


### Windows Terminal 配置方法


**第一步：**打开 Windows Terminal 的 `settings.json` 文件，路径为：


```
%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
```


**第二步：**在文件的根级 `actions` 数组中添加以下配置，定义一个发送 `Shift+Enter` 转义序列的动作：


## 实例


```
"actions": [
  {
    "command": {
      "action": "sendInput",
      "input": "\u001b[13;2u"    // Shift+Enter 对应的标准转义序列（CSI u 格式）
    },
    "id": "User.sendInput.ShiftEnterCustom"
  }
]
```


**第三步：**在文件的根级 `keybindings` 数组中添加按键绑定，将 `Shift+Enter` 映射到上面定义的动作：


## 实例


```
"keybindings": [
  {
    "keys": "shift+enter",
    "id": "User.sendInput.ShiftEnterCustom"
  }
]
```


**第四步：**保存 `settings.json` 文件后，重启 Windows Terminal 或打开一个新标签页使配置生效。


**
如果你使用的是其他终端（如 iTerm2、Kitty、Alacritty 等），请参考对应终端的文档，找到"按键映射"或"Key bindings"相关设置，将 `Shift+Enter` 配置为发送 `\u001b[13;2u` 转义序列即可。








	  AI 思考中...





			** [OpenCode 主题](https://www.runoob.com/opencode-theme.html)
			[OpenCode 自定义命令](https://www.runoob.com/opencode-commands.html) **













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