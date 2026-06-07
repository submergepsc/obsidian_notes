# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-complex.html

在数学和工程计算中，我们常常需要处理 复数（complex number），比如信号处理、傅里叶变换、电路分析等。


C++ 标准库提供了 `` 头文件，让你可以像处理普通数字一样轻松操作复数。


一个复数由实部（real part）和虚部（imaginary part）构成，形式：


```
z = a + bi
```


复数是实数和虚数的组合，通常表示为 `a + bi`，其中 `a` 是实部，`b` 是虚部，`i` 是虚数单位，满足 `i^2 = -1`。


在 C++ 中，复数类型由 `std::complex` 表示，其中 `T` 可以是任意的算术类型，如 `float`、`double` 或 `long double`。


要使用 `` 库，首先需要在你的 C++ 程序中包含这个头文件：


```
#include <iostream>
#include <complex>
```


## 实例


```cpp
#include <iostream>
#include <complex>  // 复数头文件

int main() {
    std::complex<double> z1(3.0, 4.0); // 3 + 4i
    std::complex<double> z2(1.0, -2.0); // 1 - 2i

    std::cout << "z1 = " << z1 << std::endl;
    std::cout << "z2 = " << z2 << std::endl;
}
```


输出：


```
z1 = (3,4)
z2 = (1,-2)
```


## 基本语法


### 创建复数


```
std::complex<double> c(5.0, 3.0); // 创建一个复数 5 + 3i
```


### 访问实部和虚部


```
double realPart = c.real(); // 获取实部
double imagPart = c.imag(); // 获取虚部
```


### 复数的基本运算


C++ 标准库 `` 支持以下基本运算：


- 加法：`operator+`
- 减法：`operator-`
- 乘法：`operator*`
- 除法：`operator/`
- 共轭：`conj`
- 模：`abs`
- 辐角：`arg`


**1 、获取实部和虚部**


```
std::cout << "实部: " << z1.real() << std::endl; // 3
std::cout << "虚部: " << z1.imag() << std::endl; // 4
```


**2、四则运算：**


## 实例


```cpp
auto z3 = z1 + z2;   // (4, 2)
auto z4 = z1 - z2;   // (2, 6)
auto z5 = z1 * z2;   // (11, -2)
auto z6 = z1 / z2;   // (-1, 2)

std::cout << "z1 + z2 = " << z3 << std::endl;
std::cout << "z1 * z2 = " << z5 << std::endl;
```


**3、常用函数**


头文件 `` 提供了很多和复数相关的数学函数。


## 实例


```cpp
#include <cmath>   // 部分数学函数需要

std::cout << "模长 |z1| = " << std::abs(z1) << std::endl;     // 5
std::cout << "幅角 arg(z1) = " << std::arg(z1) << std::endl;  // 0.927 (弧度)
std::cout << "共轭 conjugate(z1) = " << std::conj(z1) << std::endl; // (3,-4)
std::cout << "exp(z1) = " << std::exp(z1) << std::endl;       // e^(3+4i)
std::cout << "sin(z1) = " << std::sin(z1) << std::endl;
std::cout << "cos(z1) = " << std::cos(z1) << std::endl;
```


**4、极坐标表示**


有时我们需要用 极坐标（模长 + 相角） 表示复数。


## 实例


```cpp
// 从极坐标生成复数
double r = 5.0;           // 模长
double theta = M_PI / 4;  // 45 度
std::complex<double> z = std::polar(r, theta);

std::cout << "极坐标复数 z = " << z << std::endl;  // (3.53553,3.53553)
```


#### 5、模板参数


`std::complex` 是一个模板类，支持不同的数值类型：


- `std::complex`
- `std::complex`（常用）
- `std::complex`


## 实例


```cpp
std::complex<float>  zf(1.0f, 2.0f);
std::complex<double> zd(1.0, 2.0);
```


## 实例


下面是一个使用 `` 头文件的简单示例，包括创建复数、基本运算和输出结果。


## 实例


```cpp
#include <iostream>
#include <complex>

int main() {
    // 创建两个复数
    std::complex<double> c1(5.0, 3.0);   // 5 + 3i
    std::complex<double> c2(2.0, -4.0);  // 2 - 4i

    // 输出复数
    std::cout << "c1: " << c1 << std::endl;  // (5,3)
    std::cout << "c2: " << c2 << std::endl;  // (2,-4)

    // 复数加法
    std::complex<double> sum = c1 + c2;
    std::cout << "Sum: " << sum << std::endl;  // 7 - i

    // 复数减法
    std::complex<double> diff = c1 - c2;
    std::cout << "Difference: " << diff << std::endl;  // 3 + 7i

    // 复数乘法
    std::complex<double> product = c1 * c2;
    std::cout << "Product: " << product << std::endl;  // 22 - 14i

    // 复数除法
    std::complex<double> quotient = c1 / c2;
    std::cout << "Quotient: " << quotient << std::endl;  // -0.1 + 1.3i

    // 复数的共轭
    std::complex<double> conjugate = std::conj(c1);
    std::cout << "Conjugate of c1: " << conjugate << std::endl;  // 5 - 3i

    // 复数的模
    double modulus = std::abs(c1);
    std::cout << "Modulus of c1: " << modulus << std::endl;  // sqrt(34) ≈ 5.83095

    // 复数的辐角（弧度制）
    double argument = std::arg(c1);
    std::cout << "Argument of c1: " << argument << std::endl;  // atan(3/5) ≈ 0.54042 rad

    return 0;
}
```


当你运行上述程序时，你将得到以下输出：


```
c1: (5,3)
c2: (2,-4)
Sum: (7,-1)
Difference: (3,7)
Product: (22,-14)
Quotient: (-0.1,1.3)
Conjugate of c1: (5,-3)
Modulus of c1: 5.83095
Argument of c1: 0.54042
```










	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-numeric.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-valarray.html) **













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