# Java 构造方法

- Source: https://www.runoob.com/java/java-constructor.html

在 Java 中，构造方法（Constructor）是用于创建类的对象的特殊方法。


当使用 new 关键字创建对象时，构造方法会自动调用，用来初始化对象的属性。

**构造方法具有以下几个特点：**


- **与类名相同**：构造方法的名称必须与类名完全一致，包括大小写。这是构造方法的一个基本要求。
- **没有返回类型**：构造方法没有返回类型声明，即使是 `void` 也不写。这使得它与普通方法区分开来。
- **自动调用**：每次使用 `new` 创建对象时，构造方法会自动调用，以初始化对象的属性和状态。
- **不能直接调用**：构造方法只能通过 `new` 关键字在创建对象时调用，不能像普通方法那样直接调用。
- **支持重载**：可以为一个类定义多个构造方法，只要它们的参数列表不同。通过重载，可以创建不同的构造方法以适应不同的初始化需求。
- **默认构造方法**：如果没有定义任何构造方法，Java 会提供一个无参的默认构造方法。但一旦定义了任何其他构造方法，Java 不再提供默认构造方法。
- **`this` 关键字的使用**：在构造方法中可以使用 `this` 来引用当前对象的属性、方法，或调用另一个构造方法（必须是构造方法的第一行），以避免重复代码。
- **不能被继承，但可以被调用**：构造方法不能被子类继承，但子类可以使用 `super()` 来调用父类的构造方法，以便初始化继承的属性。
- **对象初始化保障**：构造方法的主要作用是初始化对象的属性和状态，保证对象在创建时处于一个合法的初始状态。


**构造方法的作用：**

- **初始化对象属性**：构造方法的主要作用是为对象的属性赋初值。
- **保证对象初始化的完整性**：在构造方法中可以设置默认值或必要参数，从而避免对象未完全初始化的问题。


---

## 构造方法的类型

Java 中的构造方法分为两种类型：**无参构造方法**和**有参构造方法**。


### 1、无参构造方法（默认构造方法）

如果一个类中没有定义任何构造方法，Java 会默认提供一个无参构造方法。例如：


## 实例


```java
public class Person {
    public Person() {
        System.out.println("Person对象已创建");
    }
}
```


- 在没有显式定义构造方法时，Java 自动提供一个默认的无参构造方法。
- 一旦定义了其他构造方法，Java 将不再提供默认构造方法。


### 2、有参构造方法

可以定义带有参数的构造方法，用来在创建对象时为属性赋值：


## 实例


```java
public class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```


调用有参构造方法时，可以为对象的属性进行初始化：


```
Person p = new Person("Alice", 25);
```


---


## 构造方法的重载

Java 支持构造方法的重载，即可以在同一个类中定义多个构造方法，只要参数列表不同即可。例如：


## 实例


```java
public class Person {
    String name;
    int age;

    public Person() {
        this.name = "Unknown";
        this.age = 0;
    }

    public Person(String name) {
        this.name = name;
        this.age = 0;
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```


创建对象时，Java 会根据传入的参数数量和类型自动选择匹配的构造方法：


```
Person p1 = new Person(); // 调用无参构造方法
Person p2 = new Person("Alice"); // 调用单参数构造方法
Person p3 = new Person("Bob", 30); // 调用双参数构造方法
```


---


## 构造方法中的 this 关键字

在构造方法中，this 关键字通常用于两种情况：

** 1、引用当前对象的属性或方法：**当构造方法的参数名与类属性名相同时，使用 this 来区分类属性和参数。例如：


## 实例


```java
public Person(String name, int age) {
    this.name = name; // this.name 表示类的属性
    this.age = age;
}
```


**2、调用另一个构造方法：**可以使用 this() 调用当前类的其他构造方法，常用于避免重复代码，但必须放在构造方法的第一行。


## 实例


```java
public Person(String name) {
    this(name, 0); // 调用另一个双参数的构造方法
}

public Person(String name, int age) {
    this.name = name;
    this.age = age;
}
```


构造方法是 Java 面向对象编程中非常重要的部分，通过使用构造方法可以有效控制对象的初始化过程，保证创建出的对象状态的完整性和一致性。








	  AI 思考中...





			** [Java 反射（Reflection）](https://www.runoob.com/java-reflection.html)
			[Java Cleaner 类](https://www.runoob.com/java-cleaner-class.html) **













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

      : ·[Java 实例](https://www.runoob.com/java-examples.html)





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