# PowerShell Cmdlet 基础

- Source: https://www.runoob.com/powershell/powershell-cmdlet.html

**Cmdlet（发音类似 "command-let"）** 是 PowerShell 中的基本命令单元，由 Microsoft 基于 .NET 框架实现的小型命令。


Cmdlet 不同于传统 shell 中的外部程序，例如 `.exe` 或 `.bat` 文件，而是内置于 PowerShell 运行时环境中的。


每个 Cmdlet 执行一项特定的任务，比如获取数据、设置属性、创建对象、导出文件等。


### Cmdlet 的命名规则：动词-名词


PowerShell 中所有 Cmdlet 的命名都遵循统一的 **"动词-名词"** 格式，例如：


- `Get-Process`：获取进程信息
- `Set-Date`：设置系统日期
- `New-Item`：创建新项（如文件或文件夹）
- `Remove-Service`：删除服务


这种命名方式既直观又一致，便于记忆和查找。


---


## Cmdlet 的基本语法结构


Cmdlet 的语法结构一般如下：


```
动词-名词 [-参数名 参数值] [-开关参数]
```


示例：


```
Get-Service -Name W32Time
```


说明：


- `Get-Service`：获取服务对象
- `-Name W32Time`：指定要查询的服务名称为 `W32Time`


再如：


```
Stop-Process -Id 1234 -Force
```


- `-Id` 是带值参数
- `-Force` 是开关参数，不需要指定值


---


## 参数与管道的结合


Cmdlet 支持**位置参数**、**命名参数**和**管道输入**。这使得命令可以灵活组合，构建复杂的工作流。


示例 1：指定参数形式


```
Get-Process -Name notepad
```


示例 2：通过管道传递


```
"notepad" | Get-Process -Name
```


示例 3：对象管道传递给另一个 Cmdlet


```
Get-Process notepad | Stop-Process
```


在上面这个例子中，`Get-Process` 获取了 notepad 进程对象，然后通过管道传递给 `Stop-Process` 来终止它。


---


## 查看 Cmdlet 的帮助信息


PowerShell 提供了完整的帮助系统，可以使用 `Get-Help` 查看任何 Cmdlet 的用法：


```
Get-Help Get-Process
```


要查看更多参数说明和示例，可加上 `-Detailed` 或 `-Examples`：


```
Get-Help Get-Process -Examples
```


如果是首次使用 PowerShell，建议执行一次以下命令来更新本地帮助：


```
Update-Help
```


---


## 常见基础 Cmdlet 速查表


| Cmdlet | 功能说明 |
| --- | --- |
| Get-Command | 查看所有可用命令 |
| Get-Help | 查看命令的帮助信息 |
| Get-Process | 获取进程列表 |
| Get-Service | 获取服务列表 |
| Start-Service | 启动服务 |
| Stop-Service | 停止服务 |
| Set-ExecutionPolicy | 设置执行策略 |
| New-Item | 创建新文件或文件夹 |
| Remove-Item | 删除文件或文件夹 |
| Copy-Item | 复制文件或文件夹 |
| Move-Item | 移动文件或文件夹 |
| Clear-Host | 清屏，类似于 cls |


---


## 实践示例：文件操作


创建文件夹：


```
New-Item -Path "C:\TestFolder" -ItemType Directory
```


在该目录下创建文本文件：


```
New-Item -Path "C:\TestFolder\demo.txt" -ItemType File
```


将内容写入文件：


```
Set-Content -Path "C:\TestFolder\demo.txt" -Value "Hello PowerShell"
```


读取文件内容：


```
Get-Content -Path "C:\TestFolder\demo.txt"
```


---


## 小结与学习建议


- Cmdlet 是 PowerShell 的核心单位，每个 Cmdlet 都是功能明确的任务执行器。
- 统一的 "动词-名词" 命名规范让 Cmdlet 可预测、易于学习。
- 管道、参数系统与对象模型相结合，使 Cmdlet 在数据处理和自动化方面表现出色。
- 掌握常用 Cmdlet 并结合对象操作，是学习 PowerShell 的重要起点。


建议初学者从以下方面着手练习：


- 使用 `Get-Command` 探索所有可用命令
- 配合 `Get-Help` 学会查阅命令用法
- 利用 `New-Item` 和 `Get-Content` 等命令进行本地文件操作
- 多尝试通过管道将命令组合起来处理数据








	  AI 思考中...





			** [PowerShell 面向对象的命令行](https://www.runoob.com/powershell-object-oriented-command-line.html)
			[PowerShell 基本语法](https://www.runoob.com/powershell-basic-syntax.html) **













### 点我分享笔记







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