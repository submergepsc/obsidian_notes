# Vue3 安装

- Source: https://www.runoob.com/vue3/vue3-install.html

## 1、独立版本


我们可以在 Vue.js 的官网上直接下载最新版本, 并用 **** 标签引入。


[下载 Vue.js](https://unpkg.com/vue@3/dist/vue.global.js)


---


## 2、使用 CDN 方法


以下推荐国外比较稳定的两个 CDN，国内还没发现哪一家比较好，目前还是建议下载到本地。


- **cdnjs** : [https://cdnjs.cloudflare.com/ajax/libs/vue/3.0.5/vue.global.js](https://cdnjs.cloudflare.com/ajax/libs/vue/3.0.5/vue.global.js)
- **Staticfile CDN（国内）** : [https://cdn.staticfile.net/vue/3.0.5/vue.global.js](https://cdn.staticfile.net/vue/3.0.5/vue.global.js)
- **unpkg**：[https://unpkg.com/vue@3/dist/vue.global.js](https://unpkg.com/vue@3/dist/vue.global.js), 会保持和 npm 发布的最新的版本一致。


## Staticfile CDN（国内）


```javascript
<div id="app">
  <p>{{ message }}</p>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-bc)


## 字节跳动 CDN（国内）


```javascript
<div id="app">
  <p>{{ message }}</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-bd)


## unpkg（国内不稳定）


```javascript
<div id="app">
  <p>{{ message }}</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-hw)


## cdnjs


```javascript
<div id="app">
  <p>{{ message }}</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-hw-cdnjs)


我们可以使用 ES 模块构建版本来创建一个更现代化和模块化的开发环境：


## 实例


```javascript
<div id="app">{{ message }}</div>

<script type="module">
  import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

  createApp({
    data() {
      return {
        message: 'Hello RUNOOB!'
      }
    }
  }).mount('#app')
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue3-hw-es)


---


## 3、NPM 方法


由于 npm 安装速度慢，本教程使用了淘宝的镜像及其命令 cnpm，安装使用介绍参照：[使用淘宝 NPM 镜像](https://www.runoob.com/../nodejs/nodejs-npm.html)。


npm 版本需要大于 3.0，如果低于此版本需要升级它：


```
# 查看版本
$ npm -v
2.3.0

#升级 npm
cnpm install npm -g


# 升级或安装 cnpm
npm install cnpm -g
```


在用 Vue.js 构建大型应用时推荐使用 cnpm 安装，cnpm 能很好地和 Webpack 或 Browserify 模块打包器配合使用，然后在命令行中运行以下命令：


```
# 最新稳定版
$ npm init vue@latest
```


这一指令将会安装并执行 create-vue，它是 Vue 官方的项目脚手架工具。


```
$ npm init vue@latest
Need to install the following packages:
  [email protected]
Ok to proceed? (y) y

Vue.js - The Progressive JavaScript Framework
# 这里需要进行一些配置，项目名输入 runoob-vue3-test，其他默认回车即可
-> Project name: … runoob-vue3-test
-> Add TypeScript? … No / Yes
-> Add JSX Support? … No / Yes
-> Add Vue Router for Single Page Application development? … No / Yes
-> Add Pinia for state management? … No / Yes
-> Add Vitest for Unit Testing? … No / Yes
-> Add an End-to-End Testing Solution? › No
-> Add ESLint for code quality? … No / Yes

Scaffolding project in /Users/runoob/runoob-test/runoob-vue3/runoob-vue3-test...

Done. Now run:

  cd runoob-vue3-test
  npm install
  npm run dev
```


如果不确定是否要开启某个功能，你可以直接按下回车键选择 No。

在项目被创建后，通过以下步骤安装依赖并启动开发服务器：


```
$ cd runoob-vue3-test
$ npm install
$ npm run dev
  VITE v4.3.4  ready in 543 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```


成功执行以上命令后访问 **http://localhost:5173/**，输出结果如下所示：


![](https://www.runoob.com/wp-content/uploads/2021/02/5b157815f8fc1792384ff0a9dbc14e47.png)

**

注意：**Vue.js 不支持 IE8 及其以下 IE 版本。


---

## 使用图形化界面


我们可以通过 **vue ui** 命令来打开图形化界面创建和管理项目：


```
vue ui
```


执行以上命令会在浏览器中打开一个图形化界面来引导项目创建：


![](https://www.runoob.com/wp-content/uploads/2021/02/vue3-ui-scaled.jpeg)


---

## Vite


Vite 是一个 web 开发构建工具，由于其原生 ES 模块导入方式，可以实现闪电般的冷服务器启动。


通过在终端中运行以下命令，可以使用 Vite 快速构建 Vue 项目，语法格式如下：


```
npm init vite-app <project-name>
```


创建项目 runoob-vue3-test2：


```
$  npm init vite-app runoob-vue3-test2
```


运行项目:


```
$ cd runoob-vue3-test2
$ cnpm install
$ cnpm run dev
> [email protected] dev /Users/runoob/runoob-test/vue3/runoob-vue3-test2
> vite

[vite] Optimizable dependencies detected:
vue

  Dev server running at:
  > Local:    http://localhost:3000/
```


打开 **http://localhost:3000/**，显示如下：


![](https://www.runoob.com/wp-content/uploads/2021/02/62FB6F27-456F-46CF-8892-93D6A3E6F341.jpg)








	  AI 思考中...





			** [Vue3 教程](https://www.runoob.com/vue3-tutorial.html)
			[Vue3 目录结构](https://www.runoob.com/vue3-directory-structure.html) **













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