# Rust 环境搭建

- Source: https://www.runoob.com/rust/rust-setup.html

Rust 支持很多的集成开发环境（IDE）或开发专用的文本编辑器。


官方网站公布支持的工具如下（[https://www.rust-lang.org/zh-CN/tools](https://www.rust-lang.org/zh-CN/tools)）：


![](https://www.runoob.com/wp-content/uploads/2020/04/F39BCE6A-4324-4B82-AE80-BD6417183600.jpg)


本教程将使用 Visual Studio Code 作为我们的开发环境（Eclipse 有专用于 Rust 开发的版本，对于初学者也是不错的选择）。


**注意：**IntelliJ IDEA 安装插件之后难以调试，所以推荐习惯使用 IDEA 的开发者使用 CLion，但 CLion 不是免费的。


## 搭建 Visual Studio Code 开发环境


首先，需要安装最新版的 Rust 编译工具和 Visual Studio Code。


Rust 编译工具：[https://www.rust-lang.org/zh-CN/tools/install](https://www.rust-lang.org/zh-CN/tools/install)


Visual Studio Code：[https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)


Rust 的编译工具依赖 C 语言的编译工具，这意味着你的电脑上至少已经存在一个 C 语言的编译环境。如果你使用的是 Linux 系统，往往已经具备了 GCC 或 clang。如果你使用的是 macOS，需要安装 Xcode。如果你是用的是 Windows 操作系统，你需要安装 Visual Studio 2013 或以上的环境（需要 C/C++ 支持）以使用 MSVC 或安装 MinGW + GCC 编译环境（Cygwin 还没有测试）。


### 安装 Rust 编译工具


Rust 编译工具可以去官方网站下载： [https://www.rust-lang.org/zh-CN/tools/install](https://www.rust-lang.org/zh-CN/tools/install)。

macOS、Linux 或其它类 Unix 系统要下载 Rustup 并安装 Rust，请在终端中运行以下命令:


```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```


Windows 要下载 [`rustup-init.exe`](https://static.rust-lang.org/rustup/dist/i686-pc-windows-gnu/rustup-init.exe) 可执行文件。


下载好的 Rustup 在 Windows 上是一个可执行程序 rustup-init.exe。


现在执行 rustup-init 文件：


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env1.png)


上图显示的是一个命令行安装向导。


**如果你已经安装 MSVC （推荐），那么安装过程会非常的简单，输入 1 并回车，直接进入第二步**。



如果你安装的是 MinGW，那么你需要输入 2 （自定义安装），然后系统会询问你 Default host triple? ，请将上图中 **default host triple** 的 "msvc" 改为 "gnu" 再输入安装程序：



![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env2.png)


其它属性都默认。


设置完所有选项，会回到安装向导界面（第一张图），这是我们输入 1 并回车即可。


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env3.png)


进行到这一步就完成了 Rust 的安装，可以通过以下命令测试：


```
rustc -V        # 注意的大写的 V
```


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env4.png)


如果以上两个命令能够输出你安装的版本号，就是安装成功了。


更多下载方式可以查阅：[https://forge.rust-lang.org/infra/other-installation-methods.html](https://forge.rust-lang.org/infra/other-installation-methods.html)



### 搭建 Visual Studio Code 开发环境


下载完 Visual Studio Code 安装包之后启动安装向导安装（此步骤不在此赘述）。


安装完 Visual Studio Code （下文简称 VSCode）之后运行 VSCode。


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env5.png)


在左边栏里找到 "Extensions"，并查找 "Chinese"，安装简体中文扩展，使界面变成中文。（如果你愿意用英文界面或计算机不支持中文字符，此步骤可以跳过）。


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env6.png)


用同样的方法再安装 rust-analyzer 和 Native Debug 两个扩展。


![](https://www.runoob.com/wp-content/uploads/2020/04/49033261-B1B8-4D70-8090-53DC45A8727E.jpeg)


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env8.png)


重新启动 VSCode，Rust 的开发环境就搭建好了。


现在新建一个文件夹，如 runoob-greeting。


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env9.png)


在 VSCode 中打开新建的文件夹：


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env10.png)


打开文件夹之后选择菜单栏中的"终端"-"新建终端"，会打开一个新的终端：


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env11.png)


在终端中输入命令：


```
cargo new greeting
```


当前文件下下会构建一个名叫 greeting 的 Rust 工程目录。


![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env12.png)


现在在终端里输入以下三个命令：


```
cd ./greeting
cargo build
cargo run
```


系统在创建工程时会生成一个 Hello, world 源程序 main.rs，这时会被编译并运行：



![](https://www.runoob.com/wp-content/uploads/2020/04/rust-env13.png)


至此，你成功的构建了一个 Rust 命令行程序！


有关在 VSCode 中调试程序的问题，详见 [Cargo 教程](https://www.runoob.com/cargo-tutorial.html)。








	  AI 思考中...





			** [Rust 教程](https://www.runoob.com/rust-tutorial.html)
			[Cargo 教程](https://www.runoob.com/cargo-tutorial.html) **













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