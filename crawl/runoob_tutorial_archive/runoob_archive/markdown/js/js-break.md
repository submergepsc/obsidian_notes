# JavaScript break 和 continue 语句

- Source: https://www.runoob.com/js/js-break.html

---


break 语句用于跳出循环。


continue 用于跳过循环中的一个迭代。


---


## break 语句


我们已经在本教程之前的章节中见到过 break 语句。它用于跳出 switch() 语句。


break 语句可用于跳出循环。


break 语句跳出循环后，会继续执行该循环之后的代码（如果有的话）：


## 实例


```javascript
for (i=0;i<10;i++)
{
    if (i==3)
    {
        break;
    }
    x=x + "The number is " + i + "<br>";
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_break)


由于这个 if 语句只有一行代码，所以可以省略花括号：


```javascript
for (i=0;i<10;i++)
{
    if (i==3) break;
    x=x + "The number is " + i + "<br>";
}
```


---


## continue 语句


continue 语句**中断当前的循环中的迭代，然后继续循环下一个迭代。 以下例子在值为 3 时，直接跳过：


## for 实例


```javascript
for (i=0;i<=10;i++)
{
    if (i==3) continue;
    x=x + "The number is " + i + "<br>";
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_continue)


## while 实例


```javascript
while (i < 10){
  if (i == 3){
    i++;    //加入i++不会进入死循环
    continue;
  }
  x= x + "该数字为 " + i + "<br>";
  i++;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_while_continue)


---


## JavaScript 标签


正如您在 switch 语句那一章中看到的，可以对 JavaScript 语句进行标记。


如需标记 JavaScript 语句，请在语句之前加上冒号：


```javascript
label:
statements
```


break 和 continue 语句仅仅是能够跳出代码块的语句。


语法:


```javascript
break labelname;

continue labelname;
```


continue 语句（带有或不带标签引用）只能用在循环中。


break 语句（不带标签引用），只能用在循环或 switch 中。


通过标签引用，break 语句可用于跳出任何 JavaScript 代码块：


## 实例


```javascript
cars=["BMW","Volvo","Saab","Ford"];
list:
{
    document.write(cars[0] + "<br>");
    document.write(cars[1] + "<br>");
    document.write(cars[2] + "<br>");
    break list;
    document.write(cars[3] + "<br>");
    document.write(cars[4] + "<br>");
    document.write(cars[5] + "<br>");
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_break_list)








	  AI 思考中...





			** [JavaScript while 循环](https://www.runoob.com/js-loop-while.html)
			[JavaScript 错误 – Throw、Try 和 Catch](https://www.runoob.com/js-errors.html) **