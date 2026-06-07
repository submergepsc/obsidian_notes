# Keras 常用层类型

- Source: https://www.runoob.com/tensorflow/keras-layer.html

Keras 是一个高级神经网络 API，它提供了丰富的层类型来构建深度学习模型。

层（Layer）是 Keras 的基本构建块，每个层接收输入数据，进行特定变换后输出结果。

本文将详细介绍 Keras 中最常用的层类型及其使用方法。


---


## 核心层类型


### Dense 全连接层


全连接层是最基础的神经网络层，每个输入节点都与输出节点相连。


## 实例


```python
from keras.layers import Dense

# 创建一个具有64个神经元，使用ReLU激活函数的全连接层
dense_layer = Dense(units=64, activation='relu')
```


**参数说明**：


- `units`：正整数，输出空间的维度
- `activation`：激活函数，如 'relu', 'sigmoid', 'tanh', 'softmax' 等
- `use_bias`：布尔值，是否使用偏置向量（默认True）
- `kernel_initializer`：权重矩阵的初始化方法


**应用场景**：


- 用于多层感知机(MLP)
- 作为分类器的最后一层
- 特征变换和非线性映射


---


### Conv2D 二维卷积层


主要用于图像处理的卷积操作，能够提取局部特征。


## 实例


```python
from keras.layers import Conv2D

# 创建一个具有32个3x3卷积核的卷积层
conv_layer = Conv2D(filters=32, kernel_size=(3, 3), activation='relu')
```


**参数说明**：


- `filters`：整数，输出空间的维度（卷积核的数量）
- `kernel_size`：整数或元组，卷积窗口的宽和高
- `strides`：卷积步长，默认为(1, 1)
- `padding`：'valid'（不填充）或 'same'（填充使输出与输入尺寸相同）


**应用场景**：


- 图像分类
- 目标检测
- 图像分割


---


### LSTM 长短期记忆网络层


用于处理序列数据的循环神经网络层，能够学习长期依赖关系。


## 实例


```python
from keras.layers import LSTM

# 创建一个具有128个单元的LSTM层
lstm_layer = LSTM(units=128, return_sequences=True)
```


**参数说明**：


- `units`：正整数，输出空间的维度
- `return_sequences`：布尔值，是否返回完整序列（默认False）
- `dropout`：0到1之间的浮点数，输入线性变换的丢弃率
- `recurrent_dropout`：0到1之间的浮点数，循环状态的丢弃率


**应用场景**：


- 自然语言处理
- 时间序列预测
- 语音识别


---


### Dropout 随机失活层


在训练过程中随机将部分神经元输出设为0，防止过拟合。


## 实例


```python
from keras.layers import Dropout

# 创建一个丢弃率为0.5的Dropout层
dropout_layer = Dropout(rate=0.5)
```


**参数说明**：


- `rate`：0到1之间的浮点数，丢弃比例
- `noise_shape`：整数张量，表示将与输入相乘的二进制丢弃掩层的形状
- `seed`：随机数种子


**应用场景**：


- 防止神经网络过拟合
- 提高模型泛化能力
- 通常在全连接层后使用


---


## 其他重要层类型


### BatchNormalization 批量归一化层


对前一层的输出进行批量归一化，加速训练并提高模型稳定性。


## 实例


```python
from keras.layers import BatchNormalization

# 创建批量归一化层
bn_layer = BatchNormalization()
```


### MaxPooling2D 二维最大池化层


通过取窗口内的最大值来下采样特征图。


## 实例


```python
from keras.layers import MaxPooling2D

# 创建2x2的最大池化层
pool_layer = MaxPooling2D(pool_size=(2, 2))
```


### Flatten 展平层


将多维输入展平为一维，常用于从卷积层过渡到全连接层。


## 实例


```python
from keras.layers import Flatten

# 创建展平层
flatten_layer = Flatten()
```


### Embedding 嵌入层


将正整数（索引）转换为固定大小的密集向量。


## 实例


```python
from keras.layers import Embedding

# 创建嵌入层，词汇表大小为1000，输出维度为64
embedding_layer = Embedding(input_dim=1000, output_dim=64)
```


---


## 层组合示例


## 实例


```python
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten

# 创建一个简单的CNN模型
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])
```


---


## 选择层的指导原则


- **输入数据类型**： - 图像数据：Conv2D + 池化层 - 序列数据：LSTM/GRU - 结构化数据：Dense层
- **模型深度**： - 深层网络需要配合BatchNormalization和Dropout
- **任务类型**： - 分类任务：最后一层使用softmax激活 - 回归任务：最后一层不使用激活函数或使用线性激活
- **计算资源**： - 大尺寸输入考虑使用池化层减少参数 - 资源有限时减少层数和单元数









	  AI 思考中...





			** [Keras 第一个神经网络](https://www.runoob.com/keras-neural-network.html)
			[TensorFlow 数据处理与管道](https://www.runoob.com/tensorflow-ata-processing-and-pipelines.html) **













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