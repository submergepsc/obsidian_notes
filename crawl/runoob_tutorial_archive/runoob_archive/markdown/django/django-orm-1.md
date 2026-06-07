# Django ORM - 单表实例

- Source: https://www.runoob.com/django/django-orm-1.html

阅读本章节前你需要先阅读了 [Django 模型](https://www.runoob.com/django-model.html) 进行基础配置及了解常见问题的解决方案。


接下来我们重新创建一个项目 app01（如果之前已创建过，忽略以下操作）:


```
django-admin.py startproject app01
```


接下来在 settings.py 中找到 INSTALLED_APPS 这一项，如下：


```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',               # 添加此项
)
```


接下来，告诉 Django 使用 pymysql 模块连接 mysql 数据库：


## 实例


```python
# 在与 settings.py 同级目录下的 __init__.py 中引入模块和进行配置
import pymysql
pymysql.install_as_MySQLdb()
```


### 创建模型

在项目中的 models.py 中添加以下类：


## app01/models.py


```python
class Book(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    title = models.CharField(max_length=32) # 书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2) # 书籍价格
    publish = models.CharField(max_length=32) # 出版社名称
    pub_date = models.DateField() # 出版时间
```


然后在命令行执行以下命令：


```
$ python3 manage.py migrate   # 创建表结构

$ python3 manage.py makemigrations app01  # 让 Django 知道我们在我们的模型有一些变更
$ python3 manage.py migrate app01   # 创建表结构
```


### 常见报错信息


如果执行以上命令时会出现如下报错信息:


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_5.png)


原因是 MySQLclient 目前只支持到 Python3.4，因此如果使用的更高版本的 python，需要修改如下：


通过报错信息的文件路径找到 ...site-packages\Django-2.0-py3.6.egg\django\db\backends\mysql 这个路径里的 base.py 文件，把这两行代码注释掉（代码在文件开头部分）：


```
if version < (1, 3, 13):
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```


