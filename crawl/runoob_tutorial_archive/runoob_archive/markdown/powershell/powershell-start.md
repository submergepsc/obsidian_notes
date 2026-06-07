# PowerShell 入门

- Source: https://www.runoob.com/powershell/powershell-start.html

PowerShell 是微软为 Windows 系统打造的一种命令行壳程序 + 脚本环境，主要用于系统管理与自动化任务。


在 **Windows 11** 中，直接在开始菜单搜索 **PowerShell** 即可。


![](https://www.runoob.com/wp-content/uploads/2025/07/powershell-start-1.jpg)


常见的快捷方式包括（如为 64 位系统）：


| 快捷方式名称 | 说明 |
| --- | --- |
| Windows PowerShell | 64 位命令行版 |
| Windows PowerShell ISE | 64 位图形脚本编辑器 |
| Windows PowerShell (x86) | 32 位命令行版 |
| Windows PowerShell ISE (x86) | 32 位图形脚本编辑器 |


⚠️ 注意：Windows 11 本身不支持 32 位系统，但仍包含 x86 的 PowerShell 版本以兼容旧程序。


---


## 启动 PowerShell 的方法


### 普通启动方式

单击 Windows PowerShell 快捷方式启动 PowerShell 控制台。


PowerShell 控制台的标题栏会显示 "Windows PowerShell"。


![](https://www.runoob.com/wp-content/uploads/2025/07/powershell-start-2.jpg)


**注意：**某些命令在以普通用户身份运行 PowerShell 时可以正常运行，但 PowerShell 本身不参与用户访问控制（UAC），无法提示用户提升权限。


### 用户访问控制（UAC）说明

**UAC 作用：**Windows 安全功能，防止恶意代码以提升权限运行。


** 普通用户权限限制**：当以普通用户身份运行时，尝试执行需要管理员权限的命令会报错。


例如停止 Windows 服务：


```
Stop-Service -Name W32Time
```


报错信息示例：


```
Stop-Service : Service 'Windows Time (W32Time)' cannot be stopped due to
the following error: Cannot open W32Time service on computer '.'.
At line:1 char:1
+ Stop-Service -Name W32Time
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : CloseError: (System.ServiceProcess.ServiceCon
   troller:ServiceController) [Stop-Service], ServiceCommandException
    + FullyQualifiedErrorId : CouldNotStopService,Microsoft.PowerShell.Comm
   ands.StopServiceCommand
```


**解决方案：需**要使用提升为本地管理员权限的用户运行 PowerShell。

配置了第二个域用户帐户，符合最小权限原则，不是域管理员且无域内提升权限。


**操作步骤：**


- 右键点击 Windows PowerShell 快捷方式
- 选择"以管理员身份运行"


![](https://www.runoob.com/wp-content/uploads/2025/07/powershell-start-3.jpg)


**系统提示：**由于当前以普通用户登录，Windows 会提示输入本地管理员用户凭据。


![](https://www.runoob.com/wp-content/uploads/2025/07/powershell-start-4.png)


**确认提升：**提升后的 PowerShell 窗口标题栏显示"管理员：Windows PowerShell"。


![](https://www.runoob.com/wp-content/uploads/2025/07/powershell-start-5.jpg)


**效果：**在提升的 PowerShell 中运行需要管理员权限的命令，不再遇到 UAC 错误。


**权限提升原则**：只有在绝对必要时才应以管理员身份提升 PowerShell。

**远程计算机：**面向远程计算机时，无需提升 PowerShell 权限。提升权限只影响本地命令。


**固定快捷方式：**可将 PowerShell 或 Windows 终端快捷方式固定到任务栏，方便启动：


![](https://www.runoob.com/wp-content/uploads/2025/07/powershell-start-6.jpg)


**安全启动提升的 PowerShell：**如果需要提升权限启动 PowerShell，可按住 Shift 键，同时右键点击任务栏上固定的 PowerShell 图标，选择"以管理员身份运行"


![](https://www.runoob.com/wp-content/uploads/2025/07/powershell-start-7.jpg)


---


## 确定 PowerShell 版本及执行策略指南


### 一、查看 PowerShell 版本


PowerShell 提供自动变量 `$PSVersionTable`，包含当前 PowerShell 会话的版本和相关信息。


```
$PSVersionTable
```


输出结果类似如下：


```
Name                           Value
----                           -----
PSVersion                      5.1.22621.2428
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.22621.2428
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
```


### 版本说明


- Windows PowerShell 5.1 预装于当前支持的 Windows 版本中，是推荐使用的版本。
- PowerShell 7（跨平台版）并非 Windows PowerShell 5.1 的替代品，而是与之并行安装的不同产品。
- PowerShell 6（也称 PowerShell Core）已不再受支持。


### 二、理解执行策略（Execution Policy）


执行策略是 PowerShell 的安全功能，用于控制脚本运行条件，防止无意执行恶意脚本。

**

注意：执行策略不是安全边界，熟练用户可绕过。


### 执行策略的作用范围


- 可以针对本地计算机（LocalMachine）、当前用户（CurrentUser）或当前会话（Process）设置。
- 也可通过组策略管理用户和计算机的执行策略。


### 常见 Windows 默认执行策略


| 操作系统版本 | 默认执行策略 |
| --- | --- |
| Windows Server 2022 | RemoteSigned |
| Windows Server 2019 | RemoteSigned |
| Windows Server 2016 | RemoteSigned |
| Windows 11 | Restricted |
| Windows 10 | Restricted |


> Restricted** 表示默认不允许执行任何脚本。


### 三、查询当前执行策略


查询当前策略：


```
Get-ExecutionPolicy
```


输出结果类似如下：


```
Restricted
```


列出所有范围的执行策略设置：


```
Get-ExecutionPolicy -List
```


输出类似如下：


```
Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser       Undefined
 LocalMachine       Undefined
```


### 四、执行策略对脚本运行的影响示例


假设有脚本文件 `Get-TimeService.ps1`，直接在交互式命令行运行该命令正常：


```
Get-Service -Name W32Time
```


但是，从脚本中运行相同的命令时，PowerShell 将返回错误。


```
.\Get-TimeService.ps1
```


错误信息：


```
.\Get-TimeService.ps1 : File C:\tmp\Get-TimeService.ps1 cannot be loaded
because running scripts is disabled on this system. For more information,
see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\Get-TimeService.ps1
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```


### 五、修改执行策略


#### 1. 设置为 RemoteSigned（推荐）


允许运行本地脚本和受信任发布者签名的远程脚本。


```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```


- 必须以管理员身份运行 PowerShell 才能更改本地计算机（LocalMachine）的执行策略。
- 更改时会有确认提示：


```
Do you want to change the execution policy? [Y] Yes  [A] Yes to All  ...
```


#### 2. 仅修改当前用户的执行策略（无需管理员权限）


```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```


### 六、常见错误提示及解决


**未提升管理员权限修改 LocalMachine 策略时错误：**


```
Access to the registry key 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell' is denied.
```


**解决方案**：以管理员身份运行 PowerShell 后重试，或只修改当前用户策略。


### 七、修改后验证


执行策略修改为 `RemoteSigned` 后，运行脚本：


```
.\Get-TimeService.ps1
```


输出结果：


```
Status   Name    DisplayName
------   ----    -----------
Running  W32Time Windows Time
```


### 八、注意事项 脚本是纯文本文件，扩展名为 .ps1。 推荐使用 Visual Studio Code 或文本编辑器编写脚本。 在修改执行策略前，请阅读官方文档 about_Execution_Policies 了解相关安全风险。 AI 思考中... PowerShell 核心概念 PowerShell 面向对象的命令行 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/../skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/../skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/../skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/../skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/../skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/../skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/../skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)

      : · [免责声明](https://www.runoob.com/../disclaimer/index.html)

      : · [关于我们](https://www.runoob.com/../aboutus/index.html)

      : · [文章归档](https://www.runoob.com/../archives/index.html)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/../index/index.html)**
    **[runoob.com](https://www.runoob.com/../index/index.html)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **