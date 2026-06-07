# TypeScript 工具类型

- Source: https://www.runoob.com/typescript/ts-utility-types.html

工具类型（Utility Types）是 TypeScript 内置的一系列高级类型。


它们可以帮助开发者快速创建和转换类型，提高代码的可复用性和类型安全性。


工具类型本质上是泛型类型，通过映射类型和条件类型实现。


---







    TypeScript 工具类型




  原始类型


    interface User {
    id: number;
    name: string;
    email: string;
    }




工具类型 Partial - 所有可选 Required - 所有必填 Readonly - 所有只读 Pick - 选择属性 Omit - 排除属性 结果类型 type Result = { id?: number; name?: string; email?: string; } 常用工具类型 Partial 属性全部可选 { a?: T } Required 属性全部必填 { -? } Readonly 属性全部只读 { readonly } Pick 选择指定属性 { pick } Record 构造对象类型 Omit 排除指定属性 --- ## 为什么需要工具类型 在实际的 TypeScript 开发中，我们经常需要基于现有类型创建新的类型。


手动创建这些类型不仅繁琐，而且容易出错。


工具类型提供了一种声明式的方式来转换和创建类型，大大提高了开发效率。


**
概念说明：**工具类型是 TypeScript 预定义的一系列泛型类型。它们使用映射类型和条件类型来实现类型的转换和生成。


---


## Partial - 可选属性


Partial 将类型 T 的所有属性设置为可选。


这在创建部分更新对象或处理表单数据时非常有用。


## 实例


```javascript
// 定义用户接口，包含必填属性
interface User {
    // 用户 ID
    id: number;
    // 用户名
    name: string;
    // 用户邮箱
    email: string;
}

// Partial：将所有属性变为可选
// 转换后的类型所有属性都是可选的
type PartialUser = Partial<User>;

// 使用 PartialUser 类型
// 可以只提供部分属性，不需要全部提供
var user: PartialUser = { name: "Alice" };

console.log("部分用户: " + JSON.stringify(user));
```


**运行结果：**


```
部分用户: {"name":"Alice"}
```


**
应用场景：**Partial 常用于更新对象数据。例如：只更新用户的一部分信息时，不需要传入完整的用户对象。


---


## Required - 必填属性


Required 与 Partial 相反，将所有可选属性设置为必填。


当需要确保对象包含所有属性时使用。


## 实例


```javascript
// 定义配置接口，属性都是可选的
interface Config {
    // 服务器地址
    host?: string;
    // 端口号
    port?: number;
}

// Required：将所有可选属性变为必填
// 转换后的类型所有属性都是必填的
type RequiredConfig = Required<Config>;

// 使用 RequiredConfig 类型
// 必须提供所有属性
var config: RequiredConfig = { host: "localhost", port: 8080 };

console.log("配置: " + JSON.stringify(config));
```


**运行结果：**


```
配置: {"host":"localhost","port":8080}
```


**
说明：**Required 不仅移除可选属性（?），还会移除 readonly 修饰符。


---


## Readonly - 只读属性


Readonly 将所有属性设置为只读。


创建后不允许修改的 对象时非常有用。


## 实例


```javascript
// 定义用户接口
interface User {
    // 用户名
    name: string;
    // 用户年龄
    age: number;
}

// Readonly：将所有属性变为只读
// 转换后的类型所有属性都不能修改
type ReadonlyUser = Readonly<User>;

// 创建只读用户对象
var user: ReadonlyUser = { name: "Alice", age: 25 };

// 尝试修改只读属性会报错
// user.name = "Bob"; // 错误：只读属性不能修改

console.log("只读用户: " + JSON.stringify(user));
```


**
应用场景：**Readonly 常用于定义配置对象、枚举值映射等不希望被修改的数据。


---


## Pick - 选择属性


Pick 从类型 T 中选择指定的属性 K 组成新类型。


当你只需要某个类型的部分属性时使用。


## 实例


```javascript
// 定义完整的用户接口
interface User {
    // 用户 ID
    id: number;
    // 用户名
    name: string;
    // 用户邮箱
    email: string;
    // 用户密码
    password: string;
}

// Pick：选择指定的属性组成新类型
// 从 User 中选择 id 和 name 属性
type UserBasicInfo = Pick<User, "id" | "name">;

// 使用选择后的类型
var user: UserBasicInfo = { id: 1, name: "Alice" };

console.log("用户基本信息: " + JSON.stringify(user));
```


**运行结果：**


```
用户基本信息: {"id":1,"name":"Alice"}
```


**
对比：**Pick 和 Partial 结合使用，可以创建只包含部分可选属性的类型。


---


## Omit - 排除属性


Omit 从类型 T 中排除指定的属性 K，返回剩余属性组成的新类型。


与 Pick 相反，用于删除不需要的属性。


## 实例


```javascript
// 定义完整的用户接口
interface User {
    // 用户 ID
    id: number;
    // 用户名
    name: string;
    // 用户邮箱
    email: string;
    // 用户密码
    password: string;
}

// Omit：排除指定的属性
// 从 User 中排除 password 属性
type UserWithoutPassword = Omit<User, "password">;

// 使用排除后的类型
var user: UserWithoutPassword = { id: 1, name: "Alice", email: "[email protected]" };

console.log("无密码用户: " + JSON.stringify(user));
```


**运行结果：**


```
无密码用户: {"id":1,"name":"Alice","email":"[email protected]"}
```


