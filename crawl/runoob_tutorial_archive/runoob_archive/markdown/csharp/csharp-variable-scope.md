# C# 变量作用域

- Source: https://www.runoob.com/csharp/csharp-variable-scope.html

在 C# 中，变量的作用域定义了变量的可见性和生命周期。

变量的作用域通常由花括号 **{}** 定义的代码块来确定。


以下是关于C#变量作用域的一些基本规则：


### 局部变量

在方法、循环、条件语句等代码块内声明的变量是局部变量，它们只在声明它们的代码块中可见。


## 实例


```csharp
void MyMethod()
{
    int localVar = 10; // 局部变量
    // ...
}
// localVar 在这里不可见
```


### 块级作用域

在 C# 7及更高版本中，引入了块级作用域，即使用大括号 **{}** 创建的任何块都可以定义变量的作用域。


## 实例


```csharp
{
    int blockVar = 20; // 块级作用域
    // ...
}
// blockVar 在这里不可见
```


### 方法参数作用域

方法的参数也有其自己的作用域，它们在整个方法中都是可见的。


## 实例


```csharp
void MyMethod(int parameter)
{
    // parameter 在整个方法中可见
    // ...
}
```


### 全局变量

在类的成员级别定义的变量是成员变量，它们在整个类中可见，如果在命名空间级别定义，那么它们在整个命名空间中可见。


## 实例


```csharp
class MyClass
{
    int memberVar = 30; // 成员变量，在整个类中可见
}
```


### 静态变量作用域

静态变量是在类级别上声明的，但它们的作用域也受限于其定义的类。


## 实例


```csharp
class MyClass
{
    static int staticVar = 40; // 静态变量，在整个类中可见
}
```


### 循环变量作用域

在 for 循环中声明的循环变量在循环体内可见
。


## 实例


```csharp
for (int i = 0; i < 5; i++)
{
    // i 在循环体内可见
}
// i 在这里不可见
```


总体而言，变量的作用域有助于管理变量的可见性和生命周期，确保变量在其有效范围内使用，也有助于防止命名冲突。








	  AI 思考中...





			** [C# 语言测验](https://www.runoob.com/csharp-quiz.html)
			[C# AI 编程助手](https://www.runoob.com/fitten-code-csharp.html) **













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