---
data: 2026-04-27
tags:
  - Windows
  - tips
  - index
cssclasses:
---

# windows little tips

这个页面只收 Windows 下最常翻、最容易忘但又马上要用的东西。

## reload terminal

- PowerShell 里临时重载配置：`. $PROFILE`
- 这只能重载 profile 内容；如果你刚改的是系统/用户环境变量，通常还是要新开终端
- 如果想缩短输入，可以在 `$PROFILE` 里自己加一个 `rl` 函数

```powershell
function rl {
    . $PROFILE
}
```

## 终端体系

- 终端总入口：[[terminal有关问题或者脚本有关问题]]
- `cmd`：老式文本流
- `powershell`：Windows PowerShell 5.1
- `pwsh`：PowerShell 7+，更现代，适合脚本化
- 详细区别：[[terminal有关问题或者脚本有关问题/cmd,powershell,pwsh命令区别]]

## VS Code / PowerShell

- 如果 VS Code 里每次都得手动 `.$PROFILE`，先查是不是开了 `-NoProfile`
- 排查入口：[[terminal有关问题或者脚本有关问题]]

## 自启动

- 任务管理器“启动”页是管理面板，不是启动源本体
- 常见启动源：
  - 注册表 `HKLM/HKCU\\...\\Run`
  - `shell:startup`
  - `shell:common startup`
  - `services.msc`
- 详细说明：[[tips/windows系统自启有关]]

## 快速打开系统工具

- `taskmgr`：任务管理器
- `regedit`：注册表
- `services.msc`：服务
- `gpedit.msc`：组策略
- `devmgmt.msc`：设备管理器
- `diskmgmt.msc`：磁盘管理
- `msinfo32`：系统信息

完整说明：[[tools/Windows 核心系统工与运行命令指南]]

## 文件与编辑

- AI 代码复制进富文本/编辑器出现多余空行时，可试 `Ctrl + Shift + V`
- 查看当前 PowerShell 进程绝对路径：
  ```powershell
  (Get-Process -Id $PID).Path
  ```
- `Ctrl + Shift + C`：复制文件路径
- `Ctrl + H`：显示/隐藏隐藏文件

## 文件与链接

- 目录连接 / 符号链接：[[terminal有关问题或者脚本有关问题/目录连接-cmd的mklink命令]]
- 文件名和批量删除问题，也可参考：[[tips/带有复杂文件名文件的批量删除]]

## 微信和日常效率

- 微信快捷表情：[[tips/微信输入表情实现qq一样的快捷方式]]
- 放进开机自启，常见做法是快捷方式丢进 `shell:startup`

## 一眼记住

- 现代脚本优先 `pwsh`
- 管系统底层先想到 `regedit`、`services.msc`、`Autoruns`
- 任务管理器禁用启动项，通常比应用自己的“开机自启”开关更上位
