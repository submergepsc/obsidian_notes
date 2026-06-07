# Ollama API 交互

- Source: https://www.runoob.com/ollama/ollama-api.html

Ollama 提供了基于 HTTP 的 API，允许开发者通过编程方式与模型进行交互。

本文将详细介绍 Ollama API 的详细使用方法，包括请求格式、响应格式以及示例代码。


---


## 1. 启动 Ollama 服务

在使用 API 之前，需要确保 Ollama 服务正在运行。可以通过以下命令启动服务：


```
ollama serve
```


默认情况下，服务会运行在 **http://localhost:11434**。


---


## 2. API 端点

Ollama 提供了以下主要 API 端点：


生成文本（Generate Text）


- **端点**：`POST /api/generate`
- **功能**：向模型发送提示词（prompt），并获取生成的文本。
- **请求格式**：
```
{
  "model": "<model-name>",  // 模型名称
  "prompt": "<input-text>", // 输入的提示词
  "stream": false,          // 是否启用流式响应（默认 false）
  "options": {              // 可选参数
    "temperature": 0.7,     // 温度参数
    "max_tokens": 100       // 最大 token 数
  }
}
```

- **响应格式**：
```
{
  "response": "<generated-text>", // 生成的文本
  "done": true                    // 是否完成
}
```


### 聊天（Chat）


- **端点**：`POST /api/chat`
- **功能**：支持多轮对话，模型会记住上下文。
- **请求格式**：
```
{
  "model": "<model-name>",  // 模型名称
  "messages": [             // 消息列表
    {
      "role": "user",       // 用户角色
      "content": "<input-text>" // 用户输入
    }
  ],
  "stream": false,          // 是否启用流式响应
  "options": {              // 可选参数
    "temperature": 0.7,
    "max_tokens": 100
  }
}
```

- **响应格式**：
```
{
  "message": {
    "role": "assistant",    // 助手角色
    "content": "<generated-text>" // 生成的文本
  },
  "done": true
}
```


### 列出本地模型（List Models）


- **端点**：`GET /api/tags`
- **功能**：列出本地已下载的模型。
- **响应格式**：
```
{
  "models": [
    {
      "name": "<model-name>", // 模型名称
      "size": "<model-size>", // 模型大小
      "modified_at": "<timestamp>" // 修改时间
    }
  ]
}
```


### 拉取模型（Pull Model）


- **端点**：`POST /api/pull`
- **功能**：从模型库中拉取模型。
- **请求格式**：
```
{
  "name": "<model-name>" // 模型名称
}
```

- **响应格式**：
```
{
  "status": "downloading", // 下载状态
  "digest": "<model-digest>" // 模型摘要
}
```


---


## 3. 使用示例


### 生成文本

使用 curl 发送请求：


## 实例


```
curl http://localhost:11434/api/generate -d '{
  "model": "deepseek-coder",
  "prompt": "你好，你能帮我写一段代码吗？",
  "stream": false
}'
```


### 多轮对话

使用 curl 发送请求：


## 实例


```
curl http://localhost:11434/api/chat -d '{
  "model": "deepseek-coder",
  "messages": [
    {
      "role": "user",
      "content": "你好，你能帮我写一段 Python 代码吗？"
    }
  ],
  "stream": false
}'
```


### 列出本地模型

使用 curl 发送请求：


```
curl http://localhost:11434/api/tags
```


### 拉取模型

使用 curl 发送请求：


## 实例


```
curl http://localhost:11434/api/pull -d '{
  "name": "deepseek-coder"
}'
```


---


## 4. 流式响应

Ollama 支持流式响应（streaming response），适用于实时生成文本的场景。


### 启用流式响应

在请求中设置 **"stream": true**，API 会逐行返回生成的文本。


## 实例


```
curl http://localhost:11434/api/generate -d '{
  "model": "deepseek-coder",
  "prompt": "你好，你能帮我写一段代码吗？",
  "stream": true
}'
```


### 响应格式

每行返回一个 JSON 对象：


## 实例


```
{
  "response": "<partial-text>", // 部分生成的文本
  "done": false                 // 是否完成
}
```


---


## 5. 编程语言示例


Python 使用 requests 库与 Ollama API 交互：


## 实例


```
import requests

# 生成文本
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "deepseek-coder",
        "prompt": "你好，你能帮我写一段代码吗？",
        "stream": False
    }
)
print(response.json())
```


多轮对话:


## 实例


```
response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "deepseek-coder",
        "messages": [
            {
                "role": "user",
                "content": "你好，你能帮我写一段 Python 代码吗？"
            }
        ],
        "stream": False
    }
)
print(response.json())
```


JavaScript 使用 fetch API 与 Ollama 交互：


## 实例


```
// 生成文本
fetch("http://localhost:11434/api/generate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "deepseek-coder",
    prompt: "你好，你能帮我写一段代码吗？",
    stream: false
  })
})
  .then(response => response.json())
  .then(data => console.log(data));
```


多轮对话:


## 实例


```
fetch("http://localhost:11434/api/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "deepseek-coder",
    messages: [
      {
        role: "user",
        content: "你好，你能帮我写一段 Python 代码吗？"
      }
    ],
    stream: false
  })
})
  .then(response => response.json())
  .then(data => console.log(data));
```









	  AI 思考中...





			** [Ollama 模型交互](https://www.runoob.com/ollama-cli.html)
			[Ollama Python 使用](https://www.runoob.com/ollama-python-sdk.html) **













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