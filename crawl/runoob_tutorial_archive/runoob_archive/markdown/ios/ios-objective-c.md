# Objective-C 简介

- Source: https://www.runoob.com/ios/ios-objective-c.html

在iOS的开发中使用的是Objective C语言，它是一种面向对象的语言，因而对于已经掌握面向对象语言知识的编程者来说是非常简单的。


---


## 接口和实现


在Objective里完成的文件被称为界面文件，该类文件的定义被称为实现文件。


一个简单的界面文件MyClass.h将如图所示:


```
@interface MyClass:NSObject{
// 类变量声明
}
// 类属性声明
// 类方法和声明
@end
```


执行MyClass.m文件，如下所示


```
@implementation MyClass
// 类方法定义
@end
```


---


## 创建对象


完成创建对象，如下所示


```
MyClass  *objectName = [[MyClass alloc]init] ;
```


---


## 方法（methods）


Objective C中声明的方法如下所示:


```
-(returnType)methodName:(typeName) variable1 :(typeName)variable2;
```


下面显示了一个示例:


```
-(void)calculateAreaForRectangleWithLength:(CGfloat)length
andBreadth:(CGfloat)breadth;
```


你可能会想什么是andBreadth字符串，其实它的可选字符串可以帮助我们阅读和理解方法，尤其是当方法被调用的时候。


在同一类中调用此方法，我们使用下面的语句。


```
[self calculateAreaForRectangleWithLength:30 andBreadth:20];
```


正如上文所说的andBreath使用有助于我们理解breath是20。Self用来指定它是一个类的方法。


**类方法（class methods）**


直接而无需创建的对象，可以访问类方法。他们没有任何变量和它关联的对象。示例如下:


```
+(void)simpleClassMethod;
```


它可以通过使用类名（假设作为MyClass类名称）访问，如下所示:


```
[MyClass simpleClassMethod];
```


**实例方法**


可以创建的类的对象后只访问实例方法，内存分配到的实例变量。实例方法如下所示:


```
-(void)simpleInstanceMethod;
```


创建类的对象后，它可以访问它。如下所示:


```
MyClass  *objectName = [[MyClass alloc]init] ;
[objectName simpleInstanceMethod];
```


---


## Objective C的重要数据类型


| 序号 | 数据类型 |
| --- | --- |
| 1 | NSString字符串 |
| 2 | CGfloat 浮点值的基本类型 |
| 3 | NSInteger 整型 |
| 4 | BOOL 布尔型 |


---


## 打印日志


NSLog用于打印一份声明，它将打印在设备日志和调试版本的控制台和分别调试模式上。


如 NSlog(@"");


---


## 控制结构


除了几个增补的条款外，大多数的控制结构与C以及C++相同


**属性（properties）**


用于访问类的外部类的变量属性


比如：@property（非原子、强）NSString*myString


**访问属性**


可以使用点运算符访问属性，若要访问上一属性可以执行以下操作


```
self.myString = @"Test";
```


还可以使用set的方法，如下所示：


```
[self setMyString:@"Test"];
```


**类别（categories）**


类用于将方法添加到现有类。通过这种方法可以将方法添加到类，甚至不用执行文件，就可以在其中定义实际的类。MyClass的样本类别，如下所示：


```
@interface MyClass(customAdditions)
- (void)sampleCategoryMethod;
@end

@implementation MyClass(categoryAdditions)

-(void)sampleCategoryMethod{
   NSLog(@"Just a test category");
}
```


---


## 数组


NSMutableArray 和 NSArray 是 ObjectiveC 中使用的数组类，前者是可变数组，后者是不可变数组。如下:


```
NSMutableArray *aMutableArray = [[NSMutableArray alloc]init];
[anArray addObject:@"firstobject"];
NSArray *aImmutableArray = [[NSArray alloc]
initWithObjects:@"firstObject",nil];
```


---


## 词典


NSMutableDictionary和NSDictionary是Objective中使用的字典，前者可变词典，后者不可变词典，如下所示:


```
NSMutableDictionary*aMutableDictionary = [[NSMutableArray alloc]init];
[aMutableDictionary setObject:@"firstobject" forKey:@"aKey"];
NSDictionary*aImmutableDictionary= [[NSDictionary alloc]initWithObjects:[NSArray arrayWithObjects:
@"firstObject",nil] forKeys:[ NSArray arrayWithObjects:@"aKey"]];
```









	  AI 思考中...





			** [iOS环境搭建](https://www.runoob.com/ios-setup.html)
			[创建第一款iPhone应用程序](https://www.runoob.com/ios-first-iphone-application.html) **













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