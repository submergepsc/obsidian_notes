# Chart.js 混合图

- Source: https://www.runoob.com/chartjs/chartjs-scatter.html

Chart.js 可以创建由两种或多种不同图表类型组合而成的混合图表，比如条形图与折线图的混合。


创建混合图表时，我们在每个数据集上指定图表类型。


混合图 **type** 属性为 **scatter**。


柱形图 **type** 属性为 **bar** ，折线图 **type** 属性为 **line** ， type 描述了图表类型。


```
const mixedChart = new Chart(ctx, {
    data: {
        datasets: [{
            type: 'bar',
            label: '柱形图数据集',
            data: [45, 49,52, 48]
        }, {
            type: 'line',
            label: '折线图数据集',
            data: [50, 40, 45, 49],
        }],
        labels: ['一月份', '二月份', '三月份', '四月份']
    },
    options: options
});
```


接下来我们创建一个简单的混合图：


## 实例


```javascript
const ctx = document.getElementById('myChart');
const data = {
  labels: [
    '一月份',
    '二月份',
    '三月份',
    '四月份'
  ],
  datasets: [{
    type: 'bar',
    label: '柱形图数据集',
    data: [45, 49,52, 48],
    borderColor: 'rgb(255, 99, 132)',
    backgroundColor: 'rgba(255, 99, 132, 0.2)'
  }, {
    type: 'line',
    label: '折线图数据集',
    data: [50, 40, 45, 49],
    fill: false,
    borderColor: 'rgb(54, 162, 235)'
  }]
};
const config = {
  type: 'scatter',
  data: data,
  options: {
    responsive: true, // 设置图表为响应式，根据屏幕窗口变化而变化
    maintainAspectRatio: false,// 保持图表原有比例
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
};
const myChart = new Chart(ctx, config);
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trychartjs_scatter)


以上实例输出结果为：

*







	  AI 思考中...





			* [Chart.js 折线图](https://www.runoob.com/chartjs-line.html)
			[Chart.js 极地图](https://www.runoob.com/chartjs-polararea.html) **













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