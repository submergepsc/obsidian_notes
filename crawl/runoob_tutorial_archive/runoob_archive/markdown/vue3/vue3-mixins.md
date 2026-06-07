# Vue3 混入

- Source: https://www.runoob.com/vue3/vue3-mixins.html

混入 (mixins)定义了一部分可复用的方法或者计算属性。混入对象可以包含任意组件选项。当组件使用混入对象时，所有混入对象的选项将被混入该组件本身的选项。


来看一个简单的实例：


## 实例


```javascript
// 定义混入对象
const myMixin = {
  created() {
    this.hello()
  },
  methods: {
    hello() {
      console.log('欢迎来到混入实例-RUNOOB!')
    }
  }
}

// 定义一个应用，使用混入
const app = Vue.createApp({
  mixins: [myMixin]
})

app.mount('#app') // => "欢迎来到混入实例-RUNOOB!"
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-mixin)


---


## 选项合并


当组件和混入对象含有同名选项时，这些选项将以恰当的方式混合。


比如，数据对象在内部会进行浅合并 (一层属性深度)，在和组件的数据发生冲突时以组件数据优先。


以下实例中，Vue 实例与混入对象包含了相同的方法。从输出结果可以看出两个选项合并了。


## 实例


```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Vue 测试实例 - 菜鸟教程(runoob.com)</title>
<script src="https://unpkg.com/vue@next"></script>
</head>
<body>
<div id = "app"></div>
<script type = "text/javascript">
const myMixin = {
  data() {
    return {
      message: 'hello',
      foo: 'runoob'
    }
  }
}

const app = Vue.createApp({
  mixins: [myMixin],
  data() {
    return {
      message: 'goodbye',
      bar: 'def'
    }
  },
  created() {
    document.write(JSON.stringify(this.$data))
  }
})
```


输出结果为：


```javascript
{"message":"goodbye","foo":"runoob","bar":"def"}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-mixin2)


同名钩子函数将合并为一个数组，因此都将被调用。另外，mixin 对象的钩子将在组件自身钩子之前调用。


```
const myMixin = {
  created() {
    console.log('mixin 对象的钩子被调用')
  }
}

const app = Vue.createApp({
  mixins: [myMixin],
  created() {
    console.log('组件钩子被调用')
  }
})

// => "mixin 对象的钩子被调用"
// => "组件钩子被调用"
```


值为对象的选项，例如 methods、components 和 directives，将被合并为同一个对象。两个对象键名冲突时，取组件对象的键值对。


## 实例


```javascript
const myMixin = {
  methods: {
    foo() {
      console.log('foo')
    },
    conflicting() {
      console.log('from mixin')
    }
  }
}

const app = Vue.createApp({
  mixins: [myMixin],
  methods: {
    bar() {
      console.log('bar')
    },
    conflicting() {
      console.log('from self')
    }
  }
})

const vm = app.mount('#app')

vm.foo() // => "foo"
vm.bar() // => "bar"
vm.conflicting() // => "from self"
```


以上实例，我们调用了以下三个方法：


```
vm.foo();
vm.bar();
vm.conflicting();
```


从输出结果 methods 选项中如果碰到相同的函数名则 Vue 实例有更高的优先级会执行输出。


---

## 全局混入


也可以全局注册混入对象。注意使用！ 一旦使用全局混入对象，将会影响到 所有 之后创建的 Vue 实例。使用恰当时，可以为自定义对象注入处理逻辑。


## 实例


```javascript
const app = Vue.createApp({
  myOption: 'hello!'
})

// 为自定义的选项 'myOption' 注入一个处理器。
app.mixin({
  created() {
    const myOption = this.$options.myOption
    if (myOption) {
      document.write(myOption)
    }
  }
})

app.mount('#app') // => "hello!"
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-mixin4)


谨慎使用全局混入对象，因为会影响到每个单独创建的 Vue 实例 (包括第三方模板)。








	  AI 思考中...





			** [Vue3 路由(Vue Router)](https://www.runoob.com/vue3-routing.html)
			[Vue3 Ajax(axios)](https://www.runoob.com/vue3-ajax-axios.html) **













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