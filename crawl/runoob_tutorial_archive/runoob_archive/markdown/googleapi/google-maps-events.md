# Google 地图事件

- Source: https://www.runoob.com/googleapi/google-maps-events.html

---


点击标记缩放地图 - 绑定在google地图上的事件。


---


## 点击标记缩放地图


我们仍然使用上一遍文章使用的英国伦敦的地图。


点用户点击标记时实现缩放地图的功能(点击标记时绑定地图缩放事件)。


代码如下：


## 实例


```
// Zoom to 9 when clicking on marker
google.maps.event.addListener(marker,'click',function() {
  map.setZoom(9);
  map.setCenter(marker.getPosition());
});
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_marker_click)


使用 addListener() 事件处理程序来注册事件的监听。该方法使用一个对象，一个事件来监听，当指定的事件发生时 函数将被调用。


---


## 重置标记


我们通过给地图添加事件处理程序来改变 'center' 属性，以下代码使用 center_changed 事件在3秒后标记移会中心点:


## 实例


```
google.maps.event.addListener(map,'center_changed',function() {
  window.setTimeout(function() {
    map.panTo(marker.getPosition());
  },3000);
});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_marker_pan)


---


## 点击标记时打开信息窗口。


点击标记在信息窗口显示一些文本信息：


## 实例


```
var infowindow = new google.maps.InfoWindow({
  content:"Hello World!"
});

google.maps.event.addListener(marker, 'click', function() {
  infowindow.open(map,marker);
});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_marker_infowindow)


---


## 设置标记及打开每个标记的信息窗口


当用户点击地图时执行一个窗口


用户点击地图某个位置时使用 placeMarker() 函数在指定位置上放置一个标记，并弹出信息窗口：


## 实例


```
google.maps.event.addListener(map, 'click', function(event) {
  placeMarker(event.latLng);
});

function placeMarker(location) {
  var marker = new google.maps.Marker({
    position: location,
    map: map,
  });
  var infowindow = new google.maps.InfoWindow({
    content: 'Latitude: ' + location.lat() +
    '<br>Longitude: ' + location.lng()
  });
  infowindow.open(map,marker);
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_marker_infowindow2)


---


## Google 地图 - 事件参考手册


[Google Maps API 参考手册](https://www.runoob.com/google-maps-ref.html)。








	  AI 思考中...





			** [Google 地图叠加层](https://www.runoob.com/google-maps-overlays.html)
			[Google 地图控件集](https://www.runoob.com/google-maps-controls.html) **













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