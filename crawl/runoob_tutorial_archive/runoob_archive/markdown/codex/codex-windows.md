# Codex Windows 原生支持

- Source: https://www.runoob.com/codex/codex-windows.html

Codex 在 Windows 上提供原生支持，无需 WSL 即可运行。本节介绍 Windows 平台特有的功能和配置。


---


## Windows 支持概述


Codex 支持以下 Windows 环境：


| 环境 | 支持状态 |
| --- | --- |
| Windows 11（原生） | 官方支持 |
| Windows 10 | 官方支持 |
| Windows 11 + WSL2 | 完整支持 |


![](https://www.runoob.com/wp-content/uploads/2026/04/windows-sandbox.webp)


**Codex 可以在 Windows 上原生运行，保持 Windows 工作流程。


---


## 安装


### 使用 winget 安装


## winget 安装


```
# 使用 winget 安装
winget install OpenAI.Codex

# 或者安装预览版
winget install OpenAI.Codex --source winget --accept-source-agreements --accept-package-agreements
```


### 使用 Chocolatey


## Chocolatey 安装


```
# 使用 Chocolatey 安装
choco install codex -y
```


### 手动安装


从 GitHub 下载 Windows 版本：


```
https://github.com/openai/codex/releases
```


下载 .exe 安装程序并运行。


> 推荐使用 winget 或 Chocolatey 安装，以便自动更新。


---


## 原生沙箱


Codex 可以在 Windows PowerShell 中原生运行：


- 无需 WSL 或虚拟机
- 保持 Windows 工作流程
- 与 Windows 工具无缝集成


### 沙箱模式配置


## 配置沙箱


```
# Windows 沙箱配置
[windows]
# 沙箱模式：unelevated | elevated
sandbox = "unelevated"

# 在私有桌面运行沙盒子进程
sandbox_private_desktop = true
```


### 沙箱模式说明


| 模式 | 说明 |
| --- | --- |
| unelevated | 标准用户权限运行（推荐） |
| elevated | 管理员权限运行 |


> 推荐使用 unelevated 模式以保持安全性。


---


### PowerShell 集成


Codex 可以直接在 PowerShell 中使用：


## PowerShell 中使用


```
# 启动 Codex
codex

# 非交互模式
codex exec "审查代码"

# 使用 PowerShell 命令
codex ! Get-Process
```


### CMD 支持


Codex 也支持传统的 CMD 环境：


## CMD 中使用


```
# 在 CMD 中运行
codex exec "列出文件"
```


> Codex 自动检测终端类型并优化输出。


---


## Windows 特有配置


### 路径处理


Windows 路径与 Unix 不同，Codex 会自动处理：


- 反斜杠转换为正斜杠
- 盘符处理
- UNC 路径支持


### 环境变量


## Windows 环境变量


```
# 设置 Codex 特定的环境变量
set CODEX_HOME=C:\Users\YourName\.codex
set CODEX_SQLITE_HOME=C:\Users\YourName\.codex
```


### 代理配置


## 代理设置


```
# 设置代理
set HTTP_PROXY=http://proxy.example.com:8080
set HTTPS_PROXY=http://proxy.example.com:8080

# 然后运行 Codex
codex
```


> 如果你的网络需要代理，配置环境变量即可。


---


## 故障排除


### 常见问题


#### 无法启动？


- 检查是否安装了必要的 Visual C++ 运行库
- 尝试以管理员权限运行
- 检查杀毒软件是否阻止


#### PowerShell 命令不执行？


确保 PowerShell 可执行文件在 PATH 中。


#### 中文路径问题？


Codex 支持 Unicode，但某些旧版终端可能有问题。


> 大多数问题可以通过重新安装或更新解决。


### 日志位置


Windows 日志位置：


```
%USERPROFILE%\.codex\log\codex-tui.log
```


> 查看日志可以了解详细的错误信息。


---


## 与 WSL2 比较


| 特性 | 原生 Windows | WSL2 |
| --- | --- | --- |
| 性能 | 更快 | 稍慢 |
| 设置 | 简单 | 需要安装 WSL |
| 兼容性 | Windows 工具 | Linux 工具 |
| 维护 | 自动更新 | 独立更新 |


> 对于大多数 Windows 用户，推荐使用原生版本。


---


## 最佳实践


- 使用 winget 或 Chocolatey 安装
- 保持系统和 Codex 更新
- 使用 unelevated 沙箱模式
- 配置合理的代理（如需要）


> Windows 原生支持让 Codex 可以无缝融入你的 Windows 工作流程。


---


## 常见问题


### Q: Windows 原生版本和 WSL 版本哪个好？


对于大多数用户，原生版本更好 - 更快、更简单。


### Q: 可以和 WSL 共存吗？


可以，两者可以同时安装使用。


### Q: 需要管理员权限吗？


不需要，unelevated 模式不需要管理员权限。


### Q: 支持 PowerShell ISE 吗？


推荐使用 Windows Terminal 或新版 PowerShell。








	  AI 思考中...





			** [Codex GitHub 集成](https://www.runoob.com/codex-github.html)
			[Codex Worktrees 使用](https://www.runoob.com/codex-worktrees.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#7011141d191e3002051e1f1f125e131f1d)

      : · [免责声明](https://www.runoob.com/disclaimer)

      : · [关于我们](https://www.runoob.com/aboutus)

      : · [文章归档](https://www.runoob.com/archives)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/)**
    **[runoob.com](https://www.runoob.com/)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **