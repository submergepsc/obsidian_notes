# VBScript LBound 函数

- Source: https://www.runoob.com/vbscript/func-lbound.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


LBound 函数返回指示数组维数的最小下标。


**注意：**任何维数的 LBound 总是 0。


**提示：**LBound 函数与 UBound 函数共同使用，可以确定数组的大小。


### 语法


LBound(arrayname[,dimension])


**
| 参数 | 描述 |
| --- | --- |
| arrayname | 必需。数组变量的名称。 |
| dimension | 可选。要返回哪一维的下界。 1 = 第一维， 2 = 第二维，以此类推。默认是 1 。 |


## 实例


## 实例 1


```
<script type="text/vbscript">
days=Array("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
document.write(LBound(days) & "<br />")
document.write(UBound(days) & "<br />")
</script>
```


以上实例输出结果：


```
0
6
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_lbound_func)


## 实例 2


一个二维数组：


```
<script type="text/vbscript">
Dim food(2,3)
food(0,0)="Apple"
food(0,1)="Banana"
food(0,2)="Orange"
food(0,3)="Lemon"
food(1,0)="Pizza"
food(1,1)="Hamburger"
food(1,2)="Spaghetti"
food(1,3)="Meatloaf"
food(2,0)="Cake"
food(2,1)="Cookie"
food(2,2)="Icecream"
food(2,3)="Chocolate"
document.write(LBound(food,1) & "<br />")
document.write(UBound(food,1) & "<br />")
document.write(LBound(food,2) & "<br />")
document.write(UBound(food,2) & "<br />")
</script>
```


以上实例输出结果：


```
0
2
0
3
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_lbound_func2)


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript Join 函数](https://www.runoob.com/func-join.html)
			[VBScript Split 函数](https://www.runoob.com/func-split.html) **













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