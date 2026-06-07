# Ollama Python 使用

- Source: https://www.runoob.com/ollama/ollama-python-sdk.html

Ollama 提供了 Python SDK，可以让我们能够在 Python 环境中与本地运行的模型进行交互。


通过 Ollama 的 Python SDK 能够轻松地将自然语言处理任务集成到 Python 项目中，执行各种操作，如文本生成、对话生成、模型管理等，且不需要手动调用命令行。


### 安装 Python SDK

首先，我们需要安装 Ollama 的 Python SDK。

可以使用 pip 安装：


```
pip install ollama
```


确保你的环境中已安装了 Python 3.x，并且网络环境能够访问 Ollama 本地服务。


### 启动本地服务

在使用 Python SDK 之前，确保 Ollama 本地服务已经启动。

你可以使用命令行工具来启动它：


```
ollama serve
```


启动本地服务后，Python SDK 会与本地服务进行通信，执行模型推理等任务。


### 使用 Ollama 的 Python SDK 进行推理

安装了 SDK 并启动了本地服务后，我们就可以通过 Python 代码与 Ollama 进行交互。


首先，从 ollama 库中导入 chat 和 ChatResponse：


```
from ollama import chat
from ollama import ChatResponse
```


通过 Python SDK，你可以向指定的模型发送请求，生成文本或对话：


## 实例


```
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='deepseek-coder', messages=[
  {
    'role': 'user',
    'content': '你是谁？',
  },
])
# 打印响应内容
print(response['message']['content'])

# 或者直接访问响应对象的字段
#print(response.message.content)
```


执行以上代码，输出结果为：


```
我是由中国的深度求索（DeepSeek）公司开发的编程智能助手，名为DeepCoder。我可以帮助你解答与计算机科学相关的问题和任务。如果你有任何关于这方面的话题或者需要在某个领域进行学习或查询信息时请随时提问！
```


llama SDK 还支持流式响应，我们可以在发送请求时通过设置 **stream=True** 来启用响应流式传输。


## 实例


```
from ollama import chat

stream = chat(
    model='deepseek-coder',
    messages=[{'role': 'user', 'content': '你是谁？'}],
    stream=True,
)

# 逐块打印响应内容
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
```


---


## 自定义客户端

你还可以创建自定义客户端，来进一步控制请求配置，比如设置自定义的 headers 或指定本地服务的 URL。


### 创建自定义客户端


通过 Client，你可以自定义请求的设置（如请求头、URL 等），并发送请求。


## 实例


```
from ollama import Client

client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'}
)

response = client.chat(model='deepseek-coder', messages=[
    {
        'role': 'user',
        'content': '你是谁?',
    },
])
print(response['message']['content'])
```


### 异步客户端

如果你希望异步执行请求，可以使用 AsyncClient 类，适用于需要并发的场景。


## 实例


```
import asyncio
from ollama import AsyncClient

async def chat():
    message = {'role': 'user', 'content': '你是谁?'}
    response = await AsyncClient().chat(model='deepseek-coder', messages=[message])
    print(response['message']['content'])

asyncio.run(chat())
```


异
步客户端支持与传统的同步请求一样的功能，唯一的区别是请求是异步执行的，可以提高性能，尤其是在高并发场景下。


### 异步流式响应

如果你需要异步地处理流式响应，可以通过将 **stream=True** 设置为异步生成器来实现。


## 实例


```
import asyncio
from ollama import AsyncClient

async def chat():
    message = {'role': 'user', 'content': '你是谁?'}
    async for part in await AsyncClient().chat(model='deepseek-coder', messages=[message], stream=True):
        print(part['message']['content'], end='', flush=True)

asyncio.run(chat())
```


这里，响应将逐部分地异步返回，每部分都可以即时处理。


---


## 常用 API 方法

Ollama Python SDK 提供了一些常用的 API 方法，用于操作和管理模型。


**1. chat 方法**

与模型进行对话生成，发送用户消息并获取模型响应：


```
ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': 'Why is the sky blue?'}])
```


**2. generate 方法**

用于文本生成任务。与 chat 方法类似，但是它只需要一个 prompt 参数：


```
ollama.generate(model='llama3.2', prompt='Why is the sky blue?')
```


**3. list 方法**


列出所有可用的模型：


```
ollama.list()
```


**4. show 方法**


显示指定模型的详细信息：


```
ollama.show('llama3.2')
```


**5. create 方法**


从现有模型创建新的模型：


```
ollama.create(model='example', from_='llama3.2', system="You are Mario from Super Mario Bros.")
```


**6. copy 方法**

复制模型到另一个位置：


```
ollama.copy('llama3.2', 'user/llama3.2')
```


**7. delete 方法**


删除指定模型：


```
ollama.delete('llama3.2')
```


**8. pull 方法**


从远程仓库拉取模型：


```
ollama.pull('llama3.2')
```


**9. push 方法**


将本地模型推送到远程仓库：


```
ollama.push('user/llama3.2')
```


**10. embed 方法**


生成文本嵌入：


```
ollama.embed(model='llama3.2', input='The sky is blue because of rayleigh scattering')
```


**11. ps 方法**

查看正在运行的模型列表：


```
ollama.ps()
```


---


## 错误处理

Ollama SDK 会在请求失败或响应流式传输出现问题时抛出错误。


我们可以使用 try-except 语句来捕获这些错误，并根据需要进行处理。


## 实例


```
model = 'does-not-yet-exist'

try:
    response = ollama.chat(model)
except ollama.ResponseError as e:
    print('Error:', e.error)
    if e.status_code == 404:
        ollama.pull(model)
```


在上述例子中，如果模型 does-not-yet-exist 不存在，抛出 ResponseError 错误，捕获后你可以选择拉取该模型或进行其他处理。








	  AI 思考中...





			** [Ollama API 交互](https://www.runoob.com/ollama-api.html)
			[Ollama Open WebUI](https://www.runoob.com/ollama-open-webui.html) **













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