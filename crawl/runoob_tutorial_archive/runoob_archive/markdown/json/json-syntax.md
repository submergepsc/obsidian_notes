# JSON 语法

- Source: https://www.runoob.com/json/json-syntax.html

---


JSON 语法是 JavaScript 语法的子集。


---


## JSON 语法规则


JSON 语法是 JavaScript 对象表示语法的子集。


- 数据在**名称/值**对中
- 数据由逗号 **,** 分隔
- 使用斜杆 **\** 来转义字符
- 大括号 **{}** 保存对象
- 中括号 **[]** 保存数组，数组可以包含多个对象


**JSON 的两种结构：**


**1、对象：**大括号 **{}** 保存的对象是一个无序的**名称/值**对集合。一个对象以左括号 **{** 开始， 右括号 **}** 结束。每个"键"后跟一个冒号 **:**，**名称/值**对使用逗号 **,** 分隔。


![](https://www.runoob.com/wp-content/uploads/2013/09/object.png)


**2、数组：**中括号 **[]** 保存的数组是值（value）的有序集合。一个数组以左中括号 **[** 开始， 右中括号 **]** 结束，值之间使用逗号 **,** 分隔。


![](https://www.runoob.com/wp-content/uploads/2013/09/array.png)


值（value）可以是双引号括起来的字符串（string）、数值(number)、true、false、 null、对象（object）或者数组（array），它们是可以嵌套。


![](https://www.runoob.com/wp-content/uploads/2013/09/value.png)


---


## JSON 名称/值对


JSON 数据的书写格式是：


```
key : value
```


名称/值对包括字段名称（在双引号中），后面写一个冒号，然后是值：


```json
"name" : "菜鸟教程"
```


这很容易理解，等价于这条 JavaScript 语句：


```json
name = "菜鸟教程"
```


---


## JSON 值


JSON 值可以是：


- 数字（整数或浮点数）
- 字符串（在双引号中）
- 逻辑值（true 或 false）
- 数组（在中括号中）
- 对象（在大括号中）
- null


---


## JSON 数字


JSON 数字可以是整型或者浮点型：


```json
{ "age":30 }
```


---


## JSON 对象


JSON 对象在大括号 **{}** 中书写：


```
{key1 : value1, key2 : value2, ... keyN : valueN }
```


对象可以包含多个名称/值对：


```json
{ "name":"菜鸟教程" , "url":"www.runoob.com" }
```


这一点也容易理解，与这条 JavaScript 语句等价：


```json
name = "菜鸟教程"
url = "www.runoob.com"
```


**
---


## JSON 数组


JSON 数组在中括号 **[]** 中书写：


数组可包含多个对象：


```
[
    { key1 : value1-1 , key2:value1-2 },
    { key1 : value2-1 , key2:value2-2 },
    { key1 : value3-1 , key2:value3-2 },
    ...
    { key1 : valueN-1 , key2:valueN-2 },
]
```


```json
{
    "sites": [
        { "name":"菜鸟教程" , "url":"www.runoob.com" },
        { "name":"google" , "url":"www.google.com" },
        { "name":"微博" , "url":"www.weibo.com" }
    ]
}
```


在上面的例子中，对象 sites** 是包含三个对象的数组。每个对象代表一条关于某个网站（name、url）的记录。


---


## JSON 布尔值


JSON 布尔值可以是 true 或者 false：


```json
{ "flag":true }
```


---


## JSON null


JSON 可以设置 null 值：


```json
{ "runoob":null }
```


---


## JSON 使用 JavaScript 语法


因为 JSON 使用 JavaScript 语法，所以无需额外的软件就能处理 JavaScript 中的 JSON。


通过 JavaScript，您可以创建一个对象数组，并像这样进行赋值：


## 实例


```json
var sites = [
    { "name":"runoob" , "url":"www.runoob.com" },
    { "name":"google" , "url":"www.google.com" },
    { "name":"微博" , "url":"www.weibo.com" }
];
```


可以像这样访问 JavaScript 对象数组中的第一项（索引从 0 开始）：


```json
sites[0].name;
```


返回的内容是：


```json
runoob
```


可以像这样修改数据：


```json
sites[0].name="菜鸟教程";
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_objectarray)



在下面的章节，您将学到如何把 JSON 文本转换为 JavaScript 对象。


---


## JSON 文件


- JSON 文件的文件类型是 **.json**
- JSON 文本的 MIME 类型是 **application/json**








	  AI 思考中...





			** [JSON 使用](https://www.runoob.com/json-eval.html)
			[JSON 简介](https://www.runoob.com/json-intro.html) **













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