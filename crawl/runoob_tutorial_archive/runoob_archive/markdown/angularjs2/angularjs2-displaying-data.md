# Angular 2 数据显示

- Source: https://www.runoob.com/angularjs2/angularjs2-displaying-data.html

本章节我们将为大家介绍如何将数据显示到用户界面上，可以使用以下三种方式：


- 通过插值表达式显示组件的属性
- 通过 NgFor 显示数组型属性
- 通过 NgIf 实现按条件显示


---


## 通过插值表达式显示组件的属性


要显示组件的属性，插值是最简单的方式，格式为：**{{属性名}}**。


以下代码基于 [Angular 2 TypeScript 环境配置](https://www.runoob.com/angularjs2-typescript-setup.html) 来创建，你可以在该章节上下载源码，并修改以下提到的几个文件。


## app/app.component.ts 文件：


```javascript
import { Component } from '@angular/core';
@Component({
  selector: 'my-app',
  template: `
    <h1>{{title}}</h1>
    <h2>我喜欢的网站: {{mySite}}</h2>
    `
})
export class AppComponent {
  title = '站点列表';
  mySite = '菜鸟教程';
}
```


Angular 会自动从组件中提取 title 和 mySite 属性的值，并显示在浏览器中，显示信息如下：


![](https://www.runoob.com/wp-content/uploads/2016/09/BAD05521-3124-426C-8A6B-5AF28613557A.jpg)

**

注意：**模板是包在反引号 (`) 中的一个多行字符串，而不是单引号 (')。


---


## 使用 ngFor 显示数组属性


我们也可以循环输出多个站点，修改以下文件：


## app/app.component.ts 文件：


```javascript
import { Component } from '@angular/core';
@Component({
  selector: 'my-app',
  template: `
    <h1>{{title}}</h1>
    <h2>我喜欢的网站: {{mySite}}</h2>
    <p>网站列表:</p>
    <ul>
      <li *ngFor="let site of sites">
        {{ site }}
      </li>
    </ul>
    `
})

export class AppComponent {
  title = '站点列表';
  sites = ['菜鸟教程', 'Google', 'Taobao', 'Facebook'];
  mySite = this.sites[0];
}
```


代码中我们在模板使用 Angular 的 ngFor 指令来显示 sites 列表中的每一个条目，不要忘记 *ngFor 中的前导星号 (*) 。。


修改后，浏览器显示如下所示：


![](https://www.runoob.com/wp-content/uploads/2016/09/588F2110-7BAC-40A3-B8A9-6A8DD097BBF0.jpg)


实例中 ngFor 循环了一个数组， 事实上 ngFor 可以迭代任何可迭代的对象。


接下来我们在 app 目录下创建 site.ts 的文件，代码如下：


## app/site.ts 文件：


```javascript
export class Site {
  constructor(
    public id: number,
    public name: string) { }
}
```


以上代码中定义了一个带有构造函数和两个属性： id 和 name 的类。


接着我们循环输出 Site 类的 name 属性：


## app/app.component.ts 文件：


```javascript
import { Component } from '@angular/core';
import { Site } from './site';

@Component({
  selector: 'my-app',
  template: `
    <h1>{{title}}</h1>
    <h2>我喜欢的网站: {{mySite.name}}</h2>
    <p>网站列表:</p>
    <ul>
      <li *ngFor="let site of sites">
        {{ site.name }}
      </li>
    </ul>
    `
})

export class AppComponent {
  title = '站点列表';
  sites = [
      new Site(1, '菜鸟教程'),
      new Site(2, 'Google'),
      new Site(3, 'Taobao'),
      new Site(4, 'Facebook')
      ];
  mySite = this.sites[0];
}
```


修改后，浏览器显示如下所示：


![](https://www.runoob.com/wp-content/uploads/2016/09/588F2110-7BAC-40A3-B8A9-6A8DD097BBF0.jpg)


---


## 通过 NgIf 进行条件显示


我们可以使用 NgIf 来设置输出指定条件的数据。


以下实例中我们判断如果网站数 3 个以上，输出提示信息：修改以下 app.component.ts 文件，代码如下：


## app/app.component.ts 文件：


```javascript
import { Component } from '@angular/core';
import { Site } from './site';

@Component({
  selector: 'my-app',
  template: `
    <h1>{{title}}</h1>
    <h2>我喜欢的网站: {{mySite.name}}</h2>
    <p>网站列表:</p>
    <ul>
      <li *ngFor="let site of sites">
       {{ site.name }}
      </li>
    </ul>
    <p *ngIf="sites.length > 3">你有很多个喜欢的网站!</p>
    `
})

export class AppComponent {
  title = '站点列表';
  sites = [
      new Site(1, '菜鸟教程'),
      new Site(2, 'Google'),
      new Site(3, 'Taobao'),
      new Site(4, 'Facebook')
      ];
  mySite = this.sites[0];
}
```


修改后，浏览器显示如下所示，底部多了个提示信息：


![](https://www.runoob.com/wp-content/uploads/2016/09/7931418A-C914-46D3-9EF6-85CAF666FA9B.jpg)








	  AI 思考中...





			** [Angular 2 架构](https://www.runoob.com/angularjs2-architecture.html)
			[Angular 2 用户输入](https://www.runoob.com/angularjs2-user-input.html) **













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