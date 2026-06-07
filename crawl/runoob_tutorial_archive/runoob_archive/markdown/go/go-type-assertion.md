# Go 类型断言

- Source: https://www.runoob.com/go/go-type-assertion.html

在 Go 语言中，类型断言（Type Assertion）是一种用于检查接口值的实际类型的机制。


类型断言是 Go 语言中处理接口类型的重要工具，它允许我们从接口值中提取出具体的类型，并对其进行操作。


类型断言通常用于处理接口类型的变量，因为接口变量可以存储任何实现了该接口的具体类型的值。


### 基本语法


类型断言的基本语法如下：


```
value, ok := interfaceValue.(Type)
```


- `interfaceValue` 是一个接口类型的变量。
- `Type` 是你想要断言的类型。
- `value` 是断言成功后的具体类型的值。
- `ok` 是一个布尔值，表示断言是否成功。


如果断言成功，`value` 将是 `interfaceValue` 的实际值，`ok` 为 `true`；如果断言失败，`value` 将是 `Type` 的零值，`ok` 为 `false`。


## 实例


```go
package main

import "fmt"

func main() {
    var i interface{} = "Hello, Go!"

    // 尝试将 i 断言为 string 类型
    s, ok := i.(string)
    if ok {
        fmt.Println("断言成功:", s)
    } else {
        fmt.Println("断言失败")
    }

    // 尝试将 i 断言为 int 类型
    n, ok := i.(int)
    if ok {
        fmt.Println("断言成功:", n)
    } else {
        fmt.Println("断言失败")
    }
}
```


### 输出结果


```
断言成功: Hello, Go!
断言失败
```


---


## 类型断言的另一种形式


除了上述的 `value, ok := interfaceValue.(Type)` 形式，Go 还支持另一种形式的类型断言，它不返回布尔值，而是直接在断言失败时引发 panic。

这种形式的语法如下：


```
value := interfaceValue.(Type)
```


### 示例代码


## 实例


```go
package main

import "fmt"

func main() {
    var i interface{} = "Hello, Go!"

    // 直接断言为 string 类型
    s := i.(string)
    fmt.Println("断言成功:", s)

    // 直接断言为 int 类型（会引发 panic）
    n := i.(int)
    fmt.Println("断言成功:", n)
}
```


### 输出结果


```
断言成功: Hello, Go!
panic: interface conversion: interface {} is string, not int
```


---


## 类型断言的常见用途


### 1. 处理多种类型的接口值


Go 还提供了特殊的 **type switch** 语法来测试多种类型：


```
switch v := i.(type) {
case T1:
    // v的类型是T1
case T2:
    // v的类型是T2
default:
    // 默认情况
}
```


当接口变量可能存储多种类型的值时，类型断言可以帮助我们根据实际类型执行不同的操作。


## 实例


```go
func printType(i interface{}) {
    switch v := i.(type) {
    case int:
        fmt.Println("这是一个整数:", v)
    case string:
        fmt.Println("这是一个字符串:", v)
    default:
        fmt.Println("未知类型")
    }
}
```


### 2. 从接口中提取具体类型


在处理接口类型的变量时，我们可能需要将其转换为具体的类型以便进行进一步的操作。


## 实例


```go
func processInterface(i interface{}) {
    if s, ok := i.(string); ok {
        fmt.Println("处理字符串:", s)
    } else if n, ok := i.(int); ok {
        fmt.Println("处理整数:", n)
    } else {
        fmt.Println("无法处理的类型")
    }
}
```


---


## 注意事项


- **类型断言只能用于接口类型**：类型断言只能用于接口类型的变量，不能用于非接口类型的变量。
- **避免 panic**：在使用不返回布尔值的类型断言时，务必确保类型断言不会失败，否则会引发 panic。
- **类型断言的性能**：类型断言在运行时进行类型检查，因此可能会带来一定的性能开销。在性能敏感的场景中，应谨慎使用。









	  AI 思考中...





			** [Go 语言正则表达式](https://www.runoob.com/go-regex.html)
			[Go 继承](https://www.runoob.com/go-inheritance.html) **













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