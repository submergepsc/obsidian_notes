# Django 路由

- Source: https://www.runoob.com/django/django-routers.html

路由简单的来说就是根据用户请求的 URL 链接来判断对应的处理程序，并返回处理结果，也就是 URL 与 Django 的视图建立映射关系。


Django 路由在 urls.py 配置，urls.py 中的每一条配置对应相应的处理方法。


Django 不同版本 urls.py 配置有点不一样：


### Django1.1.x 版本


**url() 方法**：普通路径和正则路径均可使用，需要自己手动添加正则首位限制符号。


## 实例


```python
from django.conf.urls import url # 用 url 需要引入

urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^index/$', views.index), # 普通路径
    url(r'^articles/([0-9]{4})/$', views.articles), # 正则路径
]
```


### Django 2.2.x 之后的版本


- path：用于普通路径，不需要自己手动添加正则首位限制符号，底层已经添加。
- re_path：用于正则路径，需要自己手动添加正则首位限制符号。


## 实例


```python
from django.urls import re_path # 用re_path 需要引入
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index), # 普通路径
    re_path(r'^articles/([0-9]{4})/$', views.articles), # 正则路径
]
```


**总结：**Django1.1.x 版本中的 url 和 Django 2.2.x 版本中的 re_path 用法相同。


---


## 正则路径中的分组


### 正则路径中的无名分组


无名分组按位置传参，一一对应。


views 中除了 request，其他形参的数量要与 urls 中的分组数量一致。


## urls.py


```python
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("^index/([0-9]{4})/$", views.index),
]
```


## views.py


```python
from django.shortcuts import HttpResponse

def index(request, year):
    print(year) # 一个形参代表路径中一个分组的内容，按顺序匹配
    return HttpResponse('菜鸟教程')
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env1.png)


### 正则路径中的有名分组


语法：


```
(?P<组名>正则表达式)
```


有名分组按关键字传参，与位置顺序无关。


views 中除了 request，其他形参的数量要与 urls 中的分组数量一致， 并且 views 中的形参名称要与 urls 中的组名对应。


## urls.py


```python
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("^index/(?P[0-9]{4})/(?P[0-9]{2})/$", views.index),
]
```


## views.py


```python
from django.shortcuts import HttpResponse
def index(request, year, month):
    print(year,month) # 一个形参代表路径中一个分组的内容，按关键字对应匹配
    return HttpResponse('菜鸟教程')
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env2.png)


### 正则路径中的有名分组


### 路由分发(include)


**存在问题**：Django 项目里多个app目录共用一个 urls 容易造成混淆，后期维护也不方便。


**解决**：使用路由分发（include），让每个app目录都单独拥有自己的 urls。


**步骤：**


- 1、在每个 app 目录里都创建一个 urls.py 文件。
- 2、在项目名称目录下的 urls 文件里，统一将路径分发给各个 app 目录。


## 实例


```python
from django.contrib import admin
from django.urls import path,include # 从 django.urls 引入 include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("app01/", include("app01.urls")),
    path("app02/", include("app02.urls")),
]
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env3.png)


在各自 app 目录下，写自己的 urls.py 文件，进行路径跳转。


app01 目录:


```
from django.urls import path,re_path
from app01 import views # 从自己的 app 目录引入 views
urlpatterns = [
    re_path(r'^login/(?P<m>[0-9]{2})/$', views.index, ),
]
```


app02 目录:


```
from django.urls import path,re_path
from app02 import views # 从自己的 app 目录引入views
urlpatterns = [
    re_path("^xxx/(?P[0-9]{4})/$", views.xxx),
]
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env4.png)


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env5.png)


在各自 app 目录下的 views.py 文件中写各自的视图函数。


---


## 反向解析


随着功能的增加，路由层的 url 发生变化，就需要去更改对应的视图层和模板层的 url，非常麻烦，不便维护。


这时我们可以利用反向解析，当路由层 url 发生改变，在视图层和模板层动态反向解析出更改后的 url，免去修改的操作。


反向解析一般用在模板中的超链接及视图中的重定向。


### 普通路径


在 urls.py 中给路由起别名，**name="路由别名"**。


```
path("login1/", views.login, name="login")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env6.png)


在 views.py 中，从 django.urls 中引入 reverse，利用 **reverse("路由别名")** 反向解析:


```
return redirect(reverse("login"))
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env7.png)


在模板 templates 中的 HTML 文件中，利用 **{% url "路由别名" %}** 反向解析。


```
<form action="{% url 'login' %}" method="post">
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env8.png)


### 正则路径（无名分组）


在 urls.py 中给路由起别名，**name="路由别名"**。


```
re_path(r"^login/([0-9]{2})/$", views.login, name="login")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env9.png)


在 views.py 中，从 django.urls 中引入 reverse，利用 **reverse("路由别名"，args=(符合正则匹配的参数,))** 反向解析。


```
return redirect(reverse("login",args=(10,)))
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env10.png)


在模板 templates 中的 HTML 文件中利用 **{% url "路由别名" 符合正则匹配的参数 %}** 反向解析。


```
<form action="{% url 'login' 10 %}" method="post">
```



![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env11.png)


### 正则路径（有名分组）


在 urls.py 中给路由起别名，**name="路由别名"**。


```
re_path(r"^login/(?P<year>[0-9]{4})/$", views.login, name="login")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env12.png)


在 views.py 中，从 django.urls 中引入 reverse，利用 **reverse("路由别名"，kwargs={"分组名":符合正则匹配的参数}) **反向解析。


```
return redirect(reverse("login",kwargs={"year":3333}))
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env13.png)


在模板 templates 中的 HTML 文件中，利用 **{% url "路由别名" 分组名=符合正则匹配的参数 %}** 反向解析。


```
<form action="{% url 'login' year=3333 %}" method="post">
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env14.png)


---


## 命名空间

命名空间（英语：Namespace）是表示标识符的可见范围。

一个标识符可在多个命名空间中定义，它在不同命名空间中的含义是互不相干的。

一个新的命名空间中可定义任何标识符，它们不会与任何重复的标识符发生冲突，因为重复的定义都处于其它命名空间中。


**存在问题：**路由别名 name 没有作用域，Django 在反向解析 URL 时，会在项目全局顺序搜索，当查找到第一个路由别名 name 指定 URL 时，立即返回。当在不同的 app 目录下的urls 中定义相同的路由别名 name 时，可能会导致 URL 反向解析错误。


**解决：**使用命名空间。


### 普通路径

定义命名空间（include 里面是一个元组）格式如下：


```
include(("app名称：urls"，"app名称"))
```


实例：


```
path("app01/", include(("app01.urls","app01")))
path("app02/", include(("app02.urls","app02")))
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env15.png)


在 app01/urls.py 中起相同的路由别名。


```
path("login/", views.login, name="login")
```



![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env16.png)


在 views.py 中使用名称空间，语法格式如下：


```
reverse("app名称：路由别名")
```


实例：


```
return redirect(reverse("app01:login")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env17.png)


在 templates 模板的 HTML 文件中使用名称空间，语法格式如下：


```
{% url "app名称：路由别名" %}
```


实例：


```
<form action="{% url 'app01:login' %}" method="post">
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-env18.png)








	  AI 思考中...





			** [Django 简介](https://www.runoob.com/django-intro.html)
			[Django 视图](https://www.runoob.com/django-views.html) **













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