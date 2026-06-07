# Django ORM – 多表实例

- Source: https://www.runoob.com/django/django-orm-2.html

表与表之间的关系可分为以下三种：


- **一对一**: 一个人对应一个身份证号码，数据字段设置 unique。
- **一对多**: 一个家庭有多个人，一般通过外键来实现。
- **多对多**: 一个学生有多门课程，一个课程有很多学生，一般通过第三个表来实现关联。


![](https://www.runoob.com/wp-content/uploads/2020/05/orm11.png)


### 创建模型


接下来我们来看下多表多实例。


## 实例


```python
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")

class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()
```


**说明：**


- 1、EmailField 数据类型是邮箱格式，底层继承 CharField，进行了封装，相当于 MySQL 中的 varchar。
- 2、Django1.1 版本不需要联级删除：on_delete=models.CASCADE，Django2.2 需要。
- 3、一般不需要设置联级更新.
- 4、外键在一对多的多中设置：**models.ForeignKey("关联类名", on_delete=models.CASCADE)**。
- 5、OneToOneField = ForeignKey(...，unique=True)设置一对一。
- 6、若有模型类存在外键，创建数据时，要先创建外键关联的模型类的数据，不然创建包含外键的模型类的数据时，外键的关联模型类的数据会找不到。


### 表结构


**书籍表 Book**：title 、 price 、 pub_date 、 publish（外键，多对一） 、 authors（多对多）


**出版社表 Publish**：name 、 city 、 email


**作者表 Author**：name 、 age 、 au_detail（一对一）


**作者详情表 AuthorDetail**：gender 、 tel 、 addr 、 birthday


以下是表格关联说明：


[![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_1.png)](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_1.png)


### 插入数据

我们在 MySQL 中执行以下 SQL 插入操作：


```
insert into app01_publish(name,city,email) values ("华山出版社", "华山", "[email protected]"), ("明教出版社", "黑木崖", "[email protected]")

# 先插入 authordetail 表中多数据
insert into app01_authordetail(gender,tel,addr,birthday) values (1,13432335433,"华山","1994-5-23"), (1,13943454554,"黑木崖","1961-8-13"), (0,13878934322,"黑木崖","1996-5-20")

# 再将数据插入 author，这样 author 才能找到 authordetail
insert into app01_author(name,age,au_detail_id) values ("令狐冲",25,1), ("任我行",58,2), ("任盈盈",23,3)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_1.gif)


---


## ORM - 添加数据


### 一对多(外键 ForeignKey)


**方式一:** 传对象的形式，返回值的数据类型是对象，书籍对象。


**步骤：**


- a. 获取出版社对象
- b. 给书籍的出版社属性 pulish 传出版社对象


## app01/views.py 文件代码：


```python
def add_book(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  给书籍的出版社属性publish传出版社对象
    book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
    print(book, type(book))
    return HttpResponse(book)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_2.gif)


方式二: 传对象 id 的形式(由于传过来的数据一般是 id,所以传对象 id 是常用的)。


一对多中，设置外键属性的类(多的表)中，MySQL 中显示的字段名是:**外键属性名_id**。


返回值的数据类型是对象，书籍对象。


**步骤：**

- a. 获取出版社对象的 id
- b. 给书籍的关联出版社字段 pulish_id 传出版社对象的 id


## app01/views.py 文件代码：


```python
def add_book(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  获取出版社对象的id
    pk = pub_obj.pk
    #  给书籍的关联出版社字段 publish_id 传出版社对象的id
    book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)
    print(book, type(book))
    return HttpResponse(book)
```



![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_3.gif)


### 多对多(ManyToManyField)：在第三张关系表中新增数据


**方式一:** 传对象形式，无返回值。


**步骤：**


- a. 获取作者对象
- b. 获取书籍对象
- c. 给书籍对象的 authors 属性用 add 方法传作者对象


## app01/views.py 文件代码：


```python
def add_book(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    ying = models.Author.objects.filter(name="任盈盈").first()
    #  获取书籍对象
    book = models.Book.objects.filter(title="菜鸟教程").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象
    book.authors.add(chong, ying)
    return HttpResponse(book)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_4.gif)


**方式二:** 传对象id形式，无返回值。


**步骤：**


- a. 获取作者对象的 id
- b. 获取书籍对象
- c. 给书籍对象的 authors 属性用 add 方法传作者对象的 id


## app01/views.py 文件代码：


```python
def add_book(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    #  获取作者对象的id
    pk = chong.pk
    #  获取书籍对象
    book = models.Book.objects.filter(title="冲灵剑法").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象的id
    book.authors.add(pk)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_5.gif)


### 关联管理器(对象调用)


**前提：**


- 多对多（双向均有关联管理器）
- 一对多（只有多的那个类的对象有关联管理器，即反向才有）


**语法格式：**


```
正向：属性名
反向：小写类名加 _set
```


**注意：**一对多只能反向


**常用方法：**


**add()**：用于多对多，把指定的模型对象添加到关联对象集（关系表）中。


**注意：**add() 在一对多(即外键)中，只能传对象（ *QuerySet数据类型），不能传 id（*[id表]）。


***[ ]** 的使用:

# 方式一：传对象

```python
book_obj = models.Book.objects.get(id=10)
author_list = models.Author.objects.filter(id__gt=2)
book_obj.authors.add(*author_list)  # 将 id 大于2的作者对象添加到这本书的作者集合中
# 方式二：传对象 id
book_obj.authors.add(*[1,3]) # 将 id=1 和 id=3 的作者对象添加到这本书的作者集合中
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_6.gif)


反向：**小写表名_set**


```python
ying = models.Author.objects.filter(name="任盈盈").first()
book = models.Book.objects.filter(title="冲灵剑法").first()
ying.book_set.add(book)
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_7.gif)


