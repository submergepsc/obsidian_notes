# ionic 手势事件

- Source: https://www.runoob.com/ionic/ionic-gesture-event.html

| 事件 | 描述 | 用法 | 实例 |
| --- | --- | --- | --- |
| on-hold | 长按的时间是500毫秒。 |
```
<button
    on-hold="onHold()"
    class="button">
    Test
    </button>
```
 | 尝试一下 » |
| on-tap | 这个是手势轻击事件，如果长按时间超过250毫秒，那就不是轻击了。。 |
```
<button
    on-tap="onTap()"
    class="button">
    Test
    </button>
```
 | 尝试一下 » |
| on-double-tap | 手双击屏幕事件 |
```
<button
    on-double-tap="onDoubleTap()"
    class="button">
    Test
    </button>
```
 | 尝试一下 » |
| on-touch | 这个和 on-tap 还是有区别的，这个是立即执行，而且是用户点击立马执行。不用等待 touchend/mouseup 。 |
```
<button on-touch="onTouch()"
    class="button">
    Test
    </button>
```
 | 尝试一下 » |
| on-release | 当用户结束触摸事件时触发。 |
```
<button
    on-release="onRelease()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |
| on-drag | 这个有点类似于PC端的拖拽。当你一直点击某个物体，并且手开始移动，都会触发 on-drag。 |
```
<button
    on-drag="onDrag()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |
| on-drag-up | 向上拖拽。 |
```
<button
    on-drag-up="onDragUp()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |
| on-drag-right | 向右拖拽。 |
```
<button
    on-drag-right="onDragRight()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |
| on-drag-down | 向下拖拽。 |
```
<button
    on-drag-down="onDragDown()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |
| on-drag-left | 向左边拖拽。 |
```
<button
    on-drag-left="onDragLeft()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |
| on-swipe | 指手指滑动效果，可以是任何方向上的。而且也和 on-drag 类似，都有四个方向上单独的事件。 |
```
<button
    on-swipe="onSwipe()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |
| on-swipe-up | 向上的手指滑动效果。 |
```
<button
    on-swipe-up="onSwipeUp()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |
| on-swipe-right | 向右的手指滑动效果。 |
```
<button
    on-swipe-right="onSwipeRight()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |
| on-swipe-down | 向下的手指滑动效果。 |
```
<button
    on-swipe-down="onSwipeDown()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |
| on-swipe-left | 向左的手指滑动效果。 |
```
<button
    on-swipe-left="onSwipeLeft()"
    class="button">
    Test
</button>
```
 | 尝试一下 » |


---


## $ionicGesture


一个angular服务展示ionicionic.EventController手势。


### 方法


```
on(eventType, callback, $element)
```


在一个元素上添加一个事件监听器。


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| eventType | string | 监听的手势事件。 |
| callback | function(e) | 当手势事件发生时触发的事件。 |
| $element | element | angular元素监听的事件。 |
| options | object | 对象。 |


```
off(eventType, callback, $element)
```


在一个元素上移除一个手势事件监听器。


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| eventType | string | 移除监听的手势事件。 |
| callback | function(e) | 移除监听器。 |
| $element | element | 被监听事件的angular元素。 |








	  AI 思考中...





			** [ionic 切换开关操作](https://www.runoob.com/ionic-ion-toggle.html)
			[ionic 头部和底部](https://www.runoob.com/ionic-ion-header-bar.html) **













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