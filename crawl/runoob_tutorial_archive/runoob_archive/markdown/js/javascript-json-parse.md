# JavaScript JSON.parse()

- Source: https://www.runoob.com/js/javascript-json-parse.html

[![JavaScript JSON](https://www.runoob.com/images/up.gif) JavaScript JSON](https://www.runoob.com/js-json.html)


---


JSON.parse() 方法用于将一个 JSON 字符串转换为对象。


### 语法


```
JSON.parse(text[, reviver])
```


**参数说明：**


- **text:**必需， 一个有效的 JSON 字符串。
- **reviver:** 可选，一个转换结果的函数， 将为对象的每个成员调用此函数。


### 返回值：


返回给定 JSON 字符串转换后的对象。


### 实例


```javascript
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML =obj.employees[1].name
	+ " " + obj.employees[1].site;
</script>
```

**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjson_parse1)


使用可选参数：


### 实例


```javascript
JSON.parse('{"p": 5}', function(k, v) {
  if (k === '') { return v; }
  return v * 2;
});

JSON.parse('{"1": 1, "2": 2, "3": {"4": 4, "5": {"6": 6}}}', function(k, v) {
  console.log(k); // 输出当前属性，最后一个为 ""
  return v;       // 返回修改的值
});
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjson_parse2)



[![JavaScript JSON](https://www.runoob.com/images/up.gif) JavaScript JSON](https://www.runoob.com/js-json.html)









	  AI 思考中...





			** [JavaScript 类型转换](https://www.runoob.com/js-type-conversion.html)
			[JavaScript JSON.stringify()](https://www.runoob.com/javascript-json-stringify.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

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