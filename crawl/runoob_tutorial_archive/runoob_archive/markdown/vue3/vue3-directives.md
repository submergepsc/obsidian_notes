# Vue3 指令

- Source: https://www.runoob.com/vue3/vue3-directives.html

Vue 指令（Directives）是 Vue.js 的一项核心功能，它们可以在 HTML 模板中以 **v-** 开头的特殊属性形式使用，用于将响应式数据绑定到 DOM 元素上或在 DOM 元素上进行一些操作。


Vue 指令是带有前缀 **v-** 的特殊 HTML 属性，它赋予 HTML 标签额外的功能。


与传统的 JavaScript 方法相比，使用 Vue 创建响应式页面要容易得多，并且需要的代码更少。


以下是几个常用的 Vue 指令：


| 指令 | 描述 |
| --- | --- |
| v-bind | 用于将 Vue 实例的数据绑定到 HTML 元素的属性上。 |
| v-if | 用于根据表达式的值来条件性地渲染元素或组件。 |
| v-show | v-show 是 Vue.js 提供的一种指令，用于根据表达式的值来条件性地显示或隐藏元素。 |
| v-for | 用于根据数组或对象的属性值来循环渲染元素或组件。 |
| v-on | 用于在 HTML 元素上绑定事件监听器，使其能够触发 Vue 实例中的方法或函数。 |
| v-model | 用于在表单控件和 Vue 实例的数据之间创建双向数据绑定。 |


除了这些常用的指令，Vue 还提供了一些其他的指令，如 v-text、v-html 等，以及自定义指令，让开发者能够更加灵活地操作 DOM 元素。


### 实例

以下是一些使用 Vue 指令的示例：


使用 **v-model** 指令实现表单数据双向绑定：


## 实例


```javascript
<div id="app" class="demo">
    <input type="text" v-model="message">
    <p>{{ message }}</p>
</div>

<script>
const HelloVueApp = {
  data() {
    return {
      message: 'Hello Vue!!'
    }
  }
}

Vue.createApp(HelloVueApp).mount('#app')
</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-directives-1)

使用 **v-bind** 指令将 Vue 实例的数据绑定到 HTML 元素的属性上：


## 实例


```javascript
<div id="app" class="demo">
    <img v-bind:src="imageSrc">
</div>

<script>
const HelloVueApp = {
  data() {
    return {
      imageSrc: 'https://static.jyshare.com/images/code-icon-script.png'
    }
  }
}

Vue.createApp(HelloVueApp).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-directives-2)

使用 **v-if** 和 **v-else** 指令根据表达式的值来条件性地渲染元素或组件：


## 实例


```javascript
<div id="app" class="demo">
    <p v-if="showMessage">Hello Vue!</p>
    <p v-else>Goodbye Vue!</p>
</div>

<script>
const HelloVueApp = {
  data() {
    return {
      showMessage: true
    }
  }
}

Vue.createApp(HelloVueApp).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-directives-3)


使用 **v-for** 指令根据数组的属性值循环渲染元素或组件：


## 实例


```javascript
<div id="app" class="demo">
  <ul>
    <li v-for="item in items" :key="item.id">
      {{ item.text }}
    </li>
  </ul>
</div>

<script>
const HelloVueApp = {
  data() {
    return {
      items: [
        { id: 1, text: 'Item 1' },
        { id: 2, text: 'Item 2' },
        { id: 3, text: 'Item 3' }
      ]
    }
  }
}

Vue.createApp(HelloVueApp).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-directives-4)


使用 v-on 指令在 HTML 元素上绑定事件监听器：


## 实例


```javascript
<div id="app">
  <div id="lightDiv">
    <div v-show="lightOn"></div>
    <img src="https://static.jyshare.com/images/svg/img_lightBulb.svg">
  </div>
  <button v-on:click=" lightOn =! lightOn ">开/关</button>
</div>

<script>
const app = Vue.createApp({
  data() {
    return {
      lightOn: false
    }
  }
})
app.mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-directives-5)

以下是一个使用 **v-show** 指令的示例：


## 实例


```javascript
<div id="hello-vue" class="demo">
    <button v-on:click="showMessage = !showMessage">显示/隐藏</button>
    <p v-show="showMessage">Hello Vue!</p>
</div>

<script>
const HelloVueApp = {
  data() {
    return {
      showMessage: true
    }
  }
}

Vue.createApp(HelloVueApp).mount('#hello-vue')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-directives-6)








	  AI 思考中...





			** [Vue3 组合式 API](https://www.runoob.com/vue3-composition-api.html)
			[Vue3 创建单文件组件(SFC)](https://www.runoob.com/vue3-sfc.html) **













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