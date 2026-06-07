# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-cmath.html

C++ 标准库提供了丰富的功能，其中 `` 是一个包含数学函数的头文件，它提供了许多基本的数学运算和常数。


`` 是 C++ 标准库中的一个头文件，它定义了一组数学函数，这些函数可以执行基本的数学运算，如幂运算、三角函数、对数、绝对值等。


要使用 `` 中的函数，你需要在你的 C++ 程序中包含这个头文件：


```
#include <cmath>
```


## 常用函数


`` 提供了许多数学函数，以下是一些常用的函数。

### 1. 基本数学函数


| 函数 | 功能 | 示例 |
| --- | --- | --- |
| abs(x) | 计算整数 x 的绝对值 | abs(-5) // 5 |
| fabs(x) | 计算浮点数 x 的绝对值 | fabs(-5.5) // 5.5 |
| fmod(x, y) | 计算 x 除以 y 的余数 | fmod(5.3, 2) // 1.3 |
| remainder(x, y) | 计算 x 除以 y 的余数 | remainder(5.5, 2) // 1.5 |
| fmax(x, y) | 返回 x 和 y 中的较大值 | fmax(3.5, 4.2) // 4.2 |
| fmin(x, y) | 返回 x 和 y 中的较小值 | fmin(3.5, 4.2) // 3.5 |
| hypot(x, y) | 计算 sqrt(x*x + y*y) | hypot(3, 4) // 5 |

### 2. 指数和对数函数

| 函数 | 功能 | 示例 |
| --- | --- | --- |
| exp(x) | 计算 e^x，e 为自然对数的底数 | exp(1) // 2.71828... |
| log(x) | 计算 x 的自然对数 | log(2.71828) // 1 |
| log10(x) | 计算 x 的以 10 为底的对数 | log10(100) // 2 |
| pow(x, y) | 计算 x 的 y 次方 | pow(2, 3) // 8 |
| sqrt(x) | 计算 x 的平方根 | sqrt(16) // 4 |
| cbrt(x) | 计算 x 的立方根 | cbrt(27) // 3 |
| expm1(x) | 计算 e^x - 1 | expm1(1) // 1.71828... |
| log1p(x) | 计算 log(1 + x)，适用于 x 接近 0 的情况 | log1p(0.00001) // 0.00001 |



### 3. 三角函数


| 函数 | 功能 | 示例 |
| --- | --- | --- |
| sin(x) | 计算 x 的正弦值，x 以弧度为单位 | sin(3.14159 / 2) // 1 |
| cos(x) | 计算 x 的余弦值，x 以弧度为单位 | cos(3.14159) // -1 |
| tan(x) | 计算 x 的正切值，x 以弧度为单位 | tan(0) // 0 |
| asin(x) | 计算 x 的反正弦值，返回弧度 | asin(1) // 3.14159/2 |
| acos(x) | 计算 x 的反余弦值，返回弧度 | acos(-1) // 3.14159 |
| atan(x) | 计算 x 的反正切值，返回弧度 | atan(1) // 3.14159/4 |
| atan2(y, x) | 计算 y/x 的反正切值，返回弧度 | atan2(1, 1) // 3.14159/4 |


### 4. 双曲函数


| 函数 | 功能 | 示例 |
| --- | --- | --- |
| sinh(x) | 计算 x 的双曲正弦 | sinh(0) // 0 |
| cosh(x) | 计算 x 的双曲余弦 | cosh(0) // 1 |
| tanh(x) | 计算 x 的双曲正切 | tanh(1) // 0.7616 |
| asinh(x) | 计算 x 的反双曲正弦 | asinh(1) // 0.8814 |
| acosh(x) | 计算 x 的反双曲余弦，x ≥ 1 | acosh(1) // 0 |
| atanh(x) | 计算 x 的反双曲正切，x 在 (-1, 1) | atanh(0.5) // 0.5493 |


### 5. 取整和浮点数操作


