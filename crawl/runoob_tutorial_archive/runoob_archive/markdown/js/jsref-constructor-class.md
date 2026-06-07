# JavaScript 类(class) constructor() 方法

- Source: https://www.runoob.com/js/jsref-constructor-class.html

[![JavaScript 类(class)](https://www.runoob.com/images/up.gif) JavaScript 类(class)](https://www.runoob.com/js-class-intro.html)

---


## 实例


## 实例


创建了一个类，名为 "Runoob"，并初始化该类:


```javascript
class Runoob {
    constructor(name, url) {
        this.name = name;
        this.url = url;
    }
}
let site = new Runoob("菜鸟教程",  "https://www.runoob.com");
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_class_init)


---


## 定义和用法


constructor() 方法是一种特殊的方法(构造方法)，用于创建和初始化在类中创建的对象。


创建对象时会自动调用构造方法 constructor()。


如果没有显式指定构造方法，则会添加默认的 constructor 方法。


如果不指定一个构造函数 (constructor) 方法，则使用一个默认的构造函数 (constructor)。

在一个构造方法中可以使用 super 关键字来调用一个父类的构造方法。


## 语法


```
constructor(parameters)
```


---


## 技术细节


| JavaScript 版本: | ECMAScript 2015 (ES6) |
| --- | --- |


## 浏览器支持

constructor() 是 ECMAScript6 (ES6) 特性。

ES6 (JavaScript 2015) 支持目前所有主流的浏览器。


|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Chrome | Edge | Firefox | Safari | Opera |
| Yes | Yes | Yes | Yes | Yes |

Internet Explorer 11 或更旧版本的 IE 不支持 constructor() 方法。





---

[![JavaScript 类(class)](https://www.runoob.com/images/up.gif) JavaScript 类(class)](https://www.runoob.com/js-class-intro.html)







	  AI 思考中...





			** [JavaScript 静态方法](https://www.runoob.com/js-class-static.html)
			[JavaScript 类(class) extends 关键字](https://www.runoob.com/jsref-class-extends.html) **













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