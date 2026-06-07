# VBScript FormatCurrency 函数

- Source: https://www.runoob.com/vbscript/func-formatcurrency.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


FormatCurrency 函数返回作为货币值被格式化的表达式，使用计算机系统控制面板中定义的货币符号。


### 语法


FormatCurrency(Expression[,NumDigAfterDec[,**
IncLeadingDig[,UseParForNegNum[,GroupDig]]]])


| 参数 | 描述 |
| --- | --- |
| expression | 必需。需被格式化的表达式。 |
| NumDigAfterDec | 可选。指示小数点右侧显示位数的数值。默认值为 -1（使用的是计算机的区域设置）。 |
| IncLeadingDig | 可选。指示是否显示小数值的前导零： -2 = TristateUseDefault - 使用计算机的区域设置 -1 = TristateTrue - True 0 = TristateFalse - False |
| UseParForNegNum | 可选。指示是否将负值置于括号中： -2 = TristateUseDefault - 使用计算机的区域设置 -1 = TristateTrue - True 0 = TristateFalse - False |
| GroupDig | 可选。指示是否使用计算机区域设置中指定的数字分组符号将数字分组： -2 = TristateUseDefault - 使用计算机的区域设置 -1 = TristateTrue - True 0 = TristateFalse - False |


## 实例


## 实例 1


```
<script type="text/vbscript">
document.write(FormatCurrency(20000))
</script>
```


以上实例输出结果：


```
$20,000.00
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_formatcurrency_func)


## 实例 2


设置小数点后的位数：


```
<script type="text/vbscript">
document.write(FormatCurrency(20000,2) & "<br />")
document.write(FormatCurrency(20000,5))
</script>
```


以上实例输出结果：


```
$20,000.00
$20,000.00000
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_formatcurrency_func2)


## 实例 3


是否显示小数值的前导零：


```
<script type="text/vbscript">
document.write(FormatCurrency(.20,,0) & "<br />")
document.write(FormatCurrency(.20,,-1))
</script>
```


以上实例输出结果：


```
$.20
$0.20
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_formatcurrency_func3)


## 实例 4


是否将负值置于括号中：


```
<script type="text/vbscript">
document.write(FormatCurrency(-50,,,0) & "<br />")
document.write(FormatCurrency(-50,,,-1))
</script>
```


以上实例输出结果：


```
-$50.00
($50.00)
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_formatcurrency_func4)


## 实例 5


是否将一百万美元分组：


```
<script type="text/vbscript">
document.write(FormatCurrency(1000000,,,,0) & "<br />")
document.write(FormatCurrency(1000000,,,,-1))
</script>
```


以上实例输出结果：


```
$1000000.00
$1,000,000.00
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_formatcurrency_func5)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript Oct 函数](https://www.runoob.com/func-oct.html)
			[VBScript FormatNumber 函数](https://www.runoob.com/func-formatnumber.html) **













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