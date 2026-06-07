# Go 语言正则表达式

- Source: https://www.runoob.com/go/go-regex.html

正则表达式（Regular Expression，简称 regex 或 regexp）是一种用于匹配字符串的强大工具。

正则表达式通过定义一种模式（pattern），可以快速搜索、替换或提取符合该模式的字符串，详细可以参见[正则表达式教程](https://www.runoob.com/../regexp/regexp-tutorial.html)。

在 Go 语言中，正则表达式通过 `regexp` 包来实现。


---


## Go 语言中的 regexp 包


Go 语言的标准库提供了 `regexp` 包，用于处理正则表达式。以下是 `regexp` 包中常用的函数和方法：


- **`Compile` 和 `MustCompile`** 用于编译正则表达式。`Compile` 返回一个 `*Regexp` 对象和一个错误，而 `MustCompile` 在编译失败时会直接 panic。
- **`MatchString`** 检查字符串是否匹配正则表达式。
- **`FindString` 和 `FindAllString`** 用于查找匹配的字符串。`FindString` 返回第一个匹配项，`FindAllString` 返回所有匹配项。
- **`ReplaceAllString`** 用于替换匹配的字符串。
- **`Split`** 根据正则表达式分割字符串。


---


## 正则表达式的基本语法


以下是一些常用的正则表达式语法：


- `.`：匹配任意单个字符（除了换行符）。
- `*`：匹配前面的字符 0 次或多次。
- `+`：匹配前面的字符 1 次或多次。
- `?`：匹配前面的字符 0 次或 1 次。
- `\d`：匹配数字字符（等价于 `[0-9]`）。
- `\w`：匹配字母、数字或下划线（等价于 `[a-zA-Z0-9_]`）。
- `\s`：匹配空白字符（包括空格、制表符、换行符等）。
- `[]`：匹配括号内的任意一个字符（例如 `[abc]` 匹配 `a`、`b` 或 `c`）。
- `^`：匹配字符串的开头。
- `$`：匹配字符串的结尾。


---


## 示例代码


以下是一些使用 Go 语言正则表达式的示例：


### 示例 1：检查字符串是否匹配正则表达式


## 实例


```go
package main

import (
    "fmt"
    "regexp"
)

func main() {
    pattern := `^[a-zA-Z0-9]+$`
    regex := regexp.MustCompile(pattern)

    str := "Hello123"
    if regex.MatchString(str) {
        fmt.Println("字符串匹配正则表达式")
    } else {
        fmt.Println("字符串不匹配正则表达式")
    }
}
```


### 示例 2：查找匹配的字符串


## 实例


```go
package main

import (
    "fmt"
    "regexp"
)

func main() {
    pattern := `\d+`
    regex := regexp.MustCompile(pattern)

    str := "我有 3 个苹果和 5 个香蕉"
    matches := regex.FindAllString(str, -1)
    fmt.Println("找到的数字：", matches)
}
```


### 示例 3：替换匹配的字符串


## 实例


```go
package main

import (
    "fmt"
    "regexp"
)

func main() {
    pattern := `\s+`
    regex := regexp.MustCompile(pattern)

    str := "Hello    World"
    result := regex.ReplaceAllString(str, " ")
    fmt.Println("替换后的字符串：", result)
}
```


### 示例 4：分割字符串


## 实例


```go
package main

import (
    "fmt"
    "regexp"
)

func main() {
    pattern := `,`
    regex := regexp.MustCompile(pattern)

    str := "apple,banana,orange"
    parts := regex.Split(str, -1)
    fmt.Println("分割后的字符串：", parts)
}
```


---


## 注意事项


- **性能问题** 正则表达式的匹配和替换操作可能会消耗较多资源，尤其是在处理大量数据时。建议在性能敏感的场景下谨慎使用。
- **转义字符** 在 Go 语言中，正则表达式中的反斜杠 `\` 需要写成 `\\`，因为反斜杠在字符串中也是转义字符。
- **错误处理** 使用 `Compile` 函数时，务必检查返回的错误，以避免程序崩溃。









	  AI 思考中...





			** [Go 语言文件处理](https://www.runoob.com/go-file-handle.html)
			[Go 类型断言](https://www.runoob.com/go-type-assertion.html) **













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