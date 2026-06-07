# Sklearn 安装

- Source: https://www.runoob.com/sklearn/sklearn-install.html

要学习 Sklearn，安装是第一步，由于 Sklearn 依赖于其他几个库（如 NumPy、SciPy 和 matplotlib），所以我们需要确保这些依赖库也已安装。


系统环境要求：


- **Python 版本**：scikit-learn 支持 Python 3.7 及以上版本。
- **操作系统**：scikit-learn 可以在 Windows、macOS 和 Linux 等主流操作系统上运行。
- **包管理工具**：你可以使用 `pip` 或 `conda` 来安装 scikit-learn。


本章节我们使用 pip 安装 scikit-learn。


安装前，确保已安装 Python 和 pip。


** 检查 Python 是否安装：**


```
python --version
```


检查 pip 是否安装：


```
pip --version
```


如果未安装 python 和 pip，可以参考我们的： [Python 安装](https://www.runoob.com/../python3/python3-install.html) 与 [Pip 安装](https://www.runoob.com/../python3/python3-pip.html)。


**

注意：**目前最新的 Python 版本已经预装了 pip。


**注意：**Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具。


---


## 安装 Sklearn

**Sklearn 全称为 scikit-learn。**


使用 pip 安装最新版本的 scikit-learn：


```
pip install scikit-learn
```


如果你希望安装特定版本的 scikit-learn，可以指定版本号：


```
pip install scikit-learn==1.2.0
```


### 检查安装是否成功

安装完成后，我们可以通过以下代码检查 scikit-learn 是否安装成功：


## 实例


```python
import sklearn
print(sklearn.__version__)
```


如果成功显示 scikit-learn 的版本号，类似如下，则表示安装成功：


```
1.5.2
```


## 使用 conda 安装 scikit-learn

如果你使用的是 Anaconda 环境，推荐使用 conda 来安装 scikit-learn。


Anaconda 是一个用于科学计算的 Python 发行版，内置了许多数据科学和机器学习的库，方便开发者使用。

如果你还不了解 Anaconda，可以参考：[Anaconda 教程](https://www.runoob.com/../python-qt/anaconda-tutorial.html)。


### 创建一个新的 conda 环境（可选）

你可以选择为 scikit-learn 创建一个新的虚拟环境，以避免与其他项目发生冲突：


```
conda create -n sklearn-env python=3.9
conda activate sklearn-env
```


### 安装 scikit-learn

使用 conda 安装 scikit-learn：


```
conda install scikit-learn
```


如果你想安装特定版本，可以指定版本号：


```
conda install scikit-learn=1.2.0
```


### 验证安装

在 conda 环境中，你可以通过 Python shell 或 Jupyter Notebook 来验证安装：


## 实例


```python
import sklearn
print(sklearn.__version__)
```


如果成功显示 scikit-learn 的版本号，类似如下，则表示安装成功：


```
1.5.2
```


---


## 安装其他依赖

scikit-learn 依赖于一些其他库，特别是：

- **NumPy**：用于处理数组和数值计算
- **SciPy**：提供更高级的数学计算工具
- **matplotlib**（可选）：用于数据可视化
- **joblib**（可选）：用于模型的持久化（保存和加载）


如果你使用 pip 安装，scikit-learn 会自动安装这些依赖，但如果你想手动安装或更新它们，可以使用以下命令：


```
pip install numpy scipy matplotlib joblib
```


使用 conda 安装，则所有的依赖库会自动安装。










	  AI 思考中...





			** [Sklearn 简介](https://www.runoob.com/sklearn-intro.html)
			[Sklearn 基础概念](https://www.runoob.com/sklearn-basics.html) **













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