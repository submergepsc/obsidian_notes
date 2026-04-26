---
data: 2026-04-08
---
#### reload terminal:
1. `. $profile`,但是对于修改了环境变量和不可行
2. 在`notepad $profile`,在`$profile`中添加 下面代码后直接使用`rl`重新加载。
```shell
1. 
# =========================================
# 自定义快捷命令: 一键重载终端配置
# ==========================================
function rl {
    Write-Host "🔄 正在重新加载终端配置..." -ForegroundColor Cyan
    . $PROFILE
    Write-Host "✅ 重载完成！" -ForegroundColor Green
}
```

## ai代码复制空行问题
`ctrl+shift+v`可以解析ai生成的html，防止多余的空行
查看终端绝对地址：`(Get-Process -Id $PID).Path` %%2026-04-11%%

# 快捷键
`ctrl+shift+C`直接复制文件地址。

文件夹ctrl+h显示隐藏文件