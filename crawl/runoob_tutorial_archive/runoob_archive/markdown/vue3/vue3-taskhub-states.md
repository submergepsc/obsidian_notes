# 状态管理与数据持久化

- Source: https://www.runoob.com/vue3/vue3-taskhub-states.html

上一章节已经完成了组件化，我们现在面临最后一个实战痛点：**页面刷新，数据全丢**。


为了解决这个问题，我们将引入 Vue 官方推荐的状态管理库 **Pinia**，并结合 **Tailwind v4** 的样式能力，实现数据的**持久化存储**。


---


## Pinia 状态管理与数据持久化

Pinia 是 Vue.js 的轻量级状态管理库，它让你能够在组件之间共享和管理状态，我们可以把 Pinia 想象成一个全局的数据仓库，所有组件都可以从这里获取数据或者更新数据。


Pinia 相关内容参考：[Pinia 入门教程](https://www.runoob.com/vue3-pinia.html)。


### 为什么要用 Pinia？


在之前的代码中，数据都在 `App.vue` 里。如果项目变大（比如增加统计页面、用户中心），在组件间传递数据会变成套娃式的噩梦（Props Hell）。


- **Pinia** 提供了一个全局的数据仓库。
- 任何组件都可以直接从仓库取数据，或者触发仓库的方法。


安装与初始化：


```
npm install pinia
npm install @vue/devtools-kit -D
```


在 src/main.js 中注册：


## 实例


```javascript
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import './style.css'

const app = createApp(App)
app.use(createPinia()) // 插件注册
app.mount('#app')
```


### 创建 Task Store (仓库)


在 src 目录下创建 stores 目录，然后在 src/stores 目录下新建 taskStore.js。


![](https://www.runoob.com/wp-content/uploads/2026/01/f163b796-0f1f-43ec-8764-3cd4bcfaff5a.png)


我们将把原本在 App.vue 里的逻辑全部搬过来。


## 实例


```javascript
import { defineStore } from 'pinia'
import { ref, computed, watch } from 'vue'

export const useTaskStore = defineStore('task-store', () => {
  // --- 1. 状态 (State) ---
  // 尝试从 LocalStorage 读取初始值
  const savedTasks = localStorage.getItem('my-tasks')
  const tasks = ref(savedTasks ? JSON.parse(savedTasks) : [])
  const filter = ref('all')

  // --- 2. 派生状态 (Getters) ---
  const filteredTasks = computed(() => {
    if (filter.value === 'active') return tasks.value.filter(t => !t.isCompleted)
    if (filter.value === 'completed') return tasks.value.filter(t => t.isCompleted)
    return tasks.value
  })

  // --- 3. 动作 (Actions) ---
  const addTask = (title) => {
    tasks.value.unshift({ id: crypto.randomUUID(), title, isCompleted: false })
  }

  const removeTask = (id) => {
    tasks.value = tasks.value.filter(t => t.id !== id)
  }

  const toggleTask = (id) => {
    const task = tasks.value.find(t => t.id === id)
    if (task) task.isCompleted = !task.isCompleted
  }

  // --- 4. 持久化 (Persistence) ---
  // 监听 tasks 的变化，一旦变化就写入 LocalStorage
  watch(tasks, (newVal) => {
    localStorage.setItem('my-tasks', JSON.stringify(newVal))
  }, { deep: true }) // 深度监听数组内部对象的变化

  return {
    tasks,
    filter,
    filteredTasks,
    addTask,
    removeTask,
    toggleTask
  }
})
```


### 重构 App.vue (连接仓库)

现在的 App.vue 不需要自己管理数据了，只需调用 Store 即可。


## 实例


```javascript
<script setup>
import { storeToRefs } from 'pinia'
import { useTaskStore } from '@/stores/taskStore'
import TaskHeader from './components/TaskHeader.vue'
import TaskInput from './components/TaskInput.vue'
import TaskFilter from './components/TaskFilter.vue'
import TaskItem from './components/TaskItem.vue'

// 初始化仓库
const taskStore = useTaskStore()

// 使用 storeToRefs 保持数据的响应式解构
// 这样在模板里可以直接用 filter 和 filteredTasks
const { filter, filteredTasks } = storeToRefs(taskStore)
const { addTask, removeTask, toggleTask } = taskStore
</script>

<template>
  <div class="min-h-screen py-12 px-4">
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
      </main>
    </div>
  </div>
</template>
```


---


## 知识点详解


### 1. storeToRefs 是什么？


如果你直接这样写：`const { filter } = taskStore`，你会丢失响应式。当你修改 `filter` 时，页面不会刷新。


- **原因**：Store 是一个用 `reactive` 包裹的对象，直接解构会破坏引用。
- **解决方法**：使用 `storeToRefs`。它会将仓库里的状态转换为 `ref`，确保解构后依然能"牵一发而动全身"。


### 2. watch 的深度监听 (deep: true)


在持久化逻辑中，我们监听的是 `tasks` 数组。


- 如果不加 `{ deep: true }`，只有当数组被替换（如 `tasks.value = []`）时才会触发保存。
- 加上后，数组内部对象的属性修改（如任务从"待办"变"完成"）也会被捕获并存入硬盘。


### 3. 持久化思路


我们采用了"初始化读取 + 变更写入"的闭环：


- **读取**：Store 创建时从 `localStorage` 获取数据，让应用有"记忆"。
- **写入**：利用 `watch` 实现全自动化同步，开发者再也不用手动写 `setItem`。


---


## Tailwind v4 的最终润色


在 Store 的加持下，我们可以给应用增加一些**全局反馈样式**。比如在 `TaskHeader.vue` 中展示任务进度：


## 实例


```javascript
<script setup>
<script setup>
import { computed } from 'vue';
import { storeToRefs } from 'pinia';
import { useTaskStore } from '@/stores/taskStore'; // 确保路径正确

// 1. 初始化 store
const taskStore = useTaskStore();

// 2. 使用 storeToRefs 解构 tasks，确保它是响应式的
// 如果直接 const { tasks } = taskStore; 进度条将不会随勾选而移动
const { tasks } = storeToRefs(taskStore);

// 3. 编写进度逻辑
const progress = computed(() => {
  const total = tasks.value.length;
  if (total === 0) return 0; // 防止除以零

  const completedCount = tasks.value.filter(t => t.isCompleted).length;
  // 计算百分比并取整
  return Math.round((completedCount / total) * 100);
});
</script>

<template>
  <header class="bg-linear-to-br from-blue-600 to-indigo-700 p-8 text-white">
    <h1 class="text-3xl font-black tracking-tight">TaskHub</h1>

    <div class="mt-6">
      <div class="flex justify-between items-end mb-2">
        <p class="text-blue-100/80 text-xs font-bold uppercase tracking-wider">完成进度</p>
        <span class="text-2xl font-mono font-black">{{ progress }}%</span>
      </div>

      <div class="h-2 w-full bg-white/20 rounded-full overflow-hidden backdrop-blur-sm">
        <div
          class="h-full bg-white shadow-[0_0_15px_rgba(255,255,255,0.5)] transition-all duration-500 ease-out"
          :style="{ width: `${progress}%` }"
        ></div>
      </div>
    </div>
  </header>
</template>
```


修改后，整个界面就有了进度条的功能：


![](https://www.runoob.com/wp-content/uploads/2026/01/45d8fc70-cab5-464b-b25f-c217e74197cd.png)









	  AI 思考中...





			** [组件拆分](https://www.runoob.com/vue3-taskhub-split.html)
			[路由系统](https://www.runoob.com/vue3-taskhub-router.html) **













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