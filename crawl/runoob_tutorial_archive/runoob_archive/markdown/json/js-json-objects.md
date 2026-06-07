# JSON 对象

- Source: https://www.runoob.com/json/js-json-objects.html

---


## 对象语法


## 实例


```json
{ "name":"runoob", "alexa":10000, "site":null }
```


JSON 对象使用在大括号 **{...}** 中书写。


对象可以包含多个 **key/value（键/值）**对。


key 必须是字符串，value 可以是合法的 JSON 数据类型（字符串, 数字, 对象, 数组, 布尔值或 null）。


key 和 value 中使用冒号 **:** 分割。


每个 key/value 对使用逗号 **,** 分割。

![](https://www.runoob.com/wp-content/uploads/2013/09/object.png)


---


## 访问对象值


你可以使用点号 **.** 来访问对象的值：


## 实例


```json
var myObj, x;
myObj = { "name":"runoob", "alexa":10000, "site":null };
x = myObj.name;
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_object_dot)


你也可以使用中括号（[]）来访问对象的值：


## 实例


```json
var myObj, x;
myObj = { "name":"runoob", "alexa":10000, "site":null };
x = myObj["name"];
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_object_bracket)


---


## 循环对象


你可以使用 for-in 来循环对象的属性：


## 实例


```json
var myObj = { "name":"runoob", "alexa":10000, "site":null };
for (x in myObj) {
    document.getElementById("demo").innerHTML += x + "<br>";
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_object_loop)


在 for-in 循环对象的属性时，使用中括号（[]）来访问属性的值：


## 实例


```json
var myObj = { "name":"runoob", "alexa":10000, "site":null };
for (x in myObj) {
    document.getElementById("demo").innerHTML += myObj[x] + "<br>";
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_object_loop_bracket)


---


## 嵌套 JSON 对象


JSON 对象中可以包含另外一个 JSON 对象：


## 实例


```json
myObj = {
    "name":"runoob",
    "alexa":10000,
    "sites": {
        "site1":"www.runoob.com",
        "site2":"m.runoob.com",
        "site3":"c.runoob.com"
    }
}
```


你可以使用点号 **.** 或者中括号 **[...]** 来访问嵌套的 JSON 对象。


## 实例


```json
x = myObj.sites.site1;
// 或者
x = myObj.sites["site1"];
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_object_nested)


---


## 修改值


你可以使用点号 **.** 来修改 JSON 对象的值：


## 实例


```json
myObj.sites.site1 = "www.google.com";
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_object_modify)


你可以使用中括号 **[...]** 来修改 JSON 对象的值：


## 实例


```json
myObj.sites["site1"] = "www.google.com";
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_object_modify_bracket)


---


## 删除对象属性


我们可以使用 delete** 关键字来删除 JSON 对象的属性：


## 实例


```json
delete myObj.sites.site1;
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_object_delete)


你可以使用中括号 **[...]** 来删除 JSON 对象的属性：


## 实例


```json
delete myObj.sites["site1"]
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_object_delete_bracket)








	  AI 思考中...





			** [JSONP 教程](https://www.runoob.com/json-jsonp.html)
			[JSON 数组](https://www.runoob.com/js-json-arrays.html) **