# Vue3 条件语句

- Source: https://www.runoob.com/vue3/vue3-v-if.html

在 Vue 3 中，你可以在模板中使用多种条件语句来控制组件的渲染。

主要的条件语句有 `v-if`、`v-else-if`、`v-else` 和 `v-show`，以下是它们的用法及区别：


- **`v-if`**：元素在条件为 `false` 时不会被渲染到 DOM 中，适用于条件变化不频繁的情况。
- **`v-show`**：元素总是渲染到 DOM 中，适用于条件变化频繁的情况，切换显示隐藏性能更好。
- **`v-else-if` 和 `v-else`**：用于处理多个条件分支，配合 `v-if` 使用。


## 条件判断


### v-if

根据表达式的真假条件性地渲染元素。如果表达式为真，则渲染该元素；如果为假，则不渲染（不会在 DOM 中生成该元素）。


条件判断使用 v-if 指令，指令的表达式返回 true 时才会显示：


## v-if 指令


在元素中使用 v-if 指令：


```javascript
<div id="app">
    <p v-if="seen">现在你看到我了</p>
</div>

<script>
const app = {
  data() {
    return {
      seen: true /* 改为false，信息就无法显示 */
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-if)

这里， v-if 指令将根据表达式 seen 的值( true 或 false )来决定是否插入 p 元素。

因为 v-if 是一个指令，所以必须将它添加到一个元素上。如果是多个元素，可以包裹在  元素上，并在上面使用 v-if。最终的渲染结果将不包含  元素。


## v-if 指令


在  元素上使用 v-if 指令：


```javascript
<div id="app">
    <template v-if="seen">
        <h1>网站</h1>
        <p>Google</p>
        <p>Runoob</p>
        <p>Taobao</p>
    </template>
</div>

<script>
const app = {
  data() {
    return {
      seen: true /* 改为false，信息就无法显示 */
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-if-template)

### v-else 与 v-if 搭配使用，表示在前一个 v-if 表达式为假时渲染的元素。


可以用 v-else 指令给 v-if 添加一个 "else" 块：


## v-else 指令


随机生成一个数字，判断是否大于 0.5，然后输出对应信息：


```javascript
<div id="app">
    <div v-if="Math.random() > 0.5">
      随机数大于 0.5
    </div>
    <div v-else>
      随机数小于等于 0.5
    </div>
</div>

<script>
Vue.createApp().mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-if-else)


### v-else-if

在 v-if 和 v-else 之间添加额外的条件判断，可以连续使用多个 v-else-if。


## v-else 指令


判断 type 变量的值：


```javascript
<div id="app">
    <div v-if="type === 'A'">
         A
    </div>
    <div v-else-if="type === 'B'">
      B
    </div>
    <div v-else-if="type === 'C'">
      C
    </div>
    <div v-else>
      Not A/B/C
    </div>
</div>

<script>
const app = {
  data() {
    return {
      type: "C"
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-else-if)


> v-else 、v-else-if 必须跟在 v-if 或者 v-else-if之后。


### v-show

根据表达式的真假条件性地显示或隐藏元素，与 v-if 不同的是，v-show 始终会在 DOM 中保留元素，只是通过 CSS 的 display 属性控制元素的显示和隐藏。


我们也可以使用 v-show 指令来根据条件展示元素：


## v-show 指令


```javascript
<h1 v-show="ok">Hello!</h1>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-show)


如果需要频繁切换元素的显示与隐藏，推荐使用 v-show，因为它只是简单地切换 CSS 样式，而不是重新渲染整个元素。









	  AI 思考中...





			** [Vue3 模板语法](https://www.runoob.com/vue3-template-syntax.html)
			[Vue3 循环语句](https://www.runoob.com/vue3-v-for.html) **













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