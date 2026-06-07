# TypeScript 对象

- Source: https://www.runoob.com/typescript/ts-object.html

对象是包含一组键值对的实例。 值可以是标量、函数、数组、对象等，如下实例：


```javascript
var object_name = {
    key1: "value1", // 标量
    key2: "value",
    key3: function() {
        // 函数
    },
    key4:["content1", "content2"] //集合
}
```


以上对象包含了标量，函数，集合(数组或元组)。


### 对象实例


## TypeScript


```javascript
var sites = {
   site1:"Runoob",
   site2:"Google"
};
// 访问对象的值
console.log(sites.site1)
console.log(sites.site2)
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var sites = {
   site1:"Runoob",
   site2:"Google"
};
// 访问对象的值
console.log(sites.site1)
console.log(sites.site2)
```


输出结果为：


```
Runoob
Google
```


---


## TypeScript 类型模板


假如我们在 JavaScript 定义了一个对象：


```javascript
var sites = {
   site1:"Runoob",
   site2:"Google"
};
```


这时如果我们想在对象中添加方法，可以做以下修改：


```
sites.sayHello = function(){ return "hello";}
```


如果在 TypeScript 中使用以上方式则会出现编译错误，因为Typescript 中的对象必须是特定类型的实例。


## TypeScript


```javascript
var sites = {
    site1: "Runoob",
    site2: "Google",
    sayHello: function () { } // 类型模板
};
sites.sayHello = function () {
    console.log("hello " + sites.site1);
};
sites.sayHello();
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var sites = {
    site1: "Runoob",
    site2: "Google",
    sayHello: function () { } // 类型模板
};
sites.sayHello = function () {
    console.log("hello " + sites.site1);
};
sites.sayHello();
```


输出结果为：


```
hello Runoob
```


此外对象也可以作为一个参数传递给函数，如下实例：


## TypeScript


```javascript
var sites = {
    site1:"Runoob",
    site2:"Google",
};
var invokesites = function(obj: { site1:string, site2 :string }) {
    console.log("site1 :"+obj.site1)
    console.log("site2 :"+obj.site2)
}
invokesites(sites)
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var sites = {
    site1: "Runoob",
    site2: "Google"
};
var invokesites = function (obj) {
    console.log("site1 :" + obj.site1);
    console.log("site2 :" + obj.site2);
};
invokesites(sites);
```


输出结果为：


```
site1 :Runoob
site2 :Google
```


---

## 鸭子类型(Duck Typing)

鸭子类型（英语：duck typing）是动态类型的一种风格，是多态(polymorphism)的一种形式。


在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定。


**
可以这样表述：


"当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。"


在鸭子类型中，关注点在于对象的行为能做什么，而不是关注对象所属的类型。例如，在不使用鸭子类型的语言中，我们可以编写一个函数，它接受一个类型为"鸭子"的对象，并调用它的"走"和"叫"方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的"走"和"叫"方法。如果这些需要被调用的方法不存在，那么将引发一个运行时错误。任何拥有这样的正确的"走"和"叫"方法的对象都可被函数接受的这种行为引出了以上表述，这种决定类型的方式因此得名。


```javascript
interface IPoint {
    x:number
    y:number
}
function addPoints(p1:IPoint,p2:IPoint):IPoint {
    var x = p1.x + p2.x
    var y = p1.y + p2.y
    return {x:x,y:y}
}

// 正确
var newPoint = addPoints({x:3,y:4},{x:5,y:1})

// 错误
var newPoint2 = addPoints({x:1},{x:4,y:3})
```










	  AI 思考中...





			** [TypeScript 类](https://www.runoob.com/ts-class.html)
			[TypeScript 命名空间](https://www.runoob.com/ts-namespace.html) **













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