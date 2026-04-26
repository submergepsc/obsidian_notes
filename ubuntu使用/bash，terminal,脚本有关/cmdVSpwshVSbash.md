好，这一版我给你整理成 **CMD（批处理） vs Bash vs PowerShell 的完整对照笔记**，你可以直接丢进 Obsidian 用👇

---

# 🧠 Windows CMD vs Bash vs PowerShell 全面对照

---

# 🎯 核心差异（必须先搞清）

| 维度   | CMD      | Bash  | PowerShell   |
| ---- | -------- | ----- | ------------ |
| 本质   | 批处理解释器   | Shell | Shell + 脚本语言 |
| 数据类型 | 字符串      | 字符串   | **对象（核心差异）** |
| 能力   | 最弱       | 强     | 最强           |
| 推荐程度 | ❌ 不推荐长期用 | ✅     | ✅            |

👉 一句话：

* CMD：**古老脚本工具**
* Bash：**工具链 + 文本流**
* PowerShell：**现代自动化语言**

---

# 🧩 启动配置文件对照

| 功能   | CMD        | Bash        | PowerShell |
| ---- | ---------- | ----------- | ---------- |
| 启动配置 | ❌ 没有标准     | `~/.bashrc` | `$PROFILE` |
| 自动执行 | 注册表 / 快捷方式 | shell 自动加载  | 自动加载       |

👉 CMD 没有类似 `.bashrc` / `$PROFILE` 的好机制 ❗

---

# 🧩 alias / 快捷命令

## CMD ❌ 没有 alias

👉 替代方案：`doskey`

```cmd id="d9mpt1"
doskey ob=obsidian "C:\path\to\vault"
```

👉 但问题：

* ❌ 只在当前窗口有效
* ❌ 关闭终端就没了

---

## Bash

```bash id="q7a4zk"
alias ob='obsidian /path'
```

---

## PowerShell

```powershell id="1i1v9s"
Set-Alias ob obsidian
```

---

# 🧩 持久化“alias”

## CMD（曲线救国）

👉 方法 1：写进 bat

```bat id="5vjsai"
@echo off
doskey ob=obsidian "C:\path\to\vault"
cmd
```

👉 方法 2：注册表（不推荐）

---

## Bash / PowerShell（正统）

```bash id="l4d2aq"
~/.bashrc
```

```powershell id="x0n03p"
$PROFILE
```

---

# 🧩 函数（CMD 没有）

| 功能 | CMD  | Bash | PowerShell |
| -- | ---- | ---- | ---------- |
| 函数 | ❌ 没有 | ✅    | ✅          |

---

# 🧩 脚本文件对照

| 类型 | CMD             | Bash  | PowerShell |
| -- | --------------- | ----- | ---------- |
| 文件 | `.bat` / `.cmd` | `.sh` | `.ps1`     |

---

## 示例：打开 Obsidian

### CMD

```bat id="6gb2oy"
@echo off
start "" "obsidian://open?path=C:\path\to\vault"
```

或：

```bat id="r6k26b"
@echo off
"C:\Program Files\Obsidian\Obsidian.exe" "C:\path\to\vault"
```

---

### Bash

```bash id="1u0k2t"
obsidian "/path/to/vault"
```

---

### PowerShell

```powershell id="ffb6d7"
obsidian "C:\path\to\vault"
```

---

# 🧩 PATH / 命令查找

| 功能 | CMD             | Bash           | PowerShell     |
| -- | --------------- | -------------- | -------------- |
| 查看 | `echo %PATH%`   | `echo $PATH`   | `$env:PATH`    |
| 添加 | `set PATH=`（临时） | `export PATH=` | `$env:PATH +=` |

---

## CMD 永久添加 PATH

👉 系统变量（图形界面）

或：

```cmd id="x3yo0x"
setx PATH "%PATH%;C:\your\path"
```

---

# 🧩 环境变量

| 功能 | CMD             | Bash               | PowerShell         |
| -- | --------------- | ------------------ | ------------------ |
| 设置 | `set VAR=value` | `export VAR=value` | `$env:VAR="value"` |
| 使用 | `%VAR%`         | `$VAR`             | `$env:VAR`         |

