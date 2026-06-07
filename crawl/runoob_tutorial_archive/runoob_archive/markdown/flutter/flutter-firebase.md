# Firebase 集成

- Source: https://www.runoob.com/flutter/flutter-firebase.html

Firebase 是 Google 提供的移动和 Web 应用开发平台，本节将介绍如何在 Flutter 中集成 Firebase。


---


## Firebase 概述


Firebase 提供多种后端服务，包括认证、数据库、存储、分析等。


| 服务 | 说明 |
| --- | --- |
| Firebase Auth | 用户身份验证 |
| Cloud Firestore | 云端 NoSQL 数据库 |
| Realtime Database | 实时数据库 |
| Cloud Storage | 云端文件存储 |
| Firebase Analytics | 应用数据分析 |
| Cloud Functions | 云端无服务器函数 |


---


## 安装与配置


### 添加依赖


```
dependencies:
  firebase_core: ^2.0.0
  firebase_auth: ^4.0.0
  cloud_firestore: ^4.0.0
```


### Firebase 初始化


## 实例：初始化 Firebase


```
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // 初始化 Firebase
  await Firebase.initializeApp();

  runApp(const MyApp());
}
```


---


## Firebase Auth - 用户认证


## 实例：邮箱密码登录


```
import 'package:firebase_auth/firebase_auth.dart';

class AuthService {
  final FirebaseAuth _auth = FirebaseAuth.instance;

  // 注册
  Future<User?> registerWithEmail(String email, String password) async {
    try {
      final credential = await _auth.createUserWithEmailAndPassword(
        email: email,
        password: password,
      );
      return credential.user;
    } on FirebaseAuthException catch (e) {
      print('注册失败: ${e.message}');
      return null;
    }
  }

  // 登录
  Future<User?> signInWithEmail(String email, String password) async {
    try {
      final credential = await _auth.signInWithEmailAndPassword(
        email: email,
        password: password,
      );
      return credential.user;
    } on FirebaseAuthException catch (e) {
      print('登录失败: ${e.message}');
      return null;
    }
  }

  // 退出登录
  Future<void> signOut() async {
    await _auth.signOut();
  }

  // 监听登录状态
  Stream<User?> get authStateChanges {
    return _auth.authStateChanges();
  }
}
```


---


## Cloud Firestore - 数据库


## 实例：Firestore 基本操作


```
import 'package:cloud_firestore/cloud_firestore.dart';

class FirestoreService {
  final FirebaseFirestore _db = FirebaseFirestore.instance;

  // 添加文档
  Future<void> addUser(Map<String, dynamic> user) async {
    await _db.collection('users').add(user);
    // 或指定 ID
    // await _db.collection('users').doc('user_id').set(user);
  }

  // 获取单个文档
  Future<Map<String, dynamic>?> getUser(String id) async {
    final doc = await _db.collection('users').doc(id).get();
    return doc.data();
  }

  // 获取集合所有文档
  Future<List<Map<String, dynamic>>> getUsers() async {
    final snapshot = await _db.collection('users').get();
    return snapshot.docs.map((doc) => doc.data()).toList();
  }

  // 条件查询
  Future<List<Map<String, dynamic>>> getUsersByAge(int age) async {
    final snapshot = await _db
        .collection('users')
        .where('age', isGreaterThanOrEqualTo: age)
        .get();
    return snapshot.docs.map((doc) => doc.data()).toList();
  }

  // 更新文档
  Future<void> updateUser(String id, Map<String, dynamic> data) async {
    await _db.collection('users').doc(id).update(data);
  }

  // 删除文档
  Future<void> deleteUser(String id) async {
    await _db.collection('users').doc(id).delete();
  }

  // 实时监听
  Stream<QuerySnapshot> watchUsers() {
    return _db.collection('users').snapshots();
  }
}
```


---


## Firebase Storage - 文件存储


## 实例：文件上传


```
import 'package:firebase_storage/firebase_storage.dart';
import 'dart:io';

class StorageService {
  final FirebaseStorage _storage = FirebaseStorage.instance;

  // 上传文件
  Future<String?> uploadFile(File file, String path) async {
    try {
      final ref = _storage.ref().child(path);
      final result = await ref.putFile(file);
      return await result.ref.getDownloadURL();
    } on FirebaseException catch (e) {
      print('上传失败: ${e.message}');
      return null;
    }
  }

  // 下载文件 URL
  Future<String?> getDownloadURL(String path) async {
    try {
      final ref = _storage.ref().child(path);
      return await ref.getDownloadURL();
    } on FirebaseException catch (e) {
      print('获取 URL 失败: ${e.message}');
      return null;
    }
  }

  // 删除文件
  Future<void> deleteFile(String path) async {
    await _storage.ref().child(path).delete();
  }
}
```


**

Firebase 提供了强大的后端服务，是 Flutter 应用快速构建后端的最佳选择。










	  AI 思考中...





			** [Flutter 最佳实践](https://www.runoob.com/flutter-best-practices.html)
			[Flutter 进阶](https://www.runoob.com/flutter-advanced.html) **













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