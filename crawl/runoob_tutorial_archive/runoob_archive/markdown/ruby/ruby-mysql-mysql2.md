# Ruby 连接 Mysql - MySql2

- Source: https://www.runoob.com/ruby/ruby-mysql-mysql2.html

前面一章节我们介绍了 Ruby DBI 的使用。这章节我们技术 Ruby 连接 Mysql 更高效的驱动 mysql2，目前也推荐使用这种方式连接 MySql。


安装 mysql2 驱动：


```ruby
gem install mysql2
```


你需要使用 –with-mysql-config 配置 mysql_config 的路径，如： **–with-mysql-config=/some/random/path/bin/mysql_config**。


### 连接


连接数据库语法如下：


```ruby
client = Mysql2::Client.new(:host => "localhost", :username => "root")
```


更多参数可以查看 [http://api.rubyonrails.org/classes/ActiveRecord/ConnectionAdapters/MysqlAdapter.html](http://api.rubyonrails.org/classes/ActiveRecord/ConnectionAdapters/MysqlAdapter.html)。


### 查询


```ruby
results = client.query("SELECT * FROM users WHERE group='githubbers'")
```


### 特殊字符转义


```ruby
escaped = client.escape("gi'thu\"bbe\0r's")
results = client.query("SELECT * FROM users WHERE group='#{escaped}'")
```


计算结果集返回的数量:


```
results.count
```


### 迭代结果集：


```ruby
results.each do |row|
  # row 是哈希
  # 键值是数据库字段
  # 值都是对应 MySQL中数据
  puts row["id"] # row["id"].class == Fixnum
  if row["dne"]  # 不存在则是 nil
    puts row["dne"]
  end
end
```


## 实例


```ruby
#!/usr/bin/ruby -w
require 'mysql2'

client = Mysql2::Client.new(
    :host     => '127.0.0.1', # 主机
    :username => 'root',      # 用户名
    :password => '123456',    # 密码
    :database => 'test',      # 数据库
    :encoding => 'utf8'       # 编码
    )
results = client.query("SELECT VERSION()")
results.each do |row|
  puts row
end
```


以上实例运行输出结果为：


```
{"VERSION()"=>"5.6.21"}
```


### 连接选项


```ruby
Mysql2::Client.new(
  :host,
  :username,
  :password,
  :port,
  :database,
  :socket = '/path/to/mysql.sock',
  :flags = REMEMBER_OPTIONS | LONG_PASSWORD | LONG_FLAG | TRANSACTIONS | PROTOCOL_41 | SECURE_CONNECTION | MULTI_STATEMENTS,
  :encoding = 'utf8',
  :read_timeout = seconds,
  :write_timeout = seconds,
  :connect_timeout = seconds,
  :reconnect = true/false,
  :local_infile = true/false,
  :secure_auth = true/false,
  :default_file = '/path/to/my.cfg',
  :default_group = 'my.cfg section',
  :init_command => sql
  )
```


更多内容请参阅：[http://www.rubydoc.info/gems/mysql2/0.2.3/frames](http://www.rubydoc.info/gems/mysql2/0.2.3/frames)。 AI 思考中... ** [Ruby RubyGems](https://www.runoob.com/ruby-rubygems.html) ### 点我分享笔记 笔记需要是本篇文章的内容扩展！
**

[文章投稿，可点击这里](https://www.runoob.com/tougao)


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)


### 分享笔记前必须登录！


[注册邀请码获取方式](https://www.runoob.com/w3cnote/runoob-user-test-intro.html#invite)
-->





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