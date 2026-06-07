# Flutter 平台特定代码

- Source: https://www.runoob.com/flutter/flutter-platform-channels.html

本节将介绍如何使用平台通道（Platform Channels）在 Flutter 中调用原生平台代码。


---


## 平台通道概述


平台通道允许 Dart 代码与原生平台（iOS/Android）进行通信。


| 类型 | 说明 |
| --- | --- |
| MethodChannel | 方法通道，用于调用平台方法 |
| EventChannel | 事件通道，用于流式数据 |


---


## Dart 端调用


## 实例：MethodChannel 用法


```
import 'package:flutter/services.dart';

// 定义通道
class PlatformChannel {
  static const MethodChannel _channel = MethodChannel('my_app/channel');

  // 调用原生方法 - 获取电池电量
  static Future<int> getBatteryLevel() async {
    try {
      final int batteryLevel = await _channel.invokeMethod('getBatteryLevel');
      return batteryLevel;
    } on PlatformException catch (e) {
      print('获取电池电量失败: ${e.message}');
      return -1;
    }
  }

  // 调用原生方法 - 显示Toast
  static Future<void> showToast(String message) async {
    try {
      await _channel.invokeMethod('showToast', {'message': message});
    } on PlatformException catch (e) {
      print('显示Toast失败: ${e.message}');
    }
  }

  // 调用原生方法 - 获取设备信息
  static Future<Map<String, dynamic>> getDeviceInfo() async {
    try {
      final result = await _channel.invokeMapMethod('getDeviceInfo');
      return result ?? {};
    } on PlatformException catch (e) {
      print('获取设备信息失败: ${e.message}');
      return {};
    }
  }
}

// 使用示例
class MyWidget extends StatelessWidget {
  const MyWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () async {
        final battery = await PlatformChannel.getBatteryLevel();
        print('电池电量: $battery%');
      },
      child: const Text('获取电池电量'),
    );
  }
}
```


---


## Android 端实现（Kotlin）


## 实例：Android 端代码


```
// MainActivity.kt
package com.example.my_app

import android.os.Bundle
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel

class MainActivity : FlutterActivity() {
    private val CHANNEL = "my_app/channel"

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)

        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL)
            .setMethodCallHandler { call, result ->
                when (call.method) {
                    "getBatteryLevel" -> {
                        val batteryLevel = getBatteryLevel()
                        if (batteryLevel != -1) {
                            result.success(batteryLevel)
                        } else {
                            result.error("UNAVAILABLE", "无法获取电池电量", null)
                        }
                    }
                    "showToast" -> {
                        val message = call.argument<String>("message")
                        showToast(message!!)
                        result.success(null)
                    }
                    else -> {
                        result.notImplemented()
                    }
                }
            }
    }

    private fun getBatteryLevel(): Int {
        return try {
            val batteryManager = getSystemService(BATTERY_SERVICE) as BatteryManager
            batteryManager.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
        } catch (e: Exception) {
            -1
        }
    }

    private fun showToast(message: String) {
        android.widget.Toast.makeText(this, message, android.widget.Toast.LENGTH_SHORT).show()
    }
}
```


---


## iOS 端实现（Swift）


## 实例：iOS 端代码


```
// AppDelegate.swift
import Flutter
import UIKit

@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
    private let CHANNEL = "my_app/channel"

    override func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        let controller = window?.rootViewController as! FlutterViewController

        let channel = FlutterMethodChannel(
            name: CHANNEL,
            binaryMessenger: controller.binaryMessenger
        )

        channel.setMethodCallHandler { (call: FlutterMethodCall, result: @escaping FlutterResult) in
            switch call.method {
            case "getBatteryLevel":
                self.getBatteryLevel(result: result)
            case "showToast":
                if let args = call.arguments as? [String: Any],
                   let message = args["message"] as? String {
                    self.showToast(message: message)
                    result(nil)
                }
            default:
                result(FlutterMethodNotImplemented)
            }
        }

        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }

    private func getBatteryLevel(result: @escaping FlutterResult) {
        UIDevice.current.isBatteryMonitoringEnabled = true
        let batteryLevel = UIDevice.current.batteryLevel

        if batteryLevel < 0 {
            result(FlutterError(code: "UNAVAILABLE", message: "无法获取电池电量", details: nil))
        } else {
            result(Int(batteryLevel * 100))
        }
    }

    private func showToast(message: String) {
        let alert = UIAlertController(title: nil, message: message, preferredStyle: .alert)
        present(alert, animated: true)
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
            alert.dismiss(animated: true)
        }
    }
}
```


**

平台通道是 Flutter 与原生代码通信的主要方式，常用于调用系统 API、硬件功能或使用第三方原生 SDK。










	  AI 思考中...





			** [Flutter 调试与 DevTools](https://www.runoob.com/flutter-devtools.html)
			[Flutter 测试](https://www.runoob.com/flutter-test.html) **













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