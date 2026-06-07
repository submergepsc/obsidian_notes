# PyCharm 创建 Django 项目

- Source: https://www.runoob.com/pycharm/pycharm-django.html

PyCharm 是一款强大的 Python IDE，提供了对 Django 框架的出色支持，尤其是在其专业版（PyCharm Pro）中。


### 启动 PyCharm 并新建项目


- 打开 PyCharm，点击 "新建项目"
- 在左侧选择 "Django"
- 设置项目位置（Location）
- 配置 Python 解释器（建议新建虚拟环境）


![](https://www.runoob.com/wp-content/uploads/2025/05/3a99daf8-66d4-40f5-98e2-adb6ee31732f.png)


### 配置项目参数


- **项目名称**：使用小写字母和下划线组合（如 DjangoProject）
- **模板语言**：默认选择 Django
- **前端框架**：可根据需要选择（初学者可不选）
- **启用 Django admin**：可勾选

![](https://www.runoob.com/wp-content/uploads/2025/05/19f5a1b1-0dab-4e78-8025-aaaf44e2c488.png)


### 等待项目初始化


PyCharm 会自动：


- 创建虚拟环境
- 安装 Django 最新稳定版
- 生成基础项目结构


---


## 项目结构解析


创建完成后，您会看到以下主要文件和目录：


![](https://www.runoob.com/wp-content/uploads/2025/05/76dac1e3-a3a9-4fb7-ac0a-81088e53c41c.png)


### 项目根目录


- **manage.py**：Django 命令行工具
- **项目同名目录**（如 DjangoProject/）：包含项目主要配置


### 项目配置目录


- **init**.py：标识这是一个 Python 包
- **settings.py**：项目配置文件
- **urls.py**：URL 路由配置
- **wsgi.py**：WSGI 服务器配置


### 其他重要文件


- **requirements.txt**：项目依赖文件（PyCharm 可能自动生成）
- **venv/**：虚拟环境目录（如果选择创建虚拟环境）


---


## 运行 Django 开发服务器


### 通过 PyCharm 运行


- 点击 PyCharm 右上角的运行配置下拉菜单
- 选择 "配置 -> 编辑"![](https://www.runoob.com/wp-content/uploads/2025/05/67201bfa-a82d-43cf-abf2-b5d60f1c8da1.png)
- 确保配置了 Django 服务器
- 点击绿色运行按钮![](https://www.runoob.com/wp-content/uploads/2025/05/29f913ea-ba58-47e8-a357-6219e80c947a.png)


### 通过命令行运行


- 打开 PyCharm 的终端
- 输入命令：`python3 manage.py runserver` ![](https://www.runoob.com/wp-content/uploads/2025/05/7afe9f62-fb6b-4e6e-931c-58b03c848c22.png)启动成功后，终端信息显示如下： ![](https://www.runoob.com/wp-content/uploads/2025/05/c7bd6507-91f1-407c-9848-3f0a48fab646.png)
- 访问 http://127.0.0.1:8000 查看默认页面: ![](https://www.runoob.com/wp-content/uploads/2025/05/97164d7b-e924-4309-aba3-dbbc69ffecc2.png)


### 常见问题解决


- **端口冲突**：使用 `python manage.py runserver 8080` 指定其他端口
- **数据库未迁移**：首次运行需执行 `python manage.py migrate`


---


## 创建 Django 应用


### 创建新应用


在 PyCharm 的终端中输入：


```
python3 manage.py startapp myapp
```


![](https://www.runoob.com/wp-content/uploads/2025/05/311b2d84-ccab-44fd-b49e-bec3dfade362.png)


将应用添加到 `settings.py` 的 **INSTALLED_APPS** 中:


```
INSTALLED_APPS = [
    ...
    'myapp',
]
```


![](https://www.runoob.com/wp-content/uploads/2025/05/4a49bc19-34e8-41c3-b90f-4e7fbe497ac3.png)


在项目 `urls.py` 中包含应用路由：


## 实例


```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]
```


![](https://www.runoob.com/wp-content/uploads/2025/05/d094b9cf-af54-4cf1-b791-115b59c2b517.png)


### 应用目录结构


- **migrations/**：数据库迁移文件
- **admin.py**：管理后台配置
- **apps.py**：应用配置
- **models.py**：数据模型定义
- **tests.py**：测试代码
- **views.py**：视图函数


### myapp 目录下配置 URL 路由


打开 myapp/models.py，定义模型。例如：


## 实例


```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```


保存后，运行 python manage.py makemigrations 和 python manage.py migrate 以更新数据库。


** 创建视图和 URL：**


在 myapp/views.py 中定义视图：


## 实例


```python
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myapp/post_list.html', {'posts': posts})
```


在 myapp/urls.py（需要手动创建）中配置 URL：


## 实例


```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```


在项目根目录创建 DjangoProject/templates/myapp/ 文件夹，然后在改文件夹下创建 post_list.html：


## 实例


```python
<!DOCTYPE html>
<html>
<head>
    <title>Post List</title>
</head>
<body>
    <h1>Posts</h1>
    <ul>
        {% for post in posts %}
            <li>{{ post.title }} - {{ post.created_at }}</li>
        {% empty %}
            <li>No posts available.</li>
        {% endfor %}
    </ul>
</body>
</html>
```


确保 settings.py 中的 TEMPLATES 设置包含正确的模板目录：


```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        ...
    }
]
```










	  AI 思考中...





			** [PyCharm 数据库工具](https://www.runoob.com/pycharm-dbtool.html)














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