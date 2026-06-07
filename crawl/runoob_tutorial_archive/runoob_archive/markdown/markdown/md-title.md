# Markdown 标题

- Source: https://www.runoob.com/markdown/md-title.html

Markdown 标题有两种格式。


### 1、使用 = 和 - 标记一级和二级标题


= 和 - 标记语法格式如下：


```
我展示的是一级标题
=================

我展示的是二级标题
-----------------
```


显示效果如下图：


![](https://www.runoob.com/wp-content/uploads/2019/03/01986C87-7E19-4497-878E-AE996AFC088E.jpg)


### 使用 # 号标记


Markdown 使用 `**#**` 号来创建标题，这是从 HTML 的 `` 到 `` 标签概念演化而来的。


使用 **#** 号可表示 1-6 级标题，一级标题对应一个 **#** 号，二级标题对应两个 **#** 号，以此类推。


```
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```


显示效果如下图：


![](https://www.runoob.com/wp-content/uploads/2019/03/md2.gif)


**重要注意事项**：


*符号与文字间的空格*：`#` 号和标题文字之间必须有一个空格。这是标准的 Markdown 语法要求。


```
# 正确写法
#错误写法
```


*行首位置*：`#` 号必须在行首，前面不能有其他字符（空格或制表符）。


*唯一的一级标题*：在一个文档中，通常只使用一个一级标题作为文档的主标题，这符合良好的文档结构规范。


### 标题的嵌套结构


标题的层次结构应该遵循逻辑顺序，不应该跳级使用。良好的标题结构就像一本书的目录：


**推荐的层次结构**：


```
# 主题：人工智能概述

## 第一部分：基础概念
### 什么是人工智能
### 发展历史
#### 早期发展（1950-1980）
#### 现代发展（1980至今）

## 第二部分：应用领域
### 自然语言处理
### 计算机视觉
### 机器学习
#### 监督学习
#### 无监督学习
#### 强化学习
```


**避免的错误结构**：


```
# 主标题
### 直接跳到三级标题（不推荐）
## 然后才是二级标题
```


### 标题编号的最佳实践


**自动编号 vs 手动编号**：


许多 Markdown 处理器和编辑器支持自动生成标题编号，因此在源码中通常不需要手动添加编号：


```
# 引言
## 背景
## 目标
# 方法论
## 数据收集
## 分析方法
```


**标题锚点**：


大多数 Markdown 处理器会自动为标题创建锚点（anchor），便于页面内跳转：


```
[跳转到方法论部分](#方法论)
```


**标题长度建议**：


- 保持标题简洁明了，一般不超过 10 个汉字或 20 个英文字符
- 使用描述性词语，避免模糊的标题如"其他"、"杂项"
- 可以使用冒号来分隔主题和副主题








	  AI 思考中...





			** [Markdown 教程](https://www.runoob.com/md-tutorial.html)
			[Markdown 文本格式](https://www.runoob.com/md-paragraph.html) **













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