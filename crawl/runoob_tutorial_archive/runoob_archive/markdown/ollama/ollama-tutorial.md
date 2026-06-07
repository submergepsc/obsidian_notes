# Ollama 教程

- Source: https://www.runoob.com/ollama/ollama-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/02/bala-ollama.webp)


Ollama 是一个开源的本地大语言模型运行框架，专为在本地机器上便捷部署和运行大型语言模型（LLM）而设计。


Ollama 支持多种操作系统，包括 macOS、Windows、Linux 以及通过 Docker 容器运行。

Ollama 提供对模型量化的支持，可以显著降低显存要求，使得在普通家用计算机上运行大型模型成为可能。


---


## 谁适合阅读本教程？

Ollama 适用于开发者、研究人员以及对数据隐私有较高要求的用户，它可以帮助用户在本地环境中快速部署和运行大型语言模型，同时提供灵活的定制化选项。


使用 Ollama，我们可以在在本地运行 Llama 3.3、DeepSeek-R1、Phi-4、Mistral、Gemma 2 和其他模型。


---


## 学习本教程前你需要了解


本教程适合有 Python 基础的开发者学习，如果不了解 Python 可以查阅 [Python 3.x 基础教程](https://www.runoob.com/../python3/python3-tutorial.html)。


理解 Docker 镜像和容器的区别，知道如何从 Docker Hub 拉取镜像并运行容器，docker 相关内容参见： [Docker 教程](https://www.runoob.com/../docker/docker-tutorial.html)。


熟悉命令行工具（如终端或命令提示符）的基本操作，例如文件和目录的创建、删除、移动，以及如何运行脚本和程序。


---


## 创建新的模型

我们可以使用 **ollama create** 命令从 Modelfile 创建模型：


## 实例


```
ollama create model -of ./Modelfile
```


---


## 相关链接

Ollama 官方地址：[https://ollama.com/](https://ollama.com/)

Github 开源地址：[https://github.com/ollama/ollama](https://github.com/ollama/ollama)

Ollama 官方文档：[https://github.com/ollama/ollama/tree/main/docs](https://github.com/ollama/ollama/tree/main/docs)








	  AI 思考中...






			[Ollama 简介](https://www.runoob.com/ollama-intro.html) **













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