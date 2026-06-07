# TensorFlow 教程

- Source: https://www.runoob.com/tensorflow/tensorflow-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/06/TensorFlow_logo.svg.png)

TensorFlow 是一个**数学计算的工具箱**，专门为机器学习任务而设计，让开发者能够轻松地构建从简单线性回归到复杂神经网络的各种模型。


TensorFlow 是由 Google 开发的开源机器学习框架，用于构建和训练各种机器学习和深度学习模型。


TensorFlow 名字来源于其核心概念：**Tensor（张量）** 和 **Flow（流动）**，表示数据以张量的形式在计算图中流动。


---


## 阅读本教程前，您需要了解的知识：


学习本教程需要具备：**[Python](https://www.runoob.com/../python3/python3-basic-syntax.html) + 基础数学 + [机器学习](https://www.runoob.com/../ml/ml-tutorial.html)概念**。



#### (1) 数学基础


- **线性代数**：矩阵运算、向量空间（如张量操作）。
- **概率与统计**：概率分布、贝叶斯定理（理解损失函数、评估指标）。
- **微积分**：梯度、导数（理解反向传播和优化算法）。


#### (2) 编程基础


- **Python**：TensorFlow 主要使用 Python 接口，需熟悉语法、函数、面向对象编程。
- 基础算法：如循环、递归、数据结构（列表、字典）。


#### (3) 机器学习基础


- 了解监督学习、无监督学习的基本概念（如分类、回归、聚类）。
- 熟悉经典算法（如线性回归、神经网络）。
- 理解模型评估方法（如准确率、交叉验证）。


#### (4) 工具基础（可选但建议）


- **[NumPy](https://www.runoob.com/../numpy/numpy-tutorial.html)/[Pandas](https://www.runoob.com/../pandas/pandas-tutorial.html)**：用于数据预处理。
- **[Matplotlib](https://www.runoob.com/../matplotlib/matplotlib-tutorial.html)/[Seaborn](https://www.runoob.com/../matplotlib/seaborn-tutorial.html)**：用于数据可视化。
- **[Scikit-learn](https://www.runoob.com/../sklearn/sklearn-tutorial.html)**：对比传统机器学习方法。

---


## 适合学习 TensorFlow 的人群

- **AI/ML 研究者**：需要实现和优化深度学习模型。
- **数据科学家**：希望用深度学习处理复杂数据（如图像、文本、语音等）。
- **软件工程师**：想将 AI 模型部署到生产环境（如移动端、云端）。
- **学生/爱好者**：对 AI 感兴趣，希望掌握前沿技术。
- **硬件/算法工程师**：涉及 AI 加速、模型优化或自定义算子开发。


---


## 相关资料


- TensorFlow 官网：[https://www.tensorflow.org/](https://www.tensorflow.org/)
- TensorFlow 学习：[https://www.tensorflow.org/learn?hl=zh-cn](https://www.tensorflow.org/learn?hl=zh-cn)
- TensorFlow Github：[https://github.com/tensorflow](https://github.com/tensorflow)










	  AI 思考中...






			[TensorFlow 简介](https://www.runoob.com/tensorflow-intro.html) **













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