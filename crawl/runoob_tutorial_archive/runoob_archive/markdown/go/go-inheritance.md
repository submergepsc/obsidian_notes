# Go 继承

- Source: https://www.runoob.com/go/go-inheritance.html

在面向对象编程（OOP）中，继承是一种机制，允许一个类（子类）从另一个类（父类）继承属性和方法。通过继承，子类可以复用父类的代码，并且可以在不修改父类的情况下扩展或修改其行为。


Go 语言并不是一种传统的面向对象编程语言，它没有类和继承的概念。

Go 使用结构体（struct）和接口（interface）来实现类似的功能。


---


## Go 中的 "继承"


Go 语言没有传统面向对象语言中的类(class)和继承(inheritance)概念，而是通过组合(composition)和接口(interface)来实现类似的功能。


### 1. 组合（Composition）


组合是 Go 中实现代码复用的主要方式。通过将一个结构体嵌入到另一个结构体中，子结构体可以"继承"父结构体的字段和方法。


## 实例


```go
package main

import "fmt"

// 父结构体
type Animal struct {
    Name string
}

// 父结构体的方法
func (a *Animal) Speak() {
    fmt.Println(a.Name, "says hello!")
}

// 子结构体
type Dog struct {
    Animal // 嵌入 Animal 结构体
    Breed  string
}

func main() {
    dog := Dog{
        Animal: Animal{Name: "Buddy"},
        Breed:  "Golden Retriever",
    }

    dog.Speak() // 调用父结构体的方法
    fmt.Println("Breed:", dog.Breed)
}
```


#### 代码解释


- `Animal` 是父结构体，包含一个字段 `Name` 和一个方法 `Speak`。
- `Dog` 是子结构体，通过嵌入 `Animal` 结构体，继承了 `Animal` 的字段和方法。
- 在 `main` 函数中，我们创建了一个 `Dog` 实例，并调用了 `Speak` 方法。


---


### 2. 接口（Interface）


接口是 Go 中实现多态的主要方式。通过定义接口，不同的结构体可以实现相同的方法，从而实现类似继承的多态行为。


#### 示例代码


## 实例


```go
package main

import "fmt"

// 定义接口
type Speaker interface {
    Speak()
}

// 父结构体
type Animal struct {
    Name string
}

// 实现接口方法
func (a *Animal) Speak() {
    fmt.Println(a.Name, "says hello!")
}

// 子结构体
type Dog struct {
    Animal
    Breed string
}

func main() {
    var speaker Speaker

    dog := Dog{
        Animal: Animal{Name: "Buddy"},
        Breed:  "Golden Retriever",
    }

    speaker = &dog
    speaker.Speak() // 通过接口调用方法
}
```


#### 代码解释


- `Speaker` 是一个接口，定义了一个 `Speak` 方法。
- `Animal` 结构体实现了 `Speaker` 接口。
- `Dog` 结构体通过嵌入 `Animal` 结构体，间接实现了 `Speaker` 接口。
- 在 `main` 函数中，我们将 `Dog` 实例赋值给 `Speaker` 接口，并通过接口调用 `Speak` 方法。


### Go 与经典继承的区别


| 特性 | 经典继承 | Go 的方式 |
| --- | --- | --- |
| 代码复用 | 通过继承 | 通过组合(嵌入结构体) |
| 多态 | 通过继承和方法重写 | 通过接口实现 |
| 关系 | "是一个"(is-a)关系 | "有一个"(has-a)或"实现了"关系 |
| 灵活性 | 继承关系固定 | 可以运行时组合 |


** 完整继承模拟：**


## 实例


```go
package main

import "fmt"

// 基类
type Vehicle struct {
    Brand string
}

func (v *Vehicle) Start() {
    fmt.Println(v.Brand, "started")
}

// 派生类
type Car struct {
    Vehicle // 嵌入Vehicle
    Model  string
}

// 重写Start方法
func (c *Car) Start() {
    fmt.Println(c.Brand, c.Model, "car started")
}

func main() {
    v := Vehicle{Brand: "Toyota"}
    c := Car{
        Vehicle: Vehicle{Brand: "Honda"},
        Model:  "Civic",
    }

    v.Start() // Toyota started
    c.Start() // Honda Civic car started
    c.Vehicle.Start() // Honda started
}
```


Go 的这种设计避免了传统继承的许多问题，如脆弱的基类问题，同时提供了更大的灵活性。








	  AI 思考中...





			** [Go 类型断言](https://www.runoob.com/go-type-assertion.html)
			[Go 语言泛型](https://www.runoob.com/go-generics.html) **













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