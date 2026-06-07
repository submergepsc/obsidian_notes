# CMake 基础

- Source: https://www.runoob.com/cmake/cmake-basic.html

## CMakeLists.txt 文件

CMakeLists.txt 是 CMake 的配置文件，用于定义项目的构建规则、依赖关系、编译选项等。


每个 CMake 项目通常都有一个或多个 CMakeLists.txt 文件。


### 文件结构和基本语法


CMakeLists.txt 文件使用一系列的 CMake 指令来描述构建过程。常见的指令包括：


1、指定 CMake 的最低版本要求：


```
cmake_minimum_required(VERSION <version>)
```


例如：


```
cmake_minimum_required(VERSION 3.10)
```


2、定义项目的名称和使用的编程语言：


```
project(<project_name> [<language>...])
```


例如：


```
project(MyProject CXX)
```


3、指定要生成的可执行文件和其源文件：


```
add_executable(<target> <source_files>...)
```


例如：


```
add_executable(MyExecutable main.cpp other_file.cpp)
```


4、创建一个库（静态库或动态库）及其源文件：


```
add_library(<target> <source_files>...)
```


例如：


```
add_library(MyLibrary STATIC library.cpp)
```


5、链接目标文件与其他库：


```
target_link_libraries(<target> <libraries>...)
```


例如：


```
target_link_libraries(MyExecutable MyLibrary)
```


6、添加头文件搜索路径：


```
include_directories(<dirs>...)
```


例如：


```
include_directories(${PROJECT_SOURCE_DIR}/include)
```


7、设置变量的值：


```
set(<variable> <value>...)
```


例如：


```
set(CMAKE_CXX_STANDARD 11)
```


8、设置目标属性：


```
target_include_directories(TARGET target_name
                          [BEFORE | AFTER]
                          [SYSTEM] [PUBLIC | PRIVATE | INTERFACE]
                          [items1...])
```


例如：


```
target_include_directories(MyExecutable PRIVATE ${PROJECT_SOURCE_DIR}/include)
```


9、安装规则：


```
install(TARGETS target1 [target2 ...]
        [RUNTIME DESTINATION dir]
        [LIBRARY DESTINATION dir]
        [ARCHIVE DESTINATION dir]
        [INCLUDES DESTINATION [dir ...]]
        [PRIVATE_HEADER DESTINATION dir]
        [PUBLIC_HEADER DESTINATION dir])
```


例如：


```
install(TARGETS MyExecutable RUNTIME DESTINATION bin)
```


10、条件语句 (if, elseif, else, endif 命令)


```
if(expression)
  # Commands
elseif(expression)
  # Commands
else()
  # Commands
endif()
```


例如：


```
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  message("Debug build")
endif()
```


11、自定义命令 (add_custom_command 命令)：


```
add_custom_command(
   TARGET target
   PRE_BUILD | PRE_LINK | POST_BUILD
   COMMAND command1 [ARGS] [WORKING_DIRECTORY dir]
   [COMMAND command2 [ARGS]]
   [DEPENDS [depend1 [depend2 ...]]]
   [COMMENT comment]
   [VERBATIM]
)
```


例如：


```
add_custom_command(
   TARGET MyExecutable POST_BUILD
   COMMAND ${CMAKE_COMMAND} -E echo "Build completed."
)
```


### 实例

一个简单的 CMakeLists.txt 文件示例：


## 实例


```
cmake_minimum_required(VERSION 3.10)
project(MyProject CXX)

# 添加源文件
add_executable(MyExecutable main.cpp)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)
```


---


## 变量和缓存


CMake 使用变量来存储和传递信息，这些变量可以在 CMakeLists.txt 文件中定义和使用。

变量可以分为普通变量和缓存变量。


### 变量定义与使用


**定义变量：**


```
set(MY_VAR "Hello World")
```


**使用变量：**


```
message(STATUS "Variable MY_VAR is ${MY_VAR}")
```


### 缓存变量

缓存变量存储在 CMake 的缓存文件中，用户可以在 CMake 配置时修改这些值。缓存变量通常用于用户输入的设置，例如编译选项和路径。


** 定义缓存变量：**


```
set(MY_CACHE_VAR "DefaultValue" CACHE STRING "A cache variable")
```


**使用缓存变量：**


```
message(STATUS "Cache variable MY_CACHE_VAR is ${MY_CACHE_VAR}")
```


---


## 查找库和包

CMake 可以通过 **find_package()** 指令自动检测和配置外部库和包。

常用于查找系统安装的库或第三方库。


### find_package() 指令


基本用法：


```
find_package(Boost REQUIRED)
```


指定版本：


```
find_package(Boost 1.70 REQUIRED)
```


查找库并指定路径：


```
find_package(OpenCV REQUIRED PATHS /path/to/opencv)
```


使用查找到的库：


```
target_link_libraries(MyExecutable Boost::Boost)
```


设置包含目录和链接目录：


```
include_directories(${Boost_INCLUDE_DIRS})
link_directories(${Boost_LIBRARY_DIRS})
```


### 使用第三方库

假设你想在项目中使用 Boost 库，CMakeLists.txt 文件可能如下所示：


## 实例


```
cmake_minimum_required(VERSION 3.10)
project(MyProject CXX)

# 查找 Boost 库
find_package(Boost REQUIRED)

# 添加源文件
add_executable(MyExecutable main.cpp)

# 链接 Boost 库
target_link_libraries(MyExecutable Boost::Boost)
```


### include_directories() 和 target_include_directories()

在 CMake 中，include_directories() 和 target_include_directories() 都用于指定头文件的搜索路径，但它们的作用范围和使用方式有显著区别。


**相同点：**


- 两者都用于添加头文件的搜索路径，编译器会在这些路径中查找 #include 指令中指定的头文件。
- 两者都支持绝对路径和相对路径，相对路径是相对于当前 CMakeLists.txt 文件所在的目录。
- 两者都可以用于指定公共头文件路径（PUBLIC）、私有头文件路径（PRIVATE）或接口头文件路径（INTERFACE）。


**区别：**


| 特性 | include_directories() | target_include_directories() |
| --- | --- | --- |
| 作用范围 | 全局作用域，影响所有目标（target）。 | 仅作用于指定的目标（target）。 |
| 推荐使用场景 | 适用于简单的项目或旧版 CMake 项目。 | 适用于现代 CMake 项目，推荐优先使用。 |
| 目标关联性 | 不直接关联到特定目标，可能影响所有目标。 | 显式关联到特定目标，避免污染其他目标。 |
| 可维护性 | 较差，容易导致全局路径污染。 | 较好，路径与目标绑定，逻辑清晰。 |
| 作用域控制 | 无法精确控制路径的作用范围。 | 可以通过 PUBLIC、PRIVATE、INTERFACE 精确控制路径的作用范围。 |
| 现代 CMake 推荐 | 不推荐使用，除非有特殊需求。 | 推荐使用，符合现代 CMake 的最佳实践。 |









	  AI 思考中...





			** [CMake 安装与配置](https://www.runoob.com/cmake-install-setup.html)
			[CMake 构建流程](https://www.runoob.com/cmake-build-flow.html) **













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