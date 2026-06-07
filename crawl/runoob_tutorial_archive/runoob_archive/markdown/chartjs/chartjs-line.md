# Chart.js 折线图

- Source: https://www.runoob.com/chartjs/chartjs-line.html

折线图是排列在工作表的列或行中的数据可以绘制到折线图中。

折线图可以显示随时间（根据常用比例设置）而变化的连续数据，因此非常适用于显示在相等时间间隔下数据的趋势。


折线图 **type** 属性为 **line** ，type 描述了图表类型。


```
const config = {
  type: 'line',
  data: data,
};
```


接下来我们创建一个简单的折线图：


## 实例


```javascript
const ctx = document.getElementById('myChart');
const labels = ['一月份', '二月份', '三月份','四月份', '五月份', '六月份', '七月份'];  // 设置 X 轴上对应的标签
const data = {
  labels: labels,
  datasets: [{
    label: '我的第一个折线图',
    data: [65, 59, 80, 81, 56, 55, 40],
    fill: false,
    borderColor: 'rgb(75, 192, 192)', // 设置线的颜色
    tension: 0.1
  }]
};
const config = {
  type: 'line', // 设置图表类型
  data: data,
};
const myChart = new Chart(ctx, config);
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trychartjs_line)

以上实例输出结果为：

*

接下来我们丰富一下折线图，添加选项，设置如下：


## 实例


```javascript
const ctx = document.getElementById('myChart');
const labels = ['一月份', '二月份', '三月份','四月份', '五月份', '六月份', '七月份'];  // 设置 X 轴上对应的标签
const data = {
  labels: labels,
  datasets: [{
    label: '我的第一个折线图',
    data: [65, 59, 80, 81, 56, 55, 40],
    fill: false,
    borderColor: 'rgb(75, 192, 192)', // 设置线的颜色
        backgroundColor: ['rgba(179, 0, 33, 0.5)'],// 设置点的填充色
        pointStyle: 'circle',     //设置点类型为圆点
    pointRadius: 6,    //设置圆点半径
    pointHoverRadius: 10, //设置鼠标移动上去后圆点半径
    tension: 0.1
  }]
};
const config = {
  type: 'line', // 设置图表类型
  data: data,
  options: {
    responsive: true,  // 设置图表为响应式

    interaction: {  // 设置每个点的交互
      intersect: false,
    },
    scales: {  // 设置 X 轴与 Y 轴
      x: {
        display: true,
        title: {
          display: true,
          text: '日期'
        }
      },
      y: {
        display: true,
        title: {
          display: true,
          text: '票数'
        }
      }
    }
  }
};
const myChart = new Chart(ctx, config);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trychartjs_line2)


以上实例输出结果为：


### 垂直折线图


垂直折线图是水平折线图的变体。

垂直折线图需要将选项对象中的 indexAxis 属性设置为 **y**，indexAxis 属性的默认值为 x**。


## 实例


```javascript
const ctx = document.getElementById('myChart');
const labels = ['一月份', '二月份', '三月份','四月份', '五月份', '六月份', '七月份'];  // 设置 X 轴上对应的标签
const data = {
  labels: labels,
  datasets: [{
    label: '我的第一个折线图',
    data: [65, 59, 80, 81, 56, 55, 40],
    fill: false,
    borderColor: 'rgb(75, 192, 192)', // 设置线的颜色
        backgroundColor: ['rgba(179, 0, 33, 0.5)'],// 设置点的填充色
        pointStyle: 'circle',     //设置点类型为圆点
    pointRadius: 6,    //设置圆点半径
    pointHoverRadius: 10, //设置鼠标移动上去后圆点半径
    tension: 0.1
  }]
};
const config = {
  type: 'line', // 设置图表类型
  data: data,
  options: {
    indexAxis: 'y', // 设置垂直折线图
    responsive: true,  // 设置图表为响应式

    interaction: {  // 设置每个点的交互
      intersect: false,
    },
    scales: {  // 设置 X 轴与 Y 轴
      x: {
                beginAtZero: true,// 设置 X 轴从 0 开始
        display: true,
        title: {
          display: true,
          text: '日期'
        }
      },
      y: {
        display: true,
        title: {
          display: true,
          text: '票数'
        }
      }
    }
  }
};
const myChart = new Chart(ctx, config);
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trychartjs_line3)

以上实例输出结果为：









	  AI 思考中...





			* [Chart.js 饼图](https://www.runoob.com/chartjs-pie.html)
			[Chart.js 混合图](https://www.runoob.com/chartjs-scatter.html) **













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