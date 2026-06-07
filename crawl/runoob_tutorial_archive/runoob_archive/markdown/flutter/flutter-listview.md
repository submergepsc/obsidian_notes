# Flutter ListView 与滚动

- Source: https://www.runoob.com/flutter/flutter-listview.html

ListView 是 Flutter 中最常用的滚动列表 Widget，用于显示可滚动的内容列表。


---


## ListView 基本用法


## 实例：ListView 基本用法


```
// 方式1：children 参数（适用于少量项目）
ListView(
  children: [
    ListTile(title: Text('第一项')),
    ListTile(title: Text('第二项')),
    ListTile(title: Text('第三项')),
  ],
)

// 方式2：ListView.builder（适用于大量或无限列表）
ListView.builder(
  itemCount: 100,
  itemBuilder: (context, index) {
    return ListTile(title: Text('第 ${index + 1} 项'));
  },
)

// 方式3：ListView.separated（带分隔符）
ListView.separated(
  itemCount: 10,
  separatorBuilder: (context, index) => const Divider(),  // 分隔线
  itemBuilder: (context, index) {
    return ListTile(title: Text('第 ${index + 1} 项'));
  },
)
```


---


## ListView 常用属性


| 属性 | 说明 |
| --- | --- |
| scrollDirection | 滚动方向，默认为 Axis.vertical（垂直） |
| reverse | 是否反向滚动 |
| padding | 列表内边距 |
| itemExtent | 固定项目高度，可提升性能 |
| prototypeItem | 原型项目，用于计算高度 |


## 实例：横向 ListView


```
// 横向滚动列表
SizedBox(
  height: 120,  // 必须设置高度
  child: ListView.builder(
    scrollDirection: Axis.horizontal,  // 横向滚动
    itemCount: 20,
    itemBuilder: (context, index) {
      return Container(
        width: 100,
        margin: const EdgeInsets.symmetric(horizontal: 8),
        color: Colors.blue[100],
        child: Center(
          child: Text('项 $index'),
        ),
      );
    },
  ),
)
```


---


## GridView - 网格布局


GridView 用于创建二维网格列表。


## 实例：GridView 用法


```
// GridView.count - 固定列数
GridView.count(
  crossAxisCount: 3,  // 3 列
  children: List.generate(20, (index) {
    return Container(
      margin: const EdgeInsets.all(4),
      color: Colors.blue[100],
      child: Center(child: Text('${index + 1}')),
    );
  }),
)

// GridView.builder - 动态构建
GridView.builder(
  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
    crossAxisCount: 4,  // 4 列
    mainAxisSpacing: 8,  // 垂直间距
    crossAxisSpacing: 8,  // 水平间距
    childAspectRatio: 1,  // 宽高比
  ),
  itemCount: 50,
  itemBuilder: (context, index) {
    return Container(
      color: Colors.green[100],
      child: Center(child: Text('${index + 1}')),
    );
  },
)

// GridView.extent - 自适应列数
GridView.extent(
  maxCrossAxisExtent: 150,  // 最大列宽
  children: List.generate(20, (index) {
    return Container(
      margin: const EdgeInsets.all(4),
      color: Colors.orange[100],
      child: Center(child: Text('${index + 1}')),
    );
  }),
)
```


---


## 滚动控制


使用 ScrollController 可以控制滚动位置。


## 实例：滚动控制


```
class ScrollExample extends StatefulWidget {
  const ScrollExample({super.key});

  @override
  State<ScrollExample> createState() => _ScrollExampleState();
}

class _ScrollExampleState extends State<ScrollExample> {
  // 创建滚动控制器
  late ScrollController _controller;

  @override
  void initState() {
    super.initState();
    _controller = ScrollController();
    // 监听滚动事件
    _controller.addListener(() {
      print('滚动位置: ${_controller.offset}');
    });
  }

  @override
  void dispose() {
    // 销毁控制器
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // 滚动到顶部按钮
        ElevatedButton(
          onPressed: () {
            // 滚动到顶部
            _controller.animateTo(
              0,
              duration: const Duration(milliseconds: 500),
              curve: Curves.easeInOut,
            );
          },
          child: const Text('滚动到顶部'),
        ),
        // 列表
        Expanded(
          child: ListView.builder(
            controller: _controller,  // 绑定控制器
            itemCount: 100,
            itemBuilder: (context, index) {
              return ListTile(title: Text('第 ${index + 1} 项'));
            },
          ),
        ),
      ],
    );
  }
}
```


---


## Slivers 高级滚动


CustomScrollView 配合 Slivers 可以实现更复杂的滚动效果。


## 实例：Slivers 实现折叠效果


```
// 带折叠应用栏的滚动视图
CustomScrollView(
  slivers: [
    // 折叠应用栏
    SliverAppBar(
      expandedHeight: 200,  // 展开高度
      pinned: true,  // 固定在顶部
      flexibleSpace: FlexibleSpaceBar(
        title: const Text('折叠标题'),
        background: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              colors: [Colors.blue, Colors.purple],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
          ),
        ),
      ),
    ),
    // 列表内容
    SliverList(
      delegate: SliverChildBuilderDelegate(
        (context, index) => ListTile(title: Text('第 ${index + 1} 项')),
        childCount: 30,
      ),
    ),
  ],
)

// 网格 Sliver
CustomScrollView(
  slivers: [
    const SliverAppBar(
      title: Text('图片网格'),
      pinned: true,
    ),
    SliverGrid(
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
      ),
      delegate: SliverChildBuilderDelegate(
        (context, index) => Card(
          child: Image.network('https://picsum.photos/200?$index'),
        ),
        childCount: 20,
      ),
    ),
  ],
)
```


**

Slivers 提供了一种高效的方式来处理大量滚动项目，它们只渲染可见区域的项目，从而提供良好的性能。










	  AI 思考中...





			** [Flutter Container 与装饰](https://www.runoob.com/flutter-container.html)
			[Flutter 用户输入](https://www.runoob.com/flutter-user-input.html) **













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