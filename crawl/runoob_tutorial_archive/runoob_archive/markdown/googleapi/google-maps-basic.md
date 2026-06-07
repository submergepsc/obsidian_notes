# Google Maps 基础

- Source: https://www.runoob.com/googleapi/google-maps-basic.html

---


## 创建一个简单的 Google 地图


现在让我们创建一个简单的 Google 地图。


以下是显示了英国伦敦的 Google 地图：


## 实例


```
<!DOCTYPE html>
<html>
<head>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDJW4jsPlNKgv6jFm3B5Edp5ywgdqLWdmc&callback=initMap" async defer></script>

<script>
function initialize()
{
    var mapProp = {
        center:new google.maps.LatLng(51.508742,-0.120850),
        zoom:5,
        mapTypeId:google.maps.MapTypeId.ROADMAP
    };
    var map=new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

google.maps.event.addDomListener(window, 'load', initialize);
</script>
</head>

<body>
<div id="googleMap" style="width:500px;height:380px;"></div>

</body>
</html>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_first)


---


## 实例解析


我们以以上实例来解析 Google 地图的创建过程。


## 应用为什么要声明 HTML5?


<!DOCTYPE html>

大多数浏览器使用 "标准模式" 的 HTML5 文档渲染页面，这就意味着你的应用是兼容各大浏览器的。


另外，如果没有DOCTYPE标签，浏览器则使用混杂模式 (quirks mode)进行渲染页面内容。


提示：** 应该注意的是一些"混杂模式 "中的CSS并不能使用于标准模式中。在具体的应用中，所有基于百分比的大小都必须从父块元素继承 。如果在父模块中没有指定大小，默认值为 0 x 0 像素。如果你想使用百分比，可以在 标签中声明，如下所示：


<style type="text/css">**
html {height:100%}

body {height:100%;margin:0;padding:0}

#googleMap {height:100%}

</style>

这个样式声明表明地图模块的（GoogleMap）应 HTML高度为100%。


---


## 添加 Google 地图 API Key


在以下实例中第一个 标签中必须包含 Google 地图 API：


<script src="http://maps.googleapis.com/maps/api/js?key=*YOUR_API_KEY***&sensor=***TRUE_OR_FALSE***"></script>

将google生成的 API key 放置于 **key** 参数中(key=*YOUR_API_KEY)*。


The **sensor** 参数是必须的，该参数用于指明应用程序是否使用一个传感器 (类似 GPS 导航) 来定位用户的位置。参数值可以设置为 true 或者 false。


**HTTPS**


如果你的应用是安全的HTTP(HTTPS:HTTP Secure)应用,你可以使用 HTTPS 来加载 Google 地图 API：


<script src="https://maps.googleapis.com/maps/api/js?key=***YOUR_API_KEY***&sensor=***TRUE_OR_FALSE***"></script>


**异步加载**


同样我们也可以在页面完全载入后再加载 Google 地图 API。


以下实例使用了 window.onload 来实现页面完全载入后加载 Google 地图 。 loadScript() 函数创建了加载 Google 地图 API  标签。此外在标签的末尾添加了 callback=initialize 参数， initialize()作为回调函数会在API完全载入后执行：


## 实例


```
function loadScript()
{
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBzE9xAESye6Kde-3hT-6B90nfwUkcS8Yw&sensor=false&callback=initialize";
  document.body.appendChild(script);
}

window.onload = loadScript;
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_async)


---


## 定义地图属性


在初始化地图前，我们需要先创建一个 Map 属性对象来定义一些地图的属性：


var mapProp = {

  center:new google.maps.LatLng(51.508742,-0.120850),

  zoom:7,

  mapTypeId: google.maps.MapTypeId.ROADMAP

};


center（中心点）**


中心属性指定了地图的中心，该中心通过坐标（纬度，经度）在地图上创建一个中心点。


**Zoom（缩放级数）**


zoom 属性指定了地图的 缩放级数。zoom: 0 显示了整个地球地图的完全缩放。


**MapTypeId（地图的初始类型）**


mapTypeId 属性指定了地图的初始类型。


mapTypeId包括如下四种类型：


- google.maps.MapTypeId.HYBRID：显示卫星图像的主要街道透明层
- google.maps.MapTypeId.ROADMAP：显示普通的街道地图
- google.maps.MapTypeId.SATELLITE：显示卫星图像
- google.maps.MapTypeId.TERRAIN：显示带有自然特征（如地形和植被）的地图


---


## 在哪里显示 Google 地图


通常 Google 地图使用于  元素中：


<div id="googleMap" style="width:500px;height:380px;"></div>

**注意：** 地图将以div中设置的大小来显示地图的大小，所以我们可以在  元素中设置地图的大小。


---


## 创建一个 Map 对象


var map=new google.maps.Map(document.getElementById("googleMap")**
,mapProp);

以上代码使用参数(mapProp)在 元素 (id为googleMap) 创建了一个新的地图。


提示：**如果想在页面中创建多个地图，你只需要添加新的地图对象即可。


以下实例定义了四个地图实例 (四个地图使用了不同的地图类型):


## 实例


```
var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
var map2 = new google.maps.Map(document.getElementById("googleMap2"),mapProp2);
var map3 = new google.maps.Map(document.getElementById("googleMap3"),mapProp3);
var map4 = new google.maps.Map(document.getElementById("googleMap4"),mapProp4);
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_map_many)


---


## 加载地图


窗口载入后通过执行 initialize() 函数来初始化 Map 对象，这样可以确保在页面完全载入后再加载 Google 地图：


google.maps.event.addDomListener(window, 'load', initialize);







	  AI 思考中...





			** [Google 地图 API](https://www.runoob.com/google-maps-api-key.html)
			[Google 地图叠加层](https://www.runoob.com/google-maps-overlays.html) **













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