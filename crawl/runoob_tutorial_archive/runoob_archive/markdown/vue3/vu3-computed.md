# Vue3 计算属性

- Source: https://www.runoob.com/vue3/vu3-computed.html

计算属性用于根据其他数据的变化动态计算衍生出来的属性值，而且具有缓存机制，只有相关依赖发生变化时才会重新计算。


计算属性关键词: **computed**。


计算属性在处理一些复杂逻辑时是很有用的。


可以看下以下反转字符串的例子：


## 实例 1


```javascript
<div id="app">
  {{ message.split('').reverse().join('') }}
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-str-reverse1)


实例 1 中模板变的很复杂起来，也不容易看懂理解。


接下来我们看看使用了计算属性的实例：


## 实例 2


```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Vue 测试实例 - 菜鸟教程(runoob.com)</title>
<script src="https://cdn.staticfile.org/vue/3.0.5/vue.global.js"></script>
</head>
<body>
<div id="app">
  <p>原始字符串: {{ message }}</p>
  <p>计算后反转字符串: {{ reversedMessage }}</p>
</div>

<script>
const app = {
  data() {
    return {
      message: 'RUNOOB!!'
    }
  },
  computed: {
    // 计算属性的 getter
    reversedMessage: function () {
      // `this` 指向 vm 实例
      return this.message.split('').reverse().join('')
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-str-reverse2)


实例 2 中声明了一个计算属性 reversedMessage 。


提供的函数将用作属性 vm.reversedMessage 的 getter 。


vm.reversedMessage 依赖于 vm.message，在 vm.message 发生改变时，vm.reversedMessage 也会更新。


使用 computed 函数来定义计算属性：


## 实例


```javascript
<template>
  <div>
    <p>商品名称：{{ productName }}</p>
    <p>商品价格：{{ formattedPrice }}</p>
    <button @click="increasePrice">增加价格</button>
  </div>
</template>

<script>
import { reactive, computed } from 'vue';

export default {
  setup() {
    // 响应式数据
    const state = reactive({
      name: '手机',
      price: 2000
    });

    // 计算属性
    const productName = computed(() => {
      return `优惠 ${state.name}`;
    });

    const formattedPrice = computed(() => {
      return `￥${state.price.toFixed(2)}`;
    });

    // 方法
    const increasePrice = () => {
      state.price += 100;
    };

    return {
      productName,
      formattedPrice,
      increasePrice
    };
  }
};
</script>
```


### 说明



`computed` 函数**:


- 在 `setup` 函数中使用 `computed` 函数来定义计算属性。
- 通过箭头函数返回计算的值，该函数会自动跟踪其依赖的响应式数据（`state` 对象中的 `name` 和 `price`）。



**使用计算属性**:


- `productName` 计算属性衍生自 `state.name`，每当 `state.name` 发生变化时，`productName` 会自动更新。
- `formattedPrice` 计算属性衍生自 `state.price`，每当 `state.price` 发生变化时，`formattedPrice` 会自动更新。



**响应式数据**:


- 使用 `reactive` 函数创建 `state` 对象，使其成为响应式数据，可以监听其属性的变化。



**方法**:


- `increasePrice` 方法用于增加 `state.price` 的值，每点击一次按钮，`state.price` 值增加 100，并且 `formattedPrice` 计算属性会相应更新。




---


## computed vs methods


我们可以使用 methods 来替代 computed，效果上两个都是一样的，但是 computed 是基于它的依赖缓存，只有相关依赖发生改变时才会重新取值。而使用 methods ，在重新渲染的时候，函数总会重新调用执行。


## 实例 3


```javascript
methods: {
  reversedMessage2: function () {
    return this.message.split('').reverse().join('')
  }
}
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-str-reverse3)


可以说使用 computed 性能会更好，但是如果你不希望缓存，你可以使用 methods 属性。


---


## computed setter


computed 属性默认只有 getter ，不过在需要时你也可以提供一个 setter ：


## 实例 4


```javascript
const app = {
  data() {
    return {
      name: 'Google',
      url: 'http://www.google.com'
    }
  },
  computed: {
    site: {
      // getter
      get: function () {
        return this.name + ' ' + this.url
      },
      // setter
      set: function (newValue) {
        var names = newValue.split(' ')
        this.name = names[0]
        this.url = names[names.length - 1]
      }
    }
  }
}
vm = Vue.createApp(app).mount('#app')
document.write('name: ' + vm.name);
document.write('<br>');
document.write('url: ' + vm.url);
document.write('<br>------ 更新数据 ------<br>');
// 调用 setter， vm.name 和 vm.url 也会被对应更新
vm.site = '菜鸟教程 https://www.runoob.com';
document.write('name: ' + vm.name);
document.write('<br>');
document.write('url: ' + vm.url);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-str-reverse4)


从实例运行结果看在运行 **vm.site = '菜鸟教程 http://www.runoob.com';** 时，setter** 会被调用， **vm.name** 和 **vm.url** 也会被对应更新。


![](https://www.runoob.com/wp-content/uploads/2021/02/4F03C6BE-B450-40ED-AD26-1980A3F81AFF.jpeg)








	  AI 思考中...





			** [Vue3 循环语句](https://www.runoob.com/vue3-v-for.html)
			[Vue3 组件](https://www.runoob.com/vue3-components.html) **













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