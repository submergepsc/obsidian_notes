# Flask 第一个应用

- Source: https://www.runoob.com/flask/flask-step1.html

上一章节我们已经成功安装了 Flask，接下来我们可以创建一个简单的 Flask 应用。


首先，创建一个名为 app.py 的文件，并添加以下内容：


## 实例


```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```


在命令行中运行 Flask 应用：


```
python app.py
```


你会看到 Flask 开发服务器启动，并显示类似于以下内容：


```
...
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 977-918-914
...
```


打开浏览器，访问 http://127.0.0.1:5000/，应该会看到 "Hello, World!" 的消息，表示 Flask 已成功安装并运行。

![](https://www.runoob.com/wp-content/uploads/2024/08/flask-step-1.png)


### 代码解析：


- **from flask import Flask**： 这行代码从 `flask` 模块中导入了 `Flask` 类。`Flask` 类是 Flask 框架的核心，用于创建 Flask 应用程序实例。
- **app = Flask(__name__)**： 这行代码创建了一个 Flask 应用实例。`__name__` 是一个特殊的 Python 变量，它在模块被直接运行时是 `'__main__'`，在被其他模块导入时是模块的名字。传递 `__name__` 给 `Flask` 构造函数允许 Flask 应用找到和加载配置文件。
- **@app.route('/')**： 这是一个装饰器，用于告诉 Flask 哪个 URL 应该触发下面的函数。在这个例子中，它指定了根 URL（即网站的主页）。
- **def hello_world():**： 这是定义了一个名为 `hello_world` 的函数，它将被调用当用户访问根URL时。
- **return 'Hello, World!'**： 这行代码是 `hello_world` 函数的返回值。当用户访问根 URL 时，这个字符串将被发送回用户的浏览器。
- **if __name__ == '__main__':**：这行代码是一个条件判断，用于检查这个模块是否被直接运行，而不是被其他模块导入。如果是直接运行，下面的代码块将被执行。
- **app.run(debug=True)**：这行代码调用 Flask 应用实例的 `run` 方法，启动 Flask 内置的开发服务器。`debug=True` 参数会启动调试模式，这意味着应用会在代码改变时自动重新加载，并且在发生错误时提供一个调试器。








	  AI 思考中...





			** [Flask 安装](https://www.runoob.com/flask-install.html)
			[Flask 基本概念](https://www.runoob.com/flask-basic-concept.html) **













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