---

# 🧩 引号规则

## CMD

| 类型    | 行为   |
| ----- | ---- |
| `" "` | 唯一引号 |
| `' '` | 普通字符 |

👉 CMD 没有单双引号区别 ❗

---

## Bash / PowerShell

| 类型    | 行为    |
| ----- | ----- |
| `' '` | 不解析变量 |
| `" "` | 解析变量  |

---

## 示例

### CMD

```cmd id="6rd1gc"
echo %USERPROFILE%
```

---

### Bash

```bash id="7d1e0p"
echo "$HOME"
```

---

### PowerShell

```powershell id="r1y3nq"
echo $env:USERPROFILE
```

---

# 🧩 执行脚本

| 操作 | CMD          | Bash          | PowerShell     |
| -- | ------------ | ------------- | -------------- |
| 执行 | `script.bat` | `./script.sh` | `.\script.ps1` |

---

# 🧩 管道（Pipe）

## CMD（很弱）

```cmd id="gcb9qf"
tasklist | find "obsidian"
```

👉 纯文本匹配

---

## Bash

```bash id="qg07o5"
ps aux | grep obsidian
```

---

## PowerShell（最强）

```powershell id="r9jv1n"
Get-Process | Where-Object {$_.Name -like "*obsidian*"}
```

👉 对象过滤 ✔

---

# 🧩 GUI 启动对照

| 功能   | CMD    | Linux      |
| ---- | ------ | ---------- |
| 双击启动 | `.bat` | `.desktop` |

---

### CMD

```bat id="w4xyk5"
start "" "C:\path"
```

---

### Linux

```ini id="y03qbf"
Exec=obsidian "/path"
```

---

# 🧠 对应关系总表（核心）

| Windows CMD | Bash        | PowerShell      |
| ----------- | ----------- | --------------- |
| `.bat`      | `.sh`       | `.ps1`          |
| `doskey`    | `alias`     | `Set-Alias`     |
| ❌ 无 profile | `~/.bashrc` | `$PROFILE`      |
| `%VAR%`     | `$VAR`      | `$env:VAR`      |
| `start`     | `xdg-open`  | `Start-Process` |

---

# 🧠 最佳实践（你这个场景）

## CMD 推荐做法

👉 用 `.bat`

```bat id="r1zw5y"
@echo off
start "" "obsidian://open?path=C:\obsidian_notes"
```

👉 或：

```bat id="iv1xhc"
@echo off
obsidian "C:\obsidian_notes"
```

---

## Linux 推荐

```bash id="p4xnyr"
alias ob='obsidian /media/loviya/新的D盘/obsidian_notes'
```

---

## PowerShell 推荐

```powershell id="nq6vqn"
function ob {
    obsidian "C:\obsidian_notes"
}
```

---

# 🚀 一句话总结

👉 CMD = “能用但很原始”
👉 Bash = “灵活强大”
👉 PowerShell = “最现代（对象级）”

---

# 🔥 最实用结论（给你记）

👉 CMD 没有：

* ❌ 真正的 alias
* ❌ profile
* ❌ 函数

👉 所以：

> 👉 **复杂操作不要用 CMD，直接用 PowerShell 或 Bash**

---

如果你下一步想再升级，我可以给你做一份：

👉 **“Linux / PowerShell / CMD 常用命令 50 条速查表（对照版）”**


# pwshVSbash脚本命令对照
好，这里我给你整理一份**精简但够用的 Linux（Bash） vs PowerShell 对照笔记**，结构适合直接放进 Obsidian 👇

---

# 🧠 Linux（Bash） vs PowerShell 对照笔记（精简版）

---

# 🎯 核心差异（最重要）

| 维度   | Bash（Linux） | PowerShell    |
| ---- | ----------- | ------------- |
| 核心模型 | 文本流         | **对象流（核心差异）** |
| 输出   | 字符串         | 对象（带属性）       |
| 管道   | 传字符串        | 传对象           |
| 设计风格 | 工具组合        | 类编程语言         |

👉 一句话总结：

* Bash：**处理文本**
* PowerShell：**处理对象**

---

# 🧩 启动配置（≈ profile）

