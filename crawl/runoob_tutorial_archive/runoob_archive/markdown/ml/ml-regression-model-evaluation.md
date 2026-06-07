# 回归模型评估

- Source: https://www.runoob.com/ml/ml-regression-model-evaluation.html

在机器学习的世界里，构建一个模型只是第一步，就像我们烤好了一个蛋糕，必须尝一尝才能知道它是否成功。对于回归模型（一种用于预测连续数值的模型，比如预测房价、气温或销售额），**模型评估**就是我们的**品尝**环节。它告诉我们模型预测得有多准，哪里做得好，哪里还有改进空间。


本文将带你系统学习回归模型的评估方法，从核心概念到具体指标，再到代码实践，让你不仅能看懂评估报告，更能亲手为你的模型"打分"。


---


## 回归模型与评估的核心概念


在深入指标之前，我们需要理解几个基础概念，它们是所有评估方法的基石。


### 什么是回归问题？


回归问题是监督学习的一种，其目标是基于输入特征预测一个**连续的数值**。


- **例子**：根据房屋的面积、房龄、地理位置（特征）来预测其售价（连续的数值）。


### 为什么需要评估？


- **模型选择**：比较不同算法（如线性回归、决策树回归）哪个在你的数据上表现更好。
- **参数调优**：调整模型参数（如正则化强度）时，需要一个客观标准来判断调整是否有效。
- **性能确认**：确保模型在未知数据上也有可靠的预测能力，避免"纸上谈兵"。


### 关键术语：误差


所有评估指标都围绕着"误差"展开。误差是模型预测值（ŷ）与真实值（y）之间的差异。


- **单个点的误差**：`误差 = y - ŷ`
- 评估的本质，就是**用不同的方式汇总和分析这些误差**。


---


## 核心评估指标详解


我们将介绍最常用、最重要的几个评估指标，并用一个简单的例子贯穿始终。


**假设我们预测了5个房子的价格：**


| 真实价格（y） | 预测价格（ŷ） | 误差（y - ŷ） |
| --- | --- | --- |
| 200 | 210 | -10 |
| 150 | 145 | 5 |
| 300 | 310 | -10 |
| 400 | 380 | 20 |
| 250 | 255 | -5 |


### 1. 平均绝对误差（MAE）


**通俗理解**：把所有预测"误差"的绝对值加起来，然后算个平均数。它直接反映了"平均来看，预测值大概偏离真实值多少单位"。


**计算公式**： `MAE = (1/n) * Σ|y_i - ŷ_i|` 其中 `n` 是样本数量，`Σ` 是求和符号。


**计算示例**： `MAE = (|-10| + |5| + |-10| + |20| + |-5|) / 5 = (10+5+10+20+5)/5 = 50/5 = 10`


**解读**：平均来说，我们的房价预测偏离真实价格 **10万元**。


**特点**：


- **优点**：直观易懂，不受极端误差值（异常值）的过度影响。
- **缺点**：绝对值函数在数学上不是处处可导，这在某些优化场景中不太方便。


### 2. 均方误差（MSE）


**通俗理解**：先把每个误差"平方"一下（让负号消失并放大误差），然后求平均值。它对**大的误差非常敏感**。


**计算公式**： `MSE = (1/n) * Σ(y_i - ŷ_i)^2`


**计算示例**： `MSE = [(-10)^2 + (5)^2 + (-10)^2 + (20)^2 + (-5)^2] / 5 = (100+25+100+400+25)/5 = 650/5 = 130`


**解读**：误差平方的平均值是130。这个数值本身没有直接的单位意义（是万元^2），但用于比较模型时非常有效。


**特点**：


- **优点**：数学性质优秀（处处可导），是许多模型（如线性回归）训练时最小化的目标函数。
- **缺点**：量纲与原始数据不同，数值大小不易解释；对异常值敏感。


### 3. 均方根误差（RMSE）


**通俗理解**：就是MSE的平方根。相当于把MSE"打回原形"，让它和真实值、预测值回到同一个量纲上。


**计算公式**： `RMSE = sqrt(MSE)`


**计算示例**： `RMSE = sqrt(130) ≈ 11.4`


**解读**：平均来看，我们的预测大约偏离真实值 **11.4万元**。这个解释和MAE（10万元）类似，但RMSE因为先平方再开方，会给予大误差更高的权重，所以通常比MAE大。


**特点**：


- **优点**：具有和原始数据相同的量纲，解释性比MSE强；对大误差惩罚更重，在重视大误差的场景（如金融风险预测）中很常用。
- **缺点**：同样对异常值敏感。


### 4. R² 分数（决定系数）


**通俗理解**：我的模型，比"瞎猜"（用平均值猜）强多少？它是一个**比例值**，衡量模型对数据变化的解释能力。


**计算公式**： `R² = 1 - (Σ(y_i - ŷ_i)^2 / Σ(y_i - y_mean)^2)` 其中 `y_mean` 是真实值的平均值。


**"瞎猜"模型**：对于任何房子，我都预测房价的平均值（`y_mean`）。


- 计算得到 `y_mean = (200+150+300+400+250)/5 = 260`
- "瞎猜"模型的误差平方和：`Σ(y_i - 260)^2 = 1600+12100+1600+19600+100 = 35000`


**计算示例**： `R² = 1 - (650 / 35000) = 1 - 0.01857 ≈ 0.9814`


**解读**：我们的模型能够解释目标变量（房价）**98.14%** 的波动。这表示模型拟合得非常好。


**特点**：


