# Markdown 链接

- Source: https://www.runoob.com/markdown/md-link.html

链接是使 Markdown 文档具有交互性的关键元素。

掌握链接语法能让你创建内容丰富、易于导航的文档。


链接使用方法如下：


```
[链接名称](链接地址)
[链接文字](链接地址 "可选的标题")
```


或者:


```
<链接地址>
```


一个简单的链接：


```
这是一个链接 [菜鸟教程](https://www.runoob.com)
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/49E6CB42-F780-4DA6-8290-DC757B51FB9A.jpg)


直接使用链接地址：


```
<https://www.runoob.com>
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/9BFF60A1-DD71-4B63-987B-4665B31C7787.jpg)


设置可选标题：


```
这是一个链接 [菜鸟教程](https://www.runoob.com)
欢迎访问 [GitHub](https://github.com) 官网
这是 [百度搜索](https://www.baidu.com "百度一下，你就知道")
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/970c6f7d-308f-498b-901d-c08b0e9a112f.png)


** 链接标题的作用：**


- 当鼠标悬停在链接上时显示提示信息
- 对搜索引擎优化和无障碍访问有帮助
- 标题文字放在双引号、单引号或括号中都可以


邮箱链接：


```
markdown联系我：[发送邮件](mailto:[email protected])
电话联系：[拨打电话](tel:+86-138-0013-8000)
```


### 参考链接


参考式链接将链接定义与使用分离，让文档更整洁，特别适合长文档或需要多次引用相同链接的情况。


基本语法：


```
markdown[链接文字][参考标签]

[参考标签]: URL "可选标题"
```


我们可以通过变量来设置一个链接，变量赋值在文档末尾进行：


```
这个链接用 1 作为网址变量 [Google][1]
这个链接用 runoob 作为网址变量 [Runoob][runoob]
然后在文档的结尾为变量赋值（网址）

  [1]: http://www.google.com/
  [runoob]: http://www.runoob.com/
```


显示结果如下：


![](https://www.runoob.com/wp-content/uploads/2019/03/EC3ED5D2-4F0D-492A-81B3-D485623D1A9E.jpg)


**简化写法：**

当参考标签与链接文字相同时，可以省略第二个方括号：


```
markdown 我喜欢使用 [GitHub][] 来管理代码。

[GitHub]: https://github.com
```


**参考链接的优势：**


- 文档正文更清爽，不被长 URL 打断
- 便于链接的统一管理和更新
- 相同链接可以重复使用，避免重复定义
- 链接定义可以放在文档任意位置（通常放在末尾）


**组织技巧：**


```
markdown# 学习资源推荐

## 在线教程
- [MDN Web Docs][mdn] - 权威的 Web 技术文档
- [RUNOOB][rnb] - 适合初学者的教程网站
- [freeCodeCamp][fcc] - 免费的编程学习平台

## 代码托管
- [GitHub][github] - 最受欢迎的代码托管服务
- [GitLab][gitlab] - 企业级的代码管理平台

<!-- 链接定义区域 -->
[mdn]: https://developer.mozilla.org/
[rnb]: https://www.runoob.com/
[fcc]: https://www.freecodecamp.org/
[github]: https://github.com/
[gitlab]: https://gitlab.com/
```


![](https://www.runoob.com/wp-content/uploads/2019/03/62f0c8a9-3a98-49e1-818b-ae7e380ace6b.png)


### 自动链接识别

现代 Markdown 解析器通常支持自动识别 URL 和邮箱地址：


URL 自动识别：


```
markdown直接输入网址：https://www.example.com
用尖括号包围：<https://www.example.com>
```


邮箱自动识别：


```
markdown联系邮箱：[email protected]
或者：<[email protected]>
```


** 注意事项：**


- 自动识别功能依赖于具体的 Markdown 解析器
- 为了确保兼容性，建议使用标准的链接语法
- 某些特殊字符可能影响自动识别


### 锚点链接的使用

锚点链接用于在同一文档内跳转，特别适合长文档的导航：

跳转到标题：


```
## 目录
- [第一章：介绍](#第一章介绍)
- [第二章：安装](#第二章安装)
- [第三章：使用方法](#第三章使用方法)

# 第一章：介绍
这里是介绍内容...

# 第二章：安装
这里是安装说明...

# 第三章：使用方法
这里是使用说明...
```


![](https://www.runoob.com/wp-content/uploads/2019/03/168d1b90-c15c-42c4-8ba0-586e82eda749.png)


**锚点规则：**


- 标题会自动生成锚点
- 锚点名称通常是标题的小写形式
- 空格替换为连字符
- 移除特殊字符


** 手动创建锚点：**


```
<a id="custom-anchor"></a>
## 自定义锚点位置

[跳转到自定义位置](#custom-anchor)
```


页面顶部返回链接：


```
[回到顶部](#)
```










	  AI 思考中...





			** [Markdown 代码](https://www.runoob.com/md-code.html)
			[Markdown 图片](https://www.runoob.com/md-image.html) **













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