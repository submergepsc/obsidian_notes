# Anaconda 教程

- Source: https://www.runoob.com/python-qt/anaconda-tutorial.html

Python 量化可以直接使用 Anaconda 工具来提高效率，免去一些安装的烦恼。


Anaconda 是一个数据科学和机器学习的软件套装，它包含了许多工具和库，让您能够更轻松地进行编程、分析数据和构建机器学习模型。


Anaconda 包及其依赖项和环境的管理工具为 **conda** 命令，文章后面部分会详细介绍。


与传统的 **Python pip** 工具相比 Anaconda 的**conda** 可以更方便地在不同环境之间进行切换，环境管理较为简单。


### 为什么选择 Anaconda？


- **方便安装：** 安装 Anaconda 就像安装一个应用程序一样简单，它为您预先安装好了许多常用的工具，无需单独配置。
- **包管理器：** Anaconda 包含一个名为 Conda 的包管理器，用于安装、更新和管理软件包。Conda 不仅限于 Python，还支持多种其他语言的包管理。
- **环境管理：** 使用 Anaconda，您可以轻松地创建和管理多个独立的 Python 环境，比如可以安装 python2 和 python3 环境，然后实现自由切换。这对于在不同项目中使用不同的库和工具版本非常有用，以避免版本冲突。
- **集成工具和库：** Anaconda 捆绑了许多用于数据科学、机器学习和科学计算的重要工具和库，如 NumPy、Pandas、Matplotlib、SciPy、Scikit-learn 等。
- **Jupyter 笔记本：** Jupyter 是一个交互式的计算环境，支持多种编程语言，但在 Anaconda 中主要用于 Python。它允许用户创建和共享包含实时代码、方程式、可视化和叙述文本的文档。
- **Spyder 集成开发环境：** Anaconda 中集成了 Spyder，这是一个专为科学计算和数据分析而设计的开发环境，具有代码编辑、调试和数据可视化等功能。
- **跨平台性：** Anaconda 可在 Windows、macOS 和 Linux 等操作系统上运行，使其成为一个跨平台的解决方案。
- **社区支持：** Anaconda 拥有庞大的社区，用户可以在社区论坛上获取帮助、分享经验和解决问题。


---


## Anaconda 安装