| 功能   | Bash               | PowerShell         |
| ---- | ------------------ | ------------------ |
| 配置文件 | `~/.bashrc`        | `$PROFILE`         |
| 编辑   | `nano ~/.bashrc`   | `notepad $PROFILE` |
| 生效   | `source ~/.bashrc` | `. $PROFILE`       |

---

# 🧩 快捷命令（alias / function）

## alias（简单）

### Bash

```bash id="9a0r6h"
alias ob='obsidian /path/to/vault'
```

### PowerShell

```powershell id="4jds5l"
Set-Alias ob obsidian
```

⚠️ 两边 alias 都不适合复杂逻辑

---

## function（推荐）

### Bash

```bash id="b0ozq2"
ob() {
    obsidian "/path/to/vault"
}
```

### PowerShell

```powershell id="diyc2n"
function ob {
    obsidian "C:\path\to\vault"
}
```

👉 **完全对等 ✔**

---

# 🧩 脚本

| 类型 | Bash          | PowerShell     |
| -- | ------------- | -------------- |
| 文件 | `.sh` 或无后缀    | `.ps1`         |
| 执行 | `./script.sh` | `.\script.ps1` |

---

# 🧩 PATH（命令查找）

| 功能 | Bash              | PowerShell         |
| -- | ----------------- | ------------------ |
| 查看 | `echo $PATH`      | `$env:PATH`        |
| 添加 | `export PATH=...` | `$env:PATH += ...` |

---

# 🧩 环境变量

| 功能 | Bash               | PowerShell         |
| -- | ------------------ | ------------------ |
| 定义 | `export VAR=value` | `$env:VAR="value"` |
| 使用 | `$VAR`             | `$env:VAR`         |

---

# 🧩 引号规则（重点）

| 类型    | Bash  | PowerShell |
| ----- | ----- | ---------- |
| `' '` | 不解析变量 | 不解析变量      |
| `" "` | 解析变量  | 解析变量       |

---

## 示例

### Bash

```bash id="khsn3o"
name=loviya
echo "$name"
```

### PowerShell

```powershell id="rq8k4k"
$name="loviya"
echo "$name"
```

---

# 🧩 管道（Pipe）

## Bash（文本）

```bash id="q3tw1x"
ps aux | grep obsidian
```

---

## PowerShell（对象）

```powershell id="1q0o2g"
Get-Process | Where-Object {$_.Name -like "*obsidian*"}
```

👉 PowerShell 可以直接访问属性 ✔

---

# 🧩 命令执行

| 操作      | Bash       | PowerShell     |
| ------- | ---------- | -------------- |
| 当前目录执行  | `./script` | `.\script.ps1` |
| PATH 查找 | 自动         | 自动             |

---

# 🧩 GUI 启动

| 功能   | Linux      | PowerShell      |
| ---- | ---------- | --------------- |
| 打开程序 | `obsidian` | `obsidian`      |
| 打开文件 | `xdg-open` | `Start-Process` |

---

# 🧠 总体映射

| PowerShell      | Bash        |
| --------------- | ----------- |
| `$PROFILE`      | `~/.bashrc` |
| `function`      | `function`  |
| `Set-Alias`     | `alias`     |
| `$env:VAR`      | `$VAR`      |
| `Start-Process` | `xdg-open`  |
| `.ps1`          | `.sh`       |

---

# 🧠 最佳实践（你的场景）

👉 打开 Obsidian 仓库：

## Bash

```bash id="3g6d7m"
alias ob='obsidian /media/loviya/新的D盘/obsidian_notes'
```

或：

```bash id="7ifzqv"
ob() {
    obsidian "/media/loviya/新的D盘/obsidian_notes"
}
```

---

## PowerShell

```powershell id="0vx1hd"
function ob {
    obsidian "C:\obsidian_notes"
}
```

---

# 🚀 一句话总结

👉 Bash = 文本工具链
👉 PowerShell = 对象脚本语言

👉 但在“快捷命令 / 打开程序”这种场景：

> ✔ 两者基本一一对应

---

如果你要再进阶，我可以帮你做一份：

👉 **“Bash ↔ PowerShell 常用命令 50 条对照（实战版）”**
