# Dash 教程

- Source: https://www.runoob.com/dash/dash-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/01/1344061-20210110191333418-2111010974.png)


Dash 是一个基于 Python 的开源框架，用于快速构建数据驱动的 Web 应用程序。


Dash 的核心优势在于它的易用性和灵活性，使得即使是没有前端开发经验的开发人员也能轻松上手。

Dash 允许用户通过简单的 Python 代码创建交互式的数据可视化应用，而无需掌握复杂的前端技术（如 JavaScript、HTML、CSS）。


---


## 谁适合阅读本教程？

Dash 是一个强大的工具，适合那些希望快速构建数据驱动型 Web 应用的开发者。


Dash 特别适合数据科学家、分析师和工程师,可以用几行代码创建一个功能强大的 Web 应用，展示数据分析结果、机器学习模型预测或其他数据驱动的功能。


Dash 的核心目标是让用户能够专注于数据和逻辑，而不是前端开发。

通过 Dash，你可以用几行代码创建一个功能强大的 Web 应用，展示数据分析结果、机器学习模型预测或其他数据驱动的功能。


Dash 可以将复杂的数据分析和可视化任务转化为交互式的 Web 应用，从而更有效地展示和分享工作成果。


---


## 学习本教程前你需要了解


本教程适合有 Python 基础的开发者学习，如果不了解 Python 可以查阅 [Python 3.x 基础教程](https://www.runoob.com/../python3/python3-tutorial.html)。


---


## 一个简单的 Dash 程序


以下是一个基本 Dash 示例：


## 实例


```
# 导入 Dash 相关库
from dash import Dash, dcc, html, Input, Output

# 创建 Dash 应用实例
app = Dash(__name__)

# 定义应用的布局
app.layout = html.Div([
    # 创建一个文本输入框
    dcc.Input(
        id='input',  # 输入框的 ID，用于回调函数
        value='初始值',  # 输入框的默认值
        type='text'  # 输入框类型为文本
    ),
    # 创建一个用于显示输出的 Div
    html.Div(id='output')
])

# 定义回调函数
@app.callback(
    Output('output', 'children'),  # 输出到 id 为 'output' 的 Div 的 children 属性
    Input('input', 'value')  # 输入来自 id 为 'input' 的输入框的 value 属性
)
def update_output_div(input_value):
    # 返回格式化后的字符串，显示用户输入的内容
    return f'你输入了: {input_value}'

# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)  # 启动应用，debug=True 表示开启调试模式
```


这个简单的应用包含一个输入框和一个显示区域。当用户在输入框中输入内容时，显示区域会实时更新显示用户输入的内容。


![](https://www.runoob.com/wp-content/uploads/2025/01/4903a8dd-95de-4cf7-a297-4ec897a83882.png)


---


## 相关链接

官方地址：[https://plotly.com/dash/](https://plotly.com/dash/)

Github 开源地址：[https://github.com/plotly/dash](https://github.com/plotly/dash)

Dash 官方文档：[https://dash.plotly.com/](https://dash.plotly.com/)








	  AI 思考中...






			[Dash 简介](https://www.runoob.com/dash-intro.html) **













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