# TypeScript 运算符

- Source: https://www.runoob.com/typescript/ts-operators.html

运算符用于执行程序代码运算，会针对一个以上操作数项目来进行运算。


考虑以下计算：


```
7 + 5 = 12
```


以上实例中 7、5 和 12 是操作数。


运算符 **+** 用于加值。


运算符 **=** 用于赋值。


TypeScript 主要包含以下几种运算：


- 算术运算符
- 逻辑运算符
- 关系运算符
- 按位运算符
- 赋值运算符
- 三元/条件运算符
- 字符串运算符
- 类型运算符


---


## 算术运算符


假定 **y=5**，下面的表格解释了这些算术运算符的操作：


| 运算符 | 描述 | 例子 | x 运算结果 | y 运算结果 |
| --- | --- | --- | --- | --- |
| + | 加法 | x=y+2 | 7 | 5 |
| - | 减法 | x=y-2 | 3 | 5 |
| * | 乘法 | x=y*2 | 10 | 5 |
| / | 除法 | x=y/2 | 2.5 | 5 |
| % | 取模（余数） | x=y%2 | 1 | 5 |
| ++ | 自增 | x=++y | 6 | 6 |
| x=y++ | 5 | 6 |  |  |
| -- | 自减 | x=--y | 4 | 4 |
| x=y-- | 5 | 4 |  |  |


### 实例


```javascript
var num1:number = 10
var num2:number = 2
var res:number = 0

res = num1 + num2
console.log("加:        "+res);

res = num1 - num2;
console.log("减: "+res)

res = num1*num2
console.log("乘:    "+res)

res = num1/num2
console.log("除:   "+res)

res = num1%num2
console.log("余数:   "+res)

num1++
console.log("num1 自增运算: "+num1)

num2--
console.log("num2 自减运算: "+num2)
```


使用 **tsc** 命令编译以上代码得到如下 JavaScript 代码：


```javascript
var num1 = 10;
var num2 = 2;
var res = 0;
res = num1 + num2;
console.log("加:        " + res);
res = num1 - num2;
console.log("减: " + res);
res = num1 * num2;
console.log("乘:    " + res);
res = num1 / num2;
console.log("除:   " + res);
res = num1 % num2;
console.log("余数:   " + res);
num1++;
console.log("num1 自增运算: " + num1);
num2--;
console.log("num2 自减运算: " + num2);
```


执行以上 JavaScript 代码，输出结果为：


```
加:        12
减: 8
乘:    20
除:   5
余数:   0
num1 自增运算: 11
num2 自减运算: 1
```


---


## 关系运算符


关系运算符用于计算结果是否为 true 或者 false。


x=5，下面的表格解释了关系运算符的操作：


| 运算符 | 描述 | 比较 | 返回值 |
| --- | --- | --- | --- |
| == | 等于 | x==8 | false |
| x==5 | true |  |  |
| != | 不等于 | x!=8 | true |
| > | 大于 | x>8 | false |
| = | 大于或等于 | x>=8 | false |
|  5 是使用了 && 运算符的组合表达式，第一个表达式返回了 false，由于 && 运算需要两个表达式都为 true，所以如果第一个为 false，就不再执行后面的判断(a > 5 跳过计算)，直接返回 false。


|| 运算符只要其中一个表达式为 true ，则该组合表达式就会返回 true。


考虑以下实例：


```
var a = 10
var result = ( a>5 || a<10)
```


以上实例中 a > 5 与 a > | 右移，把 >> 左边的运算数的各二进位全部右移若干位，>> 右边的数指定移动的位数。 | x = 5 >> 1 | 0101 >> 1 | 0010 | 2 |
| >>> | 无符号右移，与有符号右移位类似，除了左边一律使用0 补位。 | x = 2 >>> 1 | 0010 >>> 1 | 0001 | 1 |


### 实例


```javascript
var a:number = 2;   // 二进制 10
var b:number = 3;   // 二进制 11

var result;

result = (a & b);
console.log("(a & b) => ",result)

result = (a | b);
console.log("(a | b) => ",result)

result = (a ^ b);
console.log("(a ^ b) => ",result);

result = (~b);
console.log("(~b) => ",result);

result = (a << b);
console.log("(a << b) => ",result);

result = (a >> b);
console.log("(a >> b) => ",result);

result = (a >>> 1);
console.log("(a >>> 1) => ",result);
```


使用 **tsc** 命令编译以上代码得到如下 JavaScript 代码：


```javascript
var a = 2; // 二进制 10
var b = 3; // 二进制 11
var result;
result = (a & b);
console.log("(a & b) => ", result);
result = (a | b);
console.log("(a | b) => ", result);
result = (a ^ b);
console.log("(a ^ b) => ", result);
result = (~b);
console.log("(~b) => ", result);
result = (a << b);
console.log("(a << b) => ", result);
result = (a >> b);
console.log("(a >> b) => ", result);
result = (a >>> 1);
console.log("(a >>> 1) => ", result);
```


