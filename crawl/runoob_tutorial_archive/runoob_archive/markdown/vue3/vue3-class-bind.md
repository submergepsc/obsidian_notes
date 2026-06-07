# Vue3 样式绑定

- Source: https://www.runoob.com/vue3/vue3-class-bind.html

## Vue.js class


class 与 style 是 HTML 元素的属性，用于设置元素的样式，我们可以用 v-bind 来设置样式属性。


v-bind 在处理 class 和 style 时， 表达式除了可以使用字符串之外，还可以是对象或数组。


**v-bind:class** 可以简写为 **:class**。


---

## class 属性绑定


我们可以为 **v-bind:class** 设置一个对象，从而动态的切换 **class**:


## 实例 1


实例中将 isActive 设置为 true 显示了一个绿色的 div 块，如果设置为 false 则不显示：


```javascript
<div :class="{ 'active': isActive }"></div>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class1)


以上实例 div class 渲染结果为：


```
<div class="active"></div>
```


我们也可以在对象中传入更多属性用来动态切换多个 class 。


此外，**:class** 指令也可以与普通的 class 属性共存。


## 实例 2


text-danger 类背景颜色覆盖了 active 类的背景色：


```javascript
<div class="static" :class="{ 'active' : isActive, 'text-danger' : hasError }">
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class2)


以上实例 div class 渲染结果为：


```
<div class="static text-danger"></div>
```


![](https://www.runoob.com/wp-content/uploads/2021/03/EF8BD574-33D2-4790-BC98-C1820712F7EA.jpg)


当 isActive 或者 hasError 变化时，class 属性值也将相应地更新。例如，如果 active 的值为 true，class 列表将变为 "static active text-danger"。


我们也可以直接绑定数据里的一个对象：


## 实例 3


text-danger 类背景颜色覆盖了 active 类的背景色：


```javascript
<div id="app">
    <div class="static" :class="classObject"></div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class3)


实例 3 与 实例 2 的渲染结果是一样的。


此外，我们也可以在这里绑定一个返回对象的计算属性。这是一个常用且强大的模式：


## 实例 4


```javascript
data() {
  return {
    isActive: true,
    error: null
  }
},
computed: {
  classObject() {
    return {
      active: this.isActive && !this.error,
      'text-danger': this.error && this.error.type === 'fatal'
    }
  }
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class4)


### 数组语法


我们可以把一个数组传给 v-bind:class** ，实例如下：


## 实例 5


```javascript
<div class="static" :class="[activeClass, errorClass]"></div>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class5)

以上实例 div class 渲染结果为：


```
<div class="static active text-danger"></div>
```


我们还可以使用三元表达式来切换列表中的 class ：


## 实例 6


errorClass 是始终存在的，isActive 为 true 时添加 activeClass 类：


```javascript
<div id="app">
    <div class="static" :class="[isActive ? activeClass : '', errorClass]"></div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class6)

以上实例 div class 渲染结果为：


```
<div class="static text-danger"></div>
```


---


## Vue.js style(内联样式)


我们可以在 **v-bind:style** 直接设置样式，可以简写为 **:style**：


## 实例 7


```javascript
<div id="app">
    <div :style="{ color: activeColor, fontSize: fontSize + 'px' }">菜鸟教程</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class7)

以上实例 div style 渲染结果为：


```
<div style="color: red; font-size: 30px;">菜鸟教程</div>
```


![](https://www.runoob.com/wp-content/uploads/2021/03/1B6E97AF-98AB-4288-A974-B67D4D2211CB.jpg)


也可以直接绑定到一个样式对象**，让模板更清晰：


## 实例 8


```javascript
<div id="app">
  <div :style="styleObject">菜鸟教程</div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class8)


v-bind:style** 可以使用数组将多个样式对象应用到一个元素上：


## 实例 9


```javascript
<div id="app">
  <div :style="[baseStyles, overridingStyles]">菜鸟教程</div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class9)


> 注意：当 v-bind:style** 使用需要特定前缀的 CSS 属性时，如 transform ，Vue.js 会自动侦测并添加相应的前缀。


### 多重值

可以为 style 绑定中的 property 提供一个包含多个值的数组，常用于提供多个带前缀的值，例如：


```
<div :style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }"></div>
```


这样写只会渲染数组中最后一个被浏览器支持的值。在本例中，如果浏览器支持不带浏览器前缀的 flexbox，那么就只会渲染 display: flex。


---

## 组件上使用 class 属性

当你在带有单个根元素的自定义组件上使用 class 属性时，这些 class 将被添加到该元素中。此元素上的现有 class 将不会被覆盖。


## 实例 10


```javascript
<div id="app">
    <runoob class="classC classD"></runoob>
</div>

<script>
// 创建一个Vue 应用
const app = Vue.createApp({})

// 定义一个名为 runoob的新全局组件
app.component('runoob', {
    template: '<h1 class="classA classB">I like runoob!</h1>'
})

app.mount('#app')
</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class10)


以上实例 div class 渲染结果为：


```
<h1 class="classA classB classC classD">I like runoob!</h1>
```


![](https://www.runoob.com/wp-content/uploads/2021/03/CE467D96-FC8B-4FD2-A6B6-68015F777437.jpg)


对于带数据绑定 class 也同样适用：


```
<my-component :class="{ active: isActive }"></my-component>
```


当 isActive 为 true 时，HTML 将被渲染成为：


```
<p class="active">Hi</p>
```


如果你的组件有多个根元素，你需要定义哪些部分将接收这个类。可以使用 **$attrs** 组件属性执行此操作：


## 实例 11


```javascript
<div id="app">
    <runoob class="classA"></runoob>
</div>

<script>
const app = Vue.createApp({})

app.component('runoob', {
  template: `
    <p :class="$attrs.class">I like runoob!</p>
    <span>这是一个子组件</span>
  `
})

app.mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-class11)


注意**：template 中 **`** 是反引号，不是单引号 **'**。


以上实例 div class 渲染结果为：


```
<div id="app" data-v-app=""><p class="classA">I like runoob!</p><span>这是一个子组件</span></div>
```


![](https://www.runoob.com/wp-content/uploads/2021/03/64339E69-CC45-4AD8-82D0-5EB00F7B9E89.jpg)









	  AI 思考中...





			** [Vue3 监听属性](https://www.runoob.com/vue3-watch.html)
			[Vue3 事件处理](https://www.runoob.com/vue3-events.html) **













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