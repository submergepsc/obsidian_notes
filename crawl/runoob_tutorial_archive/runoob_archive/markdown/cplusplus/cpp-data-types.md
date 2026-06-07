# C++ 数据类型

- Source: https://www.runoob.com/cplusplus/cpp-data-types.html

使用编程语言进行编程时，需要用到各种变量来存储各种信息。变量保留的是它所存储的值的内存位置。这意味着，当您创建一个变量时，就会在内存中保留一些空间。


您可能需要存储各种数据类型（比如字符型、宽字符型、整型、浮点型、双浮点型、布尔型等）的信息，操作系统会根据变量的数据类型，来分配内存和决定在保留内存中存储什么。


## 基本的内置类型


C++ 为程序员提供了种类丰富的内置数据类型和用户自定义的数据类型。下表列出了七种基本的 C++ 数据类型：


| 类型 | 关键字 |
| --- | --- |
| 布尔型 | bool |
| 字符型 | char |
| 整型 | int |
| 浮点型 | float |
| 双浮点型 | double |
| 无类型 | void |
| 宽字符型 | wchar_t |


其实 wchar_t 是这样来的：


```
typedef short int wchar_t;
```


所以 wchar_t 实际上的空间是和 short int 一样。


一些基本类型可以使用一个或多个类型修饰符进行修饰：


| 修饰符 | 描述 | 示例 |
| --- | --- | --- |
| signed | 表示有符号类型（默认） | signed int x = -10; |
| unsigned | 表示无符号类型 | unsigned int y = 10; |
| short | 表示短整型 | short int z = 100; |
| long | 表示长整型 | long int a = 100000; |
| const | 表示常量，值不可修改 | const int b = 5; |
| volatile | 表示变量可能被意外修改，禁止编译器优化 | volatile int c = 10; |
| mutable | 表示类成员可以在 const 对象中修改 | mutable int counter; |


下表显示了各种变量类型在内存中存储值时需要占用的内存，以及该类型的变量所能存储的最大值和最小值。


**注意：**不同系统会有所差异，一字节为 8 位。


**注意：**默认情况下，int、short、long都是带符号的，即 signed。


**注意：**long int 8 个字节，int 都是 4 个字节，早期的 C 编译器定义了 long int 占用 4 个字节，int 占用 2 个字节，新版的 C/C++ 标准兼容了早期的这一设定。


| 数据类型 | 描述 | 大小（字节） | 范围/取值示例 |
| --- | --- | --- | --- |
| bool | 布尔类型，表示真或假 | 1 | true 或 false |
| char | 字符类型，通常用于存储 ASCII 字符 | 1 | -128 到 127 或 0 到 255 |
| signed char | 有符号字符类型 | 1 | -128 到 127 |
| unsigned char | 无符号字符类型 | 1 | 0 到 255 |
| wchar_t | 宽字符类型，用于存储 Unicode 字符 | 2 或 4 | 取决于平台 |
| char16_t | 16 位 Unicode 字符类型（C++11 引入） | 2 | 0 到 65,535 |
| char32_t | 32 位 Unicode 字符类型（C++11 引入） | 4 | 0 到 4,294,967,295 |
| short | 短整型 | 2 | -32,768 到 32,767 |
| unsigned short | 无符号短整型 | 2 | 0 到 65,535 |
| int | 整型 | 4 | -2,147,483,648 到 2,147,483,647 |
| unsigned int | 无符号整型 | 4 | 0 到 4,294,967,295 |
| long | 长整型 | 4 或 8 | 取决于平台 |
| unsigned long | 无符号长整型 | 4 或 8 | 取决于平台 |
| long long | 长长整型（C++11 引入） | 8 | -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807 |
| unsigned long long | 无符号长长整型（C++11 引入） | 8 | 0 到 18,446,744,073,709,551,615 |
| float | 单精度浮点数 | 4 | 约 ±3.4e±38（6-7 位有效数字） |
| double | 双精度浮点数 | 8 | 约 ±1.7e±308（15 位有效数字） |
| long double | 扩展精度浮点数 | 8、12 或 16 | 取决于平台 |


### C++11 新增类型


| 数据类型 | 描述 | 示例 |
| --- | --- | --- |
| auto | 自动类型推断 | auto x = 10; |
| decltype | 获取表达式的类型 | decltype(x) y = 20; |
| nullptr | 空指针常量 | int* ptr = nullptr; |
| std::initializer_list | 初始化列表类型 | std::initializer_list list = {1, 2, 3}; |
| std::tuple | 元组类型，可以存储多个不同类型的值 | std::tuple t(1, 2.0, 'a'); |

