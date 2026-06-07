# Google 地图类型

- Source: https://www.runoob.com/googleapi/google-maps-types.html

---


HYBRID类型的google地图:


---


## Google 地图- 基本地图类型


Google Maps API 中提供了以下地图类型：


- `MapTypeId.ROADMAP`，用于显示默认的道路地图视图
- `MapTypeId.SATELLITE`，用于显示 Google 地球卫星图片
- `MapTypeId.HYBRID`，用于同时显示普通视图和卫星视图
- `MapTypeId.TERRAIN`，用于根据地形信息显示实际地图。


要通过 Map 修改正在使用的地图类型，您可以为其设置 mapTypeId 属性:


var mapProp = {**
  center:new google.maps.LatLng(51.508742,-0.120850),

  zoom:7,

  mapTypeId: google.maps.MapTypeId.HYBRID

};

或者动态修改 mapTypeId：


map.setMapTypeId(google.maps.MapTypeId.HYBRID);


---


## Google 地图- 45° 图像


Google Maps API 针对特定位置支持特殊的 45° 图像。


此类高分辨率图像可提供朝向各基本方向（东南西北）的透视视图。对于支持的地图类型，这些图片还可提供更高的缩放级别。


现有的 google.maps.MapTypeId.SATELLITE 和 google.maps.MapTypeId.HYBRID 地图类型支持高缩放级别的 45° 透视图像（如果有的话）。如果您放大的位置拥有此类图像，那么这些地图类型将会自动通过以下方式更改其视图：


- **地图上现有的任何平移控件都将会变更为在现有的导航控件周围添加一个罗盘转轮。您可以通过该罗盘来更改任意 45° 图像的方向，方法是：拖动该罗盘转轮，然后将方向对准包含图像的最近支持方向。
- **一个旋转控件将会间隙显示在现有的平移和缩放控件之间，它可用于将图像围绕支持方向旋转。旋转控件仅支持顺时针方向旋转。
- 以当前位置为中心的 45° 透视图像将会替代卫星图像或混合图像。默认情况下，此类视图会朝向北方。如果您缩小地图，则地图会重新显示默认的卫星图像或混合图像。
- MapType 控件将启用子菜单切换控件，用于显示 45° 图像。


注意：**缩小显示 45° 图像的地图类型将会还原所有更改，并重新构建原始地图类型。


以下示例显示了意大利威尼斯公爵宫45°视图：


## 实例


```
var mapProp = {
    center:myCenter,
    zoom:18,
    mapTypeId:google.maps.MapTypeId.HYBRID
};
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryhtml_map_types_45)


提示：**Google 正在不断地为更多城市添加 45° 图像。有关最新信息，请参阅 [Google 地图上的 45° 图像](https://goo.gl/AIWE)列表。


---


## Google 地图 - 启用和停用 45° 图像 - setTilt(0)


您可以通过在 Map 对象上调用 setTilt(0) 来停用 45° 图像。要启用适用于支持的地图类型的 45° 透视图像，请调用 setTilt(45)。


## 实例


```
map.setTilt(0);
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryhtml_map_types_settilt)


---


## Google 地图 - 参考手册


[Google 地图 API 参考手册](https://www.runoob.com/google-maps-ref.html)。









	  AI 思考中...





			** [Google 地图控件集](https://www.runoob.com/google-maps-controls.html)
			[Google 地图参考手册](https://www.runoob.com/google-maps-ref.html) **













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