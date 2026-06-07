# Zig 环境安装

- Source: https://www.runoob.com/zig/zig-setup.html

在配置 Zig 编程语言的开发环境时，需要安装 Zig 编译器并设置相关的开发工具。

以下是在不同操作系统上配置 Zig 的步骤：


## 使用包管理器来安装


### Windows


Zig 在 Chocolatey 上可用：


```
choco install zig
```


Windows (winget)


```
winget install zig.zig
```


Windows (scoop)：


```
scoop install zig
```


### MacOS

Homebrew 安装：


```
brew install zig
```


### Linux


Ubuntu (snap)


稳定版本安装：


```
snap install zig --classic --beta
```


Fedora:


```
dnf install zig
```


FreeBSD:


```
pkg install lang/zig
```



配置完毕后，你就可以开始使用 Zig 编程语言进行开发了。


## 源码安装

我们也可以下载源码来编译安装。


Zig 源码包下载地址：[https://ziglang.org/zh/download/](https://ziglang.org/zh/download/)。


![](https://www.runoob.com/wp-content/uploads/2024/07/53b0ae868d797ee6e94fd8d39acd67172.png)


下载后，使用 tar 命令来解压：


```
tar -xvf zig-macos-aarch64-0.13.0.tar.xz
```


然后进入源码包，进行后续的编译安装：


```
cd zig-macos-aarch64-0.13.0
```


也可以从 Zig 的 GitHub 仓库克隆源码：


```
git clone https://github.com/ziglang/zig.git
```



### 依赖项


- cmake >= 3.5
- gcc >= 7.0.0 或者 clang >= 6.0.0
- LLVM、Clang、LLD 开发库 == 18.x，使用相同版本的 gcc 或 clang 编译 可以使用系统包管理器安装，或者从源代码构建。




### 指令


- 在 Zig 源码目录下，创建一个 build 目录：
```
mkdir build
cd build
```

- 运行 cmake：
```
cmake ..
```

- 构建和安装 Zig：
```
make install
```



请注意 `CMAKE_PREFIX_PATH` 这个方便的 cmake 变量。CMake 会优先在这个位置查找 LLVM 和其他依赖项。


这些步骤将生成 `stage3/bin/zig`，这是由 Zig 自身构建的 Zig 编译器。


### macOS + Homebrew


对于 macOS 使用 Homebrew：


- 在 Zig 源码目录下，创建一个 build 目录：
```
mkdir build
cd build
```

- 运行 cmake，并启用静态 LLVM：
```
cmake .. -DZIG_STATIC_LLVM=ON -DCMAKE_PREFIX_PATH="$(brew --prefix llvm@18);$(brew --prefix zstd)"
```

- 构建和安装 Zig：
```
make install
```



### FreeBSD


对于 FreeBSD：


- 使用 pkg 安装必要的依赖项：
```
sudo pkg install -qyr FreeBSD devel/llvm18 devel/cmake archivers/zstd textproc/libxml2 archivers/lzma
```

- 在 Zig 源码目录下，创建一个 build 目录：
```
mkdir build
cd build
```

- 运行 cmake，并启用静态 LLVM：
```
cmake .. -DZIG_STATIC_LLVM=ON -DCMAKE_PREFIX_PATH="/usr/local/llvm18;/usr/local"
```

- 构建和安装 Zig：
```
make install
```



这些步骤会在你的系统上安装 Zig 编译器。









	  AI 思考中...





			** [Zig 教程](https://www.runoob.com/zig-tutorial.html)
			[Zig 基本语法](https://www.runoob.com/zig-basic-syntax.html) **













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