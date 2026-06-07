# IOS-Twitter和Facebook

- Source: https://www.runoob.com/ios/ios-twitter-facebook.html

---


## 简介


Twitter已经整合到iOS5.0，而Facebook已经被集成在 iOS 6.0中。本教程的重点讲解如何利用苹果提供的类在iOS5.0和iOS6.0中部署Twitter和Facebook。


### 实例步骤


1. 创建一个简单View based application


2. 选择项目文件，然后选择"targets(目标)"，然后在 choose frameworks（选择框架）中添加Social.framework 和 Accounts.framework


3. 添加两个名为facebookPost 和 twitterPost的按钮，并为他们创建 ibActions。


4. 更新 ViewController.h 如下


```
#import <Social/Social.h>
#import <Accounts/Accounts.h>
#import <UIKit/UIKit.h>

@interface ViewController : UIViewController

-(IBAction)twitterPost:(id)sender;
-(IBAction)facebookPost:(id)sender;

@end
```


5. 更新ViewController.m ，如下所示


```
#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

-(IBAction)facebookPost:(id)sender{

   SLComposeViewController *controller = [SLComposeViewController
   composeViewControllerForServiceType:SLServiceTypeFacebook];
   SLComposeViewControllerCompletionHandler myBlock =
   ^(SLComposeViewControllerResult result){
          if (result == SLComposeViewControllerResultCancelled)
          {
            NSLog(@"Cancelled");
          }
          else
          {
            NSLog(@"Done");
          }
          [controller dismissViewControllerAnimated:YES completion:nil];
        };
   controller.completionHandler =myBlock;
   //Adding the Text to the facebook post value from iOS
   [controller setInitialText:@"My test post"];
   //Adding the URL to the facebook post value from iOS
   [controller addURL:[NSURL URLWithString:@"http://www.test.com"]];
   //Adding the Text to the facebook post value from iOS
   [self presentViewController:controller animated:YES completion:nil];
}

-(IBAction)twitterPost:(id)sender{
    SLComposeViewController *tweetSheet = [SLComposeViewController
    composeViewControllerForServiceType:SLServiceTypeTwitter];
    [tweetSheet setInitialText:@"My test tweet"];
    [self presentModalViewController:tweetSheet animated:YES];
}

@end
```


### 输出


运行该应用程序并单击 facebookPost 时我们将获得以下输出


![FBTwit_Output1](https://www.runoob.com/wp-content/uploads/2013/11/FBTwit_Output1.jpg)


当我们单击 twitterPost 时，我们将获得以下输出


![FBTwit_Output2](https://www.runoob.com/wp-content/uploads/2013/11/FBTwit_Output2.jpg)








	  AI 思考中...





			** [iOS自动布局](https://www.runoob.com/ios-auto-layouts.html)
			[iOS内存管理](https://www.runoob.com/ios-memory.html) **













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