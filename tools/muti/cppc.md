 [TOC]
# C++ Lambda表达式详解
## 1. Lambda表达式的基本概念
Lambda表达式是C++11引入的重要特性，用于创建匿名函数对象（闭包）。
### 基本语法
```cpp
[capture](parameters) -> return_type {
    // 函数体
}
```
## 2. Lambda表达式的组成部分
### 2.1 捕获列表 [capture]
```cpp
// 1. 值捕获
int x = 10;
auto lambda1 = [x]() { return x * 2; };
// 2. 引用捕获
int y = 20;
auto lambda2 = [&y]() { y++; return y; };
// 3. 隐式捕获
int a = 1, b = 2;
auto lambda3 = [=]() { return a + b; };  // 隐式值捕获所有变量
auto lambda4 = [&]() { a++; b++; };       // 隐式引用捕获所有变量
// 4. 混合捕获
int m = 5, n = 6;
auto lambda5 = [=, &n]() { return m + n; };  // m值捕获，n引用捕获
auto lambda6 = [&, m]() { return n + m; };   // n引用捕获，m值捕获
// 5. this指针捕获
class MyClass {
    int value = 100;
public:
    void func() {
        auto lambda = [this]() { return value; };
    }
};
```
### 2.2 参数列表 (parameters)
```cpp
// 带参数的lambda
auto add = [](int a, int b) { return a + b; };
auto result = add(5, 3);  // 8
// 默认参数（C++14起）
auto greet = [](const std::string& name = "World") {
    std::cout << "Hello, " << name << "!\n";
};
greet();      // Hello, World!
greet("Alice"); // Hello, Alice!
// auto参数（C++14起）
auto autoParam = [](auto x, auto y) { return x + y; };
autoParam(5, 3.14);  // 返回8.14
```
### 2.3 返回类型 -> return_type
```cpp
// 显式指定返回类型
auto lambda1 = [](double a, double b) -> int {
    return static_cast<int>(a + b);
};
// 自动推导返回类型（C++14起）
auto lambda2 = [](auto a, auto b) {
    return a + b;  // 类型自动推导
};
// 复杂返回类型示例
auto make_pair = []() -> std::pair<int, std::string> {
    return {42, "answer"};
};
```
### 2.4 mutable关键字
```cpp
int counter = 0;
// 错误：值捕获的变量默认是const
// auto lambda1 = [counter]() { counter++; };
// 正确：使用mutable修改值捕获的变量
auto lambda2 = [counter]() mutable {
    counter++;
    std::cout << "Counter: " << counter << "\n";
};
lambda2();  // Counter: 1
lambda2();  // Counter: 2
std::cout << "Original counter: " << counter << "\n";  // 仍然是0
```
## 3. Lambda表达式的实际应用
### 3.1 与STL算法结合
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    // 使用lambda过滤偶数
    numbers.erase(std::remove_if(numbers.begin(), numbers.end(),
        [](int n) { return n % 2 == 0; }), numbers.end());
    // 使用lambda排序
    std::sort(numbers.begin(), numbers.end(), 
        [](int a, int b) { return a > b; });
    // 使用lambda转换
    std::vector<int> squares;
    std::transform(numbers.begin(), numbers.end(), 
        std::back_inserter(squares),
        [](int n) { return n * n; });
    // 使用lambda累加
    int sum = std::accumulate(numbers.begin(), numbers.end(), 0,
        [](int total, int n) { return total + n; });
    // 使用lambda查找
    auto it = std::find_if(numbers.begin(), numbers.end(),
        [](int n) { return n > 5; });
    return 0;
}
```
### 3.2 异步编程和回调
```cpp
#include <iostream>
#include <thread>
#include <future>
int main() {
    // 使用lambda创建线程
    std::thread t([]() {
        std::cout << "Hello from thread!\n";
    });
    t.join();
    // 使用lambda创建异步任务
    auto future = std::async([](int x, int y) {
        return x * y;
    }, 6, 7);
    std::cout << "Result: " << future.get() << "\n";
    // 定时任务回调
    std::function<void()> callback = []() {
        std::cout << "Callback executed\n";
    };
    return 0;
}
```
### 3.3 自定义比较器和函数对象
```cpp
#include <iostream>
#include <set>
#include <map>
int main() {
    // 自定义set比较器
    auto comp = [](const std::string& a, const std::string& b) {
        return a.length() < b.length();
    };
    std::set<std::string, decltype(comp)> stringSet(comp);
    // 自定义map比较器
    auto mapComp = [](int a, int b) { return a > b; };
    std::map<int, std::string, decltype(mapComp)> sortedMap(mapComp);
    // 函数对象存储
    std::vector<std::function<int(int, int)>> operations;
    operations.push_back([](int a, int b) { return a + b; });
    operations.push_back([](int a, int b) { return a - b; });
    operations.push_back([](int a, int b) { return a * b; });
    for (auto& op : operations) {
        std::cout << op(10, 5) << "\n";
    }
    return 0;
}
```
## 4. Lambda的高级特性
### 4.1 泛型Lambda（C++14起）
```cpp
auto generic_lambda = [](auto container) {
    for (auto& item : container) {
        std::cout << item << " ";
    }
    std::cout << "\n";
};
std::vector<int> v = {1, 2, 3};
std::list<std::string> l = {"a", "b", "c"};
generic_lambda(v);  // 1 2 3
generic_lambda(l);  // a b c
```
### 4.2 模板Lambda（C++20起）
```cpp
// C++20支持模板参数
auto template_lambda = []<typename T>(const std::vector<T>& vec) {
    return vec.size();
};
std::vector<int> vi = {1, 2, 3};
std::vector<double> vd = {1.1, 2.2};
std::cout << template_lambda(vi) << "\n";  // 3
std::cout << template_lambda(vd) << "\n";  // 2
```
### 4.3 捕获表达式（C++14起）
```cpp
// 初始化捕获（移动语义）
std::unique_ptr<int> ptr = std::make_unique<int>(42);
auto lambda = [ptr = std::move(ptr)]() {
    return *ptr;
};
// 捕获表达式
int x = 10;
auto lambda2 = [y = x + 5]() { return y; };  // y = 15
```
## 5. Lambda的性能特点
```cpp
#include <chrono>
#include <functional>
void benchmark() {
    auto start = std::chrono::high_resolution_clock::now();
    // Lambda通常比std::function更快
    auto lambda = [](int x) { return x * x; };
    // 而std::function有类型擦除开销
    std::function<int(int)> func = lambda;
    // 内联优化
    std::vector<int> nums(1000000);
    std::generate(nums.begin(), nums.end(),
        [n = 0]() mutable { return n++; });
    // 编译器通常能内联lambda
    std::transform(nums.begin(), nums.end(), nums.begin(),
        [](int x) { return x * 2; });
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cout << "Time: " << duration.count() << "ms\n";
}
```
## 6. Lambda的最佳实践
### 6.1 保持Lambda简洁
```cpp
// 不好：过于复杂的lambda
auto bad_lambda = [](const std::vector<int>& vec) -> std::vector<int> {
    std::vector<int> result;
    // ... 复杂逻辑
    return result;
};
// 好：复杂逻辑提取到函数
auto good_lambda = [](const std::vector<int>& vec) {
    return processVector(vec);
};
```
### 6.2 注意捕获的变量生命周期
```cpp
std::function<int()> create_lambda() {
    int local_var = 42;
    // 危险：捕获了局部变量的引用
    // return [&local_var]() { return local_var; };
    // 安全：值捕获
    return [local_var]() { return local_var; };
}
```
### 6.3 使用auto避免类型问题
```cpp
// 使用auto接收lambda
auto lambda = [](int x) { return x * 2; };
// 不要使用函数指针（除非无捕获）
int (*func_ptr)(int) = [](int x) { return x; };  // 仅适用于无捕获lambda
```
## 7. Lambda与函数对象的对比
```cpp
// 传统的函数对象
struct AddFunctor {
    int operator()(int a, int b) const {
        return a + b;
    }
};
// Lambda表达式
auto add_lambda = [](int a, int b) { return a + b; };
// 使用对比
int main() {
    AddFunctor functor;
    std::cout << functor(3, 4) << "\n";     // 7
    std::cout << add_lambda(3, 4) << "\n";  // 7
    // Lambda的优势：闭包能力
    int base = 100;
    auto add_with_base = [base](int x) { return base + x; };
    std::cout << add_with_base(50) << "\n";  // 150
    return 0;
}
```
## 总结
C++ Lambda表达式的主要作用：
1. **创建匿名函数**：就地定义函数，无需命名
2. **实现闭包**：捕获外部变量，形成闭包
3. **简化STL算法**：为算法提供简洁的谓词和操作
4. **提高代码可读性**：将逻辑放在使用的地方
5. **支持函数式编程**：作为一等公民传递函数
6. **优化性能**：通常可以被编译器内联优化
7. **增强泛型编程**：支持auto参数和模板参数
Lambda表达式是现代C++编程中不可或缺的工具，它极大地提高了代码的表达能力和灵活性。
# string用法
这是一个整理好的 `std::string` 常用函数速查表，分为 **成员函数** 和 **常用非成员辅助函数** 两部分，方便你复习和查阅。
### 1. `std::string` 核心成员函数速查表
| **分类** | **函数名**                | **功能描述**             | **常用写法示例**                   | **核心注意点/返回值**                                     |
| -------- | ------------------------- | ------------------------ | ---------------------------------- | --------------------------------------------------------- |
| **容量** | **`size()`** / `length()` | 返回字符串长度（字符数） | `int len = s.size();`              | 两者完全等价，推荐用 `size()` 以适配 STL 风格。           |
|          | **`empty()`**             | 判断是否为空             | `if (s.empty()) ...`               | 比 `s.size() == 0` 语义更清晰且效率略高。                 |
|          | `clear()`                 | 清空字符串               | `s.clear();`                       | 变成空串 `""`，`size()` 变为 0。                          |
| **访问** | **`operator[]`**          | 下标访问（不检查越界）   | `char c = s[i];`                   | **速度最快**，但越界会导致程序崩溃。                      |
|          | `at()`                    | 下标访问（检查越界）     | `char c = s.at(i);`                | 若越界抛出 `std::out_of_range` 异常，更安全。             |
|          | `back()`                  | 访问最后一个字符         | `s.back() = 'a';`                  | C++11 引入，方便修改末尾字符。                            |
| **修改** | **`operator+=`**          | 追加字符串或字符         | `s += "abc";`   `s += 'A';`        | 最常用的拼接方式，支持链式调用。                          |
|          | `push_back()`             | 尾部添加**一个**字符     | `s.push_back('X');`                | 仅支持单字符 `char`。                                     |
|          | `pop_back()`              | 删除尾部**一个**字符     | `s.pop_back();`                    | 字符串必须非空，否则未定义行为。                          |
|          | `append()`                | 追加内容                 | `s.append(str);`                   | 功能比 `+=` 更丰富，可指定追加某字符串的一部分。          |
|          | `insert()`                | 插入字符/字符串          | `s.insert(pos, "str");`            | 在下标 `pos` **之前**插入。复杂度 $O(N)$。                |
|          | `erase()`                 | 删除部分内容             | `s.erase(pos, len);`               | 从 `pos` 开始删 `len` 个。**省略 `len` 则删到末尾**。     |
|          | `replace()`               | 替换部分内容             | `s.replace(pos, len, "str");`      | 将从 `pos` 开始的 `len` 个字符替换为新串。                |
| **查找** | **`substr()`**            | 截取子串                 | `string sub = s.substr(pos, len);` | **极常用**。省略 `len` 则截取到末尾。返回新 string 对象。 |
|          | **`find()`**              | 正向查找子串/字符        | `size_t p = s.find("key");`        | 找到返回下标；**找不到返回 `string::npos`**。             |
|          | `rfind()`                 | 反向查找（从右往左）     | `size_t p = s.rfind("key");`       | 找最后一次出现的位置。                                    |
| **转换** | **`c_str()`**             | 转为 C 风格字符串        | `printf("%s", s.c_str());`         | 返回 `const char*`，用于兼容 C 接口（如 `fopen`）。       |
|          | `data()`                  | 获取底层数据指针         | `char* p = s.data();`              | C++17 后返回非 const 指针，可直接修改内存。               |
------
### 2. 常用类型转换辅助函数 (非成员函数)
这些函数**不属于** string 类内部，而是定义在全局的辅助函数，用于 string 和数字互转。
| **函数名**             | **功能**                       | **示例**                              | **说明**                                            |
| ---------------------- | ------------------------------ | ------------------------------------- | --------------------------------------------------- |
| **`std::to_string()`** | 数值 $\rightarrow$ String      | `string s = to_string(123);`          | 支持 int, long long, double, float 等所有数值类型。 |
| **`std::stoi()`**      | String $\rightarrow$ int       | `int n = stoi("123");`                | 自动跳过前导空格。若无法转换会抛异常。              |
| **`std::stoll()`**     | String $\rightarrow$ long long | `long long n = stoll("10000000000");` | 处理大整数使用。                                    |
| **`std::stod()`**      | String $\rightarrow$ double    | `double d = stod("3.14");`            | 处理浮点数使用。                                    |
------
### 3. 两个新手常犯的错误
1. **`find` 的返回值判断**：
   - **错误写法**：`if (s.find("abc") == -1)`
   - **正确写法**：`if (s.find("abc") != std::string::npos)`
   - *原因*：返回值类型是 `size_t` (无符号整数)，虽然强转后可能等于 -1，但标准做法是和 `npos` 比较。
2. **`substr` 的参数**：
   - `s.substr(pos, len)` 的第二个参数是**长度**，不是结束下标。
   - 例如 `s = "abcde"`, `s.substr(1, 3)` 得到的是 `"bcd"` (从下标1开始，取3个)，而不是 `"bc"`。
# erase
​	
