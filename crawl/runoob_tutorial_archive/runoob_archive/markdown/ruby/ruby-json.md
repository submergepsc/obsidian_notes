# Ruby JSON

- Source: https://www.runoob.com/ruby/ruby-json.html

本章节我们将为大家介绍如何使用 Ruby 语言来编码和解码 JSON 对象。


---


## 环境配置


在使用 Ruby 编码或解码 JSON 数据前，我们需要先安装 Ruby JSON 模块。在安装该模块前你需要先安装 Ruby gem，我们使用 Ruby gem 安装 JSON 模块。 但是，如果你使用的是最新版本的 Ruby，可能已经安装了 gem，解析来我们就可以使用以下命令来安装Ruby JSON 模块：


```
$gem install json
```


---


## 使用 Ruby 解析 JSON


以下为JSON数据，将该数据存储在 input.json 文件中：


## input.json 文件


```ruby
{
  "President": "Alan Isaac",
  "CEO": "David Richardson",

  "India": [
    "Sachin Tendulkar",
    "Virender Sehwag",
    "Gautam Gambhir"
  ],

  "Srilanka": [
    "Lasith Malinga",
    "Angelo Mathews",
    "Kumar Sangakkara"
  ],

  "England": [
    "Alastair Cook",
    "Jonathan Trott",
    "Kevin Pietersen"
  ]
}
```


以下的 Ruby 程序用于解析以上 JSON 文件；


## 实例


```ruby
#!/usr/bin/ruby
require 'rubygems'
require 'json'
require 'pp'

json = File.read('input.json')
obj = JSON.parse(json)

pp obj
```


以上实例执行结果为：


```
{"President"=>"Alan Isaac",
 "CEO"=>"David Richardson",

 "India"=>
  ["Sachin Tendulkar", "Virender Sehwag", "Gautam Gambhir"],

"Srilanka"=>
  ["Lasith Malinga ", "Angelo Mathews", "Kumar Sangakkara"],

 "England"=>
  ["Alastair Cook", "Jonathan Trott", "Kevin Pietersen"]
}
```









	  AI 思考中...





			** [Ruby 数据类型](https://www.runoob.com/ruby-datatypes.html)
			[Ruby 中文编码](https://www.runoob.com/ruby-encoding.html) **













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