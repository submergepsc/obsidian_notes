# 线性回归 (Linear Regression)

- Source: https://www.runoob.com/ml/ml-linear-regression.html

线性回归（Linear Regression）是机器学习中最基础且广泛应用的算法之一。


线性回归 (Linear Regression) 是一种用于预测连续值的最基本的机器学习算法，它假设目标变量 **y** 和特征变量 **x** 之间存在线性关系，并试图找到一条最佳拟合直线来描述这种关系。


```
y = w * x + b
```


其中：


- `y` 是预测值
- `x` 是特征变量
- `w` 是权重 (斜率)
- `b` 是偏置 (截距)


线性回归的目标是找到最佳的 `w` 和 `b`，使得预测值 `y` 与真实值之间的误差最小。常用的误差函数是均方误差 (MSE)：


```
MSE = 1/n * Σ(y_i - y_pred_i)^2
```


其中：


- y_i 是实际值。
- y_pred_i 是预测值。
- n 是数据点的数量。


我们的目标是通过调整 w 和 b ，使得 MSE 最小化。


## 如何求解线性回归？


### 1、最小二乘法


最小二乘法是一种常用的求解线性回归的方法，它通过求解以下方程来找到最佳的 ( w ) 和 ( b )。


最小二乘法的目标是最小化残差平方和（RSS），其公式为：


\[ \text{RSS} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 \]


其中：


- `\( y_i \)` 是实际值。
- `\( \hat{y}_i \)` 是预测值，由线性回归模型 `\( \hat{y}_i = w x_i + b \)` 计算得到。


通过最小化 RSS，可以得到以下正规方程：


\[ \begin{cases} w \sum_{i=1}^n x_i^2 + b \sum_{i=1}^n x_i = \sum_{i=1}^n x_i y_i \\ w \sum_{i=1}^n x_i + b n = \sum_{i=1}^n y_i \end{cases} \]


### 矩阵形式


将正规方程写成矩阵形式：


\[ \begin{bmatrix} \sum_{i=1}^n x_i^2 & \sum_{i=1}^n x_i \\ \sum_{i=1}^n x_i & n \end{bmatrix} \begin{bmatrix} w \\ b \end{bmatrix} = \begin{bmatrix} \sum_{i=1}^n x_i y_i \\ \sum_{i=1}^n y_i \end{bmatrix} \]


### 求解方法


通过求解上述矩阵方程，可以得到最佳的 `\( w \)` 和 `\( b \)`：


\[ \begin{bmatrix} w \\ b \end{bmatrix} = \begin{bmatrix} \sum_{i=1}^n x_i^2 & \sum_{i=1}^n x_i \\ \sum_{i=1}^n x_i & n \end{bmatrix}^{-1} \begin{bmatrix} \sum_{i=1}^n x_i y_i \\ \sum_{i=1}^n y_i \end{bmatrix} \]


### 2、梯度下降法


梯度下降法的目标是最小化损失函数 `\( J(w, b) \) ` 。对于线性回归问题，通常使用均方误差（MSE）作为损失函数：


\[ J(w, b) = \frac{1}{2m} \sum_{i=1}^m (y_i - \hat{y}_i)^2 \]


其中：


- `\( m \)` 是样本数量。
- `\( y_i \)` 是实际值。
- `\( \hat{y}_i \)` 是预测值，由线性回归模型 `\( \hat{y}_i = w x_i + b \)` 计算得到。


梯度是损失函数对参数的偏导数，表示损失函数在参数空间中的变化方向。对于线性回归，梯度计算如下：


\[ \frac{\partial J}{\partial w} = -\frac{1}{m} \sum_{i=1}^m x_i (y_i - \hat{y}_i) \]


\[ \frac{\partial J}{\partial b} = -\frac{1}{m} \sum_{i=1}^m (y_i - \hat{y}_i) \]


### 参数更新规则


梯度下降法通过以下规则更新参数 `\( w \)` 和 `\( b \)`：


\[ w := w - \alpha \frac{\partial J}{\partial w} \]


\[ b := b - \alpha \frac{\partial J}{\partial b} \]


其中：


- `\( \alpha \)` 是学习率（learning rate），控制每次更新的步长。


### 梯度下降法的步骤


- **初始化参数**：初始化 `\( w \)` 和 `\( b \)` 的值（通常设为 0 或随机值）。
- **计算损失函数**：计算当前参数下的损失函数值 `\( J(w, b) \)`。
- **计算梯度**：计算损失函数对 `\( w \)` 和 `\( b \)` 的偏导数。
- **更新参数**：根据梯度更新 `\( w \)` 和 `\( b \)`。
- **重复迭代**：重复步骤 2 到 4，直到损失函数收敛或达到最大迭代次数。


## 使用 Python 实现线性回归


下面我们通过一个简单的例子来演示如何使用 Python 实现线性回归。


### 1、导入必要的库


## 实例


```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
```


### 2、生成模拟数据


## 实例


```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 生成一些随机数据
np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# 可视化数据
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Generated Data From Runoob')
plt.show()
```


显示如下所示：


![](https://www.runoob.com/wp-content/uploads/2025/01/ml-linear-regression-1.png)


### 3、使用 Scikit-learn 进行线性回归


## 实例


```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 生成一些随机数据
np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(x, y)

# 输出模型的参数
print(f"斜率 (w): {model.coef_[0][0]}")
print(f"截距 (b): {model.intercept_[0]}")

# 预测
y_pred = model.predict(x)

# 可视化拟合结果
plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.show()
```


输出结果：


```
斜率 (w): 2.968467510701019
截距 (b): 4.222151077447231
```


显示如下所示：


![](https://www.runoob.com/wp-content/uploads/2025/01/ml-linear-regression-2.png)


我们可以使用 `score()` 方法来评估模型性能，返回 R^2 值。


## 实例


```
import numpy as np
from sklearn.linear_model import LinearRegression

# 生成一些随机数据
np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(x, y)
# 计算模型得分
score = model.score(x, y)
print("模型得分:", score)
```


输出结果为：


```
模型得分: 0.7469629925504755
```


### 4、手动实现梯度下降法


## 实例


```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 生成一些随机数据
np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# 初始化参数
w = 0
b = 0
learning_rate = 0.1
n_iterations = 1000

# 梯度下降
for i in range(n_iterations):
    y_pred = w * x + b
    dw = -(2/len(x)) * np.sum(x * (y - y_pred))
    db = -(2/len(x)) * np.sum(y - y_pred)
    w = w - learning_rate * dw
    b = b - learning_rate * db

# 输出最终参数
print(f"手动实现的斜率 (w): {w}")
print(f"手动实现的截距 (b): {b}")

# 可视化手动实现的拟合结果
y_pred_manual = w * x + b
plt.scatter(x, y)
plt.plot(x, y_pred_manual, color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Manual Gradient Descent Fit')
plt.show()
```


输出结果：


```
手动实现的斜率 (w): 2.968467510701028
手动实现的截距 (b): 4.222151077447219
```


显示如下所示：


![](https://www.runoob.com/wp-content/uploads/2025/01/ml-linear-regression-3.png)










	  AI 思考中...





			** [机器学习算法](https://www.runoob.com/ml-algorithms.html)
			[逻辑回归（Logistic Regression）](https://www.runoob.com/ml-logistic-regression.html) **













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