# VBScript DateAdd 函数

- Source: https://www.runoob.com/vbscript/vb-func-dateadd.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


DateAdd 函数返回已添加指定时间间隔的日期。


### 语法


DateAdd(interval,number,date)


**
| 参数 | 描述 |
| --- | --- |
| interval | 必需。您想要添加的时间间隔。可采用下面的值： yyyy - 年 q - 季度 m - 月 y - 当年的第几天 d - 日 w - 当周的第几天 ww - 当年的第几周 h - 小时 n - 分 s - 秒 |
| number | 必需。需要添加的时间间隔的数目。可对未来的日期使用正值，对过去的日期使用负值。 |
| date | 必需。代表被添加的时间间隔的日期的变量或文字。 |


## 实例


## 实例 1


如何使用参数：


```
<script type="text/vbscript">
document.write(DateAdd("yyyy",1,"31-Jan-10") & "<br />")
document.write(DateAdd("q",1,"31-Jan-10") & "<br />")
document.write(DateAdd("m",1,"31-Jan-10") & "<br />")
document.write(DateAdd("y",1,"31-Jan-10") & "<br />")
document.write(DateAdd("d",1,"31-Jan-10") & "<br />")
document.write(DateAdd("w",1,"31-Jan-10") & "<br />")
document.write(DateAdd("ww",1,"31-Jan-10") & "<br />")
document.write(DateAdd("h",1,"31-Jan-10 08:50:00") & "<br />")
document.write(DateAdd("n",1,"31-Jan-10 08:50:00") & "<br />")
document.write(DateAdd("s",1,"31-Jan-10 08:50:00") & "<br />")
</script>
```


以上实例输出结果：


```
1/31/2011
4/30/2010
2/28/2010
2/1/2010
2/1/2010
2/1/2010
2/7/2010
1/31/2010 9:50:00 AM
1/31/2010 8:51:00 AM
1/31/2010 8:50:01 AM
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_dateadd_func)


## 实例 2


从 2001 年 1 月 31 日减去一个月：


```
<script type="text/vbscript">
document.write(DateAdd("m",-1,"31-Jan-10"))
</script>
```


以上实例输出结果：


```
12/31/2009
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_dateadd_func2)


## 实例 3


从现在添加一天：


```
<script type="text/vbscript">
document.write(DateAdd("d",1,Now()))
</script>
```


以上实例输出结果：


```
document.write(DateAdd("d",1,Now()))
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_dateadd_func3)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript Date 函数](https://www.runoob.com/vb-func-date.html)
			[VBScript DateDiff 函数](https://www.runoob.com/vb-func-datediff.html) **













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