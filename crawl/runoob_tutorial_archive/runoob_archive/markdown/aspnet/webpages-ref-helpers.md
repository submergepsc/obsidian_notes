# ASP.NET Web Pages - 更多帮助器

- Source: https://www.runoob.com/aspnet/webpages-ref-helpers.html

---


## ASP.NET 帮助器 - 对象参考手册


---


## Analytics 对象参考手册（Google）


| Helper | 描述 |
| --- | --- |
| Analytics.GetGoogleHtml(webPropertyId) | 为指定的 ID 呈现 Google Analytics JavaScript 代码。 |
| Analytics.GetStatCounterHtml(project, security) | 为指定的项目呈现 StatCounter Analytics JavaScript 代码。 |
| Analytics.GetYahooHtml(account) | 为指定的账号呈现 Yahoo Analytics JavaScript 代码。 |

**
---


## Bing 对象参考手册


| Helper | 描述 |
| --- | --- |
| Bing.SearchBox([boxWidth]) | 给 Bing 传递搜索。您可以设置 Bing.SiteUrl 和 Bing.SiteTitle 属性来设定站点搜索和搜索框的标题，通常是在 _AppStart 页面设置这些属性。 |
| Bing.AdvancedSearchBox([, boxWidth] [, resultWidth] [, resultHeight] [, themeColor] [, locale]) | 用可选的格式显示 Bing 搜索结果在页面上。您可以设置 Bing.SiteUrl 和 Bing.SiteTitle 属性来设定站点搜索和搜索框的标题，通常是在 _AppStart 页面设置这些属性。 |


---


## Chart 对象参考手册


| Helper | 描述 |
| --- | --- |
|  |  |
| Chart(width, height [, template] [, templatePath]) | 初始化图表。 |
| Chart.AddLegend([title] [, name]) | 给图表添加一个图例。 |
| Chart.AddSeries([name] [, chartType] [, chartArea] [, axisLabel] [, legend] [, markerStep] [, xValue] [, xField] [, yValues] [, yFields] [, options]) | 给图表添加一系列数据。 |


---


## Crypto 对象参考手册


| Helper | 描述 |
| --- | --- |
| Crypto.Hash(string [, algorithm]) Crypto.Hash(bytes [, algorithm]) | 返回指定数据的哈希。默认算法是 sha256。 |


---


## Facebook 对象参考手册


| Helper | 描述 |
| --- | --- |
| Facebook.LikeButton(href [, buttonLayout] [, showFaces] [, width] [, height] [, action] [, font] [, colorScheme] [, refLabel]) | 让 Facebook 用户连接到网页。 |


---


## FileUpload 对象参考手册


| Helper | 描述 |
| --- | --- |
| FileUpload.GetHtml([initialNumberOfFiles] [, allowMoreFilesToBeAdded] [, includeFormTag] [, addText] [, uploadText]) | 为上传文件呈现 UI。 |


---


## GamerCard 对象参考手册


| Helper | 描述 |
| --- | --- |
| GamerCard.GetHtml(gamerTag) | 呈现指定的 Xbox gamer 标签。 |


---


## Gravatar 对象参考手册


| Helper | 描述 |
| --- | --- |
| Gravatar.GetHtml(email [, imageSize] [, defaultImage] [, rating] [, imageExtension] [, attributes]) | 为指定的电子邮件地址呈现 Gravatar 图像。 |


---


## Json 对象参考手册


| Helper | 描述 |
| --- | --- |
| Json.Encode(object) | 用 JavaScript Object Notation (JSON) 把数据对象转换为字符串。 |
| Json.Decode(string) | 转换 JSON 编码的输入字符串为您指定的数据对象。 |


---


## LinkShare 对象参考手册


| Helper | 描述 |
| --- | --- |
| LinkShare.GetHtml(pageTitle [, pageLinkBack] [, twitterUserName] [, additionalTweetText] [, linkSites]) | 使用指定的标题和可选的 URL 呈现社会网络链接。 |


---


