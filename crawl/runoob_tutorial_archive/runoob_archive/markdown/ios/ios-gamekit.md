# IOS GameKit

- Source: https://www.runoob.com/ios/ios-gamekit.html

---


## 简介


GameKit是iOS SDK中一个常用的框架。其核心功能有3个：


- 交互游戏平台Game Center，
- P2P设备通讯功能
- In-Game Voice。


## 实例步骤


1.在链接 iTunes 时请确保拥有一个唯一的 App ID（ unique App ID），App ID在我们应用程序更新 bundle ID时及在Xcode代码签名与相应的配置文件需要使用到。


2.创建新的应用程序和更新应用程序信息。在添加新的应用程序文档可以了解更多有关信息。


3.打开你申请的application,点击Manage Game Center选项。进入后点击Enable Game Center使你的Game Center生效。接下来设置自己的Leaderboard和Achievements。


4.下一步涉及处理代码，并为我们的应用程序创建用户界面。


5.创建一个single view application，并输入 bundle identifier 。


6.更新 ViewController.xib，如下所示


![gamekitInterface](https://www.runoob.com/wp-content/uploads/2013/11/gamekitInterface.jpg)


7.选择项目文件，然后选择目标，然后添加GameKit.framework


8.为已添加的按钮创建IBActions


9.更新ViewController.h文件，如下所示


```
#import <UIKit/UIKit.h>
#import <GameKit/GameKit.h>

@interface ViewController : UIViewController
<GKLeaderboardViewControllerDelegate>

-(IBAction)updateScore:(id)sender;
-(IBAction)showLeaderBoard:(id)sender;

@end
```


10.更新ViewController.m ，如下所示


```
#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    if([GKLocalPlayer localPlayer].authenticated == NO)
    {
      [[GKLocalPlayer localPlayer]
      authenticateWithCompletionHandler:^(NSError *error)
      {
         NSLog(@"Error%@",error);
      }];
    }
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (void) updateScore: (int64_t) score
forLeaderboardID: (NSString*) category
{
    GKScore *scoreObj = [[GKScore alloc]
    initWithCategory:category];
    scoreObj.value = score;
    scoreObj.context = 0;
    [scoreObj reportScoreWithCompletionHandler:^(NSError *error) {
        // Completion code can be added here
        UIAlertView *alert = [[UIAlertView alloc]
        initWithTitle:nil message:@"Score Updated Succesfully"
        delegate:self cancelButtonTitle:@"Ok" otherButtonTitles: nil];
        [alert show];

    }];
}
-(IBAction)updateScore:(id)sender{
    [self updateScore:200 forLeaderboardID:@"runoob"];
}
-(IBAction)showLeaderBoard:(id)sender{
    GKLeaderboardViewController *leaderboardViewController =
    [[GKLeaderboardViewController alloc] init];
    leaderboardViewController.leaderboardDelegate = self;
    [self presentModalViewController:
    leaderboardViewController animated:YES];

}
#pragma mark - Gamekit delegates
- (void)leaderboardViewControllerDidFinish:
(GKLeaderboardViewController *)viewController{
    [self dismissModalViewControllerAnimated:YES];
}

@end
```


### 输出


运行该应用程序，输出结果如下


![gamekit_Output1](https://www.runoob.com/wp-content/uploads/2013/11/gamekit_Output1.jpg)


当我们单击显示排行榜时，屏幕显示如下:


![gamekit_Output2](https://www.runoob.com/wp-content/uploads/2013/11/gamekit_Output2.jpg)


当我们点击更新分数，比分将被更新到我们排行榜上，我们会得到一个信息，如下图所示


![gamekit_Output3](https://www.runoob.com/wp-content/uploads/2013/11/gamekit_Output3.jpg)








	  AI 思考中...





			** [iOS整合iAD](https://www.runoob.com/ios-iad.html)
			[iOS 故事板(Storyboards)](https://www.runoob.com/ios-storyboards.html) **













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