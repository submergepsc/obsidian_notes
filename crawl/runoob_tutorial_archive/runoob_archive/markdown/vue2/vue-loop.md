# 

- Source: https://www.runoob.com/vue2/vue-loop.html

## Vue.js 循环语句


循环使用 v-for 指令。

v-for 指令需要以 **site in sites** 形式的特殊语法， sites 是源数据数组并且 site 是数组元素迭代的别名。

v-for 可以绑定数据到数组来渲染一个列表：


## v-for 指令


```javascript
<div id="app">
  <ol>
    <li v-for="site in sites">
      {{ site.name }}
    </li>
  </ol>
</div>

<script>
new Vue({
  el: '#app',
  data: {
    sites: [
      { name: 'Runoob' },
      { name: 'Google' },
      { name: 'Taobao' }
    ]
  }
})
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-v-for)


模板中使用 v-for：


## v-for


```javascript
<ul>
  <template v-for="site in sites">
    <li>{{ site.name }}</li>
    <li>--------------</li>
  </template>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-v-for2)


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
new Vue({
  el: '#app',
  data: {
    object: {
      name: '菜鸟教程',
      url: 'http://www.runoob.com',
      slogan: '学的不仅是技术，更是梦想！'
    }
  }
})
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-v-for-obj)


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


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-v-for-obj2)


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


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-v-for-obj3)


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


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-v-for-int)









	  AI 思考中...





			** [Vue.js 样式绑定](https://www.runoob.com/vue-class-style.html)
			[Vue.js 事件处理器](https://www.runoob.com/vue-events.html) **