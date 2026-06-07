# Flutter 导航与路由

- Source: https://www.runoob.com/flutter/flutter-navigation.html

本节将介绍 Flutter 中的导航和路由机制，包括页面跳转、参数传递和命名路由。


---


## Navigator 基础


Flutter 使用 Navigator 进行页面管理，基于栈（stack）结构实现页面跳转。


## 实例：基本页面跳转


```
// 跳转到新页面
Navigator.of(context).push(
  MaterialPageRoute(
    builder: (context) => const DetailPage(),
  ),
);

// 返回上一页
Navigator.of(context).pop();

// 带结果返回
Navigator.of(context).pop('返回的数据');

// 替换当前页面（不可返回）
Navigator.of(context).pushReplacement(
  MaterialPageRoute(
    builder: (context) => const HomePage(),
  ),
);

// 回到根页面
Navigator.of(context).popUntil((route) => route.isFirst);
```


---


## MaterialPageRoute vs CupertinoPageRoute


## 实例：不同平台的页面切换动画


```
// Android 风格 - 从底部升起
Navigator.of(context).push(
  MaterialPageRoute(
    builder: (context) => const DetailPage(),
  ),
);

// iOS 风格 - 从右侧滑入
Navigator.of(context).push(
  CupertinoPageRoute(
    builder: (context) => const DetailPage(),
  ),
);

// 自定义过渡效果
Navigator.of(context).push(
  PageRouteBuilder(
    pageBuilder: (context, animation, secondaryAnimation) {
      return const DetailPage();
    },
    transitionsBuilder: (context, animation, secondaryAnimation, child) {
      // 淡入淡出效果
      return FadeTransition(
        opacity: animation,
        child: child,
      );
    },
    transitionDuration: const Duration(milliseconds: 300),
  ),
);
```


---


## 页面参数传递


实例：传递参数到新页面


```
// 跳转到详情页并传递参数
Navigator.of(context).push(
  MaterialPageRoute(
    builder: (context) => ProductDetailPage(productId: 123),
  ),
);

// 详情页接收参数
class ProductDetailPage extends StatelessWidget {
  final int productId;

  const ProductDetailPage({
    super.key,
    required this.productId,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('商品 $productId')),
      body: Center(child: Text('商品 ID: $productId')),
    );
  }
}

// 传递多个参数
class UserProfilePage extends StatelessWidget {
  final String name;
  final int age;

  const UserProfilePage({
    super.key,
    required this.name,
    required this.age,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('$name 的主页')),
      body: Center(child: Text('年龄: $age')),
    );
  }
}

// 跳转
Navigator.of(context).push(
  MaterialPageRoute(
    builder: (context) => const UserProfilePage(
      name: '张三',
      age: 25,
    ),
  ),
);
```


---


## 命名路由


使用命名路由可以简化页面跳转配置。


## 实例：命名路由配置


```
void main() {
  runApp(
    MaterialApp(
      // 定义路由表
      initialRoute: '/',
      routes: {
        '/': (context) => const HomePage(),
        '/detail': (context) => const DetailPage(),
        '/user': (context) => const UserPage(),
        '/settings': (context) => const SettingsPage(),
      },
    ),
  );
}

// 跳转
Navigator.pushNamed(context, '/detail');

// 带参数跳转
Navigator.pushNamed(context, '/user', arguments: {'name': '张三', 'age': 25});

// 在目标页面获取参数
class DetailPage extends StatelessWidget {
  const DetailPage({super.key});

  @override
  Widget build(BuildContext context) {
    // 获取传递的参数
    final args = ModalRoute.of(context)?.settings.arguments as Map?;

    return Scaffold(
      appBar: AppBar(title: const Text('详情页')),
      body: Center(
        child: Text('参数: $args'),
      ),
    );
  }
}
```


---


## 路由传值的另一种方式


## 实例：onGenerateRoute


```
MaterialApp(
  onGenerateRoute: (settings) {
    // 根据路由名称返回不同页面
    switch (settings.name) {
      case '/':
        return MaterialPageRoute(
          builder: (_) => const HomePage(),
        );
      case '/detail':
        // 从 arguments 获取参数
        final args = settings.arguments as Map<String, dynamic>?;
        return MaterialPageRoute(
          builder: (_) => DetailPage(
            id: args?['id'] ?? 0,
            title: args?['title'] ?? '',
          ),
        );
      case '/product':
        final productId = settings.name?.split('/').last;
        return MaterialPageRoute(
          builder: (_) => ProductPage(id: productId ?? ''),
        );
      default:
        return MaterialPageRoute(
          builder: (_) => const NotFoundPage(),
        );
    }
  },
)
```


**

对于简单的应用，基础 Navigator.push 就足够了；对于中大型应用，建议使用命名路由或路由管理库来统一管理页面。










	  AI 思考中...





			** [Flutter HTTP 请求](https://www.runoob.com/flutter-http.html)
			[Flutter 表单与验证](https://www.runoob.com/flutter-form-validation.html) **













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