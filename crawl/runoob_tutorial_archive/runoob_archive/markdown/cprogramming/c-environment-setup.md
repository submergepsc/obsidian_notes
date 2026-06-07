# C 环境设置

- Source: https://www.runoob.com/cprogramming/c-environment-setup.html

如果您想要设置 C 语言环境，您需要确保电脑上有以下两款可用的软件，文本编辑器和 C 编译器。


## 文本编辑器


通过编辑器创建的文件通常称为源文件，源文件包含程序源代码。

C 程序的源文件通常使用扩展名 **.c**。


在开始编程之前，请确保您有一个文本编辑器，且有足够的经验来编写一个计算机程序，然后把它保存在一个文件中，编译并执行它。


- **Visual Studio Code**：虽然它是一个通用的文本编辑器，但它有很多插件支持 C/C++ 开发，使其成为一个流行的选择，通过安装 C/C++ 插件和调整设置，你可以使其成为一个很好的 C 语言开发环境。安装教程：[https://www.runoob.com/w3cnote/vscode-tutorial.html](https://www.runoob.com/w3cnote/vscode-tutorial.html) 下载地址：[https://code.visualstudio.com/](https://code.visualstudio.com/)
- **Sublime Text**：Sublime Text 是一个轻量级、快速和高度可定制的文本编辑器，有很多插件支持 C 语言的开发。它具有强大的代码编辑功能和快捷键，使得编码更加高效。 下载地址：[https://www.sublimetext.com/](https://www.sublimetext.com/)
- **Atom**：Atom 是一个开源的文本编辑器，由 GitHub 开发，它有很多插件和主题，可以定制为一个适合 C 语言开发的环境。 下载地址：[https://atom-editor.cc/](https://atom-editor.cc/)
- **Vim** 和 **Emacs**：这两个是传统的文本编辑器，它们有着强大的编辑功能和高度的可定制性，对于熟练的用户来说非常强大，有很多插件和配置可以支持C语言的开发。
- **Eclipse**：Eclipse 是另一个功能强大的集成开发环境，虽然它最初是为 Java 开发设计的，但通过安装 C/C++ 插件，可以使其支持 C 语言开发。
- 32 位系统：[installer.exe](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/)
- 64 位系统：[installer.exe](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/installer/)


![](https://www.runoob.com/wp-content/uploads/2014/09/6576bba5be6352d1268c7769704a537e44.png)


这种安装，会碰到网络连接错误问题，所以我们可以直接下载 sjlj （稳定的，64 位和 32 位都支持）：


- [下载 32 位 sjlj](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/8.1.0/threads-posix/sjlj/)
- [下载 64 位 sjlj](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/sjlj/)


下载完成后，解压，在 bin 目录里面就可以找到 g++.exe 或者 gcc.exe：


![](https://www.runoob.com/wp-content/uploads/2014/09/0c7bc6a0115ffa879f01885c9bbe6e75.png)


当安装 MinGW 时，您至少要安装 gcc-core、gcc-g++、binutils 和 MinGW runtime，但是一般情况下都会安装更多其他的项。


添加您安装的 MinGW 的 bin 子目录到您的 **PATH** 环境变量中，这样您就可以在命令行中通过简单的名称来指定这些工具。


![](https://www.runoob.com/wp-content/uploads/2014/09/c3452d2b6a990b107498381ccfef5bd4.png)


当完成安装时，您可以从 Windows 命令行上运行 gcc、g++、ar、ranlib、dlltool 和其他一些 GNU 工具。









	  AI 思考中...





			** [C 简介](https://www.runoob.com/c-intro.html)
			[C 程序结构](https://www.runoob.com/c-program-structure.html) **