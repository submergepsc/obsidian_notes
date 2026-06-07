# OpenCode GitHub

- Source: https://www.runoob.com/opencode/opencode-github.html

OpenCode 可以深度集成 GitHub 工作流，让 AI 直接参与 Issue、Pull Request 和代码审查流程。


**通过在评论中输入 /opencode 或 /oc，即可触发 AI 自动执行任务。**


**OpenCode GitHub = 把 AI 变成你的自动化开发成员，直接参与 Issue、PR 和代码流程。**


---


## 一、核心能力


- **Issue 分析：**自动理解问题并给出解释
- **自动修复：**创建分支并提交 PR
- **代码审查：**分析 PR 并提出改进建议
- **自动化执行：**基于 GitHub Actions 运行


**特点：**


- 运行在你自己的 GitHub Runner 中
- 安全可控，不依赖外部服务器执行代码


---


## 二、快速安装（推荐）


在 GitHub 项目根目录运行：


```
opencode github install
```


该命令会自动完成：


- 安装 GitHub App
- 创建 GitHub Actions 工作流
- 引导配置 API Key


---


## 三、手动安装（进阶）


### 1、安装 GitHub App


访问：


```
https://github.com/apps/opencode-agent
```


安装到你的仓库


---


### 2、添加工作流文件


创建文件：


```
.github/workflows/opencode.yml
```


示例：


```
name: opencode

on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]

jobs:
  opencode:
    if: |
      contains(github.event.comment.body, '/oc') ||
      contains(github.event.comment.body, '/opencode')
    runs-on: ubuntu-latest
    permissions:
      id-token: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@v6
        with:
          fetch-depth: 1
          persist-credentials: false

      - name: Run OpenCode
        uses: anomalyco/opencode/github@latest
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        with:
          model: anthropic/claude-sonnet-4-20250514
```


---


### 3、配置 Secrets


在 GitHub 仓库中：


- 进入 Settings → Secrets → Actions
- 添加 API Key（如 ANTHROPIC_API_KEY）


---


## 四、配置参数说明


| 参数 | 说明 |
| --- | --- |
| model | 使用的模型（必填） |
| agent | 指定代理 |
| prompt | 自定义提示词 |
| share | 是否分享会话 |
| token | GitHub Token |


**说明：**


- 默认使用 OpenCode GitHub App 的 Token
- 也可以使用 GITHUB_TOKEN 或 PAT


---


## 五、支持的触发事件


| 事件 | 说明 |
| --- | --- |
| issue_comment | 评论触发 /opencode |
| pull_request_review_comment | 代码行评论触发 |
| issues | Issue 创建/更新 |
| pull_request | PR 自动审查 |
| schedule | 定时任务 |
| workflow_dispatch | 手动触发 |


---


## 六、常见使用方式


### 1、解释 Issue


在 Issue 评论：


```
/opencode explain this issue
```


AI 会总结问题并解释


---


### 2、自动修复 Issue


```
/opencode fix this
```


自动：


- 创建分支
- 修改代码
- 提交 Pull Request


---


### 3、修改 PR


```
Delete the attachment from S3 when the note is removed /oc
```


直接在 PR 上执行修改


---


### 4、代码行级操作（非常强）


在 PR 的 Files 页面评论：


```
/oc add error handling here
```


OpenCode 会自动获取：


- 文件路径
- 行号
- 上下文 diff


无需手动说明位置


---


## 七、定时任务（自动化）


示例：每周扫描 TODO


```
on:
  schedule:
    - cron: "0 9 * * 1"
```


示例 prompt：


```
Review the codebase for TODO comments and summarize them
```


**注意：**


- 定时任务必须提供 prompt
- 需要写权限（contents / pull-requests）


---


## 八、PR 自动审查


示例：


```
on:
  pull_request:
    types: [opened, synchronize]
```


默认行为：


- 分析代码质量
- 检测潜在 Bug
- 提出改进建议


---


## 九、Issue 自动分类


可以自动处理新 Issue，例如：


- 过滤垃圾账号
- 自动回复建议
- 补充文档说明


**注意：**


- issues 事件必须提供 prompt


---


## 十、自定义提示词（高级用法）


可以覆盖默认行为：


```
prompt: |
  Review this pull request:
  - Check for bugs
  - Suggest improvements
```


用于：


- 统一代码规范
- 定制审查标准
- 自动化团队流程


---


## 十一、安全与权限


推荐权限配置：


```
permissions:
  id-token: write
  contents: write
  pull-requests: write
  issues: write
```


**说明：**


- 最小权限原则
- 仅开放必要能力









	  AI 思考中...





			** [OpenCode Web 使用](https://www.runoob.com/opencode-web.html)
			[OpenCode GitLab](https://www.runoob.com/opencode-gitlab.html) **













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