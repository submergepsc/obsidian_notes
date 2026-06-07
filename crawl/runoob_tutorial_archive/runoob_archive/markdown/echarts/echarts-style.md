# ECharts 样式设置

- Source: https://www.runoob.com/echarts/echarts-style.html

ECharts 可以通过样式设置来改变图形元素或者文字的颜色、明暗、大小等。


---


## 颜色主题


ECharts4 开始，除了默认主题外，内置了两套主题，分别为 **light** 和 **dark**。


使用方式如下：


## 实例


```javascript
var chart = echarts.init(dom, 'light');

或者

var chart = echarts.init(dom, 'dark');
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_pie1_light)


另外，我们也可以在官方的 [主题编辑器](http://echarts.baidu.com/theme-builder/) 选择自己喜欢的主题下载。


[![](https://www.runoob.com/wp-content/uploads/2019/11/CC43DF51-2C46-4AB1-B256-7823D0027379.jpg)](https://www.runoob.com/wp-content/uploads/2019/11/CC43DF51-2C46-4AB1-B256-7823D0027379.jpg)


目前主题下载提供了 JS 版本和 JSON 版本。


如果你使用 JS 版本，可以将 JS 主题代码保存一个 **主题名.js** 文件，然后在 HTML 中引用该文件，最后在代码中使用该主题。


比如上图中我们选中了一个主题，将 JS 代码保存为 wonderland.js**。


## 实例


```javascript
<!-- 引入主题 -->
<script src="https://www.runoob.com/static/js/wonderland.js"></script>
...

// HTML 引入 wonderland.js 文件后，在初始化的时候调用
var myChart = echarts.init(dom, 'wonderland');
// ...
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_pie1_wonderland_js)


如果主题保存为 JSON 文件，那么可以自行加载和注册。


比如上图中我们选中了一个主题，将 JSON 代码保存为 wonderland.json**。


## 实例


```javascript
//主题名称是 wonderland
$.getJSON('wonderland.json', function (themeJSON) {
    echarts.registerTheme('wonderland', themeJSON)
    var myChart = echarts.init(dom, 'wonderland');
});
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_pie1_wonderland_json)

注意：**我们使用了 $.getJSON，所以需要引入 jQuery。


---


## 调色盘


调色盘可以在 option 中设置。


调色盘给定了一组颜色，图形、系列会自动从其中选择颜色。


可以设置全局的调色盘，也可以设置系列自己专属的调色盘。


```javascript
option = {
    // 全局调色盘。
    color: ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3'],

    series: [{
        type: 'bar',
        // 此系列自己的调色盘。
        color: ['#dd6b66','#759aa0','#e69d87','#8dc1a9','#ea7e53','#eedd78','#73a373','#73b9bc','#7289ab', '#91ca8c','#f49f42'],
        ...
    }, {
        type: 'pie',
        // 此系列自己的调色盘。
        color: ['#37A2DA', '#32C5E9', '#67E0E3', '#9FE6B8', '#FFDB5C','#ff9f7f', '#fb7293', '#E062AE', '#E690D1', '#e7bcf3', '#9d96f5', '#8378EA', '#96BFFF'],
        ...
    }]
}
```


全局调色盘实例：


## 实例


```javascript
// 全局调色盘。
color: ['#ff0000','#00ff00', '#0000ff', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3'],
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_pie1_color2)


系列调色盘实例：


## 实例


```javascript
series: [{
    type: 'pie',
    // 此系列自己的调色盘。
    color: ['#ff0000','#00ff00', '#0000ff', '#9FE6B8', '#FFDB5C','#ff9f7f', '#fb7293', '#E062AE', '#E690D1', '#e7bcf3', '#9d96f5', '#8378EA', '#96BFFF'],
    ...
}]
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_pie1_color1)


---


## 直接的样式设置 itemStyle, lineStyle, areaStyle, label, ...


直接的样式设置是比较常用设置方式。纵观 ECharts 的 [option](https://www.echartsjs.com/zh/option.html#title) 中，很多地方可以设置 [itemStyle](https://www.echartsjs.com/zh/option.html#series.itemStyle)、[lineStyle](https://www.echartsjs.com/zh/option.html#series-line.lineStyle)、[areaStyle](https://www.echartsjs.com/zh/option.html#series-line.areaStyle)、[label](https://www.echartsjs.com/zh/option.html#series.label) 等等。这些的地方可以直接设置图形元素的颜色、线宽、点的大小、标签的文字、标签的样式等等。


一般来说，ECharts 的各个系列和组件，都遵从这些命名习惯，虽然不同图表和组件中，`itemStyle`、`label` 等可能出现在不同的地方。


直接样式设置的另一篇介绍，参见 [ECharts 饼图](https://www.runoob.com/echarts-pie.html)。


---


## 高亮的样式：emphasis


在鼠标悬浮到图形元素上时，一般会出现高亮的样式。默认情况下，高亮的样式是根据普通样式自动生成的。


如果要自定义高亮样式可以通过 emphasis 属性来定制：


## 实例


```javascript
// 高亮样式。
emphasis: {
    itemStyle: {
        // 高亮时点的颜色
        color: 'red'
    },
    label: {
        show: true,
        // 高亮时标签的文字
        formatter: '高亮时显示的标签内容'
    }
},
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_pie1_emphasis)








	  AI 思考中...





			** [ECharts 饼图](https://www.runoob.com/echarts-pie.html)
			[ECharts 异步加载数据](https://www.runoob.com/echarts-ajax-data.html) **













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