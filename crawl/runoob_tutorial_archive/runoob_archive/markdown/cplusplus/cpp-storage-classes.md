# C++ 存储类

- Source: https://www.runoob.com/cplusplus/cpp-storage-classes.html

存储类定义 C++ 程序中变量/函数的范围（可见性）和生命周期。这些说明符放置在它们所修饰的类型之前。下面列出 C++ 程序中可用的存储类：


- **auto**：这是默认的存储类说明符，通常可以省略不写。auto 指定的变量具有自动存储期，即它们的生命周期仅限于定义它们的块（block）。auto 变量通常在栈上分配。
- **register**：用于建议编译器将变量存储在CPU寄存器中以提高访问速度。在 C++11 及以后的版本中，register 已经是一个废弃的特性，不再具有实际作用。
- **static**：用于定义具有静态存储期的变量或函数，它们的生命周期贯穿整个程序的运行期。在函数内部，static变量的值在函数调用之间保持不变。在文件内部或全局作用域，static变量具有内部链接，只能在定义它们的文件中访问。
- **extern**：用于声明具有外部链接的变量或函数，它们可以在多个文件之间共享。默认情况下，全局变量和函数具有 extern 存储类。在一个文件中使用extern声明另一个文件中定义的全局变量或函数，可以实现跨文件共享。
- **mutable (C++11)**：用于修饰类中的成员变量，允许在const成员函数中修改这些变量的值。通常用于缓存或计数器等需要在const上下文中修改的数据。
- **thread_local (C++11)**：用于定义具有线程局部存储期的变量，每个线程都有自己的独立副本。线程局部变量的生命周期与线程的生命周期相同。


从 C++ 17 开始，auto 关键字不再是 C++ 存储类说明符，且 register 关键字被弃用。


中的存储类说明符为程序员提供了控制变量和函数生命周期及可见性的手段。

合理使用存储类说明符可以提高程序的可维护性和性能。

从 C++11 开始，register 已经失去了原有的作用，而 mutable 和 thread_local 则是新引入的特性，用于解决特定的编程问题。


下面是一个展示不同存储类说明符的实例：


## 实例


```cpp
#include <iostream>

// 全局变量，具有外部链接，默认存储类为extern
int globalVar;

void function() {
    // 局部变量，具有自动存储期，默认存储类为auto
    auto int localVar = 10;

    // 静态变量，具有静态存储期，生命周期贯穿整个程序
    static int staticVar = 20;

    const int constVar = 30; // const变量默认具有static存储期

    // 尝试修改const变量，编译错误
    // constVar = 40;

    // mutable成员变量，可以在const成员函数中修改
    class MyClass {
    public:
        mutable int mutableVar;

        void constMemberFunc() const {
            mutableVar = 50; // 允许修改mutable成员变量
        }
    };

    // 线程局部变量，每个线程有自己的独立副本
    thread_local int threadVar = 60;
}

int main() {
    extern int externalVar; // 声明具有外部链接的变量

    function();

    return 0;
}
```


## auto 存储类


自 C++ 11 以来，**auto** 关键字用于两种情况：声明变量时根据初始化表达式自动推断该变量的类型、声明函数时函数返回值的占位符。

C++98 标准中 auto 关键字用于自动变量的声明，但由于使用极少且多余，在 C++17 中已删除这一用法。


根据初始化表达式自动推断被声明的变量的类型，如：


```cpp
auto f=3.14;      //double
auto s("hello");  //const char*
auto z = new auto(9); // int*
auto x1 = 5, x2 = 5.0, x3='r';//错误，必须是初始化为同一类型
```


## register 存储类

register 是一种存储类（storage class），用于声明变量，并提示编译器将这些变量存储在寄存器中，以便快速访问。


使用 register 关键字可以提高程序的执行速度，因为它减少了对内存的访问次数。

然而，需要注意的是，register 存储类只是一种提示，编译器可以忽略它，因为现代的编译器通常会自动优化代码，选择合适的存储位置。


**语法格式：**


```
register data_type variable_name;
```


- `register` 是存储类的关键字，用于提示编译器将变量存储在寄存器中。
- `data_type` 是变量的数据类型，可以是任何合法的 C++ 数据类型。
- `variable_name` 是变量的名称。


```cpp
void loop() {
    register int i;
    for (i = 0; i < 1000; ++i) {
        // 循环体
    }
}
```


register 存储类用于提示编译器将变量存储在寄存器中，以便提高访问速度。然而，由于现代编译器的自动优化能力，使用 register 关键字并不是必需的，而且在实践中很少使用。


在 C++11 标准中，register 关键字不再是一个存储类说明符，而是一个废弃的特性。这意味着在 C++11 及以后的版本中，使用 register 关键字将不会对程序产生任何影响。


在 C++ 中，可以使用引用或指针来提高访问速度，尤其是在处理大型数据结构时。


## static 存储类


**static** 存储类指示编译器在程序的生命周期内保持局部变量的存在，而不需要在每次它进入和离开作用域时进行创建和销毁。因此，使用 static 修饰局部变量可以在函数调用之间保持局部变量的值。


static 修饰符也可以应用于全局变量。当 static 修饰全局变量时，会使变量的作用域限制在声明它的文件内。


在 C++ 中，当 static 用在类数据成员上时，会导致仅有一个该成员的副本被类的所有对象共享。


## 实例


```cpp
#include <iostream>

// 函数声明
void func(void);

static int count = 10; /* 全局变量 */

int main()
{
    while(count--)
    {
       func();
    }
    return 0;
}
// 函数定义
void func( void )
{
    static int i = 5; // 局部静态变量
    i++;
    std::cout << "变量 i 为 " << i ;
    std::cout << " , 变量 count 为 " << count << std::endl;
}
```


