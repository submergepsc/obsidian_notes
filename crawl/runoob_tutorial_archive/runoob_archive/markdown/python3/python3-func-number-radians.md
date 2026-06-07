# Python3 radians() 函数

- Source: https://www.runoob.com/python3/python3-func-number-radians.html

[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)


---


## 描述


**radians()** 方法将角度转换为弧度。


角度和弧度关系是：2π 弧度 = 360°。从而 1°≈0.0174533 弧度，1 弧度≈57.29578°。


- 1) 角度转换为弧度公式：弧度=角度÷180×π
- 2)弧度转换为角度公式： 角度=弧度×180÷π


### 语法


以下是 radians() 方法的语法:


```
import math

math.radians(x)
```


**注意：**radians()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。


---


### 参数


- x -- 一个角度数值，默认单位是角度 **°**。


---


## 返回值


返回一个角度的弧度值。


---


## 实例


以下展示了使用 radians() 方法的实例：


## 实例


```python
#!/usr/bin/python3
import math

print ("radians(90) : ",  math.radians(90))     # 1 弧度等于大概 57.3°
print ("radians(45) : ",  math.radians(45))
print ("radians(30) : ",  math.radians(30))
print ("radians(180) : ",  math.radians(180))  # 180 度的弧度为 π

print("180 / pi : ", end ="")
print (math.radians(180 / math.pi))
```


以上实例运行后输出结果为：


```
radians(90) :  1.5707963267948966
radians(45) :  0.7853981633974483
radians(30) :  0.5235987755982988
radians(180) :  3.141592653589793
180 / pi : 1.0
```


[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)








	  AI 思考中...





			** [Python3 degrees() 函数](https://www.runoob.com/python3-func-number-degrees.html)
			[Python3 capitalize()方法](https://www.runoob.com/python3-string-capitalize.html) **













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