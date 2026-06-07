# Markdown 文本格式

- Source: https://www.runoob.com/markdown/md-paragraph.html

Markdown 段落没有特殊的格式，直接编写文字就好，**段落的换行是使用两个以上空格加上回车**。


![](https://www.runoob.com/wp-content/uploads/2019/03/36A89BDA-A062-4D66-A41B-0EBEE7891AB9.jpg)


当然也可以在段落后面使用一个空行来表示重新开始一个段落。


![](https://www.runoob.com/wp-content/uploads/2019/03/3F254936-778E-417A-BEF2-467116A55D00.jpg)


---


## 字体

文本强调是写作中的重要技巧，Markdown 提供了简洁的方式来实现粗体和斜体效果。


Markdown 可以使用以下几种字体：粗体和斜体。


**粗体语法：**使用两个星号 ****** 或两个下划线 **__** 包围文字：


```
这是**粗体文字**使用星号
这是__粗体文字__使用下划线
```


**斜体语法：**使用一个星号 ***** 或一个下划线 **_** 包围文字：


```
这是*斜体文字*使用星号
这是_斜体文字_使用下划线
```


**粗斜体组合：**使用三个星号 ******* 或三个下划线 **___**。


```
*斜体文本*
_斜体文本_
**粗体文本**
__粗体文本__
***粗斜体文本***
___粗斜体文本___
```


显示效果如下所示：


![](https://www.runoob.com/wp-content/uploads/2019/03/md3.gif)


**混合使用技巧：**


```
这段文字包含**粗体**、*斜体*和***粗斜体***的组合效果。
```


渲染效果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/496aecf3-2e95-4a93-84ca-5627a338a84b.png)


**使用建议**：


- 推荐使用星号 `*****` 而不是下划线 `**_**`，因为星号在各种 Markdown 解析器中兼容性更好
- 不要过度使用强调，重点突出才有效果
- 在中英文混合时，建议在强调符号前后加空格以提高可读性


---


## 分隔线


你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：


```
***

* * *

*****

- - -

----------
```


显示效果如下所示：


![](https://www.runoob.com/wp-content/uploads/2019/03/3F46EAA9-DADE-48FD-99AA-DF7BEBFAA4FA.jpg)


---


## 删除线


如果段落上的文字要添加删除线，只需要在文字的两端加上两个波浪线 **~~** 即可，实例如下：


```
RUNOOB.COM
GOOGLE.COM
~~BAIDU.COM~~
```


显示效果如下所示：


![](https://www.runoob.com/wp-content/uploads/2019/03/B5270A31-15D0-410B-AE1D-B9655B8F331C.jpg)


---


## 下划线


下划线可以通过 HTML 的 **** 标签来实现：


```
<u>带下划线文本</u>
```


显示效果如下所示：


![](https://www.runoob.com/wp-content/uploads/2019/03/05A27273-B66D-43DE-A3DB-0D32FF024093.jpg)


---


## 脚注


脚注是对文本的补充说明。


Markdown 脚注的格式如下:


```
[^要注明的文本]
```


以下实例演示了脚注的用法：


```
创建脚注格式类似这样 [^RUNOOB]。

[^RUNOOB]: 菜鸟教程 -- 学的不仅是技术，更是梦想！！！
```


演示效果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/md5.gif)


---


## 行内代码标记


行内代码用于在正文中标记代码片段、命令、变量名等：


**基本语法**：**使用一个反引号 **`** 包围代码：


```
使用 `git commit` 命令提交代码
变量 `userName` 存储用户名
在终端中输入 `npm install` 安装依赖
```


渲染效果：


![](https://www.runoob.com/wp-content/uploads/2019/03/640ad406-9653-4cc7-bdc1-338a4730941e.png)


包含反引号的代码：**当代码本身包含反引号时，使用两个反引号包围。


```
要显示反引号，使用 `` `code` `` 这样的格式
```


渲染效果：


![](https://www.runoob.com/wp-content/uploads/2019/03/8e4a61c7-1cdb-4040-8fce-ff0f3084941c.png)


**应用场景**：


- 技术文档中的 API 名称、函数名
- 配置文件中的参数名
- 命令行指令
- 键盘快捷键（如 `Ctrl+C`）

---


## 文本高亮（扩展语法）


文本高亮不是标准 Markdown 语法，但许多扩展支持：


**常见语法**（部分平台支持）：


```
这是==高亮文本==
```


**HTML 替代方案**：


```
这是<mark>高亮文本</mark>
```


![](https://www.runoob.com/wp-content/uploads/2019/03/95218e18-da76-4a3d-be5a-e209c96e925e.png)


---


## 段落和换行

### 段落的创建方法


在 Markdown 中，段落是文本的基本单位，理解段落规则对于正确格式化文档至关重要。


**段落基本规则**：


- 段落由一个或多个连续的文本行组成
- 段落之间由一个或多个空行分隔
- 普通段落不应该用空格或制表符缩进


**正确的段落写法**：


```
这是第一个段落。它可以包含多个句子，内容可以很长，会自动换行显示。

这是第二个段落。注意上面有一个空行分隔。

这是第三个段落。
```


![](https://www.runoob.com/wp-content/uploads/2019/03/11c1ffe7-d09a-4bad-9fd2-150a38eab091.png)


**常见错误**：


```
这是第一段
这是第二段（错误：没有空行分隔）

    这是缩进段落（错误：不应该缩进）
```


![](https://www.runoob.com/wp-content/uploads/2019/03/5b49fe95-3ccd-4f43-9c17-0614288e8e68.png)


### 强制换行技巧


有时需要在不创建新段落的情况下换行，Markdown 提供了几种方法：


**方法一：行尾两个空格****在行尾添加两个或更多空格，然后按回车：


```
第一行内容（这里有两个空格）
第二行内容
```


方法二：HTML 换行标签**


```
第一行内容<br>
第二行内容
```


**方法三：反斜杠（部分解析器支持）**


```
第一行内容\
第二行内容
```


**实际应用示例**：


```
地址：北京市朝阳区
电话：010-12345678
邮箱：[email protected]

诗歌示例：
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
```


![](https://www.runoob.com/wp-content/uploads/2019/03/b4bf6043-c14c-482b-b50e-db65bf4a76db.png)


### 空行的作用


空行在 Markdown 中扮演重要角色：


**分隔段落**：


```
第一段内容

第二段内容
```


**分隔不同元素**：


```
# 标题

段落内容

- 列表项1
- 列表项2

另一段内容
```


**最佳实践建议**：


- 在标题和内容之间留空行
- 在列表前后留空行
- 在代码块前后留空行
- 保持一致的空行使用习惯








	  AI 思考中...





			** [Markdown 标题](https://www.runoob.com/md-title.html)
			[Markdown 列表](https://www.runoob.com/md-lists.html) **













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