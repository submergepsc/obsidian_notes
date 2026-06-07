# 

- Source: https://www.runoob.com/vue3/vue3-v-for.html

## Vue.js 循环语句


在 Vue 中，循环语句主要通过 v-for 指令来实现，用于遍历数组或对象，生成对应数量的元素。


在元素上使用 v-for 指令，根据源数据的数组或对象进行循环渲染元素。


遍历数组：


```
v-for="(item, index) in items"
```


遍历对象：


```
v-for="(value, key, index) in object"
```


- **key 的作用**: 使用 `v-for` 渲染列表时，必须为每个项提供一个唯一的 `key` 属性，以便 Vue 能够识别每个项的唯一性，从而进行高效的 DOM 更新。
- **嵌套循环**: 可以嵌套使用多个 `v-for` 来渲染多维数组或对象结构。


v-for 可以绑定数据到数组来渲染一个列表：


## v-for 实例


```javascript
<div id="app">
  <ol>
    <li v-for="site in sites">
      {{ site.text }}
    </li>
  </ol>
</div>
<script>
const app = {
  data() {
    return {
      sites: [
        { text: 'Google' },
        { text: 'Runoob' },
        { text: 'Taobao' }
      ]
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-for)

v-for 还支持一个可选的第二个参数，参数值为当前项的索引：


## v-for 实例


index 为列表项的索引值：


```javascript
<div id="app">
  <ol>
    <li v-for="(site, index) in sites">
      {{ index }} -{{ site.text }}
    </li>
  </ol>
</div>
<script>
const app = {
  data() {
    return {
      sites: [
        { text: 'Google' },
        { text: 'Runoob' },
        { text: 'Taobao' }
      ]
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-for-index)

模板  中使用 v-for：


## v-for


```javascript
<ul>
  <template v-for="site in sites">
    <li>{{ site.text }}</li>
    <li>--------------</li>
  </template>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-for2)


### v-for 迭代对象


v-for 可以通过一个对象的属性来迭代数据：


## v-for


```javascript
<div id="app">
  <ul>
    <li v-for="value in object">
    {{ value }}
    </li>
  </ul>
</div>

<script>
const app = {
  data() {
    return {
      object: {
        name: '菜鸟教程',
        url: 'http://www.runoob.com',
        slogan: '学的不仅是技术，更是梦想！'
      }
    }
  }
}

Vue.createApp(app).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-for-obj)


你也可以提供第二个的参数为键名：


## v-for


```javascript
<div id="app">
  <ul>
    <li v-for="(value, key) in object">
    {{ key }} : {{ value }}
    </li>
  </ul>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-for-obj2)


第三个参数为索引：


## v-for


```javascript
<div id="app">
  <ul>
    <li v-for="(value, key, index) in object">
     {{ index }}. {{ key }} : {{ value }}
    </li>
  </ul>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-for-obj3)


### v-for 迭代整数


v-for 也可以循环整数


## v-for


```javascript
<div id="app">
  <ul>
    <li v-for="n in 10">
     {{ n }}
    </li>
  </ul>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-for-int)


## 显示过滤/排序后的结果


我们可以对数组的元素进行处理后再显示出来，一般可以通过创建一个计算属性，来返回过滤或排序后的数组。


## v-for 实例


输出数组中的偶数：


```javascript
<div id="app">
  <ul>
    <li v-for="n in evenNumbers">{{ n }}</li>
  </ul>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-for-evenNumbers)


### v-for/v-if 联合使用


以上实例联合使用 v-for/v-if 给 select 设置默认值：


## v-for/v-if 实例


v-for 循环出列表，v-if 设置选中值：


```javascript
<div id="app">
   <select @change="changeVal($event)" v-model="selOption">
      <template v-for="(site,index) in sites" :site="site" :index="index" :key="site.id">
         <!-- 索引为 1 的设为默认值，索引值从0 开始-->
         <option v-if = "index == 1" :value="site.name" selected>{{site.name}}</option>
         <option v-else :value="site.name">{{site.name}}</option>
      </template>
   </select>
   <div>您选中了:{{selOption}}</div>
</div>

<script>
const app = {
    data() {
        return {
            selOption: "Runoob",
            sites: [
                  {id:1,name:"Google"},
                  {id:2,name:"Runoob"},
                  {id:3,name:"Taobao"},
            ]
         }

    },
    methods:{
        changeVal:function(event){
            this.selOption = event.target.value;
            alert("你选中了"+this.selOption);
        }
    }
}

Vue.createApp(app).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-for-if)


## 在组件上使用 v-for


如果你还没了解组件的内容，可以先跳过这部分。

在自定义组件上，你可以像在任何普通元素上一样使用 v-for：


```
<my-component v-for="item in items" :key="item.id"></my-component>
```


然而，任何数据都不会被自动传递到组件里，因为组件有自己独立的作用域。为了把迭代数据传递到组件里，我们要使用 props：


```
<my-component
  v-for="(item, index) in items"
  :item="item"
  :index="index"
  :key="item.id"
></my-component>
```


不自动将 item 注入到组件里的原因是，这会使得组件与 v-for 的运作紧密耦合。明确组件数据的来源能够使组件在其他场合重复使用。


下面是一个简单的 todo 列表的完整例子：


## 实例


```javascript
<div id="todo-list-example">
  <form v-on:submit.prevent="addNewTodo">
    <label for="new-todo">Add a todo</label>
    <input
      v-model="newTodoText"
      id="new-todo"
      placeholder="E.g. Feed the cat"
    />
    <button>Add</button>
  </form>
  <ul>
    <todo-item
      v-for="(todo, index) in todos"
      :key="todo.id"
      :title="todo.title"
      @remove="todos.splice(index, 1)"
    ></todo-item>
  </ul>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-v-for-component)









	  AI 思考中...





			** [Vue3 条件语句](https://www.runoob.com/vue3-v-if.html)
			[Vue3 计算属性](https://www.runoob.com/vu3-computed.html) **













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