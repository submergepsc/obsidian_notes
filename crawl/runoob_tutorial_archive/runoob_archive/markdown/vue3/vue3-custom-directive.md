# Vue3 自定义指令

- Source: https://www.runoob.com/vue3/vue3-custom-directive.html

除了默认设置的核心指令( v-model 和 v-show ), Vue 也允许注册自定义指令。


下面我们注册一个全局指令 v-focus, 该指令的功能是在页面加载时，元素获得焦点：


## 实例


```javascript
<div id="app">
    <p>页面载入时，input 元素自动获取焦点：</p>
    <input v-focus>
</div>

<script>
const app = Vue.createApp({})
// 注册一个全局自定义指令 `v-focus`
app.directive('focus', {
  // 当被绑定的元素挂载到 DOM 中时……
  mounted(el) {
    // 聚焦元素
    el.focus()
  }
})
app.mount('#app')
</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-custom-directive1)


我们也可以在实例使用 directives 选项来注册局部指令，这样指令只能在这个实例中使用：


## 实例


```javascript
<div id="app">
    <p>页面载入时，input 元素自动获取焦点：</p>
    <input v-focus>
</div>

<script>
const app = {
   data() {
      return {
      }
   },
   directives: {
      focus: {
         // 指令的定义
         mounted(el) {
            el.focus()
         }
      }
   }
}

Vue.createApp(app).mount('#app')
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-custom-directive2)


---


## 钩子


### 钩子函数


指令定义函数提供了几个钩子函数（可选）：


- `created `: 在绑定元素的属性或事件监听器被应用之前调用。
- `beforeMount `: 指令第一次绑定到元素并且在挂载父组件之前调用。。
- `mounted `: 在绑定元素的父组件被挂载后调用。。
- `beforeUpdate`: 在更新包含组件的 VNode 之前调用。。
- `updated`: 在包含组件的 VNode 及其子组件的 VNode 更新后调用。
- `beforeUnmount`: 当指令与在绑定元素父组件卸载之前时，只调用一次。
- `unmounted`: 当指令与元素解除绑定且父组件已卸载时，只调用一次。


## 实例


```javascript
import { createApp } from 'vue'
const app = createApp({})

// 注册
app.directive('my-directive', {
  // 指令是具有一组生命周期的钩子：
  // 在绑定元素的 attribute 或事件监听器被应用之前调用
  created() {},
  // 在绑定元素的父组件挂载之前调用
  beforeMount() {},
  // 绑定元素的父组件被挂载时调用
  mounted() {},
  // 在包含组件的 VNode 更新之前调用
  beforeUpdate() {},
  // 在包含组件的 VNode 及其子组件的 VNode 更新之后调用
  updated() {},
  // 在绑定元素的父组件卸载之前调用
  beforeUnmount() {},
  // 卸载绑定元素的父组件时调用
  unmounted() {}
})

// 注册 (功能指令)
app.directive('my-directive', () => {
  // 这将被作为 `mounted` 和 `updated` 调用
})

// getter, 如果已注册，则返回指令定义
const myDirective = app.directive('my-directive')
```


### 钩子函数参数


钩子函数的参数有：


el**


**el** 指令绑定到的元素。这可用于直接操作 DOM。


**binding**


binding 是一个对象，包含以下属性：


- `instance`：使用指令的组件实例。
- `value`：传递给指令的值。例如，在 `v-my-directive="1 + 1"` 中，该值为 `2`。
- `oldValue`：先前的值，仅在 `beforeUpdate` 和 `updated` 中可用。值是否已更改都可用。
- `arg`：参数传递给指令 (如果有)。例如在 `v-my-directive:foo` 中，arg 为 `"foo"`。
- `modifiers`：包含修饰符 (如果有) 的对象。例如在 `v-my-directive.foo.bar` 中，修饰符对象为 `{foo: true，bar: true}`。
- `dir`：一个对象，在注册指令时作为参数传递。例如，在以下指令中：


```
app.directive('focus', {
  mounted(el) {
    el.focus()
  }
})
```


dir 将会是以下对象：


```
{
  mounted(el) {
    el.focus()
  }
}
```


**vnode**


作为 el 参数收到的真实 DOM 元素的蓝图。


** prevNode**

上一个虚拟节点，仅在 beforeUpdate 和 updated 钩子中可用。


以下实例演示了这些参数的使用：


## 实例


```javascript
<div id="app">
   <div v-runoob="{ name: '菜鸟教程', url: 'www.runoob.com' }"></div>
</div>
​
<script>
const app = Vue.createApp({})
app.directive('runoob', (el, binding, vnode) => {
console.log(binding.value.name) // => "菜鸟教程"
console.log(binding.value.url) // => "www.runoob.com"
var s = JSON.stringify
el.innerHTML = s(binding.value)
})
app.mount('#app')
</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-custom-directive3)


有时候我们不需要其他钩子函数，我们可以简写函数，如下格式：


```
Vue.directive('runoob', function (el, binding) {
  // 设置指令的背景颜色
  el.style.backgroundColor = binding.value.color
})
```


指令函数可接受所有合法的 JavaScript 表达式，以下实例传入了 JavaScript 对象：


## 实例


```javascript
<div id="app">
    <div v-runoob="{ color: 'green', text: '菜鸟教程!' }"></div>
</div>

<script>
Vue.directive('runoob', function (el, binding) {
    // 简写方式设置文本及背景颜色
    el.innerHTML = binding.value.text
    el.style.backgroundColor = binding.value.color
})
new Vue({
  el: '#app'
})
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-custom-directive4)









	  AI 思考中...





			** [Vue3 表单](https://www.runoob.com/vue3-forms.html)
			[Vue3 路由(Vue Router)](https://www.runoob.com/vue3-routing.html) **













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