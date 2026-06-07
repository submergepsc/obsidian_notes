# IOS通用应用程序

- Source: https://www.runoob.com/ios/ios-universal-applications.html

---


## 简介


通用的应用程序是为iPhone和iPad在一个单一的二进制文件中设计的应用程序。这有助于代码重用，并能够帮助更快进行更新。


### 实例步骤


1、创建一个简单的View based application（视图应用程序）


2、在文件查看器的右边，将文件ViewController.xib的文件名称更改为ViewController_iPhone.xib，如下所示


![UniversalAppInterfaceRename](https://www.runoob.com/wp-content/uploads/2013/11/UniversalAppInterfaceRename.jpg)


3、选择"File -> New -> File... "，然后选择User Interface，再选择View，单击下一步


![NewIpadXib](https://www.runoob.com/wp-content/uploads/2013/11/NewIpadXib.jpg)


4、选择iPad作为设备，单击下一步:


![UniversalAppSelectDeviceType](https://www.runoob.com/wp-content/uploads/2013/11/UniversalAppSelectDeviceType.jpg)


5、将该文件另存为ViewController_iPad.xib，然后选择创建


6、在ViewController_iPhone.xib和ViewController_iPad.xibd的屏幕中心添加标签


7、在ViewController_iPhone.xib中选择identity inspector，设置custom class为ViewController


![UniversalAppSetClass](https://www.runoob.com/wp-content/uploads/2013/11/UniversalAppSetClass.jpg)


8、更新AppDelegate.m中的 application:DidFinishLaunching:withOptions方法


```
- (BOOL)application:(UIApplication *)application
  didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
   self.window = [[UIWindow alloc] initWithFrame:[[UIScreen
   mainScreen] bounds]];
   // Override point for customization after application launch.
   if (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPhone) {
        self.viewController = [[ViewController alloc]
        initWithNibName:@"ViewController_iPhone" bundle:nil];
   }
   else{
        self.viewController = [[ViewController alloc] initWithNibName:
        @"ViewController_iPad" bundle:nil];
   }
   self.window.rootViewController = self.viewController;
   [self.window makeKeyAndVisible];
   return YES;
}
```


9、在项目摘要中更新设备中为universal，如下所示：


![UniversalAppSetDevices](https://www.runoob.com/wp-content/uploads/2013/11/UniversalAppSetDevices.jpg)


### 输出


运行该应用程序，我们会看到下面的输出


![UniversalAppiPhone_Output](https://www.runoob.com/wp-content/uploads/2013/11/UniversalAppiPhone_Output.jpg)


在iPad模拟器中运行应用程序,我们会得到下面的输出:


![UniversalAppiPad_Output](https://www.runoob.com/wp-content/uploads/2013/11/UniversalAppiPad_Output.jpg)








	  AI 思考中...





			** [iOS加速度传感器(accelerometer)](https://www.runoob.com/ios-accelerometer.html)
			[iOS相机管理](https://www.runoob.com/ios-camera.html) **













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