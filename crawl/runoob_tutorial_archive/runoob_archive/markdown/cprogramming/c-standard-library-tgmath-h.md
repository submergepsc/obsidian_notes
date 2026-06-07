# C 标准库

- Source: https://www.runoob.com/cprogramming/c-standard-library-tgmath-h.html

`` 是 C 标准库中的一个头文件，提供了**类型泛型数学函数**（Type-Generic Math Functions）。

`` 库在 C99 标准中引入，允许开发者使用统一的函数名来调用不同类型的数学函数（如 `float`、`double` 和 `long double`），而无需显式指定函数的具体类型。


`` 的主要目的是：


- 简化数学函数的使用，避免为不同类型（如 `float`、`double`、`long double`）显式调用不同的函数（如 `sinf`、`sin`、`sinl`）。
- 提高代码的可读性和可维护性。
- 支持复数类型的数学函数。


---


### 1、类型泛型宏


`` 定义了一组类型泛型宏，这些宏根据参数的类型自动选择正确的数学函数。例如：


- `sin(x)`：如果 `x` 是 `float`，则调用 `sinf(x)`；如果 `x` 是 `double`，则调用 `sin(x)`；如果 `x` 是 `long double`，则调用 `sinl(x)`。
- `sqrt(x)`：如果 `x` 是 `float`，则调用 `sqrtf(x)`；如果 `x` 是 `double`，则调用 `sqrt(x)`；如果 `x` 是 `long double`，则调用 `sqrtl(x)`。


这些宏支持以下类型的参数：


- 实数类型：`float`、`double`、`long double`。
- 复数类型：`float complex`、`double complex`、`long double complex`。


---


### 2、支持的函数


`` 支持以下类型泛型数学函数：


#### 基本数学函数


| 函数 | 描述 |
| --- | --- |
| sin | 正弦函数 |
| cos | 余弦函数 |
| tan | 正切函数 |
| asin | 反正弦函数 |
| acos | 反余弦函数 |
| atan | 反正切函数 |
| atan2 | 两个参数的反正切函数 |
| sinh | 双曲正弦函数 |
| cosh | 双曲余弦函数 |
| tanh | 双曲正切函数 |
| asinh | 反双曲正弦函数 |
| acosh | 反双曲余弦函数 |
| atanh | 反双曲正切函数 |


#### 指数和对数函数


| 函数 | 描述 |
| --- | --- |
| exp | 指数函数 |
| log | 自然对数函数 |
| log10 | 常用对数函数 |
| pow | 幂函数 |


#### 其他函数


| 函数 | 描述 |
| --- | --- |
| sqrt | 平方根函数 |
| fabs | 绝对值函数 |
| ceil | 向上取整函数 |
| floor | 向下取整函数 |
| fmod | 浮点数取余函数 |


---


### 3、实例


以下是一个使用 `` 的示例，展示了如何使用类型泛型数学函数：


## 实例


```c
#include <stdio.h>
#include <tgmath.h>

int main() {
    // 实数类型
    float f = 1.5f;
    double d = 2.5;
    long double ld = 3.5L;

    // 使用类型泛型函数
    printf("sin(f) = %f\n", sin(f));       // 调用 sinf
    printf("sin(d) = %f\n", sin(d));       // 调用 sin
    printf("sin(ld) = %Lf\n", sin(ld));    // 调用 sinl

    // 复数类型
    double complex z = 1.0 + 2.0 * I;

    // 使用类型泛型函数
    double complex sqrt_z = sqrt(z);
    printf("sqrt(z) = %f + %fi\n", creal(sqrt_z), cimag(sqrt_z));

    return 0;
}
```


**输出结果**：


```
sin(f) = 0.997495
sin(d) = 0.598472
sin(ld) = 0.350783
sqrt(z) = 1.272020 + 0.786151i
```


### 4、注意事项


- `` 仅在 C99 及更高版本中可用。
- 类型泛型宏根据参数的类型自动选择正确的函数，因此参数的类型必须明确。
- 如果参数类型不明确（例如，整数常量），编译器可能会选择默认的 `double` 版本。
- 复数类型的函数需要包含 `` 头文件。


---


### 5、实现原理


`` 的实现依赖于 C 语言的泛型选择机制（`_Generic` 关键字）。例如，`sin` 宏的定义可能如下：


```
#define sin(x) _Generic((x), \
    float: sinf,             \
    double: sin,             \
    long double: sinl        \
)(x)
```


`_Generic` 关键字根据 `x` 的类型选择正确的函数。

`` 提供了类型泛型数学函数，简化了不同数值类型（如 `float`、`double`、`long double` 和复数类型）的数学函数调用。它是 C99 标准中的一个重要特性，特别适用于需要处理多种数值类型的科学计算和工程应用。通过使用 ``，开发者可以编写更简洁、更通用的代码。









	  AI 思考中...





			** [C 标准库 ](https://www.runoob.com/c-standard-library-complex-h.html)
			[C 标准库 ](https://www.runoob.com/c-standard-library-fenv-h.html) **













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