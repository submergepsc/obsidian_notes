# TypeScript + Vue3 实战

- Source: https://www.runoob.com/typescript/ts-vue3.html

Vue 3 对 TypeScript 有很好的支持，本教程介绍 Vue 3 + TypeScript 的开发实践。


Vue 3 的 Composition API 和 TypeScript 的类型系统完美结合，可以让代码更安全、更易维护。


**
Vue3 教程查看：[https://www.runoob.com/vue3/vue3-tutorial.html](https://www.runoob.com/../vue3/vue3-tutorial.html)


---






  Vue 3 + TypeScript 类型支持



  Vue 3 组件

    defineComponent()
    PropType<User>
    emits: ['edit', 'delete']




  组合式 API

    ref<T>(initial)
    computed<T>(() => {})
    reactive<T>(obj)




  类型定义

    interface User {
    id: number
    name: string
    }




  Vue 3 + TypeScript 优势



  完整的类型推断



  Props 类型检查



  Emits 事件类型





--- ## 为什么需要在 Vue 3 中使用 TypeScript Vue 3 从设计之初就全面拥抱 TypeScript，提供了极好的类型支持。


Composition API 的函数式写法与 TypeScript 类型系统完美配合：ref 有泛型支持、computed 有类型推断、props 有完整的类型检查。


使用 TypeScript 可以让 Vue 组件的属性、事件、响应式数据都有类型保护。


> Vue 3 原生支持：**Vue 3 的源码使用 TypeScript 编写，与 TypeScript 无缝集成。


---


## 创建项目


使用 Vite 创建支持 TypeScript 的 Vue 3 项目。


## 初始化


```javascript
# 使用 Vite 创建 Vue 3 + TypeScript 项目（推荐）
npm create vite@latest my-vue-app -- --template vue-ts

# 进入项目目录
cd my-vue-app

# 安装依赖
npm install
```


**
推荐：**Vite 是 Vue 官方推荐的建设工具，创建项目时直接选择 vue-ts 模板即可。


---


## 组件类型


使用 defineComponent 和 PropType 定义组件和 Props 类型。


## src/components/UserCard.vue


```javascript
<template>
  <div class="user-card">
    <h3>{{ user.name }}</h3>
    <p>{{ user.email }}</p>
    <button @click="handleEdit">编辑</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'

// 定义用户类型接口
interface User {
  id: number
  name: string
  email: string
}

export default defineComponent({
  name: 'UserCard',
  // Props 定义
  props: {
    // 使用 PropType 进行类型声明
    user: {
      type: Object as PropType<User>,
      required: true
    }
  },
  // 声明组件发出的事件
  emits: ['edit'],
  setup(props, { emit }) {
    // 处理编辑点击
    const handleEdit = () => {
      emit('edit', props.user)
    }

    return { handleEdit }
  }
})
</script>
```


**运行结果：**


```
UserCard 组件渲染成功
```


**
PropType：**当 props 的类型是复杂对象时，需要使用 PropType 进行类型断言。


---


## 组合式 API 类型


使用 ref、computed 等响应式 API 时，TypeScript 提供完整的类型支持。


## src/components/Counter.vue


```javascript
<template>
  <div>
    <p>计数: {{ count }}</p>
    <p>倍增: {{ doubled }}</p>
    <button @click="increment">+1</button>
    <button @click="decrement">-1</button>
  </div>
</template>

<script lang="ts">
import { ref, computed } from 'vue'

export default {
  setup() {
    // ref：定义响应式数据，泛型指定类型
    const count = ref<number>(0)

    // computed：计算属性，自动推断返回类型
    const doubled = computed(() => count.value * 2)

    // 定义方法
    const increment = () => {
      count.value++
    }

    const decrement = () => {
      count.value--
    }

    return { count, doubled, increment, decrement }
  }
}
</script>
```


**运行结果：**


```
Counter 组件渲染成功
```


**
类型推断：**Vue 3 的组合式 API 会根据初始值自动推断类型，复杂类型可以显式指定泛型。


---


## 接口定义


在 types 目录集中定义项目的类型接口。


## src/types/index.ts


```javascript
// 用户类型定义
export interface User {
  id: number       // 用户 ID
  name: string    // 用户名
  email: string   // 邮箱
  avatar?: string // 头像（可选）
}

// 创建用户的数据传输对象
export interface CreateUserDTO {
  name: string    // 用户名
  email: string  // 邮箱
  password: string // 密码
}

// 通用 API 响应类型
export interface ApiResponse<T> {
  success: boolean  // 是否成功
  data?: T         // 成功时的数据
  error?: string   // 失败时的错误信息
}
```


**
类型集中管理：**将类型定义放在 types 目录，便于在多个组件中复用。


---


## 注意事项


- **defineComponent：**提供完整的类型推断
- **PropType：**复杂 Props 类型需要使用
- **ref 泛型：**复杂类型显式指定
- **emits：**声明事件类型


**
最佳实践：**Vue 3 推荐使用组合式 API + TypeScript，可以获得最佳的开发体验。


---


## 总结


Vue 3 与 TypeScript 完美结合。


- **defineComponent：**获得完整的类型推断
- **PropType：**为 props 提供类型安全
- **ref：**泛型参数指定响应式类型
- **computed：**自动推断计算属性类型


**
建议：**Vue 3 项目强烈建议使用 TypeScript，特别是在大型应用中。








	  AI 思考中...





			** [TypeScript + Node.js 实战](https://www.runoob.com/ts-nodejs.html)
			[TypeScript + React 实战](https://www.runoob.com/ts-react.html) **













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