![](https://www.runoob.com/wp-content/uploads/2015/01/wUC7W1KOjgwuTi0n.png)


一般点报错的代码文件路径信息，会自动跳转到报错文件中行数，此时我们在报错的代码行数注释掉。


这时数据库 runoob 就会创建一个 app01_book 的表。


接下来我们在app01 项目里添加 views.py 和 models.py 文件，app01 项目目录结构：


```
app01
|-- app01
|   |-- __init__.py
|   |-- __pycache__
|   |-- asgi.py
|   |-- migrations
|   |-- models.py
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   `-- wsgi.py
```


### 数据库添加


规则配置：


## app01/urls.py: 文件代码：



```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book),
]
```


**方式一：**模型类实例化对象


需从 app 目录引入 models.py 文件：


```
from app 目录 import models
```


并且实例化对象后要执行 **对象.save()** 才能在数据库中新增成功。


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    book = models.Book(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8")
    book.save()
    return HttpResponse("<p>数据添加成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_1.gif)


**方式二：**通过 ORM 提供的 objects 提供的方法 create 来实现（推荐）


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.create(title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10")
    print(books, type(books)) # Book object (18)
    return HttpResponse("<p>数据添加成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_2.gif)


### 查找


使用 **all()** 方法来查询所有内容。


返回的是 QuerySet 类型数据，类似于 list，里面放的是一个个模型类的对象，可用索引下标取出模型类的对象。


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.all()
    print(books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_3.gif)


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_8.png)


**filter()** 方法用于查询符合条件的数据。

返回的是 QuerySet 类型数据，类似于 list，里面放的是满足条件的模型类的对象，可用索引下标取出模型类的对象。


pk=3 的意思是主键 primary key=3，相当于 id=3。


因为 id 在 pycharm 里有特殊含义，是看内存地址的内置函数 id()，因此用 pk。


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.filter(pk=5)
    print(books)
    print("//////////////////////////////////////")
    books = models.Book.objects.filter(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_4.gif)


**exclude() ** 方法用于查询不符合条件的数据。

返回的是 QuerySet 类型数据，类似于 list，里面放的是不满足条件的模型类的对象，可用索引下标取出模型类的对象。


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.exclude(pk=5)
    print(books)
    print("//////////////////////////////////////")
    books = models.Book.objects.exclude(publish='菜鸟出版社', price=300)
    print(books, type(books))  # QuerySet类型，类似于list。
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_5.gif)


**get()** 方法用于查询符合条件的返回模型类的对象符合条件的对象只能为一个，如果符合筛选条件的对象超过了一个或者没有一个都会抛出错误。


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.get(pk=5)
    books = models.Book.objects.get(pk=18)  # 报错，没有符合条件的对象
    books = models.Book.objects.get(price=200)  # 报错，符合条件的对象超过一个
    print(books, type(books))  # 模型类的对象
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_6.gif)


**order_by()** 方法用于对查询结果进行排序。

返回的是 QuerySet类型数据，类似于list，里面放的是排序后的模型类的对象，可用索引下标取出模型类的对象。


**注意：**


- a、参数的字段名要加引号。
- b、降序为在字段前面加个负号 **-**。


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.order_by("price") # 查询所有，按照价格升序排列
    books = models.Book.objects.order_by("-price") # 查询所有，按照价格降序排列
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_7.gif)


**reverse()** 方法用于对查询结果进行反转。

返回的是 QuerySe t类型数据，类似于 list，里面放的是反转后的模型类的对象，可用索引下标取出模型类的对象。


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    # 按照价格升序排列：降序再反转
    books = models.Book.objects.order_by("-price").reverse()
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_8.gif)


**count() **方法用于查询数据的数量返回的数据是整数。


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.count() # 查询所有数据的数量
    books = models.Book.objects.filter(price=200).count() # 查询符合条件数据的数量
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_9.gif)


**first()** 方法返回第一条数据返回的数据是模型类的对象也可以用索引下标 **[0]**。


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.first() # 返回所有数据的第一条数据
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_10.gif)


last() 方法返回最后一条数据返回的数据是模型类的对象不能用索引下标 **[-1]**，ORM 没有逆序索引。


## app01/views.py: 文件代码：



```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.last() # 返回所有数据的最后一条数据
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_11.gif)


**exists()** 方法用于判断查询的结果 QuerySet 列表里是否有数据。


返回的数据类型是布尔，有为 true，没有为 false。

**注意：**判断的数据类型只能为 QuerySet 类型数据，不能为整型和模型类的对象。


## 实例


```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.exists()
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为整型
    books = models.Book.objects.count().exists()
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为模型类对象
    books = models.Book.objects.first().exists()
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_12.gif)


**values()** 方法用于查询部分字段的数据。


返回的是 QuerySet 类型数据，类似于 list，里面不是模型类的对象，而是一个可迭代的字典序列，字典里的键是字段，值是数据。


**注意：**


- 参数的字段名要加引号
- 想要字段名和数据用 **values**
- ## 实例
```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    # 查询所有的id字段和price字段的数据
    books = models.Book.objects.values("pk","price")
    print(books[0]["price"],type(books)) # 得到的是第一条记录的price字段的数据
    return HttpResponse("<p>查找成功！</p>")
```
 ![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_13.gif) **values_list()** 方法用于查询部分字段的数据。 返回的是 QuerySet 类型数据，类似于 list，里面不是模型类的对象，而是一个个元组，元组里放的是查询字段对应的数据。 **注意：** 参数的字段名要加引号
- 只想要数据用 values_list


## 实例


```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    # 查询所有的price字段和publish字段的数据
    books = models.Book.objects.values_list("price","publish")
    print(books)
    print(books[0][0],type(books)) # 得到的是第一条记录的price字段的数据
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_14.gif)


**distinct() **方法用于对数据进行去重。


返回的是 QuerySet 类型数据。


