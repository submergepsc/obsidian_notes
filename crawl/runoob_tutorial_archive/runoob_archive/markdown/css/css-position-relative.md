# CSS position: relative 属性值

- Source: https://www.runoob.com/css/css-position-relative.html

[![CSS position 属性](https://www.runoob.com/images/up.gif) CSS position 属性](https://www.runoob.com/css-positioning.html)

---


`position: relative` 是 CSS 定位属性中非常实用的一个值。

**相对定位**允许元素相对于其在**正常文档流中的原始位置**进行偏移，同时保留其在文档流中的空间。


这意味着元素移动后，原来占据的位置**仍然被保留**，不会影响周围元素的布局。


**单词释义**：`relative` 来自拉丁语 `relativus`，意为"相对的、相关的"，表示位置是相对于某个参考点确定的。


---


## 基本语法


`position: relative` 需要配合 `top`、`right`、`bottom`、`left` 属性来指定偏移量。


```
/* 语法 */
position: relative;

/* 常用组合：向上偏移 20px，向左偏移 10px */
.box {
    position: relative;
    top: -20px;
    left: 10px;
}
```


## 属性说明


`relative` 定位需要结合以下偏移属性使用：


### 偏移属性


| 属性 | 说明 | 正值效果 | 负值效果 |
| --- | --- | --- | --- |
| top | 相对于原始位置上边缘的偏移 | 向下移动 | 向上移动 |
| bottom | 相对于原始位置下边缘的偏移 | 向上移动 | 向下移动 |
| left | 相对于原始位置左边缘的偏移 | 向右移动 | 向左移动 |
| right | 相对于原始位置右边缘的偏移 | 向左移动 | 向右移动 |


### z-index 属性


`position: relative` 会**激活** `z-index` 属性，允许你控制元素的堆叠顺序：


```
.box {
    position: relative;
    z-index: 10;  /* 设置堆叠顺序，数值越大越在上层 */
}
```


---


## 核心特性


### 特性 1：保留原始空间


这是 `relative` 最重要的特性。元素偏移后，原来在文档流中的位置**仍然保留**，周围元素不会移动来填补这个空缺。


### 特性 2：作为绝对定位的参照


`relative` 元素经常用作**定位上下文**，让其中的 `absolute` 元素相对于它定位：


```
/* 父元素 relative 作为参照 */
.parent {
    position: relative;
}

/* 子元素 absolute 相对于 parent 定位 */
.child {
    position: absolute;
    top: 0;
    left: 0;
}
```


### 特性 3：激活 z-index


只有当 `position` 不是 `static` 时，`z-index` 才会生效。


---


## 实例


让我们通过实例来深入理解 `position: relative` 的特性。


### 示例 1：相对偏移的基本用法


这个例子展示了元素如何相对于原始位置偏移：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            padding: 20px;
            background-color: #f5f5f5;
            border: 2px solid #ddd;
        }

        .box {
            width: 120px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            margin: 10px;
            background-color: #3498db;
            border-radius: 4px;
        }

        /* 第二个盒子使用相对定位偏移 */
        .box-2 {
            position: relative;
            top: 20px;    /* 相对于原始位置向下移动 20px */
            left: 30px;   /* 相对于原始位置向右移动 30px */
            background-color: #e74c3c;  /* 红色，更醒目 */
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box box-1">盒子 1</div>
        <div class="box box-2">盒子 2 (relative)</div>
        <div class="box box-3">盒子 3</div>
    </div>
    <p>观察：盒子 2 发生了偏移，但它原来的位置仍然被保留（盒子 3 位置不变）。</p>
</body>
</html>
```


### 示例 2：负值偏移


负值可以让元素向相反方向移动：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            padding: 30px;
            background-color: #f0f0f0;
            border: 2px solid #ccc;
        }

        .box {
            width: 150px;
            height: 50px;
            background-color: #2ecc71;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 4px;
            margin-bottom: 5px;
        }

        /* 使用负值向上和向左移动 */
        .moved-up {
            position: relative;
            top: -20px;   /* 向上移动 20px */
        }

        .moved-left {
            position: relative;
            left: -30px;  /* 向左移动 30px */
        }

        .both {
            position: relative;
            top: -40px;
            left: 20px;
            background-color: #e74c3c;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box">原始位置</div>
        <div class="box moved-up">top: -20px (上移)</div>
        <div class="box moved-left">left: -30px (左移)</div>
        <div class="box both">组合偏移</div>
    </div>
</body>
</html>
```


### 示例 3：作为绝对定位的参照容器


`relative` 最常见的用途是创建一个定位容器，让子元素的 `absolute` 定位相对于它：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        /* 父容器设置为 relative，创建定位上下文 */
        .card {
            position: relative;       /* 关键：作为子元素定位的参照 */
            width: 300px;
            height: 200px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        /* 图片样式 */
        .card-image {
            width: 100%;
            height: 100%;
            background-color: #3498db;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
        }

        /* 标签使用 absolute 定位，相对于 .card 容器 */
        .card-badge {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #e74c3c;
            color: white;
            padding: 5px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: bold;
        }

        /* 另一种常见用法：右下角的操作按钮 */
        .card-action {
            position: absolute;
            bottom: 15px;
            right: 15px;
            background-color: #2ecc71;
            color: white;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="card-image">卡片图片</div>
        <div class="card-badge">NEW</div>
        <div class="card-action">查看详情</div>
    </div>
    <p>由于 .card 设置了 position: relative，.card-badge 和 .card-action 会相对于卡片边缘定位，而不是整个页面。</p>
</body>
</html>
```


### 示例 4：使用 z-index 控制堆叠顺序


`relative` 定位可以配合 `z-index` 实现元素的层叠效果：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            position: relative;
            height: 200px;
            background-color: #f5f5f5;
            border: 2px solid #ddd;
        }

        .box {
            width: 120px;
            height: 80px;
            position: absolute;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            border-radius: 4px;
        }

        /* 第一个盒子 */
        .box-1 {
            top: 20px;
            left: 20px;
            background-color: #e74c3c;
            z-index: 1;
        }

        /* 第二个盒子 */
        .box-2 {
            top: 40px;
            left: 60px;
            background-color: #2ecc71;
            z-index: 2;
        }

        /* 第三个盒子 */
        .box-3 {
            top: 60px;
            left: 100px;
            background-color: #9b59b6;
            z-index: 3;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box box-1">z-index: 1</div>
        <div class="box box-2">z-index: 2</div>
        <div class="box box-3">z-index: 3</div>
    </div>
    <p>z-index 数值越大，元素越在上层。紫色盒子 (z-index: 3) 遮盖了绿色盒子 (z-index: 2)。</p>
</body>
</html>
```


---


## 注意事项

**
性能提示：**使用 `position: relative` 进行偏移时，元素虽然视觉上移动了，但它在文档流中的原始位置仍被保留。这意味着浏览器需要同时渲染两个位置，可能会影响渲染性能。在复杂页面中应谨慎使用。


### top 和 bottom 同时使用


当 `top` 和 `bottom` 同时使用时，`top` 优先级更高，`bottom` 会被忽略：


```
.box {
    position: relative;
    top: 20px;
    bottom: 50px;  /* 会被忽略，元素最终在 top: 20px 的位置 */
}
```


### left 和 right 同时使用


同样的，`left` 优先级高于 `right`：


```
.box {
    position: relative;
    left: 30px;
    right: 50px;  /* 会被忽略，元素最终在 left: 30px 的位置 */
}
```


---


## 与其它定位值的对比


| 定位值 | 是否保留原始空间 | 偏移参照 | 常见用途 |
| --- | --- | --- | --- |
| static | 是（未偏移） | 无 | 默认布局 |
| relative | 是 | 原始位置 | 微调位置、创建定位容器 |
| absolute | 否 | 最近定位祖先元素 | 精确放置元素 |
| fixed | 否 | 视口 | 固定导航、返回顶部 |
| sticky | 是（阈值前） | 视口（阈值后） | 滚动时固定 |


---


## 常见应用场景


### 场景 1：图标与文字的对齐微调


有时图标和文字略微错位，可以用 `relative` 精确调整：


```
.icon {
    position: relative;
    top: 2px;  /* 向下微调 2px，实现更好的垂直居中 */
}
```


### 场景 2：悬停时的轻微位移效果


按钮悬停时向下移动一点点，增加交互感：


```
.button:hover {
    position: relative;
    top: 2px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
```


### 场景 3：创建弹窗的定位容器


```
.modal-container {
    position: relative;  /* 让弹窗相对于这个容器定位 */
}

.modal {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```


---


## 总结


`position: relative` 是 CSS 布局中非常重要的定位方式：


- 元素相对于**原始位置**偏移，同时**保留原始空间**
- 激活 `z-index`，可以控制堆叠顺序
- 经常用作 `absolute` 定位的**参照容器**
- `top` 和 `left` 优先级高于 `bottom` 和 `right`
- 常用于微调元素位置、创建定位上下文、制作交互效果


---


[![CSS position 属性](https://www.runoob.com/images/up.gif) CSS position 属性](https://www.runoob.com/css-positioning.html)









	  AI 思考中...





			** [CSS position: fixed 属性值](https://www.runoob.com/css-position-fixed.html)
			[CSS position: sticky 属性值](https://www.runoob.com/css-position-sticky.html) **













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