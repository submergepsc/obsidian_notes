# 

- Source: https://www.runoob.com/ios/ios-delegates.html

## 委托（Delegates）示例


假设对象A调用B来执行一项操作，操作一旦完成，对象A就必须知道对象B已完成任务且对象A将执行其他必要操作。


在上面的示例中的关键概念有


- A是B的委托对象
- B引用一个A
- A将实现B的委托方法
- B通过委托方法通知


创建一个委托（Delegates）对象


1. 创建一个单一视图的应用程序


2. 然后选择文件 File -> New -> File...


![addNewFile](https://www.runoob.com/wp-content/uploads/2013/11/addNewFile.jpg)


3. 然后选择Objective C单击下一步


4. 将SampleProtocol的子类命名为NSObject，如下所示


![setProtocolName](https://www.runoob.com/wp-content/uploads/2013/11/setProtocolName.jpg)


5. 然后选择创建


6.向SampleProtocol.h文件夹中添加一种协议，然后更新代码，如下所示：


```
#import <Foundation/Foundation.h>
// 协议定义
@protocol SampleProtocolDelegate <NSObject>
@required
- (void) processCompleted;
@end
// 协议定义结束
@interface SampleProtocol : NSObject

{
   // Delegate to respond back
   id <SampleProtocolDelegate> _delegate;

}
@property (nonatomic,strong) id delegate;

-(void)startSampleProcess; // Instance method

@end
```


7.修改 SampleProtocol.m 文件代码，实现实例方法：


```
#import "SampleProtocol.h"

@implementation SampleProtocol

-(void)startSampleProcess{

    [NSTimer scheduledTimerWithTimeInterval:3.0 target:self.delegate
    selector:@selector(processCompleted) userInfo:nil repeats:NO];
}
@end
```


8. 将标签从对象库拖到UIView，从而在ViewController.xib中添加UILabel，如下所示:


![delegateLabel](https://www.runoob.com/wp-content/uploads/2013/11/delegateLabel.jpg)


9. 创建一个IBOutlet标签并命名为myLabel，然后按如下所示更新代码并在ViewController.h里显示SampleProtocolDelegate


```
#import <UIKit/UIKit.h>
#import "SampleProtocol.h"

@interface ViewController : UIViewController<SampleProtocolDelegate>
{
    IBOutlet UILabel *myLabel;
}
@end
```


10. 完成授权方法，为SampleProtocol创建对象和调用startSampleProcess方法。如下所示，更新ViewController.m文件


```
#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    SampleProtocol *sampleProtocol = [[SampleProtocol alloc]init];
    sampleProtocol.delegate = self;
    [myLabel setText:@"Processing..."];
    [sampleProtocol startSampleProcess];
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

#pragma mark - Sample protocol delegate
-(void)processCompleted{
    [myLabel setText:@"Process Completed"];
}


@end
```


11. 将看到如下所示的输出结果，最初的标签也会继续运行，一旦授权方法被SampleProtocol对象所调用，标签运行程序的代码也会更新。


![delegateResult](https://www.runoob.com/wp-content/uploads/2013/11/delegateResult.jpg)








	  AI 思考中...





			** [iOS操作（action）和输出口（Outlet）](https://www.runoob.com/ios-action-outlet.html)
			[iOS UI元素](https://www.runoob.com/ios-ui.html) **













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