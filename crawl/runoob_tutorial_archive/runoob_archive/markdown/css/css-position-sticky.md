# CSS position: sticky 属性值

- Source: https://www.runoob.com/css/css-position-sticky.html

[![CSS position 属性](https://www.runoob.com/images/up.gif) CSS position 属性](https://www.runoob.com/css-positioning.html)

---


`position: sticky` 是 CSS 定位属性中相对较新的值。**粘性定位**是**相对定位**和**固定定位**的混合体：元素在跨越指定的**阈值**之前表现得像相对定位，之后表现得像固定定位。


这是实现"吸顶导航"、"表格标题固定"等效果的现代解决方案。


**单词释义**：`sticky` 意为"粘性的"，表示元素会"粘"在某个位置不动。


---


## 基本语法


`position: sticky` 需要配合至少一个方向（`top`、`right`、`bottom`、`left`）的阈值来指定"粘性"生效的位置。


```
/* 语法 */
position: sticky;

/* 常用组合：滚动到距离顶部 10px 时固定 */
.sticky-header {
    position: sticky;
    top: 10px;
}
```


## 工作原理


`sticky` 定位的工作方式可以分解为两个阶段：


### 阶段 1：正常滚动（相对定位）


当元素在视口中**未达到**指定的阈值时，元素按照正常文档流布局，**会随页面滚动移动**。此时它相当于 `position: relative`。


### 阶段 2：固定显示（固定定位）


当元素滚动到**超过**指定的阈值时，元素**固定**在那个位置，不再随页面滚动。此时它相当于 `position: fixed`。


### 阈值条件


| 属性 | 触发条件 |
| --- | --- |
| top: 10px | 元素顶部距离视口顶部 > 10px 时固定 |
| bottom: 10px | 元素底部距离视口底部 > 10px 时固定 |
| left: 10px | 元素左边距离视口左边 > 10px 时固定 |
| right: 10px | 元素右边距离视口右边 > 10px 时固定 |


---


## 核心特性


### 特性 1：双向行为


sticky 兼具 relative 和 fixed 的特点，是两者的完美结合。


### 特性 2：不需要父元素设置定位


与 `absolute` 不同，sticky 元素**不需要**父元素设置任何定位属性。


### 特性 3：父容器overflow的限制


如果父元素设置了 `overflow: hidden`、`overflow: auto` 或 `overflow: scroll`，sticky 定位可能会失效。


### 特性 4：激活 z-index


sticky 定位会激活 `z-index` 属性。


---


## 实例


让我们通过实例深入理解 `position: sticky` 的特性。


### 示例 1：吸顶导航栏


这是 sticky 定位最常见的应用：实现吸顶导航栏。


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
        }

        /* 页面顶部大图区域 */
        .hero {
            height: 300px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 36px;
            font-weight: bold;
        }

        /* 粘性导航栏 */
        .sticky-nav {
            position: sticky;
            top: 0;  /* 滚动到顶部时固定 */
            background-color: #2c3e50;
            color: white;
            padding: 15px 30px;
            z-index: 100;
        }

        .sticky-nav ul {
            list-style: none;
            display: flex;
            gap: 30px;
            max-width: 800px;
            margin: 0 auto;
        }

        .sticky-nav a {
            color: white;
            text-decoration: none;
        }

        /* 内容区域 */
        .content {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        .section {
            margin-bottom: 40px;
            padding: 20px;
            background-color: #f5f5f5;
            border-radius: 4px;
        }

        .tall-spacer {
            height: 1500px;
        }
    </style>
</head>
<body>
    <div class="hero">
        RUNOOB 教程
    </div>

    <nav class="sticky-nav">
        <ul>
            <li><a href="#">首页</a></li>
            <li><a href="#">教程</a></li>
            <li><a href="#">实例</a></li>
            <li><a href="#">工具</a></li>
            <li><a href="#">关于</a></li>
        </ul>
    </nav>

    <div class="content">
        <div class="section">
            <h2>第一章：入门</h2>
            <p>这是第一章的内容。向下滚动查看导航栏的粘性效果。</p>
        </div>
        <div class="section">
            <h2>第二章：进阶</h2>
            <p>这是第二章的内容。</p>
        </div>
        <div class="section">
            <h2>第三章：高级</h2>
            <p>这是第三章的内容。</p>
        </div>
        <div class="section">
            <h2>第四章：实战</h2>
            <p>这是第四章的内容。</p>
        </div>
        <div class="section">
            <h2>第五章：项目</h2>
            <p>这是第五章的内容。</p>
        </div>
        <div class="tall-spacer"></div>
    </div>
</body>
</html>
```


### 示例 2：表格标题行固定


sticky 定位非常适合用于固定表格的表头：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        .table-container {
            max-width: 600px;
            max-height: 300px;
            overflow-y: auto;  /* 需要设置 overflow 才能看到固定效果 */
            border: 2px solid #ddd;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        /* 表头使用 sticky 定位 */
        th {
            position: sticky;
            top: 0;
            background-color: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
        }

        td {
            padding: 10px 12px;
            border-bottom: 1px solid #eee;
        }

        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h2>学生成绩表</h2>
    <p>向下滚动查看表头固定效果：</p>

    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th>学号</th>
                    <th>姓名</th>
                    <th>语文</th>
                    <th>数学</th>
                    <th>英语</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>001</td>
                    <td>张三</td>
                    <td>85</td>
                    <td>92</td>
                    <td>88</td>
                </tr>
                <tr>
                    <td>002</td>
                    <td>李四</td>
                    <td>90</td>
                    <td>87</td>
                    <td>95</td>
                </tr>
                <tr>
                    <td>003</td>
                    <td>王五</td>
                    <td>78</td>
                    <td>85</td>
                    <td>82</td>
                </tr>
                <tr>
                    <td>004</td>
                    <td>赵六</td>
                    <td>92</td>
                    <td>88</td>
                    <td>90</td>
                </tr>
                <tr>
                    <td>005</td>
                    <td>钱七</td>
                    <td>88</td>
                    <td>91</td>
                    <td>87</td>
                </tr>
                <tr>
                    <td>006</td>
                    <td>孙八</td>
                    <td>85</td>
                    <td>89</td>
                    <td>93</td>
                </tr>
                <tr>
                    <td>007</td>
                    <td>周九</td>
                    <td>80</td>
                    <td>86</td>
                    <td>84</td>
                </tr>
                <tr>
                    <td>008</td>
                    <td>吴十</td>
                    <td>91</td>
                    <td>93</td>
                    <td>89</td>
                </tr>
                <tr>
                    <td>009</td>
                    <td>郑十一</td>
                    <td>87</td>
                    <td>85</td>
                    <td>88</td>
                </tr>
                <tr>
                    <td>010</td>
                    <td>陈十二</td>
                    <td>89</td>
                    <td>90</td>
                    <td>91</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>
```


### 示例 3：侧边栏粘性效果


当页面内容很长时，可以让侧边栏在滚动到一定位置后固定：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
        }

        .container {
            display: grid;
            grid-template-columns: 1fr 200px;
            max-width: 900px;
            margin: 0 auto;
        }

        .main-content {
            padding: 20px;
        }

        /* 粘性侧边栏 */
        .sidebar {
            position: sticky;
            top: 20px;  /* 距离顶部 20px 时固定 */
            height: fit-content;
            background-color: #3498db;
            color: white;
            padding: 15px;
            border-radius: 4px;
        }

        .content-block {
            background-color: #f5f5f5;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 4px;
        }

        .tall-block {
            height: 800px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="main-content">
            <h1>主内容区域</h1>
            <p>向下滚动查看侧边栏的粘性效果。</p>

            <div class="content-block">
                <h2>内容区域 1</h2>
                <p>这是第一段内容。</p>
            </div>
            <div class="content-block">
                <h2>内容区域 2</h2>
                <p>这是第二段内容。</p>
            </div>
            <div class="content-block">
                <h2>内容区域 3</h2>
                <p>这是第三段内容。</p>
            </div>
            <div class="content-block tall-block">
                <h2>长内容区域</h2>
                <p>这是比较长的内容区域，用来展示侧边栏的粘性效果。</p>
                <p>继续向下滚动...</p>
            </div>
            <div class="content-block">
                <h2>内容区域 4</h2>
                <p>这是第四段内容。</p>
            </div>
            <div class="content-block">
                <h2>内容区域 5</h2>
                <p>这是第五段内容。</p>
            </div>
        </div>

        <aside class="sidebar">
            <h3>侧边栏</h3>
            <p>我会粘在右侧</p>
            <p>直到滚动出视口</p>
        </aside>
    </div>
</body>
</html>
```


### 示例 4：分段标题固定


sticky 定位非常适合用于文章的分段标题固定：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }

        /* 分段标题固定 */
        .chapter-title {
            position: sticky;
            top: 0;
            background-color: #2c3e50;
            color: white;
            padding: 15px;
            margin: 20px 0 10px;
            border-radius: 4px;
        }

        .content {
            padding: 0 15px;
            line-height: 1.8;
            margin-bottom: 30px;
        }

        .tall-content {
            height: 600px;
        }
    </style>
</head>
<body>
    <h1>书籍章节示例</h1>

    <div class="chapter-title">第一章：初识编程</div>
    <div class="content">
        <p>编程是一门创造性的艺术。本章将带你了解什么是编程，以及为什么学习编程如此重要。</p>
    </div>

    <div class="chapter-title">第二章：环境搭建</div>
    <div class="content tall-content">
        <p>在开始编写代码之前，我们需要先搭建开发环境。本章介绍如何安装必要的工具和配置开发环境。</p>
        <p>内容区域足够长，以便产生滚动效果。</p>
    </div>

    <div class="chapter-title">第三章：基础语法</div>
    <div class="content">
        <p>本章介绍编程语言的基础语法，包括变量、数据类型、运算符等核心概念。</p>
    </div>

    <div class="chapter-title">第四章：控制结构</div>
    <div class="content tall-content">
        <p>控制结构决定了程序的执行顺序。介绍条件语句和循环语句的使用方法。</p>
    </div>

    <div class="chapter-title">第五章：函数</div>
    <div class="content">
        <p>函数是组织代码的基本单元。本章讲解如何定义和调用函数。</p>
    </div>
</body>
</html>
```


### 示例 5：双向粘性定位


可以同时设置水平和垂直方向的粘性定位：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        .calendar {
            width: 350px;
            border: 2px solid #ddd;
        }

        /* 星期标题行 - 顶部固定 */
        .weekday {
            position: sticky;
            top: 0;
            background-color: #3498db;
            color: white;
            padding: 10px;
            text-align: center;
        }

        /* 时间列 - 左侧固定 */
        .time-label {
            position: sticky;
            left: 0;
            background-color: #ecf0f1;
            padding: 20px 10px;
            border-right: 1px solid #ddd;
            font-weight: bold;
        }

        /* 日期单元格 */
        .day-cell {
            padding: 20px;
            border: 1px solid #eee;
            text-align: center;
        }

        .day-cell:nth-child(2) {
            position: sticky;
            left: 50px;  /* 时间列宽度 + 边框 */
            background-color: white;
        }

        /* 模拟日历网格 */
        .calendar-grid {
            display: grid;
            grid-template-columns: 50px repeat(5, 1fr);
        }
    </style>
</head>
<body>
    <h2>课程表（双向粘性）</h2>
    <p>向下和向右滚动查看效果：</p>

    <div class="calendar">
        <div class="calendar-grid">
            <!-- 星期标题行 -->
            <div></div>  <!-- 时间列空白 -->
            <div class="weekday">周一</div>
            <div class="weekday">周二</div>
            <div class="weekday">周三</div>
            <div class="weekday">周四</div>
            <div class="weekday">周五</div>

            <!-- 时间行 1 -->
            <div class="time-label">8:00</div>
            <div class="day-cell">数学</div>
            <div class="day-cell">语文</div>
            <div class="day-cell">英语</div>
            <div class="day-cell">物理</div>
            <div class="day-cell">化学</div>

            <!-- 时间行 2 -->
            <div class="time-label">9:00</div>
            <div class="day-cell">英语</div>
            <div class="day-cell">数学</div>
            <div class="day-cell">化学</div>
            <div class="day-cell">语文</div>
            <div class="day-cell">物理</div>

            <!-- 时间行 3 -->
            <div class="time-label">10:00</div>
            <div class="day-cell">物理</div>
            <div class="day-cell">化学</div>
            <div class="day-cell">数学</div>
            <div class="day-cell">英语</div>
            <div class="day-cell">语文</div>

            <!-- 时间行 4 -->
            <div class="time-label">11:00</div>
            <div class="day-cell">语文</div>
            <div class="day-cell">物理</div>
            <div class="day-cell">数学</div>
            <div class="day-cell">化学</div>
            <div class="day-cell">英语</div>
        </div>
    </div>
</body>
</html>
```


---


## 注意事项

**
浏览器兼容性：**`position: sticky` 在现代浏览器中得到良好支持，但 IE 浏览器完全不支持。如果需要支持 IE，需要使用 JavaScript 或其他 polyfill 方案作为降级处理。


### 父元素 overflow 的影响


如果父元素设置了以下属性，sticky 定位会**失效**：


```
overflow: hidden
overflow: auto
overflow: scroll
```


### 必须设置阈值


至少需要设置 `top`、`right`、`bottom` 或 `left` 中的**一个**，否则 sticky 不会生效（元素会按照正常文档流布局）。


### 阈值计算


sticky 定位的阈值是**相对于视口**计算的，而不是父元素。


---


## 与其它定位值的对比


| 定位值 | 是否脱离文档流 | 固定条件 | 兼容性 |
| --- | --- | --- | --- |
| static | 否 | 无 | 所有浏览器 |
| relative | 否 | 无 | 所有浏览器 |
| absolute | 是 | 无 | 所有浏览器 |
| fixed | 是 | 始终固定 | 所有浏览器 |
| sticky | 阈值前否，阈值后是 | 滚动超过阈值 | 现代浏览器（IE 不支持） |


---


## 常见应用场景


### 场景 1：吸顶导航


```
.nav {
    position: sticky;
    top: 0;
}
```


### 场景 2：表格表头固定


```
th {
    position: sticky;
    top: 0;
}
```


### 场景 3：侧边栏固定


```
.sidebar {
    position: sticky;
    top: 20px;
}
```


### 场景 4：文章章节标题


```
.chapter-header {
    position: sticky;
    top: 0;
    background: white;  /* 固定时显示背景 */
}
```


---


## 总结


`position: sticky` 是现代网页布局中非常实用的技术：


- 是**相对定位**和**固定定位**的结合体
- 需要设置至少一个方向的阈值（top/right/bottom/left）
- 滚动超过阈值前：按照正常文档流布局（相对定位）
- 滚动超过阈值后：固定在当前位置（固定定位）
- 不需要父元素设置任何定位
- 父元素设置 overflow 会导致失效
- 现代浏览器支持良好，IE 不支持
- 常用于吸顶导航、表头固定、侧边栏固定、分段标题固定


---


[![CSS position 属性](https://www.runoob.com/images/up.gif) CSS position 属性](https://www.runoob.com/css-positioning.html)









	  AI 思考中...





			** [CSS position: relative 属性值](https://www.runoob.com/css-position-relative.html)














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

      : ·[CSS 实例](https://www.runoob.com/css-examples.html)

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