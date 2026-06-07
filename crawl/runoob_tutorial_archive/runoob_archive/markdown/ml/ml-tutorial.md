# 机器学习教程

- Source: https://www.runoob.com/ml/ml-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2024/12/Machine-learning-logo-1.webp)

机器学习（Machine Learning）是人工智能（AI）的一个分支，它使计算机系统能够利用数据和算法自动学习和改进其性能。

机器学习是让机器通过经验（数据）来做决策和预测。

机器学习已经广泛应用于许多领域，包括推荐系统、图像识别、语音识别、金融分析等。


举个例子，通过机器学习，汽车可以学习如何识别交通标志、行人和障碍物，以实现自动驾驶。


---


## 机器学习与传统编程的区别


| 传统编程 | 机器学习 |
| --- | --- |
| 程序员编写明确的规则 | 计算机从数据中学习规则 |
| 适用于问题明确、规则清晰的情况 | 适用于复杂、规则难以明确的情况 |
| 例子：编写计算器程序 | 例子：编写识别垃圾邮件的程序 |


![](https://www.runoob.com/wp-content/uploads/2024/12/be8eeeae-fa30-4fb1-9761-0e08973aa970.png)


---


## 机器学习的三大要素


机器学习包含三个基本要素：


### 1. 数据


数据是机器学习的燃料，质量越高、数量越多的数据，通常能让模型学得越好。


- **训练数据**：用来教模型的数据
- **测试数据**：用来检验模型学习效果的数据
- **真实数据**：模型在实际应用中遇到的新数据


### 2. 算法


算法是机器学习的学习方法，不同的算法适用于不同类型的问题。


- **监督学习**：有标准答案的学习
- **无监督学习**：没有标准答案，自己找规律
- **强化学习**：通过试错和奖励来学习


### 3. 模型


模型是学习的结果，就像学生学到的知识一样。


- **训练过程**：算法从数据中学习规律
- **推理过程**：使用学到的规律做预测


---


## 实例


接下来我们通过一个简单的例子来理解机器学习的基本流程。

我们将使用 Python 创建一个简单的线性回归模型来预测房价。


## 实例


```
# 导入需要的库
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

# 设置图表风格，让图表更好看
sns.set_style("whitegrid")
# -------------------------- 设置中文字体 start --------------------------
plt.rcParams['font.sans-serif'] = [
    # Windows 优先
    'SimHei', 'Microsoft YaHei',
    # macOS 优先
    'PingFang SC', 'Heiti TC',
    # Linux 优先
    'WenQuanYi Micro Hei', 'DejaVu Sans'
]
# 修复负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
# -------------------------- 设置中文字体 end --------------------------

# 1. 准备数据
# 假设我们有房屋面积和对应的价格数据
# 房屋面积（平方米）
house_sizes = np.array([50, 60, 70, 80, 90, 100, 110, 120]).reshape(-1, 1)
# 房屋价格（万元）
house_prices = np.array([150, 180, 210, 240, 270, 300, 330, 360])

# 2. 创建并训练模型
# 创建线性回归模型
model = LinearRegression()
# 用数据训练模型（学习面积和价格之间的关系）
model.fit(house_sizes, house_prices)

# 3. 使用模型进行预测
# 预测 85 平方米的房屋价格
predicted_price = model.predict([[85]])
print(f"85 平方米的房屋预测价格：{predicted_price[0]:.2f} 万元")

# 4. 可视化结果
plt.scatter(house_sizes, house_prices, color='blue', label='实际数据')
plt.plot(house_sizes, model.predict(house_sizes), color='red', label='预测线')
plt.scatter([85], predicted_price, color='green', s=100, label='预测点')
plt.xlabel('房屋面积（平方米）')
plt.ylabel('房屋价格（万元）')
plt.title('RUNOOB 机器学习测试 -- 房屋面积与价格关系')
plt.legend()
plt.grid(True)
plt.show()
```


**运行结果：**


```
85 平方米的房屋预测价格：255.00 万元
```


这个例子展示了机器学习的基本流程：


- 准备数据（房屋面积和价格）
- 选择算法（线性回归）
- 训练模型（让计算机学习面积和价格的关系）
- 使用模型预测（预测新面积的价格）


输出的图如下：


![](https://www.runoob.com/wp-content/uploads/2024/12/a9b85f4b-ea0c-455f-8036-9d36ae0b512f.png)









	  AI 思考中...






			[机器学习简介](https://www.runoob.com/ml-intro.html) **













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