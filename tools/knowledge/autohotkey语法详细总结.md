[使用 Program |AutoHotkey v2 --- Using the Program | AutoHotkey v2](https://www.autohotkey.com/docs/v2/Program.htm)



太棒了。既然你已经具备了一定的使用经验，并且打算将这份内容作为技术笔记或教程发表，那我们就跳过基础的“如何安装”和“什么是快捷键”的赘述，直接切入 **AutoHotkey v2** 的核心编程范式。

v2 版本彻底抛弃了 v1 混乱的命令式语法，全面拥抱了表达式、函数和面向对象的设计。这份教程大纲以现代编程语言的视角为你梳理 AHK v2 的语法体系，非常适合有一定代码基础的读者。

---

# 🚀 AutoHotkey v2 核心语法速通：从入门到进阶

AutoHotkey v2 是一门专为 Windows 桌面自动化设计的轻量级脚本语言。与前代相比，v2 实现了语法的全面现代化：**一切皆对象，一切皆表达式，一切皆函数**。

## 1. 基础语法与变量声明

在 v2 中，不再有 `.` 和 `=` 的混淆，统一使用 `:=` 进行赋值，强制使用表达式语法。

### 1.1 变量与赋值
AHK 是动态类型语言，变量无需预先声明类型。

```autohotkey
; 统一使用 := 进行赋值
appTitle := "Visual Studio Code"
timeout := 5000
isReady := true

; 字符串拼接统一使用空格或句点
fullMessage := "正在启动 " appTitle "，请等待 " timeout " 毫秒。"
```

### 1.2 数据类型与数据结构
v2 原生支持现代化的数据结构：数组 (Array) 和 映射 (Map)。

```autohotkey
; 数组 (Array) - 索引从 1 开始
myArray := ["Python", "Rust", "C++"]
myArray.Push("JavaScript")
MsgBox(myArray[1]) ; 输出 Python

; 映射/字典 (Map) - 键值对
myMap := Map("Name", "Loviya", "Role", "Developer")
myMap["Tool"] := "Obsidian"
MsgBox(myMap["Role"]) ; 输出 Developer
```

## 2. 核心灵魂：热键与热字符串

这是 AHK 的看家本领，也是与系统底层的直接接口。

### 2.1 基础热键 (Hotkeys)
修饰键符号：`#` (Win), `!` (Alt), `^` (Ctrl), `+` (Shift)。
在 v2 中，多行热键**必须**被包裹在大括号 `{}` 中，形成一个独立的作用域。

```autohotkey
; 按下 Ctrl + Alt + T 启动或激活终端
^!t::
{
    if WinExist("ahk_exe WindowsTerminal.exe") {
        WinActivate()
    } else {
        Run("wt.exe")
    }
}
```

### 2.2 热字符串 (Hotstrings)
用于文本快速展开或自动纠错。可以带有选项，例如 `*`（无需按空格即触发）和 `O`（省略结尾字符）。

```autohotkey
; 输入 /em 自动展开为颜文字，且无需额外按空格
:*: /em::(❁´◡`❁)

; 输入 @my 展开为邮箱地址
::@my::my.email@example.com
```

## 3. 控制流体系

v2 的控制流语法与 C++ / JavaScript 高度一致。

### 3.1 条件判断 (If / Switch)
```autohotkey
status := 200

if (status = 200) {
    MsgBox("请求成功")
} else if (status = 404) {
    MsgBox("未找到")
} else {
    MsgBox("未知错误")
}

; Switch 语句用于优雅地处理多分支
Switch status {
    Case 200: MsgBox("OK")
    Case 500: MsgBox("Server Error")
    Default: MsgBox("Unknown")
}
```

### 3.2 循环结构 (Loop / For / While)
```ahk
; 基础循环 5 次，内置变量 A_Index 记录当前次数
Loop 5 {
    MsgBox("当前循环次数：" A_Index)
}

; For 循环遍历数组或 Map
for index, element in ["A", "B", "C"] {
    MsgBox("Index: " index ", Value: " element)
}

; While 循环
count := 0
while (count < 3) {
    count++
}
```

## 4. 函数与作用域

v2 强制规定了清晰的变量作用域（局部、全局）。

### 4.1 函数定义与调用
```autohotkey
; 标准函数定义
CalculateSum(a, b := 0) { ; b 为默认参数
    return a + b
}

result := CalculateSum(10, 20)

; 胖箭头函数 (Fat Arrow) - 极其适合单行简写
Square(x) => x * x
MsgBox(Square(5)) ; 输出 25
```

### 4.2 作用域管理
在函数内部修改外部变量时，必须使用 `global` 关键字显式声明。

```autohotkey
counter := 0

IncrementCounter() {
    global counter ; 声明引用全局变量
    counter++
}
```

## 5. 核心系统控制接口

这是 AHK 发挥自动化威力的关键内置模块。

### 5.1 窗口与进程管理
* `Run(Target)`: 运行程序、文档或网址。
* `WinExist(WinTitle)`: 检查窗口是否存在。
* `WinActivate(WinTitle)`: 激活特定窗口。
* `WinClose(WinTitle)`: 关闭窗口。

```autohotkey
; 复杂的窗口查找：寻找标题包含 "Notepad" 的窗口
if WinExist("ahk_class Notepad") {
    WinActivate()
    SendText("自动输入的文本")
}
```

### 5.2 输入模拟 (Send)
* `Send(Keys)`: 发送按键，会解析特殊符号（如 `^c` 模拟 Ctrl+C）。
* `SendText(Text)`: 原样发送文本，极其安全，不会解析控制字符。

---

这份大纲涵盖了 v2 的核心编程范式，结构紧凑，适合作为技术分享的基础骨架。为了让你的这篇教程更具实战价值、更吸引读者，你希望在文章末尾补充哪一类的实战案例？比如：**剪贴板深度处理**、**多应用之间的联动自动化**，还是**自定义图形界面（GUI）的编写**？