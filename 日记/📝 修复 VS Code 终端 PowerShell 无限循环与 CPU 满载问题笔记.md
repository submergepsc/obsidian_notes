### 🔴 症状描述

- **现象：** 打开 VS Code 终端后，PowerShell 不断自动执行未知命令、无法输入，伴随电脑风扇狂转（CPU 占用极高）。
    
- **边界条件：** 外部系统自带的 PowerShell 正常，VS Code 内部的 CMD 终端正常，禁用所有插件（安全模式）启动 VS Code 依然死循环。这说明问题**仅限于 VS Code 挂载 PowerShell 时的底层机制**。
    ``

### 🔍 核心原因

1. **AI 插件配置污染（直接诱因）：** AI 编程助手（如通义灵码、Claude Code 等）出现异常，将大量的 C++ 源代码片段（如 `for`, `if`, `ofstream`）错误地写入了 VS Code 的 `chat.tools.terminal.autoApprove`（终端自动执行免确认白名单）配置中，导致终端一启动就被疯狂注入这些无效代码。
    
2. **Shell 整合与底层 Profile 死锁（根本原因）：** VS Code 默认会在后台运行 `shellIntegration.ps1` 脚本以实现命令高亮和状态追踪，该机制或系统深层的 PowerShell `$PROFILE` 配置文件与当前环境发生严重冲突，导致终端陷入无限重试的死锁。
    

---

### 🛠️ 详细解决步骤与代码更改

#### 第一步：清理被污染的 `settings.json`

- **操作：**
    
    1. 在 VS Code 中按 `Ctrl + Shift + P`。
        
    2. 输入并选择 **首选项: 打开用户设置(JSON)** (`Preferences: Open User Settings (JSON)`)。
        
- **修改：** 找到 `"chat.tools.terminal.autoApprove": { ... }` 这一段。**删除**里面所有像 C++ 源代码的键值对（例如 `"ofstream": true`, `"Person::count": true`, `"//": true` 等），仅保留正常的终端命令（如 `python`, `npm`, `git`, `ls` 等设为 `true`）。
    

#### 第二步：添加“终极隔离配置”（核心修复代码）

在同一个 `settings.json` 文件中（大括号 `{}` 内部的任意空行处），添加以下两段配置。这段代码的作用是**强制禁用 VS Code 的附加 Shell 脚本**，并让 PowerShell 以**完全纯净（无配置文件）**的模式启动。

JSON

```json
    // 1. 禁用 VS Code 的 Shell 整合功能，防止其后台脚本触发死循环
    "terminal.integrated.shellIntegration.enabled": false,

    // 2. 强制 PowerShell 以“-NoProfile”模式启动，斩断所有隐形环境配置的干扰
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "icon": "terminal-powershell",
            "args": ["-NoProfile"]
        }
    },
    
    ## 实际上就是这段代码起了作用
    // 3. 确保 PowerShell 依然是默认终端
    "terminal.integrated.defaultProfile.windows": "PowerShell",
```

_(注意：确保粘贴后 JSON 格式正确，上一行末尾要有逗号 `,`)_

#### 第三步：物理清场（结束幽灵进程与缓存）

1. **杀掉死循环进程：** 彻底关闭 VS Code，按下 `Ctrl + Shift + Esc` 打开**任务管理器**，找到所有残留的 `pwsh.exe` 或 `Windows PowerShell` 进程，右键点击**结束任务**。直到风扇声音降下来。
    
2. **清除终端死亡记忆：** 重新打开 VS Code，按下 `Ctrl + Shift + P`，输入并运行 **终端: 终止所有终端** (`Terminal: Kill All Terminals`)。