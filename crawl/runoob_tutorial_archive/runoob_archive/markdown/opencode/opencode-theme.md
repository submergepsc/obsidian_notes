# OpenCode 主题

- Source: https://www.runoob.com/opencode/opencode-theme.html

OpenCode 支持多种主题系统，您可以选择内置主题、自动适配终端主题，或者完全自定义主题，从而获得一致且舒适的终端体验。


---


## 终端要求


为了确保主题能够正确显示完整色彩，您的终端必须支持 **真彩色（24 位色）**。


- **检查支持情况：**


```
echo $COLORTERM
```


输出应为：


```
truecolor
或
24bit
```


- **启用真彩色：**


```
export COLORTERM=truecolor
```


- **常见支持终端：**


- iTerm2
- Alacritty
- Kitty
- Windows Terminal
- GNOME Terminal（新版本）


如果终端不支持真彩色，主题将回退为 256 色，可能导致颜色失真。


---


## 内置主题


OpenCode 内置多种主题，可直接使用：


| 主题名称 | 说明 |
| --- | --- |
| system | 自动适配终端主题 |
| tokyonight | Tokyonight 风格 |
| everforest | Everforest 风格 |
| ayu | Ayu 暗色主题 |
| catppuccin | Catppuccin 主题 |
| catppuccin-macchiato | Catppuccin 变体 |
| gruvbox | Gruvbox 风格 |
| kanagawa | Kanagawa 风格 |
| nord | Nord 风格 |
| matrix | 黑客风格（黑底绿字） |
| one-dark | Atom One Dark |


---


## system 主题（推荐）


**system** 主题会自动适配您的终端配色：


- 根据终端背景生成灰度层级
- 使用 ANSI 标准颜色
- 保持终端默认文本与背景


适用于：


- 使用自定义终端主题的用户
- 希望所有终端工具风格统一的用户


---


## 使用主题


方式一：在 TUI 中选择主题


```
/theme
```


方式二：通过配置文件设置


**tui.json**


```
{
  "$schema": "https://opencode.ai/tui.json",
  "theme": "tokyonight"
}
```


---


## 自定义主题


OpenCode 支持通过 JSON 定义完全自定义主题。


### 主题加载优先级


- 内置主题
- 用户目录：~/.config/opencode/themes/
- 项目目录：.opencode/themes/
- 当前目录：./.opencode/themes/


后加载的主题会覆盖前面的。


---


## 创建主题


用户级主题：


```
mkdir -p ~/.config/opencode/themes
vim ~/.config/opencode/themes/my-theme.json
```


项目级主题：


```
mkdir -p .opencode/themes
vim .opencode/themes/my-theme.json
```


---


## 主题格式说明


支持以下格式：


- 十六进制颜色：#ffffff
- ANSI 颜色：0-255
- 颜色引用：primary
- 深浅模式：


```
{
  "dark": "#000000",
  "light": "#ffffff"
}
```


- 继承终端默认：


```
"text": "none"
```


---


## 完整示例


**my-theme.json**


```
{
  "$schema": "https://opencode.ai/theme.json",
  "defs": {
    "bg": "#1e1e2e",
    "fg": "#cdd6f4",
    "primary": "#89b4fa",
    "accent": "#f38ba8",
    "success": "#a6e3a1",
    "warning": "#f9e2af"
  },
  "theme": {
    "primary": {
      "dark": "primary",
      "light": "#005f87"
    },
    "accent": {
      "dark": "accent",
      "light": "#d7005f"
    },
    "background": {
      "dark": "bg",
      "light": "#ffffff"
    },
    "text": {
      "dark": "fg",
      "light": "#000000"
    },
    "border": {
      "dark": "#313244",
      "light": "#cccccc"
    },
    "syntaxKeyword": {
      "dark": "primary",
      "light": "#0000ff"
    },
    "syntaxString": {
      "dark": "success",
      "light": "#008000"
    },
    "syntaxComment": {
      "dark": "#6c7086",
      "light": "#999999"
    }
  }
}
```


---


## 总结


OpenCode 主题系统具备以下特点：


- 支持内置主题，开箱即用
- 支持 system 自动适配终端
- 支持 JSON 自定义主题
- 支持多层级覆盖机制


如果你追求极致体验，建议：


- 终端开启 truecolor
- 优先使用 system 主题或自定义主题








	  AI 思考中...





			** [OpenCode 代理（Agent）](https://www.runoob.com/opencode-agent.html)
			[OpenCode 快捷键](https://www.runoob.com/opencode-keybindings.html) **













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