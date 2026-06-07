# CSS 听觉参考手册

- Source: https://www.runoob.com/cssref/css-ref-aural.html

---


听觉样式表使用了语音合成和声音效果的结合，让用户收听信息，而不是读取信息。


有声显示可用于：


- 失明人士
- 帮助用户学习阅读
- 帮助具有阅读问题的用户
- 家庭娱乐
- 在车上


听觉呈现通常会把文档转化为纯文本，然后传给屏幕阅读器（可读出屏幕上所有字符的一种程序）。


听觉样式表的一个例子：


## 实例


```css
h1,h2,h3,h4
{
    voice-family:male;
    richness:80;
    cue-before:url("beep.au")
}
```


上面的例子用语音合成器播放声音，开头有一个男性的声音说话。

**
---


## CSS 听觉参考手册


CSS"列表示在CSS版本的属性定义（CSS1或CSS2）。


| Property | Description | Values | CSS |
| --- | --- | --- | --- |
| azimuth | 设置声音应该来自哪里 | angle left-side far-left left center-left center center-right right far-right right-side behind leftwards rightwards | 2 |
| cue | 在一个声明中设置cue属性 | cue-before cue-after | 2 |
| cue-after | 指定要播放的声音在一个元素的内容后面 | none url | 2 |
| cue-before | 指定要播放的声音在一个元素的内容前面 | none url | 2 |
| elevation | 设置声音应该来自哪里 | angle below level above higher lower | 2 |
| pause | 在一个声明中设置pause属性 | pause-before pause-after | 2 |
| pause-after | 在一个元素的内容之后，指定暂停 | time % | 2 |
| pause-before | 在一个元素的内容之前，指定暂停 | time % | 2 |
| pitch | 指定讲话声音 | frequency x-low low medium high x-high | 2 |
| pitch-range | 指定讲话声音的变化。（单调的声音或动态的声音？） | number | 2 |
| play-during | 指定在读一个元素的内容时要播放的声音 | auto none url mix repeat | 2 |
| richness | 指定丰富的讲话声音。（浑厚的声音或细的声音？） | number | 2 |
| speak | 指定内容是否会提供听觉方式 | normal none spell-out | 2 |
| speak-header | 此属性设置或检索表格标题是在所有的单元格之前发声，还是到一个不与之关联的单元格就结束发声。 | always once | 2 |
| speak-numeral | 设置或检索数字如何发音。 | digits continuous | 2 |
| speak-punctuation | 设置或检索标点字符如何发音 | none code | 2 |
| speech-rate | 指定发言速度 | number x-slow slow medium fast x-fast faster slower | 2 |
| stress | 讲话声音在指定的地方"重音" | number | 2 |
| voice-family | 设置或检索当前声音类型 | specific-voice generic-voice | 2 |
| volume | 指定发言的音量 | number % silent x-soft soft medium loud x-loud | 2 |








	  AI 思考中...





			** [CSS 选择器](https://www.runoob.com/css-selectors.html)
			[CSS Web安全字体](https://www.runoob.com/css-websafe-fonts.html) **













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