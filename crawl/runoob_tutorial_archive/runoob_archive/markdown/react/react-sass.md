# React Sass

- Source: https://www.runoob.com/react/react-sass.html

Sass（Syntactically Awesome Stylesheets）是一种 CSS 预处理器。

Sass 允许你使用 CSS 中尚不存在的特性，比如变量、嵌套规则、混入、函数等等。


Sass 文件在服务器上执行，并将生成的 CSS 发送到浏览器。


你可以在我们的 [Sass 教程](https://www.runoob.com/../sass/sass-tutorial.html) 中了解更多关于 Sass 的信息。


### 安装 Sass

在终端中运行以下命令来安装 Sass：


```
npm i sass
```


现在你已经准备好在项目中包含 Sass 文件了！


### 创建一个 Sass 文件

创建 Sass 文件的方式与创建 CSS 文件相同，但 Sass 文件的扩展名是 **.scss**。

在 Sass 文件中，你可以使用变量和其他 Sass 功能。


### 实例例


创建一个变量来定义文本的颜色：


my-sass.scss 文件代码：


## my-sass.scss


```javascript
$myColor: red;

h1 {
  color: $myColor;
}
```


像导入 CSS 文件一样导入 Sass 文件：


## 实例


```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import './my-sass.scss';

const Header = () => {
  return (
    <>
      <h1>Hello Style!</h1>
      <p>Add a little style!.</p>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Header />);
```


以上代码中，我们创建了一个 Sass 文件 `my-sass.scss`，并在其中使用了 Sass 变量 `$myColor` 来定义 `h1` 的颜色。然后，我们在 `index.js` 中像导入普通 CSS 文件一样导入了这个 Sass 文件，并在 `Header` 组件中使用了这些样式。








	  AI 思考中...





			** [React 使用 CSS 样式](https://www.runoob.com/react-css.html)
			[React Tailwind CSS](https://www.runoob.com/react-tailwind.html) **













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