# Pandas 与 NumPy 结合使用

- Source: https://www.runoob.com/pandas/pandas-numpy.html

Pandas 基于 NumPy 构建，两者紧密集成。理解它们的交互可以更高效地进行数据处理和科学计算。


---


## 相互转换


### DataFrame/Series 与 NumPy 互转


## 实例


```python
import pandas as pd
import numpy as np

# DataFrame 转 NumPy 数组
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})

arr = df.to_numpy()
print("DataFrame 转数组：")
print(arr)
print(f"类型: {type(arr)}")
print()

# Series 转数组
s = pd.Series([1, 2, 3])
arr = s.values  # 或 s.to_numpy()
print("Series 转数组：")
print(arr)
print()

# NumPy 转 DataFrame
arr = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(arr, columns=["A", "B"])
print("数组转 DataFrame：")
print(df)
```


---


## NumPy 函数在 Pandas 中使用


## 实例


```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4, 5])

# 使用 NumPy 函数
print("绝对值：", np.abs(s))
print("平方根：", np.sqrt(s))
print("指数：", np.exp(s))
print("对数：", np.log(s))
print()

# 条件筛选
print("大于3的值：")
print(s[s > 3])
```


### 向量化运算


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

# 向量化运算
print("A + B:", (df["A"] + df["B"]).tolist())
print("A * B:", (df["A"] * df["B"]).tolist())
print("A > B:", (df["A"] > df["B"]).tolist())
print()

# 使用 apply 进行逐元素计算
result = df.apply(lambda x: np.multiply(x, 2))
print("每个元素 * 2：")
print(result)
```


---


## 数值计算技巧


## 实例


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [10, 20, 30, 40, 50]
})

# 计算 A 相对于 B 的百分比变化
df["变化率"] = np.divide(df["A"], df["B"], where=df["B"] != 0) * 100
print("百分比变化：")
print(df)
print()

# 使用 np.where 进行条件赋值
df["标签"] = np.where(df["A"] > 3, "大", "小")
print("条件标签：")
print(df)
```


---


## 统计计算


## 实例


```python
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# NumPy 统计函数
print(f"均值: {np.mean(s):.2f}")
print(f"标准差: {np.std(s):.2f}")
print(f"最大值: {np.max(s)}")
print(f"最小值: {np.min(s)}")
print()

# 中位数
print(f"中位数: {np.median(s)}")
```


**
Pandas 和 NumPy 的深度集成使得复杂的数据处理变得简单高效。









	  AI 思考中...





			** [Pandas 处理大文件（chunksize）](https://www.runoob.com/pandas-chunksize.html)
			[Pandas 与 Matplotlib / Seaborn 进阶可视化](https://www.runoob.com/panda-matplotlib-seaborn.html) **













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