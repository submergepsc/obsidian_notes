# Vue3 内置指令

- Source: https://www.runoob.com/vue3/vue3-ref-directives.html

Vue.js 内置了多个指令（Directives），用于在模板中添加特定的响应式行为或操作 DOM。

以下是 Vue.js 中常用的内置指令：


| 指令 | 用法示例 | 说明 |
| --- | --- | --- |
| v-text |  | 更新元素的 textContent，类似于插值 {{ }}，但是是单向绑定。 |
| v-html |  | 更新元素的 innerHTML，用于输出 HTML。 |
| v-model |  | 在表单控件元素上创建双向数据绑定，将输入字段与数据属性同步。 |
| v-show |  | 根据表达式的真假切换元素的显示与隐藏，使用 CSS 的 display 属性。 |
| v-if | Visible | 根据表达式的真假条件性地渲染元素，当条件为假时元素将从 DOM 中移除。 |
| v-else | VisibleNot Visible | v-if 的补充指令，用于显示条件为假时的备用内容。 |
| v-else-if | Type AType B | 连续使用于 v-if 和 v-else 之后，用于多条件判断。 |
| v-for | {{ item }} | 遍历数组或对象的每个元素，生成相应数量的元素。 |
| v-on | Click me | 绑定事件监听器，用于监听 DOM 事件，可以简写为 @。 |
| v-bind |  | 动态绑定 HTML 属性，可以简写为 :。 |
| v-slot | Header | 用于具名插槽的语法，提供插入子组件内容的位置。 |
| v-pre | {{ message }} | 跳过这个元素和它的所有子元素的编译过程，用于显示原始 Mustache 标签。 |
| v-cloak | [v-cloak] { display: none; } | 在 Vue 实例编译完成前隐藏模板内容，避免显示未编译的 Mustache 标签。 |
| v-once | {{ message }} | 只渲染元素和组件一次，不会随后续数据变化而更新。 |
| v-memo |
```
<div v-memo="[valueA, valueB]">
  ...
</div>
```
 | 缓存一个模板的子树。 当组件重新渲染，如果 valueA 和 valueB 都保持不变，这个 及其子项的所有更新都将被跳过。实际上，甚至虚拟 DOM 的 vnode 创建也将被跳过，因为缓存的子树副本可以被重新使用。 |


### v-text


- **用法**: ``
- **说明**: 更新元素的 `textContent`，类似于插值 `{{ }}`，但是是单向绑定。可以用于设置元素的纯文本内容。


## 实例


```javascript
<p v-text="message"></p>
```


## 实例


```javascript
data() {
    return {
    message: 'Hello, Vue!'
    };
}
```


### v-html


- **用法**: ``
- **说明**: 更新元素的 `innerHTML`，用于输出包含 HTML 结构的内容。需要注意安全性，避免 XSS 攻击。


## 实例


```javascript
<div v-html="htmlContent"></div>
```


## 实例


```javascript
data() {
    return {
        htmlContent: '<strong>Vue.js</strong> is awesome!'
    };
}
```


### v-model


- **用法**: `*`
- **说明**: 在表单控件元素上创建双向数据绑定，将输入字段与数据属性同步，支持多种表单控件类型。


## 实例


```javascript
<input type="text" v-model="message">
```


## 实例


```javascript
data() {
    return {
    message: ''
    };
}
```


### v-show


- **用法**: ``
- **说明**: 根据表达式的真假切换元素的显示与隐藏，使用 CSS 的 `display` 属性控制元素的可见性。


## 实例


```javascript
<div v-show="isVisible">Visible when true</div>
```


## 实例


```javascript
data() {
    return {
    isVisible: true
    };
}
```


### v-if / v-else / v-else-if


- **用法**: `
Visible

Not Visible
`
- **说明**: 根据表达式的真假条件性地渲染元素。`v-else` 和 `v-else-if` 是 `v-if` 的补充指令，用于多条件判断。


## 实例


```javascript
<p v-if="isVisible">Visible</p>
<p v-else>Not Visible</p>
```


## 实例


```javascript
data() {
    return {
        isVisible: true
    };
}
```


### v-for


- **用法**: `{{ item }}`
- **说明**: 遍历数组或对象的每个元素，生成相应数量的元素，支持指定键（key）来提高渲染效率。


## 实例


```javascript
<ul>
<li v-for="(item, index) in items" :key="index">{{ item }}</li>
</ul>
```


## 实例


```javascript
data() {
    return {
        items: ['Apple', 'Banana', 'Cherry']
    };
}
```


### v-on (@)


- **用法**: `**Click me`
- **说明**: 绑定事件监听器，用于监听 DOM 事件，可以简写为 `@`。支持修饰符和动态事件名。


## 实例


```javascript
<button v-on:click="handleClick">Click me</button>
```


## 实例


```javascript
methods: {
    handleClick() {
    alert('Button clicked');
    }
}
```


### v-bind ( : )


- **用法**: `![](https://www.runoob.com/imageSrc)`
- **说明**: 动态绑定 HTML 属性，可以简写为 `:`。用于动态设置元素的属性，例如 `src`、`href` 等。


## 实例


```javascript
<img v-bind:src="imageSrc" alt="Vue Logo">
```


## 实例


```javascript
data() {
    return {
    imageSrc: 'https://vuejs.org/images/logo.png'
    };
}
```


### v-slot


- **用法**: `Header`
- **说明**: 用于具名插槽的语法，提供插入子组件内容的位置，用于自定义组件的内容分发。


## 实例


```javascript
<BaseLayout>
    <template v-slot:header>
    <h2>Header Content</h2>
    </template>
    <template v-slot:footer>
    <p>Footer Content</p>
    </template>
</BaseLayout>
```


## 实例


```javascript
// BaseLayout 组件定义
Vue.component('BaseLayout', {
    template: `
    <div>
        <header><slot name="header"></slot></header>
        <main><slot></slot></main>
        <footer><slot name="footer"></slot></footer>
    </div>
    `
});
```


### v-pre


- **用法**: `{{ message }}`
- **说明**: 跳过这个元素及其所有子元素的编译过程，用于显示原始 Mustache 标签，防止 Vue 编译内容。


## 实例


```javascript
<div v-pre>{{ message }}</div>
```


## 实例


```javascript
data() {
    return {
    message: 'Hello, Vue!'
    };
}
```


### v-cloak


- **用法**: `[v-cloak] { display: none; }`
- **说明**: 在 Vue 实例编译完成前隐藏模板内容，避免显示未编译的 Mustache 标签。


## 实例


```javascript
<div v-cloak>{{ message }}</div>
```


## 实例


```javascript
[v-cloak] { display: none; }
```


## 实例


```javascript
data() {
    return {
    message: 'Hello, Vue!'
    };
}
```


### v-once


- **用法**: `
{{ message }}
`
- **说明**: 只渲染元素和组件一次，不会随后续数据变化而更新，用于静态内容或不经常更新的内容。


## 实例


```javascript
<p v-once>{{ message }}</p>
```


## 实例


```javascript
data() {
    return {
    message: 'Hello, Vue!'
    };
}
```









	  AI 思考中...





			* [Vue 组件实例](https://www.runoob.com/vue-component-instance.html)
			[Vue 实例选项](https://www.runoob.com/vue-ref-options.html) **













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