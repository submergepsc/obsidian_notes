# ECharts 安装

- Source: https://www.runoob.com/echarts/echarts-install.html

## 1、独立版本


我们可以在直接下载 echarts.min.js 并用 **** 标签引入。


[echarts.min.js(4.7.0)](https://cdn.staticfile.net/echarts/4.7.0/echarts.min.js)


另外，开发环境下可以使用源代码版本 echarts.js 并用 **** 标签引入，源码版本包含了常见的错误提示和警告。


[echarts.js(4.7.0)](https://cdn.staticfile.net/echarts/4.7.0/echarts.js) 我们也可以在 ECharts 的官网上直接下载更多丰富的版本，包含了不同主题跟语言，下载地址：[https://echarts.apache.org/zh/download.html](https://echarts.apache.org/zh/download.html)。


这些构建好的 echarts 提供了下面这几种定制：


- 完全版：`echarts/dist/echarts.js`，体积最大，包含所有的图表和组件，所包含内容参见：`echarts/echarts.all.js`。
- 常用版：`echarts/dist/echarts.common.js`，体积适中，包含常见的图表和组件，所包含内容参见：`echarts/echarts.common.js`。
- 精简版：`echarts/dist/echarts.simple.js`，体积较小，仅包含最常用的图表和组件，所包含内容参见：`echarts/echarts.simple.js`。


---


## 2、使用 CDN 方法


以下推荐国外比较稳定的两个 CDN，国内还没发现哪一家比较好，目前还是建议下载到本地。


- **Staticfile CDN（国内）** : [https://cdn.staticfile.net/echarts/4.3.0/echarts.min.js](https://cdn.staticfile.net/echarts/4.3.0/echarts.min.js)
- **jsDelivr**：[https://cdn.jsdelivr.net/npm/[email protected]/dist/echarts.min.js](https://cdn.jsdelivr.net/npm/echarts@4.3.0/dist/echarts.min.js)。
- **cdnjs** : [https://cdnjs.cloudflare.com/ajax/libs/echarts/4.3.0/echarts.min.js](https://cdnjs.cloudflare.com/ajax/libs/echarts/4.3.0/echarts.min.js)


## Staticfile CDN（国内）


```javascript
<!-- 为ECharts准备一个具备大小（宽高）的Dom -->
<div id="main" style="width: 600px;height:400px;"></div>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_intro)


## jsDelivr


```javascript
<!-- 为ECharts准备一个具备大小（宽高）的Dom -->
<div id="main" style="width: 600px;height:400px;"></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_intro_baidu)


## cdnjs


```javascript
<!-- 为ECharts准备一个具备大小（宽高）的Dom -->
<div id="main" style="width: 600px;height:400px;"></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_intro_cdnjs)


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


通过 cnpm 获取 echarts：


```
# 最新稳定版
$ cnpm install echarts --save
```


安装完成后 ECharts 和 zrender 会放在 node_modules 目录下，我们可以直接在项目代码中使用 **require('echarts')** 来使用。


## 实例


```javascript
var echarts = require('echarts');

// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('main'));
// 绘制图表
myChart.setOption({
    title: {
        text: 'ECharts 入门示例'
    },
    tooltip: {},
    xAxis: {
        data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
});
```










	  AI 思考中...





			** [ECharts 教程](https://www.runoob.com/echarts-tutorial.html)
			[ECharts 配置语法](https://www.runoob.com/echarts-setup.html) **













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