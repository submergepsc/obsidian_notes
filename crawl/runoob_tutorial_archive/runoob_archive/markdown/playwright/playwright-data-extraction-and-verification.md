# Playwright 数据提取和验证

- Source: https://www.runoob.com/playwright/playwright-data-extraction-and-verification.html

数据提取和验证是自动化测试的关键，主要包括 **获取页面数据、断言验证、截图和录制**，不仅能验证功能是否正确，还能辅助调试和回归测试。


## 元素信息获取


在测试中经常需要读取页面信息进行验证，Playwright 提供了丰富的 API。


### 1. 获取文本内容


## 实例


```javascript
// 获取单个元素的文本
const text = await page.textContent('#welcome');
console.log(text);

// 获取多个元素的文本
const items = await page.$$eval('.list-item', els => els.map(e => e.textContent));
console.log(items);
```


### 2. 获取属性值


```
const value = await page.getAttribute('#username', 'placeholder');
console.log(value); // "请输入用户名"
```


### 3. 获取样式信息


```
// 获取元素的 style 属性
const color = await page.$eval('#btn', el => getComputedStyle(el).color);
console.log(color);
```


### 4. 元素状态检查


```
await page.isVisible('#dialog');   // 是否可见
await page.isHidden('#loading');   // 是否隐藏
await page.isEnabled('#submit');   // 是否可用
await page.isDisabled('#submit');  // 是否禁用
await page.isChecked('#agree');    // 复选框是否选中
```


---


## 断言和验证


Playwright 提供了 **内置断言库**（`[@playwright](https://github.com/playwright)/test`），便于编写测试用例。


### 1. 内置断言方法


在 `[@playwright](https://github.com/playwright)/test` 中，使用 `expect` 进行断言。


## 实例


```javascript
import { test, expect } from '@playwright/test';

test('验证示例', async ({ page }) => {
  await page.goto('https://example.com');

  // 文本断言
  await expect(page.locator('h1')).toHaveText('Example Domain');

  // 属性断言
  await expect(page.locator('a')).toHaveAttribute('href', 'https://www.iana.org/domains/example');

  // 可见性断言
  await expect(page.locator('h1')).toBeVisible();
});
```


### 2. 文本内容验证


```
await expect(page.locator('#message')).toHaveText('登录成功');
await expect(page.locator('#username')).toHaveValue('testuser');
```


### 3. 元素状态验证


```
await expect(page.locator('#submit')).toBeEnabled();
await expect(page.locator('#agree')).toBeChecked();
await expect(page.locator('#loading')).toBeHidden();
```


### 4. 页面标题和 URL 验证


```
await expect(page).toHaveTitle(/Playwright/);
await expect(page).toHaveURL('https://playwright.dev/');
```


---


## 截图和录制


截图与录制在调试、失败用例分析和回归测试中非常有用。


### 1. 页面截图


```
await page.screenshot({ path: 'screenshot.png', fullPage: true });
```


- `path`: 保存路径
- `fullPage`: 是否截取整个页面


### 2. 元素截图


```
const element = page.locator('#logo');
await element.screenshot({ path: 'logo.png' });
```


### 3. 视频录制


在创建 `context` 时启用录制：


```
const context = await browser.newContext({
  recordVideo: { dir: 'videos/' }
});
const page = await context.newPage();
await page.goto('https://example.com');
await context.close(); // 关闭后保存视频
```


### 4. 截图对比（快照测试）


Playwright 支持快照对比，常用于回归测试。


```
import { test, expect } from '@playwright/test';

test('页面快照测试', async ({ page }) => {
  await page.goto('https://playwright.dev');
  expect(await page.screenshot()).toMatchSnapshot('homepage.png');
});
```


会将截图与基准图像 `homepage.png` 对比，检测 UI 变化。


好的 ✅ 那我来为 **第六章：数据提取和验证** 补充一个 **完整实战案例**，并整理出 **API 对照表**。这样你就能既有实战，又能快速查表。


---


## 实战案例 —— 登录验证与截图快照


这个案例涵盖了：**信息提取 + 断言验证 + 页面截图**。


## 实例


