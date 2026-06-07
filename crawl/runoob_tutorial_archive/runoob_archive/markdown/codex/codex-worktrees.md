# Codex Worktrees 使用

- Source: https://www.runoob.com/codex/codex-worktrees.html

Worktrees 允许你在 Git 仓库中创建多个工作目录，使你能够并行处理不同的任务而不会相互干扰。


---


## 什么是 Worktree？


Git Worktree 是 Git 的一个功能，允许你在同一个仓库中创建多个工作目录。Codex 对 Worktree 提供了原生支持。


### 使用场景


- 并行开发多个功能
- 保持主分支干净
- 同时进行开发和代码审查


![](https://www.runoob.com/wp-content/uploads/2026/04/app-worktree.webp)

**Worktree 让你可以像有多台电脑一样同时工作。


---


## 在 Codex 中使用 Worktree


### 创建 Worktree


## 创建 Worktree


```
# 在 Codex 应用中创建 Worktree
# 1. 选择项目
# 2. 点击 "New" -> "Worktree"
# 3. 输入分支名称
# 4. 点击创建
```


### 在 Worktree 中运行任务


在创建线程时选择 Worktree 模式：


| 模式 | 说明 |
| --- | --- |
| Local | 在当前项目目录工作 |
| Worktree | 在独立的 Git worktree 中工作 |


> Worktree 模式创建新的 Git worktree，保持变更隔离。


---


### Worktree 管理


## 管理 Worktree


```
# 查看 worktree 列表
git worktree list

# 创建新的 worktree
git worktree add ../feature-branch -b feature-branch

# 删除 worktree
git worktree remove ../feature-branch
```


---


## 最佳实践


- 为每个功能或修复创建独立的 Worktree
- 使用描述性的分支名称
- 完成后及时清理不需要的 Worktree


> Worktree 是并行开发的利器，特别适合大型项目。








	  AI 思考中...





			** [Codex Windows 原生支持](https://www.runoob.com/codex-windows.html)














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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#ee8f8a838780ae9c9b8081818cc08d8183)

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