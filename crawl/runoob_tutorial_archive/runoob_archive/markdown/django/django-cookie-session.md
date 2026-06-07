# Django cookie 与 session

- Source: https://www.runoob.com/django/django-cookie-session.html

Cookie 是存储在客户端计算机上的文本文件，并保留了各种跟踪信息。


识别返回用户包括三个步骤：


- 服务器脚本向浏览器发送一组 Cookie。例如：姓名、年龄或识别号码等。
- 浏览器将这些信息存储在本地计算机上，以备将来使用。
- 当下一次浏览器向 Web 服务器发送任何请求时，浏览器会把这些 Cookie 信息发送到服务器，服务器将使用这些信息来识别用户。


HTTP 是一种"无状态"协议，这意味着每次客户端检索网页时，客户端打开一个单独的连接到 Web 服务器，服务器会自动不保留之前客户端请求的任何记录。


但是仍然有以下三种方式来维持 Web 客户端和 Web 服务器之间的 session 会话：


## Cookies


一个 Web 服务器可以分配一个唯一的 session 会话 ID 作为每个 Web 客户端的 cookie，对于客户端的后续请求可以使用接收到的 cookie 来识别。


在Web开发中，使用 session 来完成会话跟踪，session 底层依赖 Cookie 技术。


![](https://www.runoob.com/wp-content/uploads/2020/05/cookie.png)


### Django 中 Cookie 的语法


设置 cookie:


```
rep.set_cookie(key,value,...)
rep.set_signed_cookie(key,value,salt='加密盐',...)
```


获取 cookie:


```
request.COOKIES.get(key)
```


删除 cookie:


```
rep =HttpResponse || render || redirect
rep.delete_cookie(key)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-cs_2.png)


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-cs_3.png)


### 创建应用和模型


## models.py


```python
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-cs_4.png)


## urls.py


```python
from django.contrib import admin
from django.urls import path
from cookie import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('index/', views.index),
    path('logout/', views.logout),
    path('order/', views.order)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-cs_5.png)


## views.py


```python
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
    print(user_obj.username)

    if not user_obj:
        return redirect("/login/")
    else:
        rep = redirect("/index/")
        rep.set_cookie("is_login", True)
        return rep

def index(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/login/')
    return render(request, "index.html")

def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    return rep # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面

def order(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, "order.html")
```


以下创建三个模板文件：login.html、index.html、order.html。


## login.html


```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h3>用户登录</h3>
<form action="" method="post">
    {% csrf_token %}
    <p>用户名： <input type="text" name="username"></p>
    <p>密码： <input type="password" name="pwd"></p>
    <input type="submit">
</form>

</body>
</html>
```


## index.html


```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h2>index 页面。。。</h2>

<a href="/logout/">注销</a>

</body>
</html>
```


## order.html


```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h2>order 页面。。。</h2>

<a href="/logout/">注销</a>

</body>
</html>
```


运行结果如下图所示：


![](https://static.jyshare.com/images/mix/Django-cs_1.gif)


## Session(保存在服务端的键值对)


服务器在运行时可以为每一个用户的浏览器创建一个其独享的 session 对象，由于 session 为用户浏览器独享，所以用户在访问服务器的 web 资源时，可以把各自的数据放在各自的 session 中，当用户再去访问该服务器中的其它 web 资源时，其它 web 资源再从用户各自的 session 中取出数据为用户服务。


![](https://www.runoob.com/wp-content/uploads/2020/05/5-21-1.jpg)


### 工作原理


- a. 浏览器第一次请求获取登录页面 login。
- b. 浏览器输入账号密码第二次请求，若输入正确，服务器响应浏览器一个 index 页面和一个键为 sessionid，值为随机字符串的 cookie，即 set_cookie ("sessionid",随机字符串)。
- c. 服务器内部在 django.session 表中记录一条数据。 django.session 表中有三个字段。 session_key：存的是随机字符串，即响应给浏览器的 cookie 的 sessionid 键对应的值。
- session_data：存的是用户的信息，即多个 request.session["key"]=value，且是密文。
- expire_date：存的是该条记录的过期时间（默认14天）


d. 浏览器第三次请求其他资源时，携带 cookie :{sessionid:随机字符串}，服务器从 django.session 表中根据该随机字符串取出该用户的数据，供其使用（即保存状态）。


**注意:** django.session 表中保存的是浏览器的信息，而不是每一个用户的信息。 因此， 同一浏览器多个用户请求只保存一条记录（后面覆盖前面）,多个浏览器请求才保存多条记录。


cookie 弥补了 http 无状态的不足，让服务器知道来的人是"谁"，但是 cookie 以文本的形式保存在浏览器端，安全性较差，且最大只支持 4096 字节，所以只通过 cookie 识别不同的用户，然后，在对应的 session 里保存私密的信息以及超过 4096 字节的文本。


session 设置：


```
request.session["key"] = value
```


执行步骤：


- a. 生成随机字符串
- b. 把随机字符串和设置的键值对保存到 django_session 表的 session_key 和 session_data 里
- c. 设置 **cookie：set_cookie("sessionid",随机字符串)** 响应给浏览器


session 获取：


```
request.session.get('key')
```


执行步骤：

- a. 从 cookie 中获取 sessionid 键的值，即随机字符串。
- b. 根据随机字符串从 django_session 表过滤出记录。
- c. 取出 session_data 字段的数据。


session 删除，删除整条记录（包括 session_key、session_data、expire_date 三个字段）：


```
request.session.flush()
```


删除 session_data 里的其中一组键值对：


```
del request.session["key"]
```


执行步骤：

- a. 从 cookie 中获取 sessionid 键的值，即随机字符串
- b. 根据随机字符串从 django_session 表过滤出记录
- c. 删除过滤出来的记录


### 实例


创建路由:


## urls.py


```python
from session import views as session_views

urlpatterns = [
    path('session_login/', session_views.login),
    path('s_index/', session_views.s_index),
    path('s_logout/', session_views.s_logout),
]
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-cs_8.png) 创建视图函数:


## views.py


```python
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
    print(user_obj.username)

    if not user_obj:
        return redirect("/session_login/")
    else:
        request.session['is_login'] = True
        request.session['user1'] = username
        return redirect("/s_index/")

def s_index(request):
    status = request.session.get('is_login')
    if not status:
        return redirect('/session_login/')
    return render(request, "s_index.html")

def s_logout(request):
   # del request.session["is_login"] # 删除session_data里的一组键值对
    request.session.flush() # 删除一条记录包括(session_key session_data expire_date)三个字段
    return redirect('/session_login/')
```


模板文件：


## s_index.html


```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h2>session_index 页面。。。{{ request.session.user1 }}</h2>
<a href="/s_logout/">注销</a>
</body>
</html>
```


运行结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-cs_2.gif)








	  AI 思考中...





			** [Django 用户认证（Auth）组件](https://www.runoob.com/django-auth.html)
			[Django 中间件](https://www.runoob.com/django-middleware.html) **













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