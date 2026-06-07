# Chart.js 环形图

- Source: https://www.runoob.com/chartjs/chartjs-doughnut.html

环形图又叫做甜甜圈图，其本质是饼图将中间区域挖空。

环形图是由两个及两个以上大小不一的饼图叠在一起，挖去中间的部分所构成的图形。


- 饼图是用圆形及圆内扇形的角度来表示数值大小的图形，它主要用于表示一个样本（或总体）中各组成部分的数据占全部数据的比例，对于研究结构性问题十分有用。 环形图与饼图类似，但又有区别。环形图中间有一个"空洞"，每个样本用一个环来表示，样本中的每一部分数据用环中的一段表示。因此环形图可显示多个样本各部分所占的相应比例，从而有利于构成的比较研究。


环形图 **type** 属性为 **doughnut** ，type 描述了图表类型。


```
const config = {
  type: 'doughnut',
  data: data,
};
```


接下来我们创建一个简单的环形图：


## 实例


```javascript
const ctx = document.getElementById('myChart');
const data = {
  labels: [
    'Red',
    'Blue',
    'Yellow'
  ],
  datasets: [{
    label: '环形图实例',
    data: [300, 50, 100],
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
    hoverOffset: 4
  }]
};
const config = {
  type: 'doughnut',
  data: data,
  options: {
    responsive: true, // 设置图表为响应式，根据屏幕窗口变化而变化
    maintainAspectRatio: false,// 保持图表原有比例
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero:true
                }
          }]
    }
  }
};
const myChart = new Chart(ctx, config);
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trychartjs_doughnut)


以上实例输出结果为：

*







	  AI 思考中...





			* [Chart.js 气泡图](https://www.runoob.com/chartjs-bubble.html)
			[Chart.js 饼图](https://www.runoob.com/chartjs-pie.html) **













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