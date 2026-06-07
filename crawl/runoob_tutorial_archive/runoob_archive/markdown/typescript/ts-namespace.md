# TypeScript 命名空间

- Source: https://www.runoob.com/typescript/ts-namespace.html

命名空间一个最明确的目的就是解决重名问题。


假设这样一种情况，当一个班上有两个名叫小明的学生时，为了明确区分它们，我们在使用名字之外，不得不使用一些额外的信息，比如他们的姓（王小明，李小明），或者他们父母的名字等等。


命名空间定义了标识符的可见范围，一个标识符可在多个命名空间中定义，它在不同命名空间中的含义是互不相干的。这样，在一个新的命名空间中可定义任何标识符，它们不会与任何已有的标识符发生冲突，因为已有的定义都处于其他命名空间中。


TypeScript 中命名空间使用 **namespace** 来定义，语法格式如下：


```javascript
namespace SomeNameSpaceName {
   export interface ISomeInterfaceName {      }
   export class SomeClassName {      }
}
```


以上定义了一个命名空间 SomeNameSpaceName，如果我们需要在外部可以调用 SomeNameSpaceName 中的类和接口，则需要在类和接口添加 **export** 关键字。


要在另外一个命名空间调用语法格式为：


```
SomeNameSpaceName.SomeClassName;
```


如果一个命名空间在一个单独的 TypeScript 文件中，则应使用三斜杠 /// 引用它，语法格式如下：


```
/// <reference path = "SomeFileName.ts" />
```


以下实例演示了命名空间的使用，定义在不同文件中：


## IShape.ts 文件代码：


```javascript
namespace Drawing {
    export interface IShape {
        draw();
    }
}
```


## Circle.ts 文件代码：


```javascript
/// <reference path = "IShape.ts" />
namespace Drawing {
    export class Circle implements IShape {
        public draw() {
            console.log("Circle is drawn");
        }
    }
}
```


## Triangle.ts 文件代码：


```javascript
/// <reference path = "IShape.ts" />
namespace Drawing {
    export class Triangle implements IShape {
        public draw() {
            console.log("Triangle is drawn");
        }
    }
}
```


## TestShape.ts 文件代码：


```javascript
/// <reference path = "IShape.ts" />
/// <reference path = "Circle.ts" />
/// <reference path = "Triangle.ts" />
function drawAllShapes(shape:Drawing.IShape) {
    shape.draw();
}
drawAllShapes(new Drawing.Circle());
drawAllShapes(new Drawing.Triangle());
```


使用 tsc 命令编译以上代码：


```
tsc --out app.js TestShape.ts
```


得到以下 JavaScript 代码：


## JavaScript


```javascript
/// <reference path = "IShape.ts" />
var Drawing;
(function (Drawing) {
    var Circle = /** @class */ (function () {
        function Circle() {
        }
        Circle.prototype.draw = function () {
            console.log("Circle is drawn");
        };
        return Circle;
    }());
    Drawing.Circle = Circle;
})(Drawing || (Drawing = {}));
/// <reference path = "IShape.ts" />
var Drawing;
(function (Drawing) {
    var Triangle = /** @class */ (function () {
        function Triangle() {
        }
        Triangle.prototype.draw = function () {
            console.log("Triangle is drawn");
        };
        return Triangle;
    }());
    Drawing.Triangle = Triangle;
})(Drawing || (Drawing = {}));
/// <reference path = "IShape.ts" />
/// <reference path = "Circle.ts" />
/// <reference path = "Triangle.ts" />
function drawAllShapes(shape) {
    shape.draw();
}
drawAllShapes(new Drawing.Circle());
drawAllShapes(new Drawing.Triangle());
```


使用 node 命令查看输出结果为：


```
$ node app.js
Circle is drawn
Triangle is drawn
```


---

## 嵌套命名空间


命名空间支持嵌套，即你可以将命名空间定义在另外一个命名空间里头。


```javascript
namespace namespace_name1 {
    export namespace namespace_name2 {
        export class class_name {    }
    }
}
```


成员的访问使用点号 **.** 来实现，如下实例：


## Invoice.ts 文件代码：


```javascript
namespace Runoob {
   export namespace invoiceApp {
      export class Invoice {
         public calculateDiscount(price: number) {
            return price * .40;
         }
      }
   }
}
```


## InvoiceTest.ts 文件代码：


```javascript
/// <reference path = "Invoice.ts" />
var invoice = new Runoob.invoiceApp.Invoice();
console.log(invoice.calculateDiscount(500));
```


使用 tsc 命令编译以上代码：


```
tsc --out app.js InvoiceTest.ts
```


得到以下 JavaScript 代码：


## JavaScript


```javascript
var Runoob;
(function (Runoob) {
    var invoiceApp;
    (function (invoiceApp) {
        var Invoice = /** @class */ (function () {
            function Invoice() {
            }
            Invoice.prototype.calculateDiscount = function (price) {
                return price * .40;
            };
            return Invoice;
        }());
        invoiceApp.Invoice = Invoice;
    })(invoiceApp = Runoob.invoiceApp || (Runoob.invoiceApp = {}));
})(Runoob || (Runoob = {}));
/// <reference path = "Invoice.ts" />
var invoice = new Runoob.invoiceApp.Invoice();
console.log(invoice.calculateDiscount(500));
```


使用 node 命令查看输出结果为：


```
$ node app.js
200
```









	  AI 思考中...





			** [TypeScript 对象](https://www.runoob.com/ts-object.html)
			[TypeScript 模块](https://www.runoob.com/ts-module.html) **













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