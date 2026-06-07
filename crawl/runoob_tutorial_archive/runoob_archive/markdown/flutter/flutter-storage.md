# Flutter 本地存储

- Source: https://www.runoob.com/flutter/flutter-storage.html

本节将介绍 Flutter 中的本地存储方案，包括 SharedPreferences、文件存储和 SQLite 数据库。


---


## SharedPreferences - 轻量级存储


SharedPreferences 适合存储简单的键值对数据。


### 添加依赖


```
dependencies:
  shared_preferences: ^2.0.0
```


## 实例：SharedPreferences 使用


```
import 'package:shared_preferences/shared_preferences.dart';

// 保存数据
Future<void> saveData() async {
  final prefs = await SharedPreferences.getInstance();

  // 保存字符串
  await prefs.setString('username', '张三');

  // 保存整数
  await prefs.setInt('age', 25);

  // 保存布尔值
  await prefs.setBool('isLoggedIn', true);

  // 保存列表（JSON 字符串）
  await prefs.setStringList('tags', ['flutter', 'dart']);
}

// 读取数据
Future<void> loadData() async {
  final prefs = await SharedPreferences.getInstance();

  final username = prefs.getString('username') ?? '';
  final age = prefs.getInt('age') ?? 0;
  final isLoggedIn = prefs.getBool('isLoggedIn') ?? false;
  final tags = prefs.getStringList('tags') ?? [];

  print('用户名: $username');
  print('年龄: $age');
  print('已登录: $isLoggedIn');
  print('标签: $tags');
}

// 删除数据
Future<void> deleteData() async {
  final prefs = await SharedPreferences.getInstance();

  // 删除单个
  await prefs.remove('username');

  // 删除所有
  await prefs.clear();
}
```


---


## 文件存储


使用 path_provider 获取应用文档目录进行文件存储。


### 添加依赖


```
dependencies:
  path_provider: ^2.0.0
```


## 实例：文件读写


```
import 'dart:io';
import 'package:path_provider/path_provider.dart';

// 获取文档目录
Future<Directory> get _documentDirectory async {
  return await getApplicationDocumentsDirectory();
}

// 写入文件
Future<void> writeFile() async {
  final dir = await _documentDirectory;
  final file = File('${dir.path}/my_file.txt');

  // 写入文本
  await file.writeAsString('Hello Flutter!');

  // 写入字节
  final bytes = [72, 101, 108, 108, 111];  // "Hello"
  await file.writeAsBytes(bytes);
}

// 读取文件
Future<void> readFile() async {
  final dir = await _documentDirectory;
  final file = File('${dir.path}/my_file.txt');

  if (await file.exists()) {
    // 读取文本
    final content = await file.readAsString();
    print('文件内容: $content');

    // 读取字节
    final bytes = await file.readAsBytes();
    print('字节: $bytes');
  }
}

// JSON 文件存储
Future<void> saveJson() async {
  final dir = await _documentDirectory;
  final file = File('${dir.path}/data.json');

  final data = {
    'name': '张三',
    'age': 25,
    'skills': ['Flutter', 'Dart'],
  };

  // 使用 jsonEncode 保存 JSON
  await file.writeAsString(jsonEncode(data));
}
```


---


## SQLite 数据库


使用 sqflite 进行 SQLite 数据库操作。


### 添加依赖


```
dependencies:
  sqflite: ^2.0.0
  path: ^1.8.0
```


## 实例：SQLite 基本操作


```
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

// 数据库帮助类
class DatabaseHelper {
  static final DatabaseHelper instance = DatabaseHelper._init();
  static Database? _database;

  DatabaseHelper._init();

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDB('my_app.db');
    return _database!;
  }

  // 初始化数据库
  Future<Database> _initDB(String filePath) async {
    final dbPath = await getDatabasesPath();
    final path = join(dbPath, filePath);

    return await openDatabase(
      path,
      version: 1,
      onCreate: _createDB,
    );
  }

  // 创建表
  Future<void> _createDB(Database db, int version) async {
    await db.execute('''
      CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
      )
    ''');
  }

  // 插入数据
  Future<int> insertUser(Map<String, dynamic> user) async {
    final db = await database;
    return await db.insert('users', user);
  }

  // 查询所有用户
  Future<List<Map<String, dynamic>>> getAllUsers() async {
    final db = await database;
    return await db.query('users');
  }

  // 条件查询
  Future<List<Map<String, dynamic>>> getUserByName(String name) async {
    final db = await database;
    return await db.query(
      'users',
      where: 'name = ?',
      whereArgs: [name],
    );
  }

  // 更新数据
  Future<int> updateUser(int id, Map<String, dynamic> user) async {
    final db = await database;
    return await db.update(
      'users',
      user,
      where: 'id = ?',
      whereArgs: [id],
    );
  }

  // 删除数据
  Future<int> deleteUser(int id) async {
    final db = await database;
    return await db.delete(
      'users',
      where: 'id = ?',
      whereArgs: [id],
    );
  }

  // 关闭数据库
  Future<void> close() async {
    final db = await database;
    db.close();
  }
}

// 使用示例
Future<void> dbExample() async {
  final db = DatabaseHelper.instance;

  // 添加用户
  await db.insertUser({
    'name': '张三',
    'email': '[email protected]',
    'age': 25,
  });

  // 查询所有
  final users = await db.getAllUsers();
  print('用户列表: $users');

  // 更新用户
  await db.updateUser(1, {'name': '李四', 'age': 30});

  // 删除用户
  await db.deleteUser(1);
}
```


**

数据存储方案选择：简单键值用 SharedPreferences，复杂结构用 SQLite，文件存储适合大文件。










	  AI 思考中...





			** [Flutter 动画基础](https://www.runoob.com/flutter-animation.html)
			[Flutter 图片与资源](https://www.runoob.com/flutter-images.html) **













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