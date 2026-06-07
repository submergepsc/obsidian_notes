# AngularJS Bootstrap

- Source: https://www.runoob.com/angularjs/angularjs-bootstrap.html

---


AngularJS 的首选样式表是 Twitter Bootstrap， Twitter Bootstrap 是目前最受欢迎的前端框架。


[查看 Bootstrap教程](https://www.runoob.com/../bootstrap/bootstrap-tutorial.html)。


---


## Bootstrap


你可以在你的 AngularJS 应用中加入 Twitter Bootstrap，你可以在你的 元素中添加如下代码:


```javascript
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
```


如果站点在国内，建议使用百度静态资源库的Bootstrap，代码如下：


```javascript
<link rel="stylesheet" href="//apps.bdimg.com/libs/bootstrap/3.3.4/css/bootstrap.min.css">
```


以下是一个完整的 HTML 实例, 使用了 AngularJS 指令和 Bootstrap 类。


---


## HTML 代码


```javascript
<!DOCTYPE html><html>
<link rel="stylesheet"
href="http://apps.bdimg.com/libs/bootstrap/3.3.4/css/bootstrap.min.css">
 <script src="http://apps.bdimg.com/libs/angular.js/1.4.6/angular.min.js"></script>
<body
 ng-app="myApp" ng-controller="userCtrl">
 <div class="container"><h3>Users</h3><table
class="table table-striped">  <thead><tr>
    <th>Edit</th>    <th>First
Name</th>    <th>Last Name</th>  </tr></thead>
  <tbody><tr
ng-repeat="user in users">    <td>
      <button class="btn" ng-click="editUser(user.id)">

<span class="glyphicon glyphicon-pencil"></span>&nbsp;&nbsp;Edit

</button>    </td>    <td>{{ user.fName }}</td>
    <td>{{ user.lName }}</td>

</tr></tbody></table><hr><button class="btn btn-success"
ng-click="editUser('new')">
  <span class="glyphicon glyphicon-user"></span> Create New User
</button><hr>
<h3 ng-show="edit">Create New User:</h3><h3 ng-hide="edit">Edit
User:</h3><form class="form-horizontal"><div class="form-group">

<label class="col-sm-2 control-label">First Name:</label>  <div
class="col-sm-10">
    <input type="text" ng-model="fName" ng-disabled="!edit"
placeholder="First Name">  </div>
	</div> <div class="form-group">

<label class="col-sm-2 control-label">Last Name:</label>  <div
class="col-sm-10">
    <input type="text" ng-model="lName" ng-disabled="!edit"
placeholder="Last Name">  </div></div>
	<div class="form-group">

<label class="col-sm-2 control-label">Password:</label>  <div
class="col-sm-10">    <input type="password" ng-model="passw1"
placeholder="Password">  </div></div>
	<div class="form-group">

<label class="col-sm-2 control-label">Repeat:</label>  <div
class="col-sm-10">    <input type="password" ng-model="passw2"
placeholder="Repeat Password">  </div></div>
</form><hr>
<button class="btn btn-success" ng-disabled="error || incomplete">
  <span class="glyphicon glyphicon-save"></span> Save
Changes</button></div>
<script src = "myUsers.js"></script></body>
 </html>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_myusers)


---


## 指令解析


| AngularJS 指令 | 描述 |
| --- | --- |
|







	  AI 思考中...





			* [AngularJS 输入验证](https://www.runoob.com/angularjs-validation.html)
			[AngularJS 包含](https://www.runoob.com/angularjs-include.html) **