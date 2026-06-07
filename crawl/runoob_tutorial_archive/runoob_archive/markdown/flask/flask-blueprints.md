# Flask 蓝图 (Blueprints)

- Source: https://www.runoob.com/flask/flask-blueprints.html

Flask 的蓝图（Blueprints）是一种组织代码的机制，允许你将 Flask 应用分解成多个模块。这样可以更好地组织应用逻辑，使得应用更具可维护性和可扩展性。

每个蓝图可以有自己的路由、视图函数、模板和静态文件，这样可以将相关的功能分组。


通过使用蓝图，你可以将 Flask 应用拆分成多个模块，每个模块处理相关的功能，使得代码更加清晰和易于管理。


**创建蓝图**：在独立的模块中定义蓝图，并指定路由和视图函数。

**注册蓝图**：在主应用中注册蓝图，并设置路由前缀。


**使用蓝图中的模板和静态文件**：将模板和静态文件放在蓝图的 `templates` 和 `static` 文件夹中。

**使用请求钩子和错误处理**：在蓝图中定义请求钩子和错误处理函数。


**为什么需要蓝图？**

- **模块化开发**：将功能相关的代码组织在一起
- **代码复用**：蓝图可以跨项目重用
- **延迟绑定**：可以在不绑定到应用的情况下定义路由
- **多团队协作**：不同团队可以并行开发不同蓝图
- **灵活部署**：可以按需注册蓝图


---


## 1. 创建蓝图


蓝图是 Flask 提供的一种将应用程序分解为更小、更模块化组件的方式。它本质上是一个记录了操作（如路由、错误处理器等）的容器，这些操作会在蓝图注册到应用时被执行。


**创建蓝图涉及到以下几个步骤：**


**定义蓝图：**在一个独立的模块（文件）中定义蓝图。

**注册蓝图：**在主应用中注册蓝图，使其生效。


假设我们要创建一个博客应用，其中包含用户管理和博客功能，我们可以将这些功能分成两个蓝图：auth 和 blog。


项目结构：


```
yourapp/
│
├── app.py
├── auth/
│   ├── __init__.py
│   └── routes.py
│
└── blog/
    ├── __init__.py
    └── routes.py
```


### 2. 定义蓝图

auth/routes.py 文件代码：


## 实例


```python
from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    return redirect(url_for('auth.login'))

@auth_bp.route('/register')
def register():
    return render_template('auth/register.html')
```


**Blueprint('auth', __name__)**：创建一个名为 auth 的蓝图。


蓝图中定义的路由函数可以用来处理请求。


blog/routes.py 文件代码：


## 实例


```python
from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def index():
    return render_template('blog/index.html')

@blog_bp.route('/post/<int:post_id>')
def post(post_id):
    return render_template('blog/post.html', post_id=post_id)
```


**Blueprint('blog', __name__)**：创建一个名为 blog 的蓝图。


### 3. 注册蓝图

app.py 文件代码：


## 实例


```python
from flask import Flask

app = Flask(__name__)

# 导入蓝图 (修改为从模块导入)
from auth.routes import auth_bp
from blog.routes import blog_bp

# 注册蓝图 (添加了静态文件处理)
app.register_blueprint(
    auth_bp,
    url_prefix='/auth',
    static_folder='static',  # 可选的静态文件配置
    template_folder='templates'
)

app.register_blueprint(
    blog_bp,
    url_prefix='/blog',
    static_folder='static',  # 可选的静态文件配置
    template_folder='templates'
)

if __name__ == '__main__':
    app.run(debug=True)
```


- `app.register_blueprint(auth, url_prefix='/auth')`：注册 `auth` 蓝图，并将所有的路由前缀设置为 `/auth`。
- `app.register_blueprint(blog, url_prefix='/blog')`：注册 `blog` 蓝图，并将所有的路由前缀设置为 `/blog`。


### 4. 使用蓝图中的模板和静态文件

蓝图中的模板和静态文件应放在蓝图的文件夹下的 templates 和 static 子文件夹中。


项目结构：


```
yourapp/
│
├── app.py                # 主应用入口文件
│
├── auth/                 # 认证模块
│   ├── __init__.py       # 蓝图初始化文件
│   └── routes.py         # 认证相关路由
│
├── blog/                 # 博客模块
│   ├── __init__.py       # 蓝图初始化文件
│   └── routes.py         # 博客相关路由
│
└── templates/            # 模板目录
    ├── auth/             # 认证模板
    │   ├── login.html    # 登录页面
    │   └── register.html # 注册页面
    │
    └── blog/             # 博客模板
        ├── index.html    # 博客首页
        └── post.html     # 博文详情页
```


### 5. 在蓝图中使用请求钩子

蓝图支持请求钩子，例如 **before_request** 和 **after_request**，可以在蓝图中定义这些钩子来处理请求和响应。


auth/routes.py 文件代码：


## 实例


```python
@auth.before_app_request
def before_request():
    # 执行在每个请求之前的操作
    pass

@auth.after_app_request
def after_request(response):
    # 执行在每个请求之后的操作
    return response
```


### 6. 在蓝图中定义错误处理

蓝图也可以定义自己的错误处理函数。


blog/routes.py 文件代码：


## 实例


```python
@blog.errorhandler(404)
def page_not_found(error):
    return 'Page not found', 404
```









	  AI 思考中...





			** [Flask 数据库操作](https://www.runoob.com/flask-orm.html)
			[Flask 错误处理](https://www.runoob.com/flask-error.html) **













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