# Chart.js 柱形图

- Source: https://www.runoob.com/chartjs/chartjs-type-bar.html

柱形图是一种以长方形的长度为变量的统计图表。

柱形图用来比较两个或以上的价值（不同时间或者不同条件），只有一个变量，通常利用于较小的数据集分析。


柱形图的 **type** 属性为 **bar** ，type 描述了图表类型。


```
const config = {
  type: 'bar',
  data: data,
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  },
};
```


接下来我们创建一个简单的柱形图：


## 实例


```javascript
const ctx = document.getElementById('myChart');
const labels = ['一月份', '二月份', '三月份','四月份', '五月份', '六月份', '七月份'];  // 设置 X 轴上对应的标签
const data = {
  labels: labels,
  datasets: [{
    label: '我的第一个柱形图',
    data: [65, 59, 80, 81, 56, 55, 40],
    backgroundColor: [      // 设置每个柱形图的背景颜色
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)'
    ],
    borderColor: [     //设置每个柱形图边框线条颜色
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgb(201, 203, 207)'
    ],
    borderWidth: 1     // 设置线条宽度
  }]
};
const config = {
  type: 'bar', // 设置图表类型
  data: data,  // 设置数据集
  options: {
    scales: {
      y: {
        beginAtZero: true // 设置 y 轴从 0 开始
      }
    }
  },
};
const myChart = new Chart(ctx, config);
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trychartjs_bar)


以上实例输出结果为：

*

### 水平柱形图


水平柱形图是垂直条形图的变，常用于显示数据趋势，以及并排比较多个数据集。

设置水平柱形图需要将选项对象中的 indexAxis 属性设置为 **y**，indexAxis 属性的默认值为 **x**。


## 实例


```javascript
const ctx = document.getElementById('myChart');
const labels = ['一月份', '二月份', '三月份','四月份', '五月份', '六月份', '七月份'];  // 设置 X 轴上对应的标签
const data = {
  labels: labels,
  datasets: [{
    axis: 'y',
    label: '我的第一个柱形图',
    data: [65, 59, 80, 81, 56, 55, 40],
    fill: false,
    backgroundColor: [      // 设置每个柱形图的背景颜色
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)'
    ],
    borderColor: [     //设置每个柱形图边框线条颜色
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgb(201, 203, 207)'
    ],
    borderWidth: 1     // 设置线条宽度
  }]
};
const config = {
  type: 'bar', // 设置图表类型
  data: data,  // 设置数据集
  options: {
    indexAxis: 'y',
  }
};
const myChart = new Chart(ctx, config);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trychartjs_bar2)

以上实例输出结果为：









	  AI 思考中...





			* [Chart.js 使用](https://www.runoob.com/chartjs-usage.html)
			[Chart.js 气泡图](https://www.runoob.com/chartjs-bubble.html) **













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