# 地图 API Map() 构造器

- Source: https://www.runoob.com/googleapi/ref-map.html

**
## 实例


创建一个 Google 地图:


```
var map=new google.maps.Map(document.getElementById("googleMap"),mapOpt);
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_ref_map)


---


## 定义和用法


Map() 构造器创建了一个新的地图并插入到指定的HTML元素中（ 元素)。


---


## 语法


new google.maps.Map(*HTMLElement*,*MapOptions*)

## 参数值


| 参数 | 描述 |
| --- | --- |
| HTMLElement | 规定要把地图放置在那个 HTML 元素中。 |
| MapOptions | 带有地图初始化变量/选项的 MapOptions 对象。 |


---


## Map() 的方法


| 方法 | 返回值 | 描述 |
| --- | --- | --- |
| fitBounds(LatLngBounds) | None | 设置要包含给定边界的视口。 |
| getBounds() | LatLng,LatLng | 返回当前视口的西南纬度/经度和东北纬度/经度。 |
| getCenter() | LatLng | 返回地图的中心的纬度/经度。 |
| getDiv() | Node | 返回包含地图的 DOM 对象。 |
| getHeading() | number | 返回航拍图像的罗盘航向（支持 SATELLITE 和 HYBRID 地图类型）。 |
| getMapTypeId() | HYBRID ROADMAP SATELLITE TERRAIN | 返回当前地图类型。 |
| getProjection() | Projection | 返回当前 Projection（投影）。 |
| getStreetView() | StreetViewPanorama | 返回绑定到地图的默认的 StreetViewPanorama。 |
| getTilt() | number | 返回航拍图像的入射角度数（支持 SATELLITE 和 HYBRID 地图类型）。 |
| getZoom() | number | 返回地图的当前缩放级别。 |
| panBy(xnumber,ynumber) | None | 通过以像素计的给定距离改变地图的中心。 |
| panTo(LatLng) | None | 改变地图的中心为给定的 LatLng。 |
| panToBounds(LatLngBounds) | None | 将地图平移所需的最小距离以包含给定的 LatLngBounds。 |
| setCenter(LatLng) | None |  |
| setHeading(number) | None | 设置航拍图像的罗盘方向（以度为单位进行测量），基本方向为北方。 |
| setMapTypeId(MapTypeId) | None | 改变要显示的地图类型。 |
| setOptions(MapOptions) | None |  |
| setStreetView(StreetViewPanorama) | None | 绑定一个 StreetViewPanorama 到地图上。 |
| setTilt(number) | None | 设置航拍图像的入射角度数（支持 SATELLITE 和 HYBRID 地图类型）。 |
| setZoom(number) | None |  |


## Map() 的属性


| 属性 | 类型 | 描述 |
| --- | --- | --- |
| controls | Array.> | 要附加到地图上的额外控件。 |
| mapTypes | MapTypeRegistry | 按字符串 ID 划分的 MapType 实例的注册表。 |
| overlayMapTypes | MVCArray. | 要叠加的额外地图类型。 |


## Map() 的事件


| 事件 | 参数 | 描述 |
| --- | --- | --- |
| bounds_changed | None | 当可视区域范围更改时会触发此事件。 |
| center_changed | None | 当地图 center（中心）属性更改时会触发此事件。 |
| click | MouseEvent | 当用户点击地图（但不是点击标记或信息窗口）时会触发此事件。 |
| dblclick | MouseEvent | 当用户双击地图时会触发此事件。请注意，触发此事件前还会触发点击事件。 |
| drag | None | 当用户拖动地图时会反复触发此事件。 |
| dragend | None | 当用户停止拖动地图时会触发此事件。 |
| dragstart | None | 当用户开始拖动地图时会触发此事件。 |
| heading_changed | None | 当地图 heading（方向）属性更改时会触发此事件。 |
| idle | None | 当地图在平移或缩放之后变为闲置状态时会触发此事件。 |
| maptypeid_changed | None | 当 mapTypeId 属性更改时会触发此事件。 |
| mousemove | MouseEvent | 只要用户的鼠标在地图容器上移动，就会触发此事件。 |
| mouseout | MouseEvent | 当用户的鼠标从地图容器上退出时会触发此事件。 |
| mouseover | MouseEvent | 当用户的鼠标进入地图容器时会触发此事件。 |
| projection_changed | None | 当投影更改时会触发此事件。 |
| resize | None | 当地图（div）更改尺寸时会触发此事件。 |
| rightclick | MouseEvent | 当用户右击地图时会触发此事件。 |
| tilesloaded | None | 当可见图块载入完成后会触发此事件。 |
| tilt_changed | None | 当地图 tilt（倾斜）属性更改时会触发此事件。 |
| zoom_changed | None | 当地图 zoom（缩放）属性更改时会触发此事件。 |









	  AI 思考中...





			** [Google 地图参考手册](https://www.runoob.com/google-maps-ref.html)
			[地图 API MapOptions 对象](https://www.runoob.com/ref-mapoptions.html) **













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