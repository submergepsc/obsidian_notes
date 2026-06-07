# 设计模式

- Source: https://www.runoob.com/python-design-pattern/python-design-pattern-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/11/design-patterns-in-python.png) 设计模式（Design Pattern）是一套被反复验证的可复用解决方案，用于解决在软件设计中常见的问题。


简单来说，设计模式是一种**写代码的套路**。

设计模式不是具体的代码，而是告诉你在某种情况下该用什么结构来组织代码，使系统更灵活、更易维护。


---


## 设计模式的本质


想象一下建筑行业中的蓝图：建筑师不会每次都从零开始设计房屋，而是会参考经过验证的建筑模式。同样，在软件开发中，设计模式为我们提供了经过验证的"软件蓝图"，帮助我们避免重复发明轮子。

---


## 为什么需要设计模式


### 1. 可维护性更高



- 设计模式能让代码更易修改。
- 当需求变化时，只需改动特定模块，而不是全局大改。


### 2. 可复用性强


抽象化设计让你能在多个项目中复用同样的结构。


### 3. 团队协作语言


"用装饰器模式实现这个功能"——团队成员一听就懂意图，节省沟通成本。


### 4. 提升架构思维


学习设计模式不是背代码，而是学会如何抽象问题、如何设计扩展点。


---


## 设计模式的分类


设计模式通常分为三大类，每类解决不同层面的设计问题：


### 创建型模式


这类模式关注对象的创建机制，让对象创建更加灵活和符合需求。


**主要模式包括：**


- 单例模式：确保一个类只有一个实例
- 工厂模式：提供创建对象的接口，让子类决定实例化哪个类
- 建造者模式：将复杂对象的构建与其表示分离


### 结构型模式


这类模式关注类和对象的组合方式，形成更大的结构。


**主要模式包括：**


- 适配器模式：使不兼容的接口能够协同工作
- 装饰器模式：动态地为对象添加新功能
- 代理模式：为其他对象提供一种代理以控制对这个对象的访问


### 行为型模式


这类模式关注对象之间的职责分配和通信方式。


**主要模式包括：**


- 观察者模式：定义对象间的一对多依赖关系
- 策略模式：定义一系列算法，使它们可以相互替换
- 命令模式：将请求封装为对象


---


## 常用设计模式应用场景


让我们通过一个表格来快速了解几个常用设计模式的应用场景：


| 设计模式 | 解决的问题 | 典型应用场景 |
| --- | --- | --- |
| 单例模式 | 确保全局唯一实例 | 数据库连接、配置管理、日志系统 |
| 工厂模式 | 对象创建逻辑复杂 | 根据不同条件创建不同类型对象 |
| 观察者模式 | 对象间动态通知 | 事件处理系统、消息订阅 |
| 装饰器模式 | 动态扩展功能 | IO流处理、中间件链 |









	  AI 思考中...






			[Python 设计模式](https://www.runoob.com/python-design-pattern-intro.html) **













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