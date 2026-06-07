# TypeScript 装饰器

- Source: https://www.runoob.com/typescript/ts-decorators.html

装饰器（Decorators）是 TypeScript 的一项实验性功能。


它允许开发者在不修改原类的情况下，为类、方法、属性或参数添加额外的功能。


装饰器本质上是一个函数，它可以在运行时被调用，以修改目标对象的行为。






  装饰器类型与应用位置



  @ClassDecorator
  类装饰器



属性装饰器 @propertyDecorator 方法装饰器 @methodDecorator 参数装饰器 @paramDecorator 访问器装饰器 @getterDecorator 装饰器工厂（Decorator Factory） 装饰器工厂是返回装饰器函数的函数，通过参数实现配置化 例如：function color(code: string) { return function(target) { ... }; } → @color("34") --- ## 装饰器简介 装饰器采用 `@` 符号作为语法糖，可以附加在类、方法、访问器、属性或参数上。


这种模式常用于框架开发，如 Angular、TypeORM 等都大量使用装饰器来实现依赖注入、数据验证等功能。


**
注意：**装饰器目前是实验性功能，需要在 tsconfig.json 中显式启用。在生产环境中使用时请确认项目对实验性特性的支持程度。


---


## 配置启用装饰器


在使用装饰器之前，需要在 TypeScript 配置文件 tsconfig.json 中启用相关编译选项。


## tsconfig.json 配置


```javascript
{
    "compilerOptions": {
        // 启用装饰器语法
        "experimentalDecorators": true,

        // 启用装饰器元数据（用于依赖注入框架）
        "emitDecoratorMetadata": true
    }
}
```


**参数说明：**


- **experimentalDecorators：**启用装饰器语法支持，这是使用装饰器的前提条件
- **emitDecoratorMetadata：**在编译后的 JavaScript 中生成装饰器的元数据，供依赖注入框架使用


---


## 类装饰器


类装饰器应用于类的构造函数，可以修改类的定义或添加额外的处理逻辑。


类装饰器接收一个参数，即目标类的构造函数。


## 类装饰器基本用法


```javascript
// 定义一个类装饰器函数
// 参数 target 就是被装饰的类构造函数
function sealed(target: Function) {
    // 打印装饰器被应用到的类名
    console.log("装饰器 applied to: " + target.name);

    // 使用 Object.seal 锁定构造函数和原型
    // 防止在运行时添加或删除属性
    Object.seal(target);
    Object.seal(target.prototype);
}

// 使用 @ 语法将装饰器应用到类上
@sealed
class Person {
    name: string;

    constructor(name: string) {
        this.name = name;
    }
}

// 创建实例测试
var person = new Person("RUNOOB");
console.log("创建: " + person.name);

// 尝试添加新属性（会被阻止，因为类被 seal 了）
// person.age = 25; // 静默失败
```


**运行结果：**


```
装饰器 applied to: Person
创建: RUNOOB
```


**说明：**


类装饰器在类定义时就会执行，通常用于修改类行为、添加元数据或实现 AOP（面向切面编程）。


---


## 方法装饰器


方法装饰器应用于类的方法，可以修改方法的属性描述符（Property Descriptor）。


方法装饰器接收三个参数：目标对象、属性名称和属性描述符。


## 方法装饰器基本用法


```javascript
// 定义方法装饰器工厂
// 返回一个装饰器函数
function enumerable(value: boolean) {
    // 返回装饰器函数，接收三个参数
    return function (
        target: any,           // 所属类的原型对象
        propertyKey: string,    // 方法名称
        descriptor: PropertyDescriptor // 属性描述符
    ) {
        // 修改属性的 enumerable 特性
        // false 表示该方法不可遍历
        descriptor.enumerable = value;
    };
}

class Greeter {
    greeting: string;

    constructor(message: string) {
        this.greeting = message;
    }

    // 应用装饰器，设置该方法为不可枚举
    @enumerable(false)
    greet() {
        return "Hello, " + this.greeting;
    }
}

var g = new Greeter("World");

// 检查 greet 方法是否可枚举
console.log("方法可枚举: " + g.propertyIsEnumerable("greet"));

// 遍历对象的属性
for (var key in g) {
    console.log("属性: " + key);
}
```


**运行结果：**


```
方法可枚举: false
```


**
提示：**PropertyDescriptor 包含可枚举（enumerable）、可配置（configurable）、可写（writable）和值（value）等属性，可以根据需要修改。


---


## 访问器装饰器


