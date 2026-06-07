# Pandas 与 Matplotlib / Seaborn 进阶可视化

- Source: https://www.runoob.com/pandas/panda-matplotlib-seaborn.html

Pandas 内置了基本的绘图功能，结合 Matplotlib 和 Seaborn 可以创建更丰富的可视化图表。


---


## Pandas 内置绘图


### 折线图


## 实例


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置中文显示（需要系统中安装中文字体）
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# 创建时间序列数据
dates = pd.date_range("2024-01-01", periods=30, freq="D")
df = pd.DataFrame({
    "日期": dates,
    "销售额": 100 + np.random.randn(30).cumsum(),
    "访客数": 50 + np.random.randn(30).cumsum() * 10
})
df = df.set_index("日期")

print("数据：")
print(df.head())
print("\n绘图数据准备完成，请使用 plt.show() 显示图表")
```


### 柱状图


## 实例


```python
import pandas as pd
import matplotlib.pyplot as plt

# 分类数据
data = {
    "产品": ["A", "B", "C", "D", "E"],
    "销量": [120, 150, 90, 180, 110]
}
df = pd.DataFrame(data)

# 柱状图
print("使用 df.plot.bar() 绘制柱状图")
print("\n数据：")
print(df)
```


### 饼图


## 实例


```python
import pandas as pd

# 饼图数据
s = pd.Series([30, 25, 20, 15, 10], index=["A", "B", "C", "D", "E"])

print("使用 s.plot.pie() 绘制饼图")
print("\n数据：")
print(s)
```


---


## Matplotlib 结合


## 实例


```python
import pandas as pd
import numpy as np

# 创建数据
df = pd.DataFrame({
    "x": range(10),
    "y1": np.random.randn(10).cumsum(),
    "y2": np.random.randn(10).cumsum() + 5
})

print("Matplotlib 绘图示例代码：")
print("""
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# 折线图
ax1.plot(df["x"], df["y1"], label="Y1", color="blue")
ax1.plot(df["x"], df["y2"], label="Y2", color="red")
ax1.set_title("折线图")
ax1.legend()
ax1.grid(True)

# 散点图
ax2.scatter(df["y1"], df["y2"], alpha=0.6)
ax2.set_title("散点图")
ax2.set_xlabel("Y1")
ax2.set_ylabel("Y2")

plt.tight_layout()
plt.show()
""")
```


### 子图布局


## 实例


```python
import pandas as pd
import numpy as np

# 2x2 子图示例
print("2x2 子图布局示例：")
print("""
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 1. 折线图
df["y1"].plot(ax=axes[0, 0])
axes[0, 0].set_title("折线图")

# 2. 柱状图
df["y2"].plot.bar(ax=axes[0, 1])
axes[0, 1].set_title("柱状图")

# 3. 直方图
df["y1"].hist(ax=axes[1, 0], bins=10)
axes[1, 0].set_title("直方图")

# 4. 饼图
pd.Series([10, 20, 30]).plot.pie(ax=axes[1, 1])
axes[1, 1].set_title("饼图")

plt.tight_layout()
plt.show()
""")
```


---


## Seaborn 高级可视化


## 实例


```python
import pandas as pd
import numpy as np

# 演示 Seaborn 功能
print("Seaborn 可视化示例：")
print("""
import seaborn as sns
import matplotlib.pyplot as plt

# 设置样式
sns.set_style("whitegrid")

# 1. 关系图
fig, ax = plt.subplots(figsize=(8, 5))
sns.lineplot(data=df, x="x", y="y1", ax=ax)
ax.set_title("折线图")

# 2. 分布图
sns.histplot(df["y1"], kde=True, ax=ax)

# 3. 箱线图
sns.boxplot(data=df, x="category", y="value")

# 4. 热力图
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

plt.show()
""")
```


**
Matplotlib 提供底层控制，Seaborn 提供高层接口，两者结合可以创建各种专业图表。









	  AI 思考中...





			** [Pandas 与 NumPy 结合使用](https://www.runoob.com/pandas-numpy.html)
			[Pandas 电商数据分析实战](https://www.runoob.com/pandas-ecommerce.html) **













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