# VBScript Replace 函数

- Source: https://www.runoob.com/vbscript/func-replace.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


Replace 函数使用另一个字符串替换字符串的指定部分指定的次数。


### 语法


Replace(string,find,replacewith[,start[,count[,compare]]])


**
| 参数 | 描述 |
| --- | --- |
| string | 必需。被搜索的字符串。 |
| find | 必需。将被替换的字符串部分。 |
| replacewith | 必需。用于替换的子字符串。 |
| start | 可选。指定的开始位置。默认值是 1。起始位置之前的所有字符将被删除。 |
| count | 可选。规定要执行的替换的次数。 默认值是 -1，表示进行所有可能的替换。 |
| compare | 可选。规定要使用的字符串比较类型。默认是 0。可采用下列的值： 0 = vbBinaryCompare - 执行二进制比较 1 = vbTextCompare - 执行文本比较 |


## 实例


## 实例 1


把单词 "beautiful" 替换为 "fantastic"：


```
<script type="text/vbscript">
txt="This is a beautiful day!"
document.write(Replace(txt,"beautiful","fantastic"))
</script>
```


以上实例输出结果：


```
This is a fantastic day!
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_replace_func)


## 实例 2


把字母 "i" 替换为 "##"：


```
<script type="text/vbscript">
txt="This is a beautiful day!"
document.write(Replace(txt,"i","##"))
</script>
```


以上实例输出结果：


```
Th##s ##s a beaut##ful day!
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_replace_func2)


## 实例 3


把字母 "i" 替换为 "##"，从位置 15 开始：


请注意，位置 15 之前的所有字符都会被删除。


```
<script type="text/vbscript">
txt="This is a beautiful day!"
document.write(Replace(txt,"i","##",15))
</script>
```


以上实例输出结果：


```
t##ful day!
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_replace_func3)


## 实例 4


从位置 1 开始，把前 2 个字母 "i" 替换为 "##"：


```
<script type="text/vbscript">
txt="This is a beautiful day!"
document.write(Replace(txt,"i","##",1,2))
</script>
```


以上实例输出结果：


```
Th##s ##s a beautiful day!
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_replace_func4)


## 实例 5


把字母 "t" 替换为 "##"，采用文本和二进制比较：


```
<script type="text/vbscript">
txt="This is a beautiful day!"
document.write(Replace(txt,"t","##",1,-1,1) & "<br />")
document.write(Replace(txt,"t","##",1,-1,0))
</script>
```


以上实例输出结果：


```
##his is a beau##iful day!
This is a beau##iful day!
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_replace_func5)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript Mid 函数](https://www.runoob.com/func-mid.html)
			[VBScript Right 函数](https://www.runoob.com/func-right.html) **













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