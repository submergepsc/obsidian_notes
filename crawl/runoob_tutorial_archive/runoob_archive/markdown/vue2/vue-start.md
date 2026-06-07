# Vue.js 起步

- Source: https://www.runoob.com/vue2/vue-start.html

每个 Vue 应用都需要通过实例化 Vue 来实现。


语法格式如下：


```
var vm = new Vue({
  // 选项
})
```


接下来让我们通过实例来看下 Vue 构造器中需要哪些内容：


## 实例


```javascript
<div id="vue_det">
    <h1>site : {{site}}</h1>
    <h1>url : {{url}}</h1>
    <h1>{{details()}}</h1>
</div>
<script type="text/javascript">
    var vm = new Vue({
        el: '#vue_det',
        data: {
            site: "菜鸟教程",
            url: "www.runoob.com",
            alexa: "10000"
        },
        methods: {
            details: function() {
                return  this.site + " - 学的不仅是技术，更是梦想！";
            }
        }
    })
</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-start1)

点击 "尝试一下" 按钮查看在线实例


可以看到在 Vue 构造器中有一个el 参数，它是 DOM 元素中的 id。在上面实例中 id 为 vue_det，在 div 元素中：


```
<div id = "vue_det"></div>
```


这意味着我们接下来的改动全部在以上指定的 div 内，div 外部不受影响。


接下来我们看看如何定义数据对象。


data** 用于定义属性，实例中有三个属性分别为：site、url、alexa。


**methods** 用于定义的函数，可以通过 return 来返回函数值。


**{{ }}** 用于输出对象属性和函数返回值。


```
<div id="vue_det">
    <h1>site : {{site}}</h1>
    <h1>url : {{url}}</h1>
    <h1>{{details()}}</h1>
</div>
```


当一个 Vue 实例被创建时，它向 Vue 的响应式系统中加入了其 data 对象中能找到的所有的属性。当这些属性的值发生改变时，html 视图将也会产生相应的变化。


## 实例


```javascript
<div id="vue_det">
    <h1>site : {{site}}</h1>
    <h1>url : {{url}}</h1>
    <h1>Alexa : {{alexa}}</h1>
</div>
<script type="text/javascript">
// 我们的数据对象
var data = { site: "菜鸟教程", url: "www.runoob.com", alexa: 10000}
var vm = new Vue({
    el: '#vue_det',
    data: data
})
// 它们引用相同的对象！
document.write(vm.site === data.site) // true
document.write("<br>")
// 设置属性也会影响到原始数据
vm.site = "Runoob"
document.write(data.site + "<br>") // Runoob

// ……反之亦然
data.alexa = 1234
document.write(vm.alexa) // 1234
</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-start2)


除了数据属性，Vue 实例还提供了一些有用的实例属性与方法。它们都有前缀 $，以便与用户定义的属性区分开来。例如：


## 实例


```javascript
<div id="vue_det">
    <h1>site : {{site}}</h1>
    <h1>url : {{url}}</h1>
    <h1>Alexa : {{alexa}}</h1>
</div>
<script type="text/javascript">
// 我们的数据对象
var data = { site: "菜鸟教程", url: "www.runoob.com", alexa: 10000}
var vm = new Vue({
    el: '#vue_det',
    data: data
})

document.write(vm.$data === data) // true
document.write("<br>")
document.write(vm.$el === document.getElementById('vue_det')) // true
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-start3)








	  AI 思考中...





			** [Vue.js 路由](https://www.runoob.com/vue-routing.html)
			[Vue.js 监听属性](https://www.runoob.com/vue-watch.html) **













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