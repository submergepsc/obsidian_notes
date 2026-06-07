# ECharts 事件处理

- Source: https://www.runoob.com/echarts/echarts-events.html

ECharts 中我们可以通过监听用户的操作行为来回调对应的函数。


ECharts 通过 **on** 方法来监听用户的行为，例如监控用户的点击行为。


ECharts 中事件分为两种类型:


用户鼠标操作点击，如 **'click'、'dblclick'、'mousedown'、'mousemove'、'mouseup'、'mouseover'、'mouseout'、'globalout'、'contextmenu'** 事件。


还有一种是用户在使用可以交互的组件后触发的行为事件，例如在切换图例开关时触发的 'legendselectchanged' 事件），数据区域缩放时触发的 'datazoom' 事件等等。


```
myChart.on('click', function (params) {
    // 在用户点击后控制台打印数据的名称
    console.log(params);
});

myChart.on('legendselectchanged', function (params) {
    console.log(params);
});

chart.on('click', 'series.line', function (params) {
    console.log(params);
});

chart.on('mouseover', {seriesIndex: 1, name: 'xx'}, function (params) {
    console.log(params);
});
```


---


## 鼠标事件


ECharts 支持的鼠标事件类型，包括 'click'、'dblclick'、'mousedown'、'mousemove'、'mouseup'、'mouseover'、'mouseout'、'globalout'、'contextmenu' 事件。


以下实例在点击柱形图时会弹出对话框：


## 实例


