# Pandas 数据分箱（cut / qcut）

- Source: https://www.runoob.com/pandas/pandas-cut.html

数据分箱（也称为分桶）是将连续变量离散化的过程，常用于数据预处理、特征工程和数据分析。


---


## cut 等宽分箱


`cut` 将数据划分为等宽的区间。


## 实例


```python
import pandas as pd
import numpy as np

# 创建年龄数据
ages = pd.Series([5, 15, 25, 35, 45, 55, 65, 75, 85])

print("原始数据：")
print(ages.tolist())
print()

# 等宽分箱（5个区间）
bins = [0, 20, 40, 60, 80, 100]
labels = ["儿童", "青年", "中年", "中老年", "老年"]

age_bins = pd.cut(ages, bins=bins, labels=labels)
print("等宽分箱结果：")
print(age_bins)
print()

# 包含右边界
age_bins2 = pd.cut(ages, bins=4)
print("自动等宽分箱：")
print(age_bins2)
```


### 返回类别和边界


## 实例


```python
import pandas as pd
import numpy as np

ages = pd.Series([5, 15, 25, 35, 45])

# 返回区间索引
result = pd.cut(ages, bins=4, labels=False)
print("区间索引：")
print(result)
print()

# 返回区间边界
result = pd.cut(ages, bins=4, retbins=True)
print("区间边界：")
print(result[1])
```


---


## qcut 等频分箱


`qcut` 将数据划分为具有大致相同数据点的区间。


## 实例


```python
import pandas as pd
import numpy as np

# 不均匀分布的数据
data = pd.Series([1, 1, 1, 2, 3, 4, 5, 10, 20, 30, 50, 100])

print("原始数据：")
print(data.tolist())
print()

# 等宽分箱（会导致分布不均）
cut_result = pd.cut(data, q=4)
print("等宽分箱：")
print(cut_result.value_counts())
print()

# 等频分箱（每个区间数据点数量大致相同）
qcut_result = pd.qcut(data, q=4)
print("等频分箱：")
print(qcut_result.value_counts())
```


### 指定分位数


## 实例


```python
import pandas as pd

data = pd.Series(range(1, 101))

# 按指定分位数划分
result = pd.qcut(data, q=[0, 0.1, 0.3, 0.7, 0.9, 1])
print("按分位数划分：")
print(result.value_counts().sort_index())
```


---


## 实战：数据分析


## 实例


```python
import pandas as pd
import numpy as np

# 模拟客户消费数据
np.random.seed(42)
customers = pd.DataFrame({
    "客户ID": range(1, 101),
    "消费金额": np.random.exponential(500, 100) + 100
})

# 分箱为不同消费等级
customers["消费等级"] = pd.cut(
    customers["消费金额"],
    bins=[0, 300, 500, 800, float("inf")],
    labels=["低", "中", "高", "VIP"]
)

# 统计各等级客户数
print("消费等级分布：")
print(customers["消费等级"].value_counts())
print()

# 按等级统计平均消费
print("各等级平均消费：")
print(customers.groupby("消费等级")["消费金额"].mean().round(2))
```










	  AI 思考中...





			** [Pandas 抽样与随机数据](https://www.runoob.com/pandas-sample.html)
			[Pandas 处理大文件（chunksize）](https://www.runoob.com/pandas-chunksize.html) **













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