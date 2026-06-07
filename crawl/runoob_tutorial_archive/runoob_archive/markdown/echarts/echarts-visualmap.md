# ECharts 数据的视觉映射

- Source: https://www.runoob.com/echarts/echarts-visualmap.html

数据可视化简单来讲就是将数据用图表的形式来展示，专业的表达方式就是数据到视觉元素的映射过程。


ECharts 的每种图表本身就内置了这种映射过程，我们之前学习到的柱形图就是将数据映射到长度。


此外，ECharts 还提供了 visualMap 组件 来提供通用的视觉映射。visualMap 组件中可以使用的视觉元素有：


- 图形类别（symbol）
- 图形大小（symbolSize）
- 颜色（color）
- 透明度（opacity）
- 颜色透明度（colorAlpha）
- 颜色明暗度（colorLightness）
- 颜色饱和度（colorSaturation）
- 色调（colorHue）


---


## 数据和维度


ECharts 中的数据，一般存放于 **series.data** 中。


不同的图表类型，数据格式有所不一样，但是他们的共同特点就都是数据项（dataItem） 的集合。每个数据项含有 数据值（value） 和其他信息（可选）。每个数据值，可以是单一的数值（一维）或者一个数组（多维）。


series.data 最常见的形式 是线性表，即一个普通数组：


```javascript
series: {
    data: [
        {       // 这里每一个项就是数据项（dataItem）
            value: 2323, // 这是数据项的数据值（value）
            itemStyle: {...}
        },
        1212,   // 也可以直接是 dataItem 的 value，这更常见。
        2323,   // 每个 value 都是『一维』的。
        4343,
        3434
    ]
}
series: {
    data: [
        {                        // 这里每一个项就是数据项（dataItem）
            value: [3434, 129,  '圣马力诺'], // 这是数据项的数据值（value）
            itemStyle: {...}
        },
        [1212, 5454, '梵蒂冈'],   // 也可以直接是 dataItem 的 value，这更常见。
        [2323, 3223, '瑙鲁'],     // 每个 value 都是『三维』的，每列是一个维度。
        [4343, 23,   '图瓦卢']    // 假如是『气泡图』，常见第一维度映射到x轴，
                                 // 第二维度映射到y轴，
                                 // 第三维度映射到气泡半径（symbolSize）
    ]
}
```


在图表中，往往默认把 value 的前一两个维度进行映射，比如取第一个维度映射到x轴，取第二个维度映射到y轴。如果想要把更多的维度展现出来，可以借助 visualMap 。


---


## visualMap 组件


visualMap 组件定义了把数据的指定维度映射到对应的视觉元素上。


visualMap 组件可以定义多个，从而可以同时对数据中的多个维度进行视觉映射。


visualMap 组件可以定义为 分段型（visualMapPiecewise） 或 连续型（visualMapContinuous），通过 type 来区分。例如：


```javascript
option = {
    visualMap: [
        { // 第一个 visualMap 组件
            type: 'continuous', // 定义为连续型 visualMap
            ...
        },
        { // 第二个 visualMap 组件
            type: 'piecewise', // 定义为分段型 visualMap
            ...
        }
    ],
    ...
};
```


分段型视觉映射组件，有三种模式：


- 连续型数据平均分段: 依据 visualMap-piecewise.splitNumber 来自动平均分割成若干块。
- 连续型数据自定义分段: 依据 visualMap-piecewise.pieces 来定义每块范围。
- 离散数据根据类别分段: 类别定义在 visualMap-piecewise.categories 中。


分段型视觉映射组件，展现形式如下图：


## 实例


```javascript

```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryecharts_visualmap)


---


## 视觉映射方式的配置


visualMap 中可以指定数据的指定维度映射到对应的视觉元素上。


## 实例 1


```javascript
option = {
    visualMap: [
        {
            type: 'piecewise'
            min: 0,
            max: 5000,
            dimension: 3,       // series.data 的第四个维度（即 value[3]）被映射
            seriesIndex: 4,     // 对第四个系列进行映射。
            inRange: {          // 选中范围中的视觉配置
                color: ['blue', '#121122', 'red'], // 定义了图形颜色映射的颜色列表，
                                                    // 数据最小值映射到'blue'上，
                                                    // 最大值映射到'red'上，
                                                    // 其余自动线性计算。
                symbolSize: [30, 100]               // 定义了图形尺寸的映射范围，
                                                    // 数据最小值映射到30上，
                                                    // 最大值映射到100上，
                                                    // 其余自动线性计算。
            },
            outOfRange: {       // 选中范围外的视觉配置
                symbolSize: [30, 100]
            }
        },
        ...
    ]
};
```


## 实例 2


```javascript
option = {
    visualMap: [
        {
            ...,
            inRange: {          // 选中范围中的视觉配置
                colorLightness: [0.2, 1], // 映射到明暗度上。也就是对本来的颜色进行明暗度处理。
                                          // 本来的颜色可能是从全局色板中选取的颜色，visualMap组件并不关心。
                symbolSize: [30, 100]
            },
            ...
        },
        ...
    ]
};
```


更多详情，参见 [visualMap.inRange](https://www.echartsjs.com/zh/option.html#visualMap-continuous.inRange) 和 [visualMap.outOfRange](https://www.echartsjs.com/zh/option.html#visualMap-continuous.outOfRange)。








	  AI 思考中...





			** [ECharts 响应式](https://www.runoob.com/echarts-mediaqueries.html)
			[ECharts 事件处理](https://www.runoob.com/echarts-events.html) **













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