# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-numbers.html

在 C++20 之前，我们写数学常量通常是这样：


```
const double PI = 3.14159265358979323846;
```


问题非常明显：**精度随手写、不统一、易写错、类型不安全。 C++20 正式引入 **#include **，提供标准化数学常量集合，由编译器保证精度与类型正确性。


`std::numbers` 是 C++20 中引入的一个标准库模块，主要用于提供一组常用的数学常量，是一套标准数学物理常数仓库。

`std::numbers`位于 `` 头文件中，并且包含了很多数学常量，涵盖了圆周率、自然对数的底数、黄金比例等常见常数。


C++ 使用这些常量可以提高代码的可读性、精度和效率，避免了重复定义和手动输入常数值。


`std::numbers` 与传统写法对比优势：


| 维度 | 传统写法 |  |
| --- | --- | --- |
| 精度 | 随手写 | 标准高精度 |
| 类型 | 固定 | 自动匹配 |
| 可读性 | 一般 | 语义明确 |
| 编译期常量 | 不一定 | 一定 |
| 规范性 | 差 | 标准库级 |


### std::numbers 模块包含的常量


std::numbers 命名空间下包含以下成员：


```
template<floating_point T> inline constexpr T e_v<T> // 自然常数e
template<floating_point T> inline constexpr T log2e_v<T> // log2e
template<floating_point T> inline constexpr T log10e_v<T> // log10e
template<floating_point T> inline constexpr T pi_v<T> // 圆周率π
template<floating_point T> inline constexpr T inv_pi_v<T> // 1/π
template<floating_point T> inline constexpr T inv_sqrtpi_v<T> //1/根号π
template<floating_point T> inline constexpr T ln2_v<T> // ln2
template<floating_point T> inline constexpr T ln10_v<T> // ln10
template<floating_point T> inline constexpr T sqrt2_v<T> //根号2
template<floating_point T> inline constexpr T sqrt3_v<T> //根号3
template<floating_point T> inline constexpr T inv_sqrt3_v<T> // 1/根号3
template<floating_point T> inline constexpr T egamma_v<T> // 欧拉常数γ
template<floating_point T> inline constexpr T phi_v<T> // 黄金分割比Φ
inline constexpr double e = e_v<double>
inline constexpr double log2e = log2e_v<double>
inline constexpr double log10e = log10e_v<double>
inline constexpr double pi = pi_v<double>
inline constexpr double inv_pi = pi_v<double>
inline constexpr double inv_sqrtpi = pi_v<double>
inline constexpr double ln2 = ln2_v<double>
inline constexpr double ln10 = ln10_v<double>
inline constexpr double sqrt2 = sqrt2_v<double>
inline constexpr double sqrt3 = sqrt3_v<double>
inline constexpr double inv_sqrt3 = sqrt3_v<double>
inline constexpr double egamma = egamma_v<double>
inline constexpr double phi = phi_v<double>
```


以下是 std::numbers 中包含的常量列表：


| 常量/模板名称 | 描述 | 示例值（近似） |
| --- | --- | --- |
| e_v | 数学常数 e（自然对数的底数） | 2.718281828459045 |
| log2e_v | 以 2 为底的 e 的对数（log₂(e)） | 1.4426950408889634 |
| log10e_v | 以 10 为底的 e 的对数（log₁₀(e)） | 0.4342944819032518 |
| pi_v | 数学常数 π（圆周率） | 3.141592653589793 |
| inv_pi_v | 1/π（π的倒数） | 0.318309886183121 |
| inv_sqrtpi_v | 1/√π（π的平方根的倒数） | 0.5641895835477563 |
| ln2_v | 自然对数底数 2 的对数（ln(2)） | 0.6931471805599453 |
| ln10_v | 自然对数底数 10 的对数（ln(10)） | 2.302585092994046 |
| sqrt2_v | √2（根号 2） | 1.4142135623730951 |
| sqrt3_v | √3（根号 3） | 1.7320508075688772 |
| inv_sqrt3_v | 1/√3（根号 3 的倒数） | 0.5773502691896257 |
| egamma_v | 欧拉-马歇罗尼常数 γ（Euler-Mascheroni constant） | 0.5772156649015329 |
| phi_v | 黄金比例 Φ（(1 + √5) / 2） | 1.618033988749895 |
| e | 常量 e (等价于 e_v) | 2.718281828459045 |
| log2e | 常量 log₂(e) (等价于 log2e_v) | 1.4426950408889634 |
| log10e | 常量 log₁₀(e) (等价于 log10e_v) | 0.4342944819032518 |
| pi | 常量 π (等价于 pi_v) | 3.141592653589793 |
| inv_pi | 常量 1/π (等价于 inv_pi_v) | 0.318309886183121 |
| inv_sqrtpi | 常量 1/√π (等价于 inv_sqrtpi_v) | 0.5641895835477563 |
| ln2 | 常量 ln(2) (等价于 ln2_v) | 0.6931471805599453 |
| ln10 | 常量 ln(10) (等价于 ln10_v) | 2.302585092994046 |
| sqrt2 | 常量 √2 (等价于 sqrt2_v) | 1.4142135623730951 |
| sqrt3 | 常量 √3 (等价于 sqrt3_v) | 1.7320508075688772 |
| inv_sqrt3 | 常量 1/√3 (等价于 inv_sqrt3_v) | 0.5773502691896257 |
| egamma | 常量 γ (欧拉-马歇罗尼常数) (等价于 egamma_v) | 0.5772156649015329 |
| phi | 常量黄金比例 Φ (等价于 phi_v) | 1.618033988749895 |


