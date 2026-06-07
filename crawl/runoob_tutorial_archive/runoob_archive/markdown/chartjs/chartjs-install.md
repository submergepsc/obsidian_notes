# Chart.js 安装

- Source: https://www.runoob.com/chartjs/chartjs-install.html

Chart.js 提供了多种安装方式，适合不同的开发场景：


- NPM/Yarn - 适合使用构建工具的项目开发
- CDN - 适合快速原型开发和学习
- GitHub - 适合需要最新特性或参与贡献的开发


---


## 1. 通过 NPM/Yarn 安装


NPM (Node Package Manager) 是 JavaScript 的包管理工具，适合现代前端项目开发。


### 安装步骤


```
# 使用 npm 安装
npm install chart.js

# 或者使用 yarn 安装
yarn add chart.js
```


### 在项目中引入

安装完成后，你可以在 JavaScript 文件中这样引入 Chart.js：


## 实例


```javascript
// 引入整个 Chart.js 库
import Chart from 'chart.js/auto';

// 或者按需引入特定图表类型（减小打包体积）
import { Line } from 'chart.js';
```


### 版本管理

要安装特定版本的 Chart.js，可以指定版本号：


```
npm install [email protected]
```


## 2. 通过 CDN 使用

CDN (Content Delivery Network) 是通过网络直接加载库文件的方式，适合快速原型开发。


### 推荐 CDN 地址


```
<!-- 字节跳动 CDN（国内推荐） -->
<script src="<script src="https://lf6-cdn-tos.bytecdntp.com/cdn/expire-1-M/Chart.js/3.7.1/chart.min.js"></script>"></script>

<!-- Staticfile CDN（国内备选） -->
<script src="https://cdn.staticfile.net/Chart.js/3.9.1/chart.min.js"></script>

<!-- cdnjs CDN（海外推荐） -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
```


## 实例


```javascript
<!DOCTYPE html>
<html>
<head>
    <title>Chart.js CDN 示例</title>
    <!-- 引入 Chart.js -->
   <script src="<script src="https://lf6-cdn-tos.bytecdntp.com/cdn/expire-1-M/Chart.js/3.7.1/chart.min.js"></script>"></script>
</head>
<body>
    <div style="width: 600px; height: 400px;">
        <canvas id="myChart"></canvas>
    </div>

    <script>
        // 获取 canvas 元素
        const ctx = document.getElementById('myChart').getContext('2d');

        // 创建图表
        const myChart = new Chart(ctx, {
            type: 'bar', // 图表类型
            data: {
                labels: ['一月', '二月', '三月', '四月', '五月', '六月'],
                datasets: [{
                    label: '月度销售额',
                    data: [12, 19, 3, 5, 2, 3],
                    backgroundColor: 'rgba(54, 162, 235, 0.5)'
                }]
            },
            options: {
                responsive: true, // 响应式设计
                scales: {
                    y: {
                        beginAtZero: true // y轴从0开始
                    }
                }
            }
        });
    </script>
</body>
</html>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trychartjs_install_demo1)


本系列会采用国内的 CDN 地址来测试，如下实例：


## 实例


```javascript
<script src="https://cdn.staticfile.net/Chart.js/3.9.1/chart.js"></script>
<script>
    const myChart = new Chart(ctx, {...});
</script>
```


---


## 3. 从 GitHub 获取


GitHub 是开源项目的托管平台，适合需要最新特性或参与项目贡献的开发者。


### 获取方式

克隆仓库（需要 Git）：


```
git clone https://github.com/chartjs/Chart.js.git
```


### 下载 ZIP 文件


- 访问 [Chart.js GitHub](https://github.com/chartjs/Chart.js)
- 点击 "Code" 按钮
- 选择 "Download ZIP"


### 构建项目

下载后，你可以构建自己的 Chart.js 版本：


```
cd Chart.js
npm install
npm run build
```


构建完成后，可以在 dist/ 目录找到生成的文件。

---


## 安装方式对比


| 方式 | 优点 | 缺点 | 适用场景 |
| --- | --- | --- | --- |
| NPM/Yarn | 版本管理方便，适合现代前端项目 | 需要构建工具 | 正式项目开发 |
| CDN | 简单快捷，无需构建 | 依赖网络，版本更新不及时 | 快速原型、学习 |
| GitHub | 获取最新代码，可自定义 | 需要手动构建 | 高级开发、贡献代码 |








	  AI 思考中...





			** [Chart.js 教程](https://www.runoob.com/chartjs-tutorial.html)
			[Chart.js 使用](https://www.runoob.com/chartjs-usage.html) **













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