# Angular 2 用户输入

- Source: https://www.runoob.com/angularjs2/angularjs2-user-input.html

用户点击链接、按下按钮或者输入文字时，这些用户的交互行为都会触发 DOM 事件。


本章中，我们将学习如何使用 Angular 事件绑定语法来绑定这些事件。


以下Gif图演示了该实例的操作：


![](https://www.runoob.com/wp-content/uploads/2016/09/angular2-1.gif)


源代码可以在文章末尾下载。


---


## 绑定到用户输入事件


我们可以使用 Angular 事件绑定机制来响应任何 DOM 事件 。


以下实例将绑定了点击事件：


```
<button (click)="onClickMe()">点我!</button>
```


等号左边的 (click) 表示把该按钮的点击事件作为绑定目标 。 等号右边，引号中的文本是一个 模板语句


完整代码如下：


## app/click-me.component.ts 文件：


```javascript
import { Component } from '@angular/core';

@Component({
  selector: 'click-me',
  template: `
    <button (click)="onClickMe()">点我!</button>
    {{clickMessage}}`
})
export class ClickMeComponent {
  clickMessage = '';

  onClickMe() {
    this.clickMessage = '菜鸟教程!';
  }
}
```


---


## 通过 $event 对象取得用户输入


我们可以绑定到所有类型的事件。


让我们试试绑定到一个输入框的 keyup 事件，并且把用户输入的东西回显到屏幕上。


## app/keyup.component.ts (v1) 文件：


```javascript
@Component({
  selector: 'key-up1',
  template: `
    <input (keyup)="onKey($event)">
    <p>{{values}}</p>
  `
})
export class KeyUpComponent_v1 {
  values = '';

  /*
  // 非强类型
  onKey(event:any) {
    this.values += event.target.value + ' | ';
  }
  */
  // 强类型
  onKey(event: KeyboardEvent) {
    this.values += (<HTMLInputElement>event.target).value + ' | ';
  }
}
```


以上代码中我们监听了一个事件并捕获用户输入，Angular 把事件对象存入 $event 变量中。


组件的 onKey() 方法是用来从事件对象中提取出用户输入的，再将输入的值累加到 values 的属性。


---


## 从一个模板引用变量中获得用户输入


你可以通过使用局部模板变量来显示用户数据，模板引用变量通过在标识符前加上井号 (#) 来实现。


下面的实例演示如何使用局部模板变量：


## app/loop-back.component.ts 文件：


```javascript
@Component({
  selector: 'loop-back',
  template: `
    <input #box (keyup)="0">
    <p>{{box.value}}</p>
  `
})
export class LoopbackComponent { }
```


我们在 `` 元素上定义了一个名叫 `box` 的模板引用变量。 `box` 变量引用的就是 `` 元素本身，这意味着我们可以获得 input 元素的 `value` 值，并通过插值表达式把它显示在 `` 标签中。



我们可以使用模板引用变量来修改以上 keyup 的实例：


## app/keyup.components.ts (v2) 文件：


```javascript
@Component({
  selector: 'key-up2',
  template: `
    <input #box (keyup)="onKey(box.value)">
    <p>{{values}}</p>
  `
})
export class KeyUpComponent_v2 {
  values = '';
  onKey(value: string) {
    this.values += value + ' | ';
  }
}
```


---


## 按键事件过滤 ( 通过 key.enter)


我们可以只在用户按下回车 (enter) 键的时候才获取输入框的值。


(keyup) 事件处理语句会听到每一次按键，我们可以过滤按键，比如每一个 $event.keyCode，只有在按下回车键才更新 values 属性。


Angular 可以为我们过滤键盘事件，通过绑定到 Angular 的 keyup.enter 伪事件监听回车键的事件。


## app/keyup.components.ts (v3)：


```javascript
@Component({
  selector: 'key-up3',
  template: `
    <input #box (keyup.enter)="values=box.value">
    <p>{{values}}</p>
  `
})
export class KeyUpComponent_v3 {
  values = '';
}
```


---


## blur( 失去焦点 ) 事件


接下来我们可以使用blur( 失去焦点 ) 事件，它可以再元素失去焦点后更新 values 属性。


以下实例同时监听输入回车键与输入框失去焦点的事件。


## app/keyup.components.ts (v4)：


```javascript
@Component({
  selector: 'key-up4',
  template: `
    <input #box
      (keyup.enter)="values=box.value"
      (blur)="values=box.value">

    <p>{{values}}</p>
  `
})
export class KeyUpComponent_v4 {
  values = '';
}
```


本文所使用的源码可以通过以下方式下载，不包含 node_modules 和 typings 目录。


[源代码下载](https://www.runoob.com/wp-content/uploads/2013/08/angular-quickstart.zip)








	  AI 思考中...





			** [Angular 2 数据显示](https://www.runoob.com/angularjs2-displaying-data.html)
			[Angular 2 表单](https://www.runoob.com/angularjs2-forms.html) **













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