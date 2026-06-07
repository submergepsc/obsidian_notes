# Django 视图 - FBV 与 CBV

- Source: https://www.runoob.com/django/django-views-fbv-cbv.html

**FBV（function base views）** 基于函数的视图，就是在视图里使用函数处理请求。


**CBV（class base views）** 基于类的视图，就是在视图里使用类处理请求。


### FBV

基于函数的视图其实我们前面章节一直在使用，就是使用了函数来处理用户的请求，查看以下实例：


路由配置：


## urls.py 文件


```python
urlpatterns = [
    path("login/", views.login),
]
```


## views.py 文件


```python
from django.shortcuts import render,HttpResponse

def login(request):
    if request.method == "GET":
        return HttpResponse("GET 方法")
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "runoob" and pwd == "123456":
            return HttpResponse("POST 方法")
        else:
            return HttpResponse("POST 方法1")
```


如果我们在浏览器中直接访问 http://127.0.0.1:8000/login/ ，输出结果为：


```
GET 方法
```


### CBV

基于类的视图，就是使用了类来处理用户的请求，不同的请求我们可以在类中使用不同方法来处理，这样大大的提高了代码的可读性。


定义的类要继承父类 View，所以需要先引入库：


```
from django.views import View
```


执行对应请求的方法前会优先执行 dispatch 方法(在get/post/put...方法前执行)，dispatch() 方法会根据请求的不同调用相应的方法来处理。

其实，在我们前面学到的知识都知道 Django 的 url 是将一个请求分配给可调用的函数的，而不是一个类，那是如何实现基于类的视图的呢？ 主要还是通过父类 View 提供的一个静态方法 as_view() ，as_view 方法是基于类的外部接口， 他返回一个视图函数，调用后请求会传递给 dispatch 方法，dispatch 方法再根据不同请求来处理不同的方法。


路由配置：


## urls.py 文件


```python
urlpatterns = [
    path("login/", views.Login.as_view()),
]
```


## views.py 文件


```python
from django.shortcuts import render,HttpResponse
from django.views import View

class Login(View):
    def get(self,request):
        return HttpResponse("GET 方法")

    def post(self,request):
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "runoob" and pwd == "123456":
            return HttpResponse("POST 方法")
        else:
            return HttpResponse("POST 方法 1")
```


如果我们在浏览器中直接访问 http://127.0.0.1:8000/login/ ，输出结果为：


```
GET 方法
```









	  AI 思考中...





			** [Django 中间件](https://www.runoob.com/django-middleware.html)
			[Django django-admin 命令](https://www.runoob.com/django-django-admin.html) **













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