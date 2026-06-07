# Vue3 事件处理

- Source: https://www.runoob.com/vue3/vue3-events.html

我们可以使用 v-on 指令来监听 DOM 事件，从而执行 JavaScript 代码。


**v-on** 指令可以缩写为 **@** 符号。


语法格式：


```
v-on:click="methodName"
或
@click="methodName"
```


## v-on


```javascript
<div id="app">
  <button @click="counter += 1">增加 1</button>
  <p>这个按钮被点击了 {{ counter }} 次。</p>
</div>

<script>
const app = {
  data() {
    return {
      counter: 0
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-on)


通常情况下，我们需要使用一个方法来调用 JavaScript 方法。


v-on 可以接收一个定义的方法来调用。


## v-on


```javascript
<div id="app">
  <!-- `greet` 是在下面定义的方法名 -->
  <button @click="greet">点我</button>
</div>

<script>
const app = {
  data() {
    return {
      name: 'Runoob'
    }
  },
  methods: {
    greet(event) {
      // `methods` 内部的 `this` 指向当前活动实例
      alert('Hello ' + this.name + '!')
      // `event` 是原生 DOM event
      if (event) {
        alert(event.target.tagName)
      }
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-on2)


除了直接绑定到一个方法，也可以用内联 JavaScript 语句：


## v-on


```javascript
<div id="app">
  <button @click="say('hi')">Say hi</button>
  <button @click="say('what')">Say what</button>
</div>

<script>
const app = {
  data() {

  },
  methods: {
    say(message) {
      alert(message)
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-on3)


事件处理程序中可以有多个方法，这些方法由逗号运算符分隔：


## v-on


```javascript
<div id="app">
  <!-- 这两个 one() 和 two() 将执行按钮点击事件 -->
  <button @click="one($event), two($event)">
  点我
  </button>
</div>

<script>
const app = {
  data() {
  },
  methods: {
    one(event) {
      alert("第一个事件处理器逻辑...")
    },
    two(event) {
      alert("第二个事件处理器逻辑...")
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-on4)


### 事件修饰符


Vue.js 为 v-on 提供了事件修饰符来处理 DOM 事件细节，如：event.preventDefault() 或 event.stopPropagation()。


Vue.js 通过由点 **.** 表示的指令后缀来调用修饰符。


- `.stop` - 阻止冒泡
- `.prevent` - 阻止默认事件
- `.capture` - 阻止捕获
- `.self` - 只监听触发该元素的事件
- `.once` - 只触发一次
- `.left` - 左键事件
- `.right` - 右键事件
- `.middle` - 中间滚轮事件


```
<!-- 阻止单击事件冒泡 -->
<a v-on:click.stop="doThis"></a>
<!-- 提交事件不再重载页面 -->
<form v-on:submit.prevent="onSubmit"></form>
<!-- 修饰符可以串联  -->
<a v-on:click.stop.prevent="doThat"></a>
<!-- 只有修饰符 -->
<form v-on:submit.prevent></form>
<!-- 添加事件侦听器时使用事件捕获模式 -->
<div v-on:click.capture="doThis">...</div>
<!-- 只当事件在该元素本身（而不是子元素）触发时触发回调 -->
<div v-on:click.self="doThat">...</div>

<!-- click 事件只能点击一次，2.1.4版本新增 -->
<a v-on:click.once="doThis"></a>
```


### 按键修饰符


Vue 允许为 v-on 在监听键盘事件时添加按键修饰符：


```
<!-- 只有在 keyCode 是 13 时调用 vm.submit() -->
<input v-on:keyup.13="submit">
```


记住所有的 keyCode 比较困难，所以 Vue 为最常用的按键提供了别名：


```
<!-- 同上 -->
<input v-on:keyup.enter="submit">
<!-- 缩写语法 -->
<input @keyup.enter="submit">
```


全部的按键别名：


- `.enter`
- `.tab`
- `.delete` (捕获 "删除" 和 "退格" 键)
- `.esc`
- `.space`
- `.up`
- `.down`
- `.left`
- `.right`


系统修饰键：

- `.ctrl`
- `.alt`
- `.shift`
- `.meta`


鼠标按钮修饰符:


- ` .left`
- `.right`
- `.middle`


## 实例


```javascript
<p><!-- Alt + C -->
<input @keyup.alt.67="clear">
<!-- Ctrl + Click -->
<div @click.ctrl="doSomething">Do something</div>
```


### .exact 修饰符


**.exact** 修饰符允许你控制由精确的系统修饰符组合触发的事件。


## 实例


```javascript
<!-- 即使 Alt 或 Shift 被一同按下时也会触发 -->
<button @click.ctrl="onClick">A</button>

<!-- 有且只有 Ctrl 被按下的时候才触发 -->
<button @click.ctrl.exact="onCtrlClick">A</button>

<!-- 没有任何系统修饰符被按下的时候才触发 -->
<button @click.exact="onClick">A</button>
```









	  AI 思考中...





			** [Vue3 样式绑定](https://www.runoob.com/vue3-class-bind.html)
			[Vue3 表单](https://www.runoob.com/vue3-forms.html) **













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