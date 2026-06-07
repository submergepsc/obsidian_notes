# TensorFlow 模型保存与加载

- Source: https://www.runoob.com/tensorflow/tensorflow-save-load.html

在机器学习和深度学习项目中，模型的保存与加载是至关重要的环节。

TensorFlow 提供了多种方式来保存和恢复模型，使开发者能够：


- 保存训练好的模型供后续使用
- 分享模型给其他开发者
- 从检查点恢复训练
- 部署模型到生产环境


TensorFlow 2.x 主要支持三种模型保存格式：


- SavedModel 格式（推荐）
- HDF5 格式（.h5）
- 旧版 Keras 格式


---


## 保存整个模型


### SavedModel 格式


SavedModel 是 TensorFlow 推荐的模型保存格式，它包含完整的模型信息：


## 实例


```python
import tensorflow as tf

# 创建并训练一个简单模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)

# 保存为SavedModel格式
model.save('my_model')  # 注意：没有文件扩展名
```


保存后的目录结构：


```
my_model/
├── assets/
├── variables/
│   ├── variables.data-00000-of-00001
│   └── variables.index
└── saved_model.pb
```


### HDF5 格式


HDF5 是另一种常用的模型保存格式：


## 实例


```python
# 保存为HDF5格式
model.save('my_model.h5')  # 注意.h5扩展名
```


### 两种格式的区别


| 特性 | SavedModel | HDF5 |
| --- | --- | --- |
| 包含自定义对象 | 是 | 需要额外配置 |
| 包含优化器状态 | 是 | 可选 |
| TensorFlow Serving | 原生支持 | 不支持 |
| 文件大小 | 较大 | 较小 |


---


## 加载整个模型


### 从 SavedModel 加载


## 实例


```python
# 从SavedModel加载
loaded_model = tf.keras.models.load_model('my_model')

# 验证模型
loss, acc = loaded_model.evaluate(x_test, y_test, verbose=2)
print(f"Restored model, accuracy: {100*acc:.1f}%")
```


### 从 HDF5 文件加载


## 实例


```python
# 从HDF5文件加载
loaded_model = tf.keras.models.load_model('my_model.h5')

# 验证模型
loss, acc = loaded_model.evaluate(x_test, y_test, verbose=2)
print(f"Restored model, accuracy: {100*acc:.1f}%")
```


---


## 选择性保存与加载


### 仅保存权重


## 实例


```python
# 保存权重
model.save_weights('my_model_weights')

# 保存为HDF5格式的权重
model.save_weights('my_model_weights.h5')
```


### 加载权重


## 实例


```python
# 创建相同架构的模型
new_model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
new_model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

# 加载权重
new_model.load_weights('my_model_weights')

# 或者对于.h5文件
new_model.load_weights('my_model_weights.h5')
```


### 保存自定义训练循环的检查点


## 实例


```python
# 创建检查点回调
checkpoint_path = "training_1/cp.ckpt"
cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    save_weights_only=True,
    verbose=1)

# 使用回调训练模型
model.fit(x_train, y_train,
          epochs=10,
          callbacks=[cp_callback])
```


---


## 模型保存与加载的最佳实践


- **生产环境部署**：优先使用 SavedModel 格式
- **跨平台共享**：HDF5 格式更通用
- **训练中断恢复**：使用检查点回调定期保存
- **自定义对象处理**：
```
model.save('custom_model', save_format='tf')
```

- **模型版本控制**：为不同版本的模型创建不同目录


---


## 常见问题与解决方案


### 自定义层/模型保存问题


## 实例


```python
# 自定义层示例
class CustomLayer(tf.keras.layers.Layer):
    def __init__(self, units=32, **kwargs):
        super().__init__(**kwargs)
        self.units = units

    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer="random_normal",
            trainable=True)

    def call(self, inputs):
        return tf.matmul(inputs, self.w)

    def get_config(self):
        config = super().get_config()
        config.update({"units": self.units})
        return config

# 使用自定义层并保存
model = tf.keras.Sequential([CustomLayer(10)])
model.compile(optimizer='adam', loss='mse')
model.save('custom_model')  # 会自动保存自定义层
```


### 跨版本兼容性问题


- 尽量使用相同版本的 TensorFlow 保存和加载模型
- 对于生产环境，考虑使用 TensorFlow Serving 来避免版本问题


### 大模型保存优化


## 实例


```python
# 使用save_weights替代save来减少保存时间
model.save_weights('large_model_weights.h5')
```










	  AI 思考中...





			** [TensorFlow 实例 – 回归问题](https://www.runoob.com/tensorflow-regression.html)
			[TensorFlow 模型转换与优化](https://www.runoob.com/tensorflow-conversion-and-optimization.html) **













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