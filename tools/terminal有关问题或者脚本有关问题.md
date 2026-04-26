# terminal有关
[[terminal有关问题或者脚本有关问题/terminal内核与ui界面&Windows 终端环境核心组件总结]]

[[terminal有关问题或者脚本有关问题/cmd,powershell,pwsh命令区别]]

#### vs终端每次需要`. $profile`加载才能使用lsn
检查 VS Code 是否开启了“裸奔模式”
VS Code 的设置里有一个开关，可以让终端启动时不加载任何配置（`-NoProfile`）。

1. 在 VS Code 中按 `Ctrl + ,` 打开设置。
2. 搜索 `terminal.integrated.profiles.windows`。
3. 点击 **“在 settings.json 中编辑”**。
4. 检查 `PowerShell` 这一项的配置。如果里面有 `"args": ["-NoProfile"]`，请**务必删除**它。
   * **正确的配置**应该像这样（或者干脆没有 `args` 这一行）：
     ```json
     "PowerShell": {
         "path": "powershell.exe",
         "icon": "terminal-powershell"
     }
     ```
 
[[terminal有关问题或者脚本有关问题/目录连接-cmd的mklink命令]]




# 脚本有关
####  terminal有关问题或者脚本有关问题/删除全文多余的空行脚本
```shell
# 安全版本：读取和写入都强制指定 UTF8 编码
Get-ChildItem *.md | ForEach-Object {
    (Get-Content $_.FullName -Encoding UTF8) | Where-Object { $_ -match '\S' } | Out-File $_.FullName -Encoding UTF8
}
```


