# 教程

- Source: https://www.runoob.com/appml/appml-tutorial.html

---


|  | # # 快速和简单的 # Web 开发 |
| --- | --- |


---


## 什么是 ?


 appML是一个为web应用程序设计的HTML扩展框:


- XML 语言定义了应用的模型
- JavaScript 运行于客户端浏览器上
- PHP 或者 ASP 脚本运行于服务器上


AppML 是应用模式语言（ **A**pplication **M**odeling **L**anguage）。


---


## 学习非常简单


- 超级简单的模型
- 超级简单的属性
- 超级简单的应用开发
- 运行于任何平台及任何浏览器
- 安装简单


---


## 只有 HTML, JavaScript, 和 XML


 只需要在HTML页面中包含 JavaScript，然后再服务端上存储 XML 数据：


## HTML 页面:


```
<h1>My First Web Application</h1>
	<div id="Place01"><table id="Template01"
class="appmltable"><tr>  <th>Customer</th>  <th>City</th>
 <th>Country</th></tr><tr id="appml_row">  <td>#CustomerName#</td>
 <td>#City#</td>  <td>#Country#</td></tr></table>
	</div>
<script src="appml.js"></script>
<script>
app=new AppML("appml.htmlx","Models/Customers");
app.run("Place01","Template01");
</script>
```


**
## XML :


```
<appml>
<datasource>
<database>
  <connection>Demo</connection>
  <sql>SELECT CustomerName,City,Country FROM Customers</sql>
</database>
</datasource>
</appml>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryappml_tut_03)


如果你之前已经学习了web开发，你会发现  使用非常简单。


如果你之前学习过 PHP, ASP, 或者 ASP.NET的开发, 你会清楚的看到使用  的好处。


---


## 现代 Web 架构


 是一个结合了最新的技术和现代web开发想法，使用低消耗高速简单的架构：


- 采用 MVC 架构
- 极低的带宽消耗
- 云计算的优化
- 内容完全分离
- 智能，灵活，快速的Web开发
- 高度的可扩展性和可测试性
- 简单的配置和重新配置
- 智能支持用户账号和角色


---


## 历史


1999年，Refsnes Data公司开始研发AppML,一种基于XML、用来定义Internet应用程序的语言。2000年9月，一个为了挪威手球联盟而进行的大型项目开始，其目的是想通过仅仅使用AppML将一个巨大的信息系统从旧的DOS环境转换到现代的Internet上。而这个主要的项目刚刚取得了巨大的成功。据开发者估计，和传统的Web开发相比，这次的开发时间被缩短了高达75%。


在2007年九月中旬，AppML内容实现脱机使用，因为它支持ASP和IE。


在2013年十月，AppML宣布，作为一个开放源代码的产品，在PHP、ASP.NET版本中兼容 所有的浏览器。


AppML在1999年最初的设计目标:


- AppML 应用必须运行于是有网络
- AppML 应用应具有平台独立性
- AppML 应用必须使用互联网标准 (HTTP, HTML, CSS, XML)
- AppML 应用必须支持各种应用的需求
- AppML 应用必需是自描述
- AppML 应用程序必须易于开发，维护和修改
- AppML 应用程序必须面向未来








	  AI 思考中...






			[如何使用 AppML](https://www.runoob.com/appml-howto.html) **













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