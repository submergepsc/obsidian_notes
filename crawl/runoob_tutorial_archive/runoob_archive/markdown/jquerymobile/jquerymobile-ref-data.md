# jQuery Mobile Data 属性

- Source: https://www.runoob.com/jquerymobile/jquerymobile-ref-data.html

---


## jQuery Data 属性


jQuery Mobile 使用 [HTML5 data-* 属性](https://www.runoob.com/../tags/att-object-data.html)来为移动设备创建更具触摸友好性和吸引性的外观。


在下面的参考列表中，**粗体显示的值**为默认值。


---


## 按钮


在1.4 版本以后已废弃。使用 [CSS 类](https://www.runoob.com/jquerymobile-ref-css.html) 替代。带有 **data-role="button"** 的超链接。button 元素、工具栏中的链接以及 input 字段都会自动渲染成按钮样式，不需要添加 data-role="button"。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-corners | true \| false | 规定按钮是否圆角 |
| data-icon | 图标参考手册 | 规定按钮的图标。默认没有图标。 |
| data-iconpos | left \| right \| top \| bottom \| notext | 规定图标的位置 |
| data-iconshadow | true \| false | 规定按钮图标是否有阴影 |
| data-inline | true \| false | 规定按钮是否内联 |
| data-mini | true \| false | 规定按钮是小尺寸还是常规尺寸 |
| data-shadow | true \| false | 规定按钮是否有阴影 |
| data-theme | 字母 (a-z) | 规定按钮的主题颜色 |

**
|  | 如需组合多个按钮，请使用带有 data-role="controlgroup" 属性和 data-type="horizontal\|vertical" 的容器来规定是否水平或垂直组合按钮。 |
| --- | --- |


---


## 复选框


带有 **type="checkbox"** 的成双成对的 label 和 input。它们会被自动渲染成按钮样式，data-role 不是必需的。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-mini | true \| false | 规定复选框是小尺寸还是常规尺寸 |
| data-role | none | 防止 jQuery Mobile 把复选框渲染成按钮样式 |
| data-theme | 字母 (a-z) | 规定复选框的主题颜色 |


|  | 如需组合多个复选框，请使用带有 data-role="controlgroup" 属性和 data-type="horizontal\|vertical" 的容器来规定是否水平或垂直组合复选框。 |
| --- | --- |


---


## 可折叠块


在带有 **data-role="collapsible"** 的容器内部的后跟任意 HTML 标记的标题元素。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-collapsed | true \| false | 规定内容是折叠还是展开 |
| data-collapsed-icon | 图标参考手册 | 规定可折叠按钮的图标。默认是 "plus" |
| data-content-theme | 字母 (a-z) | 规定可折叠内容的主题颜色。是否为可折叠内容添加圆角 |
| data-expanded-icon | 图标参考手册 | 规定当内容展开时可折叠按钮的图标。默认是 "minus" |
| data-iconpos | left \| right \| top \| bottom | 规定图标的位置 |
| data-inset | true \| false | 规定可折叠按钮是否渲染成圆角且带外边距 |
| data-mini | true \| false | 规定可折叠按钮是小尺寸还是常规尺寸 |
| data-theme | 字母 (a-z) | 规定可折叠按钮的主题颜色 |


---


## 可折叠集合


在带有 **data-role="collapsible-set"** 的容器内部的可折叠内容块。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-collapsed-icon | 图标参考手册 | 规定可折叠按钮的图标。默认是 "plus" |
| data-content-theme | 字母 (a-z) | 规定可折叠按钮的主题颜色 |
| data-expanded-icon | 图标参考手册 | 规定当内容展开时可折叠按钮的图标。默认是 "minus" |
| data-iconpos | left \| right \| top \| bottom \| notext | 规定图标的位置 |
| data-inset | true \| false | 规定可折叠块是否渲染成圆角且带外边距 |
| data-mini | true \| false | 规定可折叠按钮是小尺寸还是常规尺寸 |
| data-theme | 字母 (a-z) | 规定可折叠集合的主题颜色 |


---


## 内容


在 1.4 版本已废弃, 1.5 版本后不再支持。 使用 **data-role="content"** 的容器。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-theme | 字母 (a-z) | 规定内容的主题颜色。 |


---


## 控件组


带有 **data-role="controlgroup"** 的  或  容器。 组合单个类型（基于链接的按钮、单选按钮、复选框、select 元素）的多个按钮样式的 input。对于组合表单复选框和单选按钮，推荐在带有 data-role="fieldcontain" 的  内使用  容器来改进标签样式。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-mini | true \| false | 规定控件组是小尺寸还是常规尺寸 |
| data-type | horizontal \| vertical | 规定控件组是水平显示还是垂直显示 |


---


## 对话框


带有 **data-role="dialog"** 的容器或带有 **data-rel="dialog"** 的链接。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-close-btn-text | sometext | 规定对话框关闭按钮的文本 |
| data-dom-cache | true \| false | 规定是否清除各个页面的 jQuery DOM 缓存（如果设置为 true，您必须自己管理 DOM 并在所有移动设备上进行测试） |
| data-overlay-theme | 字母 (a-z) | 规定对话框页面的蒙版（背景）颜色 |
| data-theme | 字母 (a-z) | 规定对话框页面的主题颜色 |
| data-title | sometext | 规定对话框页面的标题 |


---


## 增强


带有 **data-enhance="false"** 或 **data-ajax="false"** 的容器。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-enhance | true \| false | 如果设置为 "true"（默认），jQuery Mobile 会自动渲染页面，使其更适合于移动设备。如果设置为 "false"，框架将不会渲染页面 |
| data-ajax | true \| false | 规定是否通过 ajax 加载页面 |


注意：**data-enhance="false" 必须与 $.mobile.ignoreContentEnabled=true" 一同使用来阻止 jQuery Mobile 自动渲染页面。


当 $.mobile.ignoreContentEnabled 设置为 true 时，data-ajax="false" 容器内的任何链接或表单元素将会被框架的导航功能忽略。


---


## 域容器


1.4 版本后已废弃，在 1.5 版本后不再支持，将使用 class="ui-fieldcontain 替代"。 包裹在 label/form 元素对，并带有 **data-role="fieldcontain"** 的容器。


---


## 固定工具栏


带有 **data-role="header"** 或 **data-role="footer"**，并带有 **data-position="fixed"** 属性的容器。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-disable-page-zoom | true \| false | 规定用户是否能缩放页面 |
| data-fullscreen | true \| false | 规定工具栏是否一直固定在顶部或底部 |
| data-tap-toggle | true \| false | 规定用户是否能够通过点击改变工具栏的可见性 |
| data-transition | slide \| fade \| none | 规定当点击发生时的切换效果 |
| data-update-page-padding | true \| false | 规定页面顶部和底部的内边距是否在 resize、transition 和 "updatelayout" 事件发生时更新（jQuery Mobile 在 "pageshow" 事件发生时总是更新内边距） |
| data-visible-on-page-show | true \| false | 规定当父页面显示时工具栏的可见性 |

**
---


## 翻转拨动开关


一个带有 **data-role="slider"** 的  元素和两个  元素。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-mini | true \| false | 规定开关是小尺寸还是常规尺寸 |
| data-role | none | 防止 jQuery Mobile 把拨动开关渲染成按钮样式 |
| data-theme | 字母 (a-z) | 规定拨动开关的主题颜色 |
| data-track-theme | 字母 (a-z) | 规定轨道的主题颜色 |


---


## 尾部栏


带有 **data-role="footer"** 的容器。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-id | sometext | 规定唯一 ID。对于持续的尾部栏是必需的 |
| data-position | inline \| fixed | 规定尾部栏是与页面内容内联还是保持固定在底部 |
| data-fullscreen | true \| false | 规定尾部栏是固定在底部还是覆盖在页面内容上（查看范围更大） |
| data-theme | 字母 (a-z) | 规定尾部栏的主题颜色。默认是 "a" |


注意：**如需启用全屏定位，请使用 data-position="fixed"，然后添加 data-fullscreen 属性到元素上。


---


## 头部栏


带有 **data-role="header"** 的容器。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-id | sometext | 规定唯一 ID。对于持续的头部栏是必需的 |
| data-position | inline \| fixed | 规定头部栏是与页面内容内联还是保持固定在顶部 |
| data-fullscreen | true \| false | 规定头部栏是固定在顶部还是覆盖在页面内容上（查看范围更大） |
| data-theme | 字母 (a-z) | 规定头部栏的主题颜色。默认是 "a" |


**注意：**如需启用全屏定位，请使用 data-position="fixed"，然后添加 data-fullscreen 属性到元素上。


---


## 链接


所有的链接，包含那些带有 data-role="button" 的链接和表单提交按钮。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-ajax | true \| false | 规定是否通过 ajax 加载页面来提高用户体验和交互。如果设置为 false，jQuery Mobile 将会执行一个正常的页面请求。 |
| data-direction | reverse | 反向转换动画（仅用于页面和对话框） |
| data-dom-cache | true \| false | 规定是否清除各个页面的 jQuery DOM 缓存（如果设置为 true，您必须自己管理 DOM 并在所有移动设备上进行测试） |
| data-prefetch | true \| false | 规定是否预先读取页面到 DOM 中，以便当用户访问它们时可用 |
| data-rel | back \| dialog \| external \| popup | 规定链接行为的选项。Back - 回退到历史记录中的前一个页面。Dialog - 以对话框形式打开链接，不保存到历史记录中。External - 用于链接到另一个域。Popup - 打开一个弹出窗口。 |
| data-transition | fade \| flip \| flow \| pop \| slide \| slidedown \| slidefade \| slideup \| turn \| none | 规定一个页面切换到下一个页面的效果。请查看我们的 jQuery Mobile 页面切换章节。 |
| data-position-to | origin \| jQuery selector \| window | 规定弹出框的位置。Origin - 默认。定位弹窗在打开它的链接上。jQuery selector - 定位弹窗在指定元素上。Window - 定位弹窗在窗口屏幕的中央。 |

**
---


## 列表


带有 **data-role="listview"** 的  或 。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-autodividers | true \| false | 规定是否自动划分列表项 |
| data-count-theme | 字母 (a-z) | 规定计数气泡的主题颜色。 |
| data-divider-theme | 字母 (a-z) | 规定列表分隔的主题颜色。 |
| data-filter | true \| false | 规定是否在列表中添加搜索框 |
| data-filter-placeholder | sometext | 1.4 版本后废弃。使用 HTML placeholder 属性替代。规定搜索框内的文本。默认是 "Filter items..." |
| data-filter-theme | 字母 (a-z) | 规定搜索过滤的主题颜色。 |
| data-icon | 图标参考手册 | 规定列表的图标 |
| data-inset | true \| false | 规定列表是否渲染成圆角且带外边距 |
| data-split-icon | 图标参考手册 | 规定分割按钮的图表。默认是 "arrow-r" |
| data-split-theme | 字母 (a-z) | 规定分割按钮的主题颜色。 |
| data-theme | 字母 (a-z) | 规定列表的主题颜色 |


---


## 列表项


带有 **data-role="listview"** 的  或  内的 。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-filtertext | sometext | 规定当过滤元素时要搜索的文本。该文本将会被过滤，而不是实际的列表项文本 |
| data-icon | 图标参考手册 | 规定列表项图标 |
| data-role | list-divider | 规定列表项的分隔 |
| data-theme | 字母 (a-z) | 规定列表项的主题颜色 |


注意：**data-icon 属性只作用于带有链接的列表项。


---


## 导航栏


带有 **data-role="navbar"** 容器内部的  元素。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-icon | 图标参考手册 | 规定列表项的图标 |
| data-iconpos | left \| right \| top \| bottom \| notext | 规定图标的位置 |

**
|  | 导航栏从他们的父容器中继承了主题样本。为导航栏设置 data-theme 属性是不可能的。可以为导航栏中的每个链接单独设置 data-theme 属性。 |
| --- | --- |


---


## 页面


带有 **data-role="page"** 的容器。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-add-back-btn | true \| false | 自动添加后退按钮，仅限头部栏 |
| data-back-btn-text | sometext | 规定后退按钮的一些文本 |
| data-back-btn-theme | 字母 (a-z) | 规定后退按钮的主题颜色 |
| data-close-btn-text | 字母 (a-z) | 规定对话框上关闭按钮的一些文本 |
| data-dom-cache | true \| false | 规定是否清除各个页面的 jQuery DOM 缓存（如果设置为 true，您必须自己管理 DOM 并在所有移动设备上进行测试） |
| data-overlay-theme | 字母 (a-z) | 规定对话框页面的蒙版（背景）颜色 |
| data-theme | 字母 (a-z) | 规定页面的主题颜色。 |
| data-title | sometext | 规定页面标题 |
| data-url | url | 更新 URL 的值，而不是用于请求页面的 URL |


---


## 弹窗


带有 **data-role="popup"** 的容器。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-corners | true \| false | 规定弹窗是否圆角 |
| data-overlay-theme | 字母 (a-z) | 规定弹出框的蒙版（背景）颜色。默认是透明背景（无） |
| data-shadow | true \| false | 规定弹出框是否有阴影 |
| data-theme | 字母 (a-z) | 规定弹出框的主题颜色。默认是继承的，"none" 设置弹窗为透明的 |
| data-tolerance | 30, 15, 30, 15 | 规定窗口边缘（上 top、右 right、下 bottom、左 left）的距离 |


带有 **data-rel="popup"** 的锚：


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-position-to | origin \| jQuery selector \| window | >规定弹出框的位置。Origin - 默认。定位弹窗在打开它的链接上。jQuery selector - 定位弹窗在指定元素上。Window - 定位弹窗在窗口屏幕的中央。 |
| data-rel | popup | 用于打开弹出框 |
| data-transition | fade \| flip \| flow \| pop \| slide \| slidedown \| slidefade \| slideup \| turn \| none | 规定一个页面切换到下一个页面的效果。请查看我们的 jQuery Mobile 页面切换章节。 |


---


## 单选按钮


带有 **type="radio"** 的成双成对的 label 和 input。它们会被自动渲染程按钮样式，data-role 不是必需的。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-mini | true \| false | 规定按钮是小尺寸还是常规尺寸 |
| data-role | none | 防止 jQuery Mobile 渲染单选按钮的样式为增强状态的按钮，使元素以 HTML 原生的状态显示 |
| data-theme | 字母 (a-z) | 规定单选按钮的主题颜色 |


|  | 如需组合多个单选按钮，请使用带有 data-role="controlgroup" 属性和 data-type="horizontal\|vertical" 的容器来规定是否水平或垂直组合单选按钮。 |
| --- | --- |


---


## 选择


所有的 **** 元素。这些会被自动渲染成按钮样式，date-role 是不必需的。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-icon | 图标参考手册 | 规定 select 元素的图标。默认是 "arrow-d" |
| data-iconpos | left \| right \| top \| bottom \| notext | 规定图标的位置 |
| data-inline | true \| false | 规定 select 元素是否内联 |
| data-mini | true \| false | 规定 select 元素是小尺寸还是常规尺寸 |
| data-native-menu | true \| false | 当设置为 false 时，它使用 jQuery 自带的自定义的选择菜单（如果您想要让选择菜单在所有的移动设备上都显示相同，则推荐这么使用） |
| data-overlay-theme | 字母 (a-z) | 规定 jQuery 自带的自定义的选择菜单的主题颜色（与 data-native-menu="false" 一起使用） |
| data-placeholder | true \| false | 可在一个非原生的选择菜单的 元素上设置 |
| data-role | none | 防止 jQuery Mobile 把 select 元素渲染成按钮样式 |
| data-theme | 字母 (a-z) | 规定 select 元素的主题颜色 |


|  | 如需组合多个 select 元素，请使用带有 data-role="controlgroup" 属性和 data-type="horizontal\|vertical" 的容器来规定是否水平或垂直组合 select 元素。 |
| --- | --- |


---


## 滑动块


带有 **type="range"** 的输入框。这些会被自动渲染成按钮样式，date-role 是不必需的。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-highlight | true \| false | 规定滑动轨道是否高亮突出显示 |
| data-mini | true \| false | 规定滑动块是小尺寸还是常规尺寸 |
| data-role | none | 防止 jQuery Mobile 渲染滑动块控件为按钮样式 |
| data-theme | 字母 (a-z) | 规定滑动块控件（输入框、手柄和轨道）的主题颜色 |
| data-track-theme | 字母 (a-z) | 规定滑动块轨道的主题颜色 |


---


## 文本输入框 & 文本输入域


带有 **type="text|search|etc."** 的 input 或 **textarea 元素**。这些会被自动渲染成按钮样式，date-role 是不必需的。


| Data-属性 | 值 | 描述 |
| --- | --- | --- |
| data-mini | true \| false | 规定输入框是小尺寸还是常规尺寸 |
| data-role | none | 防止 jQuery Mobile 把输入框/输入域渲染成按钮样式 |
| data-theme | 字母 (a-z) | 规定输入字段的主题颜色 |










	  AI 思考中...





			** [jQuery Mobile 实例](https://www.runoob.com/jquerymobile-examples.html)
			[jQuery Mobile 图标](https://www.runoob.com/jquerymobile-ref-icons.html) **













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