# Chart.js 使用

- Source: https://www.runoob.com/chartjs/chartjs-usage.html

使用 Chart.js 创建图表，需要初始化 Chart 类，并传入图表节点：


HTML Canvas 代码，图表显示位置：


```javascript
<canvas id="myChart" width="400" height="400"></canvas>
```




通过不同方式获取节点：


## 初始化方式


```javascript
//以下方式都可以
const ctx = document.getElementById('myChart');  // 获取节点
const ctx = document.getElementById('myChart').getContext('2d');  // getContext() 方法返回 canvas 的上下文
const ctx = $('#myChart'); // jQuery 获取
const ctx = 'myChart'; // 传入节点 ID
```


通过以上代码获得元素节点后，我们就可以创建自己的图表类型了。


以下实例我们创建一个简单的折线图：


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

以下实例创建一个柱形图，显示不同颜色的票数。


## 实例


```javascript
const ctx = document.getElementById('myChart');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# 票数',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trychartjs_intro)

以上实例输出结果为：


---

## 配置对象结构


配置对象常用结构如下：


```javascript
const config = {
  type: 'line'
  data: {}
  options: {}
  plugins: []
}
```


参数说明：**


- **type** -- 指定图表的类型
- **data** -- 图表中展示的数据集
- **options** -- 一些可选项配置，不同类型图表有不同配置
- **plugins** -- 插件










	  AI 思考中...





			* [Chart.js 安装](https://www.runoob.com/chartjs-install.html)
			[Chart.js 柱形图](https://www.runoob.com/chartjs-type-bar.html) **













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