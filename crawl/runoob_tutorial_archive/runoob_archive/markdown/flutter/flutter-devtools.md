# Flutter 调试与 DevTools

- Source: https://www.runoob.com/flutter/flutter-devtools.html

本节将介绍 Flutter 的调试工具和常用调试技巧。


---


## Flutter DevTools 简介


Flutter DevTools 是一套用于调试和分析 Flutter 应用的工具集。


### 启动 DevTools


```
$ flutter run
```


在运行应用后，终端会显示 DevTools 的 URL，通常是 `http://127.0.0.1:9100`


### 常用命令


| 命令 | 说明 |
| --- | --- |
| flutter doctor | 检查开发环境配置 |
| flutter analyze | 静态代码分析 |
| flutter test | 运行测试 |


---


## print 和 debugPrint


## 实例：基本调试输出


```
// 基础打印
print('Hello Debug');  // 输出到控制台

// debugPrint 避免长文本截断
debugPrint('这是一段很长的文本，可以完整输出而不会被截断');

// 条件打印
if (debugMode) {
  print('调试信息');
}

// 打印对象（需要 toString）
final user = {'name': '张三', 'age': 25};
print('用户信息: $user');  // 输出: 用户信息: {name: 张三, age: 25}
```


---


## 断言 - assert


断言用于在开发时检查条件，仅在调试模式下生效。


实例：使用断言


```
// 简单的断言
assert(user != null, '用户不能为空');

// 函数参数验证
void setAge(int age) {
  // 年龄必须大于 0
  assert(age > 0, '年龄必须大于 0');
  this.age = age;
}

// UI 构建中的断言（仅开发时）
Widget build(BuildContext context) {
  // 确保 context 不为 null
  assert(context != null);
  // 确保有父级 Scaffold
  assert(debugCheckHasMaterial(context));
  return Scaffold(...);
}
```


---


## 断点调试


在 VS Code 或 Android Studio 中设置断点进行调试。


### VS Code 调试


- 在代码行号左侧点击设置断点
- 按 F5 或点击调试按钮启动调试
- 使用调试工具栏控制程序执行


### 常用断点命令


| 操作 | 说明 |
| --- | --- |
| Continue / F5 | 继续执行到下一个断点 |
| Step Over / F10 | 单步执行，不进入函数 |
| Step Into / F11 | 单步执行，进入函数 |
| Step Out / Shift+F11 | 跳出当前函数 |


---


## Flutter Inspector


Flutter Inspector 是 DevTools 的一部分，用于可视化和检查 Widget 树。


### 主要功能


- **Widget Tree**: 查看 Widget 层级结构
- **Layout Explorer**: 检查布局约束
- **Performance Overlay**: 显示性能指标


---


## 常见问题调试


## 实例：调试 UI 不更新


```
// 问题：UI 不更新
// 原因：修改状态后没有调用 setState

// 错误示例
void _increment() {
  _counter++;  // 状态已改变，但 UI 不会更新！
}

// 正确示例
void _increment() {
  setState(() {
    _counter++;  // 必须调用 setState
  });
}

// 问题：状态管理混乱
// 建议：使用 Provider 或其他状态管理方案
```


**

调试时常用工具：print 输出日志、Inspector 检查 Widget 树、Timeline 分析性能。










	  AI 思考中...





			** [Flutter 图片与资源](https://www.runoob.com/flutter-images.html)
			[Flutter 平台特定代码](https://www.runoob.com/flutter-platform-channels.html) **













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