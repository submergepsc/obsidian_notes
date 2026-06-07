# C++ 数字

- Source: https://www.runoob.com/cplusplus/cpp-numbers.html

通常，当我们需要用到数字时，我们会使用原始的数据类型，如 int、short、long、float 和 double 等等。这些用于数字的数据类型，其可能的值和数值范围，我们已经在 C++ 数据类型一章中讨论过。


## C++ 定义数字


我们已经在之前章节的各种实例中定义过数字。下面是一个 C++ 中定义各种类型数字的综合实例：


## 实例


```cpp
#include <iostream>
using namespace std;

int main ()
{
   // 数字定义
   short  s;
   int    i;
   long   l;
   float  f;
   double d;

   // 数字赋值
   s = 10;
   i = 1000;
   l = 1000000;
   f = 230.47;
   d = 30949.374;

   // 数字输出
   cout << "short  s :" << s << endl;
   cout << "int    i :" << i << endl;
   cout << "long   l :" << l << endl;
   cout << "float  f :" << f << endl;
   cout << "double d :" << d << endl;

   return 0;
}
```


当上面的代码被编译和执行时，它会产生下列结果：


```
short  s :10
int    i :1000
long   l :1000000
float  f :230.47
double d :30949.4
```


## C++ 数学运算


在 C++ 中，除了可以创建各种函数，还包含了各种有用的函数供您使用。这些函数写在标准 C 和 C++ 库中，叫做**内置**函数。您可以在程序中引用这些函数。


C++ 内置了丰富的数学函数，可对各种数字进行运算。下表列出了 C++ 中一些有用的内置的数学函数。


为了利用这些函数，您需要引用数学头文件 ****。


| 序号 | 函数 & 描述 |
| --- | --- |
| 1 | double cos(double);该函数返回弧度角（double 型）的余弦。 |
| 2 | double sin(double);该函数返回弧度角（double 型）的正弦。 |
| 3 | double tan(double);该函数返回弧度角（double 型）的正切。 |
| 4 | double log(double);该函数返回参数的自然对数。 |
| 5 | double pow(double, double);假设第一个参数为 x，第二个参数为 y，则该函数返回 x 的 y 次方。 |
| 6 | double hypot(double, double);该函数返回两个参数的平方总和的平方根，也就是说，参数为一个直角三角形的两个直角边，函数会返回斜边的长度。 |
| 7 | double sqrt(double);该函数返回参数的平方根。 |
| 8 | int abs(int);该函数返回整数的绝对值。 |
| 9 | double fabs(double);该函数返回任意一个浮点数的绝对值。 |
| 10 | double floor(double);该函数返回一个小于或等于传入参数的最大整数。 |


下面是一个关于数学运算的简单实例：


## 实例


```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main ()
{
   // 数字定义
   short  s = 10;
   int    i = -1000;
   long   l = 100000;
   float  f = 230.47;
   double d = 200.374;

   // 数学运算
   cout << "sin(d) :" << sin(d) << endl;
   cout << "abs(i)  :" << abs(i) << endl;
   cout << "floor(d) :" << floor(d) << endl;
   cout << "sqrt(f) :" << sqrt(f) << endl;
   cout << "pow( d, 2) :" << pow(d, 2) << endl;

   return 0;
}
```


当上面的代码被编译和执行时，它会产生下列结果：


```
sin(d) :-0.634939
abs(i)  :1000
floor(d) :200
sqrt(f) :15.1812
pow( d, 2 ) :40149.7
```


## C++ 随机数


在许多情况下，需要生成随机数。关于随机数生成器，有两个相关的函数。一个是 **rand()**，该函数只返回一个伪随机数。生成随机数之前必须先调用 **srand()** 函数。


下面是一个关于生成随机数的简单实例。实例中使用了 **time()** 函数来获取系统时间的秒数，通过调用 rand() 函数来生成随机数：


## 实例


```cpp
#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int main ()
{
   int i,j;

   // 设置种子
   srand( (unsigned)time( NULL ) );

   /* 生成 10 个随机数 */
   for( i = 0; i < 10; i++ )
   {
      // 生成实际的随机数
      j= rand();
      cout <<"随机数： " << j << endl;
   }

   return 0;
}
```


当上面的代码被编译和执行时，它会产生下列结果：


```
随机数： 1748144778
随机数： 630873888
随机数： 2134540646
随机数： 219404170
随机数： 902129458
随机数： 920445370
随机数： 1319072661
随机数： 257938873
随机数： 1256201101
随机数： 580322989
```


---


## C++ 数学常数

在 C++ 中，数学常数（如 π、e、黄金比例等）是许多算法和应用中不可或缺的部分，虽然早期版本的 C++ 中没有直接提供这些常数，但从 C++20 开始，标准库引入了几个常用的数学常数，并提供了更高效和统一的方式来访问它们。

更多内容参考：[C++ 标准库 ``](https://www.runoob.com/cpp-libs-numbers.html)。


### π

- 常量：`std::numbers::pi`
- 类型：`std::float32_t`（32位浮动）、`std::float64_t`（64位浮动）


## 实例


```cpp
#include <cmath>
#include <iostream>

int main() {
    std::cout << "pi: " << std::numbers::pi << std::endl;
}
```


### 自然对数的底数 e (Euler's Number)

- 常量：`std::numbers::e`
- 类型：`std::float32_t`、`std::float64_t`


```
std::cout << "e: " << std::numbers::e << std::endl;
```


### 黄金比例 φ (Golden Ratio)

- 常量：`std::numbers::phi`
- 类型：`std::float32_t`、`std::float64_t`


```
std::cout << "phi: " << std::numbers::phi << std::endl;
```


## 实例


```cpp
#include <iostream>
#include <cmath>
#include <numbers>

int main() {
    std::cout << "pi: " << std::numbers::pi << std::endl;
    std::cout << "e: " << std::numbers::e << std::endl;
    std::cout << "phi: " << std::numbers::phi << std::endl;

    return 0;
}
```


输出结果为：


```
pi: 3.14159
e: 2.71828
phi: 1.61803
```










	  AI 思考中...





			** [C++ 函数](https://www.runoob.com/cpp-functions.html)
			[C++ 数组](https://www.runoob.com/cpp-arrays.html) **