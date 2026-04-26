你可以把它们分为两大阵营：
* **旧时代（基于纯文本）：`cmd`**
* **新时代（基于对象）：`powershell` 与 `pwsh`**

下面我们分三个维度把它们扒得干干净净：

### 维度一：底层哲学的根本差异 —— “字符串” vs “对象”

这是它们之间最核心、最致命的区别。

* **`cmd`（纯文本流）**：
  就像早期的 Linux Shell 一样，`cmd` 里的所有命令输出的都是**纯文本（String）**。
  如果你用 `ipconfig` 获取 IP，再想把 IP 地址提取出来，你必须写极其痛苦的“正则表达式”或者用 `findstr` 去按行截取字符串。

* **`powershell` / `pwsh`（面向对象）**：
  它们是基于 `.NET` 框架构建的。你在里面运行的**每一个命令，返回的都不是字符串，而是实实在在的“对象”（Object）！**
  就像 Python 里的字典或对象一样，它们带有属性（Properties）和方法（Methods）。如果你想获取特定进程占用的内存，不需要截取字符串，直接像调属性一样取出来就行：`(Get-Process | Where-Object Name -eq "chrome").WorkingSet`。

### 维度二：命名规范 —— “远古咒语” vs “动名词组合”

* **`cmd` 命令**：
  继承自 DOS 时代，特点是**极其简短、毫无规律**。例如：`dir`（看目录）、`cd`（进目录）、`md`（建目录）、`type`（看文件内容）。

* **`powershell` / `pwsh` 命令（称为 Cmdlet）**：
  微软为了让语法一目了然，强制规定了 **`动词-名词 (Verb-Noun)`** 的命名规范。
  例如：`Get-ChildItem`（对应 dir）、`Set-Location`（对应 cd）、`New-Item`（对应 md）、`Get-Content`（对应 type）。

> **🤯 终极迷惑行为：“为什么我在 PowerShell 里敲 `dir` 和 `cd` 也管用？”**
> 微软知道让全世界重头背那一长串“动名词”太反人类了。所以他们在 PowerShell 里内置了**别名（Alias）机制**。
> 当你在 PowerShell 里敲 `dir` 时，其实是一个别名映射，系统在后台悄悄帮你把它转换成了 `Get-ChildItem`。

### 维度三：`powershell` (5.1) 和 `pwsh` (7+) 内部的语法代差

它们俩其实是同一个语言的两个版本，基础命令 95% 都是互通的，但 `pwsh` 引入了大量现代编程语言（像 C++/Rust）才有的高级语法特性：

**1. 管道链式操作符（Pipeline Chain Operators）**
在以前的老 `powershell` 里，如果你想“执行 A，成功了再执行 B”，语法很啰嗦。而新款的 `pwsh` 直接抄了 Bash 的作业：
* `&&`（左边成功才执行右边）：`Write-Output "成功" && Get-Date`
* `||`（左边失败才执行右边）：`Get-Error || Write-Output "没报错"`

**2. 三元运算符（Ternary Operator）**
你学 C++ 绝对熟悉的语法，老版没有，新版 `pwsh` 终于支持了：
* `$result = ($age -ge 18) ? "成年" : "未成年"`

**3. 空值合并（Null-Coalescing）**
处理变量为空时的默认值，`pwsh` 用起来就像现代前端或 C# 一样优雅：
* `$name = $userName ?? "佚名"` （如果 $userName 为空，就赋值为"佚名"）

**4. 跨平台命令的取舍**
* **老版 `powershell`** 有很多只能在 Windows 上用的“特权命令”（比如 `Get-WmiObject`）。
* **新版 `pwsh`** 因为要兼顾 Linux 和 Mac，废弃了一些深度绑定 Windows 底层的旧命令，改成了更通用的跨平台标准（比如推荐用 `Get-CimInstance`）。

---

### 📝 常用命令对比“罗塞塔石碑” (Rosetta Stone)

| 操作目标 | `cmd` 命令 | `powershell` / `pwsh` 原生命令 | 在 PS 里的快捷别名 (Alias) |
| :--- | :--- | :--- | :--- |
| **列出文件** | `dir` | `Get-ChildItem` | `dir`, `ls` (跨平台习惯) |
| **切换目录** | `cd` | `Set-Location` | `cd` |
| **清屏** | `cls` | `Clear-Host` | `cls`, `clear` |
| **创建空文件** | `type nul > a.txt` | `New-Item a.txt -Type File` | `ni a.txt` |
| **查看网络** | `ipconfig` | `Get-NetIPAddress` | (仍然可直接调用 `ipconfig`) |
| **查找字符串** | `findstr` | `Select-String` | `sls` |
| **解析 JSON** | ❌ (完全做不到) | `ConvertFrom-Json` | *(这是 PS 的杀手锏)* |

**💡 给你的终极开发建议：**
既然你懂编程，**以后请把 PowerShell 7 (`pwsh`) 当作一门完整的“脚本语言”来用**，而不是像 `cmd` 那样仅仅当作一个“敲字发指令的打字机”。它的变量控制、JSON 解析、API 请求（`Invoke-RestMethod`）能力非常恐怖，写自动化脚本比 Python 还要原生。