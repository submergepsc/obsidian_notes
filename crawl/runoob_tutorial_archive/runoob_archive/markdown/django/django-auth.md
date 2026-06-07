# Django 用户认证（Auth）组件

- Source: https://www.runoob.com/django/django-auth.html

Django 用户认证（Auth）组件一般用在用户的登录注册上，用于判断当前的用户是否合法，并跳转到登陆成功或失败页面。


Django 用户认证（Auth）组件需要导入 auth 模块:


```
# 认证模块
from django.contrib import auth

# 对应数据库
from django.contrib.auth.models import User
```


返回值是用户对象。


创建用户对象的三种方法：


- **create()**：创建一个普通用户，密码是明文的。
- **create_user()**：创建一个普通用户，密码是密文的。
- **create_superuser()**：创建一个超级用户，密码是密文的，要多传一个邮箱 email 参数。

**参数：**


- username: 用户名。
- password：密码。
- email：邮箱 (create_superuser 方法要多加一个 email)。


```
from django.contrib.auth.models import User
User.objects.create(username='runboo',password='123')
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-auth_1.gif)


```
from django.contrib.auth.models import User
User.objects.create_user(username='runbooo',password='123')
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-auth_2.gif)


```
from django.contrib.auth.models import User
User.objects.create_superuser(username='runboooo',password='123',email='[email protected]')
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-auth_3.gif)


验证用户的用户名和密码使用 authenticate() 方法，从需要 auth_user 表中过滤出用户对象。


使用前要导入：


```
from django.contrib import auth
```


参数：


- username：用户名
- password：密码


**返回值：**如果验证成功，就返回用户对象，反之，返回 None。


## 实例


```python
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    valid_num = request.POST.get("valid_num")
    keep_str = request.session.get("keep_str")
    if keep_str.upper() == valid_num.upper():
        user_obj = auth.authenticate(username=username, password=password)
        print(user_obj.username)
```





![](https://www.runoob.com/wp-content/uploads/2020/05/Django-auth_4.gif)


给验证成功的用户加 session，将 request.user 赋值为用户对象。

登陆使用 login() 方法。

使用前要导入：


```
from django.contrib import auth
```


参数：


- request：用户对象

返回值：None


## 实例


```python
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    valid_num = request.POST.get("valid_num")
    keep_str = request.session.get("keep_str")
    if keep_str.upper() == valid_num.upper():
        user_obj = auth.authenticate(username=username, password=password)
        print(user_obj.username)
        if not user_obj:
            return redirect("/login/")
        else:

            auth.login(request, user_obj)
            path = request.GET.get("next") or "/index/"
            print(path)
            return redirect(path)
    else:
        return redirect("/login/")
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-auth_1.png)


注销用户使用 logout() 方法，需要清空 session 信息，将 request.user 赋值为匿名用户。


使用前要导入：


```
from django.contrib import auth
```


参数：


- request：用户对象

返回值：None


## 实例


```python
def logout(request):
    ppp = auth.logout(request)
    print(ppp) # None
    return redirect("/login/")
```


设置装饰器，给需要登录成功后才能访问的页面统一加装饰器。


使用前要导入：


```
from django.contrib.auth.decorators import login_required
```


## 实例


```python
from django.contrib.auth.decorators import login_required @login_required
def index(request):
  return HttpResponse("index页面。。。")
```


设置从哪个页面访问，登录成功后就返回哪个页面。


**解析：**


django 在用户访问页面时，如果用户是未登录的状态，就给用户返回登录页面。

此时，该登录页面的 URL 后面有参数：next=用户访问的页面的 URL。

因此，设置在用户登录成功后重定向的 URL 为 next 参数的值。

但是，若用户一开始就输入登录页面 logi，request.GET.get("next") 就取不到值，所以在后面加 or，可以设置自定义返回的页面。


## 实例


```python
# 如果直接输入 login、get() 就取不到值，path 可以自定义设置返回的页面
path = request.GET.get("next") or "/index/"
return redirect(path)
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-auth_5.gif)









	  AI 思考中...





			** [Django Form 组件](https://www.runoob.com/django-form-component.html)
			[Django cookie 与 session](https://www.runoob.com/django-cookie-session.html) **













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