访问器装饰器应用于类的 getter 和 setter 方法。


与方法装饰器类似，访问器装饰器也可以修改属性描述符。


## 访问器装饰器用法


```javascript
// 访问器装饰器工厂
function configurable(value: boolean) {
    return function (
        target: any,
        propertyKey: string,
        descriptor: PropertyDescriptor
    ) {
        // 修改属性的 configurable 特性
        // false 表示该访问器不可被重新配置或删除
        descriptor.configurable = value;
    };
}

class Point {
    private _x: number = 0;
    private _y: number = 0;

    // 使用装饰器锁定 getter
    @configurable(false)
    get x() {
        return this._x;
    }

    @configurable(false)
    get y() {
        return this._y;
    }

    set x(value: number) {
        this._x = value;
    }

    set y(value: number) {
        this._y = value;
    }
}

var point = new Point();
point.x = 10;
point.y = 20;
console.log("坐标: (" + point.x + ", " + point.y + ")");
```


**说明：**


访问器装饰器不能同时应用于同一个属性的 getter 和 setter，只能选择其中一个。


---


## 属性装饰器


属性装饰器应用于类的属性定义。


属性装饰器接收两个参数：目标对象和属性名称。


## 属性装饰器用法


```javascript
// 属性装饰器工厂
function format(formatString: string) {
    return function (
        target: any,           // 类的原型对象
        propertyKey: string     // 属性名称
    ) {
        // 在目标对象上存储元数据
        // 使用 propertyKey + "_format" 作为键名避免冲突
        Object.defineProperty(target, propertyKey + "_format", {
            value: formatString,
            writable: false,
            enumerable: false,
            configurable: true
        });
    };
}

class User {
    // 应用属性装饰器，指定日期格式
    @format("YYYY-MM-DD")
    birthDate: string;

    constructor(birthDate: string) {
        this.birthDate = birthDate;
    }
}

var user = new User("1990-01-01");
console.log("出生日期: " + user.birthDate);

// 访问存储的元数据
console.log("日期格式: " + (user as any).birthDate_format);
```


**运行结果：**


```
出生日期: 1990-01-01
日期格式: YYYY-MM-DD
```


---


## 参数装饰器


参数装饰器应用于类方法的参数，可以为参数添加元数据或标记。


参数装饰器接收三个参数：目标对象、方法名称和参数在函数中的索引。


## 参数装饰器用法


```javascript
// 参数装饰器
// 用于记录参数信息或进行验证
function logParameter(
    target: any,               // 类的原型对象
    propertyKey: string,       // 方法名称
    parameterIndex: number    // 参数在函数中的索引位置（从 0 开始）
) {
    console.log("参数装饰器: " + propertyKey +
        " 第 " + (parameterIndex + 1) + " 个参数");
}

class Greeter {
    greeting: string;

    constructor(greeting: string) {
        this.greeting = greeting;
    }

    // 在参数前使用 @ 语法应用装饰器
    greet(@logParameter name: string) {
        return this.greeting + ", " + name;
    }
}

var greeter = new Greeter("Hello");
greeter.greet("RUNOOB");
```


**运行结果：**


```
参数装饰器: greet 第 1 个参数
```


---


## 装饰器工厂


装饰器工厂是返回装饰器函数的函数。


通过装饰器工厂，可以在应用装饰器时传入自定义参数，实现更灵活的配置。


## 装饰器工厂实现带颜色的日志


```javascript
// 装饰器工厂：接收配置参数，返回装饰器函数
function color(colorCode: string) {
    // colorCode 是 ANSI 转义序列的颜色代码
    // 例如：34 = 蓝色，31 = 红色，32 = 绿色
    return function (
        target: any,
        propertyKey: string,
        descriptor: PropertyDescriptor
    ) {
        // 保存原始方法
        var originalMethod = descriptor.value;

        // 重写方法，添加颜色
        descriptor.value = function (...args: any[]) {
            // 调用原始方法获取返回值
            var result = originalMethod.apply(this, args);

            // 如果在终端环境，给输出添加颜色
            // ANSI 转义序列格式：\x1b[颜色码m 内容 \x1b[0m
            return "\x1b[" + colorCode + "m" + result + "\x1b[0m";
        };
    };
}

class Logger {
    // 使用装饰器工厂，传入蓝色代码 34
    @color("34")
    log(message: string): string {
        return message;
    }

    @color("31")
    error(message: string): string {
        return message;
    }

    @color("32")
    success(message: string): string {
        return message;
    }
}

var logger = new Logger();
console.log(logger.log("这是蓝色日志"));
console.log(logger.error("这是红色错误"));
console.log(logger.success("这是绿色成功"));
```


