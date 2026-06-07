# Go 语言指针

- Source: https://www.runoob.com/go/go-pointers.html

Go 语言中指针是很容易学习的，Go 语言中使用指针可以更简单的执行一些任务。


接下来让我们来一步步学习 Go 语言指针。


我们都知道，变量是一种使用方便的占位符，用于引用计算机内存地址。


Go 语言的取地址符是 &，放到一个变量前使用就会返回相应变量的内存地址。


以下实例演示了变量在内存中地址：


## 实例


```go
package main

import "fmt"

func main() {
   var a int = 10

   fmt.Printf("变量的地址: %x\n", &a  )
}
```


执行以上代码输出结果为：


```
变量的地址: 20818a220
```


现在我们已经了解了什么是内存地址和如何去访问它。接下来我们将具体介绍指针。


---


## 什么是指针


一个指针变量指向了一个值的内存地址。


类似于变量和常量，在使用指针前你需要声明指针。指针声明格式如下：


```
var var_name *var-type
```


var-type 为指针类型，var_name 为指针变量名，* 号用于指定变量是作为一个指针。以下是有效的指针声明：


```
var ip *int        /* 指向整型*/
var fp *float32    /* 指向浮点型 */
```


本例中这是一个指向 int 和 float32 的指针。


---


## 如何使用指针


指针使用流程：


- 定义指针变量。
- 为指针变量赋值。
- 访问指针变量中指向地址的值。


在指针类型前面加上 * 号（前缀）来获取指针所指向的内容。


## 实例


```go
package main

import "fmt"

func main() {
   var a int= 20   /* 声明实际变量 */
   var ip *int        /* 声明指针变量 */

   ip = &a  /* 指针变量的存储地址 */

   fmt.Printf("a 变量的地址是: %x\n", &a  )

   /* 指针变量的存储地址 */
   fmt.Printf("ip 变量储存的指针地址: %x\n", ip )

   /* 使用指针访问值 */
   fmt.Printf("*ip 变量的值: %d\n", *ip )
}
```


以上实例执行输出结果为：


```
a 变量的地址是: 20818a220
ip 变量储存的指针地址: 20818a220
*ip 变量的值: 20
```


---


## Go 空指针


当一个指针被定义后没有分配到任何变量时，它的值为 nil。


nil 指针也称为空指针。


nil在概念上和其它语言的null、None、nil、NULL一样，都指代零值或空值。


一个指针变量通常缩写为 ptr。


查看以下实例：


## 实例


```go
package main

import "fmt"

func main() {
   var  ptr *int

   fmt.Printf("ptr 的值为 : %x\n", ptr  )
}
```


以上实例输出结果为：


```
ptr 的值为 : 0
```


空指针判断：


```
if(ptr != nil)     /* ptr 不是空指针 */
if(ptr == nil)    /* ptr 是空指针 */
```


---


## Go指针更多内容


接下来我们将为大家介绍Go语言中更多的指针应用：


| 内容 | 描述 |
| --- | --- |
| Go 指针数组 | 你可以定义一个指针数组来存储地址 |
| Go 指向指针的指针 | Go 支持指向指针的指针 |
| Go 向函数传递指针参数 | 通过引用或地址传参，在函数调用时可以改变其值 |








	  AI 思考中...





			** [Go 语言向函数传递数组](https://www.runoob.com/go-passing-arrays-to-functions.html)
			[Go 语言指针数组](https://www.runoob.com/go-array-of-pointers.html) **













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