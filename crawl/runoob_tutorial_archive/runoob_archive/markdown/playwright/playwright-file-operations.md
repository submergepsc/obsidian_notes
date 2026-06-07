# Playwright 文件操作

- Source: https://www.runoob.com/playwright/playwright-file-operations.html

虽然 Playwright 主要是做浏览器自动化的，但它在**文件上传和下载**方面也很强大，可以轻松应对前端常见的文件交互场景。

---


## 文件上传


在 Web 表单中，文件上传通常通过 `` 完成。Playwright 提供了专门的 API 来处理：


### 方法一：setInputFiles()


```
await page.setInputFiles('input[type="file"]', 'tests/fixtures/avatar.png');
```


- **参数说明**： 选择器：文件选择框的定位方式。
- 文件路径：相对/绝对路径，支持单文件或多文件数组。


    如果传入 `[]`，表示清空已选择的文件。


### 方法二：直接通过 Locator


```
const upload = page.locator('input[type=file]');
await upload.setInputFiles(['tests/fixtures/1.png', 'tests/fixtures/2.png']);
```


### 方法三：模拟拖拽上传（部分应用支持）


```
const fileChooserPromise = page.waitForEvent('filechooser');
await page.click('button#upload'); // 触发选择文件
const fileChooser = await fileChooserPromise;
await fileChooser.setFiles('tests/fixtures/test.pdf');
```


---


## 文件下载


Playwright 可以捕获浏览器下载事件，并获取文件保存路径。


### 基本用法：监听下载


## 实例


```javascript
const [download] = await Promise.all([
  page.waitForEvent('download'),          // 等待下载开始
  page.click('a#downloadButton'),         // 触发下载
]);

// 保存文件到指定路径
await download.saveAs('downloads/report.pdf');

// 获取默认保存路径（系统临时目录）
const path = await download.path();
console.log('下载路径:', path);

// 获取下载信息
console.log(await download.url());        // 下载链接
console.log(await download.suggestedFilename()); // 推荐文件名
```


---


## 截图与录屏文件


Playwright 本身也会生成文件（截图、视频、trace 等）：


```
await page.screenshot({ path: 'screenshots/home.png', fullPage: true });
await page.video()?.saveAs('videos/test.mp4');  // 在配置中开启 video 记录才可用
```


---


## 文件操作完整示例


## 实例


```javascript
import { test, expect } from '@playwright/test';

test('文件上传与下载示例', async ({ page }) => {
  // 上传文件
  await page.goto('https://the-internet.herokuapp.com/upload');
  const uploadInput = page.locator('input[type=file]');
  await uploadInput.setInputFiles('tests/fixtures/avatar.png');
  await page.click('#file-submit');
  await expect(page.locator('#uploaded-files')).toHaveText('avatar.png');

  // 下载文件
  await page.goto('https://the-internet.herokuapp.com/download');
  const [download] = await Promise.all([
    page.waitForEvent('download'),
    page.click('a[href="some-file.txt"]'),
  ]);
  await download.saveAs('downloads/some-file.txt');
  console.log('下载完成:', await download.suggestedFilename());
});
```


---


## 文件操作 API


| API | 用途 | 参数/说明 |
| --- | --- | --- |
| page.setInputFiles(selector, files) | 上传文件 | files 可为路径字符串、数组或 FilePayload |
| locator.setInputFiles(files) | 上传文件（Locator 方式） |  |
| page.waitForEvent('filechooser') | 等待文件选择对话框 | 返回 FileChooser |
| fileChooser.setFiles(files) | 设置选择的文件 |  |
| page.waitForEvent('download') | 监听下载事件 | 返回 Download |
| download.saveAs(path) | 保存下载文件 | 自定义存储位置 |
| download.path() | 获取系统默认存储路径 |  |
| download.url() | 获取下载请求的 URL |  |
| download.suggestedFilename() | 获取推荐文件名 |  |
| page.screenshot({ path }) | 页面截图 |  |
| locator.screenshot({ path }) | 元素截图 |  |
| page.video()?.saveAs(path) | 保存录制视频 | 需配置开启 video |








	  AI 思考中...





			** [Playwright 网络拦截](https://www.runoob.com/playwright-network-interception.html)
			[Playwright 移动端测试](https://www.runoob.com/playwright-mobile-test.html) **













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