# C 标准库

- Source: https://www.runoob.com/cprogramming/c-standard-library-fenv-h.html

### C 标准库


`` 是 C 标准库中的一个头文件，用于控制浮点环境（Floating-Point Environment）。


`` 在 C99 标准中引入，提供了对浮点异常、舍入模式和其他浮点状态的控制和查询功能。


---


`` 的主要目的是：


- 检测和处理浮点异常（如除以零、溢出等）。
- 控制浮点运算的舍入模式（如向零舍入、向最近舍入等）。
- 查询和修改浮点状态标志。


---


### 1、浮点异常


浮点异常是指在浮点运算中发生的特殊情况，例如：


- **FE_DIVBYZERO**：除以零。
- **FE_INEXACT**：不精确结果。
- **FE_INVALID**：无效操作（如对负数开平方）。
- **FE_OVERFLOW**：上溢。
- **FE_UNDERFLOW**：下溢。


这些异常通过浮点状态标志来表示，可以通过 `` 中的函数检测和处理。


---


### 2、舍入模式


舍入模式控制浮点运算结果的舍入方式。`` 定义了以下舍入模式：


- **FE_TONEAREST**：向最接近的值舍入（默认模式）。
- **FE_DOWNWARD**：向负无穷舍入。
- **FE_UPWARD**：向正无穷舍入。
- **FE_TOWARDZERO**：向零舍入。


---


### 3、主要函数和宏


`` 提供了一组函数和宏，用于操作浮点环境和处理浮点异常。


#### 浮点异常处理


| 函数/宏 | 描述 |
| --- | --- |
| feclearexcept(int excepts) | 清除指定的浮点异常标志 |
| feraiseexcept(int excepts) | 触发指定的浮点异常 |
| fetestexcept(int excepts) | 测试指定的浮点异常是否发生 |
| fegetexceptflag(fexcept_t *flagp, int excepts) | 获取浮点异常标志状态 |
| fesetexceptflag(const fexcept_t *flagp, int excepts) | 设置浮点异常标志状态 |


#### 舍入模式控制


| 函数/宏 | 描述 |
| --- | --- |
| fegetround(void) | 获取当前舍入模式 |
| fesetround(int round) | 设置当前舍入模式 |


#### 浮点环境控制


| 函数/宏 | 描述 |
| --- | --- |
| fegetenv(fenv_t *envp) | 保存当前浮点环境 |
| fesetenv(const fenv_t *envp) | 恢复浮点环境 |
| feholdexcept(fenv_t *envp) | 保存当前浮点环境并清除异常标志 |
| feupdateenv(const fenv_t *envp) | 恢复浮点环境并触发异常 |


---


### 4、实例


以下是一个使用 `` 的示例，展示了如何检测浮点异常和控制舍入模式：


## 实例


```c
#include <stdio.h>
#include <fenv.h>
#include <math.h>

int main() {
    // 启用浮点异常检测
    feclearexcept(FE_ALL_EXCEPT);

    // 触发除以零异常
    double x = 1.0, y = 0.0;
    double z = x / y;

    // 检测是否发生除以零异常
    if (fetestexcept(FE_DIVBYZERO)) {
        printf("Divide by zero exception occurred.\n");
    }

    // 设置舍入模式为向零舍入
    fesetround(FE_TOWARDZERO);

    // 测试舍入模式
    double a = 1.5;
    double b = rint(a); // 舍入到整数
    printf("Rounding 1.5 toward zero: %.1f\n", b);

    return 0;
}
```


输出结果为：


```
Divide by zero exception occurred.
Rounding 1.5 toward zero: 1.0
```


**检测浮点异常**


## 实例


```c
#include <fenv.h>
#include <stdio.h>
#include <math.h>

#pragma STDC FENV_ACCESS ON

void check_exceptions() {
    // 清除所有异常标志
    feclearexcept(FE_ALL_EXCEPT);

    // 执行可能引发异常的运算
    double x = 0.0;
    double y = 1.0 / x;  // 除零

    // 检查特定异常
    if (fetestexcept(FE_DIVBYZERO)) {
        printf("Division by zero occurred!\n");
    }

    // 检查任何异常
    if (fetestexcept(FE_ALL_EXCEPT)) {
        printf("At least one floating-point exception occurred\n");
    }
}

int main() {
    check_exceptions();
    return 0;
}
```


**控制舍入方向**


## 实例


```c
#include <fenv.h>
#include <stdio.h>

#pragma STDC FENV_ACCESS ON

void test_rounding(double num) {
    int modes[] = {FE_TONEAREST, FE_UPWARD, FE_DOWNWARD, FE_TOWARDZERO};
    const char *names[] = {"Nearest", "Up", "Down", "Toward zero"};

    for (int i = 0; i < 4; i++) {
        if (fesetround(modes[i]) == 0) {
            printf("Rounding %s: %.1f -> %.0f\n",
                  names[i], num, rint(num));
        }
    }
}

int main() {
    test_rounding(2.5);  // 测试2.5在不同舍入模式下的结果
    test_rounding(-2.5); // 测试-2.5在不同舍入模式下的结果
    return 0;
}
```


