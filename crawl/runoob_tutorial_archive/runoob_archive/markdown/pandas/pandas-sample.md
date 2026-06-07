# Pandas 抽样与随机数据

- Source: https://www.runoob.com/pandas/pandas-sample.html

Pandas 提供了丰富的随机抽样功能，可以从数据集中按要求随机选取样本，也支持生成随机数据。


---


## 随机抽样


### sample 方法


## 实例


```python
import pandas as pd
import numpy as np

# 创建大数据集
df = pd.DataFrame({
    "ID": range(1, 1001),
    "值": np.random.randn(1000)
})

# 随机抽取5行
print("随机抽取5行：")
print(df.sample(5))
print()

# 抽取30%的数据
print("随机抽取30%：")
print(df.sample(frac=0.3))
print()

# 可重复抽样
print("可重复抽样5行：")
print(df.sample(5, replace=True))
```


### 设置随机种子


## 实例


```python
import pandas as pd
import numpy as np

# 设置随机种子，保证结果可复现
np.random.seed(42)

df = pd.DataFrame({
    "ID": range(1, 11),
    "值": np.random.randn(10)
})

print("使用随机种子42：")
print(df.sample(3))

# 再次运行相同种子，得到相同结果
print("\n再次运行相同种子：")
np.random.seed(42)
print(df.sample(3))
```


---


## 随机数据生成


## 实例


```python
import pandas as pd
import numpy as np

# 生成随机整数
print("随机整数 [0, 10)：")
print(pd.Series(np.random.randint(0, 10, 5)))
print()

# 生成随机浮点数
print("随机浮点数 [0, 1)：")
print(pd.Series(np.random.random(5)))
print()

# 生成正态分布随机数
print("正态分布 N(0, 1)：")
print(pd.Series(np.random.randn(5)))
print()

# 指定均值和标准差
print("正态分布 N(10, 2)：")
print(pd.Series(np.random.normal(10, 2, 5)))
print()

# 随机选择
choices = ["A", "B", "C", "D"]
print("随机选择：")
print(pd.Series(np.random.choice(choices, 10)))
```


---


## 训练测试集划分


## 实例


```python
import pandas as pd
import numpy as np

# 模拟数据集
df = pd.DataFrame({
    "特征1": np.random.randn(100),
    "特征2": np.random.randn(100),
    "目标": np.random.choice([0, 1], 100)
})

# 划分训练集和测试集 (80% / 20%)
train = df.sample(frac=0.8, random_state=42)
test = df.drop(train.index)

print(f"训练集: {len(train)} 行")
print(f"测试集: {len(test)} 行")
print()

# 分层抽样（保持目标变量比例）
print("分层抽样：")
from sklearn.model_selection import train_test_split
# 需要安装 scikit-learn: pip install scikit-learn
# train, test = train_test_split(df, test_size=0.2, stratify=df["目标"])
```










	  AI 思考中...





			** [Pandas 描述性统计](https://www.runoob.com/pandas-describe.html)
			[Pandas 数据分箱（cut / qcut）](https://www.runoob.com/pandas-cut.html) **













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