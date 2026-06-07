# 决策树（Decision Tree）

- Source: https://www.runoob.com/ml/ml-decision-tree.html

决策树（Decision Tree）是一种常用的机器学习算法，广泛应用于分类和回归问题。


决策树通过树状结构来表示决策过程，每个内部节点代表一个特征或属性的测试，每个分支代表测试的结果，每个叶节点代表一个类别或值。


### 决策树的基本概念


- **节点（Node）**：树中的每个点称为节点。根节点是树的起点，内部节点是决策点，叶节点是最终的决策结果。
- **分支（Branch）**：从一个节点到另一个节点的路径称为分支。
- **分裂（Split）**：根据某个特征将数据集分成多个子集的过程。
- **纯度（Purity）**：衡量一个子集中样本的类别是否一致。纯度越高，说明子集中的样本越相似。


### 决策树的工作原理


决策树通过递归地将数据集分割成更小的子集来构建树结构。具体步骤如下：


- **选择最佳特征**：根据某种标准（如信息增益、基尼指数等）选择最佳特征进行分割。
- **分割数据集**：根据选定的特征将数据集分成多个子集。
- **递归构建子树**：对每个子集重复上述过程，直到满足停止条件（如所有样本属于同一类别、达到最大深度等）。
- **生成叶节点**：当满足停止条件时，生成叶节点并赋予类别或值。


### 决策树的构建标准


在构建决策树时，我们需要选择最佳特征进行分割，常用的标准有：


**1. 信息增益（Information Gain）**


用于分类问题，衡量选择某一特征后数据集的纯度提升。计算公式为：


![](https://www.runoob.com/wp-content/uploads/2025/01/b891fa79-647b-4dfa-b0a2-4a763062a998.png)


其中 **Entropy** 是数据集的熵，用来衡量数据的不确定性。


**2. 基尼指数（Gini Index）**


也是用于分类问题的分裂标准，计算公式为：


![](https://www.runoob.com/wp-content/uploads/2025/01/2115f0bc-cc83-422a-8a7d-a3ae2753b990.png)


其中 pi 是类别 i 的样本占比。基尼指数越小，表示数据集越纯净。


**3. 均方误差（MSE）**

用于回归问题，衡量预测值和真实值的差异。

MSE 越小，表示回归树的预测效果越好。


---

## 决策树的优缺点


### 优点


- **易于理解和解释**：决策树的结构直观，易于理解和解释。
- **处理多种数据类型**：可以处理数值型和类别型数据。
- **不需要数据标准化**：决策树不需要对数据进行标准化或归一化处理。


### 缺点


- **容易过拟合**：决策树容易过拟合，特别是在数据集较小或树深度较大时。
- **对噪声敏感**：决策树对噪声数据较为敏感，可能导致模型性能下降。
- **不稳定**：数据的小变化可能导致生成完全不同的树。

---


## 使用Python实现决策树


接下来，我们将使用Python的`scikit-learn`库来实现一个简单的决策树分类器。


### 1. 安装必要的库


首先，确保你已经安装了`scikit-learn`库。如果没有安装，可以使用以下命令进行安装：


```
pip install scikit-learn
```


### 2. 导入库并加载数据集


我们将使用`scikit-learn`自带的鸢尾花（Iris）数据集来演示决策树的使用。


## 实例


```
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data
y = iris.target

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```


### 3. 训练决策树模型


接下来，我们使用`DecisionTreeClassifier`来训练决策树模型。


## 实例


```
# 创建决策树分类器
clf = DecisionTreeClassifier()

# 训练模型
clf.fit(X_train, y_train)
```


### 4. 预测与评估


使用训练好的模型对测试集进行预测，并评估模型的准确率。


## 实例


```
# 对测试集进行预测
y_pred = clf.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy:.2f}")
```


输出结果：


```
模型准确率: 1.00
```


### 5. 可视化决策树


为了更直观地理解决策树的结构，我们可以使用`graphviz`库来可视化决策树。


graphviz 下载地址：[https://graphviz.org/download/](https://graphviz.org/download/)


- Windows 平台可以下载适用于 Windows 的安装包（.msi 文件）。
- Linux 平台可以使用安装包的命令安装，如 **apt install graphviz**
- macOS 平台安装命令 **brew install graphviz**。


也可以源码安装，下载最新的源码包（.tar.gz 文件）。


```
tar -zxvf graphviz-<version>.tar.gz
cd graphviz-<version>
./configure
make
sudo make install
```


安装完成后，可以通过以下命令验证 Graphviz 是否安装成功：


```
dot -V
```


输出类似以下内容，说明安装成功：


```
dot - graphviz version 12.2.1 (20241206.2353)
```


安装 `graphviz` 库：


## 实例


```
pip install graphviz
```


然后，使用以下代码生成决策树的可视化图：


## 实例


```
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
import graphviz

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data
y = iris.target

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建决策树分类器
clf = DecisionTreeClassifier()

# 训练模型
clf.fit(X_train, y_train)

# 对测试集进行预测
y_pred = clf.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确率: {accuracy:.2f}")

# 导出决策树为dot文件
dot_data = export_graphviz(clf, out_file=None,
                           feature_names=iris.feature_names,
                           class_names=iris.target_names,
                           filled=True, rounded=True,
                           special_characters=True)

# 使用graphviz渲染决策树
graph = graphviz.Source(dot_data)
graph.render("iris_decision_tree")  # 保存为PDF文件
graph.view()  # 在浏览器中查看
```


执行以上代码，会生成一个 iris_decision_tree.pdf 文件，显示如下：


![](https://www.runoob.com/wp-content/uploads/2025/01/f01a4060-d9dc-4163-a287-fad50bfab846.png)









	  AI 思考中...





			** [逻辑回归（Logistic Regression）](https://www.runoob.com/ml-logistic-regression.html)
			[支持向量机](https://www.runoob.com/ml-svm.html) **













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