- **范围**：理论上，R² 的范围是 `(-∞, 1]`。 `R² = 1`：完美预测。
- `R² = 0`：模型和直接用平均值预测的效果一样。
- `R²
**优点**：无量纲，易于比较不同数据集上的模型性能。
**缺点**：随着模型特征增加，R² 会自然增大，即使增加的特征没有用，这可能导致过拟合。


---


## 指标对比与如何选择


为了更清晰地理解，我们用一个表格来总结：


| 指标 | 计算公式（简） | 量纲 | 对异常值 | 特点与适用场景 |
| --- | --- | --- | --- | --- |
| MAE | 平均绝对误差 | 与y相同 | 不敏感 | 解释最直观。关注"平均偏差多大"，适用于所有回归场景，尤其是异常值较多的数据。 |
| MSE | 平均平方误差 | y的平方 | 非常敏感 | 数学性质好。是模型训练的常用损失函数。数值本身不易解释。 |
| RMSE | MSE的平方根 | 与y相同 | 非常敏感 | 最常用。兼具MSE的数学优点和可解释性。对大误差惩罚重，在金融、预测等领域很受欢迎。 |
| R² | 1 - (模型误差/基线误差) | 无量纲 | 敏感 | 相对性能指标。用于比较模型相对于简单基准的提升程度。易于跨数据集比较。 |


**选择建议**：


- **首选报告 RMSE 和 R²**：RMSE 给出误差的实际大小，R² 给出模型的相对性能。这是最通用的组合。
- **当数据中有许多异常值时，关注 MAE**。
- **在模型训练和优化阶段，使用 MSE 作为损失函数**。
- **永远不要只看一个指标**！结合多个指标才能全面评估模型。


---


## 代码实践：使用 Scikit-learn 进行评估


现在，让我们用 Python 和机器学习库 Scikit-learn 来实际演练一遍。


### 环境准备


确保已安装必要的库：


## 实例


```
pip install numpy scikit-learn matplotlib
```


### 完整示例代码


## 实例


```
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. 创建模拟数据
np.random.seed(42) # 确保每次运行结果一致
X = 2 * np.random.rand(100, 1) # 100个样本，1个特征，范围[0,2)
y = 4 + 3 * X + np.random.randn(100, 1) # 真实关系：y = 4 + 3x + 噪声

# 2. 划分训练集和测试集（80%训练，20%测试）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 训练一个简单的线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 4. 在测试集上进行预测
y_pred = model.predict(X_test)

# 5. 计算所有评估指标
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse) # 或者用 mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

# 6. 打印评估结果
print("=== 回归模型评估报告 ===")
print(f"平均绝对误差 (MAE): {mae:.4f}")
print(f"均方误差 (MSE): {mse:.4f}")
print(f"均方根误差 (RMSE): {rmse:.4f}")
print(f"决定系数 (R² Score): {r2:.4f}")
print("\n模型系数：")
print(f"   截距 (Intercept): {model.intercept_[0]:.4f}")
print(f"   斜率 (Coefficient for X): {model.coef_[0][0]:.4f}")

# 7. 可视化结果
plt.figure(figsize=(10, 5))

# 子图1：真实值 vs 预测值散点图
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, alpha=0.7, edgecolors='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='完美预测线')
plt.xlabel('真实值 (y_test)')
plt.ylabel('预测值 (y_pred)')
plt.title('真实值 vs 预测值')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# 子图2：误差分布直方图
plt.subplot(1, 2, 2)
errors = y_test.flatten() - y_pred.flatten()
plt.hist(errors, bins=15, edgecolor='black', alpha=0.7)
plt.axvline(x=0, color='r', linestyle='--', label='零误差线')
plt.xlabel('预测误差')
plt.ylabel('频次')
plt.title('预测误差分布')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7, axis='y')

plt.tight_layout()
plt.show()
```


### 代码逐行解析


- **创建数据**：我们模拟了 `y = 4 + 3x + 噪声` 的数据，这是典型的线性关系加随机扰动。
- **划分数据集**：`train_test_split` 将数据随机分成两部分。用训练集 (`X_train`, `y_train`) 来学习模型，用从未见过的测试集 (`X_test`, `y_test`) 来评估其泛化能力。这是评估的关键一步！
- **训练模型**：创建 `LinearRegression` 对象并调用 `.fit()` 方法进行训练。
- **进行预测**：调用 `.predict()` 方法对测试集特征 `X_test` 生成预测值 `y_pred`。
- **计算指标**：使用 Scikit-learn 的 `metrics` 模块中的函数，轻松计算出 MAE, MSE, R²。RMSE 通过对 MSE 开方得到。
- **打印结果**：格式化输出所有指标和模型学到的参数。
- **可视化**： - **左图**：理想情况下，散点应紧密围绕红色虚线（完美预测线）分布。 - **右图**：误差分布直方图应大致以0为中心呈正态分布，这通常是一个好迹象。


---


## 实践练习与总结


### 动手练习


- **运行代码**：将上面的代码复制到你的 Python 环境中运行，观察输出结果和图。
- **修改数据**：尝试增大 `np.random.randn()` 中的噪声规模，重新运行。观察所有评估指标如何变化？图表有何不同？
- **更换模型**：尝试使用 `from sklearn.tree import DecisionTreeRegressor` 替换线性回归模型。比较两种模型的评估指标。
- **计算练习**：手动计算下面三个样本的 MAE, MSE, RMSE 和 R²。 - 真实值 y: [10, 20, 30] - 预测值 ŷ: [12, 18, 28]









	  AI 思考中...





			** [多项式回归](https://www.runoob.com/ml-multinomial-regression.html)
			[朴素贝叶斯](https://www.runoob.com/ml-naive-bayes.html) **













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