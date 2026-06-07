# C++ 标准库

- Source: https://www.runoob.com/cplusplus/cpp-libs-regex.html

C++ 标准库中的 `` 头文件提供了正则表达式的功能，允许开发者使用一种非常灵活的方式来搜索、替换或分割字符串。正则表达式是一种强大的文本处理工具，广泛应用于数据验证、文本分析和模式匹配等领域。


正则表达式是一种使用单个字符串来描述、匹配一系列符合某个句法规则的字符串的模式。在 C++ 中，正则表达式通过 `` 库实现。


在 C++11 的 `` 中使用正则表达式时，需要在字符串字面量中对反斜杠 **\** 进行转义，也就是写成双反斜杠 **\\**。


**
为什么要双反斜杠？**


C++ 编译器会先处理字符串字面量的转义字符，而正则表达式引擎是后处理的。


例如你写 **\d+**，编译器会把 **\d** 视为未知转义字符报错或变成 **d**，正确写法 **\\d+**，编译器先把 **\\** 转为 **\**，正则引擎再读到 **\d**。


C++11 也支持 原始字符串（raw string），可以避免双反斜杠，非常适合写复杂正则：


```
regex re(R"(\d+)");         // 原始字符串，不需要写 \\d
```


- R"(...)" 里面内容不会做转义处理
- 建议在写多层 \ 的复杂正则时使用


## 基本语法


### 正则表达式的基本组成


- **字符类**：如 `[abc]` 表示匹配 a、b 或 c 中的任意一个字符。
- **量词**：如 `*`（零次或多次）、`+`（一次或多次）、`?`（零次或一次）。
- **边界匹配**：如 `^`（行的开始）、`$`（行的结束）。
- **分组**：使用圆括号 `()` 来创建一个分组。


### C++ 库的主要类和函数


- `std::regex`：表示一个正则表达式对象。
- `std::regex_match`：检查整个字符串是否与正则表达式匹配。
- `std::regex_search`：在字符串中搜索与正则表达式匹配的部分。
- `std::regex_replace`：替换字符串中与正则表达式匹配的部分。
- `std::sregex_iterator`：迭代器，用于遍历所有匹配项。


## 实例


### 1. 整体匹配：regex_match


## 实例


```cpp
#include <iostream>
#include <regex>
using namespace std;

int main() {
    regex re("\\d+");          // 匹配数字
    string s = "12345";

    if (regex_match(s, re))
        cout << "匹配成功\n";
    else
        cout << "匹配失败\n";
}
```


输出结果：


```
匹配成功
```


### 2. 检查字符串是否匹配正则表达式


## 实例


```cpp
#include <iostream>
#include <string>
#include <regex>
using namespace std;

int main() {
    string text = "Hello, World!";
    regex pattern("^[a-zA-Z]+, [a-zA-Z]+!$");

    if (regex_match(text, pattern)) {
        cout << "The string matches the pattern." << endl;
    } else {
        cout << "The string does not match the pattern." << endl;
    }

    return 0;
}
```


输出结果：


```
The string matches the pattern.
```


### 3. 在字符串中搜索匹配项


## 实例


```cpp
#include <iostream>
#include <string>
#include <regex>
using namespace std;

int main() {
    string text = "123-456-7890 and 987-654-3210";
    regex pattern("\\d{3}-\\d{3}-\\d{4}");

    smatch matches;
    while (regex_search(text, matches, pattern)) {
        cout << "Found: " << matches[0] << endl;
        text = matches.suffix().str();  // 继续查找剩余部分
    }

    return 0;
}
```


输出结果：


```
Found: 123-456-7890
Found: 987-654-3210
```


### 4. 替换字符串中的匹配项


## 实例


```cpp
#include <iostream>
#include <string>
#include <regex>
using namespace std;

int main() {
    string text = "Hello, World!";
    regex pattern("World");
    string replacement = "Universe";

    string result = regex_replace(text, pattern, replacement);

    cout << "Original: " << text << endl;
    cout << "Modified: " << result << endl;

    return 0;
}
```


输出结果：


```
Original: Hello, World!
Modified: Hello, Universe!
```


---


## 更多内容


## 常用类与类型


| 名称 | 说明 |
| --- | --- |
| std::regex | 编译正则表达式对象 |
| std::smatch | std::string 匹配结果 |
| std::cmatch | C 字符串匹配结果 (const char*) |
| std::sregex_iterator | 用于 std::string 的匹配迭代器 |
| std::cregex_iterator | 用于 C 字符串的匹配迭代器 |
| std::syntax_option_type | 正则语法选项 |
| std::match_flag_type | 匹配控制标志 |


### 常用函数


| 函数名 | 用途 | 返回值 | 示例 |
| --- | --- | --- | --- |
| regex_match(s, re) | 检查整串是否匹配 | bool | regex_match("123", re) |
| regex_search(s, m, re) | 查找第一个匹配 | bool | regex_search(s, m, re) |
| regex_replace(s, re, fmt) | 替换匹配项 | string | regex_replace(s, re, "#") |


### smatch 匹配结果对象


| 成员 | 说明 | 示例 |
| --- | --- | --- |
| m.str() | 返回整个匹配到的内容 | cout |
| m[i] | 返回第 i 个捕获组 | m[1].str() |
| m.position() | 匹配起始位置 | m.position(0) |
| m.size() | 捕获组数量 | m.size() |
| m.empty() | 是否匹配为空 | m.empty() |


### 常用正则语法


| 符号 | 含义 | 示例 |  |  |
| --- | --- | --- | --- | --- |
| . | 任意字符 | a.c 匹配 abc |  |  |
| \d | 数字 | \d+ |  |  |
| \w | 字母数字下划线 | \w+ |  |  |
| \s | 空白字符 | \s+ |  |  |
| ^ | 开头 | ^abc |  |  |
| $ | 结尾 | xyz$ |  |  |
| + | 1 次或多次 | a+ |  |  |
| * | 0 次或多次 | a* |  |  |
| ? | 0 次或 1 次 | a? |  |  |
| {n,m} | n~m 次 | \d{2,4} |  |  |
| () | 捕获分组 | (ab)+ |  |  |
| [] | 字符集 | [A-Z] |  |  |
| ` | ` | 或 | `cat | dog` |


在 C++ 源码字符串中要写 `\\d` 而不是 `\d`，因为 `\` 需要转义。


### 典型使用示例


## 实例


```cpp
#include <iostream>
#include <regex>
using namespace std;

int main() {
    regex re("\\d+");
    string s = "abc123def456";

    // 查找第一个匹配
    smatch m;
    if (regex_search(s, m, re))
        cout << "第一个匹配: " << m.str() << endl;

    // 遍历所有匹配
    for (sregex_iterator it(s.begin(), s.end(), re), end_it; it != end_it; ++it)
        cout << "匹配到: " << it->str() << endl;

    // 替换
    string result = regex_replace(s, re, "#");
    cout << result << endl;
}
```










	  AI 思考中...





			** [C++ 标准库 ](https://www.runoob.com/cpp-libs-ctime.html)
			[C++ 标准库 *](https://www.runoob.com/cpp-libs-iterator.html) *













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