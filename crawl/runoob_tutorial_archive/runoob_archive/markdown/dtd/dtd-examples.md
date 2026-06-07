# DTD - 来自网络的实例

- Source: https://www.runoob.com/dtd/dtd-examples.html

---


## 电视节目表 DTD


由 David Moisan 创造。拷贝自： [http://www.davidmoisan.org/](http://www.davidmoisan.org/)




<!DOCTYPE TVSCHEDULE [**

<!ELEMENT TVSCHEDULE (CHANNEL+)>

<!ELEMENT CHANNEL (BANNER,DAY+)>

<!ELEMENT BANNER (#PCDATA)>

<!ELEMENT DAY (DATE,(HOLIDAY|PROGRAMSLOT+)+)>

<!ELEMENT HOLIDAY (#PCDATA)>

<!ELEMENT DATE (#PCDATA)>

<!ELEMENT PROGRAMSLOT (TIME,TITLE,DESCRIPTION?)>

<!ELEMENT TIME (#PCDATA)>

<!ELEMENT TITLE (#PCDATA)>

<!ELEMENT DESCRIPTION (#PCDATA)>


<!ATTLIST TVSCHEDULE NAME CDATA #REQUIRED>

<!ATTLIST CHANNEL CHAN CDATA #REQUIRED>

<!ATTLIST PROGRAMSLOT VTR CDATA #IMPLIED>

<!ATTLIST TITLE RATING CDATA #IMPLIED>

<!ATTLIST TITLE LANGUAGE CDATA #IMPLIED>

]>



---


## 报纸文章 DTD


拷贝自：[http://www.vervet.com/](http://www.vervet.com/)




<!DOCTYPE NEWSPAPER [


<!ELEMENT NEWSPAPER (ARTICLE+)>

<!ELEMENT ARTICLE (HEADLINE,BYLINE,LEAD,BODY,NOTES)>

<!ELEMENT HEADLINE (#PCDATA)>

<!ELEMENT BYLINE (#PCDATA)>

<!ELEMENT LEAD (#PCDATA)>

<!ELEMENT BODY (#PCDATA)>

<!ELEMENT NOTES (#PCDATA)>


<!ATTLIST ARTICLE AUTHOR CDATA #REQUIRED>

<!ATTLIST ARTICLE EDITOR CDATA #IMPLIED>

<!ATTLIST ARTICLE DATE CDATA #IMPLIED>

<!ATTLIST ARTICLE EDITION CDATA #IMPLIED>


<!ENTITY NEWSPAPER "Vervet Logic Times">

<!ENTITY PUBLISHER "Vervet Logic Press">

<!ENTITY COPYRIGHT "Copyright 1998 Vervet Logic Press">


]>


---


## 产品目录 DTD


拷贝自： [http://www.vervet.com/](http://www.vervet.com/)



<!DOCTYPE CATALOG [


<!ENTITY AUTHOR "John Doe">

<!ENTITY COMPANY "JD Power Tools, Inc.">

<!ENTITY EMAIL "[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)">


<!ELEMENT CATALOG (PRODUCT+)>


<!ELEMENT PRODUCT

(SPECIFICATIONS+,OPTIONS?,PRICE+,NOTES?)>

<!ATTLIST PRODUCT

NAME CDATA #IMPLIED

CATEGORY (HandTool|Table|Shop-Professional) "HandTool"

PARTNUM CDATA #IMPLIED

PLANT (Pittsburgh|Milwaukee|Chicago) "Chicago"

INVENTORY (InStock|Backordered|Discontinued) "InStock">


<!ELEMENT SPECIFICATIONS (#PCDATA)>

<!ATTLIST SPECIFICATIONS

WEIGHT CDATA #IMPLIED

POWER CDATA #IMPLIED>


<!ELEMENT OPTIONS (#PCDATA)>

<!ATTLIST OPTIONS

FINISH (Metal|Polished|Matte) "Matte"

ADAPTER (Included|Optional|NotApplicable) "Included"

CASE (HardShell|Soft|NotApplicable) "HardShell">


<!ELEMENT PRICE (#PCDATA)>

<!ATTLIST PRICE

MSRP CDATA #IMPLIED

WHOLESALE CDATA #IMPLIED

STREET CDATA #IMPLIED

SHIPPING CDATA #IMPLIED>


<!ELEMENT NOTES (#PCDATA)>


]>










	  AI 思考中...





			** [DTD 教程](https://www.runoob.com/dtd-tutorial.html)
			[DTD 简介](https://www.runoob.com/dtd-intro.html) **













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