```javascript
// 基于准备好的dom，初始化ECharts实例
var myChart = echarts.init(document.getElementById('main'));

// 指定图表的配置项和数据
var option = {
    xAxis: {
        data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);
// 处理点击事件并且弹出数据名称
myChart.on('click', function (params) {
    alert(params.name);
});
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_event1)


所有的鼠标事件包含参数 params，这是一个包含点击图形的数据信息的对象，格式如下：


```
{
    // 当前点击的图形元素所属的组件名称，
    // 其值如 'series'、'markLine'、'markPoint'、'timeLine' 等。
    componentType: string,
    // 系列类型。值可能为：'line'、'bar'、'pie' 等。当 componentType 为 'series' 时有意义。
    seriesType: string,
    // 系列在传入的 option.series 中的 index。当 componentType 为 'series' 时有意义。
    seriesIndex: number,
    // 系列名称。当 componentType 为 'series' 时有意义。
    seriesName: string,
    // 数据名，类目名
    name: string,
    // 数据在传入的 data 数组中的 index
    dataIndex: number,
    // 传入的原始数据项
    data: Object,
    // sankey、graph 等图表同时含有 nodeData 和 edgeData 两种 data，
    // dataType 的值会是 'node' 或者 'edge'，表示当前点击在 node 还是 edge 上。
    // 其他大部分图表中只有一种 data，dataType 无意义。
    dataType: string,
    // 传入的数据值
    value: number|Array
    // 数据图形的颜色。当 componentType 为 'series' 时有意义。
    color: string
}
```


如何区分鼠标点击到了哪里：


```
myChart.on('click', function (params) {
    if (params.componentType === 'markPoint') {
        // 点击到了 markPoint 上
        if (params.seriesIndex === 5) {
            // 点击到了 index 为 5 的 series 的 markPoint 上。
        }
    }
    else if (params.componentType === 'series') {
        if (params.seriesType === 'graph') {
            if (params.dataType === 'edge') {
                // 点击到了 graph 的 edge（边）上。
            }
            else {
                // 点击到了 graph 的 node（节点）上。
            }
        }
    }
});
```


使用 query 只对指定的组件的图形元素的触发回调：


```
chart.on(eventName, query, handler);
```


query 可为 string 或者 Object。


如果为 string 表示组件类型。格式可以是 'mainType' 或者 'mainType.subType'。例如：


```
chart.on('click', 'series', function () {...});
chart.on('click', 'series.line', function () {...});
chart.on('click', 'dataZoom', function () {...});
chart.on('click', 'xAxis.category', function () {...});
```


如果为 Object，可以包含以下一个或多个属性，每个属性都是可选的：


```
{
    <mainType>Index: number // 组件 index
    <mainType>Name: string // 组件 name
    <mainType>Id: string // 组件 id
    dataIndex: number // 数据项 index
    name: string // 数据项 name
    dataType: string // 数据项 type，如关系图中的 'node', 'edge'
    element: string // 自定义系列中的 el 的 name
}
```


例如：


```
chart.setOption({
    // ...
    series: [{
        name: 'uuu'
        // ...
    }]
});
chart.on('mouseover', {seriesName: 'uuu'}, function () {
    // series name 为 'uuu' 的系列中的图形元素被 'mouseover' 时，此方法被回调。
});
```


例如：


```
chart.setOption({
    // ...
    series: [{
        // ...
    }, {
        // ...
        data: [
            {name: 'xx', value: 121},
            {name: 'yy', value: 33}
        ]
    }]
});
chart.on('mouseover', {seriesIndex: 1, name: 'xx'}, function () {
    // series index 1 的系列中的 name 为 'xx' 的元素被 'mouseover' 时，此方法被回调。
});
```


例如：


```
chart.setOption({
    // ...
    series: [{
        type: 'graph',
        nodes: [{name: 'a', value: 10}, {name: 'b', value: 20}],
        edges: [{source: 0, target: 1}]
    }]
});
chart.on('click', {dataType: 'node'}, function () {
    // 关系图的节点被点击时此方法被回调。
});
chart.on('click', {dataType: 'edge'}, function () {
    // 关系图的边被点击时此方法被回调。
});
```


例如：


```
chart.setOption({
    // ...
    series: {
        // ...
        type: 'custom',
        renderItem: function (params, api) {
            return {
                type: 'group',
                children: [{
                    type: 'circle',
                    name: 'my_el',
                    // ...
                }, {
                    // ...
                }]
            }
        },
        data: [[12, 33]]
    }
})
chart.on('mouseup', {element: 'my_el'}, function () {
    // name 为 'my_el' 的元素被 'mouseup' 时，此方法被回调。
});
```


你可以在回调函数中获得这个对象中的数据名、系列名称后在自己的数据仓库中索引得到其它的信息候更新图表，显示浮层等等，如下示例代码：


## 实例


```javascript
myChart.on('click', function (parmas) {
    $.get('detail?q=' + params.name, function (detail) {
        myChart.setOption({
            series: [{
                name: 'pie',
                // 通过饼图表现单个柱子中的数据分布
                data: [detail.data]
            }]
        });
    });
});
```


---


## 组件交互的行为事件


在 ECharts 中基本上所有的组件交互行为都会触发相应的事件，常用的事件和事件对应参数在 events 文档中有列出。


下面是监听一个图例开关的示例：


## 实例


```javascript
// 图例开关的行为只会触发 legendselectchanged 事件
myChart.on('legendselectchanged', function (params) {
    // 获取点击图例的选中状态
    var isSelected = params.selected[params.name];
    // 在控制台中打印
    console.log((isSelected ? '选中了' : '取消选中了') + '图例' + params.name);
    // 打印所有图例的状态
    console.log(params.selected);
});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_event1)


---


## 代码触发 ECharts 中组件的行为


上面我们只说明了用户的交互操作，但有时候我们也会需要在程序里调用方法并触发图表的行为，比如显示 tooltip。


ECharts 通过 dispatchAction({ type: '' }) 来触发图表行为，统一管理了所有动作，也可以根据需要去记录用户的行为路径。


以上实例用于轮播饼图中的 tooltip：


## 实例


```javascript
setInterval(function () {
    var dataLen = option.series[0].data.length;
    // 取消之前高亮的图形
    myChart.dispatchAction({
        type: 'downplay',
        seriesIndex: 0,
        dataIndex: app.currentIndex
    });
    app.currentIndex = (app.currentIndex + 1) % dataLen;
    // 高亮当前图形
    myChart.dispatchAction({
        type: 'highlight',
        seriesIndex: 0,
        dataIndex: app.currentIndex
    });
    // 显示 tooltip
    myChart.dispatchAction({
        type: 'showTip',
        seriesIndex: 0,
        dataIndex: app.currentIndex
    });
}, 1000);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_event3)







	  AI 思考中...





			** [ECharts 数据的视觉映射](https://www.runoob.com/echarts-visualmap.html)
			[ECharts 旭日图](https://www.runoob.com/echarts-sunburst.html) **













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