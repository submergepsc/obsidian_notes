# Kotlin 枚举类

- Source: https://www.runoob.com/kotlin/kotlin-enum-classes.html

枚举类最基本的用法是实现一个类型安全的枚举。


枚举常量用逗号分隔,每个枚举常量都是一个对象。


```
enum class Color{
    RED,BLACK,BLUE,GREEN,WHITE
}
```


### 枚举初始化


每一个枚举都是枚举类的实例，它们可以被初始化：


```
enum class Color(val rgb: Int) {
    RED(0xFF0000),
    GREEN(0x00FF00),
    BLUE(0x0000FF)
}
```


默认名称为枚举字符名，值从0开始。若需要指定值，则可以使用其构造函数：


```
enum class Shape(value:Int){
    ovel(100),
    rectangle(200)
}
```


枚举还支持以声明自己的匿名类及相应的方法、以及覆盖基类的方法。如：


```
enum class ProtocolState {
    WAITING {
        override fun signal() = TALKING
    },

    TALKING {
        override fun signal() = WAITING
    };

    abstract fun signal(): ProtocolState
}
```


如果枚举类定义任何成员，要使用分号将成员定义中的枚举常量定义分隔开


---


## 使用枚举常量


Kotlin 中的枚举类具有合成方法，允许遍历定义的枚举常量，并通过其名称获取枚举常数。


```
EnumClass.valueOf(value: String): EnumClass  // 转换指定 name 为枚举值，若未匹配成功，会抛出IllegalArgumentException
EnumClass.values(): Array<EnumClass>        // 以数组的形式，返回枚举值
```


获取枚举相关信息：


```
val name: String //获取枚举名称
val ordinal: Int //获取枚举值在所有枚举数组中定义的顺序
```


### 实例


```
enum class Color{
    RED,BLACK,BLUE,GREEN,WHITE
}

fun main(args: Array<String>) {
    var color:Color=Color.BLUE

    println(Color.values())
    println(Color.valueOf("RED"))
    println(color.name)
    println(color.ordinal)

}
```


自 Kotlin 1.1 起，可以使用 `enumValues()` 和 `enumValueOf()` 函数以泛型的方式访问枚举类中的常量 ：


```
enum class RGB { RED, GREEN, BLUE }

inline fun <reified T : Enum<T>> printAllValues() {
    print(enumValues<T>().joinToString { it.name })
}


fun main(args: Array<String>) {
    printAllValues<RGB>() // 输出 RED, GREEN, BLUE
}
```









	  AI 思考中...





			** [Kotlin 泛型](https://www.runoob.com/kotlin-generics.html)
			[Kotlin 对象表达式和对象声明](https://www.runoob.com/kotlin-object-declarations.html) **













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