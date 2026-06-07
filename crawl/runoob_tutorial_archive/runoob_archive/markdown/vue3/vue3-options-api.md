# Vue3 选项式 API

- Source: https://www.runoob.com/vue3/vue3-options-api.html

以下 API 广泛用于 Vue 的选项式 API 中，用于管理状态、生命周期、插槽、依赖注入等功能。


### 1. 状态选项


| 序号 | API & 描述 | 实例 |
| --- | --- | --- |
| 1 | data 组件的数据选项，用于定义组件的状态。 | data() { return { count: 0 }; } |
| 2 | props 组件的 props 选项，定义父组件传递给子组件的数据。 | props: { msg: String } |
| 3 | computed 计算属性，用于定义基于组件状态（data、props）的派生值。 | computed: { doubledCount() { return this.count * 2; } } |
| 4 | methods 组件的方法选项，用于定义组件的业务逻辑。 | methods: { increment() { this.count += 1; } } |
| 5 | watch 监听组件的响应式数据变化，并执行回调。 | watch: { count(newVal) { console.log(newVal); } } |
| 6 | emits 定义组件可以触发的自定义事件。 | emits: ['update'] |
| 7 | expose 显式暴露给父组件访问的属性或方法。 | expose() { return { method } } |


### 2. 渲染选项


| 序号 | API & 描述 | 实例 |
| --- | --- | --- |
| 1 | template 定义组件的 HTML 模板。 | {{ count }} |
| 2 | render 使用渲染函数替代模板。 | render(h) { return h('button', { on: { click: this.increment } }, this.count) } |
| 3 | compilerOptions 配置模板编译器的选项。 | compilerOptions: { delimiters: ['{{', '}}'] } |
| 4 | slots 定义组件的插槽。 |  |


### 3. 生命周期选项


| 序号 | API & 描述 | 实例 |
| --- | --- | --- |
| 1 | beforeCreate 在组件实例化之前被调用。 | beforeCreate() { console.log('Before Create') } |
| 2 | created 组件实例已创建后调用，数据已设置。 | created() { console.log('Created') } |
| 3 | beforeMount 在挂载到 DOM 前调用，模板已编译。 | beforeMount() { console.log('Before Mount') } |
| 4 | mounted 在组件挂载到 DOM 后调用。 | mounted() { console.log('Mounted') } |
| 5 | beforeUpdate 数据变化后、组件重新渲染前调用。 | beforeUpdate() { console.log('Before Update') } |
| 6 | updated 组件更新完成后调用。 | updated() { console.log('Updated') } |
| 7 | beforeUnmount 组件卸载之前调用。 | beforeUnmount() { console.log('Before Unmount') } |
| 8 | unmounted 组件卸载后调用。 | unmounted() { console.log('Unmounted') } |
| 9 | errorCaptured 捕获子组件错误时调用。 | errorCaptured(err, vm, info) { console.error(err) } |
| 10 | renderTracked 在响应式数据发生变化并且重新渲染时调用。 | renderTracked(event) { console.log('Render Tracked') } |
| 11 | renderTriggered 在响应式数据触发重新渲染时调用。 | renderTriggered(event) { console.log('Render Triggered') } |
| 12 | activated 组件被激活时调用（仅用于 keep-alive 组件）。 | activated() { console.log('Activated') } |
| 13 | deactivated 组件被停用时调用（仅用于 keep-alive 组件）。 | deactivated() { console.log('Deactivated') } |
| 14 | serverPrefetch 服务器端渲染时获取数据的钩子。 | serverPrefetch() { return fetchData() } |


### 4. 组合选项


| 序号 | API & 描述 | 实例 |
| --- | --- | --- |
| 1 | provide 提供依赖给后代组件。 | provide('key', 'value') |
| 2 | inject 从祖先组件中注入依赖。 | inject('key') |
| 3 | mixins 引入外部混入（Mixin），以便复用逻辑。 | mixins: [myMixin] |
| 4 | extends 组件扩展另一个组件的选项。 | extends: MyComponent |


### 5. 其他杂项


| 序号 | API & 描述 | 实例 |
| --- | --- | --- |
| 1 | name 组件的名称，通常用于调试。 | name: 'MyComponent' |
| 2 | inheritAttrs 控制是否将父级组件的属性（attrs）自动继承到根元素。 | inheritAttrs: false |
| 3 | components 注册局部组件，使其可以在当前组件中使用。 | components: { LocalComponent } |
| 4 | directives 注册局部指令，使其可以在当前组件中使用。 | directives: { focus: FocusDirective } |


### 6. 组件实例


| 序号 | API & 描述 | 实例 |
| --- | --- | --- |
| 1 | $data 获取组件的数据对象。 | this.$data.count |
| 2 | $props 获取组件的 props 对象。 | this.$props.msg |
| 3 | $el 获取组件挂载的 DOM 元素。 | this.$el |
| 4 | $options 获取组件的配置选项。 | this.$options.name |
| 5 | $parent 获取父组件的实例。 | this.$parent |
| 6 | $root 获取根组件的实例。 | this.$root |
| 7 | $slots 获取组件的插槽内容。 | this.$slots.default |
| 8 | $refs 获取组件的引用对象。 | this.$refs.input |
| 9 | $attrs 获取所有未绑定到组件 props 的属性。 | this.$attrs |
| 10 | $watch() 监视组件实例的响应式数据或计算属性。 | this.$watch('count', (newCount) => { console.log(newCount) }) |
| 11 | $emit() 触发一个自定义事件。 | this.$emit('update', newVal) |
| 12 | $forceUpdate() 强制 Vue 重新渲染组件。 | this.$forceUpdate() |
| 13 | $nextTick() 在下次 DOM 更新循环结束之后执行回调。 | this.$nextTick(() => { console.log('DOM updated') }) |








	  AI 思考中...





			** [Vue3 全局 API](https://www.runoob.com/vue3-global-api.html)
			[Vue3 项目说明](https://www.runoob.com/vue3-project-intro.html) **













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