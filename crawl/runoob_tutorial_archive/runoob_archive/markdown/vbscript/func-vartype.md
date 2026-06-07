# VBScript VarType 函数

- Source: https://www.runoob.com/vbscript/func-vartype.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


VarType 函数返回指示指定变量的子类型的值。


VarType 函数返回下面的值：


- 0 = vbEmpty - 表示空（未初始化）
- 1 = vbNull - 表示 Null（无有效数据）
- 2 = vbInteger - 表示一个整数
- 3 = vbLong - 表示一个长整数
- 4 = vbSingle - 表示一个单精度浮点数
- 5 = vbDouble - 表示一个双精度浮点数
- 6 = vbCurrency - 表示货币
- 7 = vbDate - 表示日期
- 8 = vbString - 表示一个字符串
- 9 = vbObject - 表示一个 automation 对象
- 10 = vbError - 表示一个错误
- 11 = vbBoolean - 表示一个布尔值
- 12 = vbVariant - 表示 Variant（仅用于变量数组）
- 13 = vbDataObject - 表示一个数据访问对象
- 17 = vbByte - 表示一个字节
- 8192 = vbArray - 表示一个数组


**注意：**假如变量是数组，则 VarType() 会返回 8192 + VarType(array_element)。举例：整数数组的 VarType() 会返回 8192 + 2 = 8194。


### 语法


VarType(varname)


**
| 参数 | 描述 |
| --- | --- |
| varname | 必需。变量的名称。 |


## 实例


## 实例


```
<script type="text/vbscript">
x="Hello World!"
document.write(VarType(x) & "<br />")
x=4
document.write(VarType(x) & "<br />")
x=4.675
document.write(VarType(x) & "<br />")
x=Null
document.write(VarType(x) & "<br />")
x=Empty
document.write(VarType(x) & "<br />")
x=True
document.write(VarType(x))
</script>
```


以上实例输出结果：


```
8
2
5
1
0
11
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_vartype_func)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript TypeName 函数](https://www.runoob.com/func-typename.html)
			[VBScript 函数](https://www.runoob.com/vbscript-ref-functions.html) **













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