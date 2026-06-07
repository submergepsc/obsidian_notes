# Vue 组件实例

- Source: https://www.runoob.com/vue3/vue-component-instance.html

在 Vue.js 中，组件实例是 Vue 应用中最基本的构建块之一。每个组件实例都是一个 Vue 组件，它具有自己的模板、数据、方法和生命周期钩子，可以独立地管理自己的状态和行为。以下是关于 Vue 组件实例的详细介绍：


## Vue 组件实例的创建

在 Vue.js 中，创建一个组件实例通常通过 createApp 方法和组件选项对象来实现。

组件选项对象可以包含如下属性：


- **`data`**: 数据对象，用于存储组件的响应式数据。
- **`props`**: 属性数组或对象，用于接收父组件传递的数据。
- **`computed`**: 计算属性对象，根据响应式依赖进行动态计算。
- **`methods`**: 方法对象，包含组件内部的函数和操作。
- **`watch`**: 监听器对象，用于监听数据变化并做出响应。
- **`template`**: 字符串，定义组件的模板结构。
- **`render`**: 函数，用于渲染组件的虚拟 DOM。
- **`setup`**: 函数，用于设置组件的初始状态、数据、计算属性和监听器等（Vue 3 中）。

以下是一个简单的 Vue 组件实例的示例：


## 实例


```javascript
import { createApp } from 'vue';

const app = createApp({
  data() {
    return {
      message: 'Hello, Vue!'
    };
  },
  methods: {
    greet() {
      alert(this.message);
    }
  },
  template: `
    <div>
      <p>{{ message }}</p>
      <button @click="greet">Greet</button>
    </div>
  `
});

app.mount('#app');
```


**说明：**


- `data` 函数返回一个包含 `message` 属性的对象，用于存储组件的状态。
- `methods` 对象包含了一个 `greet` 方法，当点击按钮时会弹出一个提示框显示 `message` 的内容。
- `template` 字符串定义了组件的模板结构，使用了插值和事件绑定来实现数据展示和交互。


### 生命周期钩子

Vue 组件实例具有一些生命周期钩子函数，允许开发者在组件生命周期的不同阶段执行自定义逻辑。常见的生命周期钩子包括 `created`、`mounted`、`updated` 和 `destroyed` 等。


## 实例


```javascript
const app = createApp({
  data() {
    return {
      message: 'Hello, Vue!'
    };
  },
  created() {
    console.log('Component created');
  },
  mounted() {
    console.log('Component mounted');
  },
  updated() {
    console.log('Component updated');
  },
  destroyed() {
    console.log('Component destroyed');
  },
  template: `
    <div>
      <p>{{ message }}</p>
    </div>
  `
});
```


## 组件通信

Vue 组件实例之间通过 props、events、provide/inject、$parent/$children、$attrs/$listeners 等方式进行通信，具体取决于组件的关系和需求。这些机制允许组件在不同层级之间传递数据和响应用户交互。

---


## 组件实例属性


### $data

$data 属性包含组件实例的所有数据属性。它是响应式的，即当数据发生变化时，相关的视图会自动更新。


## 实例


```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello, Vue!'
    };
  }
});

const vm = app.mount('#app');
console.log(vm.$data); // { message: 'Hello, Vue!' }
```


### $props


$props 属性包含当前组件接收的所有父组件传递的属性（props）。它是只读的。


## 实例


```javascript
<!-- ParentComponent.vue -->
<template>
  <child-component :message="parentMessage"></child-component>
</template>

<script>
import ChildComponent from './ChildComponent.vue';

export default {
  components: {
    ChildComponent
  },
  data() {
    return {
      parentMessage: 'Message from parent'
    };
  }
};
</script>
```


## 实例


```javascript
// ChildComponent.vue
export default {
  props: ['message'],
  mounted() {
    console.log(this.$props.message); // 'Message from parent'
  }
};
```


### $refs


$refs 包含了组件内所有拥有 ref 特性的 DOM 元素或子组件实例。可以通过 $refs 来访问这些元素或组件实例。


## 实例


```javascript
<template>
  <div>
    <input type="text" ref="inputField">
  </div>
</template>

<script>
export default {
  mounted() {
    console.log(this.$refs.inputField); // 访问 DOM 元素
    this.$refs.inputField.focus(); // 调用 DOM 元素方法
  }
}
</script>
```


$el 属性表示当前组件实例的根 DOM 元素。在组件被挂载后才能访问到该属性。


## 实例


```javascript
const app = Vue.createApp({
  template: '<div>Hello, Vue!</div>'
});

const vm = app.mount('#app');
console.log(vm.$el); // <div id="app">Hello, Vue!</div>
```


### $attrs


$attrs 包含了父组件传递给当前组件但未在子组件声明的所有属性。这些属性可以用于向子组件传递额外的非 prop 特性。


## 实例


```javascript
<!-- ParentComponent.vue -->
<template>
  <child-component custom-attr="value"></child-component>
</template>

<!-- ChildComponent.vue -->
<script>
export default {
  mounted() {
    console.log(this.$attrs); // { custom-attr: 'value' }
  }
};
</script>
```


### $listeners


$listeners 包含了父组件传递给当前组件的所有监听器（事件处理函数），可以直接绑定到组件的根元素或其他元素上。


## 实例


```javascript
<!-- ChildComponent.vue -->
<template>
  <button v-on="$listeners">Click me</button>
</template>

<script>
export default {
  mounted() {
    console.log(this.$listeners); // { click: handleClick }
  },
  methods: {
    handleClick() {
      console.log('Button clicked');
    }
  }
};
</script>
```


---


## 组件实例方法


### $mount()


$mount() 方法手动将 Vue 组件挂载到 DOM 元素上。在 Vue 3 中，通常通过 createApp().mount() 自动挂载，少数情况下需要手动挂载。


## 实例


```javascript
const app = Vue.createApp({
  template: '<div>Hello, Vue!</div>'
});

const vm = app.mount('#app');
```


### $destroy()


$destroy() 方法销毁当前组件实例，解绑其所有的事件监听器并释放其占用的资源。在一些特定的场景，如动态创建和销毁组件时很有用。


## 实例


```javascript
vm.$destroy();
```


### $emit()


$emit() 方法用于触发当前组件实例上的自定义事件，并传递数据给父组件。通常与 v-on 指令结合使用。


## 实例


```javascript
<button @click="$emit('custom-event', eventData)">Click me</button>
```


### $nextTick()


$nextTick() 方法在下次 DOM 更新循环结束之后执行指定的回调函数。用于在 DOM 更新之后执行一些操作。


## 实例


```javascript
vm.$nextTick(() => {
  // DOM 更新完成后执行的操作
});
```


### $watch()


$watch() 方法用于监听组件实例上的数据变化，并在数据变化时执行指定的回调函数。


## 实例


```javascript
vm.$watch('message', (newValue, oldValue) => {
  console.log(`Message changed from ${oldValue} to ${newValue}`);
});
```


这些属性和方法使得 Vue 组件实例具有丰富的功能和灵活性，能够满足开发者在构建复杂应用时的各种需求，从数据管理到事件处理，再到动态组件的操作，都能够通过组件实例来进行管理和控制。








	  AI 思考中...





			** [Vue3 内置组件](https://www.runoob.com/vue3-builtin-components.html)
			[Vue3 内置指令](https://www.runoob.com/vue3-ref-directives.html) **













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