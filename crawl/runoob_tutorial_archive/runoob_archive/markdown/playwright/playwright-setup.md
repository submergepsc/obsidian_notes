# Playwright 开发环境配置

- Source: https://www.runoob.com/playwright/playwright-setup.html

Playwright 开发推荐用 **[VS Code](https://www.runoob.com/../vscode/vscode-tutorial.html)**，因为它对 JavaScript/TypeScript、调试器、扩展支持都很强大。


## 1. 安装 VS Code


- 前往 [VS Code 官网](https://code.visualstudio.com/) 下载并安装。
- 安装完成后，建议同时装上 **中文语言包**（扩展市场搜索 `Chinese (Simplified)`）。

VS Code 相关内容参考：[https://www.runoob.com/vscode/vscode-tutorial.html](https://www.runoob.com/../vscode/vscode-tutorial.html)


---


## 2. 必备扩展插件


在 VS Code 的扩展（Extensions）面板里，搜索并安装以下插件：


- **Playwright Test for VSCode** - 官方出品的 Playwright 插件 - 功能：运行/调试用例、查看测试报告、录制脚本、生成 trace - 扩展 ID：`ms-playwright.playwright` ![](https://www.runoob.com/wp-content/uploads/2025/08/ba4b9e7d-c5cc-40b1-afbf-f7721d2495cd.png)
- **JavaScript / TypeScript 支持**（VS Code 自带，通常不用额外装）
- 推荐（可选）： - **ESLint**（保证代码风格一致） - **Prettier - Code formatter**（一键格式化代码）


---


## 3. 初始化 Playwright 项目


如果还没初始化过项目，先执行：


```
npm init playwright@lates
```


VS Code 插件会自动识别项目里的 **playwright.config.ts/js**，并启用测试视图。


---


## 4. VS Code 设置


打开 VS Code 设置（快捷键 `Ctrl+,` 或 `Cmd+,`），确认以下配置：


- **保存时自动格式化** 搜索 `format on save` → 勾选 `Editor: Format On Save`
- **终端默认 shell**（根据自己系统选择） Windows 推荐 `PowerShell` 或 `Git Bash` macOS/Linux 默认即可


---


## 5. 调试配置（launch.json）


在 VS Code 左侧点击 **运行与调试** → 创建配置，选择 **Node.js**，生成 `.vscode/launch.json`，添加 Playwright 调试配置，例如：


```
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Playwright Test",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/node_modules/.bin/playwright",
      "args": ["test", "--project=chromium", "--headed"],
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen"
    }
  ]
}
```


这样就可以在 VS Code 里按 `F5` 启动调试，Playwright 会跑在有界面模式，方便观察。


---


## 6. 使用 Playwright 插件面板


安装好 **Playwright Test for VSCode** 插件后，左侧会出现一个"Playwright"图标：


- 可以直接看到项目里的测试文件和用例列表
- 点击某个用例右侧的 ▶ 按钮就能运行
- 右键选择 **Debug Test** 可以单步调试
- 运行失败的测试可以直接查看 **trace 文件**


---


## 7. 常用命令


在 VS Code 的终端运行：


```
npx playwright test           # 运行全部测试
npx playwright test login.spec.js # 运行指定文件
npx playwright codegen        # 启动录制工具（自动生成脚本）
npx playwright show-report    # 打开测试报告
```










	  AI 思考中...





			** [Playwright 安装](https://www.runoob.com/playwright-install.html)
			[Playwright 第一个脚本](https://www.runoob.com/playwright-first-script.html) **













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