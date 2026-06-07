# TypeScript 枚举（Enum）

- Source: https://www.runoob.com/typescript/ts-enum.html

枚举（Enum）是 TypeScript 中非常有用的特性，它允许我们定义一组命名常量。枚举可以使得代码更易读、更易维护，可以用有意义的名称替代"魔术数字"。


---


## 数字枚举


默认情况下，枚举从 0 开始编号。


## 实例


```javascript
enum Direction {
    Up,    // 0
    Down,  // 1
    Left,  // 2
    Right  // 3
}

var dir: Direction = Direction.Up;
console.log("方向: " + dir);
console.log("方向名称: " + Direction[0]);
```


**运行结果：**


```
方向: 0
方向名称: Up
```


---


## 手动赋值


可以手动为枚举成员指定值。


## 实例


```javascript
enum Status {
    Success = 1,
    Error = 2,
    Pending = 3
}

console.log("状态: " + Status.Success);
console.log("状态名称: " + Status[1]);
```


**运行结果：**运


```
状态: 1
状态名称: Success
```


---


## 字符串枚举


字符串枚举每个成员都必须有字符串字面量值。


## 实例


```javascript
enum Message {
    Success = "SUCCESS",
    Error = "ERROR",
    Warning = "WARNING"
}

console.log("消息: " + Message.Success);
```


**运行结果：**


```
消息: SUCCESS
```


---


## 常量枚举


使用 `const` 修饰的枚举会在编译时内联，生成更优化的代码。


## 实例


```javascript
const enum Color {
    Red = "RED",
    Green = "GREEN",
    Blue = "BLUE"
}

var favoriteColor: Color = Color.Red;
console.log("喜欢的颜色: " + favoriteColor);
```


---


## 异构枚举


枚举可以混合数字和字符串值，但不推荐使用。


## 实例


```javascript
enum BooleanLikeHeterogeneousEnum {
    No = 0,
    Yes = "YES"
}

console.log("值: " + BooleanLikeHeterogeneousEnum.No);
console.log("字符串值: " + BooleanLikeHeterogeneousEnum.Yes);
```


---


## 枚举成员类型


当枚举成员都是字面量值时，成员类型可以作为类型使用。


## 实例


```javascript
enum ShapeKind {
    Circle = "circle",
    Square = "square"
}

interface Circle {
    kind: ShapeKind.Circle;
    radius: number;
}

interface Square {
    kind: ShapeKind.Square;
    sideLength: number;
}

var c: Circle = {
    kind: ShapeKind.Circle,
    radius: 10
};

console.log("圆形: " + JSON.stringify(c));
```


---


## 运行时常量枚举


普通枚举在运行时保留为真实对象。


## 实例


```javascript
enum FileAccess {
    Read = 1 << 1,
    Write = 1 << 2,
    ReadWrite = Read | Write
}

console.log("文件访问: " + FileAccess.ReadWrite);
```


**运行结果：**


```
文件访问: 6
```


---


## 总结


- **数字枚举：**默认从 0 开始，可手动赋值
- **字符串枚举：**每个成员必须是字符串字面量
- **常量枚举：**使用 const，编译时内联
- **异构枚举：**混合数字和字符串，不推荐
- **成员类型：**字面量枚举成员可用作类型








	  AI 思考中...





			** [TypeScript 编译选项](https://www.runoob.com/ts-compiler-options.html)
			[TypeScript 类型推断](https://www.runoob.com/ts-inference.html) **













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