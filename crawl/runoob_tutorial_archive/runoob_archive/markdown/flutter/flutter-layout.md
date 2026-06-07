# Flutter 布局基础

- Source: https://www.runoob.com/flutter/flutter-layout.html

布局是 Flutter UI 开发的核心概念。

本节将介绍最常用的布局 Widget，包括 Row、Column、Stack 和 Flex 等。


---


## 布局 Widget 概述


Flutter 提供了丰富的布局 Widget，可以满足各种界面设计需求。


| Widget | 用途 |
| --- | --- |
| Row | 水平排列子 Widget |
| Column | 垂直排列子 Widget |
| Stack | 层叠排列子 Widget |
| Flex | 灵活的线性布局（Row/Column 的基类） |
| GridView | 网格布局 |
| ListView | 列表布局 |


---


## Row - 水平布局


Row 用于在水平方向上排列子 Widget。


## 实例：Row 基本用法


```
// 水平排列三个图标
Row(
  children: [
    Icon(Icons.home, color: Colors.blue),
    Icon(Icons.search, color: Colors.green),
    Icon(Icons.settings, color: Colors.grey),
  ],
)

// 带间距的 Row
Row(
  mainAxisAlignment: MainAxisAlignment.spaceEvenly,  // 主轴对齐方式
  children: [
    Icon(Icons.home, color: Colors.blue),
    Icon(Icons.search, color: Colors.green),
    Icon(Icons.settings, color: Colors.grey),
  ],
)
```


### mainAxisAlignment - 主轴对齐


| 值 | 说明 |
| --- | --- |
| MainAxisAlignment.start | 靠左对齐（默认） |
| MainAxisAlignment.center | 居中对齐 |
| MainAxisAlignment.end | 靠右对齐 |
| MainAxisAlignment.spaceBetween | 两端对齐，项目间间距相等 |
| MainAxisAlignment.spaceEvenly | 项目间和两端间距相等 |
| MainAxisAlignment.spaceAround | 项目间间距相等，大于两端间距 |


---


## Column - 垂直布局


Column 用于在垂直方向上排列子 Widget。


## 实例：Column 基本用法


```
// 垂直排列三个文本
Column(
  children: [
    Text('第一行', style: TextStyle(fontSize: 20)),
    Text('第二行', style: TextStyle(fontSize: 20)),
    Text('第三行', style: TextStyle(fontSize: 20)),
  ],
)

// 带间距和对齐的 Column
Column(
  mainAxisAlignment: MainAxisAlignment.center,  // 垂直居中
  crossAxisAlignment: CrossAxisAlignment.start,  // 水平靠左
  children: [
    Text('标题', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
    const SizedBox(height: 8),
    Text('内容内容内容'),
    const SizedBox(height: 8),
    Text('底部说明'),
  ],
)
```


### crossAxisAlignment - 交叉轴对齐


| 值 | 说明 |
| --- | --- |
| CrossAxisAlignment.start | 靠上/靠左对齐 |
| CrossAxisAlignment.center | 居中对齐 |
| CrossAxisAlignment.end | 靠下/靠右对齐 |
| CrossAxisAlignment.stretch | 拉伸以填满父容器 |


---


## Expanded 和 Flexible


Expanded 和 Flexible 用于让子 Widget 填充剩余空间。


## 实例：Expanded 用法


```
// 固定宽度 + 自适应宽度
Row(
  children: [
    // 固定宽度 100
    Container(width: 100, height: 50, color: Colors.red),
    // 占据剩余空间
    Expanded(
      child: Container(height: 50, color: Colors.green),
    ),
    // 固定宽度 50
    Container(width: 50, height: 50, color: Colors.blue),
  ],
)

// 分配比例
Row(
  children: [
    // 占 1 份
    Expanded(
      flex: 1,
      child: Container(height: 50, color: Colors.red),
    ),
    // 占 2 份
    Expanded(
      flex: 2,
      child: Container(height: 50, color: Colors.green),
    ),
    // 占 1 份
    Expanded(
      flex: 1,
      child: Container(height: 50, color: Colors.blue),
    ),
  ],
)
```


---


## Stack - 层叠布局


Stack 用于将子 Widget 层叠在一起，常用于实现浮动元素、图层叠加等效果。


## 实例：Stack 用法


```
// 基础 Stack
Stack(
  children: [
    // 底层：背景图片
    Container(
      width: 200,
      height: 200,
      color: Colors.blue,
    ),
    // 中层：半透明覆盖层
    Container(
      width: 180,
      height: 180,
      color: Colors.white.withOpacity(0.5),
    ),
    // 顶层：文字
    const Center(
      child: Text(
        '叠加内容',
        style: TextStyle(color: Colors.white, fontSize: 24),
      ),
    ),
  ],
)

// 带定位的 Stack
Stack(
  children: [
    Container(color: Colors.grey[300]),
    // 定位到右上角
    Positioned(
      right: 10,
      top: 10,
      child: Icon(Icons.close, color: Colors.red),
    ),
    // 定位到左下角
    Positioned(
      left: 10,
      bottom: 10,
      child: Text('左下角文本'),
    ),
  ],
)
```


---


## Padding 和 Margin


使用 Padding 和 Margin 控制元素的内边距和外边距。


## 实例：Padding 和 Margin


```
// 使用 Padding 设置内边距
Padding(
  padding: const EdgeInsets.all(16.0),  // 四边都 16 像素
  child: Text('有内边距的文本'),
)

// 分别设置各边
Padding(
  padding: EdgeInsets.only(
    left: 10,
    right: 20,
    top: 5,
    bottom: 5,
  ),
  child: Text('自定义内边距'),
)

// 使用 EdgeInsets.symmetric 对称边距
Padding(
  padding: EdgeInsets.symmetric(horizontal: 16, vertical: 8),
  child: Text('水平 16，垂直 8'),
)

// Container 结合 margin 和 padding
Container(
  margin: const EdgeInsets.all(10),  // 外边距
  padding: const EdgeInsets.all(16),  // 内边距
  decoration: BoxDecoration(
    color: Colors.blue[100],
    borderRadius: BorderRadius.circular(8),
  ),
  child: Text('容器内容'),
)
```


---


## Scaffold 和 AppBar


Scaffold 提供了 Material Design 的基本页面结构，AppBar 是顶部应用栏。


## 实例：Scaffold 基本结构


```
// Material Design 页面脚手架
Scaffold(
  // 顶部应用栏
  appBar: AppBar(
    title: const Text('我的应用'),
    backgroundColor: Colors.blue,
    elevation: 4,  // 阴影深度
    actions: [
      IconButton(
        icon: const Icon(Icons.search),
        onPressed: () {},
      ),
      IconButton(
        icon: const Icon(Icons.settings),
        onPressed: () {},
      ),
    ],
  ),
  // 页面主体
  body: const Center(
    child: Text('页面主体内容'),
  ),
  // 悬浮按钮
  floatingActionButton: FloatingActionButton(
    onPressed: () {},
    child: const Icon(Icons.add),
  ),
  // 底部导航栏
  bottomNavigationBar: BottomNavigationBar(
    items: const [
      BottomNavigationBarItem(icon: Icon(Icons.home), label: '首页'),
      BottomNavigationBarItem(icon: Icon(Icons.search), label: '搜索'),
      BottomNavigationBarItem(icon: Icon(Icons.person), label: '我的'),
    ],
  ),
)
```










	  AI 思考中...





			** [Flutter StatelessWidget vs StatefulWidget 深入理解](https://www.runoob.com/flutter-stateless-stateful.html)
			[Flutter Container 与装饰](https://www.runoob.com/flutter-container.html) **













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