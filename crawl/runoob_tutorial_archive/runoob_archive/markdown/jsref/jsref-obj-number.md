# JavaScript Number 对象

- Source: https://www.runoob.com/jsref/jsref-obj-number.html

---


## Number 对象


Number 对象是原始数值的包装对象。


Number 创建方式 new Number()。


## 语法


var num = new Number(value);

**注意：** 如果一个参数值不能转换为一个数字将返回 NaN (非数字值)。


---


## Number 对象属性


| 属性 | 描述 |
| --- | --- |
| constructor | 返回对创建此对象的 Number 函数的引用。 |
| MAX_VALUE | 可表示的最大的数。 |
| MIN_VALUE | 可表示的最小的数。 |
| NEGATIVE_INFINITY | 负无穷大，溢出时返回该值。 |
| NaN | 非数字值。 |
| POSITIVE_INFINITY | 正无穷大，溢出时返回该值。 |
| prototype | 允许您可以向对象添加属性和方法。 |


## Number 对象方法


| 方法 | 描述 |
| --- | --- |
| isFinite | 检测指定参数是否为无穷大。 |
| isInteger | 检测指定参数是否为整数。 |
| isNaN | 检测指定参数是否为 NaN。 |
| isSafeInteger | 检测指定参数是否为安全整数。 |
| toExponential(x) | 把对象的值转换为指数计数法。 |
| toFixed(x) | 把数字转换为字符串，结果的小数点后有指定位数的数字。 |
| toLocaleString(locales, options) | 返回数字在特定语言环境下的表示字符串。 |
| toPrecision(x) | 把数字格式化为指定的长度。 |
| toString() | 把数字转换为字符串，使用指定的基数。 |
| valueOf() | 返回一个 Number 对象的基本数字值。 |


---


## ES6 新增 Number 属性

ES 6 增加了以下三个 Number 对象的属性：


- EPSILON: 表示 1 和比最接近 1 且大于 1 的最小 Number 之间的差别
- MIN_SAFE_INTEGER: 表示在 JavaScript中最小的安全的 integer 型数字 (`-(253 - 1)`)。
- MAX_SAFE_INTEGER: 表示在 JavaScript 中最大的安全整数（`253 - 1`）。


## 实例


```
var x = Number.EPSILON;

var y = Number.MIN_SAFE_INTEGER;

var z = Number.MAX_SAFE_INTEGER;
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_es6_epsilon)

---


## ES6 新增 Number 方法


ES 6 增加了以下两个 Number 对象的方法：


- Number.isInteger(): 用来判断给定的参数是否为整数。
- Number.isSafeInteger(): 判断传入的参数值是否是一个"安全整数"。


Number.isInteger() 在参数是整数时返回 true。


## 实例


```
Number.isInteger(10);        // 返回 true
Number.isInteger(10.5);      // 返回 false
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_es6_isinteger)


Number.isSafeInteger()判断传入的参数值是否是一个"安全整数"。


安全整数范围为 `-(253 - 1)到` `253 - 1 `之间的整数，包含 `-(253 - 1)和` `253 - 1`。


## 实例


```
Number.isSafeInteger(10);    // 返回 true
Number.isSafeInteger(12345678901234567890);  // 返回 false
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_es6_issafeinteger)








	  AI 思考中...





			** [JavaScript Number prototype 属性](https://www.runoob.com/jsref-prototype-num.html)
			[JavaScript sup() 方法](https://www.runoob.com/jsref-sup.html) **













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