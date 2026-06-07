# Ruby CGI Session

- Source: https://www.runoob.com/ruby/ruby-cgi-sessions.html

CGI::Session 可以为用户和CGI环境保存持久的会话状态，会话使用后需要关闭，这样可以保证数据写入到存储当中，当会话完成后，你需要删除该数据。


## 实例


```ruby
#!/usr/bin/ruby

require 'cgi'
require 'cgi/session'
cgi = CGI.new("html4")

sess = CGI::Session.new( cgi, "session_key" => "a_test",
                              "prefix" => "rubysess.")
lastaccess = sess["lastaccess"].to_s
sess["lastaccess"] = Time.now
if cgi['bgcolor'][0] =~ /[a-z]/
  sess["bgcolor"] = cgi['bgcolor']
end

cgi.out{
  cgi.html {
    cgi.body ("bgcolor" => sess["bgcolor"]){
      "The background of this page"    +
      "changes based on the 'bgcolor'" +
      "each user has in session."      +
      "Last access time: #{lastaccess}"
    }
  }
}
```


访问 "/cgi-bin/test.cgi?bgcolor=red" 将跳转到指定背景颜色的页面。


会话数据存在在服务器的临时文件目录中，prefix 参数指定了会话的前缀，将作为临时文件的前缀。这样你在服务器上可以轻松的识别不同的会话临时文件。


---


## CGI::Session 类


CGI::Session 保持了用户与 CGI 环境的持久状态。 会话可以在内存中，也可以在硬盘上。 ### 类方法 Ruby 类 Class CGI::Session 提供了简单的方法来创建 session:


```ruby
CGI::Session::new( cgi[, option])
```


启用一个新的 CGI 会话并返回相应的 CGI::Session 对象。选项可以是可选的哈希，可以是以下值：


- **session_key:** 键名保存会话 默认为 _session_id。
- **session_id:** 唯一的会话 ID。自动生成
- **new_session:** 如果为true，为当前会话创建一个新的Session id。 如果为 false, 通过 session_id 使用已存在的 session 标识。 如果省略该参数，如果可用则使用现有的会话，否则创建一个新的。
- **database_manager:** 用于保存 sessions 的类，可以是 CGI::Session::FileStore or CGI::Session::MemoryStore。默认为 FileStore。
- **tmpdir:** 对于 FileStore, 为 session 的错存储目录。
- **prefix:** 对于 FileStore, 为 session 文件的前缀。


### 实例化方法


| 序号 | 方法描述 |
| --- | --- |
| 1 | [ ]返回给定 key 的值。查看实例。 |
| 2 | [ ]=设置给定 key 的值。 查看实例。 |
| 3 | delete调用底层数据库管理的删除方法。对于 FileStore, 删除包含 session 的物理文件。 对于 MemoryStore, 从内存中移除 session 数据。 |
| 4 | update调用底层数据库管理的更新方法。 对于 FileStore, 将 session 写入到磁盘中。 对于 MemoryStore则无效果。 |








	  AI 思考中...





			** [Ruby CGI Cookie](https://www.runoob.com/ruby-cgi-cookies.html)
			[Ruby 发送邮件 – SMTP](https://www.runoob.com/ruby-sending-email.html) **













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