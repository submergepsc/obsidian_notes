# 正则表达式 - 断言

- Source: https://www.runoob.com/regexp/regexp-assertions.html

断言（Assertion）是正则表达式中用于指定匹配位置的元字符，它们不匹配任何实际字符，而是匹配字符之间的位置。


假设我们要在一篇长文中找到所有价格后面的数字，而不是找到所有的数字，普通的正则表达式可能会匹配到所有数字，但使用断言，你可以精确地指定：**我只匹配那些紧跟在价格后面的数字**。


本文将带你系统学习正则表达式中四种核心的断言：正向先行断言、负向先行断言、正向后行断言 和 负向后行断言。


### 断言的特点


- **零宽度**：不占用匹配字符的位置
- **条件检查**：只检查是否满足特定条件
- **不影响匹配结果**：仅作为匹配的约束条件


## 实例


```regex
// 示例：匹配后面跟着 bar 的 foo
const regex = /foo(?=bar)/;
console.log(regex.test("foobar"));  // true
console.log(regex.test("food"));    // false
```


---


## 断言的类型


正则表达式中的断言主要分为两大类四种类型：


| 断言类型 | 正则语法 | 别称 | 检查方向 | 期望条件 | 通俗解释 |
| --- | --- | --- | --- | --- | --- |
| 正向先行断言 | (?=pattern) | 正前瞻 | 向右（向前） | 存在 pattern | 我要找的位置，它的右边必须是... |
| 负向先行断言 | (?!pattern) | 负前瞻 | 向右（向前） | 不存在 pattern | 我要找的位置，它的右边一定不能是... |
| 正向后行断言 | (? | 正后顾 | 向左（向后） | 存在 pattern | 我要找的位置，它的左边必须是... |
| 负向后行断言 | (? | 负后顾 | 向左（向后） | 不存在 pattern | 我要找的位置，它的左边一定不能是... |


---


## 正向先行断言 (?=...)


**正向先行断言** 用于匹配这样一个位置：在这个位置之后（右边），必须紧跟着出现指定的模式 `...`。


### 语法与参数


- **语法**：`(?=pattern)`
- **作用**：检查当前位置右侧是否匹配 `pattern`。如果匹配，则断言成功，引擎会回到当前位置继续后续匹配。
- **关键特性**：**零宽度**，即它只检查，不"吃掉"任何字符。`pattern` 中的内容不会成为最终匹配结果的一部分。


### 代码示例 1：提取价格数字


假设我们有一串文本，需要提取所有**价格：**后面的金额数字。


## 实例：JavaScript


```regex
const text = "商品A价格：299元，商品B价格：599元，运费：20元。";

// 正向先行断言
// 匹配一个或多个数字，但要求右侧紧跟"元"
// "元"本身不参与匹配结果
const pattern = /\d+(?=元)/g;

const matches = text.match(pattern);

console.log("匹配到的价格数字：", matches);
// 输出：['299', '599', '20']
```


## 实例：Python


```regex
import re

text = "商品A价格：299元，商品B价格：599元，运费：20元。"

# 使用正向先行断言
# 匹配一个或多个数字 (\d+)，但要求这个数字的右边必须紧跟着"元"
# 注意："元"本身不会被匹配到结果中
pattern = r'\d+(?=元)'
matches = re.findall(pattern, text)

print("匹配到的价格数字：", matches)
# 输出：匹配到的价格数字： ['299', '599', '20']
```


**代码解析**：


- `\d+` 是主表达式，匹配一个或多个数字。
- `(?=元)` 是断言，它检查 `\d+` 匹配到的数字串的**右侧**是否紧跟着一个"元"字。
- 引擎首先找到 `299`，然后向右看，发现是"元"，断言成功，所以 `299` 被记录。
- 继续找到 `599`，右边是"元"，成功，记录。
- 找到 `20`，右边是"元"，成功，记录。最终，我们只得到了数字部分。


### 代码示例 2：验证复杂密码


要求密码必须包含至少一个大写字母、一个小写字母和一个数字。


## 实例：JavaScript


```regex
function validatePassword(password) {
  // 多个正向先行断言
  const pattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/;
  // ^              字符串开始
  // (?=.*[A-Z])    右侧必须存在至少一个大写字母
  // (?=.*[a-z])    右侧必须存在至少一个小写字母
  // (?=.*\d)       右侧必须存在至少一个数字
  // .{8,}          总长度至少 8
  // $              字符串结束

  return pattern.test(password);
}

// 测试数据
const passwords = ["Weak", "strong123", "STRONG123", "Strong123"];

passwords.forEach(pwd => {
  console.log(`密码 '${pwd}' 是否有效：${validatePassword(pwd)}`);
});

// 输出：
// 密码 'Weak' 是否有效：false
// 密码 'strong123' 是否有效：false
// 密码 'STRONG123' 是否有效：false
// 密码 'Strong123' 是否有效：true
```


## 实例：Pyhton


```regex
import re

def validate_password(password):
    # 使用多个正向先行断言来分别检查条件
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
    # ^ 代表字符串开始
    # (?=.*[A-Z]) 断言：从当前位置（开头）向右看，必须能在任意字符（.*）后找到一个大写字母
    # (?=.*[a-z]) 断言：同样从开头向右看，必须能找到一个小写字母
    # (?=.*\d)    断言：从开头向右看，必须能找到一个数字
    # .{8,}       主表达式：匹配任意字符至少8次（总长度要求）
    # $ 代表字符串结束
    if re.match(pattern, password):
        return True
    else:
        return False

# 测试数据
passwords = ["Weak", "strong123", "STRONG123", "Strong123"]
for pwd in passwords:
    print(f"密码 '{pwd}' 是否有效：{validate_password(pwd)}")

# 输出：
# 密码 'Weak' 是否有效：False      # 长度不够，且缺数字
# 密码 'strong123' 是否有效：False # 缺大写字母
# 密码 'STRONG123' 是否有效：False # 缺小写字母
# 密码 'Strong123' 是否有效：True  # 符合所有条件
```


---


## 负向先行断言 (?!...)


**负向先行断言** 与正向先行断言相反。它匹配一个位置，在这个位置之后（右边），**不能**紧跟着出现指定的模式 `...`。


### 语法与参数


- **语法**：`(?!pattern)`
- **作用**：检查当前位置右侧是否**不匹配** `pattern`。如果不匹配，则断言成功。
- **关键特性**：同样是零宽度。


### 代码示例：查找非 ing 结尾的单词


在一句话中，找到所有不以 `ing` 结尾的单词。


## 实例：JavaScript


```regex
// 示例一：负向先行断言
const text1 = "playing swimming run walk jumping sing";
const pattern1 = /\b\w+(?<!ing)\b/g;
console.log(text1.match(pattern1));
// ['run', 'walk', 'sing']

// 示例 2：匹配不以 q 结尾的单词（正确语义版）
const text2 = "I like faq apple Iraq you banana q";
const pattern2 = /\b\w*[^q\W]\b/g;
// 含义：
// [^q\W]   单词最后一个字符不是 q
// 比 (?!q) 更符合"结尾不是 q"的真实需求
console.log(text2.match(pattern2));
// ['I', 'like', 'apple', 'you', 'banana']

// 示例 3：匹配不以 .js 结尾的文件名
const files = "index.js app.ts config.json main.js readme.md";
const pattern3 = /\b\w+\.(?!js\b)\w+\b/g;
// 含义：  \.(?!js\b)  点号后不能是 js
console.log(files.match(pattern3));
// ['app.ts', 'config.json', 'readme.md']
```


---


## 正向后行断言 (?


**正向后行断言** 用于匹配一个位置，在这个位置之前（左边），必须紧挨着出现指定的模式 `...`。

*注意：不是所有编程语言的正则引擎都支持后行断言，JavaScript 在 ES2018 后才完全支持，而 Python 的 `re` 模块支持。*


### 语法与参数


- **语法**：`(?


                **
                正向先行断言


                **
                负向先行断言


                **
                正向后行断言


                **
                负向后行断言


                **
                综合实战


                **
                交互测试







                    **
                    正向先行断言

                (?=pattern)


            **
                ** 运行示例







                    **
                    负向先行断言

                (?!pattern)



                ** 运行示例







                    **
                    正向后行断言

                (?<=pattern)



                ** 运行示例







                    **
                    负向后行断言

                (?<!pattern)



                ** 运行示例







                    **
                    综合实战示例




                ** 运行示例







                    **
                    交互式测试区


            *


                * 开始测试









### 正则表达式断言小测验




#### 1. 对于模式 `Python(?=3)` 在字符串 `"我喜欢Python3和Python2"` 中的匹配结果，以下哪项正确？


        *
        匹配到 "Python3"



        匹配到 "Python"（位于 "Python3" 中）



        匹配到 "Python"（位于 "Python2" 中）



        匹配到 "Python" 两次






#### 2. 哪个断言可以用来匹配一个前面没有字母 `q` 的数字 `7`？



        `(?=q)7`



        `(?!q)7`



        `(?<=q)7`



        `(?<!q)7`






#### 3. 模式 `(?[email protected]"` 中的匹配结果是什么？



        `admin` 和 `example`



        `admin`



        `@admin`



        `user` 和 `admin`






#### 4. 断言的主要特点是什么？（多选）



        它会消耗（匹配）字符。



        它用于检查一个位置是否满足条件。



        它的匹配宽度为零。



        它可以用来精确控制匹配的边界。




    提交答案
    重置测验











	  AI 思考中...





			* [正则表达式 – 分组和引用](https://www.runoob.com/regexp-grouping-quoting.html)
			[正则表达式 – 选择和分支](https://www.runoob.com/regexp-alternatives-branches.html) **













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