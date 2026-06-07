# Vue 实例选项

- Source: https://www.runoob.com/vue3/vue-ref-options.html

Vue 中的选项是使用 Options API 时在 Vue 实例上可用的不同选项。


Vue 实例的一些常见选项：


- **el** - 指定 Vue 实例挂载的 DOM 元素。如果不提供，则 Vue 实例不会自动挂载。
- **data** - 定义了 Vue 实例的数据对象。Vue 实例的模板和计算属性、方法、观察者等都可以访问这些数据。
- **computed** - 包含计算属性，这些属性的值是基于它们的依赖进行缓存的，只有当依赖发生变化时，计算属性才会重新计算。
- **methods** - 定义了 Vue 实例的方法，可以在模板中通过事件监听器调用。
- **watch** - 包含一个或多个观察者，用于观察和响应 Vue 实例中数据的变化。
- **props** - 定义了组件可以接收的外部数据。
- **components** - 允许在 Vue 实例中注册自定义组件。
- **directives** - 允许注册全局自定义指令。
- **filters** - 定义了过滤器，可以在模板中使用，用于文本的格式化。
- **model** - 指定组件使用的自定义 v-model 属性和事件。
- **provide/inject** - 提供依赖注入的能力，允许跨组件传递数据。
- **lifecycle hooks** - 包括 `onMounted`, `onUpdated`, `onUnmounted` 等生命周期钩子，用于在 Vue 实例的不同阶段执行代码。
- **template** - 定义了 Vue 实例的 HTML 模板。
- **render function** - 允许使用 JavaScript 函数来渲染组件，提供了更高级的自定义能力。
- **errorCaptured** - 用于全局捕获 Vue 实例的错误。
- **emits** - 定义了组件可以触发的事件。
- **setup** - Vue 3 的 Composition API 中的入口函数，用于组织组件的逻辑。


### el


挂载点，用于指定 Vue 实例挂载的 DOM 元素：


## 实例


```javascript
const app = Vue.createApp({
  // options
});
app.mount('#app');
```



### data


- **类型**: 函数或对象
- **作用**: `data` 是 Vue 实例中用来存储组件数据的地方。你可以在 `data` 中定义各种数据属性，并通过模板语法在页面上使用它们。`data` 中的数据会响应式地更新，即当数据发生变化时，相关的页面内容会自动更新。


## 实例


```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello Vue!'
    };
  }
});
```


### computed


- **类型**: 对象
- **作用**: `computed` 属性允许你声明基于响应式依赖的计算属性。计算属性只有在相关依赖发生改变时才会重新求值，并且会缓存计算结果，避免不必要的重复计算。


## 实例


```javascript
const app = Vue.createApp({
  data() {
    return {
      firstName: 'John',
      lastName: 'Doe'
    };
  },
  computed: {
    fullName() {
      return `${this.firstName} ${this.lastName}`;
    }
  }
});
```



### methods


- **类型**: 对象
- **作用**: `methods` 属性用于存放 Vue 实例中的方法。这些方法可以在模板中调用，也可以在实例的其他方法中使用。与计算属性不同，每次调用方法时都会重新执行，适合用于响应事件或执行异步操作。


## 实例


```javascript
const app = Vue.createApp({
  data() {
    return {
      count: 0
    };
  },
  methods: {
    increment() {
      this.count++;
    }
  }
});
```



### watch


- **类型**: 对象或函数
- **作用**: `watch` 属性用于观察和响应 Vue 实例中数据的变化。当监视的数据发生变化时，执行指定的回调函数。适合处理异步或复杂的数据变化逻辑。


## 实例


```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello Vue!'
    };
  },
  watch: {
    message(newValue, oldValue) {
      console.log(`Message changed from ${oldValue} to ${newValue}`);
    }
  }
});
```



### props


- **类型**: 数组或对象
- **作用**: `props` 属性用于接收父组件传递给子组件的数据。子组件通过 `props` 接收父组件传递的数据，并可以在组件内部使用。

以下例子中，MyComponent 接收一个 title 属性，并在模板中使用它：


## 实例


```javascript
const MyComponent = {
  props: ['title'],
  template: '<h1>{{ title }}</h1>'
};

const app = Vue.createApp({
  components: {
    'my-component': MyComponent
  },
  template: '<my-component title="Hello Vue 3!"></my-component>'
});

app.mount('#app');
```



### template


- **类型**: 字符串
- **作用**: `template` 属性定义了 Vue 组件的模板结构。模板中可以使用 Vue 的模板语法，包括插值、指令、计算属性等。模板最终会被编译为渲染函数，用于生成组件的虚拟 DOM。


## 实例


```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello Vue!'
    };
  },
  template: '<div>{{ message }}</div>'
});
```


### components

components 用于注册局部组件。


## 实例


```javascript
const ChildComponent = {
  template: '<div>A child component</div>'
};

const app = Vue.createApp({
  components: {
    'child-component': ChildComponent
  },
  template: '<child-component></child-component>'
}).mount('#app');
```


### provide / inject

父组件提供数据，子组件注入使用。


## 实例


```javascript
const ChildComponent = {
  inject: ['message'],
  template: '<div>{{ message }}</div>'
};

const app = Vue.createApp({
  provide() {
    return {
      message: 'Provided Message'
    };
  },
  components: {
    'child-component': ChildComponent
  },
  template: '<child-component></child-component>'
}).mount('#app');
```


