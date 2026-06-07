# Vue3 声明式渲染

- Source: https://www.runoob.com/vue3/vue3-declarative-rendering.html

声明式渲染（Declarative Rendering）是指通过数据驱动视图的更新，而不是直接操作 DOM。

声明式渲染让开发者可以更专注于业务逻辑，而不需要关心如何更新视图和 DOM。


Vue3 的声明式渲染是一种基于模板的渲染方式，它允许开发者通过简洁的模板语法来描述页面的结构和数据绑定关系，而不需要直接操作 DOM。


Vue3 的声明式渲染通过使用模板、指令（如 v-if、v-for、v-bind 等）以及响应式数据来简化 UI 更新过程。


Vue 的声明式渲染让你只需要声明 UI 应该如何呈现，Vue 会根据数据的变化自动更新视图，当你改变数据时，视图会自动响应。


Vue3 使用模板语法（类似 HTML）来描述 UI，模板中的表达式（如 {{ message }}）会绑定到组件的数据模型。


![](https://www.runoob.com/wp-content/uploads/2024/12/declarative-rendering-1.png)


---


## 1、数据绑定

数据绑定是声明式渲染的核心。

通过绑定数据，Vue 可以自动更新 DOM 元素的内容，避免了传统的手动 DOM 操作。


### 插值表达式

插值表达式是通过双花括号 **{{ }}** 来将组件的数据插入到 HTML 模板中。


## 实例


```javascript
<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello, Vue 3!'
    };
  }
};
</script>
```


以上实例中，双花括号 **{{ message }}** 会渲染为 **Hello, Vue 3!**，并且当 message 的值改变时，视图会自动更新。


在双花括号中的内容并不只限于标识符或路径——我们可以使用任何有效的 JavaScript 表达式。


```
<h1>{{ message.split('').reverse().join('') }}</h1>
```


### 属性绑定


通过 **v-bind** 指令，你可以绑定 HTML 属性到组件的数据，这样可以使得 DOM 元素的属性（如 href、class、src）根据组件的状态动态更新。


## 实例


```javascript
<template>
  <div>
    <a v-bind:href="url">点我</a>
  </div>
</template>

<script>
export default {
  data() {
    return {
      url: 'https://www.runoob.com'
    };
  }
};
</script>
```


以上实例中，v-bind:href 会将 url 数据绑定到  标签的 href 属性，当 url 发生变化时，href 会自动更新。


## 条件渲染

Vue 通过 v-if、v-else-if 和 v-else 指令实现条件渲染，根据某个数据条件来决定是否渲染某个 DOM 元素。


## 实例


```javascript
<template>
  <div>
    <p v-if="isVisible">这段文本是可见的</p>
    <button @click="toggleVisibility">切换可见性</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isVisible: true
    };
  },
  methods: {
    toggleVisibility() {
      this.isVisible = !this.isVisible;
    }
  }
};
</script>
```


以上实例中，当 isVisible 为 true 时， 标签会被渲染，当点击按钮时，isVisible 会反转， 标签的显示与否也会自动改变。


---


## 列表渲染

使用 v-for 指令可以渲染一个列表。

Vue 会根据数组的每一项渲染对应的 DOM 元素，并且在数组数据变化时，自动更新视图。


## 实例


```javascript
<template>
  <div>
    <ul>
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { id: 1, name: 'Vue 3' },
        { id: 2, name: 'JavaScript' },
        { id: 3, name: 'HTML' }
      ]
    };
  }
};
</script>
```


以上实例中，v-for 会根据 items 数组渲染出一个列表。每个列表项都有一个 key 来帮助 Vue 跟踪每一项，从而提高渲染效率。


---

## 双向数据绑定


Vue 提供了 v-model 指令来实现表单元素（如 ）和组件数据之间的双向绑定，这样，表单元素的值与数据模型保持同步，用户输入时会自动更新数据，数据变化时会自动更新视图。


## 实例


```javascript
<template>
  <div>
    <input v-model="message" placeholder="输入一些文本" />
    <p>你输入了：{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: ''
    };
  }
};
</script>
```


在以上实例中，v-model 使得 input 元素的值与 message 数据保持同步。当用户在输入框中输入文本时，message 会自动更新， 标签中的内容也会自动变化。


## 事件处理

Vue 提供了 v-on 指令来监听 DOM 事件并在事件触发时执行方法，这种方式让你能够声明式地处理用户输入、点击等事件。


## 实例


```javascript
<template>
  <div>
    <button v-on:click="increment">点击我</button>
    <p>点击次数：{{ count }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: 0
    };
  },
  methods: {
    increment() {
      this.count += 1;
    }
  }
};
</script>
```


在以上实例中，v-on:click 会监听按钮的点击事件，并在每次点击时调用 increment 方法来增加 count 的值，count 会自动更新到视图中。


---


## 计算属性

计算属性是 Vue 提供的一种声明式计算值的方式。

计算属性基于响应式数据，且只有在依赖的数据发生变化时才会重新计算。


## 实例


```javascript
<template>
  <div>
    <p>原始金额：{{ amount }}</p>
    <p>税后金额：{{ computedAmount }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      amount: 100
    };
  },
  computed: {
    computedAmount() {
      return this.amount * 1.1; // 假设税率为10%
    }
  }
};
</script>
```


computedAmount 是一个计算属性，基于 amount 计算出税后金额。当 amount 改变时，computedAmount 会自动更新，而不需要手动触发视图更新。









	  AI 思考中...





			** [Vue3 Tailwind CSS](https://www.runoob.com/vue3-tailwindcss.html)
			[使用 VSCode 开发 Vue](https://www.runoob.com/vue3-vscode.html) **













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