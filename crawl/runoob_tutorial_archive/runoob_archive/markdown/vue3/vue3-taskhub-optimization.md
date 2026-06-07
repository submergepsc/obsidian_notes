# 逻辑复用与性能优化

- Source: https://www.runoob.com/vue3/vue3-taskhub-optimization.html

在完成路由与登录逻辑后，随着项目规模扩大，我们会发现有些逻辑（如存取本地数据、弹出通知）在多个页面反复出现。同时，如果任务列表达到上千条，页面可能会出现卡顿。


这一阶段，我们将通过 **Composition API 的深度应用** 来解决代码复用和性能瓶颈问题。


---


## 逻辑复用：自定义 Composables (Hooks)


Composables 是 Vue 3 的精髓，它允许我们将逻辑（State + Actions）抽离成独立函数。


### useLocalStorage：数据持久化逻辑抽离


不再在每个 Store 或组件里手写 `localStorage.getItem`。


## 实例


```javascript
// src/composables/useLocalStorage.js
import { ref, watch } from 'vue';

export function useLocalStorage(key, defaultValue = null) {
  // 1. 初始化数据
  const storedValue = localStorage.getItem(key);
  const data = ref(storedValue ? JSON.parse(storedValue) : defaultValue);

  // 2. 监听变化并自动同步
  watch(data, (newValue) => {
    localStorage.setItem(key, JSON.stringify(newValue));
  }, { deep: true });

  return data;
}
```


### useNotification：公共 UI 逻辑抽离


实现一个简单的通知提示功能。


## 实例


```javascript
// src/composables/useNotification.js
import { ref } from 'vue';

export function useNotification() {
  const message = ref('');
  const isVisible = ref(false);

  const notify = (msg, duration = 2000) => {
    message.value = msg;
    isVisible.value = true;
    setTimeout(() => {
      isVisible.value = false;
    }, duration);
  };

  return { message, isVisible, notify };
}
```


---


## 性能调优：处理大数据量与高频渲染


当你的 TaskHub 从管理 10 个任务增长到管理 1000 个任务时，Vue 默认的"深度响应式"会带来计算压力。


### shallowRef 与 markRaw


Vue 默认的 `ref` 是递归响应式的（即对象内部的每个属性都会被代理）。


**`shallowRef`**：只监听 `.value` 的指向变化，不监听对象内部属性的变化。


- *场景*：当你从后端获取一大串只读的任务历史记录时。

**`markRaw`**：标记一个对象，使其**永远不会**被转为响应式。


- *场景*：某些复杂的第三方库实例（如 ECharts 图表实例、地图实例），包装成响应式反而会报错或极度耗费性能。


```
// 性能优化示例
import { shallowRef, markRaw } from 'vue';

// 假设这是一万条历史归档数据
const archiveTasks = shallowRef([]);

const loadArchive = (data) => {
  // 仅在赋值时触发一次响应式更新，内部属性修改不触发
  archiveTasks.value = data;
};
```


### v-once 与 v-memo (指令级优化)


#### v-once：静态内容只渲染一次


如果某个任务渲染后就不再变化（比如任务的创建时间），使用 `v-once`。


```
<span v-once>创建于: {{ task.createdAt }}</span>
```


- **原理**：Vue 渲染后会跳过该节点的后续更新检查。


#### v-memo：按需更新（Vue 3.2+）


这是优化长列表最强大的指令。它接受一个依赖数组，只有当数组里的值变化时，该节点及其子节点才会重新渲染。


```
<li v-for="task in tasks" :key="task.id" v-memo="[task.isCompleted, task.title]">
  {{ task.title }} - {{ task.isCompleted }}
</li>
```


---


## 什么时候该调优？


| 方案 | 解决的问题 | 推荐场景 |
| --- | --- | --- |
| Composables | 代码重复、逻辑散乱 | 跨组件共享逻辑（如登录检查、主题切换） |
| shallowRef | 大对象深度代理导致的内存开销 | 列表数据量级 > 1000 且只需整体替换时 |
| v-memo | 频繁触发的长列表虚拟 DOM 比对 | 复杂的 v-for 列表，且单项只有少数属性会变 |


---


## 结合到之前的项目中


你可以尝试在 `TaskItem.vue` 中应用 `v-memo`：


```
<template>
  <li v-memo="[task.id, task.isCompleted]" class="...">
     ...
  </li>
</template>
```


**现在你的项目不仅逻辑清晰（Composables），而且性能强劲。**








	  AI 思考中...





			** [路由系统](https://www.runoob.com/vue3-taskhub-router.html)
			[项目部署](https://www.runoob.com/vue3-taskhub-production.html) **













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