**
注意，各种类型的存储大小与系统位数有关，但目前通用的以64位系统为主。

以下列出了32位系统与64位系统的存储大小的差别（windows 相同）：


![](https://www.runoob.com/wp-content/uploads/2014/09/32-64.jpg)


从上表可得知，变量的大小会根据编译器和所使用的电脑而有所不同。


下面实例会输出您电脑上各种数据类型的大小。


## 实例


```cpp
#include<iostream>
#include <limits>

using namespace std;

int main()
{
    cout << "type: \t\t" << "************size**************"<< endl;
    cout << "bool: \t\t" << "所占字节数：" << sizeof(bool);
    cout << "\t最大值：" << (numeric_limits<bool>::max)();
    cout << "\t\t最小值：" << (numeric_limits<bool>::min)() << endl;
    cout << "char: \t\t" << "所占字节数：" << sizeof(char);
    cout << "\t最大值：" << (numeric_limits<char>::max)();
    cout << "\t\t最小值：" << (numeric_limits<char>::min)() << endl;
    cout << "signed char: \t" << "所占字节数：" << sizeof(signed char);
    cout << "\t最大值：" << (numeric_limits<signed char>::max)();
    cout << "\t\t最小值：" << (numeric_limits<signed char>::min)() << endl;
    cout << "unsigned char: \t" << "所占字节数：" << sizeof(unsigned char);
    cout << "\t最大值：" << (numeric_limits<unsigned char>::max)();
    cout << "\t\t最小值：" << (numeric_limits<unsigned char>::min)() << endl;
    cout << "wchar_t: \t" << "所占字节数：" << sizeof(wchar_t);
    cout << "\t最大值：" << (numeric_limits<wchar_t>::max)();
    cout << "\t\t最小值：" << (numeric_limits<wchar_t>::min)() << endl;
    cout << "short: \t\t" << "所占字节数：" << sizeof(short);
    cout << "\t最大值：" << (numeric_limits<short>::max)();
    cout << "\t\t最小值：" << (numeric_limits<short>::min)() << endl;
    cout << "int: \t\t" << "所占字节数：" << sizeof(int);
    cout << "\t最大值：" << (numeric_limits<int>::max)();
    cout << "\t最小值：" << (numeric_limits<int>::min)() << endl;
    cout << "unsigned: \t" << "所占字节数：" << sizeof(unsigned);
    cout << "\t最大值：" << (numeric_limits<unsigned>::max)();
    cout << "\t最小值：" << (numeric_limits<unsigned>::min)() << endl;
    cout << "long: \t\t" << "所占字节数：" << sizeof(long);
    cout << "\t最大值：" << (numeric_limits<long>::max)();
    cout << "\t最小值：" << (numeric_limits<long>::min)() << endl;
    cout << "unsigned long: \t" << "所占字节数：" << sizeof(unsigned long);
    cout << "\t最大值：" << (numeric_limits<unsigned long>::max)();
    cout << "\t最小值：" << (numeric_limits<unsigned long>::min)() << endl;
    cout << "double: \t" << "所占字节数：" << sizeof(double);
    cout << "\t最大值：" << (numeric_limits<double>::max)();
    cout << "\t最小值：" << (numeric_limits<double>::min)() << endl;
    cout << "long double: \t" << "所占字节数：" << sizeof(long double);
    cout << "\t最大值：" << (numeric_limits<long double>::max)();
    cout << "\t最小值：" << (numeric_limits<long double>::min)() << endl;
    cout << "float: \t\t" << "所占字节数：" << sizeof(float);
    cout << "\t最大值：" << (numeric_limits<float>::max)();
    cout << "\t最小值：" << (numeric_limits<float>::min)() << endl;
    cout << "size_t: \t" << "所占字节数：" << sizeof(size_t);
    cout << "\t最大值：" << (numeric_limits<size_t>::max)();
    cout << "\t最小值：" << (numeric_limits<size_t>::min)() << endl;
    cout << "string: \t" << "所占字节数：" << sizeof(string) << endl;
    // << "\t最大值：" << (numeric_limits<string>::max)() << "\t最小值：" << (numeric_limits<string>::min)() << endl;
    cout << "type: \t\t" << "************size**************"<< endl;
    return 0;
}
```


本实例使用了 endl**，这将在每一行后插入一个换行符，**







	  AI 思考中...





			** [C++ 注释](https://www.runoob.com/cpp-comments.html)
			[C++ 变量类型](https://www.runoob.com/cpp-variable-types.html) **