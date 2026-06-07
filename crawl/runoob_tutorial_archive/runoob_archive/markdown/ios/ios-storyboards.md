# IOS 故事板(Storyboards)

- Source: https://www.runoob.com/ios/ios-storyboards.html

---


## 简介


Storyboards在 iOS 5 中才有介绍，当我们用Storyboards时，部署目标应该是iOS5.0或更高版本。 Storyboards 帮助我们了解视觉流动的画面，在界面为
MainStoryboard.storyboard下创建所有应用程序屏幕。


### 实例步骤


1. 创建一个single view application，创建应用程序时选择 storyboard 复选框。


2. 选择MainStoryboard.storyboard，在这里你可以找到单一视图控制器。添加一个视图控制器，更新视图控制器，如下所示


![storyboardInterface](https://www.runoob.com/wp-content/uploads/2013/11/storyboardInterface.jpg)


3.连接两个视图控制器。右键单击"show modal（显示模式）"按钮，在左侧视图控制器将其拖动到右视视图控制器中,如下图所示：


![storyboardButtonAction](https://www.runoob.com/wp-content/uploads/2013/11/storyboardButtonAction.jpg)


4.现在从如下所示的三个显示选项中选择modal(模态)


![storyboardButtonActionModal](https://www.runoob.com/wp-content/uploads/2013/11/storyboardButtonActionModal.jpg)


5.更新 ViewController.h 如下所示


```
#import <UIKit/UIKit.h>

@interface ViewController : UIViewController

-(IBAction)done:(UIStoryboardSegue *)seque;

@end
```


6.更新 ViewController.m 如下所示


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
-(IBAction)done:(UIStoryboardSegue *)seque{
    [self.navigationController popViewControllerAnimated:YES];
}

@end
```


7.选择"MainStoryboard.storyboard"，并右键点击"Exit "按钮，在右侧视图控制器中选择和连接后退按钮，如下图所示


![storyboardButtonExitAction](https://www.runoob.com/wp-content/uploads/2013/11/storyboardButtonExitAction.jpg)


### 输出


在iPhone设备中运行该应用程序,得到如下输出结果


![storyboardOutput1](https://www.runoob.com/wp-content/uploads/2013/11/storyboardOutput1.jpg)


现在，选择显示模式，将得到下面的输出结果


![storyboardOutput2](https://www.runoob.com/wp-content/uploads/2013/11/storyboardOutput2.jpg)








	  AI 思考中...





			** [iOS GameKit](https://www.runoob.com/ios-gamekit.html)
			[iOS自动布局](https://www.runoob.com/ios-auto-layouts.html) **













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