# 组合实体模式

- Source: https://www.runoob.com/design-pattern/composite-entity-pattern.html

组合实体模式（Composite Entity Pattern）用在 EJB 持久化机制中。一个组合实体是一个 EJB 实体 bean，代表了对象的图解。当更新一个组合实体时，内部依赖对象 beans 会自动更新，因为它们是由 EJB 实体 bean 管理的。以下是组合实体 bean 的参与者。


- **组合实体（Composite Entity）** - 它是主要的实体 bean。它可以是粗粒的，或者可以包含一个粗粒度对象，用于持续生命周期。
- **粗粒度对象（Coarse-Grained Object）** - 该对象包含依赖对象。它有自己的生命周期，也能管理依赖对象的生命周期。
- **依赖对象（Dependent Object）** - 依赖对象是一个持续生命周期依赖于粗粒度对象的对象。
- **策略（Strategies）** - 策略表示如何实现组合实体。

---


## 概要


### 意图


将数据库中的表转换为应用程序中的组合对象，这些对象可以表示表中的单个记录或一组记录。


### 主要解决的问题


- 解决在对象关系映射中，如何高效地表示和管理数据库中的复杂数据结构，特别是当存在一对多或多对多关系时。


### 使用场景


- 当数据库表具有复杂的关系，或者需要将数据库表映射为应用程序中的复合对象时。


### 实现方式


- **组合实体类**：代表数据库中的表，可以包含单个记录或一组记录。
- **叶子实体类**：代表表中的单个记录。
- **容器实体类**：代表表中的一组记录，可以包含其他叶子或容器实体。


### 关键代码


- **组合实体类**：包含方法来添加、删除和访问子实体。
- **叶子实体类**：实现组合实体接口，代表单个记录。
- **容器实体类**：实现组合实体接口，可以包含多个叶子或容器实体。


### 应用实例


- **组织结构**：员工可以是叶子节点，表示单个员工；部门可以是容器节点，包含多个员工。


### 优点


- **简化数据访问**：通过对象的方式来简化数据库记录的访问和管理。
- **提高代码可读性**：使代码更贴近自然语言，易于理解和维护。
- **易于扩展**：可以方便地添加新的实体类型或修改现有实体。


### 缺点


- **性能问题**：在处理大量数据时，可能会遇到性能瓶颈。
- **复杂性**：对于简单的数据模型，可能会增加不必要的复杂性。


### 使用建议


- 当需要表示和管理数据库中的复杂数据结构时，考虑使用组合实体模式。


### 注意事项


- 确保组合实体模式的使用不会引入性能问题，特别是在处理大量数据时。


### 包含的几个主要角色


- **组合实体（Composite Entity）**： 代表数据库中的表，可以包含单个或多个记录。


**叶子实体（Leaf Entity）**：


- 代表表中的单个记录，不包含子实体。


**容器实体（Container Entity）**：


- 代表表中的一组记录，可以包含其他叶子或容器实体。


**数据访问对象（Data Access Object）（可选）**：


- 用于访问和操作数据库，封装了数据访问逻辑。


**客户端（Client）（可选）**：


- 使用组合实体模式来访问和操作数据库记录。


组合实体模式通过将数据库表映射为应用程序中的对象，提供了一种直观和灵活的方式来处理复杂的数据关系。


---


## 实现


我们将创建作为组合实体的 *CompositeEntity* 对象。*CoarseGrainedObject* 是一个包含依赖对象的类。


*CompositeEntityPatternDemo*，我们的演示类使用 *Client* 类来演示组合实体模式的用法。

![组合实体模式的 UML 图](https://www.runoob.com/wp-content/uploads/2014/08/compositeentity_pattern_uml_diagram.jpg)

## 步骤 1


创建依赖对象。


## DependentObject1.java



```
public class DependentObject1 {

   private String data;

   public void setData(String data){
      this.data = data;
   }

   public String getData(){
      return data;
   }
}
```


## DependentObject2.java



```
public class DependentObject2 {

   private String data;

   public void setData(String data){
      this.data = data;
   }

   public String getData(){
      return data;
   }
}
```


## 步骤 2


创建粗粒度对象。


## CoarseGrainedObject.java



```
public class CoarseGrainedObject {
   DependentObject1 do1 = new DependentObject1();
   DependentObject2 do2 = new DependentObject2();

   public void setData(String data1, String data2){
      do1.setData(data1);
      do2.setData(data2);
   }

   public String[] getData(){
      return new String[] {do1.getData(),do2.getData()};
   }
}
```


## 步骤 3


创建组合实体。


## CompositeEntity.java



```
public class CompositeEntity {
   private CoarseGrainedObject cgo = new CoarseGrainedObject();

   public void setData(String data1, String data2){
      cgo.setData(data1, data2);
   }

   public String[] getData(){
      return cgo.getData();
   }
}
```


## 步骤 4


创建使用组合实体的客户端类。


## Client.java



```
public class Client {
   private CompositeEntity compositeEntity = new CompositeEntity();

   public void printData(){
      for (int i = 0; i < compositeEntity.getData().length; i++) {
         System.out.println("Data: " + compositeEntity.getData()[i]);
      }
   }

   public void setData(String data1, String data2){
      compositeEntity.setData(data1, data2);
   }
}
```


## 步骤 5


使用 *Client* 来演示组合实体设计模式的用法。


## CompositeEntityPatternDemo.java



```
public class CompositeEntityPatternDemo {
   public static void main(String[] args) {
       Client client = new Client();
       client.setData("Test", "Data");
       client.printData();
       client.setData("Second Test", "Data1");
       client.printData();
   }
}
```


## 步骤 6


执行程序，输出结果：


```
Data: Test
Data: Data
Data: Second Test
Data: Data1
```









	  AI 思考中...





			** [业务代表模式](https://www.runoob.com/business-delegate-pattern.html)
			[数据访问对象模式](https://www.runoob.com/data-access-object-pattern.html) **













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