# Pandas 字符串操作

- Source: https://www.runoob.com/pandas/pandas-string.html

Pandas 提供了强大的字符串处理功能，通过 `.str` 访问器可以像操作 Python 字符串一样处理 Series 中的每个元素。


---


## str 访问器概述


当 Series 的数据类型是 `object` 时，可以使用 `.str` 访问器进行字符串操作。


## 实例


```python
import pandas as pd

# 创建包含字符串的 Series
s = pd.Series(["hello", "world", "pandas", "Python"])

print("原始 Series：")
print(s)
print()

# 转换为小写
print("转小写：")
print(s.str.lower())
print()

# 转换为大写
print("转大写：")
print(s.str.upper())
print()

# 首字母大写
print("首字母大写：")
print(s.str.capitalize())
```


---


## 常用字符串函数


### 大小写转换


| 方法 | 说明 | 示例 |
| --- | --- | --- |
| str.lower() | 转小写 | "Hello" → "hello" |
| str.upper() | 转大写 | "Hello" → "HELLO" |
| str.title() | 首字母大写 | "hello world" → "Hello World" |
| str.capitalize() | 首字母大写，其余小写 | "hELLO" → "Hello" |
| str.swapcase() | 大小写互换 | "HeLLo" → "hEllO" |


### 字符串查找与替换


## 实例


```python
import pandas as pd

s = pd.Series(["hello world", "python pandas", "data science", "machine learning"])

print("原始数据：")
print(s)
print()

# 包含判断
print("包含'python'：")
print(s.str.contains("python", case=False))
print()

# 开头/结尾判断
print("以'hello'开头：")
print(s.str.startswith("hello"))
print()

# 替换
print("替换空格为下划线：")
print(s.str.replace(" ", "_"))
print()

# 拆分
print("按空格拆分：")
print(s.str.split(" "))
```


### 去空格与填充


## 实例


```python
import pandas as pd

s = pd.Series(["  hello  ", "world  ", "  pandas", " python "])

print("原始数据：")
print(s)
print()

# 去除首尾空格
print("去除首尾空格：")
print(s.str.strip())
print()

# 去除左边空格
print("去除左边空格：")
print(s.str.lstrip())
print()

# 去除右边空格
print("去除右边空格：")
print(s.str.rstrip())
print()

# 填充
print("左侧填充0至长度10：")
print(s.str.pad(10, side="left", fillchar="0"))
```


---


### 切片与连接


## 实例


```python
import pandas as pd

s = pd.Series(["hello", "world", "python", "pandas"])

print("原始数据：")
print(s)
print()

# 切片
print("前3个字符：")
print(s.str[:3])
print()

# 从第1位开始取3个
print("从第1位开始取3个：")
print(s.str[1:4])
print()

# 字符串连接
s1 = pd.Series(["Hello", "World"])
s2 = pd.Series(["Python", "Pandas"])
print("使用 + 连接：")
print(s1 + " " + s2)
print()

# join 连接（使用指定分隔符）
print("join 连接：")
print(s1.str.cat(s2, sep="-"))
```


---


## 正则表达式支持


Pandas 的字符串函数支持正则表达式，这是处理复杂字符串模式的利器。


## 实例


```python
import pandas as pd

s = pd.Series([
    "[email protected]",
    "[email protected]",
    "invalid-email",
    "[email protected]"
])

print("原始数据：")
print(s)
print()

# 提取邮箱
print("提取用户名：")
print(s.str.extract(r"(\w+)@"))
print()

print("提取域名：")
print(s.str.extract(r"@(\w+\.\w+)"))
print()

# 替换
print("替换邮箱为 [email]：")
print(s.str.replace(r"\w+@\w+\.\w+", "[email]", regex=True))
print()

# 包含匹配
print("包含.com或.org：")
print(s.str.contains(r"\.com|\.org"))
```


### 提取和分割


## 实例


```python
import pandas as pd

s = pd.Series(["2024-01-01", "2024-02-15", "2024-03-20"])

print("原始数据：")
print(s)
print()

# 提取年月日
extract_df = s.str.extract(r"(\d{4})-(\d{2})-(\d{2})")
extract_df.columns = ["年", "月", "日"]
print("提取年月日：")
print(extract_df)
print()

# 按分隔符拆分
s2 = pd.Series(["a,b,c", "d,e,f", "g,h,i"])
print("按逗号拆分：")
print(s2.str.split(","))
print()

# 拆分并展开为 DataFrame
print("拆分并展开：")
print(s2.str.split(",", expand=True))
```


---


## 统计与转换


### 长度与计数


## 实例


```python
import pandas as pd

s = pd.Series(["hello", "world", "python", "pandas"])

print("原始数据：")
print(s)
print()

# 字符串长度
print("字符串长度：")
print(s.str.len())
print()

# 字符计数
s2 = pd.Series(["hello", "world", "aaa", "bbb"])
print("字符'l'出现次数：")
print(s2.str.count("l"))
```


### 类型转换


## 实例


```python
import pandas as pd

# 字符串转数值
s = pd.Series(["1", "2", "3", "abc"])
print("字符串转数值：")
print(pd.to_numeric(s, errors="coerce"))
print()

# 数值转字符串
s2 = pd.Series([1, 2, 3, 4])
print("数值转字符串：")
print(s2.astype(str).str.zfill(4))  # 补零到4位
```


---


## 实战：数据清洗


## 实例


```python
import pandas as pd
import numpy as np

# 模拟脏数据
df = pd.DataFrame({
    "姓名": ["  张三  ", "李四", "王五　"],
    "电话": ["138-0000-0000", "13900000000", "  010-12345678  "],
    "邮箱": ["[email protected]", "[email protected]", "[email protected] "]
})

print("原始数据：")
print(df)
print()

# 清洗步骤
# 1. 去除空格
df["姓名"] = df["姓名"].str.strip()
df["电话"] = df["电话"].str.replace("-", "").str.strip()
df["邮箱"] = df["邮箱"].str.strip().str.lower()

print("清洗后：")
print(df)
print()

# 2. 验证数据
print("邮箱验证：")
print(df["邮箱"].str.contains(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"))
```


---


## 注意事项


**1、处理缺失值**


字符串操作默认会跳过缺失值（NaN），如果需要处理，可以使用 `.fillna()` 先填充。


**2、大小写敏感**


大部分函数默认大小写敏感，使用 `case=False` 参数可以进行不区分大小写的匹配。


**3、正则表达式性能**


正则表达式功能强大但相对较慢，处理大数据量时注意性能。


**
字符串处理是数据清洗的重要环节，合理使用 `.str` 访问器可以高效完成大部分文本处理任务。









	  AI 思考中...





			** [Pandas 重复数据处理](https://www.runoob.com/pandas-duplicate.html)
			[Pandas 日期与时间](https://www.runoob.com/pandas-datetime.html) **













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