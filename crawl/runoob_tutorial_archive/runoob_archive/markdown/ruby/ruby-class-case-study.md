# Ruby 类案例

- Source: https://www.runoob.com/ruby/ruby-class-case-study.html

下面将创建一个名为 Customer 的 Ruby 类，声明两个方法：


- *display_details*：该方法用于显示客户的详细信息。
- *total_no_of_customers*：该方法用于显示在系统中创建的客户总数量。


## 实例


```ruby
#!/usr/bin/ruby

class Customer
   @@no_of_customers=0
   def initialize(id, name, addr)
      @cust_id=id
      @cust_name=name
      @cust_addr=addr
   end
   def display_details()
      puts "Customer id #@cust_id"
      puts "Customer name #@cust_name"
      puts "Customer address #@cust_addr"
    end
    def total_no_of_customers()
       @@no_of_customers += 1
       puts "Total number of customers: #@@no_of_customers"
    end
end
```


*display_details* 方法包含了三个 puts 语句，显示了客户 ID、客户名字和客户地址。其中，puts 语句：


```ruby
puts "Customer id #@cust_id"
```


将在一个单行上显示文本 Customer id 和变量 @cust_id 的值。


当您想要在一个单行上显示实例变量的文本和值时，您需要在 puts 语句的变量名前面放置符号（#）。文本和带有符号（#）的实例变量应使用双引号标记。


第二个方法，total_no_of_customers，包含了类变量 @@no_of_customers。表达式 @@no_of_ customers+=1 在每次调用方法 total_no_of_customers 时，把变量 no_of_customers 加 1。通过这种方式，您将得到类变量中的客户总数量。


现在创建两个客户，如下所示：


```ruby
cust1=Customer.new("1", "John", "Wisdom Apartments, Ludhiya")
cust2=Customer.new("2", "Poul", "New Empire road, Khandala")
```


在这里，我们创建了 Customer 类的两个对象，cust1 和 cust2，并向 new 方法传递必要的参数。当 initialize 方法被调用时，对象的必要属性被初始化。


一旦对象被创建，您需要使用两个对象来调用类的方法。如果您想要调用方法或任何数据成员，您可以编写代码，如下所示：


```ruby
cust1.display_details()
cust1.total_no_of_customers()
```


对象名称后总是跟着一个点号，接着是方法名称或数据成员。我们已经看到如何使用 cust1 对象调用两个方法。使用 cust2 对象，您也可以调用两个方法，如下所示：


```ruby
cust2.display_details()
cust2.total_no_of_customers()
```


## 保存并执行代码


现在，把所有的源代码放在 main.rb 文件中，如下所示：


## 实例


```ruby
#!/usr/bin/ruby

class Customer
   @@no_of_customers=0
   def initialize(id, name, addr)
      @cust_id=id
      @cust_name=name
      @cust_addr=addr
   end
   def display_details()
      puts "Customer id #@cust_id"
      puts "Customer name #@cust_name"
      puts "Customer address #@cust_addr"
   end
   def total_no_of_customers()
      @@no_of_customers += 1
      puts "Total number of customers: #@@no_of_customers"
   end
end

# 创建对象
cust1=Customer.new("1", "John", "Wisdom Apartments, Ludhiya")
cust2=Customer.new("2", "Poul", "New Empire road, Khandala")

# 调用方法
cust1.display_details()
cust1.total_no_of_customers()
cust2.display_details()
cust2.total_no_of_customers()
```


**
[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=customer_demo&type=ruby)


接着，运行程序，如下所示：


```
$ ruby main.rb
```


这将产生以下结果：


```
Customer id 1
Customer name John
Customer address Wisdom Apartments, Ludhiya
Total number of customers: 1
Customer id 2
Customer name Poul
Customer address New Empire road, Khandala
Total number of customers: 2
```









	  AI 思考中...





			** [Ruby 类和对象](https://www.runoob.com/ruby-class.html)
			[Ruby 变量](https://www.runoob.com/ruby-variable.html) **













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