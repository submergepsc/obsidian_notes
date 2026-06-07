# Playwright 网络拦截

- Source: https://www.runoob.com/playwright/playwright-network-interception.html

Playwright 的网络拦截 (Network Interception) 是自动化测试和爬虫场景中非常有用的能力，可以让我们拦截、修改、模拟网络请求与响应。


Playwright 提供了 `page.route()` 和 `page.on('request')` / `page.on('response')` 等 API，可以：


- **拦截请求**：决定是否放行、修改 URL/headers/body、或者直接返回 mock 响应。
- **监听请求/响应**：查看请求的 URL、方法、头部、响应状态码、响应体等。
- **模拟网络错误**：阻止请求、返回错误码，测试应用的容错逻辑。


常见应用场景：


- **Mock API**：不用后端接口也能跑前端 UI 测试。
- **修改请求**：比如加 token，测试异常 header。
- **性能调试**：统计请求数、响应时间。
- **错误注入**：模拟 500/404 等服务端异常。


### 拦截请求：page.route()


```
await page.route('**/api/todos', async route => {
  // 拦截匹配的请求
  console.log('拦截到请求:', route.request().url());

  // 1. 直接放行（继续请求）
  await route.continue();

  // 2. 修改请求
  // await route.continue({ headers: { ...route.request().headers(), 'X-Test': 'true' } });

  // 3. 返回 mock 响应
  // await route.fulfill({
  //   status: 200,
  //   contentType: 'application/json',
  //   body: JSON.stringify([{ id: 1, text: 'mock todo', done: false }]),
  // });

  // 4. 拒绝请求
  // await route.abort();
});
```


**参数说明**：


- `page.route(url, handler)`：注册一个拦截器，`url` 支持字符串、正则或 `**` 通配。
- `route.request()`：获取请求对象。
- `route.continue([options])`：放行请求，可以修改方法、headers、postData。
- `route.fulfill(response)`：直接返回伪造的响应。
- `route.abort([errorCode])`：中断请求，常见错误码如 `"failed"`, `"aborted"`, `"timedout"`。


### 监听请求和响应


```
// 监听所有请求
page.on('request', req => {
  console.log(`&#x27a1;&#xfe0f; 请求: ${req.method()} ${req.url()}`);
});

// 监听所有响应
page.on('response', async res => {
  console.log(`&#x2b05;&#xfe0f; 响应: ${res.status()} ${res.url()}`);
});

// 获取响应 body
const response = await page.waitForResponse('**/api/data');
console.log('响应内容:', await response.text());
```


**常用方法**：


- `request.url()` / `request.method()` / `request.headers()` / `request.postData()`
- `response.status()` / `response.headers()` / `response.text()` / `response.json()`


### 模拟网络环境


## 实例


```javascript
// 模拟网络错误
await page.route('**/*.png', route => route.abort('failed'));

// 模拟延迟
await page.route('**/api/**', async route => {
  await new Promise(r => setTimeout(r, 2000));
  await route.continue();
});
</pre>
<hr>
<h2>完整示例：Mock API</h2>
import { test, expect } from '@playwright/test';

test('拦截并 mock API', async ({ page }) => {
  // 拦截 /api/todos 请求并返回固定数据
  await page.route('**/api/todos', async route => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify([
        { id: 1, text: 'Playwright 学习', done: false },
        { id: 2, text: '写自动化测试', done: true },
      ]),
    });
  });

  await page.goto('https://example-todo-app.com');
  const items = await page.locator('.todo-item').allTextContents();
  console.log('加载到的待办事项:', items);

  // 断言 UI 显示 mock 数据
  await expect(page.locator('.todo-item')).toHaveCount(2);
  await expect(page.locator('.todo-item').first()).toContainText('Playwright 学习');
});
```


---


## 网络拦截相关 API


| API | 用途 | 常见参数/说明 |
| --- | --- | --- |
| page.route(url, handler) | 注册请求拦截 | url 可为字符串/正则/通配符 |
| route.request() | 获取请求对象 | 返回 Request |
| route.continue([options]) | 放行请求，可修改 | { method, headers, postData } |
| route.fulfill(response) | 返回自定义响应 | { status, headers, body, contentType } |
| route.abort([errorCode]) | 中断请求 | 常见：'failed', 'aborted', 'timedout' |
| page.unroute(url, handler?) | 移除拦截规则 |  |
| page.on('request', cb) | 监听请求 |  |
| page.on('response', cb) | 监听响应 |  |
| request.url()/method()/headers()/postData() | 请求信息 |  |
| response.status()/headers()/text()/json() | 响应信息 |  |
| page.waitForResponse(urlOrPredicate) | 等待特定响应 | 可传 URL 或函数 |








	  AI 思考中...





			** [Playwright Test](https://www.runoob.com/playwright-test.html)
			[Playwright 文件操作](https://www.runoob.com/playwright-file-operations.html) **













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