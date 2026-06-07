# Vue3 全局 API

- Source: https://www.runoob.com/vue3/vue3-global-api.html

Vue3 全局 API 如下：


| 序号 | API & 描述 | 实例 |
| --- | --- | --- |
| 1 | createApp() 创建 Vue 应用实例，通常用于客户端渲染。 | const app = createApp(App) |
| 2 | createSSRApp() 创建用于服务端渲染（SSR）的 Vue 应用实例。 | const app = createSSRApp(App) |
| 3 | app.mount() 将 Vue 应用实例挂载到指定的 DOM 元素上。 | app.mount('#app') |
| 4 | app.unmount() 卸载 Vue 应用实例。 | app.unmount() |
| 5 | app.onUnmount() 注册卸载时的回调函数。 | app.onUnmount(() => { console.log('App is being unmounted') }) |
| 6 | app.component() 注册全局组件，使组件在任何地方都可以使用。 | app.component('MyComponent', MyComponent) |
| 7 | app.directive() 注册全局指令，允许创建自定义指令。 | app.directive('focus', { mounted(el) { el.focus() } }) |
| 8 | app.use() 安装插件，插件可以为应用提供额外功能。 | app.use(SomePlugin) |
| 9 | app.mixin() 注册全局混入，向所有组件提供共享数据或方法。 | app.mixin({ methods: { globalMethod() { ... } } }) |
| 10 | app.provide() 向整个应用提供依赖，跨组件共享数据。 | app.provide('key', 'some value') |
| 11 | app.runWithContext() 在 Vue 应用上下文中运行一个函数，允许访问上下文数据。 | app.runWithContext(() => { console.log('Running inside app context') }) |
| 12 | app.version 获取 Vue 当前的版本号。 | console.log(app.version) |
| 13 | app.config 获取和设置应用实例的全局配置。 | app.config.globalProperties.$myProperty = 'value' |
| 14 | app.config.errorHandler 设置全局错误处理函数，在应用中出现未捕获的错误时触发。 | app.config.errorHandler = (err, vm, info) => { console.error(err) } |
| 15 | app.config.warnHandler 设置全局警告处理函数，处理应用中的警告信息。 | app.config.warnHandler = (msg, vm, trace) => { console.warn(msg) } |
| 16 | app.config.performance 启用性能监控，提供渲染性能数据。 | app.config.performance = true |
| 17 | app.config.compilerOptions 配置模板编译器的选项，控制模板的编译行为。 | app.config.compilerOptions.delimiters = ['[[', ']]'] |
| 18 | app.config.globalProperties 设置全局属性，应用中所有组件都可以访问。 | app.config.globalProperties.$myGlobalProperty = 'value' |
| 19 | app.config.optionMergeStrategies 定义组件选项合并策略，控制如何合并组件的选项。 | app.config.optionMergeStrategies.methods = (parent, child) => { return { ...parent, ...child } } |
| 20 | app.config.idPrefix 设置 Vue 实例 ID 的前缀，默认为 "vue-"。 | `app.config.idPrefix = 'myApp-' |
| 21 | app.config.throwUnhandledErrorInProduction 控制生产环境下是否抛出未处理的错误。 | app.config.throwUnhandledErrorInProduction = false |
| 22 | version 获取 Vue 当前的版本号。 | console.log(Vue.version) |
| 23 | nextTick() 在 DOM 更新完成后执行延迟回调，用于处理异步 DOM 更新。 | nextTick(() => { console.log('DOM updated') }) |
| 24 | defineComponent() 用于定义组件，提供类型推导和更简洁的语法。 | export default defineComponent({ name: 'MyComponent' }) |
| 25 | defineAsyncComponent() 定义异步组件，组件会在需要时进行懒加载。 | const AsyncComponent = defineAsyncComponent(() => import('./AsyncComponent.vue')) |


---


## 应用实例 API


### 1. createApp()


- **功能**: 创建一个 Vue 应用实例。
- **用法**: `createApp(rootComponent, rootProps)`
- **参数**: `rootComponent`: 根组件。
- `rootProps` (可选): 传递给根组件的 props。


## 实例


```javascript
import { createApp } from 'vue';
import App from './App.vue';

const app = createApp(App);
```


---


### 2. createSSRApp()


- **功能**: 创建一个支持服务器端渲染 (SSR) 的 Vue 应用实例。
- **用法**: `createSSRApp(rootComponent, rootProps)`
- **参数**: `rootComponent`: 根组件。
- `rootProps` (可选): 传递给根组件的 props。


## 实例


```javascript
import { createSSRApp } from 'vue';
import App from './App.vue';

