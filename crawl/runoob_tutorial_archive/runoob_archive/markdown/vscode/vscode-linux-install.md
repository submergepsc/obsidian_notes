# VSCode Linux 安装

- Source: https://www.runoob.com/vscode/vscode-linux-install.html

VSCode 是微软开发的跨平台免费源代码编辑器，支持 Windows、macOS 和 Linux。


在安装 VS Code 之前，请确保您的设备满足以下最低要求：


| 操作系统 | 最低要求 |
| --- | --- |
| Windows | Windows 7 64 位或更高版本 |
| macOS | macOS 10.11 El Capitan 或更高版本 |
| Linux | Ubuntu 16.04+, Debian 9+, Fedora 30+, CentOS 7+ |
**

VS Code 官方网站下载页面：[**https://code.visualstudio.com/Download**](https://code.visualstudio.com/Download)。


[![](https://www.runoob.com/wp-content/uploads/2024/12/09d4644e-f7ea-4b75-bf73-581ce3ace159.png)](http://)


默认情况下访问 VS Code 官网 [**https://code.visualstudio.com/**](https://code.visualstudio.com/)，页面会根据你的系统自动匹配安装包，比如我是 macOS，就会出现 **Download for macOS** 按钮：


![](https://www.runoob.com/wp-content/uploads/2024/12/619fba21-8281-4af8-bf1e-d65bcdf0b74c.png)


---


## 在 Linux 上安装


访问 VS Code 官网 [**https://code.visualstudio.com/**](https://code.visualstudio.com/)，会显示各大 Linux 发行平台的安装包 。


![](https://www.runoob.com/wp-content/uploads/2024/12/697d4a70-b515-47e0-adab-725c165716e4.png)


### 使用包管理器安装（推荐）


对于基于 Debian 的系统（如 Ubuntu）：


```
sudo apt update
sudo apt install software-properties-common apt-transport-https
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code
```


对于基于 Red Hat 的系统（如 Fedora）：


```
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo dnf check-update
sudo dnf install code
```


直接下载二进制包安装

从 VS Code 官网 下载适配的 .deb 或 .rpm 文件。


对于 .deb 文件：


```
sudo dpkg -i code*.deb
sudo apt-get install -f
```


对于 .rpm 文件：


sudo rpm -i code*.rpm

运行 VS Code

在终端输入 code 启动 VS Code，或者通过系统菜单打开。


![](https://www.runoob.com/wp-content/uploads/2024/12/installing-vscode-mac09.png)

---

## VSCode 的 code 命令


启用 VSCode 的 code 命令非常简单，先打开命令面板：



- macOS 系统快捷键：**⇧⌘P**
- Windows/Linux 快捷键: **Ctrl + Shift + P**


搜索安装** >shell command**:


![](https://www.runoob.com/wp-content/uploads/2024/12/525b3be6-bc44-4043-acaa-3874afbba399.png)

然后选择 **Shell Command: Install 'code' command in PATH** 即可为系统 PATH 路径添加了 **code** 命令的引用。










	  AI 思考中...





			** [VSCode macOS 安装](https://www.runoob.com/vscode-macos-install.html)
			[VSCode 界面说明](https://www.runoob.com/vscode-start-intro.html) **













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