这些常量和变量模板涵盖了圆周率、自然对数底、黄金比例等常用的数学常数，并通过不同类型的变量模板提供精度选项，如 float、double 和 long double。


## 实例


```cpp
#include <iostream>
#include <iomanip>
#include <numbers>
#include <cmath>  // 用于标准数学函数 sin, cos, log 等

using namespace std;

int main()
{
    // 使用默认的 double 类型常数
    cout << fixed << setprecision(15); // 设置所有输出为 15 位小数

    // 打印圆周率 π 的值
    cout << "圆周率 pi 的值是: " << numbers::pi << endl;

    // 打印自然对数的底数 e 的值
    cout << "自然常数 e 的值是: " << numbers::e << endl;

    // 打印根号2 (sqrt2) 的值
    cout << "根号2 (sqrt2) 的值是: " << numbers::sqrt2 << endl;

    // 打印根号3 (sqrt3) 的值
    cout << "根号3 (sqrt3) 的值是: " << numbers::sqrt3 << endl;

    // 打印黄金比例 phi 的值
    cout << "黄金比例 phi 的值是: " << numbers::phi << endl;

    // 打印欧拉-马歇罗尼常数 egamma 的值
    cout << "欧拉-马歇罗尼常数 egamma 的值是: " << numbers::egamma << endl;

    // 打印 1/π (inv_pi) 的值
    cout << "1/π (inv_pi) 的值是: " << numbers::inv_pi << endl;

    // 打印 1/√π (inv_sqrtpi) 的值
    cout << "1/√π (inv_sqrtpi) 的值是: " << numbers::inv_sqrtpi << endl;

    // 打印以 2 为底的 e 的对数 log2e 的值
    cout << "以 2 为底的 e 的对数 log2e 的值是: " << numbers::log2e << endl;

    // 打印以 10 为底的 e 的对数 log10e 的值
    cout << "以 10 为底的 e 的对数 log10e 的值是: " << numbers::log10e << endl;

    // 打印 sin(π/2) 的值
    cout << "sin(π/2) 的值是: " << sin(numbers::pi / 2) << endl;

    // 打印 cos(π) 的值
    cout << "cos(π) 的值是: " << cos(numbers::pi) << endl;

    // 打印 ln(e) 的值
    cout << "ln(e) 的值是: " << log(numbers::e) << endl;

    // 演示使用不同的数据类型
    float pi_f = numbers::pi_v<float>;  // 使用 float 类型的 pi
    cout << "\n使用 float 类型的 pi: " << setprecision(7) << pi_f << endl; // 输出 7 位小数

    long double pi_ld = numbers::pi_v<long double>;  // 使用 long double 类型的 pi
    cout << "使用 long double 类型的 pi: " << setprecision(21) << pi_ld << endl; // 输出 21 位小数

    // 计算不同精度的值
    cout << "\nsin(π/2) 使用 double: " << sin(numbers::pi / 2) << endl;
    cout << "sin(π/2) 使用 float: " << sin(static_cast<float>(numbers::pi) / 2) << endl;
    cout << "sin(π/2) 使用 long double: " << sin(static_cast<long double>(numbers::pi) / 2) << endl;

    return 0;
}
```


**代码解析：**



**格式化输出：**


- 使用 `fixed` 和 `setprecision()` 来确保输出的小数点后有固定的位数。这里默认输出 15 位小数，但也可以为每个不同的数据类型设置不同的精度。



**计算常见数学函数：**


- 计算了 `sin(π/2)`、`cos(π)` 和 `ln(e)` 等常见数学函数，并使用 `cmath` 中的函数（例如 `sin`、`cos` 和 `log`）来展示如何使用数学常数。



**不同数据类型的精度：**


- 使用 `numbers::pi_v` 和 `numbers::pi_v` 来展示不同类型的常数。对于 `float` 和 `long double`，可以使用不同的精度输出。



**使用不同类型的计算：**


- 在计算 `sin` 时，展示了如何用不同精度的类型进行计算，演示了 `float`、`double` 和 `long double` 在相同数学表达式下的差异。




