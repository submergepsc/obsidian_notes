# JavaScript 作用域

- Source: https://www.runoob.com/js/js-scope.html

---


作用域是可访问变量的集合。


---


## JavaScript 作用域


在 JavaScript 中, 对象和函数同样也是变量。


**在 JavaScript 中, 作用域为可访问变量，对象，函数的集合。**


JavaScript 函数作用域: 作用域在函数内修改。


---


## JavaScript 局部作用域


变量在函数内声明，变量为局部变量，具有局部作用域。


局部变量：只能在函数内部访问。


## 实例


```javascript
// 此处不能调用 carName 变量
function myFunction() {
    var carName = "Volvo";
    // 函数内可调用 carName 变量
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_scope_local)


因为局部变量只作用于函数内，所以不同的函数可以使用相同名称的变量。


局部变量在函数开始执行时创建，函数执行完后局部变量会自动销毁。


---


## JavaScript 全局变量


变量在函数外定义，即为全局变量。


全局变量有 全局作用域**: 网页中所有脚本和函数均可使用。


## 实例


```javascript
var carName = " Volvo";

// 此处可调用 carName 变量
function myFunction() {
    // 函数内可调用 carName 变量
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_scope_global)


如果变量在函数内没有声明（没有使用 var 关键字），该变量为全局变量。


以下实例中 carName 在函数内，但是为全局变量。


## 实例


```javascript
// 此处可调用 carName 变量

function myFunction() {
    carName = "Volvo";
    // 此处可调用 carName 变量
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_local_global)


---


## JavaScript 变量生命周期


JavaScript 变量生命周期在它声明时初始化。


局部变量在函数执行完毕后销毁。


全局变量在页面关闭后销毁。


---


## 函数参数


函数参数只在函数内起作用，是局部变量。


---


## HTML 中的全局变量


在 HTML 中, 全局变量是 window 对象，所以 window 对象可以调用函数内的未声明（未加 var)的局部变量。


注意：**所有全局变量都属于 window 对象。


## 实例


```javascript
//此处可使用 window.carName

function myFunction() {
    carName = "Volvo";
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_scope_window)


---


## 你知道吗?


|  | 你的全局变量，或者函数，可以覆盖 window 对象的变量或者函数。局部变量，包括 window 对象可以覆盖全局变量和函数。 |
| --- | --- |


在 JavaScript 中，函数内部的局部变量通常不可以直接被外部作用域访问，但有几种方式可以将函数内的局部变量暴露给外部作用域，具体如下：


- **通过全局对象：**在函数内部，可以通过将局部变量赋值给 window 对象的属性来使其成为全局可访问的。例如，使用 **window.a = a;** 语句，可以在函数外部通过 **window.a** 访问到这个局部变量的值。
- **定义全局变量：**在函数内部不使用 **var、let** 或 **const** 等关键字声明变量时，该变量会被视为全局变量，从而可以在函数外部访问。但这种做法通常不推荐，因为它可能导致意外的副作用和代码难以维护。
- **返回值：**可以通过在函数内部使用 **return** 语句返回局部变量的值，然后在函数外部接收这个返回值。这样，虽然局部变量本身不会被暴露，但其值可以通过函数调用传递到外部。
- **闭包：**JavaScript 中的闭包特性允许内部函数访问外部函数的局部变量。即使外部函数执行完毕后，其局部变量仍然可以被内部函数引用。
- **属性和方法：**定义在全局作用域中的变量和函数都会变成 window 对象的属性和方法，因此可以在调用时省略 window，直接使用变量名或函数名。








	  AI 思考中...





			** [JavaScript JSON](https://www.runoob.com/js-json.html)
			[JavaScript 事件](https://www.runoob.com/js-events.html) **