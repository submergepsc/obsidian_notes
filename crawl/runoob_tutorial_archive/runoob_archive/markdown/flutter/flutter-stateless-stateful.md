# Flutter StatelessWidget vs StatefulWidget 深入理解

- Source: https://www.runoob.com/flutter/flutter-stateless-stateful.html

理解 StatelessWidget 和 StatefulWidget 的区别是 Flutter 开发的基础。

本节将深入分析这两种 Widget 的使用场景和内部工作机制。


---


## 核心区别


Flutter 中有两种主要类型的 Widget，它们的根本区别在于是否能持有可变状态。


| 特性 | StatelessWidget | StatefulWidget |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 状态 | 不可变（immutable） | 可变（mutable） |  |  |  |
| 重建时机 | 仅在父 Widget 重建时 | 状态变化时 + 父 Widget 重建 |  |  |  |
| 性能 | 更高（无需监听状态） | 略低（需要状态管理） | 使用场景 | 静态内容 | 动态交互内容 |


---


## StatelessWidget 详解


StatelessWidget 适合用于不随时间变化的内容。一旦创建，其所有属性都是 final 的，不可修改。


### 使用场景


- 显示静态文本、图片、图标
- 展示数据列表（数据源来自父 Widget）
- 不包含用户交互的布局容器
- 表单中的只读展示部分


## 实例：StatelessWidget 完整示例


```
import 'package:flutter/material.dart';

// 用户信息展示组件（无状态）
class UserCard extends StatelessWidget {
  // 属性定义为 final，确保不可变
  final String name;
  final String email;
  final String avatarUrl;

  // const 构造函数提高性能
  const UserCard({
    super.key,
    required this.name,
    required this.email,
    this.avatarUrl = '',
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Row(
          children: [
            // 头像
            CircleAvatar(
              backgroundImage: avatarUrl.isNotEmpty
                  ? NetworkImage(avatarUrl)
                  : null,
              child: avatarUrl.isEmpty
                  ? const Icon(Icons.person)
                  : null,
            ),
            const SizedBox(width: 16),
            // 用户信息
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    name,
                    style: const TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    email,
                    style: TextStyle(
                      color: Colors.grey[600],
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```


---


## StatefulWidget 详解


StatefulWidget 适合用于需要响应用户交互或数据变化的场景。它由两部分组成：Widget 本身（不可变）和 State 对象（可变）。


### 使用场景


- 计数器、计时器等动态数据
- 表单输入
- 动画控制
- 网络请求状态展示
- 用户交互响应


### State 对象生命周期


| 方法 | 说明 |
| --- | --- |
| initState | Widget 首次创建时调用，用于初始化状态 |
| didChangeDependencies | Widget 的依赖变化时调用 |
| build | 构建 UI，每次状态变化都会调用 |
| didUpdateWidget | 父 Widget 重建时调用 |
| dispose | Widget 被移除时调用，用于清理资源 |


## 实例：StatefulWidget 完整示例


```
import 'package:flutter/material.dart';

// 计数器应用
class CounterApp extends StatefulWidget {
  const CounterApp({super.key});

  @override
  State<CounterApp> createState() => _CounterAppState();
}

class _CounterAppState extends State<CounterApp> {
  // 计数器状态
  int _counter = 0;
  // 计时器（用于演示 dispose）
  Timer? _timer;

  // 1. initState - 初始化状态
  @override
  void initState() {
    super.initState();
    // 初始化计数器
    _counter = 0;
    // 启动一个定时器（每秒增加一次）
    _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
      _increment();
    });
  }

  // 2. didChangeDependencies - 依赖变化时调用
  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
  }

  // 3. build - 构建 UI
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('计数器'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              '当前计数：',
              style: TextStyle(fontSize: 20),
            ),
            Text(
              '$_counter',
              style: const TextStyle(
                fontSize: 48,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
      ),
      // 增加按钮
      floatingActionButton: FloatingActionButton(
        onPressed: _increment,
        child: const Icon(Icons.add),
      ),
    );
  }

  // 增加计数器的方法
  void _increment() {
    // 必须调用 setState 来触发 UI 更新
    setState(() {
      _counter++;
    });
  }

  // 4. didUpdateWidget - 父 Widget 重建时调用
  @override
  void didUpdateWidget(CounterApp oldWidget) {
    super.didUpdateWidget(oldWidget);
  }

  // 5. dispose - 清理资源
  @override
  void dispose() {
    // 取消定时器，防止内存泄漏
    _timer?.cancel();
    super.dispose();
  }
}
```


---


## setState 的正确使用


在 StatefulWidget 中，必须通过 setState 来通知 Flutter 状态已更改。


### 正确用法


## 实例：正确的 setState 用法


```
// 正确：在 setState 中更新状态
void _increment() {
  setState(() {
    _counter++;
  });
}

// 正确：状态更新与 UI 无关时可以不用 setState
void _someInternalLogic() {
  // 内部逻辑，不影响 UI
  _calculateSomething();
}

// 正确：异步操作后更新状态
Future<void> _loadData() async {
  final data = await fetchData();
  setState(() {
    _items = data;
  });
}
```


### 错误用法


## 实例：错误的 setState 用法


```
// 错误：修改状态但不调用 setState
void _increment() {
  _counter++;  // 状态已改变，但 UI 不会更新！
}

// 错误：在 build 方法中调用 setState
@override
Widget build(BuildContext context) {
  // 永远不要在 build 中调用 setState！
  setState(() {
    _counter++;  // 这会导致无限循环
  });
  return Text('$_counter');
}
```


**

setState 会在下一次帧绘制时触发 build 方法的重新调用。


频繁调用 setState 或在 build 方法中调用 setState 都可能导致性能问题。


---


## 如何选择


在开发时，应该根据实际需求选择合适的 Widget 类型：


### 选择 StatelessWidget 当


- Widget 的外观不依赖于任何可变状态
- 所有需要的数据都通过构造函数从父 Widget 传入
- Widget 不需要响应用户交互
- 追求最佳性能


### 选择 StatefulWidget 当


- Widget 需要维护内部状态
- 需要响应用户输入（点击、滑动等）
- 需要响应数据变化（如网络请求返回）
- 需要控制动画










	  AI 思考中...





			** [Flutter Widget 基础](https://www.runoob.com/flutter-widget-basics.html)
			[Flutter 布局基础](https://www.runoob.com/flutter-layout.html) **













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