---


## 生命周期钩子


### beforeCreate

实例初始化之前调用。


## 实例


```javascript
const app = Vue.createApp({
  beforeCreate() {
    console.log('beforeCreate');
  }
}).mount('#app');
```


### created

实例创建完成后调用。


## 实例


```javascript
const app = Vue.createApp({
  created() {
    console.log('created');
  }
}).mount('#app');
```


### beforeMount

在挂载之前调用。


## 实例


```javascript
const app = Vue.createApp({
  beforeMount() {
    console.log('beforeMount');
  }
}).mount('#app');
```


### mounted

实例挂载完成后调用。


## 实例


```javascript
const app = Vue.createApp({
  mounted() {
    console.log('mounted');
  }
}).mount('#app');
```


### beforeUpdate

数据更新之前调用。


## 实例


```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello'
    };
  },
  beforeUpdate() {
    console.log('beforeUpdate');
  }
}).mount('#app');
```


### updated

数据更新之后调用。


## 实例


```javascript
const app = Vue.createApp({
  data() {
    return {
      message: 'Hello'
    };
  },
  updated() {
    console.log('updated');
  }
}).mount('#app');
```


### beforeUnmount

实例卸载之前调用。


## 实例


```javascript
const app = Vue.createApp({
  beforeUnmount() {
    console.log('beforeUnmount');
  }
}).mount('#app');
```


### unmounted

实例卸载之后调用。


## 实例


```javascript
const app = Vue.createApp({
  unmounted() {
    console.log('unmounted');
  }
}).mount('#app');
```


---


## 其他选项


### directives

注册局部指令。


## 实例


```javascript
const app = Vue.createApp({
  directives: {
    focus: {
      mounted(el) {
        el.focus();
      }
    }
  },
  template: '<input v-focus>'
}).mount('#app');
```


### mixins

混入对象。


## 实例


```javascript
const myMixin = {
  created() {
    console.log('Mixin created');
  }
};

const app = Vue.createApp({
  mixins: [myMixin],
  created() {
    console.log('Component created');
  }
}).mount('#app');
```


### extends

扩展另一个组件。


## 实例


```javascript
const BaseComponent = {
  created() {
    console.log('BaseComponent created');
  }
};

const app = Vue.createApp({
  extends: BaseComponent,
  created() {
    console.log('Extended component created');
  }
}).mount('#app');
```


### inheritAttrs

是否继承父组件的 attribute。


## 实例


```javascript
const MyComponent = {
  inheritAttrs: false,
  props: ['title'],
  template: '<div><h1>{{ title }}</h1></div>'
};

const app = Vue.createApp({
  components: {
    'my-component': MyComponent
  },
  template: '<my-component title="Hello" id="app"></my-component>'
}).mount('#app');
```


### setup

用于组合式 API。


## 实例


```javascript
const app = Vue.createApp({
  setup() {
    const message = Vue.ref('Hello Vue 3!');
    return { message };
  },
  template: '<h1>{{ message }}</h1>'
}).mount('#app');
```


### expose

在 Vue 3 的组合式 API 中，使用 setup 函数定义组件逻辑时，可以使用 expose 方法来明确指定要暴露给外部的属性和方法。


以下是一个简单的示例，展示如何使用 expose 在 Vue 3 组件中暴露属性和方法：


## 父组件 (ParentComponent.vue)


```javascript
<template>
  <div>
    <child-component ref="child"></child-component>
    <button @click="callChildMethod">Call Child Method</button>
  </div>
</template>

<script>
import { ref } from 'vue';
import ChildComponent from './ChildComponent.vue';

export default {
  components: {
    ChildComponent
  },
  setup() {
    const child = ref(null);

    const callChildMethod = () => {
      if (child.value) {
        child.value.exposedMethod();
      }
    };

    return {
      child,
      callChildMethod
    };
  }
};
</script>
```


## 子组件 (ChildComponent.vue)


```javascript
<template>
  <div>
    <p>{{ exposedData }}</p>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup(_, { expose }) {
    const exposedData = ref('Hello from Child Component');

    const exposedMethod = () => {
      console.log('Child component method called');
    };

    expose({
      exposedData,
      exposedMethod
    });

    return {
      exposedData
    };
  }
};
</script>
```


**说明：**


- **父组件**: - 在父组件中，使用 `ref` 创建了一个对子组件的引用 `child`。 - 在 `callChildMethod` 方法中，通过 `child.value` 访问子组件的实例，并调用子组件暴露的方法 `exposedMethod`。
- **子组件**: - 在子组件的 `setup` 函数中，通过 `ref` 创建了一个响应式数据 `exposedData`。 - 定义了一个方法 `exposedMethod`，用于展示如何暴露方法。 - 使用 `expose` 方法显式地暴露 `exposedData` 和 `exposedMethod` 给父组件。 - 返回 `exposedData`，以便在模板中使用。








	  AI 思考中...





			** [Vue3 内置指令](https://www.runoob.com/vue3-ref-directives.html)
			[Vue3 生命周期钩子](https://www.runoob.com/vue3-ref-lifecycle-hooks.html) **













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