```javascript
// login-test.spec.js
import { test, expect } from '@playwright/test';

test('用户登录并验证结果', async ({ page }) => {
  // 1. 打开登录页面
  await page.goto('https://example.com/login');

  // 2. 输入用户名和密码
  await page.fill('#username', 'testuser');
  await page.fill('#password', 'Password123');

  // 3. 点击登录
  await page.click('#submit');

  // 4. 等待跳转并检查标题
  await expect(page).toHaveTitle(/Dashboard/);

  // 5. 验证欢迎文本
  await expect(page.locator('.welcome')).toHaveText('欢迎，testuser');

  // 6. 检查按钮状态
  await expect(page.locator('#logout')).toBeVisible();
  await expect(page.locator('#logout')).toBeEnabled();

  // 7. 获取用户 ID 属性并验证
  const userId = await page.getAttribute('#user-profile', 'data-id');
  console.log('用户ID:', userId);
  expect(userId).not.toBeNull();

  // 8. 页面截图
  await page.screenshot({ path: 'login-success.png', fullPage: true });

  // 9. 快照对比（UI 回归测试）
  expect(await page.screenshot()).toMatchSnapshot('dashboard.png');
});
```


这个测试会验证：


- 页面标题和欢迎文本是否正确
- 元素是否可见 / 可用
- 用户信息属性是否存在
- 页面截图和 UI 快照对比


---


## 常用 API 表格


下面是 **数据提取与验证**相关 API 一览表。


| 方法 | 说明 | 示例 |
| --- | --- | --- |
| page.textContent(selector) | 获取元素文本内容 | await page.textContent('#msg') |
| page.innerText(selector) | 获取渲染后的纯文本 | await page.innerText('#msg') |
| page.innerHTML(selector) | 获取元素 HTML | await page.innerHTML('#content') |
| page.getAttribute(selector, name) | 获取属性值 | await page.getAttribute('#btn', 'class') |
| page.$eval(selector, fn) | 在元素上执行函数 | await page.$eval('#logo', el => el.tagName) |
| page.$$eval(selector, fn) | 批量执行函数 | await page.$$eval('.item', els => els.length) |
| page.isVisible(selector) | 是否可见 | await page.isVisible('#dialog') |
| page.isHidden(selector) | 是否隐藏 | await page.isHidden('#loading') |
| page.isEnabled(selector) | 是否启用 | await page.isEnabled('#submit') |
| page.isDisabled(selector) | 是否禁用 | await page.isDisabled('#submit') |
| page.isChecked(selector) | 是否选中 | await page.isChecked('#agree') |


### 断言与验证（@playwright/test）


| 方法 | 说明 | 示例 |
| --- | --- | --- |
| expect(locator).toHaveText(value) | 验证文本 | expect(page.locator('h1')).toHaveText('欢迎') |
| expect(locator).toHaveValue(value) | 验证输入框值 | expect(page.locator('#user')).toHaveValue('test') |
| expect(locator).toHaveAttribute(name, value) | 验证属性 | expect(page.locator('#btn')).toHaveAttribute('type', 'submit') |
| expect(locator).toBeVisible() | 元素可见 | expect(page.locator('#msg')).toBeVisible() |
| expect(locator).toBeHidden() | 元素隐藏 | expect(page.locator('#loading')).toBeHidden() |
| expect(locator).toBeEnabled() | 元素启用 | expect(page.locator('#submit')).toBeEnabled() |
| expect(locator).toBeDisabled() | 元素禁用 | expect(page.locator('#submit')).toBeDisabled() |
| expect(locator).toBeChecked() | 元素已选中 | expect(page.locator('#agree')).toBeChecked() |
| expect(page).toHaveTitle(title) | 页面标题验证 | expect(page).toHaveTitle(/Dashboard/) |
| expect(page).toHaveURL(url) | 页面 URL 验证 | expect(page).toHaveURL('https://example.com/dashboard') |


### 截图与录制


| 方法 | 说明 | 示例 |
| --- | --- | --- |
| page.screenshot(options) | 页面截图 | await page.screenshot({ path: 'page.png' }) |
| locator.screenshot(options) | 元素截图 | await page.locator('#logo').screenshot({ path: 'logo.png' }) |
| context = browser.newContext({ recordVideo }) | 开启视频录制 | recordVideo: { dir: 'videos/' } |
| expect(await page.screenshot()).toMatchSnapshot(name) | 截图对比（快照测试） | expect(await page.screenshot()).toMatchSnapshot('home.png') |








	  AI 思考中...





			** [Playwright 高级页面操作](https://www.runoob.com/playwright-advanced-page-operations.html)
			[Playwright Test](https://www.runoob.com/playwright-test.html) **













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