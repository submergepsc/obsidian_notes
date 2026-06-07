# CSS position: fixed 属性值

- Source: https://www.runoob.com/css/css-position-fixed.html

[![CSS position 属性](https://www.runoob.com/images/up.gif) CSS position 属性](https://www.runoob.com/css-positioning.html)

---


`position: fixed` 是 CSS 定位属性中用于**固定定位**的值。使用固定定位的元素会**脱离文档流**，相对于**浏览器视口**（viewport）进行定位，**不会随页面滚动而移动**。


这是实现固定导航栏、返回顶部按钮、侧边栏广告等功能的核心技术。


**单词释义**：`fixed` 来自拉丁语 `fixare`，意为"固定、安装"，表示元素位置一旦确定就不再改变。


---


## 基本语法


`position: fixed` 需要配合 `top`、`right`、`bottom`、`left` 属性来指定相对于视口的位置。


```
/* 语法 */
position: fixed;

/* 常用组合：固定在顶部 */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 60px;
}

/* 固定在右下角 */
.back-to-top {
    position: fixed;
    bottom: 20px;
    right: 20px;
}
```


## 核心特性


### 特性 1：相对于视口定位


固定定位的元素**不受父元素影响**，始终相对于浏览器窗口的可见区域定位。


### 特性 2：脱离文档流


与 `absolute` 一样，`fixed` 元素**不占据文档空间**，周围的元素会正常排列，**无视**固定定位元素的存在。


### 特性 3：固定不随滚动移动


这是 `fixed` 与 `absolute` 的**关键区别**：无论页面如何滚动，固定定位元素始终保持在指定位置。


### 特性 4：激活 z-index


固定定位会激活 `z-index` 属性，可以控制元素在视口中的堆叠顺序。


---


## 实例


让我们通过实例深入理解 `position: fixed` 的特性。


### 示例 1：固定顶部导航栏


这是 `fixed` 最常见的应用场景：固定导航栏。


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        /* 固定在顶部的导航栏 */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 60px;
            background-color: #2c3e50;
            color: white;
            display: flex;
            align-items: center;
            padding: 0 20px;
            box-sizing: border-box;
            z-index: 1000;
        }

        /* 主要内容区域 */
        .content {
            padding-top: 80px;  /* 避免被导航栏遮挡 */
            padding: 80px 20px 20px;
            max-width: 800px;
            margin: 0 auto;
        }

        .spacer {
            height: 1500px;  /* 创建足够长的滚动区域 */
        }

        .text-block {
            margin-bottom: 20px;
            padding: 20px;
            background-color: #f5f5f5;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="navbar">
        固定导航栏 - 向下滚动查看效果
    </div>
    <div class="content">
        <h1>固定定位示例</h1>
        <p>这是一个使用 position: fixed 实现的固定导航栏。</p>
        <p>无论你如何滚动页面，导航栏都会保持在页面顶部。</p>
        <div class="text-block">
            <h2>内容区域 1</h2>
            <p>这是第一段内容，用来填充页面以便产生滚动条。</p>
        </div>
        <div class="text-block">
            <h2>内容区域 2</h2>
            <p>这是第二段内容。</p>
        </div>
        <div class="text-block">
            <h2>内容区域 3</h2>
            <p>这是第三段内容。</p>
        </div>
        <div class="text-block">
            <h2>内容区域 4</h2>
            <p>这是第四段内容。</p>
        </div>
        <div class="spacer"></div>
    </div>
</body>
</html>
```


### 示例 2：固定在右下角的返回顶部按钮


固定定位也常用于制作"返回顶部"按钮：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        .content {
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }

        /* 页面足够长以产生滚动条 */
        .tall-content {
            height: 2000px;
        }

        /* 固定在右下角的按钮 */
        .back-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background-color: #e74c3c;
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 24px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s;
        }

        .back-to-top:hover {
            transform: scale(1.1);
            background-color: #c0392b;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>返回顶部按钮示例</h1>
        <p>滚动页面查看固定按钮效果。</p>
        <div class="tall-content"></div>
    </div>

    <div class="back-to-top" title="返回顶部">
        ↑
    </div>
</body>
</html>
```


### 示例 3：固定侧边栏


固定定位还可以实现固定侧边栏：


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

        /* 主容器：使用 grid 布局 */
        .container {
            display: grid;
            grid-template-columns: 1fr 200px;
            max-width: 1000px;
            margin: 0 auto;
            min-height: 2000px;
        }

        .main-content {
            padding: 20px;
            background-color: #ecf0f1;
        }

        /* 固定侧边栏 */
        .sidebar {
            position: fixed;
            top: 20px;
            right: calc(50% - 500px + 220px);
            width: 180px;
            background-color: #3498db;
            color: white;
            padding: 15px;
            border-radius: 4px;
        }

        .ad-banner {
            background-color: #e74c3c;
            padding: 10px;
            text-align: center;
            border-radius: 4px;
            margin-bottom: 10px;
        }

        .content-block {
            background-color: white;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="main-content">
            <h1>主内容区域</h1>
            <p>这是主要内容，会随着滚动条移动。</p>
            <div class="content-block">
                <p>内容段落 1 - 填充页面以便产生滚动效果。</p>
            </div>
            <div class="content-block">
                <p>内容段落 2</p>
            </div>
            <div class="content-block">
                <p>内容段落 3</p>
            </div>
            <div class="content-block">
                <p>内容段落 4</p>
            </div>
            <div class="content-block">
                <p>内容段落 5</p>
            </div>
            <div class="content-block">
                <p>内容段落 6</p>
            </div>
            <div class="content-block">
                <p>内容段落 7</p>
            </div>
            <div class="content-block">
                <p>内容段落 8</p>
            </div>
        </div>

        <div class="sidebar">
            <div class="ad-banner">广告位</div>
            <p>固定侧边栏</p>
            <p>无论主内容如何滚动，我始终保持在右侧固定位置。</p>
        </div>
    </div>
</body>
</html>
```


### 示例 4：固定在底部的页脚


有时需要将内容较少的页面页脚固定在底部：


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
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            font-family: Arial, sans-serif;
        }

        .content {
            flex: 1;
            padding: 40px 20px;
            max-width: 800px;
            margin: 0 auto;
            width: 100%;
        }

        /* 固定在底部的页脚 */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 15px;
        }
    </style>
</head>
<body>
    <div class="content">
        <h1>内容较少的页面</h1>
        <p>这个页面的内容很少，但页脚仍然固定在底部。</p>
        <p>利用 flexbox 的 flex: 1 配合 position: fixed 实现。</p>
    </div>

    <div class="footer">
        &copy; 2026 RUNOOB - 固定页脚
    </div>
</body>
</html>
```


### 示例 5：固定遮罩层


固定定位还可以用于创建全屏遮罩：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }

        .open-btn {
            padding: 12px 24px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        /* 固定遮罩层 */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 999;
        }

        /* 隐藏遮罩 */
        .modal-overlay.hidden {
            display: none;
        }

        /* 弹窗内容 */
        .modal-content {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            text-align: center;
            max-width: 400px;
        }

        .modal-content h2 {
            margin-bottom: 15px;
        }

        .close-btn {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #e74c3c;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>固定遮罩示例</h1>
    <p>点击按钮打开弹窗。</p>

    <button class="open-btn" onclick="document.querySelector('.modal-overlay').classList.remove('hidden')">
        打开弹窗
    </button>

    <div class="modal-overlay hidden">
        <div class="modal-content">
            <h2>欢迎来到 RUNOOB</h2>
            <p>这是一个使用固定定位创建的遮罩弹窗。</p>
            <p>遮罩始终覆盖整个视口，不随页面滚动。</p>
            <button class="close-btn" onclick="document.querySelector('.modal-overlay').classList.add('hidden')">
                关闭
            </button>
        </div>
    </div>
</body>
</html>
```


---


## 注意事项

**
移动端兼容性问题：**在 iOS Safari 和某些移动浏览器中，`position: fixed` 可能会有兼容性问题。元素在输入框获得焦点时可能会移动。解决方案包括：使用 `-webkit-position: fixed` 或设置 `transform: translateZ(0)` 来启用硬件加速。


### z-index 层级


固定定位元素的 `z-index` 是相对于**视口**计算的，不是相对于父元素。


### 与绝对定位的区别


| 特性 | position: absolute | position: fixed |
| --- | --- | --- |
| 定位参照 | 最近的可定位祖先元素 | 浏览器视口（viewport） |
| 页面滚动 | 随页面滚动移动 | 固定不移动 |
| 打印 | 正常显示 | 可能不显示或行为异常 |


### 防止固定定位元素被打印


```
@media print {
    .fixed-element {
        position: static;  /* 打印时取消固定定位 */
    }
}
```


---


## 常见应用场景


### 场景 1：固定顶部导航


```
.nav-header {
    position: fixed;
    top: 0;
    width: 100%;
    height: 50px;
    z-index: 100;
}
```


### 场景 2：固定返回按钮


```
.floating-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
}
```


### 场景 3：聊天窗口


```
.chat-widget {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 300px;
    height: 400px;
}
```


---


## 总结


`position: fixed` 是实现固定 UI 元素的核心技术：


- 相对于**浏览器视口**定位，不受父元素影响
- **固定不随页面滚动**移动
- 元素**脱离文档流**，不占据空间
- 激活 `z-index`，可控制堆叠顺序
- 常用于固定导航栏、返回顶部按钮、固定侧边栏、遮罩弹窗
- 移动端需注意兼容性问题


---


[![CSS position 属性](https://www.runoob.com/images/up.gif) CSS position 属性](https://www.runoob.com/css-positioning.html)









	  AI 思考中...





			** [CSS position: absolute 属性值](https://www.runoob.com/css-position-absolute.html)
			[CSS position: relative 属性值](https://www.runoob.com/css-position-relative.html) **













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