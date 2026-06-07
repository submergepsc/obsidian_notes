# TensorFlow 高级 API - Keras

- Source: https://www.runoob.com/tensorflow/tensorflow-api-keras.html

Keras 是一个用 Python 编写的高级神经网络 API，它能够以 TensorFlow, CNTK 或 Theano 作为后端运行。Keras 的设计理念是用户友好、模块化和易扩展。


### Keras 的主要特点


- **简单易用**：提供直观一致的接口，适合快速原型设计
- **模块化**：神经网络层、损失函数、优化器等都是可插拔的模块
- **易扩展**：可以轻松添加新模块来表达新的研究想法
- **支持多后端**：可以无缝运行在 TensorFlow, CNTK 或 Theano 上


---


## Keras 核心概念


### 1. 模型 (Model)


Keras 的核心数据结构是模型，模型是组织神经网络层的方式。Keras 提供了两种主要的模型：


- **Sequential 模型**：层的线性堆叠
- **Functional API**：构建复杂模型的有向无环图


### 2. 层 (Layer)


层是 Keras 的基本构建块，每个层接收输入数据，进行某种计算后输出结果。Keras 提供了多种预定义层：


- 核心层：Dense, Activation, Dropout 等
- 卷积层：Conv2D, MaxPooling2D 等
- 循环层：LSTM, GRU 等
- 其他：Embedding, BatchNormalization 等


### 3. 激活函数 (Activation Function)


激活函数决定神经元的输出，常用的有：


- ReLU (Rectified Linear Unit)
- Sigmoid
- Tanh
- Softmax (多分类问题)


---


## Keras 基本工作流程


### 1. 定义模型


## 实例


```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])
```


### 2. 编译模型


## 实例


```python
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```


### 3. 训练模型


## 实例


```python
model.fit(x_train, y_train,
          epochs=5,
          batch_size=32)
```


### 4. 评估模型


## 实例


```python
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
```


### 5. 进行预测


## 实例


```python
classes = model.predict(x_test, batch_size=128)
```


---


## Keras 常用层详解


### 1. Dense 全连接层


## 实例


```python
Dense(units,
      activation=None,
      use_bias=True,
      kernel_initializer='glorot_uniform',
      bias_initializer='zeros')
```


- `units`：正整数，输出空间的维度
- `activation`：激活函数
- `use_bias`：是否使用偏置向量
- `kernel_initializer`：权重矩阵的初始化器
- `bias_initializer`：偏置向量的初始化器


### 2. Conv2D 二维卷积层


## 实例


```python
Conv2D(filters,
       kernel_size,
       strides=(1, 1),
       padding='valid',
       activation=None)
```


- `filters`：卷积核的数目
- `kernel_size`：卷积核的尺寸
- `strides`：卷积步长
- `padding`：填充方式 ('valid' 或 'same')


### 3. LSTM 长短期记忆网络层


## 实例


```python
LSTM(units,
     activation='tanh',
     recurrent_activation='hard_sigmoid',
     return_sequences=False)
```


- `units`：正整数，输出空间的维度
- `activation`：激活函数
- `recurrent_activation`：循环步的激活函数
- `return_sequences`：是否返回完整序列


---


## Keras 模型保存与加载


### 1. 保存整个模型


## 实例


```python
model.save('my_model.h5')  # 保存架构、权重和训练配置
```


### 2. 仅保存架构


## 实例


```python
json_string = model.to_json()  # 保存为JSON
yaml_string = model.to_yaml()  # 保存为YAML
```


### 3. 仅保存权重


## 实例


```python
model.save_weights('my_model_weights.h5')
```


### 4. 加载模型


## 实例


```python
from tensorflow.keras.models import load_model

model = load_model('my_model.h5')  # 加载完整模型
```


---


## Keras 回调函数


回调函数是在训练过程中特定时间点被调用的函数，用于：


- 模型检查点
- 提前停止
- 学习率调整
- 日志记录等


### 常用回调函数


## 实例


```python
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

callbacks = [
    ModelCheckpoint(filepath='best_model.h5', monitor='val_loss', save_best_only=True),
    EarlyStopping(monitor='val_loss', patience=3)
]

model.fit(x_train, y_train,
          epochs=10,
          callbacks=callbacks,
          validation_data=(x_val, y_val))
```


---


## Keras 实践示例：MNIST 手写数字识别


## 实例


```python
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical

# 加载数据
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 数据预处理
x_train = x_train.reshape(60000, 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(10000, 28, 28, 1).astype('float32') / 255
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 构建模型
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# 编译模型
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 训练模型
model.fit(x_train, y_train,
          batch_size=128,
          epochs=12,
          verbose=1,
          validation_data=(x_test, y_test))

# 评估模型
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
```


---


## Keras 进阶技巧


### 1. 自定义层


## 实例


```python
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Layer

class MyLayer(Layer):
    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(MyLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        self.kernel = self.add_weight(name='kernel',
                                     shape=(input_shape[1], self.output_dim),
                                     initializer='uniform',
                                     trainable=True)
        super(MyLayer, self).build(input_shape)

    def call(self, x):
        return K.dot(x, self.kernel)

    def compute_output_shape(self, input_shape):
        return (input_shape[0], self.output_dim)
```


### 2. 自定义损失函数


## 实例


```python
from tensorflow.keras import backend as K

def custom_loss(y_true, y_pred):
    return K.mean(K.square(y_pred - y_true), axis=-1)

model.compile(optimizer='adam', loss=custom_loss)
```


### 3. 学习率调度


## 实例


```python
from tensorflow.keras.callbacks import LearningRateScheduler

def scheduler(epoch, lr):
    if epoch < 10:
        return lr
    else:
        return lr * K.exp(-0.1)

callback = LearningRateScheduler(scheduler)
model.fit(x_train, y_train, epochs=15, callbacks=[callback])
```


---


## Keras 常见问题与解决方案


### 1. 过拟合问题


- 增加 Dropout 层
- 使用 L1/L2 正则化
- 增加训练数据
- 使用数据增强


### 2. 训练速度慢


- 增加批量大小
- 使用更简单的模型
- 尝试不同的优化器
- 使用 GPU 加速


### 3. 梯度消失/爆炸


- 使用 BatchNormalization
- 使用适当的权重初始化
- 使用 ReLU 等非饱和激活函数
- 使用梯度裁剪


---


## 总结


Keras 作为 TensorFlow 的高级 API，提供了简单直观的接口来构建和训练深度学习模型。通过本文，你应该已经掌握了：


- Keras 的核心概念和基本工作流程
- 常用层的使用方法
- 模型的保存与加载
- 回调函数的使用
- 实际项目中的应用示例
- 进阶技巧和常见问题解决方案


Keras 的强大之处在于它的灵活性和易用性，使得深度学习模型的开发变得更加高效。随着实践的深入，你将能够构建更加复杂的神经网络模型来解决各种实际问题。









	  AI 思考中...





			** [TensorFlow 张量操作](https://www.runoob.com/tensorflow-tensor-operations.html)
			[Keras 第一个神经网络](https://www.runoob.com/keras-neural-network.html) **













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