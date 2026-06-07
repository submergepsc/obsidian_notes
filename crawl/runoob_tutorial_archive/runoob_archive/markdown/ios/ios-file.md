# IOS文件处理

- Source: https://www.runoob.com/ios/ios-file.html

---


### 简介


文件处理不能直观的通过应用程序来解释，我们可以从以下实例来了解IOS的文件处理。


IOS中对文件的操作. 因为应用是在沙箱（sandbox）中的，在文件读写权限上受到限制，只能在几个目录下读写文件。


### 文件处理中使用的方法


下面列出了用于访问和操作文件的方法的列表。 以下实例你必须替换FilePath1、FilePath和FilePath字符串为完整的文件路径，以获得所需的操作。


检查文件是否存在


```
NSFileManager *fileManager = [NSFileManager defaultManager];
   //Get documents directory
   NSArray *directoryPaths = NSSearchPathForDirectoriesInDomains
   (NSDocumentDirectory, NSUserDomainMask, YES);
   NSString *documentsDirectoryPath = [directoryPaths objectAtIndex:0];
   if ([fileManager fileExistsAtPath:@""]==YES) {
        NSLog(@"File exists");
    }
```


比较两个文件的内容


```
if ([fileManager contentsEqualAtPath:@"FilePath1" andPath:@" FilePath2"]) {
      NSLog(@"Same content");
   }
```


检查是否可写、可读、可执行文件


```
if ([fileManager isWritableFileAtPath:@"FilePath"]) {
      NSLog(@"isWritable");
   }
   if ([fileManager isReadableFileAtPath:@"FilePath"]) {
      NSLog(@"isReadable");
   }
   if ( [fileManager isExecutableFileAtPath:@"FilePath"]){
      NSLog(@"is Executable");
   }
```


移动文件


```
if([fileManager moveItemAtPath:@"FilePath1"
   toPath:@"FilePath2" error:NULL]){
      NSLog(@"Moved successfully");
   }
```


复制文件


```
if ([fileManager copyItemAtPath:@"FilePath1"
   toPath:@"FilePath2"  error:NULL]) {
      NSLog(@"Copied successfully");
   }
```


删除文件


```
if ([fileManager removeItemAtPath:@"FilePath" error:NULL]) {
      NSLog(@"Removed successfully");
   }
```


读取文件


```
NSData *data = [fileManager contentsAtPath:@"Path"];
```


写入文件


```
[fileManager createFileAtPath:@"" contents:data attributes:nil];
```










	  AI 思考中...





			** [iOS音频和视频(Audio & Video)](https://www.runoob.com/ios-audio-video.html)
			[iOS地图开发](https://www.runoob.com/ios-maps.html) **













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