# JavaScript switch 语句

- Source: https://www.runoob.com/js/js-switch.html

---


switch 语句用于基于不同的条件来执行不同的动作。


---


## JavaScript switch 语句


请使用 switch 语句来选择要执行的多个代码块之一。


## 语法


```javascript
switch(n)
{
    case 1:
        执行代码块 1
        break;
    case 2:
        执行代码块 2
        break;
    default:
        与 case 1 和 case 2 不同时执行的代码
}
```


工作原理：首先设置表达式 *n*（通常是一个变量）。随后表达式的值会与结构中的每个 case 的值做比较。如果存在匹配，则与该 case 关联的代码块会被执行。请使用 **break **来阻止代码自动地向下一个 case 运行。


## 实例


显示今天的星期名称。请注意 Sunday=0, Monday=1, Tuesday=2, 等等：


```javascript
var d=new Date().getDay();
switch (d)
{
  case 0:x="今天是星期日";
  break;
  case 1:x="今天是星期一";
  break;
  case 2:x="今天是星期二";
  break;
  case 3:x="今天是星期三";
  break;
  case 4:x="今天是星期四";
  break;
  case 5:x="今天是星期五";
  break;
  case 6:x="今天是星期六";
  break;
}
```


*x* 的运行结果：


```javascript

```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_switch)


## default 关键词


请使用 default 关键词来规定匹配不存在时做的事情：


## 实例


如果今天不是星期六或星期日，则会输出默认的消息：


```javascript
var d=new Date().getDay();
switch (d)
{
    case 6:x="今天是星期六";
    break;
    case 0:x="今天是星期日";
    break;
    default:
    x="期待周末";
}
document.getElementById("demo").innerHTML=x;
```


*x* 的运行结果：


```javascript

```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_switch2)








	  AI 思考中...





			** [JavaScript If…Else 语句](https://www.runoob.com/js-if-else.html)
			[JavaScript for 循环](https://www.runoob.com/js-loop-for.html) **