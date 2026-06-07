# Markdown 引用块

- Source: https://www.runoob.com/markdown/md-block.html

引用块用于突出显示重要信息、引用他人观点或创建视觉层次。


### 单级引用的使用


基本语法：


Markdown 区块引用是在段落开头使用 **>** 符号 ，然后后面紧跟一个**空格**符号：


```
> 区块引用
> 菜鸟教程
> 学的不仅是技术更是梦想
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/DFE1124E-BC38-4C12-B7AC-053E560D4C9C.jpg)


多行引用：


```
> 这是引用的第一行。
> 这是引用的第二行。
>
> 这是引用的第二段。
```


**简化写法：**

只在第一行使用 **>** ，其余行会自动包含在引用中：


```
> 这是一个长引用，
包含多行内容，
只需要在第一行使用 > 符号。
```


![](https://www.runoob.com/wp-content/uploads/2019/03/6c8f7287-0fff-40a1-b475-82da417563d8.png)


### 多级嵌套引用


另外区块是可以嵌套的，一个 **>** 符号是最外层，两个** >** 符号是第一层嵌套，以此类推：


```
> 最外层
> > 第一层嵌套
> > > 第二层嵌套
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/AA0A4A6A-33A7-48C7-971F-73FFC8FE85B0.jpg)


实际应用示例：


```
> **用户反馈**：这个功能很有用！
>
> > **开发团队回复**：感谢您的反馈，我们会继续优化。
> >
> > > **项目经理补充**：预计下个版本会有更多改进。
```


![](https://www.runoob.com/wp-content/uploads/2019/03/7f8ec897-4c05-45fa-af0c-b04a01372df3.png)


### 区块中使用列表


区块中使用列表实例如下：


```
> 区块中使用列表
> 1. 第一项
> 2. 第二项
> + 第一项
> + 第二项
> + 第三项
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/E3BF6399-6483-4C7A-8502-AE75E8D66C96.jpg)


### 列表中使用区块


如果要在列表项目内放进区块，那么就需要在 **>** 前添加四个空格的缩进。


列表中使用区块实例如下：


```
* 第一项
    > 菜鸟教程
    > 学的不仅是技术更是梦想
* 第二项
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/1B894FB4-53AC-4E2D-BA30-F4AE4DFA8B97.jpg)

---


## 引用块内的其他元素

引用块内可以包含几乎所有其他 Markdown 元素。


**包含标题：**


```
> ## 重要提醒
>
> 请在操作前仔细阅读文档，避免数据丢失。
```


**包含列表：**


```
> ### 注意事项
>
> 1. 备份重要数据
> 2. 检查系统兼容性
> 3. 准备回滚方案
>
> - 测试环境验证
> - 生产环境部署
> - 监控系统状态
```


**包含代码：**


```
> 要运行这个脚本，请使用以下命令：
>
> ```bash
> npm install
> npm start
> ```
>
> 执行后会在 `http://localhost:3000` 看到结果。
```


**包含链接和图片：**


```
> &#x1f4da; **推荐阅读**
>
> 详细信息请参考 [官方文档](https://example.com)
>
> ![示例图片](./images/example.png)
```


### 引用的最佳实践

**名言警句引用**


```
> "在软件开发中，最昂贵的错误就是构建正确的系统错误的方式，或者构建错误的系统正确的方式。"
>
> — Barry Boehm，软件工程专家
```


### 重要信息提示

**成功提示：**


```
> &#x2705; **成功**
>
> 配置已保存并生效。系统将在下次重启时应用新设置。
```


**警告信息：**


```
> &#x26a0;&#xfe0f; **警告**
>
> 此操作不可逆转，请确保已备份重要数据。
```


**错误信息：**


```
> &#x274c; **错误**
>
> 连接数据库失败，请检查网络连接或联系系统管理员。
```


**信息提示：**


```
> &#x2139;&#xfe0f; **提示**
>
> 首次使用需要进行账户验证，验证邮件已发送到您的邮箱。
```


![](https://www.runoob.com/wp-content/uploads/2019/03/c6c2f2aa-f9a3-4f38-8e1c-6527c85e75f7.png)


### 文档结构中的引用


**章节摘要：**


```
# 第一章：项目概述

> **本章要点**
>
> - 了解项目背景和目标
> - 掌握核心功能特性
> - 熟悉技术架构设计
```


![](https://www.runoob.com/wp-content/uploads/2019/03/3d70e623-6dfa-43d2-9cf0-38686f61b251.png)


**版本更新说明：**


```
## v2.1.0 更新内容

> **重大变更**
>
> &#x26a0;&#xfe0f; API 接口路径已调整，旧版本客户端需要更新
>
> 详见 [迁移指南](./migration-guide.md)
```









	  AI 思考中...





			** [Markdown 列表](https://www.runoob.com/md-lists.html)
			[Markdown 代码](https://www.runoob.com/md-code.html) **













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