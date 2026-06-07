# Java 变量命名规则

- Source: https://www.runoob.com/java/java-variable-naming-rules.html

在 Java 中，不同类型的变量（例如实例变量、局部变量、静态变量等）有一些命名规则和约定。


遵循一些基本规则，这有助于提高代码的可读性和维护性。


以下是各种变量命名规则的概述：


- **使用有意义的名字：** 变量名应该具有清晰的含义，能够准确地反映变量的用途。避免使用单个字符或无意义的缩写。
- **驼峰命名法（Camel Case）：** 在变量名中使用驼峰命名法，即将每个单词的首字母大写，除了第一个单词外，其余单词的首字母都采用大写形式。例如：`myVariableName`。
- **避免关键字：** 不要使用 Java 关键字（例如，class、int、boolean等）作为变量名。
- **区分大小写：** Java 是大小写敏感的，因此变量名中的大小写字母被视为不同的符号。例如，`myVariable` 和 `myvariable` 是两个不同的变量。
- **不以数字开头：** 变量名不能以数字开头，但可以包含数字。
- **遵循命名约定：** 对于不同类型的变量（局部变量、实例变量、静态变量等），可以采用不同的命名约定，例如使用前缀或后缀来区分。


### 局部变量


- 使用驼峰命名法。
- 应该以小写字母开头。
- 变量名应该是描述性的，能够清晰地表示其用途。


```
int myLocalVariable;
```


### 实例变量（成员变量）


- 使用驼峰命名法。
- 应该以小写字母开头。
- 变量名应该是描述性的，能够清晰地表示其用途。


```
private int myInstanceVariable;
```


### 静态变量（类变量）


- 使用驼峰命名法，应该以小写字母开头。
- 通常也可以使用大写蛇形命名法，全大写字母，单词之间用下划线分隔。
- 变量名应该是描述性的，能够清晰地表示其用途。


```
// 使用驼峰命名法
public static int myStaticVariable;

// 使用大写蛇形命名法
public static final int MAX_SIZE = 100;
```


### 常量


- 使用全大写字母，单词之间用下划线分隔。
- 常量通常使用 `final` 修饰。


```
public static final double PI = 3.14;
```


### 参数


- 使用驼峰命名法。
- 应该以小写字母开头。
- 参数名应该是描述性的，能够清晰地表示其用途。


```
public void myMethod(int myParameter) {
    // 方法体
}
```


### 类名


- 使用驼峰命名法。
- 应该以大写字母开头。
- 类名应该是描述性的，能够清晰地表示其用途。


```
public class MyClass {
    // 类的成员和方法
}
```










	  AI 思考中...





			** [Java 注释](https://www.runoob.com/java-comments.html)
			[Java AI 编程助手](https://www.runoob.com/fitten-code-java.html) **













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

      : ·[Java 实例](https://www.runoob.com/java-examples.html)





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