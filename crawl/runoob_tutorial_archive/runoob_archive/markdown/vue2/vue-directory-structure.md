# Vue.js 目录结构

- Source: https://www.runoob.com/vue2/vue-directory-structure.html

上一章节中我们使用了 npm 安装项目，我们在 IDE（Eclipse、Atom等） 中打开该目录，结构如下所示：


![](https://www.runoob.com/wp-content/uploads/2017/01/B6E593E3-F284-4C58-A610-94C6ACDAD485.jpg)


### 目录解析


| 目录/文件 | 说明 |
| --- | --- |
| build | 项目构建(webpack)相关代码 |
| config | 配置目录，包括端口号等。我们初学可以使用默认的。 |
| node_modules | npm 加载的项目依赖模块 |
| src | 这里是我们要开发的目录，基本上要做的事情都在这个目录里。里面包含了几个目录及文件： assets: 放置一些图片，如logo等。 components: 目录里面放了一个组件文件，可以不用。 App.vue: 项目入口文件，我们也可以直接将组件写这里，而不使用 components 目录。 main.js: 项目的核心文件。 |
| static | 静态资源目录，如图片、字体等。 |
| test | 初始测试目录，可删除 |
| .xxxx文件 | 这些是一些配置文件，包括语法配置，git配置等。 |
| index.html | 首页入口文件，你可以添加一些 meta 信息或统计代码啥的。 |
| package.json | 项目配置文件。 |
| README.md | 项目的说明文档，markdown 格式 |


在前面我们打开 APP.vue 文件，代码如下（解释在注释中）：


## src/APP.vue


```javascript
<!-- 展示模板 -->
<template>
  <div id="app">
    <img src="./assets/logo.png">
    <hello></hello>
  </div>
</template>

<script>
// 导入组件
import Hello from './components/Hello'

export default {
  name: 'app',
  components: {
    Hello
  }
}
</script>
<!-- 样式代码 -->
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```


**


接下来我们可以尝试修改下初始化的项目，将 Hello.vue 修改为以下代码：


## src/components/Hello.vue


```javascript
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: '欢迎来到菜鸟教程！'
    }
  }
}
</script>
```


重新打开页面 http://localhost:8080/，一般修改后会自动刷新，显示效果如下所示:

![](https://www.runoob.com/wp-content/uploads/2017/01/AEDE7289-0479-4F14-A9C9-898470E5620E.jpg)








	  AI 思考中...





			** [Vue.js 条件语句](https://www.runoob.com/vue-if.html)
			[Vue.js 计算属性](https://www.runoob.com/vue-computed.html) **













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