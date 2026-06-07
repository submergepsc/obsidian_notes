# CSS 图像拼合技术

- Source: https://www.runoob.com/css/css-image-sprites.html

---


## 图像拼合


图像拼合就是单个图像的集合。


有许多图像的网页可能需要很长的时间来加载和生成多个服务器的请求。


使用图像拼合会降低服务器的请求数量，并节省带宽。


---


## 图像拼合 - 简单实例


与其使用三个独立的图像，不如我们使用这种单个图像（"img_navsprites.gif"）：


![navigation images](https://www.runoob.com/images/img_navsprites.gif)


有了CSS，我们可以只显示我们需要的图像的一部分。


在下面的例子CSS指定显示 "img_navsprites.gif" 的图像的一部分：


## 实例


```css
img.home
{
width:46px;
height:44px;
background:url(img_navsprites.gif) 0 0;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_sprites_img)


实例解析：**


- ![](https://www.runoob.com/img_trans.gif) -因为不能为空,src属性只定义了一个小的透明图像。显示的图像将是我们在CSS中指定的背景图像
- 宽度：46px;高度：44px; - 定义我们使用的那部分图像
- background:url(img_navsprites.gif) 0 0; - 定义背景图像和它的位置（左0px，顶部0px）


这是使用图像拼合最简单的方法，现在我们使用链接和悬停效果。


---


## 图像拼合 - 创建一个导航列表


我们想使用拼合图像 ("img_navsprites.gif")，以创建一个导航列表。


我们将使用一个HTML列表，因为它可以链接，同时还支持背景图像：


## 实例


```css
#navlist{position:relative;}
#navlist li{margin:0;padding:0;list-style:none;position:absolute;top:0;}
#navlist li, #navlist a{height:44px;display:block;}
#home{left:0px;width:46px;}
#home{background:url('img_navsprites.gif') 0 0;}
#prev{left:63px;width:43px;}
#prev{background:url('img_navsprites.gif') -47px 0;}
#next{left:129px;width:43px;}
#next{background:url('img_navsprites.gif') -91px 0;}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_sprites_nav)


实例解析：**


- #navlist{position:relative;} - 位置设置相对定位，让里面的绝对定位
- #navlist li{margin:0;padding:0;list-style:none;position:absolute;top:0;} - margin和padding设置为0，列表样式被删除，所有列表项是绝对定位
- #navlist li, #navlist a{height:44px;display:block;} - 所有图像的高度是44px


现在开始每个具体部分的定位和样式：


- #home{left:0px;width:46px;} - 定位到最左边的方式，以及图像的宽度是46px
- #home{background:url(img_navsprites.gif) 0 0;} - 定义背景图像和它的位置（左0px，顶部0px）
- #prev{left:63px;width:43px;} - 右侧定位63px（＃home宽46px+项目之间的一些多余的空间），宽度为43px。
- #prev{background:url('img_navsprites.gif') -47px 0;} - 定义背景图像右侧47px（＃home宽46px+分隔线的1px）
- #next{left:129px;width:43px;}- 右边定位129px(#prev 63px + #prev宽是43px + 剩余的空间), 宽度是43px.
- #next{background:url('img_navsprites.gif') no-repeat -91px 0;} - 定义背景图像右边91px（＃home 46px+1px的分割线+＃prev宽43px+1px的分隔线）


---


## 图像拼合s - 悬停效果


现在，我们希望我们的导航列表中添加一个悬停效果。


|  | :hover 选择器用于鼠标悬停在元素上的显示的效果提示： :hover 选择器可以运用于所有元素。 |
| --- | --- |


我们的新图像 ("img_navsprites_hover.gif") 包含三个导航图像和三幅图像：


![navigation images](https://www.runoob.com/images/img_navsprites_hover.gif)


因为这是一个单一的图像，而不是6个单独的图像文件，当用户停留在图像上不会有延迟加载。


我们添加悬停效果只添加三行代码：


## 实例


```css
#home a:hover{background: url('img_navsprites_hover.gif') 0 -45px;}
#prev a:hover{background: url('img_navsprites_hover.gif') -47px
-45px;}
#next a:hover{background: url('img_navsprites_hover.gif') -91px
-45px;}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_sprites_hover_nav)


实例解析：**


- 由于该列表项包含一个链接，我们可以使用：hover伪类
- #home a:hover{background: transparent url(img_navsprites_hover.gif) 0 -45px;} - 对于所有三个悬停图像，我们指定相同的背景位置，只是每个再向下45px









	  AI 思考中...





			** [CSS 图像透明/不透明](https://www.runoob.com/css-image-transparency.html)
			[CSS 媒体类型](https://www.runoob.com/css-mediatypes.html) **













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