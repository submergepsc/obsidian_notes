# JavaScript 类(class) super 关键字

- Source: https://www.runoob.com/js/jsref-class-super.html

[![JavaScript 类(class)](https://www.runoob.com/images/up.gif) JavaScript 类(class)](https://www.runoob.com/js-class-intro.html)


---


## 实例


## 实例


以下实例创建的类 "Runoob"，并使用 super 调用父类 "Site" 的构造方法 :


```javascript
class Site {
  constructor(name) {
    this.sitename = name;
  }
  present() {
    return '我喜欢' + this.sitename;
  }
}

class Runoob extends Site {
  constructor(name, age) {
    super(name);
    this.age = age;
  }
  show() {
    return this.present() + ', 它创建了 ' + this.age + ' 年。';
  }
}

let noob = new Runoob("菜鸟教程", 5);
document.getElementById("demo").innerHTML = noob.show();
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_classes_inherit)


---


## 定义和用法


super 关键字用于访问和调用一个对象的父对象上的函数。。


在构造函数中使用时，super关键字将单独出现，并且必须在使用 this 关键字之前使用。super 关键字也可以用来调用父对象上的函数。


## 语法


```
super(arguments);  // 调用父构造函数
  super.parentMethod(arguments);  // 调用父方法
```


## 技术细节


| JavaScript 版本: | ECMAScript 2015 (ES6) |
| --- | --- |


## 浏览器支持


super 是 ECMAScript6 (ES6) 特性。


目前所有主流浏览器都支持 ES6 (JavaScript 2015) 。


|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Chrome | Edge | Firefox | Safari | Opera |
| Yes | Yes | Yes | Yes | Yes |


Internet Explorer 11 或更旧版本的 IE 不支持 super 关键字。


---

## 更多实例


在类中使用 super：


## 实例


```javascript
class Polygon {
  constructor(height, width) {
    this.name = 'Rectangle';
    this.height = height;
    this.width = width;
  }
  sayName() {
    return 'Hi, I am a ' + this.name + '.';
  }
  get area() {
    return this.height * this.width;
  }
  set area(value) {
    this._area = value;
  }
}

class Square extends Polygon {
  constructor(length) {
    // 这里，它调用父类的构造函数的，
    // 作为 Polygon 的 height, width
    super(length, length);

    this.height; // 需要放在 super 后面，不然引发 ReferenceErro

    // 注意：在派生的类中，在你可以使用'this'之前，必须先调用 super()。
    // 忽略这，这将导致引用错误。
    this.name = 'Square';
  }
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_classes_inherit2)


用 super 调用父类的静态方法：


## 实例


```javascript
class Rectangle {
  constructor() {}
  static logNbSides() {
    return 'I have 4 sides';
  }
}

class Square extends Rectangle {
  constructor() {}
  static logDescription() {
    return super.logNbSides() + ' which are all equal';
  }
}
Square.logDescription(); // 'I have 4 sides which are all equal'
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_classes_inherit3)


---


[![JavaScript 类(class)](https://www.runoob.com/images/up.gif) JavaScript 类(class)](https://www.runoob.com/js-class-intro.html)








	  AI 思考中...





			** [JavaScript 类(class) static 关键字](https://www.runoob.com/jsref-class-static.html)
			[JavaScript 模板字符串](https://www.runoob.com/js-string-templates.html) **













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