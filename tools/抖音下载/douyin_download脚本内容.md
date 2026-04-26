

# 完整内容

```shell
# 1. 检查并创建 PowerShell 配置文件 (如果不存在)
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force | Out-Null
    Write-Host "已为你创建 PowerShell 配置文件。" -ForegroundColor Yellow
}

# 2. 定义要注入的自定义函数代码 (前台阻塞 + 后台按键版)
$AliasCode = @"

# ==========================================
# 自定义快捷命令: DouK-Downloader 自动化启动 (防闪退完美版)
# ==========================================
function douk {
    `$exePath = "H:\apps\DouK-Downloader_V5.7_Windows_X64\main.exe"
    `$workDir = "H:\apps\DouK-Downloader_V5.7_Windows_X64"
    
    # 1. 动态生成一个 VBS 按键脚本到系统临时文件夹
    `$vbsPath = "`$env:TEMP\auto_keys.vbs"
    `$vbsCode = @'
Set WshShell = WScript.CreateObject("WScript.Shell")
WScript.Sleep 2000
WshShell.SendKeys "5{ENTER}"
WScript.Sleep 500
WshShell.SendKeys "2{ENTER}"
WScript.Sleep 500
WshShell.SendKeys "1{ENTER}"
'@
    Set-Content -Path `$vbsPath -Value `$vbsCode -Encoding Ascii
    
    Write-Host "🚀 正在全局唤醒 DouK-Downloader (前台阻塞模式)..." -ForegroundColor Green
    
    # 2. 调用 wscript 在系统后台静默执行按键脚本
    Start-Process -FilePath "wscript.exe" -ArgumentList `$vbsPath
    
    # 3. 强制切换到工作目录，并使用 & 符号在前台霸占运行
    # 这样可以确保 stdin (输入流) 永远连接着你的键盘，直到你手动退出程序
    Push-Location `$workDir
    & `$exePath
    
    # 4. 当你退出 main.exe 后，自动弹回原来的路径
    Pop-Location
}
"@

# 3. 将代码追加写入到配置文件中
Add-Content -Path $PROFILE -Value $AliasCode -Encoding UTF8
Write-Host "✅ 完美版配置已成功写入！" -ForegroundColor Green
Write-Host "👉 请重启当前 PowerShell 窗口，或者直接运行 '. `$PROFILE' 重新加载配置。" -ForegroundColor Cyan
Write-Host "🎉 之后在任何路径下输入 'douk' 即可实现无缝自动化下载！" -ForegroundColor Yellow 
```

 
> [!fjds]    **删掉旧文件**
Remove-Item -Path $PROFILE -Force -ErrorAction Ignore
`-ErrorAction Ignore` 是为了防止文件不存在时候**系统报错**



