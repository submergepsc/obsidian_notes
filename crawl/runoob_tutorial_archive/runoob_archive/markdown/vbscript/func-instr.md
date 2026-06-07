# VBScript InStr 函数

- Source: https://www.runoob.com/vbscript/func-instr.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


InStr 函数返回一个字符串在另一个字符串中首次出现的位置。


InStr 函数返回下面的值：


- 如果 string1 为 "" - InStr 返回 0
- 如果 string1 为 Null - InStr 返回 Null
- 如果 string2 为 "" - InStr 返回 start
- 如果 string2 为 Null - InStr 返回 Null
- 如果 string2 没有找到 - InStr 返回 0
- 如果在 string1 中找到 string2 - InStr 返回找到匹配字符串的位置
- 如果 start > Len(string1) - InStr 返回 0


**提示：**请参阅 InStrRev 函数。


### 语法


InStr([start,]string1,string2[,compare])


**
| 参数 | 描述 |
| --- | --- |
| start | 可选。规定每次搜索的起始位置。默认的搜索起始位置是第一个字符（1）。如果已规定 compare 参数，则必须有此参数。 |
| string1 | 必需。需要被搜索的字符串。 |
| string2 | 必需。需要搜索的字符串表达式。 |
| compare | 可选。规定要使用的字符串比较类型。默认是 0。可采用下列的值： 0 = vbBinaryCompare - 执行二进制比较 1 = vbTextCompare - 执行文本比较 |


## 实例


## 实例 1


```
<script type="text/vbscript">
txt="This is a beautiful day!"
document.write(InStr(txt,"beautiful"))
</script>
```


以上实例输出结果：


```
11
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_instr_func)


## 实例 2


查找字母 "i"，采用不同的起始位置：


```
<script type="text/vbscript">
txt="This is a beautiful day!"
document.write(InStr(1,txt,"i") & "<br />")
document.write(InStr(7,txt,"i") & "<br />")
</script>
```


以上实例输出结果：


```
3
16
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_instr_func2)


## 实例 3


查找字母 "t"，采用文本和二进制比较：


```
<script type="text/vbscript">
txt="This is a beautiful day!"
document.write(InStr(1,txt,"t",1) & "<br />")
document.write(InStr(1,txt,"t",0) & "<br />")
</script>
```


以上实例输出结果：


```
1
15
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_instr_func3)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript UBound 函数](https://www.runoob.com/func-ubound.html)
			[VBScript InStrRev 函数](https://www.runoob.com/func-instrrev.html) **













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