**注意：**


- 对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。
- distinct() 一般是联合 values 或者 values_list 使用。


## 实例


```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    # 查询一共有多少个出版社
    books = models.Book.objects.values_list("publish").distinct() # 对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。
    books = models.Book.objects.distinct()
    return HttpResponse("<p>查找成功！</p>")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_15.gif)


**filter()** 方法基于双下划线的模糊查询（exclude 同理）。


**注意：**filter 中运算符号只能使用等于号 = ，不能使用大于号 > ，小于号


```
# 查询价格大于等于200的数据
books = models.Book.objects.filter(price__gte=200)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_18.gif)

**__lt** 小于，=号后面为数字。


```
# 查询价格小于300的数据
books=models.Book.objects.filter(price__lt=300)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_19.gif)

**__lte** 小于等于，= 号后面为数字。


```
# 查询价格小于等于300的数据
books=models.Book.objects.filter(price__lte=300)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_20.gif)

**__range** 在 ... 之间，左闭右闭区间，= 号后面为两个元素的列表。


```
books=models.Book.objects.filter(price__range=[200,300])
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_21.gif)

**__contains** 包含，= 号后面为字符串。


```
books=models.Book.objects.filter(title__contains="菜")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_22.gif)


**__icontains** 不区分大小写的包含，= 号后面为字符串。


```
books=models.Book.objects.filter(title__icontains="python") # 不区分大小写
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_23.gif)

**__startswith** 以指定字符开头，= 号后面为字符串。


```
books=models.Book.objects.filter(title__startswith="菜")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_24.gif)


**__endswith** 以指定字符结尾，= 号后面为字符串。


```
books=models.Book.objects.filter(title__endswith="教程")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_25.gif)


**__year** 是 DateField 数据类型的年份，= 号后面为数字。


```
books=models.Book.objects.filter(pub_date__year=2008)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_26.gif)


**__month** 是DateField 数据类型的月份，= 号后面为数字。


```
books=models.Book.objects.filter(pub_date__month=10)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_27.gif)


**__day** 是DateField 数据类型的天数，= 号后面为数字。


```
books=models.Book.objects.filter(pub_date__day=01)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_28.gif)


### 删除


**方式一：**使用模型类的 **对象.delete()**。


**返回值：**元组，第一个元素为受影响的行数。


```
books=models.Book.objects.filter(pk=8).first().delete()
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_29.gif)


**方式二**：使用 QuerySet **类型数据.delete()**(推荐)


**返回值：**元组，第一个元素为受影响的行数。


```
books=models.Book.objects.filter(pk__in=[1,2]).delete()
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_30.gif)


**注意：**


- a. Django 删除数据时，会模仿 SQL约束 ON DELETE CASCADE 的行为，也就是删除一个对象时也会删除与它相关联的外键对象。
- b. delete() 方法是 QuerySet 数据类型的方法，但并不适用于 Manager 本身。也就是想要删除所有数据，不能不写 all。


```
books=models.Book.objects.delete()　 # 报错
books=models.Book.objects.all().delete()　　 # 删除成功
```


### 修改


**方式一：**


```
模型类的对象.属性 = 更改的属性值
模型类的对象.save()
```


**返回值：**编辑的模型类的对象。


```
books = models.Book.objects.filter(pk=7).first()
books.price = 400
books.save()
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_31.gif)


**方式二：**QuerySet 类型数据.update(字段名=更改的数据)（推荐）


**返回值：**整数，受影响的行数


## 实例


```python
from django.shortcuts import render,HttpResponse
from app01 import models
def add_book(request):
    books = models.Book.objects.filter(pk__in=[7,8]).update(price=888)
    return HttpResponse(books)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-orm_32.gif)








	  AI 思考中...





			** [Django 视图](https://www.runoob.com/django-views.html)
			[Django ORM – 多表实例](https://www.runoob.com/django-orm-2.html) **













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