## ModelState 对象参考手册


| Helper | 描述 |
| --- | --- |
| ModelStateDictionary.AddError(key, errorMessage) | 关联错误信息和一个表单域。使用 ModelState 帮助器访问成员。 |
| ModelStateDictionary.AddFormError(errorMessage) | 关联错误信息和一个表单。使用 ModelState 帮助器访问成员。 |
| ModelStateDictionary.IsValid | 如果没有验证错误，返回 true。使用 ModelState 帮助器访问成员。 |


---


## ObjectInfo 对象参考手册


| Helper | 描述 |
| --- | --- |
| ObjectInfo.Print(value [, depth] [, enumerationLength]) | 呈现一个对象和所有子对象的属性和值。 |


---


## Recaptcha 对象参考手册


| Helper | 描述 |
| --- | --- |
| Recaptcha.GetHtml([, publicKey] [, theme] [, language] [, tabIndex]) | 呈现 reCAPTCHA 验证测试。 |
| ReCaptcha.PublicKey ReCaptcha.PrivateKey | 设置 reCAPTCHA 服务的公共和私有密钥。通常是在 _AppStart 页面设置这些属性。 |
| ReCaptcha.Validate([, privateKey]) | 返回 reCAPTCHA 测试结果。 |
| ServerInfo.GetHtml() | Renders 呈现有关 ASP.NET Web Pages 的状态信息。 |


---


## Twitter 对象参考手册


| Helper | 描述 |
| --- | --- |
| Twitter.Profile(twitterUserName) | 为指定的用户呈现 Twitter 流。 |
| Twitter.Search(searchQuery) | 为指定的搜索文本呈现 Twitter 流。 |


---


## Video 对象参考手册


| Helper | 描述 |
| --- | --- |
| Video.Flash(filename [, width, height]) | 为指定的文件呈现宽度和高度可选的 Flash 视频播放。 |
| Video.MediaPlayer(filename [, width, height]) | 为指定的文件呈现宽度和高度可选 的 Windows Media 播放器。 |
| Video.Silverlight(filename, width, height) | 为指定的 .xap 文件呈现所需的宽度和高度 的 Silverlight 播放器。 |


---


## WebCache 对象参考手册


| Helper | 描述 |
| --- | --- |
| WebCache.Get(key) | 通过 key 返回指定的对象，如果对象未找到则返回 null。 |
| WebCache.Remove(key) | 通过 key 从缓存中删除指定的对象。 |
| WebCache.Set(key, value [, minutesToCache] [, slidingExpiration]) | 通过 key 把 value 放置到指定名称的缓存中。 |


---


## WebGrid 对象参考手册


| Helper | 描述 |
| --- | --- |
| WebGrid(data) | Creates a 使用查询数据创建一个新的 WebGrid 对象。 |
| WebGrid.GetHtml() | Renders markup 显示数据在 HTML 表格中。 |
| WebGrid.Pager() | 为 WebGrid 对象呈现一个页面。 |


---


## WebImage 对象参考手册


| Helper | 描述 |
| --- | --- |
| WebImage(path) | 从指定的路径加载一个图像。 |
| WebImage.AddImagesWatermark(image) | 为指定图像加水印。 |
| WebImage.AddTextWatermark(text) | 为图像添加指定文本。 |
| WebImage.FlipHorizontal() WebImage.FlipVertical() | 水平/垂直翻转图像 |
| WebImage.GetImageFromRequest() | 当图像被传送到一个文件上传页面时，加载图像。 |
| WebImage.Resize(width, height) | 调整图像大小。 |
| WebImage.RotateLeft() WebImage.RotateRight() | 向左或向右旋转图像。 |
| WebImage.Save(path [, imageFormat]) | 保存图像到指定路径。 |










	  AI 思考中...





			** [ASP.NET Web Pages WebMail 参考手册](https://www.runoob.com/webpages-ref-webmail.html)
			[ASP.NET Razor 标记](https://www.runoob.com/razor-intro.html) **













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