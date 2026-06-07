# Token (词元)

- Source: https://www.runoob.com/ai-agent/token-intro.html

**
你有没有好奇过，当你向 Deepseek、豆包、千问、ChatGPT 或 Claude 提问时，AI 是怎么读懂你的文字的？


答案的核心，就是一个叫做 **Token**，中文称之为 **词元**的概念。理解 Token，是走进 AI 世界的第一步。



### 什么是 Token (词元)？


```
Token (词元) = AI 能理解的最小文本单位
```


我们可以把它理解成：AI 世界里的文字碎片或者 AI 世界的燃料。


就像人类阅读时以词语为单位来理解意思，AI 也不会逐个字母地处理文字——它会先把文本切割成一块一块的碎片，每一块就叫做一个 Token（词元）。













          INPUT TEXT



          "ChatGPT is amazing"




TOKENS Chat G PT is amaz ing 共 6 个 Token 一个好用的比喻：**


把一篇文章想象成一块比萨，你不会整块吞下去，也不会把它碾成粉末——而是切成一块一块，每块就是一个 Token。AI 就是这样吃进文字的：切块、理解、消化。


Token 比单词更细，比字母更粗，是一种灵活的中间单位。


---


## Token 长什么样？

不同的文本，切分方式大相径庭。

常见词是一个 Token，复杂词会被拆开，标点也算 Token。









        英文句子
        "Hello, world!"

          Hello
          →
          ,
          →
           world
          →
          !

        共 4 个 Token




        复杂英文单词
        "unbelievable"

          un
          believ
          able

        共 3 个 Token  —— 长词会被拆分




        中文句子
        "你好，世界！"

          你好
          ，
          世界
          ！

        共 4 个 Token  —— 中文每字约消耗更多 Token






---


## Token 和 字、 词 有什么区别？


很多人会以为 Token = 单词，但其实**并不完全是**。


Token 的划分遵循一套特殊的算法（比如 BPE，字节对编码），结果有时候很直觉，有时候却出人意料：


| 文本 | Token 数量 | 说明 |
| --- | --- | --- |
| cat | 1 | 常见词，直接一个 Token |
| unbelievable | 4 | un + believ + able + … |
| ChatGPT | 3 | Chat + G + PT |
| 你好 | 约 2～3 | 中文通常比英文消耗更多 Token |


**
结论：** Token 比单词更细，比字母更粗，是一种灵活的中间单位。




          最细粒度

### 字符 / 字母



          粒度
          单个字母或汉字


          示例
          H, e, l, l, o


          AI 是否使用
          ❌ 太细，信息密度低


          类比
          把比萨碾成粉末





          ✦ AI 实际使用

### Token（词元）



          粒度
          词根、短词、字符组合


          示例
          Hello / Chat·G·PT / un·believ·able


          AI 是否使用
          ✅ 高效，平衡信息密度


          类比
          把比萨切成合适的一口大小





          最粗粒度

### 单词 / 句子



          粒度
          完整单词或句子


          示例
          Hello, unbelievable


          AI 是否使用
          ❌ 太粗，处理不灵活


          类比
          整块比萨一口塞进去




---


## Token 为什么重要？


### 1. 它决定了 AI 能读多少


每个 AI 模型都有一个 **上下文窗口（Context Window）**，也就是它一次能处理的最大 Token 数量。比如：


- GPT-3.5：约 4,000 Token
- GPT-4 Turbo：约 128,000 Token
- Claude 3.5：约 200,000 Token


超过这个限制，AI 就会记不住之前说的话，就像一个人的短期记忆装满了一样。


### 2. 它影响 API 的使用费用


调用 AI 接口（API）时，费用通常按 Token 数量计费。**输入的文字 + AI 回复的文字**，都会消耗 Token，所以写得越长，花费越多。


### 3. 它影响 AI 的回复速度


AI 生成文字时，是**一个 Token 一个 Token 地输出**的，所以回复越长，等待时间越久。


---


## Token 的小知识


- **1,000 个 Token ≈ 750 个英文单词**，是一个常用的估算比例。
- **中文、日文、韩文**等亚洲语言通常比英文消耗更多 Token，因为这些字符在编码上更复杂。
- **空格和标点**也算 Token！不要以为只有文字才计数。
- **代码**的 Token 消耗一般比自然语言少，因为编程语言结构紧凑。


---


## 总结


| 概念 | 一句话解释 |
| --- | --- |
| Token | AI 处理文本的最小单位，介于字符和单词之间 |
| 上下文窗口 | AI 一次能处理的最大 Token 数 |
| Token 计费 | API 调用按输入+输出的 Token 总量收费 |
| Token 生成 | AI 回复是逐 Token 产生的，越长越慢 |










	  AI 思考中...





			** [TRAE 教程](https://www.runoob.com/trae-quick-star.html)
			[LangGraph 入门教程](https://www.runoob.com/langgraph-quick-start.html) **













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