# Flutter 测试

- Source: https://www.runoob.com/flutter/flutter-test.html

本节将介绍 Flutter 中的三种测试类型：单元测试、Widget 测试和集成测试。


---


## 测试类型概述


| 类型 | 说明 | 运行命令 |
| --- | --- | --- |
| 单元测试 | 测试单个函数、类的方法 | flutter test |
| Widget 测试 | 测试单个 Widget 的 UI | flutter test |
| 集成测试 | 测试完整的应用流程 | flutter test integration_test/ |


---


## 单元测试


单元测试用于测试业务逻辑代码。


## 实例：单元测试示例


```
// math_utils.dart - 待测试的代码
class MathUtils {
  static int add(int a, int b) => a + b;
  static int subtract(int a, int b) => a - b;
  static int multiply(int a, int b) => a * b;
  static double divide(int a, int b) {
    if (b == 0) throw ArgumentError('不能除以零');
    return a / b;
  }

  static int factorial(int n) {
    if (n < 0) throw ArgumentError('负数没有阶乘');
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
  }
}

// math_utils_test.dart - 测试文件
import 'package:flutter_test/flutter_test.dart';
import 'package:my_app/math_utils.dart';

void main() {
  group('MathUtils', () {
    test('add 两个数相加', () {
      expect(MathUtils.add(2, 3), equals(5));
    });

    test('subtract 两个数相减', () {
      expect(MathUtils.subtract(5, 3), equals(2));
    });

    test('multiply 两个数相乘', () {
      expect(MathUtils.multiply(4, 5), equals(20));
    });

    test('divide 两个数相除', () {
      expect(MathUtils.divide(10, 2), equals(5));
    });

    test('divide 除以零抛出异常', () {
      expect(() => MathUtils.divide(10, 0), throwsArgumentError);
    });

    test('factorial 计算阶乘', () {
      expect(MathUtils.factorial(5), equals(120));
      expect(MathUtils.factorial(0), equals(1));
    });

    test('factorial 负数抛出异常', () {
      expect(() => MathUtils.factorial(-1), throwsArgumentError);
    });
  });
}
```


---


## Widget 测试


Widget 测试用于测试 UI 组件。


## 实例：Widget 测试


```
// counter_widget.dart - 待测试的 Widget
class CounterWidget extends StatefulWidget {
  const CounterWidget({super.key});

  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  int _count = 0;

  void _increment() {
    setState(() {
      _count++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text('计数: $_count', key: const Key('counter_text')),
        ElevatedButton(
          key: const Key('increment_button'),
          onPressed: _increment,
          child: const Text('增加'),
        ),
      ],
    );
  }
}

// counter_widget_test.dart - 测试文件
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:my_app/counter_widget.dart';

void main() {
  testWidgets('CounterWidget 显示初始计数', (WidgetTester tester) async {
    // 构建 Widget
    await tester.pumpWidget(const MaterialApp(
      home: CounterWidget(),
    ));

    // 验证初始计数显示
    expect(find.text('计数: 0'), findsOneWidget);
  });

  testWidgets('CounterWidget 点击按钮增加计数', (WidgetTester tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: CounterWidget(),
    ));

    // 找到并点击按钮
    await tester.tap(find.byKey(const Key('increment_button')));
    await tester.pump();

    // 验证计数已更新
    expect(find.text('计数: 1'), findsOneWidget);

    // 再次点击
    await tester.tap(find.byKey(const Key('increment_button')));
    await tester.pump();

    expect(find.text('计数: 2'), findsOneWidget);
  });
}
```


---


## 集成测试


集成测试用于测试完整的应用功能流程。


## 实例：集成测试


```
// integration_test/app_test.dart
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:my_app/main.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  group('应用集成测试', () {
    testWidgets('完整用户流程测试', (WidgetTester tester) async {
      // 启动应用
      await tester.pumpWidget(const MyApp());
      await tester.pumpAndSettle();

      // 验证首页显示
      expect(find.text('首页'), findsOneWidget);

      // 点击跳转到详情页
      await tester.tap(find.text('详情'));
      await tester.pumpAndSettle();

      // 验证详情页显示
      expect(find.text('详情页'), findsOneWidget);

      // 点击返回
      await tester.tap(find.byIcon(Icons.arrow_back));
      await tester.pumpAndSettle();

      // 验证回到首页
      expect(find.text('首页'), findsOneWidget);
    });
  });
}
```


**

良好的测试覆盖可以提高代码质量，建议至少对核心业务逻辑编写单元测试。










	  AI 思考中...





			** [Flutter 平台特定代码](https://www.runoob.com/flutter-platform-channels.html)
			[Flutter 打包与发布](https://www.runoob.com/flutter-build-release.html) **













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