const app = createSSRApp(App);
```


---


### 3. app.mount()


- **功能**: 将应用挂载到 DOM 元素上。
- **用法**: `app.mount(container)`
- **参数**: `container`: DOM 元素或选择器字符串。


## 实例


```javascript
app.mount('#app');
```


---


### 4. app.unmount()


- **功能**: 卸载应用实例。
- **用法**: `app.unmount()`


## 实例


```javascript
app.unmount();
```


---


### 5. app.onUnmount()


- **功能**: 注册一个回调函数，在应用卸载时调用。
- **用法**: `app.onUnmount(callback)`
- **参数**: `callback`: 卸载时调用的函数。


## 实例


```javascript
app.onUnmount(() => {
  console.log('App unmounted');
});
```


---


### 6. app.component()


- **功能**: 注册或获取全局组件。
- **用法**: 注册: `app.component(name, component)`
- 获取: `app.component(name)`



**参数**:


- `name`: 组件名称。
- `component`: 组件定义。


## 实例


```javascript
app.component('MyComponent', {
  template: '<div>My Component</div>'
});
```


---


### 7. app.directive()


- **功能**: 注册或获取全局指令。
- **用法**: 注册: `app.directive(name, directive)`
- 获取: `app.directive(name)`



**参数**:


- `name`: 指令名称。
- `directive`: 指令定义。


## 实例


```javascript
app.directive('focus', {
  mounted(el) {
    el.focus();
  }
});
```


---


### 8. app.use()


- **功能**: 安装插件。
- **用法**: `app.use(plugin, options)`
- **参数**: `plugin`: 插件。
- `options` (可选): 插件选项。


## 实例


```javascript
import MyPlugin from './MyPlugin';
app.use(MyPlugin);
```


---


### 9. app.mixin()


- **功能**: 全局混入选项。
- **用法**: `app.mixin(mixin)`
- **参数**: `mixin`: 混入对象。


## 实例


```javascript
app.mixin({
  created() {
    console.log('Global mixin created');
  }
});
```


---


### 10. app.provide()


- **功能**: 提供全局依赖。
- **用法**: `app.provide(key, value)`
- **参数**: `key`: 依赖名称。
- `value`: 依赖值。


## 实例


```javascript
app.provide('theme', 'dark');
```


---


### 11. app.runWithContext()


- **功能**: 在当前应用上下文中运行函数。
- **用法**: `app.runWithContext(fn)`
- **参数**: `fn`: 要运行的函数。


## 实例


```javascript
app.runWithContext(() => {
  console.log('Running with app context');
});
```


---


### 12. app.version


- **功能**: 获取 Vue 版本。
- **用法**: `app.version`


## 实例


```javascript
console.log(app.version);
```


---


### 13. app.config


- **功能**: 应用配置对象。
- **用法**: `app.config`


## 实例


```javascript
app.config.errorHandler = (err) => {
  console.error(err);
};
```


---


### 14. app.config.errorHandler


- **功能**: 全局错误处理函数。
- **用法**: `app.config.errorHandler = (err, vm, info) => {}`
- **参数**: `err`: 错误对象。
- `vm`: 发生错误的组件实例。
- `info`: 错误信息。


## 实例


```javascript
app.config.errorHandler = (err) => {
  console.error('Global error:', err);
};
```


---


### 15. app.config.warnHandler


- **功能**: 全局警告处理函数。
- **用法**: `app.config.warnHandler = (msg, vm, trace) => {}`
- **参数**: `msg`: 警告信息。
- `vm`: 发生警告的组件实例。
- `trace`: 警告堆栈。


## 实例


```javascript
app.config.warnHandler = (msg) => {
  console.warn('Global warning:', msg);
};
```


---


### 16. app.config.performance


- **功能**: 启用性能追踪。
- **用法**: `app.config.performance = true`


## 实例


```javascript
app.config.performance = true;
```


---


### 17. app.config.compilerOptions


- **功能**: 配置模板编译器的选项。
- **用法**: `app.config.compilerOptions = { /* options */ }`


## 实例


```javascript
app.config.compilerOptions = { whitespace: 'preserve' };
```


---


### 18. app.config.globalProperties


- **功能**: 添加全局属性。
- **用法**: `app.config.globalProperties[key] = value`


## 实例


```javascript
app.config.globalProperties.$myGlobal = 'Hello';
```


---


### 19. app.config.optionMergeStrategies


- **功能**: 自定义选项合并策略。
- **用法**: `app.config.optionMergeStrategies[key] = strategy`


## 实例


```javascript
app.config.optionMergeStrategies.customOption = (parent, child) => {
  return child || parent;
};
```


---


### 20. app.config.idPrefix


- **功能**: 设置组件 ID 前缀。
- **用法**: `app.config.idPrefix = 'my-app-'`


## 实例


```javascript
app.config.idPrefix = 'my-app-';
```


---


### 21. app.config.throwUnhandledErrorInProduction


- **功能**: 在生产环境中抛出未处理的错误。
- **用法**: `app.config.throwUnhandledErrorInProduction = true`


## 实例


```javascript
app.config.throwUnhandledErrorInProduction = true;
```


---


## 通用 API


### 1. version


- **功能**: 获取 Vue 版本。
- **用法**: `Vue.version`


## 实例


```javascript
console.log(Vue.version);
```


---


### 2. nextTick()


- **功能**: 在下次 DOM 更新循环结束之后执行回调。
- **用法**: `nextTick(callback)`
- **参数**: `callback`: 回调函数。


## 实例


```javascript
import { nextTick } from 'vue';
nextTick(() => {
  console.log('DOM updated');
});
```


---


### 3. defineComponent()


- **功能**: 定义一个组件。
- **用法**: `defineComponent(options)`
- **参数**: `options`: 组件选项。


## 实例


```javascript
import { defineComponent } from 'vue';
const MyComponent = defineComponent({
  template: '<div>My Component</div>'
});
```


---


### 4. defineAsyncComponent()


- **功能**: 定义一个异步组件。
- **用法**: `defineAsyncComponent(loader)`
- **参数**: `loader`: 异步加载函数。


## 实例


```javascript
import { defineAsyncComponent } from 'vue';
const AsyncComponent = defineAsyncComponent(() =>
  import('./MyComponent.vue')
);
```









	  AI 思考中...





			** [使用 VSCode 开发 Vue](https://www.runoob.com/vue3-vscode.html)
			[Vue3 选项式 API](https://www.runoob.com/vue3-options-api.html) **













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