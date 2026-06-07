# Vue3 内置组件

- Source: https://www.runoob.com/vue3/vue3-builtin-components.html

在 Vue.js 中，有一些内置的全局组件和内置组件，它们提供了一些常用的功能和布局支持，可以帮助开发者快速构建应用界面。

以下是一些常见的 Vue 内置组件和它们的作用：


### 1. component


`` 是一个抽象的组件，用于动态地渲染不同的组件或元素。

通过绑定 `is` 属性可以实现动态组件的切换和渲染。


```
<component :is="currentComponent"></component>
```


### 2. transition 和 transition-group


`` 和 `` 提供了在 Vue.js 中实现过渡和动画效果的功能。

通过定义过渡的 CSS 类名，可以控制元素在进入或离开 DOM 时的动画效果。


```
<transition name="fade">
  <div v-if="show">Hello!</div>
</transition>
```


```
<transition-group name="list" tag="ul">
  <li v-for="item in items" :key="item.id">{{ item.text }}</li>
</transition-group>
```



### 3. keep-alive



`` 是一个抽象组件，用于保持组件状态或避免多次渲染。

当组件被 `` 包裹时，其状态将会被缓存，而不是每次切换时重新渲染。


```
<keep-alive>
  <component :is="currentComponent"></component>
</keep-alive>
```



### 4. slot



`` 是 Vue.js 中用于插入内容的插槽组件。它允许父组件将子组件的内容传递到特定的插槽位置，使得组件更加灵活和可复用。


```
<child-component>
  <template #header>
    <h2>Header Content</h2>
  </template>
  <template #default>
    <p>Default Content</p>
  </template>
</child-component>
```


### 5. teleport



`` 允许你将 DOM 元素渲染到应用的任何地方，而不受当前 DOM 结构的限制。这在需要在应用中动态移动元素时非常有用，例如在模态框中渲染弹出内容。


```
<teleport to="body">
  <modal-dialog v-if="showModal">
    <!-- modal content -->
  </modal-dialog>
</teleport>
```



### 6. Suspense



`` 是 Vue.js 3.x 中新增的组件，用于处理异步组件的加载和状态。它可以在异步组件加载完成之前显示占位内容，并处理加载状态和错误。


```
<Suspense>
  <template #default>
    <AsyncComponent />
  </template>
  <template #fallback>
    <div>Loading...</div>
  </template>
</Suspense>
```









	  AI 思考中...





			** [Vue3 内置属性](https://www.runoob.com/vue3-builtin-attributes.html)
			[Vue 组件实例](https://www.runoob.com/vue-component-instance.html) **













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