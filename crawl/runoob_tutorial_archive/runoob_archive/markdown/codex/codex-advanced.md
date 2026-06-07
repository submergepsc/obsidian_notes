# Codex 进阶使用技巧

- Source: https://www.runoob.com/codex/codex-advanced.html

### AGENTS.md - 项目级配置


在项目根目录创建 `AGENTS.md` 文件，可以为 Codex 提供项目特定的上下文和规则，Codex 启动时会自动读取：


```
# AGENTS.md（放在项目根目录）

## 项目概述
这是一个基于 Next.js 14 + Prisma + PostgreSQL 的 SaaS 应用。
使用 App Router，不使用 Pages Router。

## 技术栈
- 前端：Next.js 14, React 18, TailwindCSS, shadcn/ui
- 后端：Next.js API Routes, Prisma ORM
- 数据库：PostgreSQL 15
- 认证：NextAuth.js

## 重要约定
- 所有数据库操作必须通过 lib/db.ts 中的 prisma 实例
- API 路由错误统一用 lib/api-error.ts 处理
- 环境变量在 .env.local 中，参考 .env.example

## 禁止事项
- 不要修改 prisma/schema.prisma，除非我明确要求
- 不要删除任何现有测试
- 生产环境的 .env 文件不要碰
```


### 会话管理


对于需要长期维护的大型任务，Codex CLI 支持会话的导出和恢复：


```
# 在交互界面中随时导出当前会话
/export session-2024-01-15.json

# 第二天继续工作时，恢复会话上下文
/load session-2024-01-15.json

# 或在启动时直接恢复上次会话
codex resume --last

# 查看所有保存的会话
ls ~/.codex/sessions/
```


### 与 VS Code 集成


Codex 官方提供了 VS Code 扩展插件，可以在 IDE 中直接使用 Codex 的功能：


- 打开 VS Code，进入扩展市场（`Cmd/Ctrl + Shift + X`）
- 搜索「Codex」或「OpenAI Codex」，安装官方插件
- 首次使用需要登录 ChatGPT 账号
- 在侧边栏中找到 Codex 图标，即可开始对话


```
VS Code 插件快捷键：
Alt + G          → 将选中的代码发送到 Codex CLI
Cmd + Shift + P  → 打开命令面板，输入 Codex 查看所有命令
```


**

💡 未订阅 ChatGPT 的用户**：可以先按前面步骤配置好 CLI 的 API Key，再用免费账号登录 VS Code 插件，这样插件会复用 CLI 的模型配置（BYO 模式）。


### CI/CD 集成（GitHub Actions）


Codex CLI 可以在 CI/CD 流水线中以无头模式运行：


```
# .github/workflows/codex-changelog.yml

name: Auto Update Changelog
on:
  push:
    branches: [main]

jobs:
  update-changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '22'

      - name: Install Codex CLI
        run: npm install -g @openai/codex

      - name: Run Codex Task
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          CODEX_QUIET_MODE: 1
        run: |
          codex exec --full-auto "根据最新 commits 更新 CHANGELOG.md"

      - name: Commit changes
        run: |
          git config --local user.email '[email protected]'
          git add CHANGELOG.md
          git commit -m 'chore: update changelog [skip ci]'
          git push
```


### 实用提示词技巧


写出好的提示词是高效使用 Codex 的关键，以下是一些经过验证的技巧：


#### 技巧一：提供足够的上下文


```
# 模糊的提示
"修复 bug"

# 详细的提示
"用户登录时报错 TypeError: Cannot read properties of null，
报错发生在 src/auth/login.ts 第 42 行，
这个函数负责验证 JWT token，帮我找出并修复这个问题"
```


#### 技巧二：分步骤执行复杂任务


```
# 第一步：先让 Codex 分析，不要它直接改
"分析 src/api/ 目录的代码质量，列出主要问题，不要修改任何文件"

# 第二步：确认方案后再执行
"好，按你说的方案，先修复错误处理问题，然后我来 review"
```


#### 技巧三：利用 ask 模式探索


```
# 用 ask 模式（只读）先了解代码库
codex -a ask "这个项目是如何处理用户认证的？梳理完整的认证流程"

# 了解清楚后，再切换到 auto-edit 进行修改
/approvals  # 切换到 auto-edit 模式
```


#### 技巧四：善用否定指令


```
# 明确告诉 Codex 不要做什么，避免不必要的修改
"重构 utils/date.ts 中的日期格式化函数，不要修改函数签名，不要改变测试文件"
```


#### 技巧五：让 Codex 先汇报再执行


```
# 先让它列计划
"你打算怎么实现这个功能？先列出步骤，不要执行"

# 确认后再开始
"计划不错，开始执行第一步"
```









	  AI 思考中...





			** [Codex 速查表](https://www.runoob.com/codex-commands.html)
			[Codex 核心概念](https://www.runoob.com/codex-concepts.html) **













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

      : · [意见反馈](https://www.runoob.com/cdn-cgi/l/email-protection#e382878e8a8da391968d8c8c81cd808c8e)

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