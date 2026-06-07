# TypeScript 类继承与多态

- Source: https://www.runoob.com/typescript/ts-class-inheritance.html

TypeScript 支持面向对象编程的继承和多态特性。






  类继承层次结构



  Animal（父类）



Dog（子类） extends Animal Cat（子类） extends Animal Dog实例 Cat实例 继承特性 • extends 继承 • super() 调用 • 方法重写 • 多态 • instanceof --- ## 类的继承 使用 extends 关键字实现继承。


## 实例


```javascript
class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    speak(): void {
        console.log(this.name + " 发出声音");
    }
}

class Dog extends Animal {
    breed: string;

    constructor(name: string, breed: string) {
        super(name);  // 调用父类构造函数
        this.breed = breed;
    }

    speak(): void {
        console.log(this.name + " 汪汪汪!");
    }
}

var dog = new Dog("旺财", "金毛");
dog.speak();
```


**运行结果：**


```
旺财 汪汪汪!
```


---


## super 关键字


super 用于调用父类的方法和构造函数。


## 实例


```javascript
class Shape {
    color: string;

    constructor(color: string) {
        this.color = color;
    }

    describe(): string {
        return "这是一个 " + this.color + " 的图形";
    }
}

class Circle extends Shape {
    radius: number;

    constructor(color: string, radius: number) {
        super(color);
        this.radius = radius;
    }

    // 重写父类方法
    describe(): string {
        // 调用父类方法并扩展
        return super.describe() + "，半径是 " + this.radius;
    }

    area(): number {
        return Math.PI * this.radius * this.radius;
    }
}

var circle = new Circle("红色", 5);
console.log(circle.describe());
console.log("面积: " + circle.area().toFixed(2));
```


**运行结果：**


```
这是一个 红色的图形，半径是 5
面积: 78.54
```


---


## 多态


子类的实例可以赋值给父类类型。


## 实例


```javascript
class Animal {
    name: string;
    constructor(name: string) { this.name = name; }
    speak(): void {
        console.log(this.name + " 发出声音");
    }
}

class Cat extends Animal {
    speak(): void {
        console.log(this.name + " 喵喵喵!");
    }
}

class Dog extends Animal {
    speak(): void {
        console.log(this.name + " 汪汪汪!");
    }
}

// 多态：数组中存储不同子类的实例
var animals: Animal[] = [
    new Cat("小白"),
    new Dog("旺财"),
    new Animal("动物")
];

// 调用同一方法，不同子类有不同实现
for (var _i = 0, animals_1 = animals; _i < animals_1.length; _i++) {
    var animal = animals_1[_i];
    animal.speak();
}
```


**运行结果：**


```
小白 喵喵喵!
旺财 汪汪汪!
动物 发出声音
```


---


## instanceof 检查


使用 instanceof 检查实例类型。


## 实例


```javascript
class Rectangle {
    width: number;
    height: number;
    constructor(width: number, height: number) {
        this.width = width;
        this.height = height;
    }
    area(): number {
        return this.width * this.height;
    }
}

class Circle {
    radius: number;
    constructor(radius: number) {
        this.radius = radius;
    }
    area(): number {
        return Math.PI * this.radius ** 2;
    }
}

var shapes = [new Rectangle(4, 5), new Circle(3)];

for (var _i = 0, shapes_1 = shapes; _i < shapes_1.length; _i++) {
    var shape = shapes_1[_i];
    if (shape instanceof Rectangle) {
        console.log("矩形面积: " + shape.area());
    } else if (shape instanceof Circle) {
        console.log("圆形面积: " + shape.area().toFixed(2));
    }
}
```


**运行结果：**


```
矩形面积: 20
圆形面积: 28.27
```


---


## protected 成员


protected 成员在子类中可见。


## 实例


```javascript
class Person {
    protected name: string;

    constructor(name: string) {
        this.name = name;
    }
}

class Employee extends Person {
    private department: string;

    constructor(name: string, department: string) {
        super(name);
        this.department = department;
    }

    public introduce(): string {
        // 可以访问 protected 成员
        return "我是 " + this.name + "，在 " + this.department + " 工作";
    }
}

var emp = new Employee("Alice", "技术部");
console.log(emp.introduce());

// console.log(emp.name); // 错误：protected 外部不可访问
```


**运行结果：**


```
我是 Alice，在 技术部 工作
```


---


## 总结


- **继承：**extends 关键字
- **super：**调用父类
- **多态：**同一接口不同实现
- **protected：**子类可见








	  AI 思考中...





			** [TypeScript 映射类型](https://www.runoob.com/ts-mapped-types.html)
			[TypeScript 错误处理](https://www.runoob.com/ts-error-handling.html) **













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