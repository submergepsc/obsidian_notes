# JSON vs XML

- Source: https://www.runoob.com/json/json-vs-xml.html

JSON 和 XML 都用于接收 web 服务端的数据。


JSON 和 XML在写法上有所不同，如下所示：


## JSON 实例


```json
{
    "sites": [
    { "name":"菜鸟教程" , "url":"www.runoob.com" },
    { "name":"google" , "url":"www.google.com" },
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}
```


## XML 实例


```json
<sites>
  <site>
    <name>菜鸟教程</name> <url>www.runoob.com</url>
  </site>
  <site>
    <name>google</name> <url>www.google.com</url>
  </site>
  <site>
    <name>微博</name> <url>www.weibo.com</url>
  </site>
</sites>
```


JSON 与 XML 的相同之处：


- JSON 和 XML 数据都是 "自我描述" ，都易于理解。
- JSON 和 XML 数据都是有层次的结构
- JSON 和 XML 数据可以被大多数编程语言使用


JSON 与 XML 的不同之处：


- JSON 不需要结束标签
- JSON 更加简短
- JSON 读写速度更快
- JSON 可以使用数组


**
最大的不同是**：XML 需要使用 XML 解析器来解析，JSON 可以使用标准的 JavaScript 函数来解析。


- [JSON.parse()](https://www.runoob.com/../js/javascript-json-parse.html): 将一个 JSON 字符串转换为 JavaScript 对象。
- [JSON.stringify()](https://www.runoob.com/../js/javascript-json-stringify.html): 将 JavaScript 值转换为 JSON 字符串。


---


## 为什么 JSON 比 XML 更好？


XML 比 JSON 更难解析。


JSON 可以直接使用现有的 JavaScript 对象解析。


针对 AJAX 应用，JSON 比 XML 数据加载更快，而且更简单：


使用 XML


- 获取 XML 文档
- 使用 XML DOM 迭代循环文档
- 接数据解析出来复制给变量


使用 JSON


- 获取 JSON 字符串
- JSON.Parse 解析 JSON 字符串


---

## 相关文章


- JavaScript JSON: [https://www.runoob.com/js/js-json.html](https://www.runoob.com/../js/js-json.html)
- XML DOM 教程: [https://www.runoob.com/dom/dom-tutorial.html](https://www.runoob.com/../dom/dom-tutorial.html)








	  AI 思考中...





			** [JSON.stringify()](https://www.runoob.com/json-stringify.html)














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