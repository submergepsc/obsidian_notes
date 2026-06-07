# Vue3 路由(Vue Router)

- Source: https://www.runoob.com/vue3/vue3-routing.html

本章节我们将为大家介绍 Vue 路由。


Vue 路由允许我们通过不同的 URL 访问不同的内容。


通过 Vue 可以实现多视图的单页 Web 应用（single page web application，SPA）。


Vue.js 路由需要载入 [vue-router 库](https://github.com/vuejs/router)


中文文档地址：[vue-router 文档](https://router.vuejs.org/zh/guide/)。


Vue Router 负责将 URL 路径与应用中的组件进行映射，当用户在应用中浏览时，URL 会更新，但页面不会重新加载，从而提供流畅的用户体验。


![](https://www.runoob.com/wp-content/uploads/2021/03/20129187VHbf5OQ3Ur.png)


上图展示了一个**两层级的嵌套路由结构**：


- **顶层 (`App.vue` 的 ``)** 负责渲染**独立布局**（如 `Login.vue`）或**主框架布局**（`Layout.vue`）。
- **主框架布局 (`Layout.vue`)** 内部包含第二个 ``，用于渲染**功能页面的子组件**（如 `Dashboard.vue`、`User.vue`），从而实现页头、侧边栏和页脚的持久化显示。
- 未匹配的路径最终会导向独立的 `page404.vue`。


### 核心组成部分


| 组成部分 | 描述 | 选项式 API 访问 | 组合式 API 访问 |
| --- | --- | --- | --- |
| router 实例 | 整个路由系统的实例，用于全局导航、添加路由等。 | this.$router | useRouter() |
| route 对象 | 当前激活的路由状态对象，包含当前 URL、参数、查询等信息。 | this.$route | useRoute() |
|  | 用于在应用中进行导航的组件，会被渲染成一个 标签，但可以阻止默认的页面刷新。 | - | - |
|  | 路由匹配到的组件将渲染在这个位置。 | - | - |


---


## 安装


### npm 安装


```
npm install vue-router
```


### npm（国内镜像）


推荐使用淘宝镜像：


```
npm install -g cnpm --registry=https://registry.npmmirror.com
cnpm install vue-router@4
```


### 直接下载 / CDN


```
https://unpkg.com/vue-router@4
```


### 基本应用


### 1、创建路由表


```
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
```


### 2、在应用中挂载


```
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
```


### 3、页面出口


```
<router-view></router-view>
```


### 4、跳转


```
<router-link to="/about">About</router-link>
```


### 5、动态路由


```
{ path: '/user/:id', component: User }
```


访问 /user/10，$route.params.id === '10'。


### 6、懒加载


```
const About = () => import('../views/About.vue')
```


### 7、导航守卫（鉴权）


```
router.beforeEach((to, from, next) => {
  next()
})
```


### 8、重定向


```
{ path: '/old', redirect: '/' }
```


### 9、404


```
{ path: '/:pathMatch(.*)*', component: NotFound }
```


---


## 简单实例


Vue.js + vue-router 可以很简单的实现单页应用。


**** 是一个组件，该组件用于设置一个导航链接，切换不同 HTML 内容。 **to** 属性为目标地址， 即要显示的内容。


以下实例中我们将 vue-router 加进来，然后配置组件和路由映射，再告诉 vue-router 在哪里渲染它们。代码如下所示：


## HTML 代码


```javascript
<div id="app">
  <h1>Hello App!</h1>
  <p>
    <!--使用 router-link 组件进行导航 -->
    <!--通过传递 `to` 来指定链接 -->
    <!--`<router-link>` 将呈现一个带有正确 `href` 属性的 `<a>` 标签-->
    <router-link to="/">Go to Home</router-link>
    <router-link to="/about">Go to About</router-link>
  </p>
  <!-- 路由出口 -->
  <!-- 路由匹配到的组件将渲染在这里 -->
  <router-view></router-view>
</div>
```


### router-link

请注意，我们没有使用常规的 a 标签，而是使用一个自定义组件 router-link 来创建链接。这使得 Vue Router 可以在不重新加载页面的情况下更改 URL，处理 URL 的生成以及编码。我们将在后面看到如何从这些功能中获益。


### router-view

router-view 将显示与 url 对应的组件。你可以把它放在任何地方，以适应你的布局。


## JavaScript 代码


```javascript
// 1. 定义路由组件.
// 也可以从其他文件导入
const Home = { template: '<div>Home</div>' }
const About = { template: '<div>About</div>' }

// 2. 定义一些路由
// 每个路由都需要映射到一个组件。
// 我们后面再讨论嵌套路由。
const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
]

// 3. 创建路由实例并传递 `routes` 配置
// 你可以在这里输入更多的配置，但我们在这里
// 暂时保持简单
const router = VueRouter.createRouter({
  // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
  history: VueRouter.createWebHashHistory(),
  routes, // `routes: routes` 的缩写
})

// 5. 创建并挂载根实例
const app = Vue.createApp({})
//确保 _use_ 路由实例使
//整个应用支持路由。
app.use(router)

app.mount('#app')

// 现在，应用已经启动了！
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-routing&basepath=0)


点击过的导航链接都会加上样式 **class ="router-link-exact-active router-link-active"**。


### 应用实例


以下例子涵盖了路由的定义**、**创建**、**挂载**、**导航**和**渲染**五个核心步骤。


**1. main.js (入口文件)**


## 实例


```javascript
import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // 导入配置好的路由实例

// 1. 创建 Vue 应用实例
const app = createApp(App);

// 2. 挂载路由
app.use(router);

// 3. 挂载到 DOM
app.mount('#app');
```


**2. router/index.js (路由配置)**


## 实例


```javascript
import { createRouter, createWebHistory } from 'vue-router';

// 导入路由组件 (这里使用同步导入简化示例)
const Home = { template: '<h2>Home Page</h2><p>Welcome to the application home!</p>' };
const About = { template: '<h2>About Us</h2><p>Learn more about this project.</p>' };

// 定义路由记录数组
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  // 404 匹配 (放在最后)
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: { template: '<div>404 Not Found</div>' }
  }
];

// 创建 Router 实例
const router = createRouter({
  // 使用 HTML5 History 模式 (推荐)
  history: createWebHistory(),
  routes, // 路由配置
});

export default router;
```


**3. App.vue (根组件)**


## 实例


```javascript
<template>
  <div>
    <h1>Vue Router 示例</h1>

    <nav>
      <router-link to="/" active-class="active-link">Home</router-link> |
      <router-link to="/about" active-class="active-link">About</router-link> |
      <router-link to="/nonexistent">404 Demo</router-link>
    </nav>

    <hr>

    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<style>
/* 简单的激活样式 */
.active-link {
  font-weight: bold;
  color: #42b983; /* Vue 绿色 */
}
/* 调整链接间距 */
nav a {
  margin: 0 5px;
  text-decoration: none;
}
</style>
```


当您运行此应用时：


- 点击 **Home** 链接，URL 变为 `/`，`` 中显示 `Home Page` 组件内容。
- 点击 **About** 链接，URL 变为 `/about`，`` 中显示 `About Us` 组件内容。
- 点击 **404 Demo** 链接，URL 变为 `/nonexistent`，`` 中显示 `404 Not Found` 组件内容。


---

## 相关属性


接下来我们可以了解下更多关于  的属性。


### to


表示目标路由的链接。 当被点击后，内部会立刻把 to 的值传到 router.push()，所以这个值可以是一个字符串或者是描述目标位置的对象。


```
<!-- 字符串 -->
<router-link to="home">Home</router-link>
<!-- 渲染结果 -->
<a href="home">Home</a>

<!-- 使用 v-bind 的 JS 表达式 -->
<router-link v-bind:to="'home'">Home</router-link>

<!-- 不写 v-bind 也可以，就像绑定别的属性一样 -->
<router-link :to="'home'">Home</router-link>

<!-- 同上 -->
<router-link :to="{ path: 'home' }">Home</router-link>

<!-- 命名的路由 -->
<router-link :to="{ name: 'user', params: { userId: 123 }}">User</router-link>

<!-- 带查询参数，下面的结果为 /register?plan=private -->
<router-link :to="{ path: 'register', query: { plan: 'private' }}">Register</router-link>
```


### replace


设置 replace 属性的话，当点击时，会调用 router.replace() 而不是 router.push()，导航后不会留下 history 记录。


```
<router-link :to="{ path: '/abc'}" replace></router-link>
```


### append


设置 append 属性后，则在当前 (相对) 路径前添加其路径。例如，我们从 /a 导航到一个相对路径 b，如果没有配置 append，则路径为 /b，如果配了，则为 /a/b


```
<router-link :to="{ path: 'relative/path'}" append></router-link>
```


### tag


有时候想要 `` 渲染成某种标签，例如 ``。 于是我们使用 `tag` prop 类指定何种标签，同样它还是会监听点击，触发导航。


```
<router-link to="/foo" tag="li">foo</router-link>
<!-- 渲染结果 -->
<li>foo</li>
```


### active-class


设置 链接激活时使用的 CSS 类名。可以通过以下代码来替代。


```
<style>
   ._active{
      background-color : red;
   }
</style>
<p>
   <router-link v-bind:to = "{ path: '/route1'}" active-class = "_active">Router Link 1</router-link>
   <router-link v-bind:to = "{ path: '/route2'}" tag = "span">Router Link 2</router-link>
</p>
```


注意这里 **class** 使用 **active-class="_active"**。


### exact-active-class


配置当链接被精确匹配的时候应该激活的 class。可以通过以下代码来替代。


```
<p>
   <router-link v-bind:to = "{ path: '/route1'}" exact-active-class = "_active">Router Link 1</router-link>
   <router-link v-bind:to = "{ path: '/route2'}" tag = "span">Router Link 2</router-link>
</p>
```


### event


声明可以用来触发导航的事件。可以是一个字符串或是一个包含字符串的数组。


```
<router-link v-bind:to = "{ path: '/route1'}" event = "mouseover">Router Link 1</router-link>
```


以上代码设置了 event 为 mouseover ，及在鼠标移动到 Router Link 1 上时导航的 HTML 内容会发生改变。


---


## Vue Router (v4, Vue 3) 核心 API 手册


### 一、createRouter 配置项


| 配置项 | 用途 | 示例 |
| --- | --- | --- |
| history | 指定 URL 模式 | createWebHistory() |
| routes | 路由表定义数组 | [{ path: '/', component: Home }] |
| scrollBehavior | 控制页面滚动位置 | { top: 0 } |
| strict | 是否严格区分结尾斜杠 | true |
| linkActiveClass | 链接激活时的 Class | 'active' |
| linkExactActiveClass | 链接精确激活时的 Class | 'exact-active' |
| parseQuery | 自定义 URL Query 解析 | (q) => ({...}) |
| stringifyQuery | 自定义 URL Query 序列化 | (obj) => 'a=1' |


### 二、History 工厂


| API | 用途 | 示例 |
| --- | --- | --- |
| createWebHistory() | 使用 HTML5 History 模式（推荐） | createWebHistory() |
| createWebHashHistory() | 使用 Hash 模式（URL 带 #） | createWebHashHistory() |
| createMemoryHistory() | 适用于 SSR (服务端渲染) | createMemoryHistory() |


### 三、RouteRecord (路由表项)


| 字段 | 用途 | 示例 |
| --- | --- | --- |
| path | 路由路径定义 | /user/:id |
| name | 路由命名 | name: 'User' |
| component | 对应的主组件 | UserView |
| components | 用于命名视图 (多 ) | { default: A, left: B } |
| redirect | 重定向目标 | redirect: '/login' |
| children | 定义嵌套子路由 | [ { path: 'profile' } ] |
| props | 将 params 自动转为组件 props | props: true |
| meta | 自定义元信息字段 | { auth: true } |
| alias | 为当前路由添加别名（多入口） | alias: '/b' |
| beforeEnter | 路由独享导航守卫 | { beforeEnter: (to,from,next)=>{} } |


### 四、路由导航 (Router 实例方法)


| Router API | 用途 | 示例 |
| --- | --- | --- |
| router.push(to) | 编程式跳转，向 history 栈添加新记录 | router.push('/a') |
| router.replace(to) | 编程式跳转，替换当前 history 记录 | router.replace('/a') |
| router.back() | 后退一步 | router.back() |
| router.forward() | 前进一步 | router.forward() |
| router.go(n) | 手动偏移 history 栈 | router.go(-1) |
| router.addRoute(route) | 动态添加路由记录 | router.addRoute({ name:'Post', ... }) |
| router.removeRoute(name) | 通过名称移除路由记录 | router.removeRoute('user') |
| router.getRoutes() | 获取所有路由记录 | router.getRoutes() |
| router.hasRoute(name) | 判断是否存在指定名称的路由 | router.hasRoute('user') |


### 五、导航守卫


| 守卫 | 作用域 | 钩子签名 |
| --- | --- | --- |
| router.beforeEach | 全局前置 | (to, from, next) => {} |
| router.beforeResolve | 全局解析阶段（在组件内守卫和异步组件解析后） | (to, from, next) => {} |
| router.afterEach | 全局后置（不能阻止导航） | (to, from, failure) => {} |
| beforeEnter | 路由独享 | beforeEnter: (to, from, next) => {} |
| beforeRouteEnter | 组件内 (访问不到 this) | beforeRouteEnter(to, from, next) {} |
| beforeRouteUpdate | 组件内 (当前路由复用时，如参数变化) | beforeRouteUpdate(to, from, next) {} |
| beforeRouteLeave | 组件内 (离开该组件时) | beforeRouteLeave(to, from, next) {} |


### 六、 属性


| 属性 | 用途 | 示例 |
| --- | --- | --- |
| to | 目标路由地址 | to="/a" 或 :to="{ name: 'user', params: { id: 1 } }" |
| replace | 导航时使用 router.replace() |  |
| custom | 自定义渲染，结合插槽使用 |  |
| active-class | 链接激活时应用的 Class | 'active' |
| exact-active-class | 链接完全匹配时应用的 Class | 'exact' |


### 七、 属性


| 属性 | 用途 | 示例 |
| --- | --- | --- |
| name | 用于多视图 (命名视图) 渲染 |  |
| route | (高级) 强制指定要渲染的路由对象 |  |


### 八、Route (当前路由对象)


该对象通过 `useRoute()` 或 `this.$route` 获取。


| 字段 | 类型 | 含义 | 示例 |
| --- | --- | --- | --- |
| params | object | 动态路径参数 | route.params.id |
| query | object | URL 查询参数 | route.query.q |
| hash | string | URL 中的哈希值 (带 #) | route.hash |
| fullPath | string | 完整的解析后路径 (含查询和哈希) | /user/1?x=1 |
| name | string | 当前路由的命名 | 'User' |
| path | string | 当前路径 (不含查询和哈希) | /user/1 |
| meta | object | 路由配置中的 meta 信息 | route.meta.auth |
| matched | RouteRecord[] | 路由匹配到的所有记录 (用于嵌套路由) | route.matched |


### 九、组合式 API (Composition API)


| API | 用途 | 示例 |
| --- | --- | --- |
| useRoute() | 获取当前路由对象 (Route) | const route = useRoute() |
| useRouter() | 获取路由实例 (Router) | const router = useRouter() |


### 十、编程式导航 (完整示例)


| 用途 | 示例 | 备注 |
| --- | --- | --- |
| 命名路由跳转 | router.push({ name:'User', params:{ id:10 } }) | 推荐方式，不依赖路径顺序 |
| 带 Query 参数跳转 | router.push({ path:'/search', query:{ q:'x' } }) | 路径 + 查询参数 |
| 可等待的 Push/Replace | await router.push('/a') | 导航是异步的，可等待其完成 |
| URL 对象跳转 | router.push({ path: '/foo', hash: '#bar' }) | 完整控制 URL 细节 |








	  AI 思考中...





			** [Vue3 自定义指令](https://www.runoob.com/vue3-custom-directive.html)
			[Vue3 混入](https://www.runoob.com/vue3-mixins.html) **













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