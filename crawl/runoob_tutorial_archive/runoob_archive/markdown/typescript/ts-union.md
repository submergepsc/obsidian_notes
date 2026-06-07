# 

- Source: https://www.runoob.com/typescript/ts-union.html

TypeScript 联合类型

联合类型（Union Types）可以通过管道(|)将变量设置多种类型，赋值时可以根据设置的类型来赋值。


**注意**：只能赋值指定的类型，如果赋值其它类型就会报错。


创建联合类型的语法格式如下：


```
Type1|Type2|Type3
```


### 实例


声明一个联合类型：


## TypeScript


```javascript
var val:string|number
val = 12
console.log("数字为 "+ val)
val = "Runoob"
console.log("字符串为 " + val)
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var val;
val = 12;
console.log("数字为 " + val);
val = "Runoob";
console.log("字符串为 " + val);
```


输出结果为：


```
数字为 12
字符串为 Runoob
```


如果赋值其它类型就会报错：


```
var val:string|number
val = true
```


也可以将联合类型作为函数参数使用：


## TypeScript


```javascript
function disp(name:string|string[]) {
        if(typeof name == "string") {
                console.log(name)
        } else {
                var i;
                for(i = 0;i<name.length;i++) {
                console.log(name[i])
                }
        }
}
disp("Runoob")
console.log("输出数组....")
disp(["Runoob","Google","Taobao","Facebook"])
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
function disp(name) {
        if (typeof name == "string") {
                console.log(name);
        }
        else {
                var i;
                for (i = 0; i < name.length; i++) {
                console.log(name[i]);
                }
        }
}
disp("Runoob");
console.log("输出数组....");
disp(["Runoob", "Google", "Taobao", "Facebook"]);
```



输出结果为：


```
Runoob
输出数组....
Runoob
Google
Taobao
Facebook
```


---


## 联合类型数组


我们也可以将数组声明为联合类型：


## TypeScript


```javascript
var arr:number[]|string[];
var i:number;
arr = [1,2,4]
console.log("**数字数组**")

for(i = 0;i<arr.length;i++) {
   console.log(arr[i])
}

arr = ["Runoob","Google","Taobao"]
console.log("**字符串数组**")

for(i = 0;i<arr.length;i++) {
   console.log(arr[i])
}
```


编译以上代码，得到以下 JavaScript 代码：


## JavaScript


```javascript
var arr;
var i;
arr = [1, 2, 4];
console.log("**数字数组**");
for (i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}
arr = ["Runoob", "Google", "Taobao"];
console.log("**字符串数组**");
for (i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}
```


输出结果为：


```
**数字数组**
1
2
4
**字符串数组**
Runoob
Google
Taobao
```









	  AI 思考中...





			** [TypeScript 元组](https://www.runoob.com/ts-tuple.html)
			[TypeScript 接口](https://www.runoob.com/ts-interface.html) **













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