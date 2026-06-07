# 路由系统

- Source: https://www.runoob.com/vue3/vue3-taskhub-router.html

上一章节我们的任务管理逻辑已经通过 Pinia 实现了持久化，现在我们需要为应用注入灵魂——**路由系统**。


在企业级开发中，路由不只是切换页面，更承担了**安全性（权限控制）**和**用户体验（动态标题）**的重任。


---


## 安装与基础配置


首先安装 Vue Router：


```
npm install vue-router
```


在 `src` 目录下创建 router 目录，并创建 `router/index.js` 文件。


![](https://www.runoob.com/wp-content/uploads/2026/01/4472e1e9-8bf2-4eac-a637-7aa428c7f7fb.png)


我们将定义两个页面：工作台 (Dashboard) 和 登录页 (Login)。


## 实例


```javascript
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue'),
    meta: { title: '登录 - TaskHub', requiresAuth: false }
  },
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/Dashboard.vue'),
    // 路由元信息 meta：用来存放自定义数据
    meta: {
      title: '我的工作台',
      requiresAuth: true,
      breadcrumb: '首页'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```


在 `src` 下创建 `views` 文件夹，并分配好页面。


- **`src/App.vue`**：根容器，只放 `` 和全局动画。
- **`src/views/Dashboard.vue`**：原本的 TaskHub 核心功能（任务列表、输入框等）。
- **`src/views/Login.vue`**：新增的登录页面。

完整结构如下：


![](https://www.runoob.com/wp-content/uploads/2026/01/ad04ab63-1cff-4eac-bc94-200db67c539e.png)


### 改造 App.vue (变成干净的容器)


## 实例


```javascript
<template>
  <div class="min-h-screen bg-slate-50">
    <router-view v-slot="{ Component }">
      <transition name="page" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<style>
/* 页面切换的淡入淡出效果 */
.page-enter-active, .page-leave-active {
  transition: opacity 0.2s ease;
}
.page-enter-from, .page-leave-to {
  opacity: 0;
}
</style>
```


### 把原本的逻辑迁入 Dashboard.vue


把之前在 `App.vue` 里写的那些代码（引入 Store、引入组件、模板布局）全部剪切到 `src/views/Dashboard.vue` 中。


## Dashboard.vue 文件代码


```javascript
<script setup>
import { storeToRefs } from 'pinia'
import { useTaskStore } from '@/stores/taskStore'
import { useRouter } from 'vue-router' // 引入路由
import TaskHeader from '@/components/TaskHeader.vue'
import TaskInput from '@/components/TaskInput.vue'
import TaskFilter from '@/components/TaskFilter.vue'
import TaskItem from '@/components/TaskItem.vue'

const taskStore = useTaskStore()
const router = useRouter()
const { filter, filteredTasks } = storeToRefs(taskStore)
const { addTask, removeTask, toggleTask } = taskStore

// 退出登录方法
const handleLogout = () => {
  localStorage.removeItem('isLoggedIn')
  router.push('/login')
}
</script>

<template>
  <div class="py-12 px-4">
    <div class="max-w-md mx-auto bg-white rounded-3xl shadow-xl border border-slate-100 overflow-hidden">
      <TaskHeader />
      <main class="p-6">
        <TaskInput @add-task="addTask" />
        <TaskFilter v-model="filter" />

        <ul class="space-y-3">
          <TransitionGroup name="list">
            <TaskItem
              v-for="task in filteredTasks"
              :key="task.id"
              :task="task"
              @toggle="toggleTask"
              @remove="removeTask"
            />
          </TransitionGroup>
        </ul>

        <button
          @click="handleLogout"
          class="mt-8 w-full py-2 text-xs text-slate-400 hover:text-red-500 transition-colors"
        >
          退出当前账号
        </button>
      </main>
    </div>
  </div>
</template>
```


### 登录逻辑实现 (Login.vue)


利用 Tailwind v4 快速构建一个极简登录页，并模拟登录行为。


## 实例


```javascript
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isLoading = ref(false)

const handleLogin = () => {
  isLoading.value = true
  // 模拟异步请求
  setTimeout(() => {
    localStorage.setItem('isLoggedIn', 'true')
    router.push('/') // 登录成功跳转首页
    isLoading.value = false
  }, 1000)
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-slate-50">
    <div class="p-8 bg-white rounded-3xl shadow-xl w-full max-w-sm border border-slate-100">
      <h2 class="text-2xl font-black mb-6 text-slate-800">欢迎回来</h2>
      <button
       @click="handleLogin"
       :disabled="isLoading"
       class="w-full bg-linear-to-r from-blue-600 to-indigo-600 text-white py-3 rounded-xl font-bold hover:opacity-90 active:scale-95 transition-all disabled:opacity-50"
     >
        {{ isLoading ? '登录中...' : '一键进入系统' }}
      </button>
      <p class="mt-4 text-center text-xs text-slate-400">测试环境：点击即可登录</p>
    </div>
  </div>
</template>
```


---


### 完善 router/index.js 的拦截逻辑


确保你的路由配置中已经开启了安检模式：


## 实例


```javascript
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue'),
    meta: { title: '登录 - TaskHub', requiresAuth: false }
  },
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/Dashboard.vue'),
    // 路由元信息 meta：用来存放自定义数据
    meta: {
      title: '我的工作台',
      requiresAuth: true,
      breadcrumb: '首页'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
// src/router/index.js (核心片段)
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('isLoggedIn') === 'true'

  // 如果去首页但没登录 -> 去登录
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login')
  }
  // 如果已登录还想去登录页 -> 回首页
  else if (to.path === '/login' && isAuthenticated) {
    next('/')
  }
  else {
    next()
  }
})
export default router
```


### 在 main.js 中完成最后拼图


确保你的 `main.js` 引入并挂载了路由：


## 实例


```javascript
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router' // 引入路由
import App from './App.vue'
import './style.css'

const app = createApp(App)
app.use(createPinia())
app.use(router) // 2. 注册路由
app.mount('#app')
```


### 最终效果


- **访问 /**`：如果你没登录，页面会闪现一下然后跳转到`/login。
- **访问 /login**`：点击按钮，本地存储`isLoggedIn`变为`true，然后瞬间切入工作台。
- **刷新页面**：Pinia 会从 LocalStorage 读取任务，路由守卫会检查登录状态，一切数据都不会丢失。


![](https://www.runoob.com/wp-content/uploads/2026/01/ab505e14-d85a-4626-8cef-ed041c8b89ce.png)


登录后，可以点击退出登录：


![](https://www.runoob.com/wp-content/uploads/2026/01/782917cb-1f4e-49f7-ad60-926a77de8605.png)


### 知识点讲解


- **为什么 `App.vue` 变空了？** 在单页面应用（SPA）中，`App.vue` 是整个应用的外壳。我们把它变空是为了能根据 URL 的变化，在其中动态地塞进不同的页面（Dashboard 或 Login）。
- **`useRouter` 的实战**： 在 `Dashboard.vue` 中，我们通过 `router.push('/login')` 实现了退出功能。注意：`push` 会向浏览器历史记录添加一条新记录，点击浏览器返回键是可以回退的。
- **Tailwind v4 的布局继承**： 由于我们在 `App.vue` 的全局容器里加了 `bg-slate-50` 和 `min-h-screen`，所有的子页面（Dashboard、Login）都会默认继承这个浅灰色背景，保证了视觉的统一性。










	  AI 思考中...





			** [状态管理与数据持久化](https://www.runoob.com/vue3-taskhub-states.html)
			[逻辑复用与性能优化](https://www.runoob.com/vue3-taskhub-optimization.html) **













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