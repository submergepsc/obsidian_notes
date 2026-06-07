# Matplotlib 中文显示

- Source: https://www.runoob.com/matplotlib/matplotlib-zh.html

Matplotlib 中文显示不是特别友好，要在 Matplotlib 中显示中文，我们可以通过两个方法：


- 设置 Matplotlib 的字体参数。
- 下载使用支持中文的字体库。

在未设置字体，默认情况显示如下，中文部分不能正常显示：

![](https://www.runoob.com/wp-content/uploads/2023/12/fad4973c29ae7f9ec1570a1989340c97.png)


---


## Matplotlib 的字体参数


我们可以先获取系统的字体库列表：


## 实例


```python
from matplotlib import pyplot as plt
import matplotlib
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in a:
    print(i)
```


输出结果类似如下：


```
...
Heiti TC
Helvetica
Helvetica Neue
Herculanum
Hiragino Maru Gothic Pro
Hiragino Mincho ProN
Hiragino Sans
Hiragino Sans GB
Hoefler Text
...
```


以上代码输出 font_manager 的 ttflist 中所有注册的名字，找一个看中文字体例如：STFangsong(仿宋）、Heiti TC（黑体）,然后添加以下代码即可。


**对于 Windows：**


```
plt.rcParams['font.family'] = 'SimHei'  # 替换为你选择的字体
```


在 Windows 系统上，选择 SimHei（黑体）或其他中文字体，并将其设置为 Matplotlib 的默认字体。


**对于 Linux：**


```
plt.rcParams['font.family'] = 'WenQuanYi Micro Hei'  # 替换为你选择的字体
```


在Linux系统上，使用 fc-list 命令查看已安装的字体，选择一个中文字体，并将其设置为 Matplotlib 的默认字体。


**对于 macOS：**


```
plt.rcParams['font.family'] = 'Heiti TC'  # 替换为你选择的字体
```


通过设置 **plt.rcParams['font.family']**，你告诉 Matplotlib 使用选择的字体来渲染文本，从而在图表中正确显示中文。

这样，你就能够在 Matplotlib 图表中使用系统支持的中文字体了。


## 实例


```python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Heiti TC'  # 替换为你选择的字体

# 创建数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 绘制折线图
plt.plot(x, y)

# 添加标题和标签
plt.title('折线图示例')
plt.xlabel('X轴')
plt.ylabel('Y轴')

# 显示图形
plt.show()
```


这样中文就可以正常显示了，显示如下：


![](https://www.runoob.com/wp-content/uploads/2023/12/e1105655de58ea37c9f579028ca22ad0.png)


各大平台系统通用方法：


```
# -------------------------- 设置中文字体 start --------------------------
plt.rcParams['font.sans-serif'] = [
    # Windows 优先
    'SimHei', 'Microsoft YaHei',
    # macOS 优先
    'PingFang SC', 'Heiti TC',
    # Linux 优先
    'WenQuanYi Micro Hei', 'DejaVu Sans'
]
# 修复负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
# -------------------------- 设置中文字体 end --------------------------
```


## 实例


```python
import numpy as np
import matplotlib.pyplot as plt

# -------------------------- 设置中文字体 start --------------------------
plt.rcParams['font.sans-serif'] = [
    # Windows 优先
    'SimHei', 'Microsoft YaHei',
    # macOS 优先
    'PingFang SC', 'Heiti TC',
    # Linux 优先
    'WenQuanYi Micro Hei', 'DejaVu Sans'
]
# 修复负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
# -------------------------- 设置中文字体 end --------------------------

# 生成模拟数据：在正弦曲线基础上加入一些随机噪声
np.random.seed(42)
X = np.linspace(0, 10, 20)
y_true = np.sin(X)                     # 真实的潜在规律（我们不知道）
y_noise = np.random.randn(20) * 0.3   # 随机噪声
y = y_true + y_noise                  # 我们实际观测到的数据

plt.scatter(X, y, label='观测数据 (含噪声)', color='blue', alpha=0.6)
plt.plot(X, y_true, label='真实规律 (y=sin(x))', color='green', linewidth=2)
plt.xlabel('X')
plt.ylabel('y')
plt.title('数据与潜在规律')
plt.legend()
plt.grid(True)
plt.show()
```


我们的目标是找到一条曲线（模型），能最好地描述这些蓝色散点（数据）所反映的规律。

模型对数据的描述程度，就是**拟合**。


---


## 使用字体库


Matplotlib 默认情况不支持中文，我们可以使用以下简单的方法来解决。


这里我们使用思源黑体，思源黑体是 Adobe 与 Google 推出的一款开源字体。


官网：[https://source.typekit.com/source-han-serif/cn/](https://source.typekit.com/source-han-serif/cn/)


GitHub 地址：[https://github.com/adobe-fonts/source-han-sans/tree/release/OTF/SimplifiedChinese](https://github.com/adobe-fonts/source-han-sans/tree/release/OTF/SimplifiedChinese)


打开链接后，在里面选一个就好了：


![](https://www.runoob.com/wp-content/uploads/2020/07/134652C4-1164-466B-ACA2-ECE8B7E6F2AF.jpg)


你也可以在网盘下载: [https://pan.baidu.com/s/10-w1JbXZSnx3Tm6uGpPGOw](https://pan.baidu.com/s/10-w1JbXZSnx3Tm6uGpPGOw)，提取码：**yxqu**。


可以下载个 OTF 字体，比如 SourceHanSansSC-Bold.otf，将该文件文件放在当前执行的代码文件中：


SourceHanSansSC-Bold.otf 文件放在当前执行的代码文件中：


## 实例



```python
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

# fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径
zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")

x = np.arange(1,11)
y =  2  * x +  5
plt.title("菜鸟教程 - 测试", fontproperties=zhfont1)

# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x 轴", fontproperties=zhfont1)
plt.ylabel("y 轴", fontproperties=zhfont1)
plt.plot(x,y)
plt.show()
```


执行输出结果如下图：


![](https://www.runoob.com/wp-content/uploads/2018/10/246E0137-BFFA-40D1-B6E1-8D4A2789B12F.jpg)








	  AI 思考中...





			** [Matplotlib imread() 方法](https://www.runoob.com/matplotlib-imread.html)
			[Seaborn 教程](https://www.runoob.com/seaborn-tutorial.html) **













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