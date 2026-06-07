# TypeScript 声明文件

- Source: https://www.runoob.com/typescript/ts-ambient.html

TypeScript 作为 JavaScript 的超集，在开发过程中不可避免要引用其他第三方的 JavaScript 的库。虽然通过直接引用可以调用库的类和方法，但是却无法使用TypeScript 诸如类型检查等特性功能。为了解决这个问题，需要将这些库里的函数和方法体去掉后只保留导出类型声明，而产生了一个描述 JavaScript 库和模块信息的声明文件。通过引用这个声明文件，就可以借用 TypeScript 的各种特性来使用库文件了。


假如我们想使用第三方库，比如 jQuery，我们通常这样获取一个 id 是 foo 的元素：


```
$('#foo');
// 或
jQuery('#foo');
```


但是在 TypeScript 中，我们并不知道 $ 或 jQuery 是什么东西：


```
jQuery('#foo');

// index.ts(1,1): error TS2304: Cannot find name 'jQuery'.
```


这时，我们需要使用 declare 关键字来定义它的类型，帮助 TypeScript 判断我们传入的参数类型对不对：


```
declare var jQuery: (selector: string) => any;

jQuery('#foo');
```


declare 定义的类型只会用于编译时的检查，编译结果中会被删除。


上例的编译结果是：


```
jQuery('#foo');
```


### 声明文件


声明文件以 **.d.ts** 为后缀，例如：


```
runoob.d.ts
```


声明文件或模块的语法格式如下：


```
declare module Module_Name {
}
```


TypeScript 引入声明文件语法格式：


```
/// <reference path = " runoob.d.ts" />
```


当然，很多流行的第三方库的声明文件不需要我们定义了，比如 jQuery 已经有人帮我们定义好了：[jQuery in DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/jquery/index.d.ts)。


### 实例


以下定义一个第三方库来演示：


## CalcThirdPartyJsLib.js 文件代码：


```javascript
var Runoob;
(function(Runoob) {
    var Calc = (function () {
        function Calc() {
        }
    })
    Calc.prototype.doSum = function (limit) {
        var sum = 0;

        for (var i = 0; i <= limit; i++) {
            sum = sum + i;
        }
        return sum;
    }
    Runoob.Calc = Calc;
    return Calc;
})(Runoob || (Runoob = {}));
var test = new Runoob.Calc();
```


如果我们想在 TypeScript 中引用上面的代码，则需要设置声明文件 Calc.d.ts，代码如下：


## Calc.d.ts 文件代码：


```javascript
declare module Runoob {
   export class Calc {
      doSum(limit:number) : number;
   }
}
```


声明文件不包含实现，它只是类型声明，把声明文件加入到 TypeScript 中：


## CalcTest.ts 文件代码：


```javascript
/// <reference path = "Calc.d.ts" />
var obj = new Runoob.Calc();
// obj.doSum("Hello"); // 编译错误
console.log(obj.doSum(10));
```


下面这行导致编译错误，因为我们需要传入数字参数：


```
obj.doSum("Hello");
```


使用 tsc 命令来编译以上代码文件：


```
tsc CalcTest.ts
```


生成的 JavaScript 代码如下：


## CalcTest.js 文件代码：


```javascript
/// <reference path = "Calc.d.ts" />
var obj = new Runoob.Calc();
//obj.doSum("Hello"); // 编译错误
console.log(obj.doSum(10));
```


最后我们编写一个 runoob.html 文件，引入 CalcTest.js 文件及第三方库 CalcThirdPartyJsLib.js：


## 实例


```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
<script src = "CalcThirdPartyJsLib.js"></script>
<script src = "CalcTest.js"></script>
</head>
<body>
    <h1>声明文件测试</h1>
    <p>菜鸟测试一下。</p>
</body>
</html>
```


浏览器打开该文件输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/01/847256CE-6F06-41FC-944E-EEB89176F358.jpg)









	  AI 思考中...





			** [TypeScript 模块](https://www.runoob.com/ts-module.html)
			[TypeScript Map 对象](https://www.runoob.com/ts-map.html) **













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