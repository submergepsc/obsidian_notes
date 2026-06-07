# XML CDATA

- Source: https://www.runoob.com/xml/xml-cdata.html

---


XML 文档中的所有文本均会被解析器解析。


只有 CDATA 区段中的文本会被解析器忽略。


---


## PCDATA - 被解析的字符数据


XML 解析器通常会解析 XML 文档中所有的文本。


当某个 XML 元素被解析时，其标签之间的文本也会被解析：


<message>**This text is also parsed**</message>


解析器之所以这么做是因为 XML 元素可包含其他元素，就像这个实例中，其中的  元素包含着另外的两个元素（first 和 last）：


<name><first>Bill</first><last>Gates</last></name>


而解析器会把它分解为像这样的子元素：


<name>**

   <first>Bill</first>


   <last>Gates</last>

</name>


解析字符数据（PCDATA）是 XML 解析器解析的文本数据使用的一个术语。


---


## CDATA - （未解析）字符数据


术语 CDATA 是不应该由 XML 解析器解析的文本数据。


像 "**" 结束：


<script>**
<![CDATA[

function matchwo(a,b)

{

if (a < b && a < 0) then


   {


   return 1;


   }

else


   {


   return 0;


   }

}

]]>

</script>

在上面的实例中，解析器会忽略 CDATA 部分中的所有内容。


关于 CDATA 部分的注释：**


CDATA 部分不能包含字符串 "]]>"。也不允许嵌套的 CDATA 部分。


标记 CDATA 部分结尾的 "]]>" 不能包含空格或换行。

**







	  AI 思考中...





			** [XML 命名空间](https://www.runoob.com/xml-namespaces.html)
			[XML 编码](https://www.runoob.com/xml-encoding.html) **













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

      : ·[XML 实例](https://www.runoob.com/xml-examples.html)

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