**运行结果：**


```
这是蓝色日志（终端显示为蓝色）
这是红色错误（终端显示为红色）
这是绿色成功（终端显示为绿色）
```


**
说明：**装饰器工厂是实际开发中最常用的形式，它允许在应用装饰器时传递参数，实现配置化。


---


## 装饰器执行顺序


当一个类上有多个装饰器时，执行顺序遵循特定的规则。


- 装饰器从下往上应用
- 同一类型的多个装饰器从右到左执行
- 参数装饰器先于方法装饰器执行


## 装饰器执行顺序示例


```javascript
// 多个装饰器叠加使用
function first() {
    console.log("first 装饰器");
    return function (target: any) {
        console.log("first 装饰器函数");
    };
}

function second() {
    console.log("second 装饰器");
    return function (target: any) {
        console.log("second 装饰器函数");
    };
}

@first()
@second()
class MyClass {
    name: string;
}

var obj = new MyClass();
```


**运行结果：**


```
second 装饰器
first 装饰器
second 装饰器函数
first 装饰器函数
```


**说明：**


装饰器函数先执行定义（console.log），然后按照从下往上的顺序执行装饰器函数。


---


## 实际应用场景


装饰器在实际项目中有广泛的应用场景。


### 日志记录


自动记录方法调用日志。


## 实例


```javascript
// 日志装饰器
function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    var originalMethod = descriptor.value;

    descriptor.value = function (...args: any[]) {
        console.log("调用方法: " + propertyKey + "，参数: " + JSON.stringify(args));
        var result = originalMethod.apply(this, args);
        console.log("方法返回: " + JSON.stringify(result));
        return result;
    };
}

class MathService {
    @log
    add(a: number, b: number): number {
        return a + b;
    }

    @log
    multiply(a: number, b: number): number {
        return a * b;
    }
}

var math = new MathService();
console.log("计算结果: " + math.add(5, 3));
```


**运行结果：**


```
调用方法: add，参数: [5,3]
方法返回: 8
计算结果: 8
```


### 权限验证


实现方法级别的权限检查。


## 实例


```javascript
// 模拟当前用户角色
var currentUser = { role: "admin" };

// 权限装饰器
function requireRole(role: string) {
    return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        var originalMethod = descriptor.value;

        descriptor.value = function (...args: any[]) {
            if (currentUser.role !== role) {
                console.log("权限不足，无法执行 " + propertyKey);
                return null;
            }
            return originalMethod.apply(this, args);
        };
    };
}

class AdminService {
    @requireRole("admin")
    deleteUser(id: number): string {
        return "删除用户 " + id + " 成功";
    }

    @requireRole("admin")
    viewUser(id: number): string {
        return "查看用户 " + id;
    }
}

var admin = new AdminService();
console.log(admin.viewUser(1));
console.log(admin.deleteUser(1));

// 模拟普通用户
currentUser = { role: "user" };
console.log(admin.deleteUser(2));
```


**运行结果：**


```
查看用户 1
删除用户 1 成功
权限不足，无法执行 deleteUser
```


---


## 注意事项


- **实验性功能：**装饰器是 ECMAScript 的_stage 3_提案，当前仍是实验性功能
- **编译选项：**必须启用 experimentalDecorators
- **类型定义：**需要较新版本的 TypeScript 以获得完整的类型支持
- **调试注意：**装饰器在编译时执行，某些调试工具可能无法正确映射源码位置


**
建议：**在项目中使用装饰器时，建议创建专门的装饰器工具类或函数库，统一管理装饰器的定义和使用。


---


## 总结


TypeScript 装饰器提供了一种强大的元编程能力。


- **类装饰器：**修改类本身，可用于添加元数据、锁定类等
- **方法装饰器：**修改方法属性，可用于日志、验证等
- **访问器装饰器：**修改 getter/setter，控制属性的可配置性
- **属性装饰器：**为属性添加元数据
- **参数装饰器：**标记或验证方法参数
- **装饰器工厂：**通过参数化实现更灵活的装饰器配置


---









	  AI 思考中...





			** [TypeScript 混入（Mixin）](https://www.runoob.com/ts-mixin.html)
			[TypeScript 类型守卫](https://www.runoob.com/ts-type-guards.html) **













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