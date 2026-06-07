# TypeScript 混入（Mixin）

- Source: https://www.runoob.com/typescript/ts-mixin.html

混入（Mixin）是一种代码复用模式，用于将多个独立的功能模块混入到一个类中。

TypeScript 通过泛型函数返回扩展类的方式实现 Mixin，弥补了单继承无法复用多个来源行为的不足。






  Mixin 组合过程



  User 类



SerializableMixin + serialize() TimestampedMixin + timestamp 扩展后的类 Mixin 工作原理 1. Mixin 是函数 接收一个类，返回扩展后的新类 2. 继承而非修改 通过 extends 继承，不修改原类 3. 可叠加组合 多个 Mixin 可以嵌套组合使用 --- ## 基本概念 Mixin 的核心是一个接收基类、返回扩展类的泛型函数。`Constructor` 类型约束用于描述"任意可被继承的类"。


## 实例


```javascript
// Constructor 类型：描述任意可实例化的类
type Constructor<T = {}> = new (...args: any[]) => T;

// Mixin 函数：接收基类，返回扩展后的新类
function Timestamped<TBase extends Constructor>(Base: TBase) {
    return class extends Base {
        createdAt = new Date();
    };
}

// 基类
class User {
    constructor(public name: string) {}
}

// 混入后得到新类
const TimestampedUser = Timestamped(User);
const user = new TimestampedUser("Alice");

console.log(user.name);                        // Alice
console.log(user.createdAt instanceof Date);   // true
```


**运行结果：**


```
Alice
true
```


**
注意：**Mixin 不修改原始类，而是返回一个全新的扩展类，原始的 `User` 类不受影响。


---


## 组合多个 Mixin


将多个 Mixin 函数嵌套调用，即可将多份能力依次叠加到同一个类上。


## 实例


```javascript
type Constructor<T = {}> = new (...args: any[]) => T;

// Mixin 1：添加时间戳
function Timestamped<TBase extends Constructor>(Base: TBase) {
    return class extends Base {
        createdAt = new Date();
    };
}

// Mixin 2：添加序列化
function Serializable<TBase extends Constructor>(Base: TBase) {
    return class extends Base {
        serialize(): string {
            return JSON.stringify(this);
        }
    };
}

// Mixin 3：添加日志（依赖 serialize 方法）
function Loggable<TBase extends Constructor<{ serialize(): string }>>(Base: TBase) {
    return class extends Base {
        log(): void {
            console.log("[LOG]", this.serialize());
        }
    };
}

class Product {
    constructor(public name: string, public price: number) {}
}

// 依次叠加三个 Mixin
const AdvancedProduct = Loggable(Serializable(Timestamped(Product)));

const p = new AdvancedProduct("Phone", 999);
p.log();
console.log(p.createdAt instanceof Date);  // true
```


**运行结果：**


```
[LOG] {"name":"Phone","price":999,"createdAt":"2026-..."}
true
```


---


## Mixin 与接口结合


Mixin 返回的类可以声明实现某个接口，使消费方通过接口类型操作混入后的对象，而不依赖具体实现。


## 实例


```javascript
type Constructor<T = {}> = new (...args: any[]) => T;

// 定义能力接口
interface ISerializable {
    serialize(): string;
}

interface ICloneable<T> {
    clone(): T;
}

// Mixin 实现接口
function Serializable<TBase extends Constructor>(Base: TBase) {
    return class extends Base implements ISerializable {
        serialize(): string {
            return JSON.stringify(this);
        }
    };
}

function Cloneable<TBase extends Constructor>(Base: TBase) {
    return class extends Base {
        clone() {
            return Object.assign(
                Object.create(Object.getPrototypeOf(this)),
                this
            );
        }
    };
}

class Article {
    constructor(public title: string, public content: string) {}
}

const RichArticle = Cloneable(Serializable(Article));

const a1 = new RichArticle("TypeScript 入门", "正文内容...");
const a2 = a1.clone();
a2.title = "TypeScript 进阶";

console.log(a1.serialize());
// {"title":"TypeScript 入门","content":"正文内容..."}

console.log(a2.serialize());
// {"title":"TypeScript 进阶","content":"正文内容..."}

console.log(a1.title === a2.title);  // false（克隆后独立修改）
```


**运行结果：**


```
{"title":"TypeScript 入门","content":"正文内容..."}
{"title":"TypeScript 进阶","content":"正文内容..."}
false
```


---


## 带约束的 Mixin


通过泛型约束，可以限定 Mixin 只能混入满足特定条件的类，避免运行时缺少必要属性。


## 实例


```javascript
type Constructor<T = {}> = new (...args: any[]) => T;

// 约束：基类必须有 id 和 name 属性
type WithIdAndName = Constructor<{ id: number; name: string }>;

function Printable<TBase extends WithIdAndName>(Base: TBase) {
    return class extends Base {
        print(): void {
            console.log(`[${this.id}] ${this.name}`);
        }
    };
}

class Item {
    constructor(public id: number, public name: string) {}
}

// 正确：Item 满足约束
const PrintableItem = Printable(Item);
const item = new PrintableItem(42, "Keyboard");
item.print();  // [42] Keyboard

// 错误示例（编译器会阻止）：
// class NoId { constructor(public name: string) {} }
// const Bad = Printable(NoId);  // 错误：NoId 缺少 id 属性
```


**运行结果：**


```
[42] Keyboard
```


---


## Mixin 与继承的对比


| 维度 | 继承（extends） | Mixin |
| --- | --- | --- |
| 来源数量 | 只能继承一个父类 | 可叠加任意数量 |
| 耦合程度 | 子类与父类强耦合 | 每个 Mixin 独立，低耦合 |
| 复用粒度 | 复用整个类的能力 | 按需复用单一功能 |
| 类型安全 | 原生支持 | 需借助泛型约束保证 |
| 适用场景 | 强 "is-a" 关系 | 横切关注点（日志、序列化、缓存等） |


---


## 总结


- **核心模式：**Mixin 是接收基类、返回扩展类的泛型函数，`Constructor` 是标准约束类型
- **能力叠加：**嵌套调用多个 Mixin 函数即可将多份能力组合到同一个类
- **接口结合：**Mixin 返回的类可以实现接口，消费方只需依赖接口而非具体类
- **泛型约束：**通过约束 `TBase` 可以限定 Mixin 的适用范围，在编译期阻止错误使用
- **适用场景：**日志、序列化、克隆、时间戳等横切关注点，优于多层继承








	  AI 思考中...





			** [TypeScript 访问修饰符](https://www.runoob.com/ts-access-modifiers.html)
			[TypeScript 装饰器](https://www.runoob.com/ts-decorators.html) **













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