# CMake 安装与配置

- Source: https://www.runoob.com/cmake/cmake-install-setup.html

CMake 支持的操作系统：


- Microsoft Windows
- Apple macOS
- Linux
- FreeBSD
- OpenBSD
- Solaris
- AIX


## 安装 CMake


CMake 可以在不同操作系统上进行安装，本文将介绍 Windows、Linux 以及 macOS 系统下的安装与配置。


CMake 安装包下载地址：[https://cmake.org/download/](https://cmake.org/download/)。


下载页面包含了源码包及二进制包：


![](https://www.runoob.com/wp-content/uploads/2024/08/8a839a1a47dcc903de5f357d6d135056.png)


我们可以在上面二进制包列表中下载适用于我们操作系统的安装包。


### Windows

选择 Windows 版本的安装包（通常是 .msi 文件）。


下载后，双击下载的 **.msi** 文件，按照安装向导的指示进行安装。


![](https://www.runoob.com/wp-content/uploads/2024/08/cmake-install-win.png)

在安装过程中，可以选择将 CMake 添加到系统的 PATH 环境变量中（建议选择此选项，以便在命令行中直接使用 cmake 命令）。


![](https://www.runoob.com/wp-content/uploads/2024/08/cmake_add_path.png)


**验证安装：**打开命令提示符（CMD）或 PowerShell，输入 **cmake --version**，查看是否能正确显示 CMake 的版本信息。


### macOS


**通过 Homebrew 安装**


打开终端（Terminal），执行以下安装命令：


```
brew install cmake
```


**通过官方安装包**

访问 CMake 官方网站的下载页面，选择 macOS 版本的 **.dmg** 文件。


下载并运行 **.dmg** 文件，拖动 CMake 图标到应用程序文件夹。


![](https://www.runoob.com/wp-content/uploads/2024/08/5cac8e3d98e790c979886af2d7cdec198.png)


安装成功后，命令都在 **/Applications/CMake.app/Contents/bin** 目录下，我们需要将环境变量添加到 **.bash_profile** 文件中，使用 vim 进行编辑：


```
vim ~/.bash_profile
```


将以下内容添加到文件末尾：


```
export PATH="/Applications/CMake.app/Contents/bin":"$PATH"
```


添加完成后，执行 **source ~/.bash_profile** 或者重新启动终端。


**验证安装：**打开终端，输入 **cmake --version**，确认 CMake 已正确安装。


### Linux

**通过包管理器安装（适用于大多数发行版）：**


- 对于 Ubuntu 或 Debian 系统：**sudo apt-get install cmake**
- 对于 Fedora 系统：**sudo dnf install cmake**
- 对于 Arch Linux 系统：**sudo pacman -S cmake**


**从源码编译安装：**


访问 CMake 官方网站下载源码包。

解压源码包，进入解压后的目录。


执行以下命令编译和安装：


```
./bootstrap
make
sudo make install
```


**验证安装：**打开终端，输入 **cmake --version**，确认 CMake 安装成功。

---


## 配置 CMake


确保 CMake 的安装路径被添加到系统的 PATH 环境变量中，这样可以在任何位置的命令行中访问 CMake。


### Windows 环境变量设置


如果在安装过程中选择了将 CMake 添加到 PATH，则不需要额外配置。


如果未选择，可以手动添加：右键点击"计算机"或"此电脑"，选择"属性" -> "高级系统设置" -> "环境变量"，在"系统变量"中找到 Path，点击"编辑"，将 CMake 的安装路径添加进去。


### macOS 和 Linux


通常安装程序会自动配置 PATH，如果没有，可以手动配置。

打开终端，编辑 **~/.bash_profile** 或 **~/.zshrc** 文件，添加以下行：


```
export PATH="/usr/local/bin:$PATH"
```


运行 **source ~/.bash_profile** 或 **source ~/.zshrc** 使更改生效。


---


## CMake GUI 使用

CMake 也提供了图形用户界面（GUI），可以用于更直观地配置项目。


在 Windows 中，通常可以从开始菜单启动。


![](https://www.runoob.com/wp-content/uploads/2024/08/GUI-Source-Binary.png)

在 macOS 和 Linux 中，使用终端命令 cmake-gui 启动。


![](https://www.runoob.com/wp-content/uploads/2024/08/2119256-20230802084914066-381386925.png)


**设置源代码目录和构建目录：**


- **源代码目录（Source Code Directory）：** 指向包含 CMakeLists.txt 文件的目录。
- **构建目录（Build Directory）：** 指向用于存放生成的构建文件的目录。建议使用独立的目录以保持源代码的整洁。


**配置和生成：**


- 点击 "Configure" 按钮，选择编译器和构建选项，CMake 会检查依赖项并生成配置。
- 点击 "Generate" 按钮，CMake 会生成适合当前平台的构建文件。


通过上述步骤，用户可以安装和配置 CMake，并使其准备好用于构建和管理项目。








	  AI 思考中...





			** [CMake 教程](https://www.runoob.com/cmake-tutorial.html)
			[CMake 基础](https://www.runoob.com/cmake-basic.html) **













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