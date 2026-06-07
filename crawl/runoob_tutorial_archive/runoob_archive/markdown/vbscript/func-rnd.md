# VBScript Rnd 函数

- Source: https://www.runoob.com/vbscript/func-rnd.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


Rnd 函数返回一个随机数。数字总是小于 1 但大于或等于 0 。


### 语法


Rnd[(number)]


**
| 参数 | 描述 |
| --- | --- |
| number | 可选。有效的数值表达式。如果数字是： >0 - Rnd 会返回序列中的下一个随机数。 =0 - Rnd 会返回最近生成的数。 省略 - Rnd 会返回序列中的下一个随机数。 |


## 实例


## 实例 1


随机数：


```
<script type="text/vbscript">
document.write(Rnd)
</script>
```


请注意，您每次都会得到相同的数字。为了避免这种情况，请使用实例 2 中的 Randomize 语句。


以上实例输出结果：


```
0.7055475
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_rnd_func)


## 实例 2


为了避免像在实例 1 中每次都得到相同的数字，请使用 Randomize 语句：


```
<script type="text/vbscript">
Randomize
document.write(Rnd)
</script>
```


以上实例输出结果：


```
0.4758112
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_rnd_func2)


## 实例 3


以下是如何在一个给定的范围内产生随机整数：


```
<script type="text/vbscript">
Dim max,min
max=100
min=1
Randomize
document.write(Int((max-min+1)*Rnd+min))
</script>
```


以上实例输出结果：


```
71
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_rnd_func3)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript Log 函数](https://www.runoob.com/func-log.html)
			[VBScript Sgn 函数](https://www.runoob.com/func-sgn.html) **













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