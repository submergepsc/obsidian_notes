# Django 安装

- Source: https://www.runoob.com/django/django-install.html

在安装 Django 前，系统需要已经安装了 Python 的开发环境。


如果你还没有安装 Python，请先从 Python 官网 [https://www.python.org/](https://www.python.org/) 下载并安装最新版本的 Python。


Django 安装也很简单使包管理工具 pip 就可以了：


```
pip install Django
```


安装完成后，你可以通过运行以下命令验证 Django 是否成功安装：


```
python3 -m django --version
```


如果一切顺利，你将看到安装的 Django 版本号，如：**4.2.7**。


开发环境推荐：


- 1、[VS Code 开发工具](https://www.runoob.com/../vscode/vscode-tutorial.html)
- 2、[PyCharm 开发工具](https://www.runoob.com/../pycharm/pycharm-tutorial.html)
- 3、[阿里 Qoder](https://qoder.com/)
- 4、[Trae 开发工具](https://www.trae.com.cn/?utm_source=advertising&utm_medium=runoob_ug_cpa&utm_term=hw_trae_runoob)


---


## Windows 下安装 Django

接下来我们来具体看下不同系统下 Django 的安装。


如果你还未安装Python环境需要先下载Python安装包。


1、Python 下载地址：[https://www.python.org/downloads/](https://www.python.org/downloads/)


2、Django 下载地址：[https://www.djangoproject.com/download/](https://www.djangoproject.com/download/)


**注意：**目前 Django 1.6.x 以上版本已经完全兼容 Python 3.x。


### Python 安装(已安装的可跳过)


安装 Python 你只需要下载 python-x.x.x.msi 文件，然后一直点击 "Next" 按钮即可。

![](https://www.runoob.com/wp-content/uploads/2015/01/install1.png)


安装完成后你需要设置 Python 环境变量。 右击计算机->属性->高级->环境变量->修改系统变量 path，添加 Python 安装地址，本文实例使用的是 C:\Python33，你需要根据你实际情况来安装。


![](https://www.runoob.com/wp-content/uploads/2015/01/install2.png)


### Django 安装


下载 Django 压缩包，解压并和 Python安装目录放在同一个根目录，进入 Django 目录，执行 python setup.py install，然后开始安装，Django 将要被安装到 Python 的 Lib下site-packages。


![](https://www.runoob.com/wp-content/uploads/2015/01/install3.jpg)


然后是配置环境变量，将这几个目录添加到系统环境变量中： C:\Python33\Lib\site-packages\django;C:\Python33\Scripts。 添加完成后就可以使用Django的django-admin.py命令新建工程了。

![](https://www.runoob.com/wp-content/uploads/2015/01/install4.jpg)


---


## 检查是否安装成功


输入以下命令进行检查:


```
>>> import django
>>> django.get_version()
```


![](https://www.runoob.com/wp-content/uploads/2015/01/install5.jpg)


如果输出了Django的版本号说明安装正确。


---


## Linux 上安装 Django


### yum 安装方法


以下安装位于 Centos Linux 环境下安装，如果是你的 Linux 系统是 ubuntu 请使用 apt-get 命令。


默认情况下 Linux 环境已经支持了Python。你可以在终端输入Python命令来查看是否已经安装。


```
Python 3.7.4 (default, Aug  1 2012, 05:14:39)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```


### 安装 setuptools


命令：


```
# Python3 安装
yum install python3-setuptools
# Python2 安装
yum install python2-setuptools
```


完成之后，就可以使用 easy_install 命令安装 django


```
easy_install django
```
 之后我们在 Python 解释器输入以下代码：


```
[root@solar django]# python
Python 3.7.4 (default, May 15 2014, 14:49:08)
[GCC 4.8.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.VERSION
(3, 0, 6, 'final', 0)
```


我们可以看到输出了Django的版本号，说明安装成功。


### pip 命令安装方法


如果你还未安装 pip 工具，可查看：[Python pip 安装与使用](https://www.runoob.com/w3cnote/python-pip-install-usage.html)。


```
sudo pip3 install Django -i https://pypi.tuna.tsinghua.edu.cn/simple
```


**-i https://pypi.tuna.tsinghua.edu.cn/simple** 指定清华镜像源，下载速度更快。


指定 Django 的下载版本（3.0.6 可以改成你要的版本）：


```
sudo pip3 install Django==3.0.6 -i https://pypi.tuna.tsinghua.edu.cn/simple
```


如果 pip







	  AI 思考中...





			** [Django 教程](https://www.runoob.com/django-tutorial.html)
			[Django 创建第一个项目](https://www.runoob.com/django-first-app.html) **