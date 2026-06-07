# TypeScript 教程

- Source: https://www.runoob.com/typescript/ts-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2019/01/typescript-logo.jpg)


TypeScript 是 JavaScript 的一个超集，支持 ECMAScript 6 标准（[ES6 教程](https://www.runoob.com/w3cnote/es6-tutorial.html)）。


TypeScript 由微软开发的自由和开源的编程语言，在 JavaScript 的基础上增加了静态类型检查的超集。


TypeScript 设计目标是开发大型应用，它可以编译成纯 JavaScript，编译出来的 JavaScript 可以运行在任何浏览器上。


---


## 为什么选择 TypeScript


TypeScript 是由 Microsoft 开发的开源编程语言，它是 JavaScript 的超集，意味着任何有效的 JavaScript 代码也是有效的 TypeScript 代码。


TypeScript 通过添加可选的静态类型、接口、枚举等特性，大大增强了 JavaScript 的开发体验。


### TypeScript 的主要优势


- **静态类型检查：**在编译时发现类型错误，减少运行时错误
- **强大的 IDE 支持：**智能代码补全、导航和重构
- **更好的代码可读性：**类型本身就是最好的文档
- **现代 JavaScript 特性：**支持 ES6+ 语法，如箭头函数、模块、类等
- **渐进式迁移：**可以逐步将现有 JavaScript 项目迁移到 TypeScript


### TypeScript 工作原理


TypeScript 不能直接在浏览器中运行，它需要先编译为 JavaScript。这个编译过程会检查类型错误，并将 TypeScript 特有的语法转换为纯 JavaScript。







  .ts 文件



TypeScript 编译器 (tsc) .js 文件 浏览器/Node.js ✓ TypeScript 编译器 (tsc) 在编译过程中进行类型检查，如果发现类型错误会报错并阻止编译。编译成功后生成纯 JavaScript 代码，可以在任何浏览器或 Node.js 环境中运行。


---


## 语言特性


TypeScript 是对 JavaScript 的类型增强扩展，在保持原有语法兼容的基础上，引入了更强的类型系统和工程能力。


### 核心增强能力（TypeScript 独有）


| 特性 | 说明 |
| --- | --- |
| 类型批注 & 编译时检查 | 在开发阶段发现类型错误，提高代码可靠性 |
| 类型推断 | 无需显式声明类型，编译器可自动推断 |
| 类型擦除 | 编译后移除类型信息，输出纯 JavaScript |
| 接口（Interface） | 用于定义对象结构，增强代码约束 |
| 枚举（Enum） | 提供命名常量集合，提升可读性 |
| 泛型（Generics） | 支持类型复用，增强函数和类的灵活性 |
| Mixin | 实现多重继承的组合模式 |
| 命名空间（Namespace） | 组织代码结构（旧方案，现多用模块） |
| 元组（Tuple） | 固定长度、不同类型的数组 |
| 异步（Await） | 提供更直观的异步流程控制 |


### 来自 ES2015 的语法支持（向下兼容）


TypeScript 同时支持并向下编译 ECMAScript 2015 的核心特性：


| 特性 | 说明 |
| --- | --- |
| 类（Class） | 面向对象编程支持 |
| 模块（Module） | 支持模块化开发（import/export） |
| 箭头函数（=>） | 更简洁的函数写法，绑定词法作用域 |
| 可选参数 | 函数参数可以省略 |
| 默认参数 | 为参数提供默认值 |


---

## JavaScript 与 TypeScript 的区别


TypeScript 是 JavaScript 的超集，扩展了 JavaScript 的语法，因此现有的 JavaScript 代码可与 TypeScript 一起工作无需任何修改，TypeScript 通过类型注解提供编译时的静态类型检查。


TypeScript 可处理已有的 JavaScript 代码，并只对其中的 TypeScript 代码进行编译。



    ![](https://www.runoob.com/wp-content/uploads/2019/01/ts-2020-11-26-2.png)



    ![](https://www.runoob.com/wp-content/uploads/2019/01/ts-2020-11-26-1.png)



---

## 第一个 TypeScript 实例


以下实例我们使用 TypeScript 来输出** Hello World!**:


## 实例


```javascript
const hello : string = "Hello World!"
console.log(hello)
```


**
[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=ts-hw&type=typescript)








	  AI 思考中...






			[TypeScript 安装](https://www.runoob.com/ts-install.html) **













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