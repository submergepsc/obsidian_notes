# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-valarray.html

C++ 的 `` 库是一个用于数值计算的库，它提供了一种高效的方式来处理数值数组。`` 库中的 `valarray` 类模板允许程序员对数组进行元素级的数学运算，包括加法、减法、乘法、除法等。此外，它还支持更高级的数学函数，如指数、对数、正弦、余弦等。


`valarray` 是 C++ 标准库中的一个类模板，用于表示和操作数值数组。它提供了一种方便的方式来执行数组的元素级操作。


### 语法


`valarray` 的基本语法如下：


```
#include <valarray>

int main() {
    std::valarray<double> va(10); // 创建一个包含10个double元素的valarray
    va = 1; // 将所有元素初始化为1
    // ...
    return 0;
}
```


## 实例

### 1. 创建和初始化 valarray


## 实例


```cpp
#include <iostream>
#include <valarray>

int main() {
    std::valarray<double> va(5); // 创建一个包含5个double元素的valarray
    va = {1.0, 2.0, 3.0, 4.0, 5.0}; // 初始化valarray

    for (auto i : va) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}
```


输出结果:


```
1 2 3 4 5
```


### 2. 基本运算


## 实例


```cpp
#include <iostream>
#include <valarray>

int main() {
    std::valarray<double> va1(5), va2(5);
    va1 = {1.0, 2.0, 3.0, 4.0, 5.0};
    va2 = {2.0, 3.0, 4.0, 5.0, 6.0};

    std::valarray<double> sum = va1 + va2; // 加法
    std::valarray<double> diff = va1 - va2; // 减法
    std::valarray<double> prod = va1 * va2; // 乘法
    std::valarray<double> quot = va1 / va2; // 除法

    std::cout << "Sum: ";
    for (auto i : sum) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    std::cout << "Difference: ";
    for (auto i : diff) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    std::cout << "Product: ";
    for (auto i : prod) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    std::cout << "Quotient: ";
    for (auto i : quot) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}
```


输出结果:


```
Sum: 3 5 7 9 11
Difference: -1 -1 1 1 -1
Product: 2 6 12 20 30
Quotient: 0.5 0.6666667 0.75 0.8 0.8333334
```


### 3. 使用 valarray 进行数学函数操作


## 实例


```cpp
#include <iostream>
#include <valarray>
#include <cmath>

int main() {
    std::valarray<double> va(5);
    va = {1.0, 2.0, 3.0, 4.0, 5.0};

    std::valarray<double> squares = va * va; // 平方
    std::valarray<double> roots = std::sqrt(va); // 开方

    std::cout << "Squares: ";
    for (auto i : squares) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    std::cout << "Square Roots: ";
    for (auto i : roots) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    return 0;
}
```


输出结果:


```
Squares: 1 4 9 16 25
Square Roots: 1 1.4142136 1.7320508
```









	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-complex.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-string.html) **













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