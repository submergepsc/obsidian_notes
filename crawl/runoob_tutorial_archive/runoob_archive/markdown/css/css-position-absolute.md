# CSS position: absolute 属性值

- Source: https://www.runoob.com/css/css-position-absolute.html

[![CSS position 属性](https://www.runoob.com/images/up.gif) CSS position 属性](https://www.runoob.com/css-positioning.html)

---


`position: absolute` 是 CSS 定位属性中最强大的值之一。

**绝对定位**使元素**脱离正常文档流**，不再占据空间，然后相对于其**最近的可定位祖先元素**进行精确定位。


这是制作弹出框、下拉菜单、悬浮卡片等 UI 组件的核心技术。


**单词释义**：`absolute` 来自拉丁语 `absolutus`，意为"绝对的、无条件的"，表示位置完全独立于文档流。


---


## 基本语法


`position: absolute` 需要配合 `top`、`right`、`bottom`、`left` 属性来指定位置。


```
/* 语法 */
position: absolute;

/* 常用组合 */
.box {
    position: absolute;
    top: 0;      /* 顶部对齐 */
    left: 0;     /* 左侧对齐 */
    /* 或者 */
    top: 50%;    /* 居中开始 */
    left: 50%;
    transform: translate(-50%, -50%);  /* 完全居中 */
}
```


## 定位原理


理解 `absolute` 定位的关键是**定位上下文**的概念：


### 定位上下文


绝对定位的元素会**逐层向上查找**，找到第一个**非 static 定位**的祖先元素作为参照。如果找不到这样的祖先元素，则相对于**初始包含块**（通常是页面）定位。


### 查找过程


```
┌─────────────────────────────────────┐
│ 初始包含块 (body 或 html)           │
│  ┌─────────────────────────────┐   │
│  │ parent (position: relative)  │ ← 找到！作为参照 │
│  │  ┌─────────────────────┐    │   │
│  │  │ child (absolute)     │    │   │
│  │  │ top: 0, left: 0      │    │   │
│  │  └─────────────────────┘    │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```


---


## 核心特性


### 特性 1：脱离文档流


`absolute` 元素**不占据文档空间**，周围的元素会无视它的存在，正常排列。这就好像元素从文档中"浮"了起来。


### 特性 2：相对于可定位祖先定位


"可定位"指的是 `position` 值不是 `static`（可以是 `relative`、`absolute`、`fixed` 或 `sticky`）。


### 特性 3：激活 z-index


和 `relative` 一样，`absolute` 会激活 `z-index` 属性。


### 特性 4：margin 会与 padding 合并


与正常文档流不同，`absolute` 元素的 margin 不会与相邻元素的 margin 合并。


---


## 实例


让我们通过实例深入理解 `position: absolute` 的工作方式。


### 示例 1：最基本的绝对定位


这个例子展示了元素如何相对于父容器定位：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        /* 父容器需要设置非 static 定位才能作为参照 */
        .container {
            position: relative;     /* 关键：作为定位参照 */
            width: 300px;
            height: 200px;
            background-color: #f5f5f5;
            border: 2px solid #3498db;
        }

        /* 绝对定位元素 */
        .absolute-box {
            position: absolute;
            top: 20px;
            right: 20px;
            width: 80px;
            height: 40px;
            background-color: #e74c3c;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        父容器 (position: relative)
        <div class="absolute-box">绝对定位</div>
    </div>
    <p>红色盒子相对于父容器（而非页面）的右上角定位。</p>
</body>
</html>
```


### 示例 2：没有定位祖先的情况


如果父元素没有设置定位，元素会一直向上查找，最终相对于页面定位：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        /* 注意：这里没有设置 position: relative */
        .container-no-position {
            width: 300px;
            height: 150px;
            background-color: #f0f0f0;
            border: 2px solid #ccc;
            padding: 20px;
        }

        /* 由于父元素没有定位，会相对于页面定位 */
        .floating-box {
            position: absolute;
            top: 10px;
            left: 10px;
            background-color: #2ecc71;
            color: white;
            padding: 10px 20px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container-no-position">
        父容器 (无定位)
        <div class="floating-box">相对于页面定位</div>
    </div>
    <p>由于父容器没有设置 position，绿色盒子会相对于整个页面（body）的左上角定位。</p>
</body>
</html>
```


### 示例 3：制作居中弹出框


这是 `absolute` 最常见的应用场景之一：制作弹窗。


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        /* 遮罩层：覆盖整个页面 */
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* 弹窗容器 */
        .modal {
            position: relative;   /* 创建定位上下文 */
            width: 400px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }

        /* 弹窗头部 */
        .modal-header {
            background-color: #3498db;
            color: white;
            padding: 15px 20px;
            font-size: 18px;
            font-weight: bold;
        }

        /* 关闭按钮：绝对定位 */
        .modal-close {
            position: absolute;
            top: 10px;
            right: 15px;
            cursor: pointer;
            font-size: 24px;
            line-height: 1;
        }

        /* 弹窗主体 */
        .modal-body {
            padding: 20px;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="overlay">
        <div class="modal">
            <div class="modal-header">
                提示信息
                <span class="modal-close">&times;</span>
            </div>
            <div class="modal-body">
                这是一个使用绝对定位制作的居中弹窗。
                关闭按钮使用 position: absolute 定位在右上角。
            </div>
        </div>
    </div>
</body>
</html>
```


### 示例 4：图片上添加文字水印


利用绝对定位可以在图片上叠加文字或标签：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        .image-container {
            position: relative;  /* 创建定位上下文 */
            display: inline-block;
        }

        .image-container img {
            width: 300px;
            height: 200px;
            display: block;
            object-fit: cover;
        }

        /* 左上角标签 */
        .badge {
            position: absolute;
            top: 10px;
            left: 10px;
            background-color: #e74c3c;
            color: white;
            padding: 4px 10px;
            font-size: 12px;
            font-weight: bold;
            border-radius: 3px;
        }

        /* 右下角水印 */
        .watermark {
            position: absolute;
            bottom: 10px;
            right: 10px;
            color: white;
            font-size: 14px;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
        }
    </style>
</head>
<body>
    <div class="image-container">
        <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200'%3E%3Crect fill='%233498db' width='300' height='200'/%3E%3Ctext x='50%25' y='50%25' text-anchor='middle' fill='white' font-size='24'%3ERUNOOB%3C/text%3E%3C/svg%3E" alt="示例图片">
        <span class="badge">精选</span>
        <span class="watermark">RUNOOB.com</span>
    </div>
</body>
</html>
```


### 示例 5：下拉菜单


绝对定位是制作下拉菜单的关键技术：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        .dropdown {
            position: relative;     /* 创建定位上下文 */
            display: inline-block;
        }

        /* 触发按钮 */
        .dropbtn {
            background-color: #3498db;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        /* 下拉内容 */
        .dropdown-content {
            position: absolute;      /* 绝对定位 */
            top: 100%;               /* 显示在按钮下方 */
            left: 0;
            min-width: 160px;
            background-color: white;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            border-radius: 4px;
            display: none;            /* 默认隐藏 */
        }

        /* 鼠标悬停时显示 */
        .dropdown:hover .dropdown-content {
            display: block;
        }

        /* 下拉选项 */
        .dropdown-content a {
            display: block;
            padding: 12px 16px;
            text-decoration: none;
            color: #333;
            border-bottom: 1px solid #eee;
        }

        .dropdown-content a:hover {
            background-color: #f5f5f5;
        }

        .dropdown-content a:last-child {
            border-bottom: none;
        }
    </style>
</head>
<body>
    <div class="dropdown">
        <button class="dropbtn">下拉菜单</button>
        <div class="dropdown-content">
            <a href="#">选项一</a>
            <a href="#">选项二</a>
            <a href="#">选项三</a>
        </div>
    </div>
    <p>鼠标悬停在上方查看下拉效果</p>
</body>
</html>
```


### 示例 6：九宫格定位


利用绝对定位可以轻松实现元素的九宫格对齐：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        .box {
            position: relative;
            width: 300px;
            height: 200px;
            background-color: #f5f5f5;
            border: 2px solid #ddd;
        }

        .corner {
            position: absolute;
            width: 80px;
            height: 40px;
            background-color: #3498db;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            border-radius: 4px;
        }

        /* 四个角落 */
        .top-left { top: 10px; left: 10px; }
        .top-right { top: 10px; right: 10px; }
        .bottom-left { bottom: 10px; left: 10px; }
        .bottom-right { bottom: 10px; right: 10px; }

        /* 四边中心 */
        .top-center {
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
        .bottom-center {
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }
        .left-center {
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
        }
        .right-center {
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
        }
    </style>
</head>
<body>
    <div class="box">
        <div class="corner top-left">左上</div>
        <div class="corner top-center">上</div>
        <div class="corner top-right">右上</div>
        <div class="corner left-center">左</div>
        <div class="corner right-center">右</div>
        <div class="corner bottom-left">左下</div>
        <div class="corner bottom-center">下</div>
        <div class="corner bottom-right">右下</div>
    </div>
</body>
</html>
```


---


## 注意事项

**
重要提示：**绝对定位元素会脱离文档流，这意味着它不占据任何空间。如果所有兄弟元素都使用绝对定位，可能会导致容器"坍塌"（高度变为 0）。确保父容器有明确的尺寸或使用其他方式撑开高度。


### 定位祖先链


绝对定位会逐层向上查找定位祖先：


```
元素的查找顺序：
1. 首先查找父元素是否有非 static 定位
2. 如果没有，继续查找祖父元素
3. 依此类推，直到 html 元素
4. 如果都没有，则相对于初始包含块（页面）定位
```


### 宽度问题


绝对定位元素的宽度**默认由内容决定**（类似行内元素）。如果需要撑满容器，需要明确设置宽度：


```
.full-width {
    position: absolute;
    left: 0;
    right: 0;     /* 配合 left: 0 和 right: 0 使宽度100% */
    /* 或者 */
    width: 100%;  /* 直接设置宽度 */
}
```


---


## 与其它定位值的对比


| 定位值 | 是否脱离文档流 | 定位参照 | 是否随滚动移动 |
| --- | --- | --- | --- |
| static | 否 | 正常文档流 | 是 |
| relative | 否（保留空间） | 原始位置 | 是 |
| absolute | 是 | 最近定位祖先 | 是 |
| fixed | 是 | 视口（浏览器窗口） | 否 |
| sticky | 否（固定前） | 是（固定后否） |  |


---


## 常见应用场景


### 场景 1：固定头部导航


```
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    height: 60px;
}
```


### 场景 2：图片轮播指示器


```
.carousel {
    position: relative;
}

.indicators {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
}
```


### 场景 3：聊天窗口的气泡定位


```
.message-bubble {
    position: absolute;
    left: 20px;
    max-width: 70%;
}
```


---


## 总结


`position: absolute` 是现代网页布局中不可或缺的技术：


- 元素**脱离文档流**，不占据空间
- 相对于**最近的可定位祖先元素**定位
- 需要配合 `top`、`right`、`bottom`、`left` 使用
- 激活 `z-index`，可以控制堆叠顺序
- 是制作弹窗、下拉菜单、浮动标签的核心技术
- 父容器需要设置为 `relative` 来创建定位上下文


---


[![CSS position 属性](https://www.runoob.com/images/up.gif) CSS position 属性](https://www.runoob.com/css-positioning.html)









	  AI 思考中...





			** [CSS position: static 属性值](https://www.runoob.com/css-position-static.html)
			[CSS position: fixed 属性值](https://www.runoob.com/css-position-fixed.html) **













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