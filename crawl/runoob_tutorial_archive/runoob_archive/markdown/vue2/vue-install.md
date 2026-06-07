# Vue.js 安装

- Source: https://www.runoob.com/vue2/vue-install.html

## 1、独立版本


我们可以在 Vue.js 的官网上直接下载 vue.min.js 并用 **** 标签引入。


[下载 Vue.js](https://v2.vuejs.org/js/vue.min.js)


---


## 2、使用 CDN 方法


以下推荐国外比较稳定的两个 CDN，国内还没发现哪一家比较好，目前还是建议下载到本地。


- **cdnjs** : [https://cdnjs.cloudflare.com/ajax/libs/vue/2.1.8/vue.min.js](https://cdnjs.cloudflare.com/ajax/libs/vue/2.1.8/vue.min.js)
- **Staticfile CDN（国内）** : [https://cdn.staticfile.net/vue/2.2.2/vue.min.js](https://cdn.staticfile.net/vue/2.2.2/vue.min.js)
- **unpkg**：[https://unpkg.com/[email protected]/dist/vue.min.js](https://unpkg.com/vue@2.6.14/dist/vue.min.js)。


## 字节跳动 CDN（国内）


```javascript
<div id="app">
  <p>{{ message }}</p>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-bc)


## unpkg（推荐）


```javascript
<div id="app">
  <p>{{ message }}</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-hw)


## cdnjs


```javascript
<div id="app">
  <p>{{ message }}</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vue2-hw-cdnjs)


--- ## 3、NPM 方法 由于 npm 安装速度慢，本教程使用了淘宝的镜像及其命令 cnpm，安装使用介绍参照：[使用淘宝 NPM 镜像](https://www.runoob.com/../nodejs/nodejs-npm.html)。


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


在用 Vue.js 构建大型应用时推荐使用 cnpm 安装：


```
# 最新稳定版
$ cnpm install vue
```


---


## 命令行工具


Vue.js 提供一个官方命令行工具，可用于快速搭建大型单页应用。


```
# 全局安装 vue-cli
$ cnpm install --global vue-cli
# 创建一个基于 webpack 模板的新项目
$ vue init webpack my-project
# 这里需要进行一些配置，默认回车即可
This will install Vue 2.x version of the template.

For Vue 1.x use: vue init webpack#1.0 my-project

? Project name my-project
? Project description A Vue.js project
? Author runoob <[email protected]>
? Vue build standalone
? Use ESLint to lint your code? Yes
? Pick an ESLint preset Standard
? Setup unit tests with Karma + Mocha? Yes
? Setup e2e tests with Nightwatch? Yes

   vue-cli · Generated "my-project".

   To get started:

     cd my-project
     npm install
     npm run dev

   Documentation can be found at https://vuejs-templates.github.io/webpack
```


进入项目，安装并运行：
```
$ cd my-project
$ cnpm install
$ cnpm run dev
 DONE  Compiled successfully in 4388ms

> Listening at http://localhost:8080
```
 成功执行以上命令后访问 http://localhost:8080/，输出结果如下所示：


![](https://www.runoob.com/wp-content/uploads/2017/01/56219E04-D156-43EC-AC59-BFE7E38A62C3.jpg)


> 注意：**Vue.js 不支持 IE8 及其以下 IE 版本。


---


## Vue 项目打包


打包 Vue 项目使用以下命令：


```
npm run build
```


执行完成后，会在 Vue 项目下生成一个 **dist** 目录，一般包含 index.html 文件及 static 目录，static 目录包含了静态文件 js、css 以及图片目录 images。


![](https://www.runoob.com/wp-content/uploads/2017/01/BEE1DA18-407F-4979-9DFD-D61FB77E2671.jpg)


如果直接双击 index.html 打开浏览器，页面可能是空白了，想要正常显示，可以修改 index.html 文件中 js、css 文件的路径。

例如我们打开 dist/index.html 文件看到路径是绝对路径：


```
<link href=/static/css/app.33da80d69744798940b135da93bc7b98.css rel=stylesheet>
<script type=text/javascript src=/static/js/app.717bb358ddc19e181140.js></script>
```


我们把 js、css 路径修改为相对路径：


```
<link href=static/css/app.33da80d69744798940b135da93bc7b98.css rel=stylesheet>
<script type=text/javascript src=static/js/app.717bb358ddc19e181140.js></script>
```


这样直接双击 dist/index.html 文件就可以在浏览器中看到效果了。


---


## 编辑器


### VS Code

VS Code（全称 Visual Studio Code）是一款由微软推出的免费、开源、跨平台的代码编辑器。

VS Code 支持 Windows、macOS 和 Linux，拥有强大的功能和灵活的扩展性。

VS Code 教程：[https://www.runoob.com/vscode/vscode-tutorial.html](https://www.runoob.com/../vscode/vscode-tutorial.html)


**

另外国内阿里与字节也有基于 VS Code 开发的 AI IDE：


- **阿里 Qoder：**[https://qoder.com/](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)
- **字节 Trae：**[https://www.trae.com.cn/](https://www.trae.com.cn/?utm_source=advertising&utm_medium=runoob_ug_cpa&utm_term=hw_trae_runoob)


![](https://www.runoob.com/wp-content/uploads/2024/12/vs-code_background.png)








	  AI 思考中...





			** [Vue.js 教程](https://www.runoob.com/vue-tutorial.html)
			[Vue.js 模板语法](https://www.runoob.com/vue-template-syntax.html) **













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