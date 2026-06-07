# ASP Browser Capabilities 组件

- Source: https://www.runoob.com/asp/asp-browser.html

---


## ASP Browser Capabilities 组件


ASP Browser Capabilities 组件会创建一个 BrowserType 对象，这个对象可测定访客浏览器的类型、性能和版本号。


当浏览器连接到服务器时，就会向服务器发送一个 HTTP User Agent 报头。这个报头包含关于浏览器的信息。


BrowserType 对象会把报头中的信息与服务器上名为 "Browscap.ini" 的文件中的信息作比较。


如果报头中的浏览器类型和版本号与 "Browsercap.ini" 文件中信息匹配，那么我们就可以使用 BrowserType 对象列出这个匹配的浏览器的相关属性。如果上述情况不匹配，这个对象会把每个属性设置为 "UNKNOWN"。


### 语法


<%**
Set MyBrow=Server.CreateObject("MSWC.BrowserType")

%>


---


## ASP Browser Capabilities 实例


下面的实例会在 ASP 文件中创建一个 BrowserType 对象，并显示当前浏览器性能的一些信息：


## 实例


```
<!DOCTYPE html><html>
<body>
<%
Set MyBrow=Server.CreateObject("MSWC.BrowserType")
%>
<table border="0" width="100%">
<tr>
<th>Client OS</th><th><%=MyBrow.platform%></th>
</tr><tr>
<td >Web Browser</td><td ><%=MyBrow.browser%></td>
</tr><tr>
<td>Browser version</td><td><%=MyBrow.version%></td>
</tr><tr>
<td>Frame support?</td><td><%=MyBrow.frames%></td>
</tr><tr>
<td>Table support?</td><td><%=MyBrow.tables%></td>
</tr><tr>
<td>Sound support?</td><td><%=MyBrow.backgroundsounds%></td>
</tr><tr>
<td>Cookies support?</td><td><%=MyBrow.cookies%></td>
</tr><tr>
<td>VBScript support?</td><td><%=MyBrow.vbscript%></td>
</tr><tr>
<td>JavaScript support?</td><td><%=MyBrow.javascript%></td>
</tr>
</table>
</body>
</html>
```


输出：


| Client OS | WinNT |
| --- | --- |
| Web Browser | IE |
| Browser version | 5.0 |
| Frame support? | True |
| Table support? | True |
| Sound support? | True |
| Cookies support? | True |
| VBScript support? | True |
| JavaScript support? | True |


[演示实例 »](https://www.runoob.com/try/showasp.php?filename=demo_browsercap)


---


## Browscap.ini 文件


"Browscap.ini" 文件用于声明属性，并设置各浏览器的默认值。


这部分内容不是关于如何维护 Browscap.ini 文件的教程，我们只提供一些关于 "Browsercap.ini" 的基础知识和概念，让您对该文件有个大概的了解。


"Browscap.ini" 文件可包含下面的信息：


[;comments]

[HTTPUserAgentHeader]

[parent=browserDefinition]

[property1=value1]

[propertyN=valueN]

[Default Browser Capability Settings]

[defaultProperty1=defaultValue1]

[defaultPropertyN=defaultValueN]


| 参数 | 描述 |
| --- | --- |
| comments | 可选项。任何起始于分号的代码行都被 BrowserType 对象忽略。 |
| HTTPUserAgentHeader | 可选项。规定与在 propertyN 中设定的 browser-property 值声明相关的 HTTP User Agent 报头。允许使用通配符。 |
| browserDefinition | 可选项。规定作为父浏览器使用的某个浏览器的 HTTP User Agent header-string。当前浏览器的定义会继承在父浏览器的定义中所有声明过的属性值。 |
| propertyN | 可选项。规定浏览器的属性。下面的表格列出了某些可能的属性： ActiveXControls - 支持 ActiveX® 控件？ Backgroundsounds - 支持背景声音？ Cdf - 支持针对网络广播的频道定义格式？ Tables - 支持表格？ Cookies - 支持 cookies？ Frames - 支持框架？ Javaapplets - 支持 Java applets？ Javascript - 支持 JScript？ Vbscript - 支持 VBScript？ Browser - 规定浏览器的名称 Beta - 浏览器是否为 beta 软件？ Platform - 规定浏览器运行的平台 Version - 规定浏览器的版本号 |
| valueN | 可选项。规定 propertyN 的值。可为字符串、整数（前缀带 #）或者布尔值。 |
| defaultPropertyN | 可选项。规定浏览器属性的名称，假如已定义的 HTTPUserAgentHeader 值中没有值能与浏览器发送的 HTTP User Agent 报头相匹配，则为这个属性分配一个默认的值。 |
| defaultValueN | 可选项。规定 defaultPropertyN 的值。可为字符串、整数（前缀带 #）或者布尔值。 |


"Browscap.ini" 文件可能如下所示：


;IE 5.0

[IE 5.0]

browser=IE

Version=5.0

majorver=#5

minorver=#0

frames=TRUE

tables=TRUE

cookies=TRUE

backgroundsounds=TRUE

vbscript=TRUE

javascript=TRUE

javaapplets=TRUE

ActiveXControls=TRUE

beta=False


;DEFAULT BROWSER

[*]

browser=Default

frames=FALSE

tables=TRUE

cookies=FALSE

backgroundsounds=FALSE

vbscript=FALSE

javascript=FALSE









	  AI 思考中...





			** [ASP AdRotator](https://www.runoob.com/asp-adrotator.html)
			[ASP Content Linking](https://www.runoob.com/asp-contentlinking.html) **













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