**create()**：创建一个新的对象，并同时将它添加到关联对象集之中。


返回新创建的对象。


```python
pub = models.Publish.objects.filter(name="明教出版社").first()
wo = models.Author.objects.filter(name="任我行").first()
book = wo.book_set.create(title="吸星大法", price=300, pub_date="1999-9-19", publish=pub)
print(book, type(book))
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_8.gif)


**remove()**：从关联对象集中移除执行的模型对象。

对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在，无返回值。


## 实例


```python
author_obj =models.Author.objects.get(id=1)
book_obj = models.Book.objects.get(id=11)
author_obj.book_set.remove(book_obj)
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_9.gif)


**clear()**：从关联对象集中移除一切对象，删除关联，不会删除对象。


对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在。


无返回值。


```python
#  清空独孤九剑关联的所有作者
book = models.Book.objects.filter(title="菜鸟教程").first()
book.authors.clear()
```


---


## ORM 查询

基于对象的跨表查询。


```
正向：属性名称
反向：小写类名_set
```


### 一对多


查询主键为 1 的书籍的出版社所在的城市（正向）。


## 实例


```python
book = models.Book.objects.filter(pk=10).first()
res = book.publish.city
print(res, type(res))
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_10.gif)


查询明教出版社出版的书籍名（反向）。

反向：**对象.小写类名_set(pub.book_set)** 可以跳转到关联的表(书籍表)。


**pub.book_set.all()**：取出书籍表的所有书籍对象，在一个 QuerySet 里，遍历取出一个个书籍对象。


## 实例


```python
pub = models.Publish.objects.filter(name="明教出版社").first()
res = pub.book_set.all()
for i in res:
    print(i.title)
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_11.gif)


### 一对一


查询令狐冲的电话（正向）


正向：对象.属性 (author.au_detail) 可以跳转到关联的表(作者详情表)


## 实例


```python
author = models.Author.objects.filter(name="令狐冲").first()
res = author.au_detail.tel
print(res, type(res))
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_12.gif)


查询所有住址在黑木崖的作者的姓名（反向）。

一对一的反向，用 **对象.小写类名** 即可，不用加 _set。


反向：对象.小写类名(addr.author)可以跳转到关联的表(作者表)。


## 实例


```python
addr = models.AuthorDetail.objects.filter(addr="黑木崖").first()
res = addr.author.name
print(res, type(res))
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_13.gif)


### 多对多

菜鸟教程所有作者的名字以及手机号（正向）。

正向：**对象.属性(book.authors)**可以跳转到关联的表(作者表)。

作者表里没有作者电话，因此再次通过**对象.属性(i.au_detail)**跳转到关联的表（作者详情表）。


## 实例


```python
book = models.Book.objects.filter(title="菜鸟教程").first()
res = book.authors.all()
for i in res:
    print(i.name, i.au_detail.tel)
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_14.gif)


查询任我行出过的所有书籍的名字（反向）。


## 实例


```python
author = models.Author.objects.filter(name="任我行").first()
res = author.book_set.all()
for i in res:
    print(i.title)
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_15.gif)


---


## 基于双下划线的跨表查询


### 正向：属性名称__跨表的属性名称 反向：小写类名__跨表的属性名称


### 一对多

查询菜鸟出版社出版过的所有书籍的名字与价格。

## 实例


```python
res = models.Book.objects.filter(publish__name="菜鸟出版社").values_list("title", "price")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_16.gif)

反向：通过 小**写类名__跨表的属性名称（book__title，book__price）** 跨表获取数据。

## 实例


```python
res = models.Publish.objects.filter(name="菜鸟出版社").values_list("book__title","book__price")
return HttpResponse("ok")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_17.gif)


### 多对多

查询任我行出过的所有书籍的名字。

正向：通过 属性名称__跨表的属性名称(authors__name) 跨表获取数据：


```
res = models.Book.objects.filter(authors__name="任我行").values_list("title")
```


反向：通过 小写类名__跨表的属性名称（book__title） 跨表获取数据：


```
res = models.Author.objects.filter(name="任我行").values_list("book__title")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_18.gif)


### 一对一


查询任我行的手机号。

正向：通过 **属性名称__跨表的属性名称(au_detail__tel) **跨表获取数据。


```
res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_19.gif)


反向：通过 **小写类名__跨表的属性名称（author__name） **跨表获取数据。


```
res = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm2_20.gif)








	  AI 思考中...





			** [Django ORM – 单表实例](https://www.runoob.com/django-orm-1.html)
			[Django ORM – 多表实例（聚合与分组查询）](https://www.runoob.com/django-orm-3.html) **













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