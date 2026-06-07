# CSS 编辑器

- Source: https://www.runoob.com/css/css-editor.html

可以使用专业的 CSS 编辑器来编辑 CSS，为大家推荐几款常用的编辑器：


- VS Code：[https://code.visualstudio.com/](https://code.visualstudio.com/)
- **阿里 Qoder：**[https://qoder.com/](https://qoder.com/users/sign-up?referral_code=whhACoCj9WryAtAh2HAqjvE2ppbzwWtz)
- Sublime Text：[http://www.sublimetext.com/](https://www.sublimetext.com/)
- 在线编辑器：[https://www.jyshare.com/front-end/61/](https://www.jyshare.com/front-end/61/)


你可以从以上软件的官网中下载对应的软件，按步骤安装即可。


接下来我们将为大家演示如何使用 VS Code 工具来创建 CSS 文件。


---

## VS Code


Visual Studio Code（简称 VS Code）是一个由微软开发，同时支持 Windows 、 Linux 和 macOS 等操作系统且开放源代码的代码编辑器，编辑器中内置了扩展程序管理的功能。


VS Code 安装教程参考：[https://www.runoob.com/vscode/vscode-tutorial.html](https://www.runoob.com/../vscode/vscode-tutorial.html)


**安装必备插件 (Extensions):****点击 VS Code 左侧边栏的方块图标（Extensions），搜索并安装以下两个插件，它们对新手至关重要：

- **Live Server:** 允许你在浏览器中实时预览网页，保存代码后浏览器会自动刷新。
- **HTML CSS Support:** 增强 CSS 的智能提示。


![](https://www.runoob.com/wp-content/uploads/2025/12/css-editor-0.png)


### 第一步: 建立项目结构


在你的电脑上创建一个名为 **my-first-css** 的文件夹


在 VS Code 中打开： 点击 VS Code 左上角的 File -> Open Folder...，选择刚才的文件夹。



- 在左侧资源管理器空白处右键，新建文件 index.html (这是网页骨架)。
- 再次右键，新建文件 style.css (这是网页的皮肤)。


![](https://www.runoob.com/wp-content/uploads/2025/12/css-editor-1.png)


### 第二步：编写 HTML 骨架


CSS 必须依附于 HTML 存在，以下是 index.html 文件代码。


在 `` 标签内输入以下代码，并一定要加上 `` 标签来关联 CSS 文件**：


```css
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的 CSS 练习</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="card">
        <h1>Hello, CSS!</h1>
        <p>这是我用 VS Code 写的第一个样式卡片。</p>
        <button>点击我</button>
    </div>

</body>
</html>
```


![](https://www.runoob.com/wp-content/uploads/2025/12/css-editor-2.png)


### 第三步：编写 CSS 样式


在 style.css 文件中输入以下代码:


## 实例


```css
/* 给整个页面加个背景色 */
body {
    background-color: #f0f2f5;
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    justify-content: center; /* 水平居中 */
    align-items: center;     /* 垂直居中 */
    height: 100vh;           /* 占满屏幕高度 */
    margin: 0;
}

/* 设计卡片样式 */
.card {
    background-color: white;
    width: 300px;
    padding: 30px;
    border-radius: 15px;      /* 圆角 */
    box-shadow: 0 4px 15px rgba(0,0,0,0.1); /* 阴影 */
    text-align: center;
}

/* 标题颜色 */
h1 {
    color: #333;
}

/* 按钮样式 */
button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s; /* 动画过渡 */
}

/* 鼠标悬停在按钮上的效果 */
button:hover {
    background-color: #0056b3;
}
```


### 第四步：运行与预览 - 回到 `index.html` 文件。 - 在编辑区任意位置点击 **鼠标右键**。 - 选择 **"Open with Live Server"**。 ![](https://www.runoob.com/wp-content/uploads/2025/12/css-editor-3.png)


此时，你的默认浏览器会自动弹出，你应该能看到一个居中的白色卡片，上面有标题和按钮。当你把鼠标放在按钮上时，颜色会变深。


运行显示结果类似如下:


![](https://www.runoob.com/wp-content/uploads/2025/12/css-editor-4.png)










	  AI 思考中...





			** [CSS AI 编程](https://www.runoob.com/fitten-code-css.html)
			[CSS position: static 属性值](https://www.runoob.com/css-position-static.html) **













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