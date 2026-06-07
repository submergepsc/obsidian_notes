# IOS自动布局

- Source: https://www.runoob.com/ios/ios-auto-layouts.html

---


## 简介


自动布局在iOS 6.0中引入，仅可以支持IOS6.0 及 更高版本。它可以帮助我们创建用于多个种设备的界面。


### 实例步骤


1.创建一个简单的 View based application


2.修改 ViewController.m 的文件内容，如下所示


```
#import "ViewController.h"
@interface ViewController ()
@property (nonatomic, strong) UIButton *leftButton;
@property (nonatomic, strong) UIButton *rightButton;
@property (nonatomic, strong) UITextField *textfield;

@end
@implementation ViewController

- (void)viewDidLoad{
    [super viewDidLoad];
    UIView *superview = self.view;
    /*1. Create leftButton and add to our view*/
    self.leftButton = [UIButton buttonWithType:UIButtonTypeRoundedRect];
    self.leftButton.translatesAutoresizingMaskIntoConstraints = NO;
    [self.leftButton setTitle:@"LeftButton" forState:UIControlStateNormal];
    [self.view addSubview:self.leftButton];
    /* 2. Constraint to position LeftButton's X*/
    NSLayoutConstraint *leftButtonXConstraint = [NSLayoutConstraint
    constraintWithItem:self.leftButton attribute:NSLayoutAttributeCenterX
    relatedBy:NSLayoutRelationGreaterThanOrEqual toItem:superview attribute:
    NSLayoutAttributeCenterX multiplier:1.0 constant:-60.0f];
    /* 3. Constraint to position LeftButton's Y*/
    NSLayoutConstraint *leftButtonYConstraint = [NSLayoutConstraint
    constraintWithItem:self.leftButton attribute:NSLayoutAttributeCenterY
    relatedBy:NSLayoutRelationEqual toItem:superview attribute:
    NSLayoutAttributeCenterY multiplier:1.0f constant:0.0f];
    /* 4. Add the constraints to button's superview*/
    [superview addConstraints:@[ leftButtonXConstraint,
    leftButtonYConstraint]];
    /*5. Create rightButton and add to our view*/
    self.rightButton = [UIButton buttonWithType:UIButtonTypeRoundedRect];
    self.rightButton.translatesAutoresizingMaskIntoConstraints = NO;
    [self.rightButton setTitle:@"RightButton" forState:UIControlStateNormal];
    [self.view addSubview:self.rightButton];
    /*6. Constraint to position RightButton's X*/
    NSLayoutConstraint *rightButtonXConstraint = [NSLayoutConstraint
    constraintWithItem:self.rightButton attribute:NSLayoutAttributeCenterX
    relatedBy:NSLayoutRelationGreaterThanOrEqual toItem:superview attribute:
    NSLayoutAttributeCenterX multiplier:1.0 constant:60.0f];
    /*7. Constraint to position RightButton's Y*/
    rightButtonXConstraint.priority = UILayoutPriorityDefaultHigh;
    NSLayoutConstraint *centerYMyConstraint = [NSLayoutConstraint
    constraintWithItem:self.rightButton attribute:NSLayoutAttributeCenterY
    relatedBy:NSLayoutRelationGreaterThanOrEqual toItem:superview attribute:
    NSLayoutAttributeCenterY multiplier:1.0f constant:0.0f];
    [superview addConstraints:@[centerYMyConstraint,
    rightButtonXConstraint]];
   //8. Add Text field
    self.textfield = [[UITextField alloc]initWithFrame:
    CGRectMake(0, 100, 100, 30)];
    self.textfield.borderStyle = UITextBorderStyleRoundedRect;
    self.textfield.translatesAutoresizingMaskIntoConstraints = NO;
    [self.view addSubview:self.textfield];
    //9. Text field Constraints
    NSLayoutConstraint *textFieldTopConstraint = [NSLayoutConstraint
    constraintWithItem:self.textfield attribute:NSLayoutAttributeTop
    relatedBy:NSLayoutRelationGreaterThanOrEqual toItem:superview
    attribute:NSLayoutAttributeTop multiplier:1.0 constant:60.0f];
    NSLayoutConstraint *textFieldBottomConstraint = [NSLayoutConstraint
    constraintWithItem:self.textfield attribute:NSLayoutAttributeTop
    relatedBy:NSLayoutRelationGreaterThanOrEqual toItem:self.rightButton
    attribute:NSLayoutAttributeTop multiplier:0.8 constant:-60.0f];
    NSLayoutConstraint *textFieldLeftConstraint = [NSLayoutConstraint
    constraintWithItem:self.textfield attribute:NSLayoutAttributeLeft
    relatedBy:NSLayoutRelationEqual toItem:superview attribute:
    NSLayoutAttributeLeft multiplier:1.0 constant:30.0f];
    NSLayoutConstraint *textFieldRightConstraint = [NSLayoutConstraint
    constraintWithItem:self.textfield attribute:NSLayoutAttributeRight
    relatedBy:NSLayoutRelationEqual toItem:superview attribute:
    NSLayoutAttributeRight multiplier:1.0 constant:-30.0f];
    [superview addConstraints:@[textFieldBottomConstraint ,
    textFieldLeftConstraint, textFieldRightConstraint,
    textFieldTopConstraint]];
}
- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
@end
```


### 输出


运行应用程序，在 iPhone 模拟器上会有下面的输出结果


![autolayoutOutputiPhonePortrait](https://www.runoob.com/wp-content/uploads/2013/11/autolayoutOutputiPhonePortrait.jpg)


当我们更改模拟器为横向的方向时，输出结果如下


![autolayoutOutputiPhoneLandscape](https://www.runoob.com/wp-content/uploads/2013/11/autolayoutOutputiPhoneLandscape.jpg)


我们在 iPhone 5 模拟器上运行同一应用程序时,输出结果如下


![autolayoutOutputiPhone5Portrait](https://www.runoob.com/wp-content/uploads/2013/11/autolayoutOutputiPhone5Portrait.jpg)


当我们更改模拟器为横向的方向时，输出结果如下:


![autolayoutOutputiPhone5Landscape](https://www.runoob.com/wp-content/uploads/2013/11/autolayoutOutputiPhone5Landscape.jpg)








	  AI 思考中...





			** [iOS 故事板(Storyboards)](https://www.runoob.com/ios-storyboards.html)
			[iOS Twitter和Facebook](https://www.runoob.com/ios-twitter-facebook.html) **













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