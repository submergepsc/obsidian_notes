# Flutter 项目结构

- Source: https://www.runoob.com/flutter/flutter-project-structure.html

了解 Flutter 项目的目录结构对于高效开发至关重要。

本节将详细介绍 Flutter 项目的各个组成部分及其作用。


---


## 项目目录结构


当你使用 `flutter create` 创建新项目后，会得到以下目录结构：


```
my_app/
├── android/          # Android 平台相关代码
├── ios/              # iOS 平台相关代码
├── lib/              # Dart 代码目录（主要开发目录）
│   └── main.dart     # 应用入口文件
├── web/              # Web 平台相关代码
├── windows/          # Windows 桌面相关代码
├── macos/            # macOS 桌面相关代码
├── linux/            # Linux 桌面相关代码
├── test/             # 测试代码目录
├── pubspec.yaml      # 项目配置文件
├── pubspec.lock      # 依赖锁定文件（自动生成）
├── analysis_options.yaml  # Dart 分析器配置
└── README.md         # 项目说明文件
```


---


## 主要目录和文件说明


### lib/ 目录 - 核心代码目录


`lib/` 目录是你编写 Dart 代码的主要地方。所有应用逻辑都应该放在这里。


| 文件/目录 | 说明 |
| --- | --- |
| main.dart | 应用的入口文件，包含 main 函数和根 Widget |
| *.dart | 其他 Dart 源文件，通常按功能模块组织 |


### android/ 目录 - Android 平台


包含 Android 原生项目文件，用于：


- 配置应用名称和图标
- 设置应用权限
- 集成原生 SDK（如 Google Play 服务）


### ios/ 目录 - iOS 平台


包含 iOS 原生项目文件（Xcode 项目），用于：


- 配置应用名称和图标
- 设置 iOS 特有的配置
- 集成 CocoaPods 依赖


### test/ 目录 - 测试代码


包含应用的测试代码，通常包括：


- 单元测试
- Widget 测试
- 集成测试


### pubspec.yaml - 项目配置


`pubspec.yaml` 是 Flutter 项目的核心配置文件，定义项目名称、版本、依赖等。


## 实例：pubspec.yaml 示例


```
# 项目名称
name: my_app
# 项目版本
version: 1.0.0+1

# 项目描述
description: "我的第一个 Flutter 应用"

# 运行环境
environment:
  sdk: ^3.0.0

# 项目依赖
dependencies:
  flutter:
    sdk: flutter

  # 添加第三方依赖
  http: ^1.0.0
  provider: ^6.0.0

# 开发依赖（仅在开发时使用）
dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0

# Flutter 配置
flutter:
  uses-material-design: true

  # 配置资源文件
  assets:
    - images/
    - assets/data.json
```


### pubspec.yaml 常用字段


| 字段 | 说明 |
| --- | --- |
| name | 项目名称，必须使用小写字母和下划线 |
| version | 项目版本号，格式为 x.y.z |
| description | 项目描述文本 |
| dependencies | 运行时依赖的包 |
| dev_dependencies | 开发时依赖的包（如测试工具） |
| flutter.assets | 需要打包的资源文件 |


---


## 依赖管理


### 添加依赖


使用 `flutter pub add` 命令添加依赖：


```
$ flutter pub add http
```


或者手动编辑 `pubspec.yaml` 后运行：


```
$ flutter pub get
```


### 常用依赖命令


| 命令 | 说明 |
| --- | --- |
| flutter pub get | 获取所有依赖 |
| flutter pub add package | 添加依赖 |
| flutter pub remove package | 移除依赖 |
| flutter pub outdated | 检查过时的依赖 |
| flutter pub upgrade | 升级依赖到最新版本 |


---


## 推荐的项目结构


随着应用规模增大，建议采用清晰的项目结构：


```
lib/
├── main.dart              # 入口文件
├── app.dart               # 应用配置
├── core/                  # 核心功能
│   ├── constants/         # 常量定义
│   ├── theme/             # 主题配置
│   └── utils/             # 工具类
├── data/                  # 数据层
│   ├── models/            # 数据模型
│   ├── repositories/     # 仓库（数据接口）
│   └── services/          # 网络服务
├── domain/                # 领域层
│   └── entities/          # 实体类
├── presentation/          # 展示层
│   ├── pages/             # 页面
│   ├── widgets/           # 组件
│   └── providers/         # 状态管理
└── routes/                # 路由配置
```


**
良好的项目结构可以提高代码可维护性，建议根据应用规模选择合适的结构。









	  AI 思考中...





			** [第一个 Flutter 应用](https://www.runoob.com/flutter-create-app.html)
			[Flutter Widget 基础](https://www.runoob.com/flutter-widget-basics.html) **













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