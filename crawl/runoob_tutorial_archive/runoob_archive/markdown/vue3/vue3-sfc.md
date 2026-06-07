# Vue3 创建单文件组件(SFC)

- Source: https://www.runoob.com/vue3/vue3-sfc.html

Vue 的单文件组件 (即 ***.vue** 文件，英文 Single-File Component，简称 SFC) 是一种特殊的文件格式，使我们能够将一个 Vue 组件的模板、逻辑与样式封装在单个文件中。


在 Vue3 中，你可以使用 **.vue** 文件来创建单文件组件(Single File Components, SFCs)，这个文件包含了组件的模板、JavaScript 代码以及 CSS 样式。


现在我们将删除通过 **npm init vue@latest** 命令创建的实例项目中的所有内容（参考 [Vue3 安装](https://www.runoob.com/vue3-install.html)），以便在 Vue 中创建自己的简单网页。


在我们开始编写代码之前，删除 、 和  标签内的所有内容，以及任何像 setup 或 scoped 这样的属性。


您的 App.vue 文件现在应该如下所示：


## App.vue 文件：


```javascript
<script></script>

<template></template>

<style></style>
```


同时我们可以先清空 **src** 目录中的文件夹 **assets** 和 **components**，里面的文件我们可以后期自己添加补充 。


main.js 文件代码修改为如下代码：


## main.js 文件代码：


```javascript
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```


现在我们就创建了一个简单的项目，在 App.vue 文件写入以下代码：


## App.vue 文件代码：


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
      message: 'Hello, RUNOOB!'
    }
  }
}
</script>

<style>
h1 {
  color: blue;
}
</style>
```


以上实例中我们定义了一个包含一个标题的简单组件。组件的模板包含一个  元素，使用了 Vue3 的模板语法将 message 属性绑定到了这个元素的文本内容中。


JavaScript 部分包含了一个 data 函数，返回了一个包含了 message 属性的对象，我们将这个属性绑定到了模板中。


最后，CSS 样式定义了标题的颜色为蓝色。


在组件的 JavaScript 部分，我们使用了新的 export default 语法，这个语法可以让我们将组件定义导出为一个默认的对象。在 Vue3 中，我们可以使用这个语法来定义组件，而不必像 Vue2 那样使用 Vue.component 函数。


访问 **http://localhost:5173/**，以上代码执行结果为：


![](https://www.runoob.com/wp-content/uploads/2023/05/bd73268cae09ec3209e42c9509f1da74.png)


### 使用组件


当我们定义好了一个组件之后，我们可以在其他组件中使用这个组件。


使用组件，我们需要先创建组件，比如以下实例在 **./src/components/** 目录下创建 **HelloRunoob.vue** 组件文件，代码如下：


## ./src/components/HelloRunoob.vue 文件代码：


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
      message: 'Hello, Runoob!'
    }
  }
}
</script>

<style>
h1 {
  color: red;
}
</style>
```


然后我们在 ./src/main.js 文件中引入并定义该组件：


## ./src/main.js 文件代码：


```javascript
import { createApp } from 'vue'

import App from './App.vue'
import HelloRunoob from './components/HelloRunoob.vue'

const app = createApp(App)
app.component('hello-runoob', HelloRunoob) // 自定义标签
app.mount('#app')
```


在父组件的模板中，我们可以使用自定义标签的方式来引入子组件，就像以下 App.vue 文件代码：


## App.vue 文件代码


```javascript
<template>
  <div>
    <hello-runoob></hello-runoob>
  </div>
</template>
```


访问 **http://localhost:5173/**，以上代码执行结果为：


![](https://www.runoob.com/wp-content/uploads/2023/05/0ed91fd15ff9df3cfcd1a198d4c2b92f.png)








	  AI 思考中...





			** [Vue3 指令](https://www.runoob.com/vue3-directives.html)
			[Vue3 基础语法](https://www.runoob.com/vue3-syntax.html) **













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