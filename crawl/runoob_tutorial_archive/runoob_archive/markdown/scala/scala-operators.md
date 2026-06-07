# Scala 运算符

- Source: https://www.runoob.com/scala/scala-operators.html

一个运算符是一个符号，用于告诉编译器来执行指定的数学运算和逻辑运算。

Scala 含有丰富的内置运算符，包括以下几种类型：


- 算术运算符
- 关系运算符
- 逻辑运算符
- 位运算符
- 赋值运算符


接下来我们将为大家详细介绍以上各种运算符的应用。


---


## 算术运算符


下表列出了 Scala 支持的算术运算符。


假定变量 A 为 10，B 为 20：


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| + | 加号 | A + B 运算结果为 30 |
| - | 减号 | A - B 运算结果为 -10 |
| * | 乘号 | A * B 运算结果为 200 |
| / | 除号 | B / A 运算结果为 2 |
| % | 取余 | B % A 运算结果为 0 |


### 实例


## 实例


```scala
object Test {
   def main(args: Array[String]) = {
      var a = 10;
      var b = 20;
      var c = 25;
      var d = 25;
      println("a + b = " + (a + b) );
      println("a - b = " + (a - b) );
      println("a * b = " + (a * b) );
      println("b / a = " + (b / a) );
      println("b % a = " + (b % a) );
      println("c % a = " + (c % a) );

   }
}
```

**[运行实例 »](https://www.runoob.com/try/runcode.php?filename=TestO&type=scala)


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
a + b = 30
a - b = -10
a * b = 200
b / a = 2
b % a = 0
c % a = 5
```


---


## 关系运算符


下表列出了 Scala 支持的关系运算符。

假定变量 A 为 10，B 为 20：


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| == | 等于 | (A == B) 运算结果为 false |
| != | 不等于 | (A != B) 运算结果为 true |
| > | 大于 | (A > B) 运算结果为 false |
| = | 大于等于 | (A >= B) 运算结果为 false |
| > | 右移动运算符 | a >> 2 输出结果 15 ，二进制解释： 0000 1111 |
| >>> | 无符号右移 | A >>>2 输出结果 15, 二进制解释: 0000 1111 |


### 实例


## 实例


```scala
object Test {
   def main(args: Array[String]) = {
      var a = 60;           /* 60 = 0011 1100 */
      var b = 13;           /* 13 = 0000 1101 */
      var c = 0;

      c = a & b;            /* 12 = 0000 1100 */
      println("a & b = " + c );

      c = a | b;            /* 61 = 0011 1101 */
      println("a | b = " + c );

      c = a ^ b;            /* 49 = 0011 0001 */
      println("a ^ b = " + c );

      c = ~a;               /* -61 = 1100 0011 */
      println("~a = " + c );

      c = a << 2;           /* 240 = 1111 0000 */
      println("a << 2 = " + c );

      c = a >> 2;           /* 15 = 1111 */
      println("a >> 2  = " + c );

      c = a >>> 2;          /* 15 = 0000 1111 */
      println("a >>> 2 = " + c );
   }
}
```


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
a & b = 12
a | b = 61
a ^ b = 49
~a = -61
a << 2 = 240
a >> 2  = 15
a >>> 2 = 15
```


---


## 赋值运算符


以下列出了 Scala 语言支持的赋值运算符:


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| = | 简单的赋值运算，指定右边操作数赋值给左边的操作数。 | C = A + B 将 A + B 的运算结果赋值给 C |
| += | 相加后再赋值，将左右两边的操作数相加后再赋值给左边的操作数。 | C += A 相当于 C = C + A |
| -= | 相减后再赋值，将左右两边的操作数相减后再赋值给左边的操作数。 | C -= A 相当于 C = C - A |
| *= | 相乘后再赋值，将左右两边的操作数相乘后再赋值给左边的操作数。 | C *= A 相当于 C = C * A |
| /= | 相除后再赋值，将左右两边的操作数相除后再赋值给左边的操作数。 | C /= A 相当于 C = C / A |
| %= | 求余后再赋值，将左右两边的操作数求余后再赋值给左边的操作数。 | C %= A is equivalent to C = C % A |
| >= | 按位右移后再赋值 | C >>= 2 相当于 C = C >> 2 |
| &= | 按位与运算后赋值 | C &= 2 相当于 C = C & 2 |
| ^= | 按位异或运算符后再赋值 | C ^= 2 相当于 C = C ^ 2 |
| \|= | 按位或运算后再赋值 | C \|= 2 相当于 C = C \| 2 |


### 实例


## 实例


```scala
object Test {
   def main(args: Array[String]) = {
      var a = 10;
      var b = 20;
      var c = 0;

      c = a + b;
      println("c = a + b  = " + c );

      c += a ;
      println("c += a  = " + c );

      c -= a ;
      println("c -= a = " + c );

      c *= a ;
      println("c *= a = " + c );

      a = 10;
      c = 15;
      c /= a ;
      println("c /= a  = " + c );

      a = 10;
      c = 15;
      c %= a ;
      println("c %= a  = " + c );

      c <<= 2 ;
      println("c <<= 2  = " + c );

      c >>= 2 ;
      println("c >>= 2  = " + c );

      c >>= a ;
      println("c >>= a  = " + c );

      c &= a ;
      println("c &= 2  = " + c );

      c ^= a ;
      println("c ^= a  = " + c );

      c |= a ;
      println("c |= a  = " + c );
   }
}
```


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
c = a + b  = 30
c += a  = 40
c -= a = 30
c *= a = 300
c /= a  = 1
c %= a  = 5
c <<= 2  = 20
c >>= 2  = 5
c >>= a  = 0
c &= 2  = 0
c ^= a  = 10
c |= a  = 10
```


---


运算符优先级取决于所属的运算符组，它会影响算式的的计算。

实例： x = 7 + 3 * 2; 这里， x 计算结果为 13, 而不是 20，因为乘法（*） 高于加法（+）, 所以它先计算 3*2 再加上 7。

查看以下表格，优先级从上到下依次递减，最上面具有最高的优先级，逗号操作符具有最低的优先级。


| 类别 | 运算符 | 关联性 |
| --- | --- | --- |
| 1 | () [] | 左到右 |
| 2 | ! ~ | 右到左 |
| 3 | * / % | 左到右 |
| 4 | + - | 左到右 |
| 5 | >> >>>  >= >=







	  AI 思考中...





			** [Scala 访问修饰符](https://www.runoob.com/scala-access-modifiers.html)
			[Scala IF…ELSE 语句](https://www.runoob.com/scala-if-else.html) **













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