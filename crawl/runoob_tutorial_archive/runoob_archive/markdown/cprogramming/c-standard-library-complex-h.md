# C 标准库

- Source: https://www.runoob.com/cprogramming/c-standard-library-complex-h.html

`` 是 C 标准库中的一个头文件，用于支持复数运算。

`` 在 C99 标准中引入，提供了一组用于定义和操作复数的类型、宏和函数。


### 1、复数类型


`` 定义了以下复数类型：


- `float complex`：单精度复数。
- `double complex`：双精度复数。
- `long double complex`：长双精度复数。


这些类型实际上是 C 标准库中定义的宏，分别扩展为 `_Complex float`、`_Complex double` 和 `_Complex long double`。


---


### 2、复数常量


`` 定义了以下宏，用于表示虚数单位 `i`：


- `I`：表示虚数单位 `i`，即 `sqrt(-1)`。


## 实例


```c
double complex z = 3.0 + 4.0 * I; // 表示复数 3 + 4i
```


### 3、复数操作函数


`` 提供了一组用于操作复数的函数，包括算术运算、三角函数、指数函数和对数函数等。以下是一些常用函数：


#### 算术运算


| 函数 | 描述 |
| --- | --- |
| creal(z) | 返回复数 z 的实部 |
| cimag(z) | 返回复数 z 的虚部 |
| cabs(z) | 返回复数 z 的模（绝对值） |
| carg(z) | 返回复数 z 的幅角（相位） |
| conj(z) | 返回复数 z 的共轭复数 |
| cproj(z) | 返回复数 z 的投影 |


#### 三角函数


| 函数 | 描述 |
| --- | --- |
| csin(z) | 返回复数 z 的正弦值 |
| ccos(z) | 返回复数 z 的余弦值 |
| ctan(z) | 返回复数 z 的正切值 |


#### 指数和对数函数


| 函数 | 描述 |
| --- | --- |
| cexp(z) | 返回复数 z 的指数值 |
| clog(z) | 返回复数 z 的自然对数 |


#### 幂函数


| 函数 | 描述 |
| --- | --- |
| cpow(z1, z2) | 返回复数 z1 的 z2 次幂 |


#### 平方根函数


| 函数 | 描述 |
| --- | --- |
| csqrt(z) | 返回复数 z 的平方根 |


---


### 4、实例


以下是一个使用 `` 的示例，展示了如何定义和操作复数：


## 实例


```c
#include <stdio.h>
#include <complex.h>

int main() {
    // 定义复数
    double complex z1 = 3.0 + 4.0 * I;
    double complex z2 = 1.0 - 2.0 * I;

    // 算术运算
    double complex sum = z1 + z2;
    double complex product = z1 * z2;

    // 输出结果
    printf("z1 = %.2f + %.2fi\n", creal(z1), cimag(z1));
    printf("z2 = %.2f + %.2fi\n", creal(z2), cimag(z2));
    printf("Sum = %.2f + %.2fi\n", creal(sum), cimag(sum));
    printf("Product = %.2f + %.2fi\n", creal(product), cimag(product));

    // 模和幅角
    printf("|z1| = %.2f\n", cabs(z1));
    printf("Phase of z1 = %.2f radians\n", carg(z1));

    // 指数函数
    double complex exp_z1 = cexp(z1);
    printf("exp(z1) = %.2f + %.2fi\n", creal(exp_z1), cimag(exp_z1));

    return 0;
}
```


**输出结果**：


```
z1 = 3.00 + 4.00i
z2 = 1.00 + -2.00i
Sum = 4.00 + 2.00i
Product = 11.00 + -2.00i
|z1| = 5.00
Phase of z1 = 0.93 radians
exp(z1) = -13.13 + -15.20i
```


---


### 5、注意事项


- `` 仅在 C99 及更高版本中可用。
- 复数类型和函数的使用需要包含 `` 头文件。
- 复数运算的性能可能低于实数运算，特别是在涉及大量计算时。


---


### 6、复数运算的数学背景


复数的一般形式为 `a + bi`，其中：


- `a` 是实部，`b` 是虚部。
- `i` 是虚数单位，满足 `i² = -1`。


复数的模（绝对值）为：




```
|z| = sqrt(a² + b²)
```


复数的幅角（相位）为：




```
arg(z) = atan2(b, a)
```


复数的指数形式为：




```
exp(z) = exp(a) * (cos(b) + i * sin(b))
```









	  AI 思考中...





			** [C 标准库 *](https://www.runoob.com/c-standard-library-inttypes-h.html)
			[C 标准库 ](https://www.runoob.com/c-standard-library-tgmath-h.html) *













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