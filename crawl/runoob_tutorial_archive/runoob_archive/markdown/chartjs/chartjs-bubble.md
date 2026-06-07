# Chart.js 气泡图

- Source: https://www.runoob.com/chartjs/chartjs-bubble.html

气泡图用于展示三个变量之间的关系。

气泡的位置由前两个变量决定，对应的是 X 轴和 Y 轴，第三个参数为气泡的大小。


```
{
    // X 轴对应值
    x: number,

    // Y 轴对应值
    y: number,

    // 气泡半径，单位为像素
    r: number
}
```


泡图的 **type** 属性为 **bubble** ，type 描述了图表类型。


```
const config = {
  type: 'bubble',
  data: data,
  options: {}
};
```


接下来我们创建一个简单的气泡图：


## 实例


```javascript
const ctx = document.getElementById('myChart');
const data = {
  datasets: [{
    label: '气泡图实例',
    data: [{
      x: 20, // X 轴
      y: 30, // Y 轴
      r: 15   // 气泡半径
    }, {
      x: 30,
      y: 20,
      r: 20
    }, {
      x: 40,
      y: 10,
      r: 10
    }],
    backgroundColor: 'rgb(255, 99, 132)'
  }]
};
const config = {
  type: 'bubble', // 设置图表类型
  data: data,  // 设置数据集
  options: {

  },
};
const myChart = new Chart(ctx, config);
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trychartjs_bubble)


以上实例输出结果为：

*







	  AI 思考中...





			* [Chart.js 柱形图](https://www.runoob.com/chartjs-type-bar.html)
			[Chart.js 环形图](https://www.runoob.com/chartjs-doughnut.html) **













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