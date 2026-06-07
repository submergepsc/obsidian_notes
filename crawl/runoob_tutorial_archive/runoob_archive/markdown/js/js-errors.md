# JavaScript 错误 - throw、try 和 catch

- Source: https://www.runoob.com/js/js-errors.html

---


**try** 语句测试代码块的错误。


**catch** 语句处理错误。


**throw** 语句创建自定义错误。


**finally** 语句在 try 和 catch 语句之后，无论是否有触发异常，该语句都会执行。


---


## JavaScript 错误


当 JavaScript 引擎执行 JavaScript 代码时，会发生各种错误。


可能是语法错误，通常是程序员造成的编码错误或错别字。


可能是拼写错误或语言中缺少的功能（可能由于浏览器差异）。


可能是由于来自服务器或用户的错误输出而导致的错误。


当然，也可能是由于许多其他不可预知的因素。


---


## JavaScript 抛出（throw）错误


当错误发生时，当事情出问题时，JavaScript 引擎通常会停止，并生成一个错误消息。


描述这种情况的技术术语是：JavaScript 将**抛出**一个错误。


---


## JavaScript try 和 catch


**try** 语句允许我们定义在执行时进行错误测试的代码块。


**catch** 语句允许我们定义当 try 代码块发生错误时，所执行的代码块。


JavaScript 语句 **try** 和 **catch** 是成对出现的。


### 语法


```javascript
try {
    ...    //异常的抛出
} catch(e) {
    ...    //异常的捕获与处理
} finally {
    ...    //结束处理
}
```


## 实例


在下面的例子中，我们故意在 try 块的代码中写了一个错字。


catch 块会捕捉到 try 块中的错误，并执行代码来处理它。


## 实例


```javascript
var txt="";
function message()
{
    try {
        adddlert("Welcome guest!");
    } catch(err) {
        txt="本页有一个错误。\n\n";
        txt+="错误描述：" + err.message + "\n\n";
        txt+="点击确定继续。\n\n";
        alert(txt);
    }
}
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_try_catch)


### finally 语句

finally 语句不论之前的 try 和 catch 中是否产生异常都会执行该代码块。


## 实例


```javascript
function myFunction() {
  var message, x;
  message = document.getElementById("p01");
  message.innerHTML = "";
  x = document.getElementById("demo").value;
  try {
    if(x == "") throw "值是空的";
    if(isNaN(x)) throw "值不是一个数字";
    x = Number(x);
    if(x > 10) throw "太大";
    if(x < 5) throw "太小";
  }
  catch(err) {
    message.innerHTML = "错误: " + err + ".";
  }
  finally {
    document.getElementById("demo").value = "";
  }
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_finally_error)


---


## Throw 语句


throw 语句允许我们创建自定义错误。


正确的技术术语是：创建或抛出异常**（exception）。


如果把 throw 与 try 和 catch 一起使用，那么您能够控制程序流，并生成自定义的错误消息。


### 语法


throw *exception*


异常可以是 JavaScript 字符串、数字、逻辑值或对象。


## 实例


本例检测输入变量的值。如果值是错误的，会抛出一个异常（错误）。catch 会捕捉到这个错误，并显示一段自定义的错误消息：


## 实例


```javascript
function myFunction() {
    var message, x;
    message = document.getElementById("message");
    message.innerHTML = "";
    x = document.getElementById("demo").value;
    try {
        if(x == "")  throw "值为空";
        if(isNaN(x)) throw "不是数字";
        x = Number(x);
        if(x < 5)    throw "太小";
        if(x > 10)   throw "太大";
    }
    catch(err) {
        message.innerHTML = "错误: " + err;
    }
}
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_throw_error)


请注意，如果 getElementById 函数出错，上面的例子也会抛出一个错误。








	  AI 思考中...





			** [JavaScript break 和 continue 语句](https://www.runoob.com/js-break.html)
			[JavaScript 表单验证](https://www.runoob.com/js-form-validation.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

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