输出：


```
圆周率 pi 的值是: 3.141592653589793
自然常数 e 的值是: 2.718281828459045
根号2 (sqrt2) 的值是: 1.414213562373095
根号3 (sqrt3) 的值是: 1.732050807568877
黄金比例 phi 的值是: 1.618033988749895
欧拉-马歇罗尼常数 egamma 的值是: 0.5772156649015329
1/π (inv_pi) 的值是: 0.318309886183121
1/√π (inv_sqrtpi) 的值是: 0.5641895835477563
以 2 为底的 e 的对数 log2e 的值是: 1.4426950408889634
以 10 为底的 e 的对数 log10e 的值是: 0.4342944819032518
sin(π/2) 的值是: 1
cos(π) 的值是: -1
ln(e) 的值是: 1

使用 float 类型的 pi: 3.1415927
使用 long double 类型的 pi: 3.141592653589793238462643
sin(π/2) 使用 double: 1
sin(π/2) 使用 float: 1
sin(π/2) 使用 long double: 1
```


---


## 使用示例

以下示例覆盖 **** 最常用的常量，代码可直接编译运行，记得加一个标准参数 **-std=c++20**：


```
g++ -std=c++20 main.cpp -o main
```


### 示例 1：基础使用


圆周率 π 计算圆的面积 / 周长：


## 实例


```cpp
#include <iostream>
#include <numbers>  // 包含数学常量
#include <cmath>    // 包含pow等数学函数

using namespace std;
using namespace std::numbers;  // 简化常量调用（可选）

int main() {
    // 圆的半径
    double r = 5.0;

    // 1. 计算圆的周长：2 * π * r
    double circumference = 2 * pi * r;  // 直接使用double版π
    cout << "半径为" << r << "的圆周长：" << circumference << endl;  // 输出：31.4159

    // 2. 计算圆的面积：π * r²
    double area = pi * pow(r, 2);
    cout << "半径为" << r << "的圆面积：" << area << endl;  // 输出：78.5398

    // 3. 高精度版本（long double）
    long double r_ld = 5.0L;
    long double area_ld = pi_v<long double> * powl(r_ld, 2);  // powl是long double版pow
    cout << "高精度圆面积：" << area_ld << endl;  // 输出更精确的78.53981633974483...

    return 0;
}
```


### 示例 2：常数 e


自然常数 e 与指数计算：


## 实例


```cpp
#include <iostream>
#include <numbers>
#include <cmath>

using namespace std;
using namespace std::numbers;

int main() {
    // 自然指数计算：e^x（exp函数是cmath中的指数函数）
    double x = 2.0;
    double exp_result = exp(x);          // 手动计算e^2
    double exp_result_direct = pow(e, x); // 用numbers::e计算e^2
    cout << "e^2 = " << exp_result << endl;          // 输出：7.38906
    cout << "e^2（直接计算）= " << exp_result_direct << endl;  // 结果一致

    return 0;
}
```


### 示例 3：黄金分割比


黄金分割比 φ 的应用：


## 实例


```cpp
#include <iostream>
#include <numbers>

using namespace std;
using namespace std::numbers;

int main() {
    // 黄金分割比：长/宽 = φ 时为黄金矩形
    double width = 10.0;
    double golden_height = width * phi;  // 黄金矩形的高度
    cout << "宽度为" << width << "的黄金矩形高度：" << golden_height << endl;  // 输出：16.1803

    // 验证φ的数学定义：φ = (1 + √5)/2
    double phi_manual = (1 + sqrt(5.0)) / 2;
    cout << "手动计算的黄金分割比：" << phi_manual << endl;  // 与numbers::phi一致

    return 0;
}
```


### 示例 4：浮点类型


不同浮点类型的常量适配：


## 实例


```cpp
#include <iostream>
#include <numbers>
#include <iomanip>  // 用于设置输出精度

using namespace std;

int main() {
    // 设置高精度输出（显示15位小数）
    cout << fixed << setprecision(15);

    // float版π（单精度）
    float pi_float = std::numbers::pi_v<float>;
    cout << "float版π：" << pi_float << endl;  // 输出：3.141592741012573

    // double版π（双精度，默认）
    double pi_double = std::numbers::pi;
    cout << "double版π：" << pi_double << endl;  // 输出：3.141592653589793

    // long double版π（高精度）
    long double pi_long_double = std::numbers::pi_v<long double>;
    cout << "long double版π：" << pi_long_double << endl;  // 输出更精确的3.1415926535897932385...

    return 0;
}
```









	  AI 思考中...





			** [C++ 数据结构](https://www.runoob.com/cpp-data-structures.html)
			[C++ 导入标准库](https://www.runoob.com/cppo-import-header-file.html) **













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