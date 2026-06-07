# 

- Source: https://www.runoob.com/typescript/ts-interface.html

TypeScript 接口

接口是一系列抽象方法的声明，是一些方法特征的集合，这些方法都应该是抽象的，需要由具体的类去实现，然后第三方就可以通过这组抽象方法调用，让具体的类执行具体的方法。


TypeScript 接口定义如下：


```
interface interface_name {
}
```


### 实例


以下实例中，我们定义了一个接口 IPerson，接着定义了一个变量 customer，它的类型是 IPerson。


customer 实现了接口 IPerson 的属性和方法。


## TypeScript


```javascript
interface IPerson {
    firstName:string,
    lastName:string,
    sayHi: ()=>string
}

var customer:IPerson = {
    firstName:"Tom",
    lastName:"Hanks",
    sayHi: ():string =>{return "Hi there"}
}

console.log("Customer 对象 ")
console.log(customer.firstName)
console.log(customer.lastName)
console.log(customer.sayHi())

var employee:IPerson = {
    firstName:"Jim",
    lastName:"Blakes",
    sayHi: ():string =>{return "Hello!!!"}
}

console.log("Employee  对象 ")
console.log(employee.firstName)
console.log(employee.lastName)
```


需要注意接口不能转换为 JavaScript。 它只是 TypeScript 的一部分。


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var customer = {
    firstName: "Tom",
    lastName: "Hanks",
    sayHi: function () { return "Hi there"; }
};
console.log("Customer 对象 ");
console.log(customer.firstName);
console.log(customer.lastName);
console.log(customer.sayHi());
var employee = {
    firstName: "Jim",
    lastName: "Blakes",
    sayHi: function () { return "Hello!!!"; }
};
console.log("Employee  对象 ");
console.log(employee.firstName);
console.log(employee.lastName);
```


输出结果为：


```
Customer 对象
Tom
Hanks
Hi there
Employee  对象
Jim
Blakes
```


---


## 联合类型和接口


以下实例演示了如何在接口中使用联合类型：


## TypeScript


```javascript
interface RunOptions {
    program:string;
    commandline:string[]|string|(()=>string);
}

// commandline 是字符串
var options:RunOptions = {program:"test1",commandline:"Hello"};
console.log(options.commandline)

// commandline 是字符串数组
options = {program:"test1",commandline:["Hello","World"]};
console.log(options.commandline[0]);
console.log(options.commandline[1]);

// commandline 是一个函数表达式
options = {program:"test1",commandline:()=>{return "**Hello World**";}};

var fn:any = options.commandline;
console.log(fn());
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
// commandline 是字符串
var options = { program: "test1", commandline: "Hello" };
console.log(options.commandline);
// commandline 是字符串数组
options = { program: "test1", commandline: ["Hello", "World"] };
console.log(options.commandline[0]);
console.log(options.commandline[1]);
// commandline 是一个函数表达式
options = { program: "test1", commandline: function () { return "**Hello World**"; } };
var fn = options.commandline;
console.log(fn());
```



输出结果为：


```
Hello
Hello
World
**Hello World**
```


---


## 接口和数组


接口中我们可以将数组的索引值和元素设置为不同类型，索引值可以是数字或字符串。


设置元素为字符串类型：


## 实例


```javascript
interface namelist {
   [index:number]:string
}

// 类型一致，正确
var list2:namelist = ["Google","Runoob","Taobao"]
// 错误元素 1 不是 string 类型
// var list2:namelist = ["Runoob",1,"Taobao"]
```


如果使用了其他类型会报错：


## 实例


```javascript
interface namelist {
   [index:number]:string
}

// 类型一致，正确
// var list2:namelist = ["Google","Runoob","Taobao"]
// 错误元素 1 不是 string 类型
var list2:namelist = ["John",1,"Bran"]
```


执行后报错如下，显示类型不一致：


```
test.ts:8:30 - error TS2322: Type 'number' is not assignable to type 'string'.

8 var list2:namelist = ["John",1,"Bran"]
                               ~

  test.ts:2:4
    2    [index:number]:string
         ~~~~~~~~~~~~~~~~~~~~~
    The expected type comes from this index signature.


Found 1 error.
```


## TypeScript


```javascript
interface ages {
   [index:string]:number
}

var agelist:ages;
 // 类型正确
agelist["runoob"] = 15

// 类型错误，输出  error TS2322: Type '"google"' is not assignable to type 'number'.
// agelist[2] = "google"
```


---


## 接口继承


接口继承就是说接口可以通过其他接口来扩展自己。


Typescript 允许接口继承多个接口。


继承使用关键字 **extends**。


单接口继承语法格式：


```
Child_interface_name extends super_interface_name
```


多接口继承语法格式：


```
Child_interface_name extends super_interface1_name, super_interface2_name,…,super_interfaceN_name
```


继承的各个接口使用逗号 **,** 分隔。


### 单继承实例


## TypeScript


```javascript
interface Person {
   age:number
}

interface Musician extends Person {
   instrument:string
}

var drummer = <Musician>{};
drummer.age = 27
drummer.instrument = "Drums"
console.log("年龄:  "+drummer.age)
console.log("喜欢的乐器:  "+drummer.instrument)
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var drummer = {};
drummer.age = 27;
drummer.instrument = "Drums";
console.log("年龄:  " + drummer.age);
console.log("喜欢的乐器:  " + drummer.instrument);
```



输出结果为：


```
年龄:  27
喜欢的乐器:  Drums
```


### 多继承实例


## TypeScript


```javascript
interface IParent1 {
    v1:number
}

interface IParent2 {
    v2:number
}

interface Child extends IParent1, IParent2 { }
var Iobj:Child = { v1:12, v2:23}
console.log("value 1: "+Iobj.v1+" value 2: "+Iobj.v2)
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var Iobj = { v1: 12, v2: 23 };
console.log("value 1: " + Iobj.v1 + " value 2: " + Iobj.v2);
```



输出结果为：


```
value 1: 12 value 2: 23
```










	  AI 思考中...





			** [TypeScript 联合类型](https://www.runoob.com/ts-union.html)
			[TypeScript 类](https://www.runoob.com/ts-class.html) **













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