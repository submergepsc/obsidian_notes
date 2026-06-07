# TypeScript 错误处理

- Source: https://www.runoob.com/typescript/ts-error-handling.html

错误处理是保证程序健壮性的重要环节。


TypeScript 提供了强大的类型系统，可以帮助开发者更好地处理和预防错误。


本文介绍 TypeScript 中常见的错误处理模式和最佳实践。


---






  错误处理方式



  try-catch

    try {
    // 可能出错的代码
    } catch (e) {
    // 处理错误
    }

  捕获并处理异常



  Result 类型

    type Result =
      | { ok: true; value: T }
      | { ok: false; error: E }

  返回结果而非抛异常



  自定义错误

    class AppError extends Error {
    code: string;
    }

  结构化错误信息



  最佳实践



  明确错误类型



  集中错误处理



  避免异常泄漏


---


## 为什么需要良好的错误处理


任何程序都可能遇到错误情况，如网络请求失败、文件不存在、用户输入错误等。


良好的错误处理可以防止程序崩溃，提供友好的错误提示，并帮助开发者定位问题。


TypeScript 的类型系统可以在编译阶段发现潜在问题，减少运行时错误。


**
概念说明：**错误处理有两种主要方式：异常处理（try-catch）和返回值处理（Result 类型）。前者使用抛出异常表示错误，后者使用返回值携带错误信息。


---


## 自定义错误类型


通过扩展 Error 类创建自定义错误类型，可以携带更多错误信息。


这使得错误处理更加精确和结构化。


## 实例


```javascript
// 定义应用程序错误类
// 扩展内置 Error 类，添加错误码
class AppError extends Error {
    // 错误码，用于程序化处理错误
    code: string;

    // 构造函数
    constructor(message: string, code: string) {
        super(message);  // 调用父类构造函数
        this.name = "AppError";  // 设置错误名称
        this.code = code;  // 保存错误码
    }
}

// 安全的除法函数
function divide(a: number, b: number): number {
    // 检查除数是否为零
    if (b === 0) {
        // 抛出自定义错误
        throw new AppError("Cannot divide by zero", "DIVIDE_BY_ZERO");
    }
    return a / b;
}

// 使用 try-catch 捕获错误
try {
    var result = divide(10, 0);
} catch (error) {
    // 检查错误类型
    if (error instanceof AppError) {
        console.log("应用错误: " + error.message + ", 代码: " + error.code);
    } else {
        console.log("未知错误: " + error);
    }
}
```


**运行结果：**


```
应用错误: Cannot divide by zero, 代码: DIVIDE_BY_ZERO
```


**
错误码：**为错误添加代码可以帮助程序更精确地处理不同类型的错误。


---


## Result 类型避免异常


另一种错误处理方式是使用 Result 类型。


它通过返回值携带错误信息，而不是抛出异常。这种方式在函数式编程中很常见。


## 实例


```javascript
// 定义 Result 类型，使用联合类型
// 成功时包含 ok: true 和值，失败时包含 ok: false 和错误
type Result<T, E = Error> =
    | { ok: true; value: T }
    | { ok: false; error: E };

// 使用 Result 类型的除法函数
function safeDivide(a: number, b: number): Result<number, string> {
    // 检查除数是否为零
    if (b === 0) {
        // 返回错误结果
        return { ok: false, error: "Cannot divide by zero" };
    }
    // 返回成功结果
    return { ok: true, value: a / b };
}

// 调用函数并处理结果
var result = safeDivide(10, 2);

// 根据结果类型进行处理
if (result.ok) {
    console.log("结果: " + result.value);
} else {
    console.log("错误: " + result.error);
}
```


**运行结果：**


```
结果: 5
```


**
优势：**Result 类型让错误处理变得显式，调用者必须处理可能的错误，而不会忽略它。


---


## Async 函数错误处理


在异步函数中，错误处理尤为重要。


可以使用 try-catch 或 Result 类型来处理异步操作中的错误。


## 实例


```javascript
// 定义用户接口
interface User {
    id: number;
    name: string;
}

// 模拟获取用户的异步函数
async function fetchUser(id: number): Promise<Result<User, Error>> {
    try {
        // 模拟网络请求
        var response = await fetch("/api/users/" + id);
        var user = await response.json();
        // 返回成功结果
        return { ok: true, value: user };
    } catch (error) {
        // 返回错误结果
        return { ok: false, error: error as Error };
    }
}

// 主函数
async function main() {
    // 调用异步函数
    var result = await fetchUser(1);

    // 处理结果
    if (result.ok) {
        console.log("用户: " + JSON.stringify(result.value));
    } else {
        console.log("错误: " + result.error.message);
    }
}

// 执行主函数
main();
```


**运行结果：**


```
用户: {"id":1,"name":"Alice"}
```


**
提示：**异步函数中的 try-catch 会捕获 await 表达式抛出的任何错误。


---


## 通用错误处理封装


可以创建一个通用的错误处理函数，简化异步代码的错误处理。


## 实例


```javascript
// 通用错误处理包装函数
// 接受一个异步函数，返回 Result 类型
async function withErrorHandling<T>(
    fn: () => Promise<T>
): Promise<Result<T, Error>> {
    try {
        // 执行传入的异步函数
        var data = await fn();
        // 返回成功结果
        return { ok: true, value: data };
    } catch (error) {
        // 返回错误结果
        return { ok: false, error: error as Error };
    }
}

// 使用通用错误处理
// 模拟获取数据
var result = await withErrorHandling(async function() {
    var response = await fetch("/api/data");
    return response.json();
});

// 根据结果处理
if (result.ok) {
    console.log("数据: " + JSON.stringify(result.value));
} else {
    console.error("错误:", result.error);
}
```


**
最佳实践：**封装通用的错误处理逻辑可以减少代码重复，提高代码可维护性。


---


## 注意事项


- **不要忽略错误：**不要使用空的 catch 块捕获并忽略错误
- **明确错误类型：**尽量使用具体的错误类型，而不是通用的 Error
- **错误边界：**在应用中建立统一的错误处理机制
- **不要过度使用异常：**对于可预期的错误，优先使用返回值而非抛异常


**
建议：**根据场景选择错误处理方式：程序错误用异常，业务错误用 Result。


---


## 总结


良好的错误处理是构建健壮应用的基础。


- **自定义错误：**扩展 Error 类，添加错误码等信息
- **Result 类型：**通过返回值处理错误，避免异常
- **async/await：**使用 try-catch 处理异步错误
- **错误封装：**创建通用错误处理函数
- **错误边界：**建立统一的错误处理机制


**
最佳实践：**根据具体场景选择合适的错误处理方式，平衡代码可读性和健壮性。


---









	  AI 思考中...





			** [TypeScript 类继承与多态](https://www.runoob.com/ts-class-inheritance.html)
			[TypeScript 交叉类型](https://www.runoob.com/ts-intersection-types.html) **













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