# 核心业务开发

- Source: https://www.runoob.com/vue3/vue3-taskhub-task.html

接下来我们将在 App.vue 中构建核心任务管理逻辑。


**整个逻辑如下：**


- **数据流向**：输入框输入内容 -> `v-model` 更新 `newTaskTitle`。
- **动作触发**：按回车 -> 执行 `addTask` -> `tasks` 数组增加一项。
- **视图更新**：`tasks` 改变 -> 触发 `filteredTasks` 自动重新计算 -> Vue 重新渲染 `li` 列表。
- **状态流转**：点击过滤器按钮 -> 修改 `currentFilter` 值 -> 再次触发 `filteredTasks` 计算 -> 页面展示不同类别的任务。


### 基础布局与响应式数据


在 src/App.vue 中编写：


## 实例


```javascript
<script setup>
import { ref, computed } from 'vue';

// 1. 任务数据模型
const tasks = ref([
  { id: '1', title: '体验 Tailwind v4 新特性', isCompleted: false },
  { id: '2', title: '掌握 Composition API', isCompleted: true }
]);

const newTaskTitle = ref('');
const currentFilter = ref('all');

// 2. 核心方法
const addTask = () => {
  const title = newTaskTitle.value.trim();
  if (!title) return;

  tasks.value.unshift({
    id: crypto.randomUUID(),
    title,
    isCompleted: false
  });
  newTaskTitle.value = '';
};

const removeTask = (id) => {
  tasks.value = tasks.value.filter(t => t.id !== id);
};

const toggleTask = (id) => {
  const task = tasks.value.find(t => t.id === id);
  if (task) task.isCompleted = !task.isCompleted;
};

// 3. 计算属性处理过滤
const filteredTasks = computed(() => {
  if (currentFilter.value === 'active') return tasks.value.filter(t => !t.isCompleted);
  if (currentFilter.value === 'completed') return tasks.value.filter(t => t.isCompleted);
  return tasks.value;
});
</script>

<template>
  <div class="min-h-screen py-12 px-4">
    <div class="max-w-md mx-auto bg-white rounded-3xl shadow-xl shadow-slate-200 border border-slate-100 overflow-hidden">

      <header class="bg-linear-to-br from-blue-600 to-indigo-700 p-8 text-white">
        <h1 class="text-3xl font-black tracking-tight">TaskHub</h1>
        <p class="text-blue-100/80 text-sm">Vue 3 + Tailwind v4 实战</p>
      </header>

      <main class="p-6">
        <div class="flex gap-2 mb-8">
          <input
            v-model="newTaskTitle"
            @keyup.enter="addTask"
            placeholder="今天要完成什么？"
            class="flex-1 bg-slate-50 border-none rounded-2xl px-4 py-3 focus:ring-2 focus:ring-brand/50 outline-none transition-all"
          />
          <button @click="addTask" class="bg-brand text-white px-6 rounded-2xl font-bold hover:scale-105 active:scale-95 transition-all">
            +
          </button>
        </div>

        <div class="flex p-1 bg-slate-100 rounded-xl mb-6">
          <button
            v-for="f in ['all', 'active', 'completed']"
            :key="f"
            @click="currentFilter = f"
            :class="[
              'flex-1 py-1.5 text-xs font-bold rounded-lg transition-all capitalize',
              currentFilter === f ? 'bg-white text-brand shadow-sm' : 'text-slate-500'
            ]"
          >
            {{ f }}
          </button>
        </div>

        <ul class="space-y-3">
          <TransitionGroup name="list">
            <li
              v-for="task in filteredTasks"
              :key="task.id"
              class="group flex items-center justify-between p-4 bg-slate-50 rounded-2xl border border-transparent hover:border-slate-200 hover:bg-white transition-all"
            >
              <div class="flex items-center gap-3">
                <input
                  type="checkbox"
                  :checked="task.isCompleted"
                  @change="toggleTask(task.id)"
                  class="w-5 h-5 accent-brand cursor-pointer"
                />
                <span :class="['text-slate-700 font-medium', task.isCompleted ? 'line-through text-slate-400 opacity-50' : '']">
                  {{ task.title }}
                </span>
              </div>
              <button @click="removeTask(task.id)" class="opacity-0 group-hover:opacity-100 text-slate-300 hover:text-red-500 transition-all p-1">
                ✕
              </button>
            </li>
          </TransitionGroup>
        </ul>

        <div v-if="filteredTasks.length === 0" class="text-center py-12 text-slate-400 text-sm">
          暂无相关任务...
        </div>
      </main>
    </div>
  </div>
</template>

<style scoped>
/* 列表过渡动画 */
.list-enter-active, .list-leave-active { transition: all 0.4s cubic-bezier(0.18, 0.89, 0.32, 1.28); }
.list-enter-from, .list-leave-to { opacity: 0; transform: translateX(30px); }
</style>
```