执行以上 JavaScript 代码，输出结果为：


```
(a & b) =>  2
(a | b) =>  3
(a ^ b) =>  1
(~b) =>  -4
(a << b) =>  16
(a >> b) =>  0
(a >>> 1) =>  1
```


---


## 赋值运算符


赋值运算符用于给变量赋值。


给定 x=10 **和** y=5**，下面的表格解释了赋值运算符：


| 运算符 | 例子 | 实例 | x 值 |
| --- | --- | --- | --- |
| = (赋值) | x = y | x = y | x = 5 |
| += (先进行加运算后赋值) | x += y | x = x + y | x = 15 |
| -= (先进行减运算后赋值) | x -= y | x = x - y | x = 5 |
| *= (先进行乘运算后赋值) | x *= y | x = x * y | x = 50 |
| /= (先进行除运算后赋值) | x /= y | x = x / y | x = 2 |


**
类似的逻辑运算符也可以与赋值运算符联合使用：**>=**, **>>>=**, **&=**, **|=** 与 **^=**。


### 实例


```javascript
var a: number = 12
var b:number = 10

a = b
console.log("a = b: "+a)

a += b
console.log("a+=b: "+a)

a -= b
console.log("a-=b: "+a)

a *= b
console.log("a*=b: "+a)

a /= b
console.log("a/=b: "+a)

a %= b
console.log("a%=b: "+a)
```


使用 **tsc** 命令编译以上代码得到如下 JavaScript 代码：


```javascript
var a = 12;
var b = 10;
a = b;
console.log("a = b: " + a);
a += b;
console.log("a+=b: " + a);
a -= b;
console.log("a-=b: " + a);
a *= b;
console.log("a*=b: " + a);
a /= b;
console.log("a/=b: " + a);
a %= b;
console.log("a%=b: " + a);
```


执行以上 JavaScript 代码，输出结果为：


```
a = b: 10
a+=b: 20
a-=b: 10
a*=b: 100
a/=b: 10
a%=b: 0
```


---


## 三元运算符 (?)


三元运算有 3 个操作数，并且需要判断布尔表达式的值。该运算符的主要是决定哪个值应该赋值给变量。


```
Test ? expr1 : expr2
```


- Test − 指定的条件语句
- expr1 − 如果条件语句 Test 返回 true 则返回该值
- expr2 − 如果条件语句 Test 返回 false 则返回该值


让我们看下以下实例：


```javascript
var num:number = -2
var result = num > 0 ? "大于 0" : "小于 0，或等于 0"
console.log(result)
```


实例中用于判断变量是否大于 0。


使用 tsc 命令编译以上代码得到如下 JavaScript 代码：


```javascript
var num = -2;
var result = num > 0 ? "大于 0" : "小于 0，或等于 0";
console.log(result);
```


以上实例输出结果如下：


```
小于 0，或等于 0
```


---


## 类型运算符


### typeof 运算符


typeof 是一元运算符，返回操作数的数据类型。


查看以下实例:


```javascript
var num = 12
console.log(typeof num);   //输出结果: number
```


使用 tsc 命令编译以上代码得到如下 JavaScript 代码：


```javascript
var num = 12;
console.log(typeof num); //输出结果: number
```


以上实例输出结果如下：


```
number
```


### instanceof


instanceof 运算符用于判断对象是否为指定的类型，后面章节我们会具体介绍它。


---


## 其他运算符


### 负号运算符(-)


更改操作数的符号，查看以下实例：


```javascript
var x:number = 4
var y = -x;
console.log("x 值为: ",x);   // 输出结果 4
console.log("y 值为: ",y);   // 输出结果 -4
```


使用 tsc 命令编译以上代码得到如下 JavaScript 代码：


```javascript
var x = 4;
var y = -x;
console.log("x 值为: ", x); // 输出结果 4
console.log("y 值为: ", y); // 输出结果 -4
```


以上实例输出结果如下：


```
x 值为:  4
y 值为:  -4
```


### 字符串运算符: 连接运算符 (+)


+ 运算符可以拼接两个字符串，查看以下实例：


```javascript
var msg:string = "RUNOOB"+".COM"
console.log(msg)
```


使用 tsc 命令编译以上代码得到如下 JavaScript 代码：


```javascript
var msg = "RUNOOB" + ".COM";
console.log(msg);
```


以上实例输出结果如下：


```
RUNOOB.COM
```










	  AI 思考中...





			** [TypeScript 变量声明](https://www.runoob.com/ts-variables.html)
			[TypeScript 条件语句](https://www.runoob.com/ts-if-statement.html) **













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