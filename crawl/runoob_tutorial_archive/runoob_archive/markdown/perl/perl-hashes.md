# Perl 哈希

- Source: https://www.runoob.com/perl/perl-hashes.html

哈希是 **key/value** 对的集合。


Perl中哈希变量以百分号 (%) 标记开始。


访问哈希元素格式：**${key}**。


以下是一个简单的哈希实例：


## 实例



```perl
#!/usr/bin/perl

%data = ('google', 'google.com', 'runoob', 'runoob.com', 'taobao', 'taobao.com');

print "\$data{'google'} = $data{'google'}\n";
print "\$data{'runoob'} = $data{'runoob'}\n";
print "\$data{'taobao'} = $data{'taobao'}\n";
```


执行以上程序，输出结果为：


![](https://www.runoob.com/wp-content/uploads/2016/06/EBB194B3-1C00-4693-9485-62B6F000641F.jpg)


---


## 创建哈希


创建哈希可以通过以下两种方式：


### 一、为每个 key 设置 value


```
$data{'google'} = 'google.com';
$data{'runoob'} = 'runoob.com';
$data{'taobao'} = 'taobao.com';
```


### 二、通过列表设置


列表中第一个元素为 key，第二个为 value。


```
%data = ('google', 'google.com', 'runoob', 'runoob.com', 'taobao', 'taobao.com');
```


也可以使用 **=>** 符号来设置 key/value:


```
%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
```


以下实例是上面实例的变种，使用 **-** 来代替引号：


```
%data = (-google=>'google.com', -runoob=>'runoob.com', -taobao=>'taobao.com');
```


使用这种方式 key 不能出现空格，读取元素方式为：


```
$val = $data{-google}
$val = $data{-runoob}
```


---


## 访问哈希元素


访问哈希元素格式：**${key}**，实例如下：


## 实例



```perl
#!/usr/bin/perl

%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');

print "\$data{'google'} = $data{'google'}\n";
print "\$data{'runoob'} = $data{'runoob'}\n";
print "\$data{'taobao'} = $data{'taobao'}\n";
```


执行以上程序，输出结果为：


![](https://www.runoob.com/wp-content/uploads/2016/06/EBB194B3-1C00-4693-9485-62B6F000641F.jpg)


---


## 读取哈希值


你可以像数组一样从哈希中提取值。


哈希值提取到数组语法格式：**@{key1,key2}**。


## 实例



```perl
#!/uer/bin/perl

%data = (-taobao => 45, -google => 30, -runoob => 40);

@array = @data{-taobao, -runoob};

print "Array : @array\n";
```


执行以上程序，输出结果为：


```
Array : 45 40
```


---


## 读取哈希的 key 和 value


### 读取所有key


我们可以使用 **keys** 函数读取哈希所有的键，语法格式如下：


```
keys %HASH
```


该函数返回所有哈希的所有 key 的数组。


## 实例



```perl
#!/usr/bin/perl

%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');

@names = keys %data;

print "$names[0]\n";
print "$names[1]\n";
print "$names[2]\n";
```


执行以上程序，输出结果为：


```
taobao
google
runoob
```


类似的我们可以使用 **values** 函数来读取哈希所有的值,语法格式如下：


```
values %HASH
```


该函数返回所有哈希的所有 value 的数组。


## 实例



```perl
#!/usr/bin/perl

%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');

@urls = values %data;

print "$urls[0]\n";
print "$urls[1]\n";
print "$urls[2]\n";
```


执行以上程序，输出结果为：


```
taobao.com
runoob.com
google.com
```


---


## 检测元素是否存在


如果你在哈希中读取不存在的 key/value 对 ，会返回 **undefined** 值，且在执行时会有警告提醒。


为了避免这种情况，我们可以使用 **exists** 函数来判断key是否存在，存在的时候读取：


## 实例



```perl
#!/usr/bin/perl

%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');

if( exists($data{'facebook'} ) ){
   print "facebook 的网址为 $data{'facebook'} \n";
}
else
{
   print "facebook 键不存在\n";
}
```


执行以上程序，输出结果为：


```
facebook 键不存在
```


以上代码中我们使用了 **IF...ELSE** 语句，在后面的章节我们会具体介绍。


---


## 获取哈希大小


哈希大小为元素的个数，我们可以通过先获取 key 或 value 的所有元素数组，再计算数组元素多少来获取哈希的大小，实例如下：


## 实例



```perl
#!/usr/bin/perl

%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');

@keys = keys %data;
$size = @keys;
print "1 - 哈希大小: $size\n";

@values = values %data;
$size = @values;
print "2 - 哈希大小: $size\n";
```


执行以上程序，输出结果为：


```
1 - 哈希大小: 3
2 - 哈希大小: 3
```


---


## 哈希中添加或删除元素


添加 key/value 对可以通过简单的赋值来完成。但是删除哈希元素你需要使用 **delete** 函数：


## 实例



```perl
#!/usr/bin/perl

%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
@keys = keys %data;
$size = @keys;
print "1 - 哈希大小: $size\n";

# 添加元素
$data{'facebook'} = 'facebook.com';
@keys = keys %data;
$size = @keys;
print "2 - 哈希大小: $size\n";

# 删除哈希中的元素
delete $data{'taobao'};
@keys = keys %data;
$size = @keys;
print "3 - 哈希大小: $size\n";
```


执行以上程序，输出结果为：


```
1 - 哈希大小: 3
2 - 哈希大小: 4
3 - 哈希大小: 3
```


---

## 迭代哈希


我们可以使用 foreach 和 while 来迭代哈希：


## 实例 - 使用 foreach


```perl
#!/usr/bin/perl

%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
foreach $key (keys %data){
    print "$data{$key}\n";
}
```


## 实例 - 使用 while


```perl
#!/usr/bin/perl

%data = ('google'=>'google.com', 'runoob'=>'runoob.com', 'taobao'=>'taobao.com');
while(($key, $value) = each(%data)){
    print "$data{$key}\n";
}
```


执行以上程序，输出结果为：


```
runoob.com
google.com
taobao.com
```









	  AI 思考中...





			** [Perl 数组](https://www.runoob.com/perl-arrays.html)
			[Perl 条件语句](https://www.runoob.com/perl-conditions.html) **













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