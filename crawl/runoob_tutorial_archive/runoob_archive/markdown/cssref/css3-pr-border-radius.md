# CSS3 border-radius 属性

- Source: https://www.runoob.com/cssref/css3-pr-border-radius.html

菜鸟教程(runoob.com)

**
## 实例


给两个 div 元素添加圆角的边框：


```css
#example1 {
  border: 2px solid red;
  border-radius: 25px;
}

#example2 {
  border: 2px solid red;
  border-radius: 50px 20px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_border-radius)


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


紧跟在 -webkit-, -ms- 或 -moz- 前的数字为支持该前缀属性的第一个浏览器版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| border-radius | 4.0 -webkit- | 9.0 | 4.0 -moz- | 5.0 -webkit- | 10.5 -o- |


---


## 属性定义及使用说明

border-radius 允许你设置元素的外边框圆角。当使用一个半径时确定一个圆形，当使用两个半径时确定一个椭圆。这个(椭)圆与边框的交集形成圆角效果。


border-radius 属性是一个最多可指定四个 **border-*-radius** 属性的复合属性


提示：** 这个属性允许你为元素添加圆角边框！


| 默认值: | 0 |
| --- | --- |
| 继承: | no |
| 版本: | CSS3 |
| JavaScript 语法: | object object.style.borderRadius="5px" |

**
---


## 语法


border-radius: *1-4 length*|*%* / *1-4 length*|*%*;

注意:** 每个半径的四个值的顺序是：左上角，右上角，右下角，左下角。如果省略左下角，右上角是相同的。如果省略右下角，左上角是相同的。如果省略右上角，左上角是相同的。


| 值 | 描述 |
| --- | --- |
| length | 定义弯道的形状。 |
| % | 使用%定义角落的形状。 |


```css
border-radius: 1em/5em;

/* 等价于： */

border-top-left-radius:     1em 5em;
border-top-right-radius:    1em 5em;
border-bottom-right-radius: 1em 5em;
border-bottom-left-radius:  1em 5em;
```




```css
border-radius: 4px 3px 6px / 2px 4px;

/* 等价于： */

border-top-left-radius:     4px 2px;
border-top-right-radius:    3px 4px;
border-bottom-right-radius: 6px 2px;
border-bottom-left-radius:  3px 4px;
```

**

椭圆边框 -** **border-radius: 15px 50px 30px 5px**：第一个值适用于左上角，第二个值适用于右上角，第三个值适用于右下角，第四个值适用于左下角：


**

椭圆边框 -** **border-radius: 15px 50px 30px**：第一个值适用于左上角，第二个值适用于右上角和左下角，第三个值适用于右下角：


**

椭圆边框 -** **border-radius: 15px 50px**：第一个值适用于左上角和右下角，第二个值适用于右上角和左下角


**

椭圆边框 -** **border-radius: 15px**：该值适用于所有四个角，均等圆角


**


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_border-radius6)


---


## 更多实例

## 实例


背景图带边框：


```css
#rcorners3 {
  border-radius: 25px;
  background: url(paper.gif);
  background-position: left top;
  background-repeat: repeat;
  padding: 20px;
  width: 200px;
  height: 150px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_border-radius4)


## 实例


不同类型参数：


```css
#rcorners7 {
    border-radius: 50px/15px;
    background: #8AC007;
    padding: 20px;
    width: 200px;
    height: 150px;
}
#rcorners8 {
    border-radius: 15px/50px;
    background: #8AC007;
    padding: 20px;
    width: 200px;
    height: 150px;
}

#rcorners9 {
    border-radius: 50%;
    background: #8AC007;
    padding: 20px;
    width: 200px;
    height: 150px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_border-radius3)


## 实例


不同参数个数：


```css
#rcorners4 {
    border-radius: 15px 50px 30px 5px;
    padding: 20px;
    width: 200px;
    height: 150px;
}

#rcorners5 {
    border-radius: 15px 50px 30px;
    padding: 20px;
    width: 200px;
    height: 150px;
}

#rcorners6 {
    border-radius: 15px 50px;
    padding: 20px;
    width: 200px;
    height: 150px;
}

#rcorners7 {
    border-radius: 15px;
    padding: 20px;
    width: 200px;
    height: 150px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_border-radius6)


## 实例


简写格式：


```css
#example1 {
  border-radius: 2em / 5em;
}
/* 等价于:
border-top-left-radius: 2em 5em;
border-top-right-radius: 2em 5em;
border-bottom-right-radius: 2em 5em;
border-bottom-left-radius: 2em 5em; */

#example2 {
  border-radius: 2em 1em 4em / 0.5em 3em;
}
/* 等价于:
border-top-left-radius: 2em 0.5em;
border-top-right-radius: 1em 3em;
border-bottom-right-radius: 4em 0.5em;
border-bottom-left-radius: 1em 3em; */
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_border-radius5)


---


## 相关文章


CSS3 教程: [CSS3 边框](https://www.runoob.com/../css3/css3-borders.html)








	  AI 思考中...





			** [CSS3 border-top-left-radius 属性](https://www.runoob.com/css3-pr-border-top-left-radius.html)
			[CSS3 border-image-width 属性](https://www.runoob.com/css3-pr-border-image-width.html) **













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