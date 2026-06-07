# Ruby 中文编码

- Source: https://www.runoob.com/ruby/ruby-encoding.html

前面章节中我们已经学会了如何用 Ruby 输出 "Hello, World!"，英文没有问题，但是如果你输出中文字符"你好，世界"就有可能会碰到中文编码问题。


Ruby 文件中如果未指定编码，在执行过程会出现报错：


```
#!/usr/bin/ruby -w

puts "你好，世界！";
```


以上程序执行输出结果为：


```
invalid multibyte char (US-ASCII)
```


以上出错信息显示了 Ruby 使用用 ASCII 编码来读源码，中文会出现乱码，解决方法为只要在文件开头加入 **# -*- coding: UTF-8 -*-**（EMAC写法） 或者 **#coding=utf-8** 就行了。


## 实例



```ruby
#!/usr/bin/ruby -w
# -*- coding: UTF-8 -*-

puts "你好，世界！";
```


**
[运行实例 »](https://www.runoob.com/try/showrb.php?filename=helloworld_cn)


输出结果为：


```
你好，世界！
```


所以如果大家再学习过程中，源代码文件中，若包含中文编码，则需要注意两点：


- 1. 必须在首行添加 **# -*- coding: UTF-8 -*-**,告诉解释器使用utf-8来解析源码。
- 2. 必须设置编辑器保存文件的编码为utf-8。
- ### 点我分享笔记 笔记需要是本篇文章的内容扩展！ [文章投稿，可点击这里](https://www.runoob.com/tougao) [注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite) ### 分享笔记前必须登录！ [注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)--> ** 取消 * * 分享笔记 昵称昵称 (必填)
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