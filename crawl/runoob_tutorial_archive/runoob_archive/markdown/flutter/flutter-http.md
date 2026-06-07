# Flutter HTTP 请求

- Source: https://www.runoob.com/flutter/flutter-http.html

本节将介绍如何在 Flutter 应用中进行 HTTP 网络请求，包括 GET、POST 请求以及 JSON 数据处理。


---


## 添加 HTTP 依赖


在 pubspec.yaml 中添加 http 包：


```
dependencies:
  http: ^1.0.0
```


然后运行：


```
$ flutter pub get
```


---


## 发送 GET 请求


## 实例：GET 请求


```
import 'dart:convert';
import 'package:http/http.dart' as http;

// 简单的 GET 请求
Future<void> fetchData() async {
  final response = await http.get(Uri.parse('https://jsonplaceholder.typicode.com/posts/1'));

  if (response.statusCode == 200) {
    // 解析 JSON 数据
    final data = jsonDecode(response.body);
    print('标题: ${data['title']}');
  } else {
    print('请求失败: ${response.statusCode}');
  }
}

// 带参数的 GET 请求
Future<void> searchData(String query) async {
  final uri = Uri.parse('https://api.example.com/search')
      .replace(queryParameters: {'q': query, 'page': '1'});

  final response = await http.get(uri);

  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);
    print('结果: $data');
  }
}
```


---


## 发送 POST 请求


## 实例：POST 请求


```
import 'dart:convert';
import 'package:http/http.dart' as http;

// POST 请求 - 发送 JSON 数据
Future<void> postData() async {
  final uri = Uri.parse('https://jsonplaceholder.typicode.com/posts');

  final response = await http.post(
    uri,
    headers: {
      'Content-Type': 'application/json',  // 设置请求头
    },
    body: jsonEncode({  // 将 Dart 对象转换为 JSON 字符串
      'title': 'Flutter 教程',
      'body': '学习 Flutter 网络请求',
      'userId': 1,
    }),
  );

  if (response.statusCode == 201) {
    final data = jsonDecode(response.body);
    print('创建成功: $data');
  } else {
    print('请求失败: ${response.statusCode}');
  }
}

// POST 请求 - 发送表单数据
Future<void> postFormData() async {
  final uri = Uri.parse('https://example.com/api/login');

  final response = await http.post(
    uri,
    body: {
      'username': 'admin',
      'password': '123456',
    },
  );

  print('响应: ${response.body}');
}
```


---


## 处理 JSON 数据


## 实例：JSON 解析


```
import 'dart:convert';

// 定义数据模型
class Article {
  final int id;
  final String title;
  final String body;
  final User user;

  Article({
    required this.id,
    required this.title,
    required this.body,
    required this.user,
  });

  // 从 JSON 解析
  factory Article.fromJson(Map<String, dynamic> json) {
    return Article(
      id: json['id'],
      title: json['title'],
      body: json['body'],
      user: User.fromJson(json['user']),
    );
  }

  // 转换为 JSON
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'body': body,
      'user': user.toJson(),
    };
  }
}

class User {
  final int id;
  final String name;

  User({required this.id, required this.name});

  factory User.fromJson(Map<String, dynamic> json) {
    return User(id: json['id'], name: json['name']);
  }

  Map<String, dynamic> toJson() {
    return {'id': id, 'name': name};
  }
}

// 使用示例
void parseJson() {
  final jsonString = '''
  {
    "id": 1,
    "title": "Flutter 教程",
    "body": "学习 Flutter",
    "user": {"id": 1, "name": "张三"}
  }
  ''';

  // 解析 JSON 字符串
  final Map<String, dynamic> json = jsonDecode(jsonString);
  final article = Article.fromJson(json);

  print('文章ID: ${article.id}');
  print('作者: ${article.user.name}');
}
```


---


## 错误处理


## 实例：完整的网络请求示例


```
import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  // 基础 URL
  static const String baseUrl = 'https://jsonplaceholder.typicode.com';

  // 通用 GET 请求方法
  static Future<dynamic> get(String endpoint) async {
    try {
      final response = await http.get(
        Uri.parse('$baseUrl/$endpoint'),
      );
      return _handleResponse(response);
    } catch (e) {
      throw ApiException('网络错误: $e');
    }
  }

  // 通用 POST 请求方法
  static Future<dynamic> post(
    String endpoint,
    Map<String, dynamic> data,
  ) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/$endpoint'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode(data),
      );
      return _handleResponse(response);
    } catch (e) {
      throw ApiException('网络错误: $e');
    }
  }

  // 处理响应
  static dynamic _handleResponse(http.Response response) {
    if (response.statusCode >= 200 && response.statusCode < 300) {
      // 成功响应
      if (response.body.isEmpty) {
        return null;
      }
      return jsonDecode(response.body);
    } else if (response.statusCode == 404) {
      throw ApiException('资源未找到', statusCode: 404);
    } else if (response.statusCode >= 500) {
      throw ApiException('服务器错误', statusCode: response.statusCode);
    } else {
      throw ApiException(
        '请求失败',
        statusCode: response.statusCode,
      );
    }
  }
}

// 自定义异常类
class ApiException implements Exception {
  final String message;
  final int? statusCode;

  ApiException(this.message, {this.statusCode});

  @override
  String toString() => 'ApiException: $message (status: $statusCode)';
}

// 使用示例
Future<void> fetchArticles() async {
  try {
    final articles = await ApiService.get('posts');
    print('获取到 ${articles.length} 篇文章');
  } on ApiException catch (e) {
    print('API 错误: $e');
  }
}
```


**

在真实应用中，建议将网络请求封装成服务类，统一处理错误、加载状态和缓存逻辑。










	  AI 思考中...





			** [Flutter 状态管理](https://www.runoob.com/flutter-state-management.html)
			[Flutter 导航与路由](https://www.runoob.com/flutter-navigation.html) **













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