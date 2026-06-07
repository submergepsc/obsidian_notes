# Django Admin 管理工具

- Source: https://www.runoob.com/django/django-admin-manage-tool.html

Django 提供了基于 web 的管理工具。


Django 自动管理工具是 django.contrib 的一部分。你可以在项目的 settings.py 中的 INSTALLED_APPS 看到它：


## /HelloWorld/HelloWorld/settings.py 文件代码：



```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
```


django.contrib是一套庞大的功能集，它是Django基本代码的组成部分。


---


## 激活管理工具


通常我们在生成项目时会在 urls.py 中自动设置好，我们只需去掉注释即可。


配置项如下所示：


## /HelloWorld/HelloWorld/urls.py 文件代码：



```python
# urls.py
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
```


当这一切都配置好后，Django 管理工具就可以运行了。


---


## 使用管理工具


启动开发服务器，然后在浏览器中访问 http://127.0.0.1:8000/admin/，得到如下界面：

![](https://www.runoob.com/wp-content/uploads/2015/01/admin1.png)

你可以通过命令 **python manage.py createsuperuser** 来创建超级用户，如下所示：


```
# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: [email protected]
Password:
Password (again):
Superuser created successfully.
[root@solar HelloWorld]#
```


之后输入用户名密码登录，界面如下：

![](https://www.runoob.com/wp-content/uploads/2015/01/A995340B-8F8C-4777-9B79-846B6A34508A.jpg)

为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin。比如，我们之前在 TestModel 中已经创建了模型 Test 。修改 TestModel/admin.py:


## HelloWorld/TestModel/admin.py: 文件代码：



```python
from django.contrib import admin
from TestModel.models import Test

# Register your models here.
admin.site.register(Test)
```


刷新后即可看到 Testmodel 数据表:

![](https://www.runoob.com/wp-content/uploads/2015/01/05F45176-FD08-4DD3-B17C-5759C7EBF515.jpg)

---


## 复杂模型


管理页面的功能强大，完全有能力处理更加复杂的数据模型。


先在 TestModel/models.py 中增加一个更复杂的数据模型：


## HelloWorld/TestModel/models.py: 文件代码：



```python
from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)

class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
```


这里有两个表。Tag 以 Contact 为外部键。一个 Contact 可以对应多个 Tag。


我们还可以看到许多在之前没有见过的属性类型，比如 IntegerField 用于存储整数。

![](https://www.runoob.com/wp-content/uploads/2015/01/admin4.png)

在 TestModel/admin.py 注册多个模型并显示：


## HelloWorld/TestModel/admin.py: 文件代码：



```python
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
admin.site.register([Test, Contact, Tag])
```


刷新管理页面，显示结果如下：

![](https://www.runoob.com/wp-content/uploads/2015/01/30A3C1A0-B31D-4E98-B129-D3F64BE3D5F4.jpg)

在以上管理工具我们就能进行复杂模型操作。


> 如果你之前还未创建表结构，可使用以下命令创建：
>
>
```
$ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate TestModel   # 创建表结构
```


---


## 自定义表单


我们可以自定义管理页面，来取代默认的页面。比如上面的 "add" 页面。我们想只显示 name 和 email 部分。修改 TestModel/admin.py:


## HelloWorld/TestModel/admin.py: 文件代码：



```python
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
```


以上代码定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。


里面的 fields 属性定义了要显示的字段。


由于该类对应的是 Contact 数据模型，我们在注册的时候，需要将它们一起注册。显示效果如下：

![](https://www.runoob.com/wp-content/uploads/2015/01/FCDF6B36-739A-4A05-9570-15E7508095CC.jpg)

我们还可以将输入栏分块，每个栏也可以定义自己的格式。修改 TestModel/admin.py为：


## HelloWorld/TestModel/admin.py: 文件代码：



```python
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
```


上面的栏目分为了 Main 和 Advance 两部分。classes 说明它所在的部分的 CSS 格式。这里让 Advance 部分隐藏：

![](https://www.runoob.com/wp-content/uploads/2015/01/67C81F36-BE39-4D09-BAC5-31379C3A2F41.jpg)

Advance 部分旁边有一个 Show 按钮，用于展开，展开后可点击 Hide 将其隐藏，如下图所示：

![](https://www.runoob.com/wp-content/uploads/2015/01/E63BA60D-A2A4-49BB-B412-E8495367A170.jpg)

---


## 内联(Inline)显示


上面的 Contact 是 Tag 的外部键，所以有外部参考的关系。


而在默认的页面显示中，将两者分离开来，无法体现出两者的从属关系。我们可以使用内联显示，让 Tag 附加在 Contact 的编辑页面上显示。


修改TestModel/admin.py：


## HelloWorld/TestModel/admin.py: 文件代码：



```python
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
```


显示效果如下：

![](https://www.runoob.com/wp-content/uploads/2015/01/8ACFC0E1-00C2-492E-9F0F-0FD471788C6A.jpg)

---


## 列表页的显示


在 Contact 输入数条记录后，Contact 的列表页看起来如下:

![](https://www.runoob.com/wp-content/uploads/2015/01/0232832C-A074-4D66-9282-818A5DB4B2A5.jpg)

我们也可以自定义该页面的显示，比如在列表中显示更多的栏目，只需要在 ContactAdmin 中增加 list_display 属性:


## HelloWorld/TestModel/admin.py: 文件代码：



```python
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
```


刷新页面显示效果如下：

![](https://www.runoob.com/wp-content/uploads/2015/01/1E47E4F4-BC33-4473-BBFA-EDF4FCE67E5C.jpg)

搜索功能在管理大量记录时非常有用，我们可以使用 search_fields 为该列表页增加搜索栏：


## HelloWorld/TestModel/admin.py: 文件代码：



```python
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
```


在本实例中我们搜索了 name 为 runoob 的记录，显示结果如下：

![](https://www.runoob.com/wp-content/uploads/2015/01/9FCFFE1A-A57A-4273-B296-3B8E7948F4AA.jpg)

Django Admin 管理工具还有非常多实用的功能，感兴趣的同学可以深入研究下。








	  AI 思考中...





			** [Django 表单](https://www.runoob.com/django-form.html)
			[Django Nginx+uwsgi 安装配置](https://www.runoob.com/django-nginx-uwsgi.html) **