# Pandas 常用函数

- Source: https://www.runoob.com/pandas/pandas-general-functions.html

Pandas 提供了大量用于数据处理和分析的函数，以下是一些常用的函数：


### 通用函数


| 函数 | 描述 |
| --- | --- |
| pd.isna(obj) | 检查对象是否为缺失值。 |
| pd.notna(obj) | 检查对象是否不为缺失值。 |
| pd.concat(objs, axis) | 连接多个对象。 |
| pd.merge(left, right, on) | 按列合并 DataFrame。 |
| pd.get_dummies(data) | 分类变量 One-Hot 编码。 |
| pd.cut(x, bins) | 连续数据分箱。 |
| pd.qcut(x, q) | 按分位数分箱。 |
| pd.to_numeric(arg) | 转换为数值。 |
| pd.to_datetime(arg) | 转换为时间。 |
| pd.unique(values) | 获取唯一值。 |
| pd.value_counts(values) | 统计频次。 |
| pd.factorize(values) | 编码分类变量。 |
| pd.crosstab(index, columns) | 交叉表。 |
| pd.pivot_table(data) | 透视表。 |
| pd.melt(frame) | 宽转长。 |


---


### 数据读取与写入（IO）


| 函数 | 描述 |
| --- | --- |
| pd.read_csv() | 读取 CSV 文件。 |
| pd.read_excel() | 读取 Excel。 |
| pd.read_json() | 读取 JSON。 |
| pd.read_html() | 解析 HTML 表格。 |
| pd.read_sql() | 从数据库读取。 |
| df.to_csv() | 写入 CSV。 |
| df.to_excel() | 写入 Excel。 |
| df.to_json() | 写入 JSON。 |
| df.to_parquet() | 写入 Parquet。 |


---


### 数据清洗


| 函数 | 描述 |
| --- | --- |
| df.dropna() | 删除缺失值。 |
| df.fillna() | 填充缺失值。 |
| df.replace() | 替换数据。 |
| df.drop_duplicates() | 去重。 |
| df.astype() | 类型转换。 |
| df.rename() | 重命名列。 |
| df.sort_values() | 排序。 |
| df.reset_index() | 重置索引。 |


---


### 数据选择与过滤


| 函数 | 描述 |
| --- | --- |
| df.head() | 前几行。 |
| df.tail() | 后几行。 |
| df.loc[] | 标签索引。 |
| df.iloc[] | 位置索引。 |
| df.query() | 条件筛选。 |
| df.filter() | 列过滤。 |


---


### 分组与聚合


| 函数 | 描述 |
| --- | --- |
| df.groupby() | 分组操作。 |
| groupby.sum() | 聚合求和。 |
| groupby.mean() | 平均值。 |
| groupby.agg() | 多聚合。 |
| groupby.transform() | 变换。 |


---


### 数学和统计函数


| 函数 | 描述 |
| --- | --- |
| Series.sum() | 求和。 |
| Series.mean() | 平均值。 |
| Series.median() | 中位数。 |
| Series.std() | 标准差。 |
| Series.var() | 方差。 |
| Series.corr() | 相关系数。 |
| Series.quantile() | 分位数。 |
| Series.cumsum() | 累计和。 |


---


### 字符串处理


| 函数 | 描述 |
| --- | --- |
| Series.str.lower() | 小写。 |
| Series.str.upper() | 大写。 |
| Series.str.strip() | 去空格。 |
| Series.str.replace() | 替换。 |
| Series.str.contains() | 匹配。 |
| Series.str.split() | 拆分。 |
| Series.str.len() | 长度。 |


---


### 时间序列


| 函数 | 描述 |
| --- | --- |
| pd.date_range() | 生成日期。 |
| pd.Timestamp() | 时间戳。 |
| pd.Timedelta() | 时间差。 |
| Series.dt.year | 年份。 |
| Series.dt.month | 月份。 |
| Series.dt.day | 天。 |
| Series.dt.weekday | 星期。 |


---


### 数据重塑


| 函数 | 描述 |
| --- | --- |
| df.pivot() | 透视。 |
| df.pivot_table() | 透视表。 |
| df.stack() | 列转行。 |
| df.unstack() | 行转列。 |
| pd.melt() | 宽转长。 |


---


## 实例



```python
import pandas as pd

# 通用函数
s = pd.Series([1, 2, 3, None])
print(pd.isna(s))

# 数学
print(s.sum())

# 字符串
s_str = pd.Series(['a', 'b'])
print(s_str.str.upper())

# 时间
dates = pd.to_datetime(['2023-01-01'])
print(dates.dt.month)
```


---


如果需要更详细的信息，可以参考 [Pandas 官方文档](https://pandas.pydata.org/docs/reference/general_functions.html)。








	  AI 思考中...





			** [Pandas Input/Output (输入输出) API 手册](https://www.runoob.com/pandas-io-api-reference.html)
			[Pandas 数组/标量/数据类型参考手册](https://www.runoob.com/pandas-arrays-scalars-data-types-ref.html) **













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