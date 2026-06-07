# Codex GitHub 集成

- Source: https://www.runoob.com/codex/codex-github.html

Codex 与 GitHub 深度集成，可以在拉取请求中直接进行代码审查。本节详细介绍如何配置和使用 GitHub 集成。


---


## 功能概述


通过 GitHub 集成，你可以：


![](https://www.runoob.com/wp-content/uploads/2026/04/app-git.webp)


- 在 PR 评论中直接请求 Codex 审查
- 自动审查每个拉取请求
- 让 Codex 修复 CI 失败问题
- 查看代码变更并提供建议


**无需离开 GitHub，Codex 就会像队友一样回复审查意见。


---


## 设置 GitHub 集成


### 前提条件


- Codex Cloud 订阅
- GitHub 账号


### 配置步骤


- 设置 [Codex Cloud](https://platform.openai.com/codex/cloud)
- 前往 [Codex 设置](https://chatgpt.com/codex/settings/code-review)
- 为仓库开启 **Code review** 功能
- 授权 Codex 访问你的仓库


> 你需要授予 Codex 读取仓库和创建拉取请求的权限。


---


## 请求代码审查


### 手动触发审查


在拉取请求评论中提及 `@codex review`：


## 请求审查


```
# 在 PR 评论中输入
@codex review

# 或者指定审查重点
@codex review for security regressions
```


### Codex 响应


Codex 会：


- 对 PR 做出反应（👀）
- 分析代码变更
- 发布审查意见
- 标记发现的问题（P0 和 P1）


> Codex 会像人类审查者一样在 PR 上发布审查意见。


### 自动审查


在设置中开启 Automatic reviews**：


- 前往 [Codex 设置](https://chatgpt.com/codex/settings/code-review)
- 开启 **Automatic reviews**
- 新 PR 打开时自动发布审查


---


## 自定义审查内容


### 设置仓库审查指南


在仓库的 `AGENTS.md` 中添加审查指南：


## 添加审查指南


```
## Review guidelines

- Don't log PII (个人身份信息)
- Verify that authentication middleware wraps every route
- Check for SQL injection vulnerabilities
- Ensure error messages don't leak sensitive information
```


### 模块特定规则


在子目录放置更具体的审查规则：


## 模块特定规则


```
# src/payment/ 模块审查规则

## Payment-specific reviews
- Verify payment processing follows PCI compliance
- Check for proper amount validation
- Ensure transaction logging
```


**更具体的规则会自动应用于对应模块的代码变更。


### 一次性审查重点


在评论中指定审查重点：


## 指定审查重点


```
# 评论示例
@codex review for security issues
@codex review for performance regressions
@codex review for documentation completeness
```


---


## 给 Codex 其他任务


在评论中提及 `@codex`（不是 review）会启动云任务：


## 其他任务


```
# 修复 CI 失败
@codex fix the CI failures

# 添加测试
@codex add tests for the new API endpoints

# 重构代码
@codex refactor this function to use async/await
```


> 使用 Codex 的其他功能就像在评论中 @ 它一样简单。


---


### GitHub Actions 集成


你也可以在 GitHub Actions 中使用 Codex：


## GitHub Actions 工作流


```
span style="color: green;">
name: Codex Review

on: [pull_request]

jobs:
  codex-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Codex Review
        run: |
          codex exec "Review code changes in this PR" --output review.md

      - name: Post Review
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = fs.readFileSync('review.md', 'utf8');
            github.rest.pulls.createReview({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number,
              body: review,
              event: 'COMMENT'
            });
```


> 将 Codex 集成到 CI/CD 流程中可以自动化代码审查。


---


## 最佳实践


### 审查指南


- 在 AGENTS.md 中明确定义审查标准
- 为不同模块设置特定规则
- 指定问题优先级（P0/P1）


### 自动化


- 为常规 PR 开启自动审查
- 对于大型变更使用手动触发
- 结合自动化工作流使用


> 好的配置可以让 Codex 的审查更加精准和高效。


---


## 常见问题


### Q: Codex 审查需要付费吗？


GitHub 集成需要 Codex Cloud 订阅。


### Q: Codex 能访问私有仓库吗？


需要授权 Codex 访问你的私有仓库。


### Q: 可以限制 Codex 审查的仓库吗？


是的，可以在设置中选择性授权仓库。


### Q: Codex 标记哪些级别的问题？


默认标记 P0（严重）和 P1（重要）问题。








	  AI 思考中...





			** [Codex AGENTS.md](https://www.runoob.com/codex-agents-md.html)
			[Codex Windows 原生支持](https://www.runoob.com/codex-windows.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#afcecbc2c6c1efdddac1c0c0cd81ccc0c2)

      : · [免责声明](https://www.runoob.com/disclaimer)

      : · [关于我们](https://www.runoob.com/aboutus)

      : · [文章归档](https://www.runoob.com/archives)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/)**
    **[runoob.com](https://www.runoob.com/)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **