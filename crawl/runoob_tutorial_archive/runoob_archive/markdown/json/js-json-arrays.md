# JSON 数组

- Source: https://www.runoob.com/json/js-json-arrays.html

---


## 数组作为 JSON 对象


## 实例


```json
[ "Google", "Runoob", "Taobao" ]
```


JSON 数组在中括号中书写。


中括号 **[]** 保存的数组是值（value）的有序集合。一个数组以左中括号 **[** 开始， 右中括号 **]** 结束，值之间使用逗号 **,** 分隔。


![](https://www.runoob.com/wp-content/uploads/2013/09/array.png)


JSON 中数组值必须是合法的 JSON 数据类型（字符串, 数字, 对象, 数组, 布尔值或 null）。


JavaScript 中，数组值可以是以上的 JSON 数据类型，也可以是 JavaScript 的表达式，包括函数，日期，及 *undefined*。


---


## JSON 对象中的数组


对象属性的值可以是一个数组：


## 实例


```json
{
"name":"网站",
"num":3,
"sites":[ "Google", "Runoob", "Taobao" ]
}
```


我们可以使用索引值来访问数组：


## 实例


```json
x = myObj.sites[0];
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_array_access)


---


## 循环数组


你可以使用 for-in 来访问数组：


## 实例


```json
for (i in myObj.sites) {
    x += myObj.sites[i] + "<br>";
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_array_loop_in)


你也可以使用 for 循环：


## 实例


```json
for (i = 0; i < myObj.sites.length; i++) {
    x += myObj.sites[i] + "<br>";
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_array_loop)


---


## 嵌套 JSON 对象中的数组


JSON 对象中数组可以包含另外一个数组，或者另外一个 JSON 对象：


## 实例


```json
myObj = {
    "name":"网站",
    "num":3,
    "sites": [
        { "name":"Google", "info":[ "Android", "Google 搜索", "Google 翻译" ] },
        { "name":"Runoob", "info":[ "菜鸟教程", "菜鸟工具", "菜鸟微信" ] },
        { "name":"Taobao", "info":[ "淘宝", "网购" ] }
    ]
}
```


我们可以使用 for-in 来循环访问每个数组：


## 实例


```json
for (i in myObj.sites) {
    x += "<h1>" + myObj.sites[i].name + "</h1>";
    for (j in myObj.sites[i].info) {
        x += myObj.sites[i].info[j] + "<br>";
    }
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_array_nested)


---


## 修改数组值


你可以使用索引值来修改数组值：


## 实例


```json
myObj.sites[1] = "Github";
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_array_modify)


---


## 删除数组元素


我们可以使用 delete** 关键字来删除数组元素：


## 实例


```json
delete myObj.sites[1];
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjson_array_delete)









	  AI 思考中...





			** [JSON 对象](https://www.runoob.com/js-json-objects.html)
			[JSON.parse()](https://www.runoob.com/json-parse.html) **