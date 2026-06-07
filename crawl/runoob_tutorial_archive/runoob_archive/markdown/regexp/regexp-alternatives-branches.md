# 正则表达式 - 选择和分支

- Source: https://www.runoob.com/regexp/regexp-alternatives-branches.html

### 1、什么是选择 (Alternation)


选择（Alternation）是指在正则表达式中使用 **`|`** 符号表示 "或" 的逻辑关系。它允许你匹配多个可能的模式之一。


```
cat|dog
```


这个模式会匹配 "cat" 或 "dog"。


### 2、什么是分支 (Branching)


分支是指正则表达式引擎在匹配过程中遇到选择点时，会尝试不同的匹配路径。当一条路径匹配失败时，引擎会回溯并尝试其他可能的路径。


---


## 原理解析


### 选择操作符 | 的工作原理


- 正则表达式引擎从左到右扫描 **`|`** 分隔的各个选项
- 尝试匹配第一个选项，如果成功则停止
- 如果第一个选项不匹配，则尝试第二个选项
- 依此类推，直到找到匹配或所有选项都尝试完毕


### 分组与选择


选择通常与分组 **`()`** 结合使用，以限定选择的范围：


## 实例


```regex
gr(a|e)y
```


这个模式会匹配 "gray" 或 "grey"。


### 分支回溯机制


当正则表达式引擎遇到选择点时：


- 记住当前位置（创建检查点）
- 尝试第一个分支
- 如果失败，回退到检查点
- 尝试下一个分支
- 重复直到成功或所有分支都尝试过


---


## 实践示例


### 基本选择示例


## 实例


```regex
// 匹配多种日期格式
const datePattern = /\b(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}\b/;

console.log(datePattern.test("March 15, 2023")); // true
console.log(datePattern.test("Sept 10, 2022"));  // false (缩写不匹配)
```


### 分组选择示例


## 实例


```regex
import re

# 匹配美式或英式拼写
pattern = r"colou?r|color"
text = "The color is red and the colour is blue"

matches = re.findall(pattern, text)
print(matches)  # 输出: ['color', 'colour']
```


### 复杂分支示例


## 实例


```regex
// 匹配多种电话号码格式
String phonePattern = "(\\(\\d{3}\\) ?|\\d{3}[-.]?)\\d{3}[-.]?\\d{4}";

String[] testNumbers = {
    "(123)456-7890",
    "123.456.7890",
    "123-456-7890",
    "1234567890"
};

for (String number : testNumbers) {
    System.out.println(number.matches(phonePattern));  // 全部输出 true
}
```


---


## 扩展应用


### 性能优化技巧


- **高频选项前置**：将最可能匹配的选项放在前面
```
(common|uncommon|rare)  # 优化顺序
```

- **避免冗余分支**：
```
(a|ab|c)  # 不好
(ab?|c)   # 更好
```

- **使用非捕获组**：当不需要捕获分组时
```
(?:pattern1|pattern2)
```


### 实际应用场景


- **日志分析**：匹配多种错误消息格式
- **表单验证**：接受多种合法输入格式
- **文本处理**：查找同义词或变体拼写
- **路由匹配**：Web框架中的URL路由









	  AI 思考中...





			** [正则表达式 – 断言](https://www.runoob.com/regexp-assertions.html)














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