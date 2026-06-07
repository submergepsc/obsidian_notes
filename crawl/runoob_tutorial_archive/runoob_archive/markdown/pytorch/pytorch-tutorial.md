# PyTorch 教程

- Source: https://www.runoob.com/pytorch/pytorch-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2024/12/pytorch-e1576624094357.webp)

PyTorch 是一个开源的机器学习库，主要用于进行计算机视觉（CV）、自然语言处理（NLP）、语音识别等领域的研究和开发。


PyTorch由 Facebook 的人工智能研究团队开发，并在机器学习和深度学习社区中广泛使用。

PyTorch 以其灵活性和易用性而闻名，特别适合于深度学习研究和开发。


## 谁适合阅读本教程？


只要您具备编程的基础知识，您就可以阅读本教程，学习 PyTorch 适合对深度学习和机器学习感兴趣的人，包括数据科学家、工程师、研究人员和学生。


## 阅读本教程前，您需要了解的知识：


在您开始阅读本教程之前，您必须具备的基础知识包括 Python 编程、基础数学（线性代数、概率论、微积分）、机器学习的基本概念、神经网络知识，以及一定的英语阅读能力来查阅文档和资料。


- **编程基础**：熟悉至少一种编程语言，尤其是 [Python](https://www.runoob.com/../python3/python3-tutorial.html)，因为 PyTorch 主要是用 Python 编写的。
- **数学基础**：了解线性代数、概率论和统计学、微积分等基础数学知识，这些是理解和实现机器学习算法的基石。
- **机器学习基础**：了解机器学习的基本概念，如监督学习、无监督学习、强化学习、模型评估指标（准确率、召回率、F1分数等）。
- **深度学习基础**：熟悉神经网络的基本概念，包括前馈神经网络、卷积神经网络（CNN）、循环神经网络（RNN）、长短期记忆网络（LSTM）等。
- **计算机视觉和自然语言处理基础**：如果你打算在这些领域应用 PyTorch，了解相关的背景知识会很有帮助。
- **Linux/Unix 基础**：虽然不是必需的，但了解 Linux/Unix 操作系统的基础知识可以帮助你更有效地使用命令行工具和脚本，特别是在数据预处理和模型训练中。
- **英语阅读能力**：由于许多文档、教程和社区讨论都是用英语进行的，具备一定的英语阅读能力将有助于你更好地学习和解决问题。


## 实例


下面的是 PyTorch 中一些基本的张量操作：如何创建随机张量、进行逐元素运算、访问特定元素以及计算总和和最大值。


## 实例


```python
import torch

# 设置数据类型和设备
dtype = torch.float  # 张量数据类型为浮点型
device = torch.device("cpu")  # 本次计算在 CPU 上进行

# 创建并打印两个随机张量 a 和 b
a = torch.randn(2, 3, device=device, dtype=dtype)  # 创建一个 2x3 的随机张量
b = torch.randn(2, 3, device=device, dtype=dtype)  # 创建另一个 2x3 的随机张量

print("张量 a:")
print(a)

print("张量 b:")
print(b)

# 逐元素相乘并输出结果
print("a 和 b 的逐元素乘积:")
print(a * b)

# 输出张量 a 所有元素的总和
print("张量 a 所有元素的总和:")
print(a.sum())

# 输出张量 a 中第 2 行第 3 列的元素（注意索引从 0 开始）
print("张量 a 第 2 行第 3 列的元素:")
print(a[1, 2])

# 输出张量 a 中的最大值
print("张量 a 中的最大值:")
print(a.max())
```


**创建张量：**

- `torch.randn(2, 3)` 创建一个 2 行 3 列的张量，填充随机数（遵循正态分布）。
- `device=device` 和 `dtype=dtype` 分别指定了计算设备（CPU 或 GPU）和数据类型（浮点型）。


**张量操作：**

- `a * b`：逐元素相乘。
- `a.sum()`：计算张量 `a` 所有元素的和。
- `a[1, 2]`：访问张量 `a` 第 2 行第 3 列的元素（注意索引从 0 开始）。
- `a.max()`：获取张量 `a` 中的最大值。


输出：（每次运行时值会有所不同）


```
张量 a:
tensor([[-0.1460, -0.3490,  0.3705],
        [-1.1141,  0.7661,  1.0823]])

张量 b:
tensor([[ 0.6901, -0.9663,  0.3634],
        [-0.6538, -0.3728, -1.1323]])

a 和 b 的逐元素乘积:
tensor([[-0.1007,  0.3372,  0.1346],
        [ 0.7284, -0.2856, -1.2256]])

张量 a 所有元素的总和:
tensor(0.6097)

张量 a 第 2 行第 3 列的元素:
tensor(1.0823)

张量 a 中的最大值:
tensor(1.0823)
```


## 参考链接

PyTorch 官网 ：[https://pytorch.org/](https://pytorch.org/)


PyTorch 官方入门教程：[https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)


PyTorch 官方文档：[https://pytorch.org/docs/stable/index.html](https://pytorch.org/docs/stable/index.html)


PyTorch 源代码：[https://github.com/pytorch/pytorch](https://pytorch.org/docs/stable/index.html)








	  AI 思考中...






			[PyTorch 简介](https://www.runoob.com/pytorch-intro.html) **













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