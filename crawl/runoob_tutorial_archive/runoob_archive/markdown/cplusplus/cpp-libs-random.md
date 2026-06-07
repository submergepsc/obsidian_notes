# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-random.html

C++ 标准库中的 `` 头文件提供了一组用于生成随机数的工具，涵盖了从简单的均匀分布到复杂的离散分布，为需要随机数的应用程序提供了广泛的选择。这些工具对于模拟、游戏开发、加密算法等领域非常有用。


`` 不仅支持生成伪随机数，还支持种子控制、各种概率分布等，使得开发者可以灵活地生成符合特定需求的随机数序列。

`` 库由以下三个主要组件构成：

- **随机数引擎**：生成伪随机数的核心，用于控制生成过程的可重复性和随机性。
- **随机数分布**：控制生成的数值遵循的概率分布类型。
- **随机数适配器**：允许调整引擎行为，如 `discard_block` 等适配器。


在 C++ 中，随机数生成器（Random Number Generator, RNG）可以分为两大类：


- **伪随机数生成器**：它们使用确定性算法生成看似随机的数列。这些数列在理论上是可预测的，但通常对于大多数应用来说足够随机。
- **真随机数生成器**：它们基于物理过程（如热噪声、放射性衰变等）生成随机数，但 C++ 标准库不直接提供这类生成器。


### 常用随机数引擎

| 引擎 | 描述 |
| --- | --- |
| std::default_random_engine | 默认随机数引擎，实现依赖于具体编译器。 |
| std::minstd_rand | 线性同余引擎，产生均匀的伪随机数序列。 |
| std::mt19937 | 梅森旋转算法，适合通用随机数生成。 |
| std::mt19937_64 | 64 位的梅森旋转算法。 |
| std::ranlux24_base | 简化的减法进位引擎，用于高质量生成。 |
| std::knuth_b | Knuth shuffle 随机数生成器。 |

常用引擎如 `std::mt19937` 因为生成速度快且生成质量高，是普遍推荐的随机数生成引擎。生成器还可以使用 `seed()` 方法指定种子，便于生成可重复的伪随机序列。


### 随机数分布类型


**1、均匀分布**

| 分布 | 描述 |
| --- | --- |
| std::uniform_int_distribution | 生成在某个整数范围内的均匀分布。 |
| std::uniform_real_distribution | 生成在某个浮点数范围内的均匀分布。 |


```
std::mt19937 gen(seed);
std::uniform_int_distribution<int> dist(1, 100); // 生成 1 到 100 间的整数
int random_int = dist(gen);
```


**2、正态分布**


| 分布 | 描述 |
| --- | --- |
| std::normal_distribution | 标准正态分布，中心对称，常用于模拟自然现象。 |
| std::lognormal_distribution | 对数正态分布。 |


```
std::mt19937 gen(seed);
std::normal_distribution<> dist(0, 1); // 平均值为0，标准差为1
double random_normal = dist(gen);
```


**3、离散分布**


| 分布 | 描述 |
| --- | --- |
| std::discrete_distribution | 生成的随机数为一组特定概率的整数。 |
| std::bernoulli_distribution | 伯努利分布，只生成 true 或 false。 |
| std::binomial_distribution | 二项分布。 |


```
std::mt19937 gen(seed);
std::discrete_distribution<int> dist({40, 10, 50}); // 概率为40%、10%、50%
int random_discrete = dist(gen);
```


### 语法


使用 `` 库的基本步骤如下：


- 包含头文件 ``。
- 创建一个随机数生成器对象。
- 使用分布类生成随机数。


## 实例


### 生成基本的随机数


## 实例


```cpp
#include <iostream>
#include <random>

int main() {
    // 使用随机设备创建一个随机种子
    std::random_device rd;

    // 使用随机种子初始化 Mersenne Twister 随机数生成器
    std::mt19937 generator(rd());

    // 生成一个随机数
    std::cout << "Random number: " << generator() << std::endl;

    return 0;
}
```


输出结果：


```
Random number: 3499211612
```


**注意：**每次运行程序时，生成的随机数可能不同。


### 使用均匀分布


## 实例


```cpp
#include <iostream>
#include <random>

int main() {
    // 创建随机数生成器
    std::mt19937 generator;

    // 创建一个均匀分布的随机数生成器，范围从 1 到 10
    std::uniform_int_distribution<int> distribution(1, 10);

    // 生成并打印 5 个随机数
    for (int i = 0; i < 5; ++i) {
        std::cout << "Random number: " << distribution(generator) << std::endl;
    }

    return 0;
}
```


输出结果：


```
Random number: 7
Random number: 10
Random number: 6
Random number: 2
Random number: 4
```


每次运行程序时，输出的随机数序列可能不同。


### 使用正态分布


## 实例


```cpp
#include <iostream>
#include <random>
#include <iomanip>

int main() {
    // 创建随机数生成器
    std::mt19937 generator;

    // 创建一个正态分布的随机数生成器，均值为 0，标准差为 1
    std::normal_distribution<double> distribution(0.0, 1.0);

    // 设置输出格式，保留两位小数
    std::cout << std::fixed << std::setprecision(2);

    // 生成并打印 5 个随机数
    for (int i = 0; i < 5; ++i) {
        std::cout << "Random number: " << distribution(generator) << std::endl;
    }

    return 0;
}
```


```
Random number: -0.15
Random number: 0.13
Random number: -1.87
Random number: 0.46
Random number: -0.21
```


使用 mt19937 引擎生成不同分布的随机数：


## 实例


```cpp
#include <iostream>
#include <random>

int main() {
    // 1. 设置种子和随机数引擎
    std::random_device rd; // 随机设备产生种子
    std::mt19937 gen(rd()); // 梅森旋转引擎

    // 2. 均匀分布的整数
    std::uniform_int_distribution<> dist_int(1, 100);
    std::cout << "Uniform integer: " << dist_int(gen) << std::endl;

    // 3. 均匀分布的浮点数
    std::uniform_real_distribution<> dist_real(0.0, 1.0);
    std::cout << "Uniform real: " << dist_real(gen) << std::endl;

    // 4. 正态分布
    std::normal_distribution<> dist_normal(0, 1);
    std::cout << "Normal: " << dist_normal(gen) << std::endl;

    // 5. 离散分布
    std::discrete_distribution<> dist_discrete({10, 20, 70});
    std::cout << "Discrete: " << dist_discrete(gen) << std::endl;

    return 0;
}
```


### 随机数适配器

机数适配器允许调整生成行为，主要有两类适配器：

- `std::discard_block_engine`：丢弃一定数量的生成值，仅保留指定间隔的值，用于减少随机性。
- `std::independent_bits_engine`：生成指定位数的随机数，便于直接生成二进制数据。


## 实例


```cpp
#include <iostream>
#include <random>

int main() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::discard_block_engine<std::mt19937, 3, 2> discard_engine(gen);
    std::cout << "Discard block random number: " << discard_engine() << std::endl;

    return 0;
}
```


### 常见用法


- **使用种子生成可重复的随机序列**：指定相同的种子使得每次运行生成相同序列。
- **生成不同分布的随机数**：选择符合应用场景的分布函数，能更好地模拟实际问题。
- **调整生成器性能**：使用不同的随机引擎来平衡生成性能与精确度。









	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-utility.html)
			[C++ 标准库 ](https://www.runoob.com/cpp-libs-locale.html) **













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