# CMake 实战练习

- Source: https://www.runoob.com/cmake/cmake-exercises.html

本文将演示如何使用 CMake 管理一个中等复杂度的项目，从创建项目到编译和运行的整个过程，涵盖了从基本配置到高级特性的实际应用。


实战内容如下：


- **创建 `CMakeLists.txt` 文件**：定义项目、库、可执行文件和测试。
- **编写源代码和测试**：编写代码和测试文件。
- **创建构建目录**：保持源代码目录整洁。
- **配置项目**：生成构建系统文件。
- **编译项目**：生成目标文件。
- **运行可执行文件**：执行程序。
- **运行测试**：验证功能正确性。
- **使用自定义命令和目标**：执行额外操作。
- **跨平台和交叉编译**：支持不同平台和架构。


### 构建一个简单的 C++ 项目

假设我们有一个项目，包含一个主程序和一个库，库中有两个不同的功能模块。

项目结构如下：


```
MyProject/
├── CMakeLists.txt
├── src/
│   ├── main.cpp
│   ├── lib/
│   │   ├── module1.cpp
│   │   ├── module2.cpp
│   ├── include/
│       └── mylib.h
└── tests/
    ├── test_main.cpp
    └── CMakeLists.txt
```


---


## 1、创建 CMakeLists.txt 文件


### 1.1 根目录 CMakeLists.txt 文件

在 MyProject 根目录下创建一个 CMakeLists.txt 文件：


## 实例


```
cmake_minimum_required(VERSION 3.10)   # 指定最低 CMake 版本
project(MyProject VERSION 1.0)          # 定义项目名称和版本

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 包含头文件路径
include_directories(${PROJECT_SOURCE_DIR}/src/include)

# 添加子目录
add_subdirectory(src)
add_subdirectory(tests)
```


### 1.2 src 目录 CMakeLists.txt 文件

在 src 目录下创建一个 CMakeLists.txt 文件：


## 实例


```
# 创建库目标
add_library(MyLib STATIC
    lib/module1.cpp
    lib/module2.cpp
)

# 指定库的头文件
target_include_directories(MyLib PUBLIC ${CMAKE_SOURCE_DIR}/src/include)

# 创建可执行文件目标
add_executable(MyExecutable main.cpp)

# 链接库到可执行文件
target_link_libraries(MyExecutable PRIVATE MyLib)
```


### 1.3 tests 目录 CMakeLists.txt 文件

在 tests 目录下创建一个 CMakeLists.txt 文件：


## 实例


```
# 查找 GTest 包
find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})

# 创建测试目标
add_executable(TestMyLib test_main.cpp)

# 链接库和 GTest 到测试目标
target_link_libraries(TestMyLib PRIVATE MyLib ${GTEST_LIBRARIES})
```


---


## 2、编写源代码和测试

以下是各个文件的代码：


### 2.1 src/main.cpp 文件代码


## 实例


```
#include <iostream>
#include "mylib.h"

int main() {
    std::cout << "Hello, CMake!" << std::endl;
    return 0;
}
```


### 2.2 src/lib/module1.cpp 文件代码


## 实例


```
#include "mylib.h"

// Implementation of module1
```


### 2.3 src/lib/module2.cpp 文件代码


## 实例


```
#include "mylib.h"

// Implementation of module2
```


### 2.4 src/include/mylib.h 文件代码


## 实例


```
#ifndef MYLIB_H
#define MYLIB_H

// Declarations of module functions

#endif // MYLIB_H
```


### 2.5 tests/test_main.cpp 文件代码


## 实例


```
#include <gtest/gtest.h>

// Test cases for MyLib
TEST(MyLibTest, BasicTest) {
    EXPECT_EQ(1, 1);
}
```


---


## 3、创建构建目录

在项目根目录下创建一个构建目录：


```
mkdir build
cd build
```


---


## 4、配置项目

在构建目录中运行 CMake 以配置项目：


```
cmake ..
```


---


## 5、编译项目

使用生成的构建系统文件进行编译，假设生成了 Makefile：


```
make
```


---


## 6、运行可执行文件

编译完成后，可以运行生成的可执行文件：


```
./MyExecutable
```


---


## 7、运行测试

使用生成的测试目标进行测试：


```
./TestMyLib
```


---

## 8、使用自定义命令和目标


### 8.1 自定义命令

在 src/CMakeLists.txt 文件中添加自定义命令：


```
add_custom_command(
    TARGET MyExecutable
    POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E echo "Build complete!"
)
```


### 8.2 自定义目标

在 src/CMakeLists.txt 文件中添加自定义目标：


```
add_custom_target(run
    COMMAND ${CMAKE_BINARY_DIR}/MyExecutable
    DEPENDS MyExecutable
)
```


运行自定义目标：


```
make run
```


---

## 9、跨平台和交叉编译


### 9.1 指定平台

如果需要指定平台进行构建，可以在运行 CMake 时指定平台：


```
cmake -DCMAKE_SYSTEM_NAME=Linux ..
```


### 9.2 使用工具链文件

创建一个工具链文件 toolchain.cmake：


```
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)
```


使用工具链文件进行构建：


```
cmake -DCMAKE_TOOLCHAIN_FILE=toolchain.cmake ..
```









	  AI 思考中...





			** [CMake 高级特性](https://www.runoob.com/cmake-advanced-features.html)














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