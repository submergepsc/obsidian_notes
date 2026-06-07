# Vue3 项目打包

- Source: https://www.runoob.com/vue3/vue3-build.html

当你准备将应用发布到生产环境时，就需要打包 Vue 项目。


打包 Vue 项目使用以下命令：


```
npm run build
```


执行以上命令，输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2021/08/BC87CFF3-5FE5-4146-B9CC-48779A04BDA0.jpeg)


执行完成后，会在 Vue 项目下会生成一个 **dist** 目录，该目录一般包含 index.html 文件及 static 目录，static 目录包含了静态文件 js、css 以及图片目录 images（如果有图片的话）。


![](https://www.runoob.com/wp-content/uploads/2021/08/2681A4D7-6268-401E-B958-C9FE7F33B32A.jpg)


如果直接双击打开 index.html，在浏览器中页面可能是空白了，要正常显示则需要修改下 index.html 文件中 js、css 文件路径。

例如我们打开 dist/index.html 文件看到 css 和 js 文件路径是绝对路径：


```
<link href=/static/css/app.33da80d69744798940b135da93bc7b98.css rel=stylesheet>
<script type=text/javascript src=/static/js/app.717bb358ddc19e181140.js></script>
...
```


我们把 js、css 文件路径修改为相对路径：


```
<link href=static/css/app.33da80d69744798940b135da93bc7b98.css rel=stylesheet>
<script type=text/javascript src=static/js/app.717bb358ddc19e181140.js></script>
...
```


这样直接双击 dist/index.html 文件就可以在浏览器中看到效果了。








	  AI 思考中...





			** [Vue3 Ajax(axios)](https://www.runoob.com/vue3-ajax-axios.html)
			[Vue3 创建项目](https://www.runoob.com/vue3-create-project.html) **













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