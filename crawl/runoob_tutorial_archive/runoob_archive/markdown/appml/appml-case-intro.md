# 案例研究 - 简介

- Source: https://www.runoob.com/appml/appml-case-intro.html

---


此案例研究演示了如何构建一个完整的  互联网应用程序，具有针对数据库中的若干表进行信息列举、编辑和搜索的功能。


---


## 我们将创建什么


我们将使用已有的数据库，名为 Demo。


对于数据库中的每个表，我们将：


- 创建原型模型
- 创建原型 HTML 页面
- 创建应用程序模型
- 创建 HTML 模板
- 创建完整的应用程序


---


## Demo 数据库


对于案例研究，我们使用 MS Office 预装的 Northwind 数据库的一个子集。


这个数据库是众所周知的，不论是使用 PHP 还是经典 ASP 抑或是 ASP.NET，都易于测试。


Demo 数据库包含了若干带有数据的表，如下所示：


## Customers


| Customer | Address | City | Country |
| --- | --- | --- | --- |
| Around the Horn | 120 Hanover Sq. | London | UK |
| Berglunds snabbkjøp | Berguvsvägen 8 | Luleå | Sweden |
| Blauer See Delikatessen | Forsterstr. 57 | Mannheim | Germany |
| Blondel père et fils | 24, place Kléber | Strasbourg | France |
| Bólido Comidas preparadas | C/ Araquil, 67 | Madrid | Spain |
| Bottom-Dollar Markets | 23 Tsawassen Blvd. | Tsawassen | Canada |

**


## Suppliers


| Supplier | Address | City | Country |
| --- | --- | --- | --- |
| Exotic Liquid | 49 Gilbert St. | London | UK |
| New Orleans Cajun Delights | P.O. Box 78934 | New Orleans | USA |
| Grandma Kelly's Homestead | 707 Oxford Rd. | Ann Arbor | USA |
| Tokyo Traders | 9-8 SekimaiMusashino-shi | Tokyo | Japan |
| Cooperativa de Quesos 'Las Cabras' | Calle del Rosal 4 | Oviedo | Spain |
| Mayumi's | 92 Setsuko Chuo-ku | Osaka | Japan |
| Pavlova, Ltd. | 74 Rose St. Moonie Ponds | Melbourne | Australia |
| Specialty Biscuits, Ltd. | 29 King's Way | Manchester | UK |
| PB Kn ckebr d AB | Kaloadagatan 13 | G teborg | Sweden |
| Refrescos Americanas LTDA | Av. das Americanas 12.890 | S o Paulo | Brazil |


## Products


| Produc | QuantityPerUnit | UnitPrice | UnitsInStock |
| --- | --- | --- | --- |
| Chai | 10 boxes x 20 bags | 18 | 39 |
| Chang | 24 - 12 oz bottles | 19 | 17 |
| Aniseed Syrup | 12 - 550 ml bottles | 10 | 13 |
| Chai | 10 boxes x 20 bags | 18 | 39 |
| Chef Anton's Gumbo Mix | 36 boxes | 21 | 0 |
| Grandma's Boysenberry Spread | 12 - 8 oz jars | 25 | 120 |
| Uncle Bob's Organic Dried Pears | 12 - 1 lb pkgs. | 30 | 15 |
| Northwoods Cranberry Sauce | 12 - 12 oz jars | 40 | 6 |
| Mishi Kobe Niku | 18 - 500 g pkgs. | 97 | 29 |
| Ikura | 12 - 200 ml jars | 31 | 31 |










	  AI 思考中...





			** [AppML 参考手册](https://www.runoob.com/appml-reference.html)
			[AppML 案例原型](https://www.runoob.com/appml-case-prototyping.html) **













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