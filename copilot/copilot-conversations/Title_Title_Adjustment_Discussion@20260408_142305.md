---
epoch: 1775629385089
modelKey: "gpt-4o|github-copilot"
topic: "Title Title Adjustment Discussion"



tags:
  - copilot-conversation
---

**user**: 改一下所有的标题，按照1,23
[Context: Notes: tools/terminal_美化.md]
[Timestamp: 2026/04/08 14:23:05]

**ai**: 以下是修改后的标题，按照1, 2, 3的顺序进行了调整：

---

### 1. 装软件 & 装字体

1. **下载终端：** 去系统自带的“微软商店”搜索下载 `Windows Terminal`。
    
2. **下载内核：** 打开终端，复制运行：`winget install Microsoft.PowerShell`。
    
3. **安装字体：** * 点此下载：[JetBrainsMono Nerd Font 压缩包](https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip)
    
    - 解压，全选里面的 `.ttf` 文件，**右键 -> 安装**。
        

### 2. 改 UI 设置 (必须重启终端并选黑色的 PowerShell 7)

1. 按 `Ctrl + ,` 打开设置。
    
2. **默认配置文件：** 改为黑底白字的 `PowerShell`。
    
3. **外观设置：** * 字体选：**`JetBrainsMono NFP`** (极其重要！没有 NFP 后缀会乱码)。
    
    - 背景图：上传二次元雨夜图，调低不透明度。保存。
        

### 3. 装引擎 & 插件

在终端**依次复制运行**以下 3 行代码（如遇提示全选 Y）：

PowerShell

```
winget install --id Starship.Starship
Install-Module -Name Terminal-Icons -Scope CurrentUser -Force
Install-Module -Name PSReadLine -Scope CurrentUser -Force
```

### 4. 写死配置文件 ($PROFILE)

1. 运行：`notepad $PROFILE` (弹窗点“是”)。
    
2. **清空里面所有内容，把下面这段完整复制进去，然后保存关闭：**
    

PowerShell

```shell
# 1. 自动化函数区

function rl { Write-Host "🔄 重载..." -ForegroundColor Cyan; . $PROFILE }

# 2. 插件与引擎启动区
Invoke-Expression (&starship init powershell)
Import-Module -Name Terminal-Icons
Set-PSReadLineOption -PredictionSource History
```

### 5. 套用“马卡龙连体箭头”主题

终端里依次运行下面 2 行代码：

PowerShell

```
mkdir -Force $HOME\.config
starship preset pastel-powerline -o "$HOME\.config\starship.toml"
```

### 6. 彻底重启

关掉终端，重新打开。

**全套雨夜马卡龙色命令行 + 自动化快捷键，瞬间点亮！** 搞定收工！
[Timestamp: 2026/04/08 14:23:14]

**user**: obsidian怎么键入反引号
[Context: Notes: tools/terminal_美化.md]
[Timestamp: 2026/04/08 15:49:39]

**ai**: 在 Obsidian 或其他文本编辑器中输入反引号（`），可以通过以下方式：

1. **键盘输入：**
   - 在大多数键盘布局中，反引号键位于键盘左上角的 **Esc** 键下方，与波浪号（`~`）共享一个键。
   - 直接按下该键即可输入反引号（`）。
   - 如果键盘需要按住 **Shift** 键才能输入波浪号（`~`），那么只需不按 **Shift** 键即可输入反引号。

2. **复制粘贴：**
   - 如果无法找到反引号键，可以直接复制以下字符：`` ` ``。

3. **输入法：**
   - 在某些输入法中，可以通过输入特定的符号代码来生成反引号。例如，在中文输入法中，输入“反引号”可能会直接出现。

如果你的键盘布局不同（如非英文键盘），可以查找对应的键位，或者通过系统设置切换到英文键盘布局来输入反引号。
[Timestamp: 2026/04/08 15:49:46]

**user**: 反引号会自动高亮代码，
[Context: Notes: tools/terminal_美化.md]
[Timestamp: 2026/04/08 15:49:58]

**ai**: 是的，在 Obsidian 中，反引号（`` ` ``）是用来标记代码块或行内代码的 Markdown 语法的一部分。以下是具体用法：

### 1. **行内代码**
使用单个反引号包裹代码，适用于短代码片段：
```
`代码内容`
```
例如：
```
`print("Hello, World!")`
```
渲染后会显示为：`print("Hello, World!")`

---

### 2. **代码块**
使用三个反引号（```）包裹代码，适用于多行代码。可以在开头的三个反引号后面指定代码语言（如 `python`、`javascript` 等），以启用语法高亮。

语法：
```
```语言
代码内容
```
```

例如：
```
```python
def hello():
    print("Hello, World!")
```
```
渲染后会显示为高亮的代码块：

```python
def hello():
    print("Hello, World!")
```

---

### 3. **取消高亮**
如果你不希望反引号触发代码高亮，可以在反引号外加上转义符号（反斜杠 `\`）：
```
\`代码内容\`
```
这样，反引号会被当作普通字符显示，而不会触发代码高亮。

---

通过这些方法，你可以灵活地在 Obsidian 中使用反引号来展示代码或避免高亮。
[Timestamp: 2026/04/08 15:50:04]