# Google 地图控件集

- Source: https://www.runoob.com/googleapi/google-maps-controls.html

---


一个Google 地图 - 默认控件集设置：


---


## Google 地图 - 默认控件集设置：


当使用一个标准的google地图，它的默认设置如下：


- .Zoom-显示一个滑动条来控制map的Zoom级别
- .PPan-地图上显示的是一个平底碗样的控件，点击4个角平移地图
- .MapType-允许用户在map types(roadmap 和 satellite)之间切换
- .StreetView-显示为一个街景小人图标，可拖拽到地图上某个点来打开街景


---


## Google 地图 - 更多控件集


除了以上默认控件集,Google还有：


- .Scale-显示地图比例尺
- .Rotate-显示一个小的圆周图标，可以转动地图
- .verview Map-从一个广域的视角俯视地图


创建地图时你可以通过设置选项指定哪些控件集显示或者通过调用 setOptions() 来改变地图的设置选项。


---


## Google 地图 - 关闭默认控件集


你可能希望能够关闭默认的控件集。


为了关闭默认控件集,设置地图的disableDefaultUI的属性为true:


## 实例


```
disableDefaultUI:true
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_controls_disable)


---


## Google 地图 - 开所有控件集


一些控件集默认显示在地图上，而其它的不会，除非你设置它们。


设置控件为true使其可见-设置控件为false则隐藏它。


以下实例开启所有的控件：


## 实例


```
panControl:true,
zoomControl:true,
mapTypeControl:true,
scaleControl:true,
streetViewControl:true,
overviewMapControl:true,
rotateControl:true
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_controls_add)


---


## Google 地图 - 修改控件集


某些地图控件是可配置的。通过制定控件选项域改变控件集。


F举个例子来说，修改Zoom 控件的选项在zoomControlOptions指定。zoomControlOptions包含如下3种选项：


- .google.maps.ZoomControlStyle.SMALL-显示最小化zoom 控件
- .google.maps.ZoomControlStyle.LARGE-显示标准zoom滑动控件
- .google.maps.ZoomControlStyle.DEFAULT-基于设备和地图大小，选择最合适的控件


## 实例


```
zoomControl:true,
zoomControlOptions:
{
  style:google.maps.ZoomControlStyle.SMALL
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_controls_modify1)


注意：** 如果需要修改一个控件，首先开启控件(设置其为true)。


另一个控件为 MapType 控件。


MapType 控件可显示为以下 style 选项之一：


- google.maps.MapTypeControlStyle.HORIZONTAL_BAR，用于在水平栏中将一组控件显示为如 Google Maps 中所示按钮。
- google.maps.MapTypeControlStyle.DROPDOWN_MENU，用于显示单个按钮控件，以便您从下拉菜单中选择地图类型。
- google.maps.MapTypeControlStyle.DEFAULT，用于显示"默认"的行为，该行为取决于屏幕尺寸，并且可能会在 API 以后的版本中有所变化。


## 实例


```
mapTypeControl:true,
mapTypeControlOptions: {
  style:google.maps.MapTypeControlStyle.DROPDOWN_MENU
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_controls_modify2)


同样你可以使用ControlPosition属性指定控件的位置:


## 实例


```
mapTypeControl:true,
mapTypeControlOptions: {
  style:google.maps.MapTypeControlStyle.DROPDOWN_MENU,
  position:google.maps.ControlPosition.TOP_CENTER
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_controls_modify3)


---


## Google 地图 - 自定义控件集


创建一个返回伦敦自定义控件，用于点击事件： (如果地图被拖拽):


## 实例


```
controlDiv.style.padding = '5px';
var controlUI = document.createElement('div');
controlUI.style.backgroundColor = 'yellow';
controlUI.style.border='1px solid';
controlUI.style.cursor = 'pointer';
controlUI.style.textAlign = 'center';
controlUI.title = 'Set map to London';
controlDiv.appendChild(controlUI);
var controlText = document.createElement('div');
controlText.style.fontFamily='Arial,sans-serif';
controlText.style.fontSize='12px';
controlText.style.paddingLeft = '4px';
controlText.style.paddingRight = '4px';
controlText.innerHTML = '<b>Home<b>'
controlUI.appendChild(controlText);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_controls_custom)


---


## Google 地图 - 控件集参考手册


[Google Maps API 参考手册](https://www.runoob.com/google-maps-ref.html).








	  AI 思考中...





			** [Google 地图事件](https://www.runoob.com/google-maps-events.html)
			[Google 地图类型](https://www.runoob.com/google-maps-types.html) **













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