**
提示：**Omit 是 Pick 的反向操作。当你需要排除少数属性时用 Omit，需要选择少数属性时用 Pick。


---


## Record - 构造对象类型


Record 构造一个对象类型，键的类型为 K，值的类型为 T。


常用于创建键值对映射、字典类型等。


## 实例


```javascript
// 定义角色类型
type Role = "admin" | "user" | "guest";

// Record：构造对象类型
// 键为 Role 类型，值为字符串数组类型
type RolePermissions = Record<Role, string[]>;

// 使用 Record 创建权限映射
var permissions: RolePermissions = {
    // 管理员拥有所有权限
    admin: ["read", "write", "delete"],
    // 普通用户拥有读写权限
    user: ["read", "write"],
    // 访客只有读权限
    guest: ["read"]
};

console.log("管理员权限: " + permissions.admin);
console.log("访客权限: " + permissions.guest);
```


**运行结果：**


```
管理员权限: read,write,delete
访客权限: read
```


**
应用场景：**Record 常用于创建配置映射、状态映射、权限映射等需要根据键快速查找值的场景。


---


## Exclude - 排除类型


Exclude 从类型 T 中排除可以赋值给类型 U 的类型。


主要用于联合类型，排除特定的类型成员。


## 实例


```javascript
// 定义联合类型，包含 a、b、c、d
type T = "a" | "b" | "c" | "d";

// Exclude：从 T 中排除指定类型
// 排除 "a"、"b"、"c"，只保留 "d"
type NonABC = Exclude<T, "a" | "b" | "c">;

// 使用排除后的类型，只能赋值 "d"
var value: NonABC = "d";

console.log("值: " + value);
```


**运行结果：**


```
值: d
```


**
说明：**Exclude 的原理是：如果 T 中的某个类型可以赋值给 U，就从 T 中移除它。


---


## Extract - 提取类型


Extract 与 Exclude 相反，从类型 T 中提取可以赋值给类型 U 的类型。


用于筛选联合类型中的特定成员。


## 实例


```javascript
// 定义混合联合类型，包含字符串和数字
type T = "a" | "b" | "c" | 1 | 2 | 3;

// Extract：从 T 中提取指定类型
// 提取所有字符串类型："a"、"b"、"c"
type Letters = Extract<T, string>;

// 使用提取后的类型
var letter: Letters = "a";

console.log("字母: " + letter);
```


**运行结果：**


```
字母: a
```


**
对比：**Extract 和 Exclude 是互补的。Extract(T, U) 等价于 Exclude(T, Exclude)。


---


## NonNullable - 排除空值


NonNullable 从类型 T 中排除 null 和 undefined。


确保类型不包含空值时使用。


## 实例


```javascript
// 定义混合类型，包含字符串、null、undefined、数字
type T = string | null | undefined | number;

// NonNullable：排除 null 和 undefined
// 转换后只保留 string 和 number
type NotNull = NonNullable<T>;

// 使用非空类型
var value: NotNull = "hello";
value = 42;

// 尝试赋值 null 会报错
// value = null; // 错误：不能赋值 null

console.log("值: " + value);
```


**
说明：**NonNullable 等价于 Exclude。


---


## ReturnType - 获取返回类型


ReturnType 获取函数类型 T 的返回类型。


常用于从已存在的函数中提取返回类型。


## 实例


```javascript
// 定义获取用户的函数
function getUser() {
    return { name: "Alice", age: 25 };
}

// 定义获取配置的函数
function getConfig() {
    return { host: "localhost", port: 8080 };
}

// ReturnType：获取函数的返回类型
// 提取 getUser 函数的返回类型
type UserType = ReturnType<typeof getUser>;
// 提取 getConfig 函数的返回类型
type ConfigType = ReturnType<typeof getConfig>;

// 使用提取的返回类型创建对象
var user: UserType = { name: "Bob", age: 30 };
var config: ConfigType = { host: "example.com", port: 3000 };

console.log("用户: " + JSON.stringify(user));
console.log("配置: " + JSON.stringify(config));
```


**运行结果：**


```
用户: {"name":"Bob","age":30}
配置: {"host":"example.com","port":3000}
```


**
提示：**ReturnType 中的 T 必须是函数类型。可以使用 typeof 获取函数的类型。


---


## 注意事项


- **工具类型都是泛型：**使用时应传入具体的类型参数
- **只读和可选：**工具类型可以组合使用，如 Partial>
- **内置类型：**这些工具类型都是 TypeScript 内置的，无需安装
- **自定义工具类型：**可以基于映射类型和条件类型创建自定义工具类型


**
进阶：**如果内置工具类型不满足需求，可以参考 TypeScript 源码自行实现自定义工具类型。


---


## 总结


TypeScript 工具类型是类型系统的重要组成部分。


- **Partial：**将所有属性变为可选
- **Required：**将所有属性变为必填
- **Readonly：**将所有属性变为只读
- **Pick：**选择指定属性
- **Omit：**排除指定属性
- **Record：**构造对象类型
- **Exclude/Extract：**类型过滤
- **NonNullable：**排除 null 和 undefined
- **ReturnType：**获取函数返回类型


**
最佳实践：**善用工具类型可以使代码更加类型安全，减少重复的类型定义，提高代码可维护性。


---









	  AI 思考中...





			** [TypeScript 可选链](https://www.runoob.com/ts-optional-chaining.html)
			[TypeScript 条件类型](https://www.runoob.com/ts-conditional-types.html) **













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