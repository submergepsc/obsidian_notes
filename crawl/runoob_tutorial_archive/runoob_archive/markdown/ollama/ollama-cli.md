# Ollama 模型交互

- Source: https://www.runoob.com/ollama/ollama-cli.html

Ollama 提供了多种方式与模型进行交互，其中最常见的就是通过命令行进行推理操作。


## 1. 命令行交互


通过命令行直接与模型进行交互是最简单的方式。


### 运行模型


使用 **ollama run** 命令启动模型并进入交互模式：


```
ollama run <model-name>
```


例如我们下载 deepseek-coder 模型：


## 实例


```
ollama run deepseek-coder
```


启动后，您可以直接输入问题或指令，模型会实时生成响应。


```
>>> 你好，你能帮我写一段代码吗？
当然可以。但是首先我想知道您希望在哪种编程语言中实现这个功能（例如Python、JavaScript等）和要解决什么问题或者完成的任务是什么样的例子呢？这样我们可以为您提供更准确的
内容，同时也方便我帮助你写出最适合您的代码片段。


>>> 写一段 python hello world
当然可以！这是一个简单的 "Hello, World!" 程序：

```python
print("Hello, World!")
```
这个脚本会输出 `Hello, World!`，并将其打印到控制台上。这只是最基本的 Python Hello world示例；Python是一种解释型、通用型的编程语言以其简洁性和易读性而闻名。它还允许
用户在代码中插入变量和表达式来创建复杂的行为。
```


### 退出交互模式


在交互模式下，输入 **/bye** 或按下 **Ctrl+d **退出。


---


## 2. 单次命令交互


如果您只需要模型生成一次响应，可以直接在命令行中传递输入。


### 使用管道输入


通过管道将输入传递给模型：


## 实例


```
echo "你是谁？" | ollama run deepseek-coder
```


输出结果如下：


```
我是由中国的深度求索（DeepSeek）公司开发的编程智能助手，名为DeepCoder。我专注于解答计算机科学相关的问题和任务。如果你有任何关于这个领域的话题或者需要帮助的地方，请
随时提问！
```


### 使用命令行参数


直接在命令行中传递输入：


```
ollama run deepseek-coder "Python 的 hello world 代码？"
```


输出结果如下：


```
在 Python 中，"Hello World!" 通常是这段简单的脚本：
```python
print("Hello World!")
```
当你运行这个程序时，它会输出 `Hello, World`。这是因为 print() 函数将字符串 "Hello, World" 打印到标准输出设备 (stdout) - 也就是你的屏幕上显示的信息（在这种情况下是命
令行终端或类似的工具中运行 Python 脚本时，它会直接写入控制台。
```


---


## 3. 多轮对话

Ollama 支持多轮对话，模型可以记住上下文。


## 实例


```
>>> 你好，你能帮我写一段 Python 代码吗？
当然可以！请告诉我你需要实现什么功能。

>>> 我想写一个计算斐波那契数列的函数。
好的，以下是一个简单的 Python 函数：
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```


---


## 4. 文件输入

可以将文件内容作为输入传递给模型。


假设 input.txt 文件内容为：


```
Python 的 hello world 代码？
```


将 input.txt 文件内容作为输入：


```
ollama run deepseek-coder < input.txt
```


---


## 5. 自定义提示词

通过 Modelfile 定义自定义提示词或系统指令，使模型在交互中遵循特定规则。


### 创建自定义模型

编写一个 Modelfile：


## 实例


```
FROM deepseek-coder
SYSTEM "你是一个编程助手，专门帮助用户编写代码。"
```


然后创建自定义模型：


```
ollama create runoob-coder -f ./Modelfile
```


运行自定义模型:


```
ollama run runoob-coder
```


---


## 6. 交互日志

Ollama 会记录交互日志，方便调试和分析。


查看日志:


```
ollama logs
```









	  AI 思考中...





			** [Ollama 基本概念](https://www.runoob.com/ollama-basic.html)
			[Ollama API 交互](https://www.runoob.com/ollama-api.html) **













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