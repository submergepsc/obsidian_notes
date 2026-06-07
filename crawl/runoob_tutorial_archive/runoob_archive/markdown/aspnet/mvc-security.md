# ASP.NET MVC - 安全

- Source: https://www.runoob.com/aspnet/mvc-security.html

---


为了学习 ASP.NET MVC，我们将构建一个 Internet 应用程序。


第 8 部分：添加安全。


---


## MVC 应用程序安全


**Models 文件夹**包含表示应用程序模型的类。


Visual Web Developer 自动创建 **AccountModels.cs** 文件，该文件包含用于应用程序认证的模型。


**AccountModels** 包含 **LogOnModel**、**ChangePasswordModel** 和 **RegisterModel**：


![Model](https://www.runoob.com/wp-content/uploads/2013/08/10.jpg)


---


## Change Password 模型


	public class ChangePasswordModel**{

[Required]
[DataType(DataType.Password)]

		[Display(Name = "Current password")]
public string OldPassword { get;
		set; }

[Required]
[StringLength(100, ErrorMessage = "The {0}
		must be at least {2}      characters long.",
		MinimumLength = 6)]
[DataType(DataType.Password)]
[Display(Name =
		"New password")]
public string NewPassword { get; set; }

[DataType(DataType.Password)]

		[Display(Name = "Confirm new password")]
[Compare("NewPassword",
		ErrorMessage = "The new password and confirmation password do not
		match.")]
public string ConfirmPassword { get; set; }

}


---


## Logon 模型


	public class LogOnModel
{

[Required]
[Display(Name = "User
		name")]
public string UserName { get; set; }

[Required]
[DataType(DataType.Password)]

		[Display(Name = "Password")]
public string Password { get; set; }

[Display(Name = "Remember me?")]
public bool RememberMe { get;
		set; }

}


---


## Register 模型


	public class RegisterModel
{

[Required]
[Display(Name =
		"User name")]
public string UserName { get; set; }

[Required]

		[DataType(DataType.EmailAddress)]
[Display(Name = "Email address")]

		public string Email { get; set; }

[Required]
[StringLength(100,
		ErrorMessage = "The {0} must be at least {2} characters long.",
		MinimumLength = 6)]
[DataType(DataType.Password)]
[Display(Name =
		"Password")]
public string Password { get; set; }

[DataType(DataType.Password)]

		[Display(Name = "Confirm password")]
[Compare("Password",
		ErrorMessage = "The password and confirmation password do not match.")]

		public string ConfirmPassword { get; set; }

}










	  AI 思考中...





			** [ASP.NET MVC 模型](https://www.runoob.com/mvc-models.html)
			[ASP.NET MVC HTML 帮助器](https://www.runoob.com/mvc-htmlhelpers.html) **













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