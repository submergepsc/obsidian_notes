# JSON - 简介

- Source: https://www.runoob.com/json/json-intro.html

---


## 在线实例


通过我们的编辑器，您可以在线编辑 JavaScript 代码，然后通过点击一个按钮来查看结果：


## JSON 实例


```json
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<h2>JavaScript 创建 JSON 对象</h2>
<p>
网站名称: <span id="jname"></span><br />
网站地址: <span id="jurl"></span><br />
网站 slogan: <span id="jslogan"></span><br />
</p>
<script>
```

 var JSONObject= {
    "name":"菜鸟教程",
    "url":"www.runoob.com",
    "slogan":"学的不仅是技术，更是梦想！"
};
document.getElementById("jname").innerHTML=JSONObject.name
document.getElementById("jurl").innerHTML=JSONObject.url
document.getElementById("jslogan").innerHTML=JSONObject.slogan </script>

</body>
</html>

**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_create)


点击 "尝试一下" 按钮查看在线实例。


---


## 与 XML 相同之处


- JSON 是纯文本
- JSON 具有"自我描述性"（人类可读）
- JSON 具有层级结构（值中存在值）
- JSON 可通过 JavaScript 进行解析
- JSON 数据可使用 AJAX 进行传输


---


## 与 XML 不同之处


- 没有结束标签
- 更短
- 读写的速度更快
- 能够使用内建的 JavaScript eval() 方法进行解析
- 使用数组
- 不使用保留字


---


## 为什么使用 JSON？


对于 AJAX 应用程序来说，JSON 比 XML 更快更易使用：


#### 使用 XML


- 读取 XML 文档
- 使用 XML DOM 来循环遍历文档
- 读取值并存储在变量中


#### 使用 JSON


- 读取 JSON 字符串
- 用 eval() 处理 JSON 字符串









	  AI 思考中...





			** [JSON 语法](https://www.runoob.com/json-syntax.html)
			[JSONP 教程](https://www.runoob.com/json-jsonp.html) **













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