# Flask 部署

- Source: https://www.runoob.com/flask/flask-deployment.html

Flask 部署是将你的 Flask 应用程序发布到生产环境中的过程，使其可以被用户访问。

部署 Flask 应用涉及选择合适的服务器和环境配置。

以下是常见的 Flask 部署方法和步骤，包括使用 WSGI 服务器和 Web 服务器，以及如何在不同平台上部署 Flask 应用。


**选择部署方式**：

- 使用 Gunicorn、uWSGI 或 Waitress 作为 WSGI 服务器。
- 使用 Nginx 或 Apache 作为反向代理服务器。
- 可以选择在 Heroku 或 Docker 上部署。


**部署步骤**：

- 安装并配置 WSGI 服务器。
- 配置 Web 服务器（如 Nginx）。
- 可选：在 Heroku 或 Docker 上部署。

**监控和维护**：

- 监控应用的性能和日志。
- 定期更新依赖和应用代码。


---

## 1. 选择部署方式

Flask 应用通常需要一个 WSGI 服务器来处理 Python 应用程序和 HTTP 请求，通常与一个 Web 服务器（如 Nginx 或 Apache）配合使用。常见的 WSGI 服务器有：


- **Gunicorn**：一个流行的 WSGI 服务器，适用于 UNIX 系统。
- **uWSGI**：支持多种协议的高性能 WSGI 服务器，适用于 UNIX 和 Windows 系统。
- **Waitress**：一个简单且高效的 WSGI 服务器，适用于 Windows 系统。


---

## 2. 使用 Gunicorn 部署 Flask 应用


### 2.1 安装 Gunicorn


```
pip install gunicorn
```


### 2.2 运行 Flask 应用


假设你的 Flask 应用在 app.py 文件中，且应用实例名为 app，可以使用以下命令启动 Gunicorn 服务器：


```
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```


- `-w 4`：启动 4 个工作进程。
- `-b 0.0.0.0:8000`：绑定到所有网络接口上的 8000 端口。
- `app:app`：指定 Flask 应用实例的位置，格式为 `模块名:实例名`。


### 2.3 配置 Nginx 作为反向代理


Nginx 通常用作反向代理，将请求转发到 Gunicorn。

以下是一个 Nginx 配置示例，/etc/nginx/sites-available/yourapp 文件内容：


```
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```


### 2.4 启用 Nginx 配置


```
sudo ln -s /etc/nginx/sites-available/yourapp /etc/nginx/sites-enabled
sudo systemctl restart nginx
```


---

## 3. 使用 uWSGI 部署 Flask 应用

### 3.1 安装 uWSGI


```
pip install uwsgi
```


### 3.2 创建 uWSGI 配置文件


uwsgi.ini 文件内容：


```
[uwsgi]
module = app:app
master = true
processes = 4
socket = 127.0.0.1:8000
chmod-socket = 660
vacuum = true
die-on-term = true
```


### 3.3 运行 uWSGI


```
uwsgi --ini uwsgi.ini
```


### 3.4 配置 Nginx 作为反向代理


Nginx 配置与 Gunicorn 部署时类似，只需将 proxy_pass 地址更新为 http://127.0.0.1:8000。


---

## 4. 使用 Waitress 部署 Flask 应用


### 4.1 安装 Waitress


```
pip install waitress
```


### 4.2 运行 Flask 应用


## 实例


```python
from waitress import serve
from app import app

serve(app, host='0.0.0.0', port=8080)
```


### 4.3 配置 Nginx 作为反向代理


Nginx 配置与 Gunicorn 部署时类似，只需将 proxy_pass 地址更新为 http://127.0.0.1:8080。


---

## 5. 在 Heroku 上部署 Flask 应用


### 5.1 安装 Heroku CLI


下载并安装 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)。


### 5.2 创建 Procfile


在项目根目录下创建一个 Procfile 文件，指定应用的启动命令。


Procfile 文件内容：


```
web: gunicorn app:app
```


### 5.3 部署到 Heroku


```
heroku create
git add .
git commit -m "Initial commit"
git push heroku main
```


### 5.4 访问应用


Heroku 会提供一个 URL，你可以通过该 URL 访问你的应用。


---

## 6. 在 Docker 中部署 Flask 应用


### 6.1 创建 Dockerfile


Dockerfile 文件内容：


```
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```


### 6.2 创建 requirements.txt


列出应用的依赖包，requirements.txt 文件内容：


```
gunicorn
```


### 6.3 构建和运行 Docker 镜像


```
docker build -t my-flask-app .
docker run -p 8000:8000 my-flask-app
```









	  AI 思考中...





			** [Flask 中间件和扩展](https://www.runoob.com/flask-middleware.html)














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