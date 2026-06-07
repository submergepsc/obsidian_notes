# JavaScript typeof, null, 和 undefined

- Source: https://www.runoob.com/js/js-typeof.html

---


## typeof 操作符


你可以使用 typeof 操作符来检测变量的数据类型。


## 实例


```javascript
typeof "John"                // 返回 string
typeof 3.14                  // 返回 number
typeof false                 // 返回 boolean
typeof [1,2,3,4]             // 返回 object
typeof {name:'John', age:34} // 返回 object
```


**
 [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_typeof_typeof)


|  | 在JavaScript中，数组是一种特殊的对象类型。 因此 typeof [1,2,3,4] 返回 object。正确检测数组的方法：
```
Array.isArray([1,2,3]); // true
[1,2,3] instanceof Array; // true
```
 |
| --- | --- |

**typeof** 是 JavaScript 中的一个操作符，用于返回给定变量的数据类型。

完整类型检测表:**


| 表达式 | 返回值 | 说明 |
| --- | --- | --- |
| typeof undefined | "undefined" | 未定义的值 |
| typeof true | "boolean" | 布尔值 |
| typeof 42 | "number" | 所有数字类型 |
| typeof "text" | "string" | 字符串 |
| typeof {a:1} | "object" | 对象、数组、null |
| typeof function(){} | "function" | 函数 |
| typeof Symbol() | "symbol" | ES6新增符号类型 |
| typeof BigInt(10) | "bigint" | ES2020新增大整数类型 |


检测未定义变量：


```
if (typeof variable === "undefined") {...}
```


检测函数是否存在：


```
if (typeof myFunction === "function") {...}
```


注意数组和null的特殊情况：


```
// 正确检测数组
if (Array.isArray(myVar)) {...}

// 正确检测null
if (myVar === null) {...}
```


---


## null


在 JavaScript 中 null 表示 "什么都没有"。


null是一个只有一个值的特殊类型。表示一个空对象引用。


|  | 用 typeof 检测 null 返回是object。 |
| --- | --- |


你可以设置为 null 来清空对象:


## 实例


```javascript
var
person = null;           // 值为 null(空), 但类型为对象
```


**
 [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_typeof_null)


你可以设置为 undefined 来清空对象:


## 实例


```javascript
var
person = undefined;     // 值为 undefined,
    类型为 undefined
```


 [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_typeof_undefined_1)


---


## undefined


在 JavaScript 中, undefined** 是一个没有设置值的变量。


**typeof** 一个没有值的变量会返回 ** undefined**。


## 实例


```javascript
var person;                  // 值为 undefined(空), 类型是undefined
```


**
 [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_typeof_undefined)


任何变量都可以通过设置值为 undefined** 来清空。 类型为 **undefined**.


## 实例


```javascript
person = undefined;          // 值为 undefined,
    类型是undefined
```


 [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_typeof_undefined_2)


---


## undefined 和 null 的区别


## 实例


null 和 undefined 的值相等，但类型不等：


```javascript
typeof undefined
    // undefinedtypeof null
    // objectnull === undefined
    // falsenull == undefined
    // true
```


 [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_typeof_undefined_3)









	  AI 思考中...





			** [JavaScript 正则表达式](https://www.runoob.com/js-regexp.html)
			[JavaScript 类型转换](https://www.runoob.com/js-type-conversion.html) **