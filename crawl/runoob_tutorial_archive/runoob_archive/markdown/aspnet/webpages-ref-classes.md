# ASP.NET Web Pages - 类

- Source: https://www.runoob.com/aspnet/webpages-ref-classes.html

---


## ASP.NET 类参考手册


| 方法 | 描述 |
| --- | --- |
| AsBool(), AsBool(true\|false) | 转换字符串值为布尔值（true/false）。如果字符串不能转换为true/false，则返回 false 或者其他规定的值。 |
| AsDateTime(), AsDateTime(value) | 转换字符串值为日期/时间。返回 DateTime。如果字符串不能转换为日期/时间，则返回 MinValue 或者其他规定的值。 |
| AsDecimal(), AsDecimal(value) | 转换字符串值为十进制值。如果字符串不能转换为十进制值，则返回 0.0 或者其他规定的值。 |
| AsFloat(), AsFloat(value) | 转换字符串值为浮点数。如果字符串不能转换为浮点数，则返回 0.0 或者其他规定的值。 |
| AsInt(), AsInt(value) | 转换字符串值为整数。如果字符串不能转换成整数，则返回 0 或者其他规定的值。 |
| Href(path [, param1 [, param2]]) | 从带有可选的附加路径部分的本地文件路径创建一个浏览器兼容的 URL。 |
| Html.Raw(value) | Renders value 呈现为 HTML 标记，而不是呈现为 HTML 编码输出。 |
| IsBool(), IsDateTime(), IsDecimal(), IsFloat(), IsInt() | 如果该值可以从字符串转换为指定的类型，则返回 true。 |
| IsEmpty() | 如果对象或者变量没有值，则返回 true。 |
| IsPost | 如果请求是 POST，则返回 true。（初始请求通常是 GET。） |
| Layout | 规定布局页面的路径应用到此页面。 |
| PageData[key], PageData[index], Page | 在当前请求的页面、布局页面、部分页面之间包含共享数据。您可以使用动态页面来对相同的数据进行属性访问。 |
| RenderBody() | (Layout pages) 呈现没有在布局页面任何命名区域的内容页的内容Renders the content of a content page that is not in any named sections. |
| RenderPage(path, values) RenderPage(path[, param1 [, param2]]) | 呈现使用了规定的路径和可选的额外数据的内容页。您可以通过 position（实例 1）或者 key（实例 2）从 PageData 获取额外参数的值。 |
| RenderSection(sectionName [, required = true\|false]) | (Layout pages) 呈现一个有名字的内容区域。设置 required 让一个区域为必需非可选的。 |
| Request.Cookies[key] | 获取或者设置 HTTP cookie 的值。 |
| Request.Files[key] | Gets 在当前请求中上传的文件。 |
| Request.Form[key] | 获取在表单中 post 的数据（作为字符串）。Request.Form 和 Request.QueryString 都要求[key] 检查。 |
| Request.QueryString[key] | 获取 URL 查询字符串中规定的数据。Request.Form 和 Request.QueryString 都要求[key] 检查。 |
| Request.Unvalidated(key) Request.Unvalidated().QueryString\|Form\|Cookies\|Headers[key] | 有选择地禁用请求验证（表单元素、查询字符串值、cookie、header 值）。请求验证默认是开启的，防止用户提交标记或者其他潜在的危险内容。 |
| Response.AddHeader(name, value) | 在应答中添加一个 HTTP 服务器响应头。 |
| Response.OutputCache(seconds [, sliding] [, varyByParams]) | Caches 在指定时间的页面输出缓存。设置 sliding 来重置每个页面的访问超时时间，设置 varyByParams 为请求页面的每个不同的查询字符串缓存不同版本的页面。 |
| Response.Redirect(path) | 重定向浏览器请求到一个新的位置。 |
| Response.SetStatus(httpStatusCode) | 设置HTTP状态代码发送到浏览器。 |
| Response.WriteBinary(data [, mimetype]) | 写入 data 内容响应可选的MIME类型。 |
| Response.WriteFile(file) | 写入文件内容响应。 |
| @section(sectionName) { content } | （布局页面）定义一个有名字的内容区域。 |
| Server.HtmlDecode(htmlText) | 解码一个HTML编码的字符串。 |
| Server.HtmlEncode(text) | 为呈现在 HTML 标记中的字符串编码。 |
| Server.MapPath(virtualPath) | 为指定的虚拟路径返回服务器的物理路径。 |
| Server.UrlDecode(urlText) | 解码URL文本。 |
| Server.UrlEncode(text) | URL文本编码。 |
| Session[key] | 获取或设置一个存在的值，直到用户关闭浏览器。 |
| ToString() | 显示一个用字符串表示的对象的值。 |
| UrlData[index] | 从 URL 获取额外的数据（例如，/MyPage/ExtraData）。 |

**








	  AI 思考中...





			** [ASP.NET Web 的 C# 和 VB 实例](https://www.runoob.com/webpages-examples.html)
			[ASP.NET Web Pages WebSecurity 参考手册](https://www.runoob.com/webpages-ref-websecurity.html) **













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