当上面的代码被编译和执行时，它会产生下列结果：


```
变量 i 为 6 , 变量 count 为 9
变量 i 为 7 , 变量 count 为 8
变量 i 为 8 , 变量 count 为 7
变量 i 为 9 , 变量 count 为 6
变量 i 为 10 , 变量 count 为 5
变量 i 为 11 , 变量 count 为 4
变量 i 为 12 , 变量 count 为 3
变量 i 为 13 , 变量 count 为 2
变量 i 为 14 , 变量 count 为 1
变量 i 为 15 , 变量 count 为 0
```


## extern 存储类


**extern** 存储类用于提供一个全局变量的引用，全局变量对所有的程序文件都是可见的。当您使用 'extern' 时，对于无法初始化的变量，会把变量名指向一个之前定义过的存储位置。


当您有多个文件且定义了一个可以在其他文件中使用的全局变量或函数时，可以在其他文件中使用 *extern* 来得到已定义的变量或函数的引用。可以这么理解，*extern* 是用来在另一个文件中声明一个全局变量或函数。


extern 修饰符通常用于当有两个或多个文件共享相同的全局变量或函数的时候，如下所示：


第一个文件：main.cpp


## 实例


```cpp
#include <iostream>

int count ;
extern void write_extern();

int main()
{
   count = 5;
   write_extern();
}
```


第二个文件：support.cpp


## 实例


```cpp
#include <iostream>

extern int count;

void write_extern(void)
{
   std::cout << "Count is " << count << std::endl;
}
```


在这里，第二个文件中的 *extern* 关键字用于声明已经在第一个文件 main.cpp 中定义的 count。现在 ，编译这两个文件，如下所示：


```
$ g++ main.cpp support.cpp -o write
```


这会产生 **write** 可执行程序，尝试执行 **write**，它会产生下列结果：


```
$ ./write
Count is 5
```


## mutable 存储类


mutable 是一个关键字，用于修饰类的成员变量，使其能够在 const 成员函数中被修改。通常情况下，const 成员函数不能修改对象的状态，但如果某个成员变量被声明为 mutable，则可以在 const 函数中对其进行修改。


**特点：**


- **允许修改**：`mutable` 成员变量可以在 `const` 成员函数内被改变。
- **设计目的**：通常用于需要在不改变对象外部状态的情况下进行状态管理的场景，比如缓存、延迟计算等。


## 实例


```cpp
#include <iostream>

class Example {
public:
    Example() : value(0), cachedValue(0) {}

    // 常量成员函数
    int getValue() const {
        return value; // 读取常量成员
    }

    // 修改 mutable 成员
    void increment() {
        ++value;
        cachedValue = value * 2; // 修改 mutable 成员
    }

    int getCachedValue() const {
        return cachedValue; // 读取 mutable 成员
    }

private:
    int value;                 // 常规成员，不能在 const 函数中修改
    mutable int cachedValue;   // 可修改成员，可以在 const 函数中修改
};

int main() {
    const Example ex;
    // ex.increment(); // 错误：无法在 const 对象上调用非 const 函数
    // ex.value = 10;  // 错误：无法修改 const 对象的成员

    std::cout << "Value: " << ex.getValue() << std::endl;
    std::cout << "Cached Value: " << ex.getCachedValue() << std::endl; // 输出为 0

    return 0;
}
```


**适用场景：**


- **缓存**：在 `const` 函数中计算并缓存结果，而不影响对象的外部状态。
- **状态跟踪**：如日志计数器，跟踪调用次数等信息，避免对类的逻辑进行侵入式修改。

**注意事项：**


- `mutable` 变量的使用应谨慎，以免导致意外的状态变化，影响代码的可读性和可维护性。
- `mutable` 适用于需要在 `const` 环境中更改状态的特定情况，而不是普遍的设计模式。


## thread_local 存储类

thread_local 是 C++11 引入的一种存储类，用于在多线程环境中管理线程特有的变量。

使用 thread_local 修饰的变量在每个线程中都有独立的实例，因此每个线程对该变量的操作不会影响其他线程。


- **独立性**：每个线程都有自己独立的变量副本，不同线程之间的读写操作互不干扰。
- **生命周期**：`thread_local` 变量在其线程结束时自动销毁。
- **初始化**：`thread_local` 变量可以进行静态初始化或动态初始化，支持在声明时初始化。

thread_local 适合用于需要存储线程状态、缓存或者避免数据竞争的场景，如线程池、请求上下文等。


以下演示了可以被声明为 thread_local 的变量：


```cpp
#include <iostream>
#include <thread>

thread_local int threadSpecificVar = 0; // 每个线程都有自己的 threadSpecificVar

void threadFunction(int id) {
    threadSpecificVar = id; // 设置线程特有的变量
    std::cout << "Thread " << id << ": threadSpecificVar = " << threadSpecificVar << std::endl;
}

int main() {
    std::thread t1(threadFunction, 1);
    std::thread t2(threadFunction, 2);

    t1.join();
    t2.join();

    return 0;
}
```


**注意事项：**


- **性能**：由于每个线程都有独立的副本，`thread_local` 变量的访问速度可能比全局或静态变量稍慢。
- **静态存储**：`thread_local` 变量的存储类型为静态存储持续时间，因此在程序整个运行期间会一直存在。








	  AI 思考中...





			** [C++ 修饰符类型](https://www.runoob.com/cpp-modifier-types.html)
			[C++ 运算符](https://www.runoob.com/cpp-operators.html) **