运行后界面如下所示：


![](https://www.runoob.com/wp-content/uploads/2026/01/f7b2aa6a-b2c3-474c-8acd-b22df774f383.png)


---


## 核心知识点


### 1. 组合式 API (Composition API)


以上代码展示了 Vue 3 最核心的逻辑组织方式：


- **`ref` (响应式基础)**：`tasks`、`newTaskTitle` 等都是响应式引用。在 `` 中修改它们必须使用 `.value`（如 `tasks.value = ...`），但在 `` 中直接写变量名。Vue 会自动追踪这些值的变化并更新 UI。
- **`computed` (计算属性)**：`filteredTasks` 是一个非常经典的应用。它基于 `tasks` 和 `currentFilter` 派生而来。
- **优势**：它是响应式的，且具有**缓存性**。如果 `tasks` 没变，多次渲染页面时，它不会重复执行过滤逻辑。


### 2. 列表渲染与 Key 值


```
<li v-for="task in filteredTasks" :key="task.id">
```


- **`:key` 的重要性**：在 Vue 中，列表循环必须提供 `key`。这里使用了 `crypto.randomUUID()` 生成的唯一 ID。这保证了当列表顺序改变或删除某项时，Vue 能准确识别具体的 DOM 节点，避免渲染错乱（特别是带有动画或输入状态的列表）。


### 3. 事件处理与修饰符


- **`@keyup.enter`**：这是一个**按键修饰符**。它让 `addTask` 函数只在用户按下回车键时触发，极大提升了输入体验。
- **事件传参**：`removeTask(task.id)` 演示了如何在模板中向函数传递当前循环项的数据。


### 4. 双向绑定 (v-model)


- `v-model="newTaskTitle"` 实现了输入框和变量的同步。
- **原理**：它实际上是 `:value` 和 `@input` 的语法糖。


### 5. 动画系统 (TransitionGroup)


- 这是 Vue 内置的组件，专门用于处理列表（`v-for`）的增删。
- 它会自动在元素进入或离开时切换 CSS 类（如 `.list-enter-from`）。配合代码底部的 `style`，就实现了列表项平滑滑入和滑出的效果。


---


## Tailwind v4 样式特性讲解


Tailwind v4 相比 v3 更加强调 **原生 CSS 能力** 和 **简洁性**。


### 1. 全新的渐变语法


- **`bg-linear-to-br`**：在 v4 中，渐变不再需要 `bg-gradient-to-br` 这种冗长的写法，直接使用 `linear-to-方位` 更加贴近原生 CSS 的 `linear-gradient`。


### 2. 透明度处理


- **`text-blue-100/80`**：`/80` 表示 80% 的透明度。v4 对颜色的透明度处理非常直观，无需预设复杂的颜色配置。


### 3. 主题变量引用


- **`bg-brand`**：我们在 CSS 的 `@theme` 中定义了 `--color-brand`。在 v4 中，只要定义了 CSS 变量，Tailwind 就会自动生成对应的工具类（如 `bg-brand`, `text-brand`, `border-brand`），无需在 JS 配置文件里折腾。


### 4. 强大的交互伪类


- **`group` 与 `group-hover:opacity-100**`：
- 在 `li` 上设置 `group`。
- 在删除按钮上设置 `group-hover:opacity-100`。
- **效果**：实现"只有鼠标悬停在这一行时，删除按钮才显示"。这种**父子状态联动**不需要写一行 JS 代码。


- **`active:scale-95`**：利用 CSS 伪类快速实现点击时的按钮缩放反馈。


### 5. 现代边框与环影


- **`focus:ring-2 focus:ring-brand/50`**：输入框聚焦时，利用 `ring` 属性制造一个外发光边框，`brand/50` 保证了光晕的通透感，而不是死板的实色。








	  AI 思考中...





			** [环境搭建](https://www.runoob.com/vue3-taskhub-config.html)
			[组件拆分](https://www.runoob.com/vue3-taskhub-split.html) **













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