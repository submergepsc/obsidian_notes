# Playwright 教程

- Source: https://www.runoob.com/playwright/playwright-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2025/08/68149f0271ec27bc6d3118eb_1_gMiUPuRGC36nxZHe2zthOg.png)

Playwright 是微软（Microsoft） 在 2020 年推出的一个开源项目，用于 Web 自动化和端到端（End-to-End）测试的开源框架。


Playwright支持多种浏览器（Chromium、Firefox 和 WebKit）和多种编程语言（JavaScript/TypeScript、Python、Java 和 .NET），旨在提供可靠、快速且功能丰富的自动化测试解决方案。


---


## 学习 Playwright 需要的基础知识？


学习 Playwright 前，掌握这几样就够了：


- **会点 [JavaScript](https://www.runoob.com/../js/js-tutorial.html)**，尤其是 `[async/await](https://www.runoob.com/../js/js-async-await.html)`；
- **会用 [Node.js](https://www.runoob.com/../nodejs/nodejs-tutorial.html) 和 [npm](https://www.runoob.com/../nodejs/nodejs-npm.html)** 来运行脚本；
- **懂点 [HTML](https://www.runoob.com/../html/html-tutorial.html) 和选择器**（比如 `#id`、`.class`）；
- **能用终端** 跑命令。


要不要我帮你把这几句话做成一张 **新手清单式配图**？


---


## Playwright 能干什么？


用一句话总结：只要人能在浏览器里点的，Playwright 几乎都能自动化完成。


比如：


- 点击按钮
- 填写表单
- 导航到不同的页面
- 截图和保存网页内容


---


## Playwright 简单实例

以下是一个 Playwright 的简单实例，可以截图百度的首页：


## 实例


```javascript
// hello.js
const { chromium } = require('playwright');

(async () => {
  // 1. 启动浏览器
  const browser = await chromium.launch({ headless: false }); // 设置 false 可以看到浏览器
  const page = await browser.newPage();

  // 2. 打开网页
  await page.goto('https://www.baidu.com');

  // 3. 截图保存
  await page.screenshot({ path: 'baidu.png' });

  // 4. 关闭浏览器
  await browser.close();

  console.log("截图已保存到 example.png");
})();
```


运行：


```
node hello.js
```


浏览器会自动输入两条待办事项，并保存截图。


---

## 相关链接


- Playwright 官网：[https://playwright.dev/](https://playwright.dev/)
- Playwright 开源地址：[https://github.com/microsoft/playwright](https://github.com/microsoft/playwright)
- Playwright API 文档：[https://playwright.dev/docs/api/class-playwright/](https://playwright.dev/docs/api/class-playwright/)










	  AI 思考中...






			[Playwright 简介](https://www.runoob.com/playwright-intro.html) **













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