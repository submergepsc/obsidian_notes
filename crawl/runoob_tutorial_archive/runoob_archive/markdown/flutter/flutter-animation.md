# Flutter 动画基础

- Source: https://www.runoob.com/flutter/flutter-animation.html

本节将介绍 Flutter 中的动画实现，包括隐式动画和显式动画。


---


## 隐式动画


隐式动画是由 Flutter 自动处理过渡效果的动画 Widget。


## 实例：AnimatedContainer


```
class AnimatedContainerExample extends StatefulWidget {
  const AnimatedContainerExample({super.key});

  @override
  State<AnimatedContainerExample> createState() =>
      _AnimatedContainerExampleState();
}

class _AnimatedContainerExampleState
    extends State<AnimatedContainerExample> {
  bool _isLarge = false;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // 点击切换尺寸
        GestureDetector(
          onTap: () => setState(() => _isLarge = !_isLarge),
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 500),  // 动画时长
            curve: Curves.easeInOut,  // 动画曲线
            width: _isLarge ? 200 : 100,
            height: _isLarge ? 200 : 100,
            color: _isLarge ? Colors.blue : Colors.red,
            child: Center(
              child: Text(
                _isLarge ? '大' : '小',
                style: const TextStyle(color: Colors.white, fontSize: 24),
              ),
            ),
          ),
        ),
        const SizedBox(height: 20),
        ElevatedButton(
          onPressed: () => setState(() => _isLarge = !_isLarge),
          child: const Text('切换'),
        ),
      ],
    );
  }
}
```


### 常用隐式动画 Widget


| Widget | 说明 |
| --- | --- |
| AnimatedContainer | 容器大小、颜色等属性变化时的动画 |
| AnimatedOpacity | 透明度变化动画 |
| AnimatedPadding | 内边距变化动画 |
| AnimatedAlign | 对齐方式变化动画 |
| AnimatedSwitcher | 切换子 Widget 时的动画 |
| AnimatedDefaultTextStyle | 文字样式变化动画 |


---


## 显式动画


显式动画使用 AnimationController 完全控制动画。


## 实例：旋转动画


```
class RotationAnimation extends StatefulWidget {
  const RotationAnimation({super.key});

  @override
  State<RotationAnimation> createState() => _RotationAnimationState();
}

class _RotationAnimationState extends State<RotationAnimation>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    // 创建动画控制器
    _controller = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    );

    // 创建旋转动画（0 到 1 映射到 0 到 2π）
    _animation = Tween<double>(begin: 0, end: 6.28).animate(
      CurvedAnimation(parent: _controller, curve: Curves.linear),
    );

    // 开始动画
    _controller.repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: AnimatedBuilder(
        animation: _animation,
        builder: (context, child) {
          return Transform.rotate(
            angle: _animation.value,  // 旋转角度
            child: const Icon(Icons.refresh, size: 100),
          );
        },
      ),
    );
  }
}
```


---


## 交错动画


## 实例：交错动画


```
class StaggeredAnimation extends StatefulWidget {
  const StaggeredAnimation({super.key});

  @override
  State<StaggeredAnimation> createState() => _StaggeredAnimationState();
}

class _StaggeredAnimationState extends State<StaggeredAnimation>
    with TickerProviderStateMixin {
  late AnimationController _controller;

  // 各个动画
  late Animation<double> _fadeAnimation;
  late Animation<double> _scaleAnimation;
  late Animation<Offset> _slideAnimation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 1500),
      vsync: this,
    );

    // 淡入动画（0-0.5）
    _fadeAnimation = Tween<double>(begin: 0, end: 1).animate(
      CurvedAnimation(
        parent: _controller,
        curve: const Interval(0, 0.5, curve: Curves.easeOut),
      ),
    );

    // 缩放动画（0.3-0.7）
    _scaleAnimation = Tween<double>(begin: 0.5, end: 1).animate(
      CurvedAnimation(
        parent: _controller,
        curve: const Interval(0.3, 0.7, curve: Curves.elasticOut),
      ),
    );

    // 滑入动画（0.5-1.0）
    _slideAnimation = Tween<Offset>(
      begin: const Offset(0, 0.5),
      end: Offset.zero,
    ).animate(
      CurvedAnimation(
        parent: _controller,
        curve: const Interval(0.5, 1, curve: Curves.easeOutCubic),
      ),
    );

    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        return FadeTransition(
          opacity: _fadeAnimation,
          child: ScaleTransition(
            scale: _scaleAnimation,
            child: SlideTransition(
              position: _slideAnimation,
              child: const Card(
                child: Padding(
                  padding: EdgeInsets.all(24),
                  child: Text('欢迎'),
                ),
              ),
            ),
          ),
        );
      },
    );
  }
}
```


---


## Hero 动画


Hero 动画用于在页面切换时创建共享元素的过渡效果。


## 实例：Hero 动画


```
// 首页 - 带 Hero 的图片
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('首页')),
      body: Center(
        child: GestureDetector(
          onTap: () => Navigator.push(
            context,
            MaterialPageRoute(builder: (_) => const DetailPage()),
          ),
          child: Hero(
            tag: 'myHero',  // 相同的 tag
            child: Image.network(
              'https://picsum.photos/200',
              width: 200,
              height: 200,
            ),
          ),
        ),
      ),
    );
  }
}

// 详情页 - 带 Hero 的图片
class DetailPage extends StatelessWidget {
  const DetailPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('详情')),
      body: Center(
        child: Hero(
          tag: 'myHero',  // 相同的 tag
          child: Image.network(
            'https://picsum.photos/200',
            width: 300,
            height: 300,
          ),
        ),
      ),
    );
  }
}
```


**

隐式动画适合简单场景，显式动画适合复杂控制。


Hero 动画是页面切换时的最佳选择。










	  AI 思考中...





			** [Flutter 主题与样式](https://www.runoob.com/flutter-theming.html)
			[Flutter 本地存储](https://www.runoob.com/flutter-storage.html) **













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