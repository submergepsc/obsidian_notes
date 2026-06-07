# Flutter 主题与样式

- Source: https://www.runoob.com/flutter/flutter-theming.html

本节将介绍 Flutter 中的主题配置，包括 Material Design 主题、自定义主题和深色模式。


---


## ThemeData - 应用主题


使用 ThemeData 可以统一配置应用的主题颜色、字体、样式等。


## 实例：配置应用主题


```
void main() {
  runApp(
    MaterialApp(
      theme: ThemeData(
        // 主色调
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.blue,
          brightness: Brightness.light,
        ),
        // 使用 Material 3
        useMaterial3: true,
        // 字体
        fontFamily: 'Roboto',
        // 应用栏主题
        appBarTheme: const AppBarTheme(
          centerTitle: true,
          elevation: 0,
        ),
        // 按钮主题
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          ),
        ),
        // 输入框主题
        inputDecorationTheme: InputDecorationTheme(
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          filled: true,
        ),
      ),
      home: const MyHomePage(),
    ),
  );
}
```


---


## Theme.of - 使用主题


在 Widget 中使用 Theme.of(context) 获取当前主题。


## 实例：使用主题颜色


```
class ThemedButton extends StatelessWidget {
  const ThemedButton({super.key});

  @override
  Widget build(BuildContext context) {
    // 获取主题
    final theme = Theme.of(context);

    return Column(
      children: [
        // 使用主题色
        Container(
          color: theme.colorScheme.primary,
          padding: const EdgeInsets.all(16),
          child: Text(
            '主要颜色',
            style: TextStyle(color: theme.colorScheme.onPrimary),
          ),
        ),
        const SizedBox(height: 16),
        // 使用次要色
        Container(
          color: theme.colorScheme.secondary,
          padding: const EdgeInsets.all(16),
          child: Text(
            '次要颜色',
            style: TextStyle(color: theme.colorScheme.onSecondary),
          ),
        ),
        const SizedBox(height: 16),
        // 使用错误色
        Container(
          color: theme.colorScheme.error,
          padding: const EdgeInsets.all(16),
          child: Text(
            '错误颜色',
            style: TextStyle(color: theme.colorScheme.onError),
          ),
        ),
      ],
    );
  }
}
```


---


## 深色模式


## 实例：深色模式支持


```
void main() {
  runApp(
    MaterialApp(
      theme: ThemeData(
        // 浅色主题
        brightness: Brightness.light,
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
      ),
      darkTheme: ThemeData(
        // 深色主题
        brightness: Brightness.dark,
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.blue,
          brightness: Brightness.dark,
        ),
      ),
      // 同时启用（可选）
      themeMode: ThemeMode.system,  // 根据系统设置
      // themeMode: ThemeMode.light   // 强制浅色
      // themeMode: ThemeMode.dark    // 强制深色
      home: const ThemeTogglePage(),
    ),
  );
}

// 切换主题
class ThemeTogglePage extends StatelessWidget {
  const ThemeTogglePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('主题切换')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('当前主题'),
            const SizedBox(height: 20),
            // 切换主题按钮
            ElevatedButton(
              onPressed: () {
                final currentMode = Theme.of(context).brightness;
                if (currentMode == Brightness.light) {
                  // 切换到深色
                  Theme.of(context).setThemeMode(ThemeMode.dark);
                } else {
                  // 切换到浅色
                  Theme.of(context).setThemeMode(ThemeMode.light);
                }
              },
              child: const Text('切换主题'),
            ),
          ],
        ),
      ),
    );
  }
}
```


---


## 自定义样式扩展


## 实例：自定义 TextTheme


```
ThemeData(
  textTheme: const TextTheme(
    // 展示文字（大标题）
    displayLarge: TextStyle(fontSize: 57, fontWeight: FontWeight.w400),
    displayMedium: TextStyle(fontSize: 45, fontWeight: FontWeight.w400),
    displaySmall: TextStyle(fontSize: 36, fontWeight: FontWeight.w400),
    // 标题文字
    headlineLarge: TextStyle(fontSize: 32, fontWeight: FontWeight.w400),
    headlineMedium: TextStyle(fontSize: 28, fontWeight: FontWeight.w400),
    headlineSmall: TextStyle(fontSize: 24, fontWeight: FontWeight.w400),
    // 标题文字
    titleLarge: TextStyle(fontSize: 22, fontWeight: FontWeight.w500),
    titleMedium: TextStyle(fontSize: 16, fontWeight: FontWeight.w500),
    titleSmall: TextStyle(fontSize: 14, fontWeight: FontWeight.w500),
    // 正文文字
    bodyLarge: TextStyle(fontSize: 16, fontWeight: FontWeight.w400),
    bodyMedium: TextStyle(fontSize: 14, fontWeight: FontWeight.w400),
    bodySmall: TextStyle(fontSize: 12, fontWeight: FontWeight.w400),
    // 标签文字
    labelLarge: TextStyle(fontSize: 14, fontWeight: FontWeight.w500),
    labelMedium: TextStyle(fontSize: 12, fontWeight: FontWeight.w500),
    labelSmall: TextStyle(fontSize: 11, fontWeight: FontWeight.w500),
  ),
)
```


**

使用 ThemeData 统一管理应用样式，可以轻松实现主题切换和样式统一，维护更方便。










	  AI 思考中...





			** [Flutter 表单与验证](https://www.runoob.com/flutter-form-validation.html)
			[Flutter 动画基础](https://www.runoob.com/flutter-animation.html) **













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