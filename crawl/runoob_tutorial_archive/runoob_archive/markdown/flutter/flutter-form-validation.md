# Flutter 表单与验证

- Source: https://www.runoob.com/flutter/flutter-form-validation.html

本节将介绍 Flutter 中表单的创建、验证和提交处理。


---


## TextFormField - 表单输入


TextFormField 是专门用于表单的 TextField，支持内置验证功能。


## 实例：基本表单


```
class LoginForm extends StatefulWidget {
  const LoginForm({super.key});

  @override
  State<LoginForm> createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {
  // 表单键（用于验证）
  final _formKey = GlobalKey<FormState>();

  // 输入控制器
  final _usernameController = TextEditingController();
  final _passwordController = TextEditingController();

  @override
  void dispose() {
    _usernameController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: [
          // 用户名输入
          TextFormField(
            controller: _usernameController,
            decoration: const InputDecoration(
              labelText: '用户名',
              prefixIcon: Icon(Icons.person),
            ),
            // 验证器
            validator: (value) {
              if (value == null || value.isEmpty) {
                return '请输入用户名';
              }
              if (value.length < 3) {
                return '用户名至少3个字符';
              }
              return null;
            },
          ),
          const SizedBox(height: 16),
          // 密码输入
          TextFormField(
            controller: _passwordController,
            obscureText: true,  // 隐藏密码
            decoration: const InputDecoration(
              labelText: '密码',
              prefixIcon: Icon(Icons.lock),
            ),
            validator: (value) {
              if (value == null || value.isEmpty) {
                return '请输入密码';
              }
              if (value.length < 6) {
                return '密码至少6个字符';
              }
              return null;
            },
          ),
          const SizedBox(height: 24),
          // 提交按钮
          ElevatedButton(
            onPressed: _submit,
            child: const Text('登录'),
          ),
        ],
      ),
    );
  }

  void _submit() {
    // 验证表单
    if (_formKey.currentState?.validate() ?? false) {
      // 验证通过
      print('用户名: ${_usernameController.text}');
      print('密码: ${_passwordController.text}');
      // 提交到服务器...
    } else {
      // 验证失败
      print('表单验证失败');
    }
  }
}
```


---


## 常用验证器


## 实例：常用验证规则


```
// 验证用户名
String? validateUsername(String? value) {
  if (value == null || value.isEmpty) {
    return '请输入用户名';
  }
  if (!RegExp(r'^[a-zA-Z0-9_]+$').hasMatch(value)) {
    return '只能包含字母、数字和下划线';
  }
  return null;
}

// 验证邮箱
String? validateEmail(String? value) {
  if (value == null || value.isEmpty) {
    return '请输入邮箱';
  }
  final emailRegex = RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$');
  if (!emailRegex.hasMatch(value)) {
    return '请输入有效的邮箱地址';
  }
  return null;
}

// 验证密码强度
String? validatePassword(String? value) {
  if (value == null || value.isEmpty) {
    return '请输入密码';
  }
  if (value.length < 8) {
    return '密码至少8个字符';
  }
  if (!RegExp(r'[A-Z]').hasMatch(value)) {
    return '密码至少包含一个大写字母';
  }
  if (!RegExp(r'[0-9]').hasMatch(value)) {
    return '密码至少包含一个数字';
  }
  return null;
}

// 验证手机号
String? validatePhone(String? value) {
  if (value == null || value.isEmpty) {
    return '请输入手机号';
  }
  final phoneRegex = RegExp(r'^1[3-9]\d{9}$');
  if (!phoneRegex.hasMatch(value)) {
    return '请输入有效的手机号';
  }
  return null;
}

// 验证两次密码一致
String? validateConfirmPassword(String? value, String password) {
  if (value == null || value.isEmpty) {
    return '请确认密码';
  }
  if (value != password) {
    return '两次密码不一致';
  }
  return null;
}
```


---


## 复杂表单示例


## 实例：注册表单


```
class RegisterForm extends StatefulWidget {
  const RegisterForm({super.key});

  @override
  State<RegisterForm> createState() => _RegisterFormState();
}

class _RegisterFormState extends State<RegisterForm> {
  final _formKey = GlobalKey<FormState>();
  final _usernameController = TextEditingController();
  final _emailController = TextEditingController();
  final _phoneController = TextEditingController();
  final _passwordController = TextEditingController();
  final _confirmPasswordController = TextEditingController();

  bool _acceptTerms = false;

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // 用户名
          TextFormField(
            controller: _usernameController,
            decoration: const InputDecoration(labelText: '用户名'),
            validator: validateUsername,
          ),
          const SizedBox(height: 16),
          // 邮箱
          TextFormField(
            controller: _emailController,
            keyboardType: TextInputType.emailAddress,
            decoration: const InputDecoration(labelText: '邮箱'),
            validator: validateEmail,
          ),
          const SizedBox(height: 16),
          // 手机号
          TextFormField(
            controller: _phoneController,
            keyboardType: TextInputType.phone,
            decoration: const InputDecoration(labelText: '手机号'),
            validator: validatePhone,
          ),
          const SizedBox(height: 16),
          // 密码
          TextFormField(
            controller: _passwordController,
            obscureText: true,
            decoration: const InputDecoration(labelText: '密码'),
            validator: validatePassword,
          ),
          const SizedBox(height: 16),
          // 确认密码
          TextFormField(
            controller: _confirmPasswordController,
            obscureText: true,
            decoration: const InputDecoration(labelText: '确认密码'),
            validator: (value) => validateConfirmPassword(
              value,
              _passwordController.text,
            ),
          ),
          const SizedBox(height: 16),
          // 同意条款
          CheckboxListTile(
            value: _acceptTerms,
            onChanged: (value) {
              setState(() {
                _acceptTerms = value ?? false;
              });
            },
            title: const Text('我同意服务条款'),
            controlAffinity: ListTileControlAffinity.leading,
          ),
          const SizedBox(height: 24),
          // 提交按钮
          ElevatedButton(
            onPressed: _acceptTerms ? _submit : null,
            child: const Text('注册'),
          ),
        ],
      ),
    );
  }

  void _submit() {
    if (_formKey.currentState?.validate() ?? false) {
      // 提交表单
      print('注册成功！');
    }
  }

  @override
  void dispose() {
    _usernameController.dispose();
    _emailController.dispose();
    _phoneController.dispose();
    _passwordController.dispose();
    _confirmPasswordController.dispose();
    super.dispose();
  }
}
```


**

表单验证应该同时在客户端（用户体验）和服务器端（安全）进行，不要仅依赖客户端验证。










	  AI 思考中...





			** [Flutter 导航与路由](https://www.runoob.com/flutter-navigation.html)
			[Flutter 主题与样式](https://www.runoob.com/flutter-theming.html) **













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