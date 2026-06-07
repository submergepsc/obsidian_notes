# Tailwind CSS 边框

- Source: https://www.runoob.com/tailwindcss/tailwindcss-borders.html

在 Tailwind CSS 中，**边框**（Borders）是布局和设计中常见的样式，用于为元素添加边界或分隔线。

Tailwind 提供了多种边框工具类，帮助你控制边框的宽度、颜色、样式、半径以及各个方向的边框。


### 边框宽度（Border Width）


边框宽度决定了元素的边框线条的粗细。Tailwind CSS 提供了不同的边框宽度值，允许你快速控制元素边框的样式。


| 类名 | 描述 | 示例 |
| --- | --- | --- |
| border-{n} | 设置所有边框宽度，n 为宽度值 | border-2（宽度为 2px） |
| border-t-{n} | 设置顶部边框宽度 | border-t-4（顶部边框宽度 4px） |
| border-r-{n} | 设置右侧边框宽度 | border-r-8（右侧边框宽度 8px） |
| border-b-{n} | 设置底部边框宽度 | border-b-1（底部边框宽度 1px） |
| border-l-{n} | 设置左侧边框宽度 | border-l-3（左侧边框宽度 3px） |


### 边框颜色（Border Color）


通过使用 `border-{color}` 工具类，你可以设置元素边框的颜色。Tailwind CSS 提供了大量的预设颜色，可以直接使用，也支持自定义颜色。


| 类名 | 描述 | 示例 |
| --- | --- | --- |
| border-{color} | 设置边框颜色 | border-red-500（红色边框） |
| border-t-{color} | 设置顶部边框颜色 | border-t-blue-300（蓝色顶部边框） |
| border-r-{color} | 设置右侧边框颜色 | border-r-gray-400（灰色右边框） |
| border-b-{color} | 设置底部边框颜色 | border-b-green-600（绿色底部边框） |
| border-l-{color} | 设置左侧边框颜色 | border-l-yellow-500（黄色左边框） |


```
<div class="border-2 border-red-500 p-4">
  红色边框，宽度为 2px
</div>
```


### 边框样式（Border Style）


Tailwind CSS 也支持设置边框的样式，如实线、虚线、点线等。通过 `border-{style}` 工具类，你可以控制边框的显示样式。


| 类名 | 描述 | 示例 |
| --- | --- | --- |
| border-solid | 设置实线边框（默认） | border-solid |
| border-dashed | 设置虚线边框 | border-dashed |
| border-dotted | 设置点线边框 | border-dotted |
| border-double | 设置双线边框 | border-double |


```
<div class="border-4 border-dashed border-blue-400 p-4">
  蓝色虚线边框，宽度为 4px
</div>
```


### 边框半径（Border Radius）


通过设置 `border-radius`，你可以控制元素的圆角效果。Tailwind CSS 提供了多种边框半径值，并允许你在不同方向上设置不同的圆角。


| 类名 | 描述 | 示例 |
| --- | --- | --- |
| rounded-{size} | 设置统一的圆角大小 | rounded-lg（大圆角） |
| rounded-tl-{size} | 设置左上角圆角 | rounded-tl-sm（小圆角） |
| rounded-tr-{size} | 设置右上角圆角 | rounded-tr-md（中等圆角） |
| rounded-br-{size} | 设置右下角圆角 | rounded-br-lg（大圆角） |
| rounded-bl-{size} | 设置左下角圆角 | rounded-bl-xl（特大圆角） |


```
<div class="border-4 border-gray-400 rounded-lg p-6">
  大圆角边框
</div>
```


### 四个方向的边框控制


你可以单独控制每个方向的边框（上、右、下、左），如：`border-t-2` 控制顶部边框的宽度，`border-r-4` 控制右侧边框的宽度，等等。


| 类名 | 描述 | 示例 |
| --- | --- | --- |
| border-t-{size} | 设置顶部边框宽度 | border-t-2（顶部边框宽度 2px） |
| border-r-{size} | 设置右侧边框宽度 | border-r-4（右侧边框宽度 4px） |
| border-b-{size} | 设置底部边框宽度 | border-b-1（底部边框宽度 1px） |
| border-l-{size} | 设置左侧边框宽度 | border-l-3（左侧边框宽度 3px） |


```
<div class="border-t-4 border-r-2 border-b-1 border-l-3 border-blue-500 p-4">
  自定义各个方向的边框
</div>
```


### 统一的边框控制（Border）


如果你想要为所有边框设置相同的样式，使用 `border` 工具类即可。可以结合其他工具类控制颜色、样式和宽度。


| 类名 | 描述 | 示例 |
| --- | --- | --- |
| border | 设置所有边框的宽度为 1px，且为实线 | border（默认宽度为 1px） |
| border-2 | 设置所有边框宽度为 2px | border-2（2px 宽度的实线） |
| border-4 | 设置所有边框宽度为 4px | border-4（4px 宽度的实线） |


```
<div class="border-4 border-solid border-green-500 p-4">
  绿色实线边框，宽度为 4px
</div>
```


### 内边框和外边框（Box Model）


Tailwind CSS 还提供了控制 **盒模型** 的工具类，尤其是内外边框、外边距和内填充等。


| 类名 | 描述 | 示例 |
| --- | --- | --- |
| box-border | 设置盒子模型为 border-box（包含边框在内） | box-border |
| box-content | 设置盒子模型为 content-box（不包含边框） | box-content |


```
<div class="box-border border-4 border-red-500 p-4">
  边框包含在内的盒子模型
</div>
```


### 结合所有边框工具的综合实例


## 实例


```css
<!-- 边框宽度和颜色 -->
<div class="border-4 border-red-500 p-4 mb-6">
    4px 宽的红色边框
</div>

<!-- 边框样式 -->
<div class="border-2 border-dashed border-blue-500 p-4 mb-6">
    蓝色虚线边框，宽度为 2px
</div>

<!-- 边框圆角 -->
<div class="border-4 border-green-500 rounded-lg p-6 mb-6">
    圆角绿色边框
</div>

<!-- 边框方向控制 -->
<div class="border-t-4 border-r-2 border-b-1 border-l-3 border-yellow-500 p-4">
    自定义方向的边框
</div>
```

**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trytailwindcss_borders1)








	  AI 思考中...





			** [Tailwind CSS 背景颜色](https://www.runoob.com/tailwindcss-backgrounds.html)
			[Tailwind CSS4 安装](https://www.runoob.com/tailwindcss4-installbynpm.html) **













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