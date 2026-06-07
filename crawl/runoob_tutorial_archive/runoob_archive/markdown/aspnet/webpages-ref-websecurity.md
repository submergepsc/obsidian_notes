# ASP.NET Web Pages - WebSecurity 对象

- Source: https://www.runoob.com/aspnet/webpages-ref-websecurity.html

---


## 描述


**WebSecurity 对象**提供 ASP.NET Web Pages 应用程序的安全性和认证。


通过 WebSecurity 对象，您可以创建用户帐户，登录和注销用户，重置或者更改密码，以及其他更多与安全性相关的功能。


---


## WebSecurity 对象参考手册 - 属性


| 属性 | 描述 |
| --- | --- |
| CurrentUserId | 获取当前登录用户的 ID。 |
| CurrentUserName | 获取当前登录用户的名称。 |
| HasUserId | 如果当前有用户 ID，则返回 true。 |
| IsAuthenticated | 如果当前用户是登录的，则返回 true。 |

**
## WebSecurity 对象参考手册 - 方法


| 方法 | 描述 |
| --- | --- |
| ChangePassword() | 为指定的用户更改密码。 |
| ConfirmAccount() | 使用帐户确认令牌确认帐户。 |
| CreateAccount() | 创建一个新的用户帐户。 |
| CreateUserAndAccount() | 创建一个新的用户帐户。 |
| GeneratePasswordResetToken() | 生成一个密码重置令牌，可以在电子邮件中发送给用户以便用户可以重设密码。 |
| GetCreateDate() | 获取指定会员创建的时间。 |
| GetPasswordChangeDate() | 获取密码变更的日期和时间。 |
| GetUserId() | 根据用户名称获取用户 ID。 |
| InitializeDatabaseConnection() | 初始化 WebSecurity 系统（数据库）。 |
| IsConfirmed() | 检查用户是否已被确认。如果已确认，则返回 true。（例如，可通过电子邮件进行确认。） |
| IsCurrentUser() | 检查当前用户的名称是否与指定用户名匹配。如果匹配，则返回 true。 |
| Login() | 设置身份验证令牌，登录用户。 |
| Logout() | 移除身份验证令牌，注销用户。 |
| RequireAuthenticatedUser() | 如果用户未通过身份验证，则设置 HTTP 状态为 401（未经授权）。 |
| RequireRoles() | 如果当前用户不是指定角色的成员，则设置 HTTP 状态为 401（未经授权）。 |
| RequireUser() | 如果当前用户不是指定用户名的用户，则设置 HTTP 状态为 401（未经授权）。 |
| ResetPassword() | 如果密码重置令牌是有效的，改变用户的密码为新密码。 |
| UserExists() | 检查指定的用户是否存在。 |


---


## 技术数据


| 名称 | 值 |
| --- | --- |
| Class | WebMatrix.WebData.WebSecurity |
| Namespace | WebMatrix.WebData |
| Assembly | WebMatrix.WebData.dll |


---


## 初始化 WebSecurity 数据库


如果您想在您的代码中使用 WebSecurity 对象，首先您必须创建或者初始化 WebSecurity 数据库。


在您的 Web 根目录下，创建一个名为 _AppStart.cshtml** 的页面（如果已存在，则直接编辑页面）。


将下面的代码复制到文件中：


## _AppStart.cshtml


```csharp
@{WebSecurity.InitializeDatabaseConnection("Users", "UserProfile",
"UserId", "Email", true);}
```


上面的代码将在每次网站（应用程序）启动时运行。它初始化了 WebSecurity 数据库。


**"Users"** 是 WebSecurity 数据库（Users.sdf）的名称。


**"UserProfile"** 是包含用户配置信息的数据库表的名称。


**"UserId"** 是包含用户 ID（主键）的列的名称。


**"Email"** 是包含用户名的列的名称。


最后一个参数 **true** 是一个布尔值，表示如果用户配置表和会员表不存在，则会自动创建表。如果不想自动创建表，应设置参数为 **false**。


|  | 虽然 true 表示自动创建数据库 表，但是数据库不会被自动创建。所以数据库必须存在。 |
| --- | --- |

**
---


## WebSecurity 数据库


UserProfile** 表为每个用户创建保存一条记录，用户 ID（主键）和用户名字（email）：


| UserId | Email |
| --- | --- |
| 1 | [email protected] |
| 2 | [email protected] |
| 3 | [email protected] |


**Membership** 表包含会员信息，比如用户是什么时候创建的，该会员是否已认证，会员是什么时候认证的，等等。


具体如下所示（一些列不显示）：


| UserId | CreateDate | ConfirmationToken | IsConfirmed | LastPasswordFailure | Password | PasswordChange |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 12.04.2012 16:12:17 | NULL | True | NULL | AFNQhWfy.... | 12.04.2012 16:12:17 |


注释：如果您想看到所有的列和内容，请打开数据库，看看里边的每个表。


---


## 简单的会员配置


在您使用 WebSecurity 对象时，如果您的站点没有配置使用 ASP.NET Web Pages 会员系统 **SimpleMembership**，可能会报错。


如果托管服务提供商的服务器的配置与您本地服务器的配置不同，也可能会报错。为了解决这个问题，请在网站的 Web.config 文件中添加以下元素：


<appSettings> **<add key="enableSimpleMembership" value="true" />

</appSettings>










	  AI 思考中...





			** [ASP.NET Web Pages 类参考手册](https://www.runoob.com/webpages-ref-classes.html)
			[ASP.NET Web Pages Database 参考手册](https://www.runoob.com/webpages-ref-database.html) **













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