# VBScript TypeName 函数

- Source: https://www.runoob.com/vbscript/func-typename.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


TypeName 函数返回指定变量的子类型。


TypeName 函数返回下面的值：


- Byte - 表示一个字节值
- Integer - 表示一个整型值
- Long - 表示一个长整型值
- Single - 表示一个单精度浮点值
- Double - 表示一个双精度浮点值
- Currency - 表示一个货币值
- Decimal - 表示一个十进制值
- Date - 表示一个日期或时间值
- String - 表示一个字符串值
- Boolean - 表示一个布尔值，True 或 False
- Empty - 表示一个未初始化变量
- Null - 表示无有效数据
-  - 表示实际对象类型名
- Object - 表示一般对象
- Unknown - 表示未知对象类型
- Nothing - 表示还未引用对象实例的对象变量
- Error - 表示一个错误


### 语法


TypeName(varname)


**
| 参数 | 描述 |
| --- | --- |
| varname | 必需。变量的名称。 |


## 实例


## 实例


```
<script type="text/vbscript">
x="Hello World!"
document.write(TypeName(x) & "<br />")
x=4
document.write(TypeName(x) & "<br />")
x=4.675
document.write(TypeName(x) & "<br />")
x=Null
document.write(TypeName(x) & "<br />")
x=Empty
document.write(TypeName(x) & "<br />")
x=True
document.write(TypeName(x))
</script>
```


以上实例输出结果：


```
String
Integer
Double
Null
Empty
Boolean
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_typename_func)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript SetLocale 函数](https://www.runoob.com/func-setlocale.html)
			[VBScript VarType 函数](https://www.runoob.com/func-vartype.html) **













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