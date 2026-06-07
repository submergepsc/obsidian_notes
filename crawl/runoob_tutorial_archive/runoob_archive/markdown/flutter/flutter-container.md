# Flutter Container 与装饰

- Source: https://www.runoob.com/flutter/flutter-container.html

Container 是 Flutter 中最常用的通用容器 Widget，它提供了设置尺寸、背景、边框、阴影等能力。


---


## Container 概述


Container 是一个组合 Widget，内部封装了 Padding、ColoredBox、SizedBox、DecoratedBox 等功能。


## 实例：Container 基本用法


```
// 最简单的 Container
Container(
  child: Text('Hello'),
)

// 带尺寸的 Container
Container(
  width: 200,
  height: 100,
  child: Text('固定尺寸'),
)

// 带颜色的 Container
Container(
  width: 200,
  height: 100,
  color: Colors.blue,
  child: Text('蓝色背景', style: TextStyle(color: Colors.white)),
)
```


---


## BoxDecoration - 装饰效果


使用 BoxDecoration 可以添加更丰富的装饰效果，如背景、边框、阴影、圆角等。


### 背景色


## 实例：背景色设置


```
// 纯色背景
Container(
  decoration: BoxDecoration(
    color: Colors.blue,
  ),
  child: const Text('蓝色背景'),
)

// 使用渐变背景
Container(
  decoration: BoxDecoration(
    gradient: LinearGradient(
      colors: [Colors.blue, Colors.green],
      begin: Alignment.topLeft,
      end: Alignment.bottomRight,
    ),
  ),
  child: const Text('渐变背景'),
)

// 径向渐变
Container(
  decoration: BoxDecoration(
    gradient: RadialGradient(
      colors: [Colors.yellow, Colors.orange],
    ),
  ),
  child: const Text('径向渐变'),
)
```


### 边框


## 实例：边框设置


```
// 简单边框
Container(
  decoration: BoxDecoration(
    border: Border.all(color: Colors.black, width: 2),
  ),
  child: const Text('黑色边框'),
)

// 各边不同边框
Container(
  decoration: BoxDecoration(
    border: Border(
      top: BorderSide(color: Colors.red, width: 2),
      bottom: BorderSide(color: Colors.blue, width: 2),
      left: BorderSide(color: Colors.green, width: 2),
      right: BorderSide(color: Colors.orange, width: 2),
    ),
  ),
  child: const Text('各边不同边框'),
)

// 圆形边框
Container(
  decoration: BoxDecoration(
    border: Border.all(color: Colors.purple, width: 3),
    borderRadius: BorderRadius.circular(10),
  ),
  padding: const EdgeInsets.all(16),
  child: const Text('圆角边框'),
)
```


### 圆角


## 实例：圆角设置


```
// 统一圆角
Container(
  width: 100,
  height: 100,
  decoration: BoxDecoration(
    color: Colors.blue,
    borderRadius: BorderRadius.circular(20),  // 圆角半径 20
  ),
)

// 不同圆角
Container(
  width: 100,
  height: 100,
  decoration: BoxDecoration(
    color: Colors.green,
    borderRadius: BorderRadius.only(
      topLeft: Radius.circular(20),
      topRight: Radius.circular(10),
      bottomLeft: Radius.circular(10),
      bottomRight: Radius.circular(20),
    ),
  ),
)

// 圆形
Container(
  width: 100,
  height: 100,
  decoration: BoxDecoration(
    color: Colors.red,
    shape: BoxShape.circle,
  ),
)
```


### 阴影


## 实例：阴影设置


```
// 简单阴影
Container(
  width: 100,
  height: 100,
  decoration: BoxDecoration(
    color: Colors.white,
    boxShadow: [
      BoxShadow(
        color: Colors.black.withOpacity(0.3),
        blurRadius: 10,  // 模糊半径
        offset: Offset(5, 5),  // 偏移量
      ),
    ],
  ),
)

// 多层阴影
Container(
  width: 100,
  height: 100,
  decoration: BoxDecoration(
    color: Colors.white,
    boxShadow: [
      BoxShadow(
        color: Colors.red.withOpacity(0.3),
        blurRadius: 5,
        offset: Offset(-3, -3),
      ),
      BoxShadow(
        color: Colors.blue.withOpacity(0.3),
        blurRadius: 5,
        offset: Offset(3, 3),
      ),
    ],
  ),
)

// 卡片阴影（使用 elevation）
Card(
  elevation: 8,
  child: Container(
    width: 100,
    height: 100,
    child: const Center(child: Text('卡片')),
  ),
)
```


---


## Clip - 裁剪


使用 Clip 类可以裁剪子 Widget 的显示区域。


## 实例：裁剪用法


```
// 圆形裁剪
ClipOval(
  child: Image.network(
    'https://example.com/avatar.jpg',
    width: 100,
    height: 100,
    fit: BoxFit.cover,
  ),
)

// 圆角矩形裁剪
ClipRRect(
  borderRadius: BorderRadius.circular(20),
  child: Image.network(
    'https://example.com/image.jpg',
    width: 200,
    height: 150,
    fit: BoxFit.cover,
  ),
)

// 自定义路径裁剪
ClipPath(
  clipper: TriangleClipper(),
  child: Image.network(
    'https://example.com/image.jpg',
    width: 200,
    height: 200,
  ),
)
```


---


## 综合示例


## 实例：综合使用示例


```
// 带渐变、圆角、阴影的卡片
class MyCard extends StatelessWidget {
  final String title;
  final String description;
  final IconData icon;

  const MyCard({
    super.key,
    required this.title,
    required this.description,
    required this.icon,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 280,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        // 渐变背景
        gradient: LinearGradient(
          colors: [Colors.blue[400]!, Colors.blue[700]!],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        // 圆角
        borderRadius: BorderRadius.circular(16),
        // 阴影
        boxShadow: [
          BoxShadow(
            color: Colors.blue.withOpacity(0.4),
            blurRadius: 12,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisSize: MainAxisSize.min,
        children: [
          // 图标
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.2),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(icon, color: Colors.white, size: 32),
          ),
          const SizedBox(height: 16),
          // 标题
          Text(
            title,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 8),
          // 描述
          Text(
            description,
            style: TextStyle(
              color: Colors.white.withOpacity(0.9),
              fontSize: 14,
            ),
          ),
        ],
      ),
    );
  }
}
```










	  AI 思考中...





			** [Flutter 布局基础](https://www.runoob.com/flutter-layout.html)
			[Flutter ListView 与滚动](https://www.runoob.com/flutter-listview.html) **













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