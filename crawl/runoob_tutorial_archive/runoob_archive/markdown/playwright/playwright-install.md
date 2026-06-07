# Playwright 安装

- Source: https://www.runoob.com/playwright/playwright-install.html

Playwright 是一个 Node.js 库，所以需要我们本地安装 Node.js，如果你已经安装了可以跳过。


### 1、安装 Node.js


Playwright 官方推荐使用 Node.js。


- 打开 [Node.js 官网](https://nodejs.org/)
- 下载并安装 **LTS（长期支持版）**
- 验证是否安装成功：
```
node -v
npm -v
```
 能看到版本号即可。

更多安装可以参考：[https://www.runoob.com/nodejs/nodejs-install-setup.html](https://www.runoob.com/../nodejs/nodejs-install-setup.html)


### 2、新建项目目录

如果成功安装 node，我们就可以开始 Playwright 的安装与使用。


在命令行执行：


```
mkdir runoob-playwright-demo
cd runoob-playwright-demo
```


### 3、初始化并安装 Playwright


执行：


```
npm init playwright@latest
```


安装过程会提示：


- 选择语言：**JavaScript** 或 **TypeScript**，熟悉哪个选哪个
- 是否要安装测试示例：推荐选 **Yes**（方便学习）
- 是否下载浏览器：选 **Yes**（Playwright 会下载 Chromium、Firefox、WebKit 三大引擎）


![](https://www.runoob.com/wp-content/uploads/2025/08/a47c0697-39d3-4ee7-bbd0-be5408c54f00.png)


安装完成后，你的项目目录大概长这样：


```
playwright-demo/
├─ tests/                # 示例测试用例
├─ playwright.config.js  # 配置文件
├─ package.json
└─ node_modules/
```


![](https://www.runoob.com/wp-content/uploads/2025/08/30482798-ee60-482b-8022-18d775edb24e.png)


---


## 第一个脚本：Hello World


新建一个 `test.js` 文件，写入以下内容：


## 实例


```javascript
// test.js
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
node test.js
```


以上是一个 Playwright 的简单实例，可以截图百度的首页。


![](https://www.runoob.com/wp-content/uploads/2025/08/85ab2da6-effe-4d60-a4a1-2faa6f49ed31.png)








	  AI 思考中...





			** [Playwright 简介](https://www.runoob.com/playwright-intro.html)
			[Playwright 开发环境配置](https://www.runoob.com/playwright-setup.html) **













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