Anaconda 安装包下载地址：[https://www.anaconda.com/download](https://www.anaconda.com/download)。


Anaconda 可在 Windows、macOS 和 Linux 等操作系统上运行，你可以根据不同平台下载安装包：


![](https://www.runoob.com/wp-content/uploads/2023/12/8fe5e0b2-08e6-4753-9feb-ccc9735476f6.png)

### macOS 平台


安装过程也很简单，双击打开下载的安装包，选择 **Install for me only**:


![](https://www.runoob.com/wp-content/uploads/2023/12/osx-install-destination1.png)


点击 **install** 按钮：

![](https://www.runoob.com/wp-content/uploads/2023/12/osx-install-type1.png)

安装完成后，点击 **Continue** 按钮，接下来就可以看到安装完成的界面：


![](https://www.runoob.com/wp-content/uploads/2023/12/osx-install-cloud-notebook1.png)


![](https://www.runoob.com/wp-content/uploads/2023/12/osx-install-success1.png)


macOS 平台安装可以参考官网：[https://docs.anaconda.com/free/anaconda/install/mac-os/](https://docs.anaconda.com/free/anaconda/install/mac-os/)


### Win 平台

Win 平台与 macOS 类似，在下载安装包后，双击安装包，同意一些协议，简单的就可以按默认设置一步步按 Next 按钮就可以。
选择安装目录：

![](https://www.runoob.com/wp-content/uploads/2023/12/win-install-destination1.png)


在 "Advanced Installation Options" 中不要勾选 "Add Anaconda to my PATH environment variable."（"添加Anaconda至我的环境变量。"），因为如果勾选，则将会影响其他程序的使用。


![](https://www.runoob.com/wp-content/uploads/2023/12/win-install-options1.png)


点击 Install 按钮进行安装，安装成功出现如下界面：


![](https://www.runoob.com/wp-content/uploads/2023/12/win-install-cloud-notebook1.png)


点击 **Next** 按钮：


![](https://www.runoob.com/wp-content/uploads/2023/12/win-install-complete1.png)


Win 平台安装可以参考官网：[https://docs.anaconda.com/free/anaconda/install/windows/](https://docs.anaconda.com/free/anaconda/install/windows/)


### Linux 平台


Linux 平台可以通过以下命令安装，可以替换安装的版本号：


```
curl -O https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
```


Linux 不同平台安装可以参考官网：[https://docs.anaconda.com/free/anaconda/install/linux/](https://docs.anaconda.com/free/anaconda/install/linux/)

---


## Anaconda 界面使用


安装完后我们就可以进入 Anaconda 管理界面查看并安装不同的环境：


![](https://www.runoob.com/wp-content/uploads/2023/12/a2f42776ebf2ebe7bffcadf4d715f6b7.png)


点击 **Evironments** 就可以查看已经安装的环境：


![](https://www.runoob.com/wp-content/uploads/2023/12/a2f42776ebf2ebe7bffcadf4d715f6b7.png)


底部还有创建与删除环境的按钮，我们可以自由操作：


![](https://www.runoob.com/wp-content/uploads/2023/12/3547f0d29abafdae5cd5f112f465bc72.png)

---


## conda 命令


除了界面操作，我们还可以在命令行使用 conda 来管理不同环境。


**conda** 是 Anaconda 发行版中的包管理器，用于安装、更新、卸载软件包，以及创建和管理不同的 Python 环境。

以下是一些常用的Conda命令及其简要介绍：


### 环境管理


**创建一个名为 "myenv" 的新环境:**


```
conda create --name myenv
```


**创建指定版本的环境**：


```
conda create --name myenv python=3.8
```


以上代码创建一个名为 "myenv" 的新环境，并指定 Python 版本为 3.8。


**激活环境：**


```
conda activate myenv
```


以上代码激活名为 "myenv" 的环境。


**要退出当前环境使用以下命令：**


```
deactivate
```


**查看所有环境：**


```
conda env list
```


以上代码查看所有已创建的环境。


**复制环境：**


```
conda create --name myclone --clone myenv
```


以上代码通过克隆已有环境创建新环境。


**删除环境：**


```
conda env remove --name myenv
```


以上代码删除名为 "myenv" 的环境。


### 包管理


**安装包：**


```
conda install package_name
```


以上代码安装名为 "package_name" 的软件包。


**安装指定版本的包：**


```
conda install package_name=1.2.3
```


以上代码安装 "package_name" 的指定版本。


**更新包：**


```
conda update package_name
```


以上代码更新已安装的软件包。


**卸载包：**


```
conda remove package_name
```


以上代码卸载已安装的软件包。


**查看已安装的包：**


```
conda list
```


查看当前环境下已安装的所有软件包及其版本。


### 其他常用命令


**查看帮助：**


```
conda --help
```


以上代码获取 conda 命令的帮助信息。


**查看 conda 版本：**


```
conda --version
```


以上代码查看安装的 conda 版本。


**搜索包：**


```
conda search package_name
```


以上代码在 conda 仓库中搜索指定的软件包。


**清理不再需要的包：**


```
conda clean --all
```


以上代码清理 conda 缓存，删除不再需要的软件包。


### Jupyter Notebook（可选）


**安装 Jupyter Notebook：**


```
conda install jupyter
```


以上代码安装 Jupyter Notebook。


**启动 Jupyter Notebook：**


```
jupyter notebook
```


以上代码在已激活的环境中启动 Jupyter Notebook。









	  AI 思考中...





			** [Python 量化金融库](https://www.runoob.com/qt-libs.html)
			[Python 量化回测](https://www.runoob.com/qt-cumulative.html) **













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