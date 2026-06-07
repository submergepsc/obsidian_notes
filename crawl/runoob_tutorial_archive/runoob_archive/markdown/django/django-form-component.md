# Django Form 组件

- Source: https://www.runoob.com/django/django-form-component.html

Django Form 组件用于对页面进行初始化，生成 HTML 标签，此外还可以对用户提交的数据进行校验（显示错误信息）。


**报错信息显示顺序：**


- 先显示字段属性中的错误信息，然后再显示局部钩子的错误信息。
- 若显示了字段属性的错误信息，就不会显示局部钩子的错误信息。
- 若有全局钩子，则全局钩子是等所有的数据都校验完，才开始进行校验，并且全局钩子的错误信息一定会显示。


使用 Form 组件，需要先导入 forms：


```
from django import forms
```


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-forms_1.png)


接下来我们在 app01 目录下创建一个 My_forms.py:


## app01/My_forms.py


```python
from django import forms
from django.core.exceptions import ValidationError
from app01 import models

class EmpForm(forms.Form):
    name = forms.CharField(min_length=4, label="姓名", error_messages={"min_length": "你太短了", "required": "该字段不能为空!"})
    age = forms.IntegerField(label="年龄")
    salary = forms.DecimalField(label="工资")
```


**字段属性：**


- **label**：输入框前面的文本信息。
- **error_message**：自定义显示的错误信息，属性值是字典， 其中 required 为设置不能为空时显示的错误信息的 key。


## app01/views.py


```python
from django.shortcuts import render, HttpResponse
from app01.My_Forms import EmpForm
from app01 import models
from django.core.exceptions import ValidationError
# Create your views here.

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "add_emp.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():  # 进行数据校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            data.pop('r_salary')
            print(data)

            models.Emp.objects.create(**data)
            return HttpResponse(
                'ok'
            )
            # return render(request, "add_emp.html", {"form": form})
        else:
            print(form.errors)    # 打印错误信息
            clean_errors = form.errors.get("__all__")
            print(222, clean_errors)
        return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})
```


app01/urls.py 文件添加以下规则：


```
path('add_emp/', views.add_emp)
```


HTML 模版：


## app01/add_emp.html


```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>

<h3>添加员工</h3>

{#1、自己手动写HTML页面#}
<form action="" method="post">
    <p>姓名：<input type="text" name="name"></p>
    <p>年龄：<input type="text" name="age"></p>
    <p>工资：<input type="text" name="salary"></p>
    <input type="submit">
</form>

{#2、通过form对象的as_p方法实现#}
{#<form action="" method="post" novalidate>#}
{#    {% csrf_token %}#}
{#    {{ form.as_p }}#}
{#    <input type="submit">#}
{#</form>#}

{#3、手动获取form对象的字段#}
{#<form action="" method="post" novalidate>#}
{#    {% csrf_token %}#}
{#    <div>#}
{#        <label for="id_{{ form.name.name }}">姓名</label>#}
{#        {{ form.name }} <span>{{ form.name.errors.0 }}</span>#}
{#    </div>#}
{#    <div>#}
{#        <label for="id_{{ form.age.name }}">年龄</label>#}
{#        {{ form.age }} <span>{{ form.age.errors.0 }}</span>#}
{#    </div>#}
{#    <div>#}
{#        <label for="id_salary">工资</label>#}
{#        {{ form.salary }} <span>{{ form.salary.errors.0 }}</span>#}
{#    </div>#}
{#    <input type="submit">#}
{#</form>#}

{#4、用for循环展示所有字段#}
{#<form action="" method="post" novalidate>#}
{#    {% csrf_token %}#}
{#    {% for field in form %}#}
{#        <div>#}
{#            <label for="id_{{ field.name }}">{{ field.label }}</label>#}
{#            {{ field }} <span>{{ field.errors.0 }}</span>#}
{#        </div>#}
{#    {% endfor %}#}
{#    <input type="submit">#}
{#</form>#}

</body>
</html>
```


运行结果如下图所示：


![](https://static.jyshare.com/images/mix/Django-forms_1.gif)


### 局部钩子和全局钩子


定义 Form 类:


## app01/My_forms.py


```python
from django import forms
from django.core.exceptions import ValidationError
from app01 import models
class EmpForm(forms.Form):
    name = forms.CharField(min_length=5, label="姓名", error_messages={"required": "该字段不能为空!",
                                                                     "min_length": "用户名太短。"})
    age = forms.IntegerField(label="年龄")
    salary = forms.DecimalField(max_digits=5, decimal_places=2, label="工资")
    r_salary = forms.DecimalField(max_digits=5, decimal_places=2, label="请再输入工资")

    def clean_name(self):  # 局部钩子
        val = self.cleaned_data.get("name")

        if val.isdigit():
            raise ValidationError("用户名不能是纯数字")
        elif models.Emp.objects.filter(name=val):
            raise ValidationError("用户名已存在！")
        else:
            return val

    def clean(self):  # 全局钩子 确认两次输入的工资是否一致。
        val = self.cleaned_data.get("salary")
        r_val = self.cleaned_data.get("r_salary")

        if val == r_val:
            return self.cleaned_data
        else:
            raise ValidationError("请确认工资是否一致。")
```


views.py 文件代码：


## app01/views.py


```python
def add_emp(request):
    if request.method == "GET":
        form = EmpForm()  # 初始化form对象
        return render(request, "add_emp.html", {"form":form})
    else:
        form = EmpForm(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect("/index/")
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "add_emp.html", {"form": form, "clear_errors": clear_errors})
```


模板文件代码如下：


## app01/add_emp.html


```python
<form action="" method="post" novalidate>
    {% csrf_token %}
    <div>
        <label for="id_{{ form.name.name }}">姓名</label>
        {{ form.name }} <span>{{ form.name.errors.0 }}</span>
    </div>
    <div>
        <label for="id_{{ form.age.name }}">年龄</label>
        {{ form.age }} <span>{{ form.age.errors.0 }}</span>
    </div>
    <div>
        <label for="id_salary">工资</label>
        {{ form.salary }} <span>{{ form.salary.errors.0 }}{{ clear_errors.0 }}</span>
    </div>
    <div>
        <label for="id_r_salary">请再输入工资</label>
        {{ form.r_salary }} <span>{{ form.r_salary.errors.0 }}{{ clear_errors.0 }}</span>
    </div>
    <input type="submit">
</form>
```


运行结果如下图所示：


![](https://www.runoob.com/wp-content/uploads/2020/05/Django-forms_2.gif)


[![](https://www.runoob.com/wp-content/uploads/2020/05/1563239932711.png)](https://www.runoob.com/wp-content/uploads/2020/05/1563239932711.png)








	  AI 思考中...





			** [Django ORM – 多表实例（聚合与分组查询）](https://www.runoob.com/django-orm-3.html)
			[Django 用户认证（Auth）组件](https://www.runoob.com/django-auth.html) **













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