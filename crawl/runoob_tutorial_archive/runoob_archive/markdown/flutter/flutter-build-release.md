# Flutter 打包与发布

- Source: https://www.runoob.com/flutter/flutter-build-release.html

本节将介绍如何将 Flutter 应用打包发布到各个平台。


---


## 构建准备


在发布前，确保应用配置正确。


### pubspec.yaml 配置


## 实例：发布配置


```
# 应用信息
name: my_app
description: "我的 Flutter 应用"
version: 1.0.0+1  # 版本号（重要！）

# 应用图标
flutter:
  uses-material-design: true
  # 生成图标需要 flutter pub run flutter_launcher_icons
```


### Android 配置


修改 android/app/build.gradle 中的应用配置：


## 实例：Android 配置


```
// android/app/build.gradle

android {
    namespace "com.example.myapp"
    compileSdk = 34

    defaultConfig {
        applicationId "com.example.myapp"  // 应用 ID
        minSdk = 21                          // 最低 Android 版本
        targetSdk = 34                       // 目标版本
        versionCode 1                        // 版本代码（每次发布递增）
        versionName "1.0.0"                  // 版本名称
    }

    signingConfigs {
        release {
            // 发布签名配置
            storeFile file("key.jks")
            storePassword "密码"
            keyAlias "别名"
            keyPassword "密钥密码"
        }
    }
}
```


---


## Android 构建


### 构建 APK


```
# 调试 APK
$ flutter build apk --debug

# 发布 APK
$ flutter build apk --release

# 带签名（需要配置 signingConfigs）
$ flutter build apk --release --target-platform android-arm64
```


### 构建 App Bundle


```
# 构建 App Bundle（推荐用于 Google Play）
$ flutter build appbundle --release
```


---


## iOS 构建


### 准备工作


- 安装 Xcode
- 配置 Apple 开发者账号
- 创建 App ID 和证书


### 命令行构建


```
# 模拟器版本
$ flutter build ios --simulator --no-codesign

# 发布版本（需要签名）
$ flutter build ipa --release
```


### 使用 Xcode 构建


- 在 ios/ 目录打开 .xcworkspace 文件
- 选择目标设备和 Signing 配置
- 点击 Product > Archive


---


## Web 构建


```
# 构建 Web 版本
$ flutter build web --release

# 输出目录：build/web/
```


### Web 配置


在 web/index.html 中配置应用：


## 实例：Web 配置


```
<!DOCTYPE html>
<html>
<head>
  <base href="/">
  <title>我的应用</title>
  <meta name="description" content="Flutter 应用">
  <!-- PWA 支持 -->
  <link rel="manifest" href="manifest.json">
</head>
<body>
  <script src="flutter.js" defer></script>
</body>
</html>
```


---


## 桌面应用构建


```
# Windows
$ flutter build windows --release

# macOS
$ flutter build macos --release

# Linux
$ flutter build linux --release
```


**

发布前务必测试应用的发布版本，调试版本可能包含额外的调试信息。










	  AI 思考中...





			** [Flutter 测试](https://www.runoob.com/flutter-test.html)
			[Flutter 最佳实践](https://www.runoob.com/flutter-best-practices.html) **













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