# PowerShell 安装

- Source: https://www.runoob.com/powershell/powershell-install.html

PowerShell 自从 6.0 起实现了完全开源和跨平台（PowerShell Core / PowerShell 7+），可运行于 Windows、Linux 和 macOS。


---


## 一、Windows 上安装 PowerShell 7+


### 方法一：使用 MSI 安装包（推荐）


- 打开 PowerShell 官方 GitHub 发布页： 👉 [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)
- 找到最新版本，下载适用于 Windows 的 `.msi` 安装包
- 双击安装，默认路径安装即可
- 安装完成后，搜索 **"PowerShell 7"** 打开即可（不会覆盖 Windows PowerShell）


### 方法二：使用命令行（Winget）


适用于 Windows 10/11 且安装了 Windows 包管理器：


```
winget install --id Microsoft.Powershell --source winget
```



可选参数：`--silent` 表示静默安装，`--version 7.4.1` 可指定版本


---


## 二、Linux 上安装 PowerShell


### Ubuntu / Debian


```
# 安装依赖
sudo apt update
sudo apt install -y wget apt-transport-https software-properties-common

# 导入微软 GPG 密钥
wget -q https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb

# 安装 PowerShell
sudo apt update
sudo apt install -y powershell
```


启动 PowerShell：


```
pwsh
```


---


### CentOS / RHEL / Fedora


```
# 添加 Microsoft YUM 源
sudo dnf install -y https://packages.microsoft.com/config/rhel/8/packages-microsoft-prod.rpm

# 安装 PowerShell
sudo dnf install -y powershell
```


或 CentOS 7 使用 `yum`：


```
sudo yum install -y powershell
```


---


### Arch Linux / Manjaro


```
sudo pacman -S powershell
```


**

如果找不到，可使用 AUR 包管理器（如 `yay`）


---


## 三、macOS 上安装 PowerShell


### 方法一：使用 Homebrew（推荐）


```
brew install --cask powershell
```


启动 PowerShell：


```
pwsh
```


### 方法二：手动下载 PKG 安装包


- 前往 GitHub 发布页 👉 [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases)
- 下载 `.pkg` 安装文件（如 `powershell-7.4.1-osx-x64.pkg`）
- 双击安装并根据引导完成


---


## 四、安装验证与卸载


### 验证是否安装成功


```
pwsh --version
```


### 卸载 PowerShell


| 平台 | 卸载方式 |
| --- | --- |
| Windows | 控制面板 → 程序与功能 → 卸载 PowerShell 7 |
| Ubuntu | sudo apt remove powershell |
| CentOS | sudo yum remove powershell |
| macOS（brew） | brew uninstall powershell |


---


## 不同平台启动命令


| 平台 | 命令 |
| --- | --- |
| Windows | pwsh.exe 或开始菜单搜索 "PowerShell 7" |
| Linux | pwsh |
| macOS | pwsh |








	  AI 思考中...





			** [PowerShell 简介](https://www.runoob.com/powershell-intro.html)
			[PowerShell 核心概念](https://www.runoob.com/powershell-core.html) **













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