**保存和恢复浮点环境**


## 实例


```c
#include <fenv.h>
#include <stdio.h>
#include <math.h>

#pragma STDC FENV_ACCESS ON

void sensitive_calculation() {
    fenv_t env;

    // 保存当前环境
    fegetenv(&env);

    // 设置严格环境: 捕获所有异常
    feclearexcept(FE_ALL_EXCEPT);

    // 执行关键计算
    double result = sqrt(-1.0);  // 无效操作

    if (fetestexcept(FE_INVALID)) {
        printf("Invalid operation detected in sensitive calculation\n");
    }

    // 恢复原始环境
    fesetenv(&env);
}

int main() {
    sensitive_calculation();
    return 0;
}
```


**临时屏蔽异常**


## 实例


```c
#include <fenv.h>
#include <stdio.h>
#include <math.h>

#pragma STDC FENV_ACCESS ON

void temp_disable_exceptions() {
    fenv_t env;

    // 保存环境并临时屏蔽所有异常
    feholdexcept(&env);

    // 执行可能产生异常的运算
    double x = 0.0;
    double y = 1.0 / x;  // 不会触发异常

    printf("Division by zero was performed but not reported\n");

    // 恢复环境并处理之前发生的异常
    feupdateenv(&env);

    // 现在可以检查异常
    if (fetestexcept(FE_DIVBYZERO)) {
        printf("Division by zero was detected after restoring environment\n");
    }
}

int main() {
    temp_disable_exceptions();
    return 0;
}
```


**精确计算示例**


## 实例


```c
#include <fenv.h>
#include <stdio.h>
#include <math.h>

#pragma STDC FENV_ACCESS ON

double precise_sum(double a, double b) {
    int original_round = fegetround();
    fenv_t env;

    // 保存环境并设置最高精度模式
    fegetenv(&env);
    fesetround(FE_TONEAREST);
    feclearexcept(FE_ALL_EXCEPT);

    double result = a + b;

    // 检查计算是否精确
    if (fetestexcept(FE_INEXACT)) {
        printf("Warning: Sum was not exact, possible precision loss\n");
    }

    // 恢复原始环境
    fesetround(original_round);
    fesetenv(&env);

    return result;
}

int main() {
    double a = 1.0 / 3.0;
    double b = 2.0 / 3.0;

    printf("Sum: %.17g\n", precise_sum(a, b));
    return 0;
}
```


**异常处理包装器**


## 实例


```c
#include <fenv.h>
#include <stdio.h>
#include <math.h>

#pragma STDC FENV_ACCESS ON

typedef double (*math_func)(double);

double safe_math(math_func f, double x, int *error) {
    fenv_t env;
    *error = 0;

    feclearexcept(FE_ALL_EXCEPT);
    fegetenv(&env);

    double result = f(x);

    int exceptions = fetestexcept(FE_ALL_EXCEPT);
    if (exceptions) {
        *error = exceptions;
        if (exceptions & FE_INVALID) printf("Invalid operation\n");
        if (exceptions & FE_DIVBYZERO) printf("Division by zero\n");
        if (exceptions & FE_OVERFLOW) printf("Overflow\n");
        if (exceptions & FE_UNDERFLOW) printf("Underflow\n");
        if (exceptions & FE_INEXACT) printf("Inexact result\n");
    }

    fesetenv(&env);
    return result;
}

int main() {
    int error;

    double a = safe_math(sqrt, -1.0, &error);
    printf("sqrt(-1) = %f (error: %d)\n", a, error);

    double b = safe_math(log, 0.0, &error);
    printf("log(0) = %f (error: %d)\n", b, error);

    return 0;
}
```


### 5、注意事项


- 使用浮点环境功能前通常需要启用 **#pragma STDC FENV_ACCESS ON**，以告知编译器不要优化掉浮点环境操作
- 并非所有实现都支持全部功能，使用前应检查宏 FE_DFL_ENV 是否定义
- `` 仅在 C99 及更高版本中可用。
- 浮点异常检测和舍入模式控制的具体行为可能依赖于硬件和编译器实现。
- 在某些平台上，浮点异常可能默认被屏蔽，需要通过 `feenableexcept` 等函数显式启用。
- 浮点环境操作可能会影响性能，应谨慎使用


`` 提供了对浮点环境的控制功能，包括浮点异常的检测和处理、舍入模式的设置以及浮点状态的查询和修改。它是进行高精度浮点计算和调试浮点问题的强大工具，特别适用于科学计算和工程应用。通过使用 ``，开发者可以更好地控制浮点运算的行为，确保计算结果的准确性和可靠性。








	  AI 思考中...





			** [C 标准库 ](https://www.runoob.com/c-standard-library-tgmath-h.html)
			[C AI 编程助手](https://www.runoob.com/fitten-code-c.html) **













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