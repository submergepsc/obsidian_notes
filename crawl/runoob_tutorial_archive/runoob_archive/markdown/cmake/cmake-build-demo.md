# CMake 构建实例

- Source: https://www.runoob.com/cmake/cmake-build-demo.html

CMake 构建步骤如下：


- **创建 `CMakeLists.txt` 文件**：定义项目、目标和依赖。
- **创建构建目录**：保持源代码目录整洁。
- **配置项目**：使用 CMake 生成构建系统文件。
- **编译项目**：使用构建系统文件编译项目。
- **运行可执行文件**：执行生成的程序。
- **清理构建文件**：删除中间文件和目标文件。


假设我们有一个简单的 C++ 项目，包含一个主程序文件和一个库文件，我们将使用 CMake 构建这个项目。


我们的项目结构如下：


```
MyProject/
├── CMakeLists.txt
├── src/
│   ├── main.cpp
│   └── mylib.cpp
└── include/
    └── mylib.h
```


- `main.cpp`：主程序源文件。
- `mylib.cpp`：库源文件。
- `mylib.h`：库头文件。
- `CMakeLists.txt`：CMake 配置文件。


### 1、创建 CMakeLists.txt 文件

在 MyProject 目录下创建 CMakeLists.txt 文件。


CMakeLists.txt 文件用于配置 CMake 项目。


** CMakeLists.txt 文件内容：**


## 实例


```
cmake_minimum_required(VERSION 3.10)   # 指定最低 CMake 版本

project(MyProject VERSION 1.0)          # 定义项目名称和版本

# 设置 C++ 标准为 C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 添加头文件搜索路径
include_directories(${PROJECT_SOURCE_DIR}/include)

# 添加源文件
add_library(MyLib src/mylib.cpp)        # 创建一个库目标 MyLib
add_executable(MyExecutable src/main.cpp)  # 创建一个可执行文件目标 MyExecutable

# 链接库到可执行文件
target_link_libraries(MyExecutable MyLib)
```


** 说明：**


- **`cmake_minimum_required(VERSION 3.10)`**：指定 CMake 的最低版本为 3.10。
- **`project(MyProject VERSION 1.0)`**：定义项目名称为 `MyProject`，版本为 1.0。
- **`set(CMAKE_CXX_STANDARD 11)`**：指定 C++ 标准为 C++11。
- **`include_directories(${PROJECT_SOURCE_DIR}/include)`**：指定头文件目录。
- **`add_library(MyLib src/mylib.cpp)`**：创建一个名为 `MyLib` 的库，源文件是 `mylib.cpp`。
- **`add_executable(MyExecutable src/main.cpp)`**：创建一个名为 `MyExecutable` 的可执行文件，源文件是 `main.cpp`。
- **`target_link_libraries(MyExecutable MyLib)`**：将 `MyLib` 库链接到 `MyExecutable` 可执行文件。


### 2、创建构建目录

为了保持源代码目录的整洁，我们将在项目根目录下创建一个单独的构建目录。


**创建构建目录**

打开终端，进入 MyProject 目录，然后创建构建目录：


```
mkdir build
cd build
```


### 3、配置项目

在构建目录中使用 CMake 配置项目。


这将生成适合平台的构建系统文件（如 Makefile）。


**运行 CMake 配置**

在构建目录中运行 CMake 配置命令：


```
cmake ..
```


- **`cmake ..`**：`..` 指向源代码目录，即包含 `CMakeLists.txt` 文件的目录。CMake 将读取 `CMakeLists.txt` 文件并生成构建系统文件。


### 4、编译项目

使用生成的构建系统文件编译项目。根据生成的构建系统文件类型，使用相应的构建命令。


**使用 Makefile**

如果生成了 Makefile（在大多数类 Unix 系统中默认生成），可以使用 make 命令进行编译：


```
make
```


- **`make`**：编译项目并生成可执行文件 `MyExecutable`。


### 5、运行可执行文件

编译完成后，可以运行生成的可执行文件。


**运行可执行文件**

在构建目录中，运行 MyExecutable：


```
./MyExecutable
```


### 6、清理构建文件

清理构建文件以删除生成的中间文件和目标文件。


**使用 make clean**

如果在 CMakeLists.txt 中定义了清理规则，可以使用 **make clean** 命令：


```
make clean
```


- **`make clean`**：删除中间文件和目标文件。


**手动删除**

如果没有定义清理规则，可以手动删除构建目录中的所有文件：


```
rm -rf build/*
```









	  AI 思考中...





			** [CMake 构建流程](https://www.runoob.com/cmake-build-flow.html)
			[CMake 高级特性](https://www.runoob.com/cmake-advanced-features.html) **













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