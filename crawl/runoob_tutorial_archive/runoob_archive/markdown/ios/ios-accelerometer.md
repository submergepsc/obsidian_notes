# IOS加速度传感器(accelerometer)

- Source: https://www.runoob.com/ios/ios-accelerometer.html

---


## 简介


加速度传感器是根据x、y和z三个方向来检测在设备位置的改变。


通过加速度传感器可以知道当前设备相对于地面的位置。


以下实例代码需要在真实设备上运行，在模拟器上是无法工作的。


### 实例步骤


1、创建一个简单的视图应用程序


2、在ViewController.xib中添加三个标签，并创建一个ibOutlets分别为：xlable、ylabel和zlabel


3、如下所示，更新ViewController.h


```
#import <UIKit/UIKit.h>

@interface ViewController : UIViewController<UIAccelerometerDelegate>
{
    IBOutlet UILabel *xlabel;
    IBOutlet UILabel *ylabel;
    IBOutlet UILabel *zlabel;

}
@end
```


4、如下所示，更新ViewController.m


```
#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
    [[UIAccelerometer sharedAccelerometer]setDelegate:self];
    //Do any additional setup after loading the view,typically from a nib
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (void)accelerometer:(UIAccelerometer *)accelerometer didAccelerate:
  (UIAcceleration *)acceleration{
    [xlabel setText:[NSString stringWithFormat:@"%f",acceleration.x]];
    [ylabel setText:[NSString stringWithFormat:@"%f",acceleration.y]];
    [zlabel setText:[NSString stringWithFormat:@"%f",acceleration.z]];
}

@end
```


### 输出


当我们在iPhone设备中运行该应用程序，得到的输出结果如下所示。


![accelerometer_Output](https://www.runoob.com/wp-content/uploads/2013/11/accelerometer_Output.jpg)








	  AI 思考中...





			** [iOS图标(Icons)](https://www.runoob.com/att-ios-ui-icons.html)
			[iOS通用应用程序](https://www.runoob.com/ios-universal-applications.html) **













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