| 函数 | 功能 | 示例 |
| --- | --- | --- |
| ceil(x) | 返回不小于 x 的最小整数 | ceil(2.3) // 3 |
| floor(x) | 返回不大于 x 的最大整数 | floor(2.3) // 2 |
| trunc(x) | 返回去除小数部分的整数值 | trunc(2.8) // 2 |
| round(x) | 返回四舍五入到最接近的整数 | round(2.5) // 3 |
| lround(x) | 返回四舍五入到 long 类型 | lround(2.5) // 3 |
| llround(x) | 返回四舍五入到 long long 类型 | llround(2.5) // 3 |
| nearbyint(x) | 返回舍入到最接近整数（但不引发浮点异常） | nearbyint(2.5) // 2 |
| rint(x) | 返回四舍五入到整数，符合当前舍入方式 | rint(2.5) // 3 |
| modf(x, &intpart) | 将 x 的整数和小数部分分离 | modf(2.3, &intpart) |


### 6. 浮点数检查


| 函数 | 功能 | 示例 |
| --- | --- | --- |
| isfinite(x) | 检查 x 是否为有限值（非无穷大或非 NaN） | isfinite(3.0) // true |
| isinf(x) | 检查 x 是否为无穷大 | isinf(1.0 / 0.0) // true |
| isnan(x) | 检查 x 是否为 NaN | isnan(0.0 / 0.0) // true |
| isnormal(x) | 检查 x 是否为正常的非零浮点数 | isnormal(1.0) // true |
| signbit(x) | 检查 x 的符号是否为负 | signbit(-5.3) // true |


## 实例


下面是一个使用 `` 的简单示例，展示了如何计算一个数的平方根、正弦值和绝对值。


## 实例 1


```cpp
#include <iostream>
#include <cmath> // 包含 <cmath> 头文件

int main() {
    double num = 9.0;
    double root = sqrt(num); // 计算平方根
    double sinValue = sin(M_PI / 2); // 计算正弦值，M_PI 是 π 的近似值
    double absValue = abs(-5.0); // 计算绝对值

    std::cout << "The square root of " << num << " is " << root << std::endl;
    std::cout << "The sine of " << M_PI / 2 << " is " << sinValue << std::endl;
    std::cout << "The absolute value of -5.0 is " << absValue << std::endl;

    return 0;
}
```


输出结果:


```
The square root of 9 is 3
The sine of 1.570796 is 1
The absolute value of -5 is 5
```


## 实例 2


```cpp
#include <iostream>
#include <cmath>

int main() {
    // 基本数学运算
    std::cout << "abs(-5) = " << abs(-5) << std::endl;
    std::cout << "fmod(5.3, 2) = " << fmod(5.3, 2) << std::endl;

    // 指数和对数函数
    std::cout << "exp(1) = " << exp(1) << std::endl;
    std::cout << "log(2.71828) = " << log(2.71828) << std::endl;
    std::cout << "pow(2, 3) = " << pow(2, 3) << std::endl;

    // 三角函数
    std::cout << "sin(3.14159 / 2) = " << sin(3.14159 / 2) << std::endl;
    std::cout << "cos(3.14159) = " << cos(3.14159) << std::endl;

    // 取整函数
    std::cout << "ceil(2.3) = " << ceil(2.3) << std::endl;
    std::cout << "floor(2.3) = " << floor(2.3) << std::endl;

    // 浮点数检查
    double x = 1.0 / 0.0;
    if (isinf(x)) {
        std::cout << "x is infinite" << std::endl;
    }

    return 0;
}
```


### 注意事项


- `` 中的函数通常接受 `float` 或 `double` 类型的参数，并返回相应类型的结果。对于 `long double` 类型，你可以使用 `` 中的函数，但需要在函数名后加上 `l` 后缀，例如 `sqrtl`。
- 某些函数，如 `pow` 和 `log`，可以接受整数作为参数，但结果仍然是浮点数。
- `` 中的函数可能会抛出异常，例如当 `sqrt` 函数的参数为负数时，会抛出 `std::domain_error` 异常。
- ### 点我分享笔记 笔记需要是本篇文章的内容扩展！ [文章投稿，可点击这里](https://www.runoob.com/tougao) [注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite) ### 分享笔记前必须登录！ [注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)--> ** 取消 * * 分享笔记 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址





















    **















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