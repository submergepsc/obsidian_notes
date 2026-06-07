# 业务代表模式

- Source: https://www.runoob.com/design-pattern/business-delegate-pattern.html

业务代表模式（Business Delegate Pattern）用于对表示层和业务层解耦。它基本上是用来减少通信或对表示层代码中的业务层代码的远程查询功能。在业务层中我们有以下实体。


- **客户端（Client）** - 表示层代码可以是 JSP、servlet 或 UI java 代码。
- **业务代表（Business Delegate）** - 一个为客户端实体提供的入口类，它提供了对业务服务方法的访问。
- **查询服务（LookUp Service）** - 查找服务对象负责获取相关的业务实现，并提供业务对象对业务代表对象的访问。
- **业务服务（Business Service）** - 业务服务接口。实现了该业务服务的实体类，提供了实际的业务实现逻辑。

---


## 概要


### 意图


抽象和封装应用程序的访问逻辑，从而为表示层提供对业务逻辑层的访问。


### 主要解决的问题


- 解决表示层与业务逻辑层之间的耦合问题，允许表示层通过业务代表间接访问业务逻辑层。


### 使用场景


- 当需要在多层应用程序中清晰地分离表示层和业务逻辑层时。


### 实现方式


- **业务代表接口**：定义访问业务逻辑的方法。
- **业务代表实现**：实现业务代表接口，封装调用业务逻辑层的逻辑。
- **业务服务**：业务逻辑层的接口或类，包含业务操作。


### 关键代码


- **业务代表接口**：声明访问业务逻辑的方法。
- **业务代表实现**：实现接口，包含调用业务服务的代码。
- **业务服务**：业务逻辑的具体实现。


### 应用实例


- **Web应用程序**：Web层作为表示层，通过业务代表访问后端服务层。


### 优点


- **表示层与业务逻辑层解耦**：业务代表作为中间层，降低耦合度。
- **集中访问逻辑**：简化表示层的代码，将访问逻辑集中在业务代表中。
- **易于维护和扩展**：添加新的业务逻辑访问时，只需修改业务代表。


### 缺点


- **可能增加复杂性**：对于简单应用程序，可能增加不必要的抽象层次。


### 使用建议


- 当开发多层应用程序，需要在表示层和业务逻辑层之间提供清晰分离时，考虑使用业务代表模式。


### 注意事项


- 业务代表应该尽量简洁，避免包含复杂的逻辑。


### 包含的几个主要角色


- **业务代表接口（Business Delegate Interface）**： 声明访问业务逻辑的方法。


**业务代表实现（Business Delegate Implementation）**：


- 实现业务代表接口，封装对业务服务的调用。


**业务服务（Business Service）**：


- 业务逻辑层的接口或类，包含实际的业务操作。


**表示层（Presentation Layer）**：


- 应用程序的前端，通过业务代表访问业务逻辑。


**业务逻辑层（Business Logic Layer）**：


- 包含应用程序的核心业务逻辑。


业务代表模式通过提供一个抽象层来访问业务逻辑，有助于保持应用程序的灵活性和可维护性。


---


## 实现


我们将创建 *Client*、*BusinessDelegate*、*BusinessService*、*LookUpService*、*JMSService* 和 *EJBService* 来表示业务代表模式中的各种实体。


*BusinessDelegatePatternDemo* 类使用 *BusinessDelegate* 和 *Client* 来演示业务代表模式的用法。


![业务代表模式的 UML 图](https://www.runoob.com/wp-content/uploads/2014/08/business.svg)


## 步骤 1


创建 BusinessService 接口。


## BusinessService.java



```
public interface BusinessService {
   public void doProcessing();
}
```


## 步骤 2


创建实体服务类。


## EJBService.java



```
public class EJBService implements BusinessService {

   @Override
   public void doProcessing() {
      System.out.println("Processing task by invoking EJB Service");
   }
}
```


## JMSService.java



```
public class JMSService implements BusinessService {

   @Override
   public void doProcessing() {
      System.out.println("Processing task by invoking JMS Service");
   }
}
```


## 步骤 3


创建业务查询服务。


## BusinessLookUp.java



```
public class BusinessLookUp {
   public BusinessService getBusinessService(String serviceType){
      if(serviceType.equalsIgnoreCase("EJB")){
         return new EJBService();
      }else {
         return new JMSService();
      }
   }
}
```


## 步骤 4


创建业务代表。


## BusinessDelegate.java



```
public class BusinessDelegate {
   private BusinessLookUp lookupService = new BusinessLookUp();
   private BusinessService businessService;
   private String serviceType;

   public void setServiceType(String serviceType){
      this.serviceType = serviceType;
   }

   public void doTask(){
      businessService = lookupService.getBusinessService(serviceType);
      businessService.doProcessing();
   }
}
```


## 步骤 5


创建客户端。


## Client.java



```
public class Client {

   BusinessDelegate businessService;

   public Client(BusinessDelegate businessService){
      this.businessService  = businessService;
   }

   public void doTask(){
      businessService.doTask();
   }
}
```


## 步骤 6


使用 BusinessDelegate 和 Client 类来演示业务代表模式。


## BusinessDelegatePatternDemo.java



```
public class BusinessDelegatePatternDemo {

   public static void main(String[] args) {

      BusinessDelegate businessDelegate = new BusinessDelegate();
      businessDelegate.setServiceType("EJB");

      Client client = new Client(businessDelegate);
      client.doTask();

      businessDelegate.setServiceType("JMS");
      client.doTask();
   }
}
```


## 步骤 7


执行程序，输出结果：


```
Processing task by invoking EJB Service
Processing task by invoking JMS Service
```









	  AI 思考中...





			** [MVC 模式](https://www.runoob.com/mvc-pattern.html)
			[组合实体模式](https://www.runoob.com/composite-entity-pattern.html) **













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