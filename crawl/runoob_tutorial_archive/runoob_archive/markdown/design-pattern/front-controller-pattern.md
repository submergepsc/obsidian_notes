# 前端控制器模式

- Source: https://www.runoob.com/design-pattern/front-controller-pattern.html

前端控制器模式（Front Controller Pattern）是用来提供一个集中的请求处理机制，所有的请求都将由一个单一的处理程序处理。该处理程序可以做认证/授权/记录日志，或者跟踪请求，然后把请求传给相应的处理程序。以下是这种设计模式的实体。


- **前端控制器（Front Controller）** - 处理应用程序所有类型请求的单个处理程序，应用程序可以是基于 web 的应用程序，也可以是基于桌面的应用程序。
- **调度器（Dispatcher）** - 前端控制器可能使用一个调度器对象来调度请求到相应的具体处理程序。
- **视图（View）** - 视图是为请求而创建的对象。

---


## 概要


### 意图


使用一个中心控制器（或处理器）来转发客户端请求到适当的处理程序。


### 主要解决的问题


- 解决Web应用程序中请求处理分散的问题，提供统一的请求处理入口。


### 使用场景


- 当需要对Web应用程序中的请求进行统一管理和分发时。


### 实现方式


- **前端控制器**：作为请求的单一入口点，负责请求的接收和转发。
- **视图**：用于呈现处理结果。
- **处理程序**：实际执行请求处理的组件。


### 关键代码


- **前端控制器**：包含逻辑以决定将请求转发到哪个处理程序。
- **处理程序映射**：将请求映射到相应的处理程序。


### 应用实例


- **Web框架**：如Spring MVC中的DispatcherServlet，作为前端控制器。


### 优点


- **集中请求处理**：简化请求处理流程，易于管理和维护。
- **减少代码重复**：通过重用控制器减少视图和处理程序中的重复代码。
- **易于扩展**：新增请求处理逻辑时，只需添加新的处理程序。


### 缺点


- **可能成为性能瓶颈**：所有请求都通过前端控制器，可能影响性能。


### 使用建议


- 当需要构建一个具有清晰请求处理流程的Web应用程序时，考虑使用前端控制器模式。


### 注意事项


- 确保前端控制器不会由于集中处理所有请求而成为性能瓶颈。


### 包含的几个主要角色


- **前端控制器（Front Controller）**： - 作为请求的单一入口点，负责接收请求并决定如何处理。
- **处理程序（Handler）**： - 实际执行请求处理的组件。
- **视图（View）**： - 用于呈现处理程序生成的响应。
- **处理程序映射（Handler Mapping）（可选）**： - 将请求映射到相应的处理程序。
- **客户端（Client）（可选）**： - 发出请求的Web浏览器或API客户端。


前端控制器模式通过提供一个集中的请求处理机制，有助于构建易于维护和扩展的Web应用程序。


---


## 实现


我们将创建 *FrontController*、*Dispatcher* 分别当作前端控制器和调度器。*HomeView* 和 *StudentView* 表示各种为前端控制器接收到的请求而创建的视图。


*FrontControllerPatternDemo*，我们的演示类使用 *FrontController* 来演示前端控制器设计模式。

![前端控制器模式的 UML 图](https://www.runoob.com/wp-content/uploads/2014/08/frontcontroller_pattern_uml_diagram.jpg)

## 步骤 1


创建视图。


## HomeView.java



```
public class HomeView {
   public void show(){
      System.out.println("Displaying Home Page");
   }
}
```


## StudentView.java



```
public class StudentView {
   public void show(){
      System.out.println("Displaying Student Page");
   }
}
```


## 步骤 2


创建调度器 Dispatcher。


## Dispatcher.java



```
public class Dispatcher {
   private StudentView studentView;
   private HomeView homeView;
   public Dispatcher(){
      studentView = new StudentView();
      homeView = new HomeView();
   }

   public void dispatch(String request){
      if(request.equalsIgnoreCase("STUDENT")){
         studentView.show();
      }else{
         homeView.show();
      }
   }
}
```


## 步骤 3


创建前端控制器 FrontController。


## FrontController.java



```
public class FrontController {

   private Dispatcher dispatcher;

   public FrontController(){
      dispatcher = new Dispatcher();
   }

   private boolean isAuthenticUser(){
      System.out.println("User is authenticated successfully.");
      return true;
   }

   private void trackRequest(String request){
      System.out.println("Page requested: " + request);
   }

   public void dispatchRequest(String request){
      //记录每一个请求
      trackRequest(request);
      //对用户进行身份验证
      if(isAuthenticUser()){
         dispatcher.dispatch(request);
      }
   }
}
```


## 步骤 4


使用 *FrontController* 来演示前端控制器设计模式。


## FrontControllerPatternDemo.java



```
public class FrontControllerPatternDemo {
   public static void main(String[] args) {
      FrontController frontController = new FrontController();
      frontController.dispatchRequest("HOME");
      frontController.dispatchRequest("STUDENT");
   }
}
```


## 步骤 5


执行程序，输出结果：


```
Page requested: HOME
User is authenticated successfully.
Displaying Home Page
Page requested: STUDENT
User is authenticated successfully.
Displaying Student Page
```









	  AI 思考中...





			** [数据访问对象模式](https://www.runoob.com/data-access-object-pattern.html)
			[拦截过滤器模式](https://www.runoob.com/intercepting-filter-pattern.html) **













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