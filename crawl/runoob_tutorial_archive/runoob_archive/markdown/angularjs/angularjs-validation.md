# AngularJS 输入验证

- Source: https://www.runoob.com/angularjs/angularjs-validation.html

---


AngularJS 表单和控件可以验证输入的数据。


---


## 输入验证


在前面的几个章节中，你已经学到关于 AngularJS 表单和控件的知识。


AngularJS 表单和控件可以提供验证功能，并对用户输入的非法数据进行警告。


|  | 客户端的验证不能确保用户输入数据的安全，所以服务端的数据验证也是必须的。 |
| --- | --- |


---


## 应用代码


```javascript
<!DOCTYPE html><html><script src="http://apps.bdimg.com/libs/angular.js/1.4.6/angular.min.js"></script>
    <body>
	<h2>Validation Example</h2><form  ng-app="myApp"
	ng-controller="validateCtrl"name="myForm" novalidate>
	<p>用户名:<br>  <input type="text" name="user" ng-model="user"
	required>  <span style="color:red" ng-show="myForm.user.$dirty &&
	myForm.user.$invalid">  <span ng-show="myForm.user.$error.required">用户名是必须的。</span>  </span></p><p>邮箱:<br>
	<input type="email" name="email" ng-model="email" required>  <span
	style="color:red" ng-show="myForm.email.$dirty && myForm.email.$invalid">
	<span ng-show="myForm.email.$error.required">邮箱是必须的。</span>
	<span ng-show="myForm.email.$error.email">非法的邮箱。</span>
	</span></p><p>  <input type="submit"
	ng-disabled="myForm.user.$dirty && myForm.user.$invalid ||
	myForm.email.$dirty && myForm.email.$invalid"></p></form>
	<script>var app = angular.module('myApp', []);app.controller('validateCtrl',
    function($scope) {
	$scope.user = 'John Doe';    $scope.email = '[email protected]';
	});</script></body></html>
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_validate)


|  | HTML 表单属性 novalidate 用于禁用浏览器默认的验证。 |
| --- | --- |


---


## 实例解析


AngularJS ng-model** 指令用于绑定输入元素到模型中。


模型对象有两个属性： **user** 和 **email**。


我们使用了 **ng-show**指令， **color:red** 在邮件的 **$dirty** 或 **$invalid** 都为 true 时才显示。


| 属性 | 描述 |
| --- | --- |
| $dirty | 表单有填写记录 |
| $valid | 字段内容合法的 |
| $invalid | 字段内容是非法的 |
| $pristine | 表单没有填写记录 |









	  AI 思考中...





			** [AngularJS 表单](https://www.runoob.com/angularjs-forms.html)
			[AngularJS Bootstrap](https://www.runoob.com/angularjs-bootstrap.html) **













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