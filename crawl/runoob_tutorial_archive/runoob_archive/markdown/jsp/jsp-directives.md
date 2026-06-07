# JSP 指令

- Source: https://www.runoob.com/jsp/jsp-directives.html

JSP指令用来设置整个JSP页面相关的属性，如网页的编码方式和脚本语言。


语法格式如下：


```
<%@ directive attribute="value" %>
```


指令可以有很多个属性，它们以键值对的形式存在，并用逗号隔开。


JSP中的三种指令标签：


| 指令 | 描述 |
| --- | --- |
|  | 定义网页依赖属性，比如脚本语言、error页面、缓存需求等等 |
|  | 包含其他文件 |
|  | 引入标签库的定义 |

---


## Page指令


Page指令为容器提供当前页面的使用说明。一个JSP页面可以包含多个page指令。


Page指令的语法格式：


```
<%@ page attribute="value" %>
```


等价的XML格式：


```
<jsp:directive.page attribute="value" />
```


---


## 属性

下表列出与Page指令相关的属性：


| 属性 | 描述 |
| --- | --- |
| buffer | 指定out对象使用缓冲区的大小 |
| autoFlush | 控制out对象的 缓存区 |
| contentType | 指定当前JSP页面的MIME类型和字符编码 |
| errorPage | 指定当JSP页面发生异常时需要转向的错误处理页面 |
| isErrorPage | 指定当前页面是否可以作为另一个JSP页面的错误处理页面 |
| extends | 指定servlet从哪一个类继承 |
| import | 导入要使用的Java类 |
| info | 定义JSP页面的描述信息 |
| isThreadSafe | 指定对JSP页面的访问是否为线程安全 |
| language | 定义JSP页面所用的脚本语言，默认是Java |
| session | 指定JSP页面是否使用session |
| isELIgnored | 指定是否执行EL表达式 |
| isScriptingEnabled | 确定脚本元素能否被使用 |


---


## Include指令


JSP可以通过include指令来包含其他文件。被包含的文件可以是JSP文件、HTML文件或文本文件。包含的文件就好像是该JSP文件的一部分，会被同时编译执行。


Include指令的语法格式如下：


```
<%@ include file="文件相对 url 地址" %>
```


**include** 指令中的文件名实际上是一个相对的 URL 地址。


如果您没有给文件关联一个路径，JSP编译器默认在当前路径下寻找。


等价的XML语法：


```
<jsp:directive.include file="文件相对 url 地址" />
```


---


## Taglib指令


JSP API允许用户自定义标签，一个自定义标签库就是自定义标签的集合。


Taglib指令引入一个自定义标签集合的定义，包括库路径、自定义标签。


Taglib指令的语法：


```
<%@ taglib uri="uri" prefix="prefixOfTag" %>
```


uri属性确定标签库的位置，prefix属性指定标签库的前缀。


等价的XML语法：


```
<jsp:directive.taglib uri="uri" prefix="prefixOfTag" />
```









	  AI 思考中...





			** [JSP 语法](https://www.runoob.com/jsp-syntax.html)
			[JSP 动作元素](https://www.runoob.com/jsp-actions.html) **













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