# CSS position: static 属性值

- Source: https://www.runoob.com/css/css-position-static.html

[![CSS position 属性](https://www.runoob.com/images/up.gif) CSS position 属性](https://www.runoob.com/css-positioning.html)

---


`position: static` 是 CSS 定位属性的默认值。

当一个元素的 `position` 值设为 `static` 时，该元素会按照文档的**正常布局流**进行排列，**不受** `top`、`right`、`bottom`、`left` 和 `z-index` 等定位属性的影响。


换句话说，`static` 就是不做任何特殊定位，元素该在哪就在哪。


**单词释义**：`static` 来自拉丁语 `staticus`，意为"静止的、不动的"，表示元素保持在原本的位置。


---


## 基本语法


`position: static` 是 CSS 定位属性中最简单、最基础的值。


```
/* 语法 */
position: static;

/* 实际示例 */
.box {
    position: static;
}
```


## 属性说明


| 属性值 | 说明 |
| --- | --- |
| static | 默认值，元素按照正常文档流定位，不受定位属性影响 |


### 相关定位属性对 static 的影响


| 属性 | 对 static 元素的效果 |
| --- | --- |
| top | 无效，不产生任何定位效果 |
| right | 无效，不产生任何定位效果 |
| bottom | 无效，不产生任何定位效果 |
| left | 无效，不产生任何定位效果 |
| z-index | 无效，无法手动设置堆叠顺序 |


---


## 实例


让我们通过实例来理解 `position: static` 的行为。


### 示例 1：static 是默认定位方式


即使不显式设置 `position: static`，元素默认就是 static 定位。让我们对比一下：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        /* 容器样式：设置背景和内边距，便于观察 */
        .container {
            padding: 20px;
            background-color: #f5f5f5;
            border: 2px solid #ddd;
        }

        /* 三个 div 块，默认就是 static 定位 */
        .box {
            padding: 15px;
            margin: 10px 0;
            background-color: #3498db;
            color: white;
            border-radius: 4px;
        }

        /* 第二个盒子尝试使用 top 属性定位（对 static 无效） */
        .box-2 {
            position: static;  /* 显式声明也是 static */
            top: 100px;       /* 这个属性不会产生任何效果 */
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box">第一个盒子 (默认 static)</div>
        <div class="box box-2">第二个盒子 (显式 static + top:100px)</div>
        <div class="box">第三个盒子 (默认 static)</div>
    </div>
</body>
</html>
```


**效果说明：**


你会发现第二个盒子并没有因为 `top: 100px` 而向下移动。这是因为 `static` 定位的元素完全忽略 `top`、`right`、`bottom`、`left` 这些定位属性。


### 示例 2：static 元素无法设置 z-index


在正常文档流中，元素的堆叠顺序由它们在 HTML 中的出现顺序决定。我们无法通过 `z-index` 来改变这个顺序：


## 实例


```css
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            position: relative;  /* 父容器设为 relative 作为参照 */
            height: 150px;
            background-color: #f0f0f0;
        }

        .box {
            width: 100px;
            height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
        }

        /* 三个盒子依次出现 */
        .box-1 {
            background-color: #e74c3c;  /* 红色 */
            position: static;            /* 默认定位 */
            z-index: 999;                /* 无效！ */
        }

        .box-2 {
            background-color: #2ecc71;  /* 绿色 */
            position: static;
            margin-top: -30px;           /* 通过负 margin 产生重叠 */
            margin-left: 60px;
        }

        .box-3 {
            background-color: #9b59b6;  /* 紫色 */
            position: static;
            margin-top: -30px;
            margin-left: 120px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box box-1">Box 1 (z-index:999)</div>
        <div class="box box-2">Box 2</div>
        <div class="box box-3">Box 3</div>
    </div>
    <p>即使 Box 1 设置了 z-index: 999，由于它是 static 定位，z-index 不起作用。</p>
    <p>最终堆叠顺序仍然是：后出现的元素在上面（Box 3 最上层，Box 1 最底层）。</p>
</body>
</html>
```


---


## 使用场景


虽然 `position: static` 看起来"什么也不做"，但在以下场景中它很有用：


### 场景 1：重置定位


当你需要取消之前设置的定位效果时，可以将 `position` 改回 `static`：


```
/* 之前可能是 relative、absolute 或 fixed */
.sidebar {
    position: fixed;
    top: 0;
}

/* 现在需要取消固定定位，恢复正常布局 */
.sidebar {
    position: static;  /* 移除固定定位效果 */
}
```


### 场景 2：作为定位子元素的参照


虽然 `static` 本身不定位，但它可以作为**定位上下文**的"基准"：


```
/* 父元素设置为 relative，虽然它自己可能是 static */
.parent {
    position: relative;  /* 创建新的定位上下文 */
}

/* 子元素 absolute 会相对于这个 parent 定位 */
.child {
    position: absolute;
    top: 10px;
    left: 10px;
}
```


### 场景 3：调试和测试


在开发过程中，如果你不确定元素为什么被定位了，可以先设回 `static` 来排查问题：


```
.debug-element {
    position: static;  /* 临时设为 static 看原始位置 */
}
```


---


## 注意事项

**
常见误区：**很多初学者会尝试使用 `top: 0`、`left: 0` 等属性来"重置"元素到左上角，但这些属性对 `static` 元素完全不起作用。如果需要这样的效果，应该使用 `relative`、`absolute` 或 `fixed` 定位。


### 与其它定位值的对比


| 定位值 | 是否脱离文档流 | 是否受 top/right/bottom/left 影响 | 是否支持 z-index |
| --- | --- | --- | --- |
| static | 否，保持正常布局 | 否 | 否 |
| relative | 否，但可以偏移 | 是，相对于原始位置偏移 | 是 |
| absolute | 是，脱离文档流 | 是，相对于最近定位祖先元素 | 是 |
| fixed | 是，脱离文档流 | 是，相对于视口定位 | 是 |
| sticky | 是，滚动到阈值后固定 | 是，设定阈值位置 | 是 |


---


## 总结


`position: static` 是 CSS 定位的基础，理解它的行为对于掌握其它定位方式至关重要。


记住以下关键点：


- `static` 是 `position` 属性的默认值
- `static` 元素按照正常文档流布局
- `top`、`right`、`bottom`、`left` 属性对 `static` 元素**无效**
- `z-index` 属性对 `static` 元素**无效**
- 常用于重置定位或作为定位上下文的基准


---


[![CSS position 属性](https://www.runoob.com/images/up.gif) CSS position 属性](https://www.runoob.com/css-positioning.html)









	  AI 思考中...





			** [CSS 编辑器](https://www.runoob.com/css-editor.html)
			[CSS position: absolute 属性值](https://www.runoob.com/css-position-absolute.html) **













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