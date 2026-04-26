### 在另一个帖子下很多佬友非常多的terminal美化方案，我都配置并尝试了一遍，帖子太长当下总结一下
**第一次发长贴，如果有什么错误还请佬友们指正和海涵!**

### 1. 修改字体，背景
 
1. **安装宿主软件：** 在微软商店（Microsoft Store）安装 **Windows Terminal**。 
2. **安装现代内核：** 在终端运行 `winget install Microsoft.PowerShell` 安装 **PowerShell 7.6 (pwsh)**。 
3. **安装灵魂字体：**  下载[ **JetBrainsMono Nerd Font** 压缩包](https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip)安装之后，ctrl+\`打开设置，`default`->`appearence`->`background image`选择图片，  
![Pasted image 20260408155512 |600](https://raw.githubusercontent.com/submergepsc/imgur/main/Pasted%20image%2020260408155512.png)
4. 然后在`appearance`->`text`->`font face`选择下载的字体
![Pasted image 20260408155750|600](https://raw.githubusercontent.com/submergepsc/imgur/main/Pasted%20image%2020260408155750.png)
---

### 2.修改主题  
oh-my-posh确实很卡，每次空回车都会卡0.2秒左右，所以最后换成了starship。
1.  **安装 Starship 引擎：** 
    - 运行 `winget install --id Starship.Starship`。 
2. **套用连体箭头主题（马卡龙色）：** 
    - 先运行 `mkdir -Force $HOME\.config` 创建配置文件夹。 
    - 再运行 `starship preset pastel-powerline -o "$HOME\.config\starship.toml"`。 
    - _注意：_ 这里必须用 `$HOME` 而不能用 `~`，否则 Windows 无法识别路径。 
效果图如下：
![d8ec25e67d6336040a86ac37a245330a|600](https://raw.githubusercontent.com/submergepsc/imgur/main/d8ec25e67d6336040a86ac37a245330a.png)
---
c
### 3. 使用代码自动填充和彩色图标插件 
1.  **安装并启用增强插件：** 
    - 在终端运行：`Install-Module -Name Terminal-Icons -Scope CurrentUser -Force`（彩色图标）。 
    - 在终端运行：`Install-Module -Name PSReadLine -Scope CurrentUser -Force`（智能补全）。 
2. **打开配置文件：** 运行 `notepad $PROFILE`（如果提示创建则选“是”）。 
3. **写入最终版代码：** 在记事本中贴入以下内容并保存：

```shell
function rl {
    Write-Host "🔄 正在重载配置..." -ForegroundColor Cyan
    . $PROFILE
} # 这段是我用来方便重启终端配置的，也可以使用**. $profile**来快速重启终端
 
# 初始化 Starship (参数必须写 powershell 而不是 pwsh)
Invoke-Expression (&starship init powershell)

# 加载文件图标
Import-Module -Name Terminal-Icons

# 开启灰色幽灵字自动补全
Set-PSReadLineOption -PredictionSource History
```

---

### 4. 分页功能
在微软powershell官方文档看到这行命令，
```shell
wt -p "Command Prompt"`; split-pane -p "windows PowerShell" `; split-pane -H wsl.exe
```
![Pasted image 20260408160303|600](https://raw.githubusercontent.com/submergepsc/imgur/main/Pasted%20image%2020260408160303.png)
![Pasted image 20260408160533|600](https://raw.githubusercontent.com/submergepsc/imgur/main/Pasted%20image%2020260408160533.png)
运行之后发现效果非常好，命令解释如下：
- **`wt`** 这是 Windows Terminal 的启动命令。 
- **`-p "Command Prompt"`** 打开 Windows Terminal 后的**主窗口**，使用名为 "Command Prompt"（即传统的 cmd 命令行）的配置启动。 
- **`;`** 这是分隔符。因为在这段代码通常是在 PowerShell 里运行的，在 PowerShell 中 `;` 默认是用来隔开两句代码的。加上前面的反引号 `` ` `` 进行转义，是告诉系统：“把这个分号原封不动地传给 `wt` 程序，作为它内部切分动作的连接符”。 
- **`split-pane -p "windows PowerShell"`** 在刚才的主窗口旁边，**切出一个分屏**（默认是垂直左右对半切），并在新切出来的这一半里，运行蓝色的 "Windows PowerShell"。  
- **`split-pane -H wsl.exe`** 在这个刚切出来的 PowerShell 窗口里，再进行一次**水平切分 (`-H` 代表 Horizontal)**，并在切出来的下半部分运行 `wsl.exe`（Windows Subsystem for Linux，即 Linux 子系统）。
### tips:
在桌面新建一个`tri_pane.bat`，把这段命令输入进去，如果在写入`$profile`是不是就可以每次默认打开三个窗口了QAQ（应该没人这么做）
```shell
wt -p "Command Prompt"; split-pane -p "windows PowerShell" ; split-pane -H wsl.exe
```