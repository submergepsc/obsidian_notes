# VBScript Filter 函数

- Source: https://www.runoob.com/vbscript/func-filter.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


Filter 函数返回一个基于 0 的数组，此数组包含以特定过滤条件为基础的字符串数组的子集。


**注意：**如果找不到与 value 参数相匹配的值，Filter 函数会返回一个空数组。


**注意：**如果参数 inputstrings 为 Null 或者不是一维数组，则会发生错误。


### 语法


Filter(inputstrings,value[,include[,compare]])


**
| 参数 | 描述 |
| --- | --- |
| inputstrings | 必需。要检索的一维字符串数组。 |
| value | 必需。要搜索的字符串。 |
| include | 可选。Boolean 值，指定返回的子字符串是否包含 Value。如果 Include 为 True，Filter 将返回包含子字符串 Value 的数组子集。如果 Include 为 False，Filter 将返回不包含子字符串 Value 的数组子集。默认值为 True。 |
| compare | 可选。规定要使用的字符串比较类型。可采用下列的值： 0 = vbBinaryCompare - 执行二进制比较 1 = vbTextCompare - 执行文本比较 |


## 实例


## 实例 1


Filter：项目包含的 "S"：


```
<script type="text/vbscript">
a=Array("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
b=Filter(a,"S")
for each x in b
    document.write(x & "<br />")
next
</script>
```


以上实例输出结果：


```
Sunday
Saturday
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_filter_func)


## 实例 2


Filter：项目不包含的 "S"（include=False）：


```
<script type="text/vbscript">
a=Array("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
b=Filter(a,"S",False)
for each x in b
    document.write(x & "<br />")
next
</script>
```


以上实例输出结果：


```
Monday
Tuesday
Wednesday
Thursday
Friday
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_filter_func2)


## 实例 3


Filter：包含 "S" 的项目，用文本比较（compare=1）：


```
<script type="text/vbscript">
a=Array("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
b=Filter(a,"S",True,1)
for each x in b
    document.write(x & "<br />")
next
</script>
```


以上实例输出结果：


```
Sunday
Tuesday
Wednesday
Thursday
Saturday
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_filter_func3)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript Array 函数](https://www.runoob.com/vb-func-array.html)
			[VBScript IsArray 函数](https://www.runoob.com/func-isarray.html) **













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