# JavaScript 类(class)

- Source: https://www.runoob.com/js/js-class-intro.html

**类是用于创建对象的模板。**


我们使用 class 关键字来创建一个类，类体在一对大括号 **{}** 中，我们可以在大括号 **{}** 中定义类成员的位置，如方法或构造函数。


每个类中包含了一个特殊的方法 **constructor()**，它是类的构造函数，这种方法用于创建和初始化一个由 **class** 创建的对象。


创建一个类的语法格式如下：


```javascript
class ClassName {
  constructor() { ... }
}
```


实例：


## 实例


```javascript
class Runoob {
  constructor(name, url) {
    this.name = name;
    this.url = url;
  }
}
```


以上实例创建了一个类，名为 "Runoob"。


类中初始化了两个属性： "name" 和 "url"。


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Chrome 49 | Edge 12 | Firefox 45 | Safari 9 | Opera 36 |
| Mar, 2016 | Jul, 2015 | Mar, 2016 | Oct, 2015 | Mar, 2016 |


## 使用类


定义好类后，我们就可以使用 **new** 关键字来创建对象：


## 实例


```javascript
class Runoob {
  constructor(name, url) {
    this.name = name;
    this.url = url;
  }
}

let site = new Runoob("菜鸟教程",  "https://www.runoob.com");
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_class_init)


创建对象时会自动调用构造函数方法 **constructor()**。


### 类表达式


类表达式是定义类的另一种方法。类表达式可以命名或不命名。命名类表达式的名称是该类体的局部名称。


## 实例


```javascript
// 未命名/匿名类
let Runoob = class {
  constructor(name, url) {
    this.name = name;
    this.url = url;
  }
};
console.log(Runoob.name);
// output: "Runoob"

// 命名类
let Runoob = class Runoob2 {
  constructor(name, url) {
    this.name = name;
    this.url = url;
  }
};
console.log(Runoob.name);
// 输出: "Runoob2"
```


构造方法


构造方法是一种特殊的方法：


- 构造方法名为 constructor()。
- 构造方法在创建新对象时会自动执行。
- 构造方法用于初始化对象属性。
- 如果不定义构造方法，JavaScript 会自动添加一个空的构造方法。


## 类的方法


我们使用关键字 class** 创建一个类，可以添加一个 **constructor()** 方法，然后添加任意数量的方法。


```javascript
class ClassName {
  constructor() { ... }
  method_1() { ... }
  method_2() { ... }
  method_3() { ... }
}
```


以下实例我们创建一个 "age" 方法，用于返回网站年龄：


## 实例


```javascript
class Runoob {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  age() {
    let date = new Date();
    return date.getFullYear() - this.year;
  }
}

let runoob = new Runoob("菜鸟教程", 2018);
document.getElementById("demo").innerHTML =
"菜鸟教程 " + runoob.age() + " 岁了。";
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_class_method)


我们还可以向类的方法发送参数：


## 实例


```javascript
class Runoob {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  age(x) {
    return x - this.year;
  }
}

let date = new Date();
let year = date.getFullYear();

let runoob = new Runoob("菜鸟教程", 2020);
document.getElementById("demo").innerHTML=
"菜鸟教程 " + runoob.age(year) + " 岁了。";
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_class_method2)


## 严格模式 "use strict"


类声明和类表达式的主体都执行在严格模式下。比如，构造函数，静态方法，原型方法，getter 和 setter 都在严格模式下执行。


如果你没有遵循严格模式，则会出现错误：


## 实例


```javascript
class Runoob {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  age() {
    // date = new Date();  // 错误
    let date = new Date(); // 正确
    return date.getFullYear() - this.year;
  }
}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_class_strict_mode)

下图实例使用类未声明的变量：


![](https://www.runoob.com/wp-content/uploads/2022/01/4C934A71-BA90-459B-A267-D28C73024B73.jpeg)


更多严格模式可以参考：[JavaScript 严格模式(use strict)](https://www.runoob.com/js-strict.html)


---

## 参考


### 类方法


| 方法 | 描述 |
| --- | --- |
| constructor() | 构造函数，用于创建和初始化类 |


### 类关键字


| 关键字 | 描述 |
| --- | --- |
| extends | 继承一个类 |
| static | 在类中定义一个静态方法 |
| super | 调用父类的构造方法 |









	  AI 思考中...





			** [Window postMessage() 方法](https://www.runoob.com/met-win-postmessage.html)
			[JavaScript 类继承](https://www.runoob.com/js-class-inheritance.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

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