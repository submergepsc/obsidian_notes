# 第一个 Flutter 应用

- Source: https://www.runoob.com/flutter/flutter-create-app.html

本节将介绍如何使用 Flutter CLI 创建新的 Flutter 项目，运行应用，并理解最基础的代码结构。


---


## 使用 Flutter CLI 创建项目


Flutter CLI 是 Flutter 的命令行工具，用于创建、管理和构建 Flutter 项目。


### 创建新项目


在终端中运行以下命令创建一个新的 Flutter 项目：


```
$ flutter create my_first_app
```


其中 `my_first_app` 是你的项目名称。Flutter 会根据这个名称创建对应的文件夹和文件。


**
项目名称必须使用小写字母和下划线，不能包含空格或特殊字符。


### 命令参数


`flutter create` 命令支持多种参数：


| 参数 | 说明 | 示例 |
| --- | --- | --- |
| --org | 指定组织标识符（反向域名格式） | --org com.example |
| --platforms | 指定支持的平台 | --platforms ios,android |
| --empty | 使用最小模板创建项目 | --empty |


```
$ flutter create hello_world
Creating project "hello_world"...
  .gitignore                    2026-04-01 10:30:22
  .metadata                     2026-04-01 10:30:22
  analysis_options.yaml         2026-04-01 10:01:15
  pubspec.yaml                  2026-04-01 10:30:22
  README.md                     2026-04-01 10:30:22
  lib/
    main.dart                    2026-04-01 10:30:22
  test/
    widget_test.dart             2026-04-01 10:22:34
  android/
  ios/
  web/
  ...
Running "flutter pub get"...                     13.2s
Running "flutter analyze"...                     3.2s
```


---


## 运行 Flutter 应用


### 启动开发服务器


项目创建完成后，进入项目目录并运行应用：


```
$ cd hello_world
$ flutter run
```


首次运行可能会花费一些时间，因为 Flutter 需要编译 Dart 代码并启动应用。


### 指定运行设备


如果你的电脑连接了多个设备（或模拟器），可以使用 `-d` 参数指定运行设备：


| 设备 | 命令 |
| --- | --- |
| Android 模拟器 | flutter run -d android |
| iOS 模拟器 | flutter run -d iphone |
| Chrome 浏览器 | flutter run -d chrome |
| Windows 桌面 | flutter run -d windows |


### 查看可用设备


运行以下命令查看所有可用的运行设备：


```
$ flutter devices
```


输出示例：


```
2 connected devices:
Chrome (web)      • chrome           • web-javascript • Chrome  • web
Windows (windows) • windows          • windows        • x64    • Windows 10.0.0
```


---


## 热重载功能


Flutter 最强大的功能之一是热重载（Hot Reload）。当你正在运行应用时：


- 修改代码并保存
- 在终端中按 `r` 键
- 应用会重新加载，你能看到最新的更改


热重载非常快，通常只需要一两秒钟。这极大地提高了开发效率，让你可以实时预览界面效果。


> 热重载不会丢失应用状态，这意味着你可以在不重启应用的情况下快速迭代 UI 设计。


---


## main.dart 文件解析 每个 Flutter 项目都有一个入口文件 lib/main.dart。让我们看看默认生成的内容： 实例：main.dart 代码


```
// lib/main.dart
// Flutter 应用的入口文件

// 引入 Material Design 组件库
import 'package:flutter/material.dart';

// 应用入口函数
void main() {
  // runApp 是 Flutter 的启动函数
  // 它接收一个 Widget 作为根 widget
  runApp(const MyApp());
}

// 根 Widget（无状态组件）
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    // MaterialApp 是 Material Design 风格的根组件
    return MaterialApp(
      // 设置应用标题
      title: 'Flutter Demo',
      // 设置主题颜色
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        // 使用 Material 3
        useMaterial3: true,
      ),
      // 应用的主页面
      home: const MyHomePage(title: 'Flutter 首页'),
    );
  }
}

// 有状态组件（可以有内部状态）
class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // 页面标题（不可变）
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  // 计数器状态
  int _counter = 0;

  // 增加计数器的方法
  void _incrementCounter() {
    // setState 通知 Flutter 状态已更改，需要重新构建 UI
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // Scaffold 是 Material Design 的页面脚手架
    return Scaffold(
      // AppBar 是顶部应用栏
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        // 显示页面标题
        title: Text(widget.title),
      ),
      // 页面主体内容
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('你点击了按钮多少次：'),
            // 显示计数器值
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      // 悬浮按钮
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: '增加',
        child: const Icon(Icons.add),
      ),
    );
  }
}
```


### 代码结构说明


| 部分 | 说明 |
| --- | --- |
| import 语句 | 引入所需的包，这里引入了 Material Design 组件库 |
| main 函数 | Dart 程序的入口点，调用 runApp 启动应用 |
| runApp 函数 | Flutter 的启动函数，接收根 Widget 作为参数 |
| StatelessWidget | 无状态组件，UI 不随时间变化 |
| StatefulWidget | 有状态组件，UI 可以响应数据变化 |
| build 方法 | 每个 Widget 必须实现的方法，用于构建 UI |









	  AI 思考中...





			** [Flutter 安装](https://www.runoob.com/flutter-install.html)
			[Flutter 项目结构](https://www.runoob.com/flutter-project-structure.html) **













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